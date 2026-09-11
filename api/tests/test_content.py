"""
Content validity is a test, not a hope (learn_togaf.md §8): every file under content/ loads
through the same validators the app uses, and the shape rules hold for every question.
"""

from pathlib import Path

from learn_togaf.config import CONTENT_DIR
from learn_togaf.content.loader import (
    load_adm,
    load_blueprint,
    load_glossary,
    load_lessons,
    load_question_sets,
)


def test_blueprint_loads_and_weights_sum_to_forty() -> None:
    blueprint = load_blueprint(CONTENT_DIR)
    assert blueprint.foundation.questions == 40
    assert blueprint.foundation.pass_mark == 24
    assert blueprint.practitioner.pass_mark == 24
    assert sum(unit.weight for unit in blueprint.units if unit.exam == "FOUNDATION") == 40


def test_every_lesson_loads_and_cites_a_section() -> None:
    blueprint = load_blueprint(CONTENT_DIR)
    lessons = load_lessons(CONTENT_DIR, blueprint)
    assert lessons, "no lessons under content/lessons"
    for lesson in lessons:
        assert lesson.front.refs, f"{lesson.id} has no refs"


def test_glossary_and_adm_load() -> None:
    blueprint = load_blueprint(CONTENT_DIR)
    assert load_glossary(CONTENT_DIR, blueprint)
    phases, techniques, artefacts = load_adm(CONTENT_DIR)
    assert {phase.code for phase in phases} == {"PRELIM", "A", "B", "C", "D", "E", "F", "G", "H", "REQ"}
    assert techniques and artefacts


def test_every_question_set_loads_with_the_exam_shape() -> None:
    blueprint = load_blueprint(CONTENT_DIR)
    sets = load_question_sets(CONTENT_DIR, blueprint)
    assert sets
    for question_set in sets:
        for question in question_set.foundation:
            assert sum(option.correct for option in question.options) == 1
            assert question.explanation.strip()
            assert question.refs
        for question in question_set.practitioner:
            assert sorted(answer.points for answer in question.answers) == [0, 1, 3, 5]
            assert all(answer.why.strip() for answer in question.answers)
            assert question.refs


def test_review_directory_is_not_loaded_as_content() -> None:
    review = CONTENT_DIR / "review"
    assert review.is_dir()
    assert not list(Path(CONTENT_DIR / "questions").glob("review/*"))
