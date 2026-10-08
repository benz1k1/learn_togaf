"""
Content validity is a test, not a hope (learn_togaf.md §8): every file under content/ loads
through the same validators the app uses, and the shape rules hold for every question. With
exams as data (learn_sabsa_archimate.md §4.1) the blueprint's five exams, the curriculum's
completeness and the crosswalk are gated here too.
"""

from pathlib import Path

from learn_togaf.config import CONTENT_DIR
from learn_togaf.content.loader import (
    assign_lessons,
    lesson_keys_of,
    load_adm,
    load_blueprint,
    load_curriculum,
    load_examples,
    load_glossary,
    load_lessons,
    load_question_sets,
    unplaced_lessons,
)
from learn_togaf.db import connect
from learn_togaf.sources.index import resolve_ref

EXAMS = {"OGEA-101", "OGEA-102", "OGA-031", "OGA-032", "SCF"}


def test_blueprint_has_five_exams_and_the_single_answer_weights_sum() -> None:
    blueprint = load_blueprint(CONTENT_DIR)
    assert set(blueprint.exams) == EXAMS
    assert blueprint.exam("OGEA-101").questions == 40 and blueprint.exam("OGEA-101").pass_mark == 24
    assert blueprint.exam("OGEA-102").scoring == "gradient" and blueprint.exam("OGEA-102").open_book
    assert blueprint.exam("OGA-032").scoring == "gradient" and blueprint.exam("OGA-032").track == "ARCHIMATE"
    assert blueprint.exam("SCF").track == "SABSA" and blueprint.exam("SCF").max_score == 48
    for exam in blueprint.exams.values():
        if exam.scoring != "single":
            continue
        weighted = [unit for unit in blueprint.units if unit.exam == exam.code]
        assert sum(unit.weight for unit in weighted) == exam.questions, exam.code
    tracks = {unit.track for unit in blueprint.units}
    assert tracks == {"TOGAF", "ARCHIMATE", "SABSA", "CROSSWALK"}
    for unit in blueprint.units:
        if unit.track == "CROSSWALK":
            assert unit.exam is None and unit.weight == 0, unit.code
        else:
            assert unit.exam in EXAMS and blueprint.exam(unit.exam).track == unit.track, unit.code


def test_every_lesson_loads_and_cites_a_section() -> None:
    blueprint = load_blueprint(CONTENT_DIR)
    lessons = load_lessons(CONTENT_DIR, blueprint)
    assert lessons, "no lessons under content/lessons"
    for lesson in lessons:
        assert lesson.front.refs, f"{lesson.id} has no refs"


def test_curriculum_places_every_lesson_exactly_once() -> None:
    """The braid is the study order, so a lesson it does not place would never be scheduled."""
    blueprint = load_blueprint(CONTENT_DIR)
    lessons = load_lessons(CONTENT_DIR, blueprint)
    curriculum = load_curriculum(CONTENT_DIR, lessons)
    assert [week.week for week in curriculum.weeks] == list(range(1, 17))
    assert not unplaced_lessons(lessons, curriculum), unplaced_lessons(lessons, curriculum)
    assert len(curriculum.ordered_ids()) == len(lessons)


def test_glossary_and_adm_load() -> None:
    blueprint = load_blueprint(CONTENT_DIR)
    assert load_glossary(CONTENT_DIR, blueprint)
    lessons = load_lessons(CONTENT_DIR, blueprint)
    phases, techniques, artefacts = load_adm(CONTENT_DIR, {lesson.id for lesson in lessons})
    assert {phase.code for phase in phases} == {"PRELIM", "A", "B", "C", "D", "E", "F", "G", "H", "REQ"}
    assert techniques and artefacts


def test_every_question_set_loads_with_the_exam_shape() -> None:
    blueprint = load_blueprint(CONTENT_DIR)
    sets = load_question_sets(CONTENT_DIR, blueprint)
    assert sets
    for question_set in sets:
        assert question_set.exam in EXAMS
        assert question_set.scoring == blueprint.exam(question_set.exam).scoring
        for question in question_set.single:
            assert sum(option.correct for option in question.options) == 1
            assert question.explanation.strip()
            assert question.refs
        for question in question_set.gradient:
            assert sorted(answer.points for answer in question.answers) == [0, 1, 3, 5]
            assert all(answer.why.strip() for answer in question.answers)
            assert question.refs


def test_question_set_directories_are_exam_codes() -> None:
    for sub in (CONTENT_DIR / "questions").iterdir():
        if sub.is_dir():
            assert sub.name in EXAMS | {"figures", "imported"}, sub


def test_every_question_belongs_to_exactly_one_lesson() -> None:
    """Check-yourself draws from the question → lesson mapping, so a question two lessons claim
    equally would be shown by both, and one no lesson claims would never be shown. The fix is
    always `lesson:` on the question, never a tie-break in code."""
    blueprint = load_blueprint(CONTENT_DIR)
    keys = lesson_keys_of(load_lessons(CONTENT_DIR, blueprint))
    units_with_lessons = {key.unit for key in keys}
    for question_set in load_question_sets(CONTENT_DIR, blueprint):
        questions = question_set.questions()
        mapping, warnings = assign_lessons(keys, questions, CONTENT_DIR / question_set.code)
        assert not warnings, "\n".join(warnings)
        unmapped = [q.id for q in questions if q.unit in units_with_lessons and q.id not in mapping]
        assert not unmapped, f"{question_set.code}: no lesson for {unmapped}"


def test_review_directory_is_not_loaded_as_content() -> None:
    review = CONTENT_DIR / "review"
    assert review.is_dir()
    assert not list(Path(CONTENT_DIR / "questions").glob("review/*"))


def test_worked_examples_cover_every_deliverable_and_every_ref_resolves() -> None:
    """The Worked examples page exists because the lessons never show a filled-in deliverable; every
    deliverable in the Content Framework's table must have one, and each must cite a real section."""
    examples = load_examples(CONTENT_DIR)
    assert examples, "no worked examples under content/examples"
    covered = " ".join(example.front.deliverable.lower() for example in examples)
    for deliverable in (
        "architecture building blocks",
        "architecture contract",
        "architecture definition document",
        "architecture principles",
        "architecture repository",
        "architecture requirements specification",
        "architecture roadmap",
        "architecture vision",
        "business principles, business goals, and business drivers",
        "capability assessment",
        "change request",
        "communications plan",
        "compliance assessment",
        "implementation and migration plan",
        "implementation governance model",
        "organizational model for enterprise architecture",
        "request for architecture work",
        "requirements impact assessment",
        "solution building blocks",
        "statement of architecture work",
        "tailored architecture framework",
        "business scenario",
        "maturity assessment",
    ):
        assert deliverable in covered, f"no worked example for {deliverable}"
    assert {example.front.phase for example in examples} == {
        "PRELIM",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "REQ",
    }
    connection = connect()
    indexed = {row["code"] for row in connection.execute("SELECT code FROM source_document")}
    for example in examples:
        for ref in example.front.refs:
            document = ref.split(" §")[0]
            if document.split(":")[0] not in {"ARCHIMATE", "WP", "SABSA"} or document in indexed:
                assert resolve_ref(connection, ref), f"{example.id}: ref {ref!r} does not resolve"
