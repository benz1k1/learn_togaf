"""
Load ``content/`` into the cache tables (learn_togaf.md §2, §5).

Content is files, not rows: the database is a cache of the files plus the learner's state.
``load_all`` rebuilds every cache table from disk inside one transaction, so a file that fails
validation leaves the previous load in place and the failure names the file and the id. Learner
state tables are never touched. Drafts under ``content/review/`` are not loaded here; the
review-queue page reads them off disk.
"""

import re
import sqlite3
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, TypeVar

import orjson
import yaml
from loguru import logger
from pydantic import BaseModel, ValidationError

from learn_togaf.content.models import (
    AdmArtefact,
    AdmPhase,
    AdmTechnique,
    Blueprint,
    Crosswalk,
    CurriculumWeek,
    ExampleDocument,
    ExampleFrontMatter,
    GlossaryTerm,
    ImportantFigure,
    Lesson,
    LessonFrontMatter,
    Question,
    QuestionSetFile,
)
from learn_togaf.db import transaction

ModelT = TypeVar("ModelT", bound=BaseModel)

_FRONT_MATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", re.DOTALL)
_LESSON_FILE_RE = re.compile(r"^(?P<nn>\d{2})_(?P<slug>[a-z0-9_\-]+)\.md$")
_EXAMPLE_FILE_RE = _LESSON_FILE_RE


class ContentError(ValueError):
    """A content file failed validation. The message names the file and, where known, the id."""


@dataclass
class LoadReport:
    units: int = 0
    objectives: int = 0
    lessons: int = 0
    terms: int = 0
    phases: int = 0
    techniques: int = 0
    artefacts: int = 0
    examples: int = 0
    crosswalks: int = 0
    weeks: int = 0
    sets: int = 0
    questions: int = 0
    warnings: list[str] = field(default_factory=list)

    def summary(self) -> str:
        return (
            f"units={self.units} objectives={self.objectives} lessons={self.lessons} terms={self.terms} "
            f"phases={self.phases} techniques={self.techniques} artefacts={self.artefacts} examples={self.examples} "
            f"crosswalks={self.crosswalks} weeks={self.weeks} sets={self.sets} questions={self.questions} "
            f"warnings={len(self.warnings)}"
        )


def _json(value: Any) -> str:
    return orjson.dumps(value).decode()


def _read_yaml(path: Path) -> Any:
    try:
        with open(path, encoding="utf-8") as handle:
            return yaml.safe_load(handle)
    except yaml.YAMLError as exc:
        raise ContentError(f"{path}: invalid YAML: {exc}") from exc


def split_front_matter(text: str, path: Path) -> tuple[dict[str, Any], str]:
    match = _FRONT_MATTER_RE.match(text)
    if not match:
        raise ContentError(f"{path}: missing YAML front matter (--- ... ---)")
    try:
        front = yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError as exc:
        raise ContentError(f"{path}: invalid front matter: {exc}") from exc
    if not isinstance(front, dict):
        raise ContentError(f"{path}: front matter must be a mapping")
    return front, match.group(2)


def load_blueprint(content_dir: Path) -> Blueprint:
    path = content_dir / "blueprint.yaml"
    if not path.is_file():
        raise ContentError(f"{path} is missing")
    try:
        return Blueprint.model_validate(_read_yaml(path))
    except ValidationError as exc:
        raise ContentError(f"{path}: {exc}") from exc


def _load_units(content_dir: Path, blueprint: Blueprint) -> dict[str, str]:
    """Unit summary Markdown by unit code, from units/<code>_*.md (optional per unit)."""
    summaries: dict[str, str] = {}
    units_dir = content_dir / "units"
    if not units_dir.is_dir():
        return summaries
    for path in sorted(units_dir.glob("*.md")):
        code = path.stem.split("_", 1)[0]
        if code not in blueprint.unit_codes():
            raise ContentError(f"{path}: unit code {code!r} is not in blueprint.yaml")
        front, body = split_front_matter(path.read_text(encoding="utf-8"), path)
        summaries[code] = body.strip()
    return summaries


def load_lessons(content_dir: Path, blueprint: Blueprint) -> list[Lesson]:
    lessons: list[Lesson] = []
    lessons_dir = content_dir / "lessons"
    if not lessons_dir.is_dir():
        return lessons
    objective_unit = blueprint.objective_unit()
    for unit_dir in sorted(path for path in lessons_dir.iterdir() if path.is_dir()):
        unit_code = unit_dir.name
        if unit_code not in blueprint.unit_codes():
            raise ContentError(f"{unit_dir}: unit {unit_code!r} is not in blueprint.yaml")
        for path in sorted(unit_dir.glob("*.md")):
            match = _LESSON_FILE_RE.match(path.name)
            if not match:
                raise ContentError(f"{path}: lesson files are named <nn>_<slug>.md")
            front_raw, body = split_front_matter(path.read_text(encoding="utf-8"), path)
            front_raw.setdefault("unit", unit_code)
            try:
                front = LessonFrontMatter.model_validate(front_raw)
            except ValidationError as exc:
                raise ContentError(f"{path}: {exc}") from exc
            if front.unit != unit_code:
                raise ContentError(
                    f"{path}: front matter unit {front.unit!r} does not match directory {unit_code!r}"
                )
            for objective in front.objectives:
                if objective_unit.get(objective) != unit_code:
                    raise ContentError(
                        f"{path}: objective {objective!r} is not an objective of unit {unit_code}"
                    )
            if not body.strip():
                raise ContentError(f"{path}: empty lesson body")
            lessons.append(
                Lesson(
                    id=f"{unit_code}/{match.group('nn')}_{match.group('slug')}",
                    unit=unit_code,
                    slug=match.group("slug"),
                    ordinal=int(match.group("nn")),
                    front=front,
                    body_md=body.strip(),
                )
            )
    return lessons


def load_examples(content_dir: Path) -> list[ExampleDocument]:
    """Worked example documents under examples/<nn>_<slug>.md — one fictional enterprise, every deliverable."""
    examples: list[ExampleDocument] = []
    examples_dir = content_dir / "examples"
    if not examples_dir.is_dir():
        return examples
    for path in sorted(examples_dir.glob("*.md")):
        match = _EXAMPLE_FILE_RE.match(path.name)
        if not match:
            raise ContentError(f"{path}: example files are named <nn>_<slug>.md")
        front_raw, body = split_front_matter(path.read_text(encoding="utf-8"), path)
        try:
            front = ExampleFrontMatter.model_validate(front_raw)
        except ValidationError as exc:
            raise ContentError(f"{path}: {exc}") from exc
        if not body.strip():
            raise ContentError(f"{path}: empty example body")
        examples.append(
            ExampleDocument(
                id=f"{match.group('nn')}_{match.group('slug')}",
                ordinal=int(match.group("nn")),
                front=front,
                body_md=body.strip(),
            )
        )
    return examples


def load_glossary(content_dir: Path, blueprint: Blueprint) -> list[GlossaryTerm]:
    path = content_dir / "glossary.yaml"
    if not path.is_file():
        return []
    raw = _read_yaml(path) or []
    if not isinstance(raw, list):
        raise ContentError(f"{path}: expected a list of terms")
    terms: list[GlossaryTerm] = []
    for item in raw:
        try:
            term = GlossaryTerm.model_validate(item)
        except ValidationError as exc:
            raise ContentError(
                f"{path}: term {item.get('id') if isinstance(item, dict) else item!r}: {exc}"
            ) from exc
        for objective in term.objectives:
            if objective not in blueprint.objective_codes():
                raise ContentError(
                    f"{path}: term {term.id}: objective {objective!r} is not in blueprint.yaml"
                )
        terms.append(term)
    ids = {term.id for term in terms}
    for term in terms:
        for other in term.confusable_with:
            if other not in ids:
                raise ContentError(f"{path}: term {term.id}: confusable_with {other!r} is not a term id")
    return terms


def _load_list(path: Path, model: type[ModelT], label: str) -> list[ModelT]:
    if not path.is_file():
        return []
    raw = _read_yaml(path) or []
    if not isinstance(raw, list):
        raise ContentError(f"{path}: expected a list of {label}")
    items: list[ModelT] = []
    for item in raw:
        try:
            items.append(model.model_validate(item))
        except ValidationError as exc:
            code = item.get("code") if isinstance(item, dict) else item
            raise ContentError(f"{path}: {label} {code!r}: {exc}") from exc
    return items


def load_adm(
    content_dir: Path, lesson_ids: set[str] | None = None
) -> tuple[list[AdmPhase], list[AdmTechnique], list[AdmArtefact]]:
    """phases.yaml, techniques.yaml, artefacts.yaml and, when present, crosswalk.yaml (one entry
    per phase, attached to the phase). ``lesson_ids`` lets the crosswalk's lesson links be
    checked; pass None to skip that check (callers that have not loaded lessons)."""
    adm_dir = content_dir / "adm"
    phases = _load_list(adm_dir / "phases.yaml", AdmPhase, "phase")
    techniques = _load_list(adm_dir / "techniques.yaml", AdmTechnique, "technique")
    artefacts = _load_list(adm_dir / "artefacts.yaml", AdmArtefact, "artefact")
    crosswalks = _load_list(adm_dir / "crosswalk.yaml", Crosswalk, "crosswalk")
    phase_codes = {phase.code for phase in phases}
    artefact_codes = {artefact.code for artefact in artefacts}
    by_phase = {phase.code: phase for phase in phases}
    for crosswalk in crosswalks:
        if crosswalk.phase not in phase_codes:
            raise ContentError(f"adm/crosswalk.yaml: phase {crosswalk.phase!r} is not in phases.yaml")
        if by_phase[crosswalk.phase].crosswalk is not None:
            raise ContentError(f"adm/crosswalk.yaml: phase {crosswalk.phase} appears twice")
        for lesson_id in [*crosswalk.archimate.lessons, *crosswalk.sabsa.lessons]:
            if lesson_ids is not None and lesson_id not in lesson_ids:
                raise ContentError(
                    f"adm/crosswalk.yaml: phase {crosswalk.phase}: lesson {lesson_id!r} does not exist"
                )
        by_phase[crosswalk.phase].crosswalk = crosswalk
    for phase in phases:
        for code in phase.artefacts:
            if code not in artefact_codes:
                raise ContentError(
                    f"adm/phases.yaml: phase {phase.code}: artefact {code!r} is not in artefacts.yaml"
                )
    for technique in techniques:
        for code in technique.phases:
            if code not in phase_codes:
                raise ContentError(
                    f"adm/techniques.yaml: {technique.code}: phase {code!r} is not in phases.yaml"
                )
    for artefact in artefacts:
        if artefact.phase not in phase_codes:
            raise ContentError(
                f"adm/artefacts.yaml: {artefact.code}: phase {artefact.phase!r} is not in phases.yaml"
            )
    return phases, techniques, artefacts


def parse_question_set(raw: Any, path: Path, blueprint: Blueprint) -> QuestionSetFile:
    """Validate one set (a file, or an import that was normalised into the file shape)."""
    if not isinstance(raw, dict):
        raise ContentError(f"{path}: a question set is a mapping with code/exam/name and a questions list")
    data = dict(raw)
    questions = data.pop("questions", [])
    exam_code = str(data.get("exam", "")).strip().upper()
    if exam_code not in blueprint.exams:
        raise ContentError(
            f"{path}: exam {exam_code!r} is not an exam code in blueprint.yaml ({', '.join(blueprint.exams)})"
        )
    exam = blueprint.exam(exam_code)
    data["exam"] = exam_code
    data["track"] = exam.track
    data["scoring"] = exam.scoring
    data.pop("foundation", None)
    data.pop("practitioner", None)
    data[exam.scoring] = questions
    try:
        question_set = QuestionSetFile.model_validate(data)
    except ValidationError as exc:
        raise ContentError(f"{path}: {exc}") from exc
    objective_unit = blueprint.objective_unit()
    for question in question_set.questions():
        if question.unit not in blueprint.unit_codes():
            raise ContentError(
                f"{path}: question {question.id}: unit {question.unit!r} is not in blueprint.yaml"
            )
        unit = blueprint.unit(question.unit)
        if unit.exam is None:
            raise ContentError(
                f"{path}: question {question.id}: unit {question.unit} has no exam; crosswalk units carry no questions"
            )
        # A unit serves every exam of its track (the A units carry OGA-031 items and OGA-032
        # scenarios alike); a question may not cross tracks.
        if unit.track != exam.track:
            raise ContentError(
                f"{path}: question {question.id}: unit {question.unit} is on the {unit.track} track, exam {exam_code} is {exam.track}"
            )
        if objective_unit.get(question.objective) != question.unit:
            raise ContentError(
                f"{path}: question {question.id}: objective {question.objective!r} is not an objective of unit {question.unit}"
            )
    return question_set


def load_question_sets(content_dir: Path, blueprint: Blueprint) -> list[QuestionSetFile]:
    sets: list[QuestionSetFile] = []
    questions_dir = content_dir / "questions"
    if not questions_dir.is_dir():
        return sets
    # One directory per exam code (questions/OGEA-101/, questions/OGA-032/, …) plus figures/ and
    # imported/; every *.yaml beneath questions/ is a set and says which exam it belongs to.
    for sub in sorted(path for path in questions_dir.iterdir() if path.is_dir()):
        for path in sorted(sub.glob("*.yaml")):
            sets.append(parse_question_set(_read_yaml(path), path, blueprint))
    codes = [question_set.code for question_set in sets]
    if len(codes) != len(set(codes)):
        raise ContentError(
            f"duplicate question set codes: {sorted({c for c in codes if codes.count(c) > 1})}"
        )
    ids = [q.id for s in sets for q in s.questions()]
    duplicates = sorted({i for i in ids if ids.count(i) > 1})
    if duplicates:
        raise ContentError(f"duplicate question ids across sets: {duplicates[:10]}")
    return sets


def load_important_figures(sources_dir: Path) -> list[ImportantFigure]:
    return _load_list(sources_dir / "figures" / "important.yaml", ImportantFigure, "figure")


# ---------------------------------------------------------------- curriculum.yaml (the braid)
@dataclass
class CurriculumOrder:
    weeks: list[CurriculumWeek]
    placement: dict[str, tuple[int, int]]  # lesson id → (week, position within the week)

    def ordered_ids(self) -> list[str]:
        return [lesson_id for lesson_id, _ in sorted(self.placement.items(), key=lambda item: item[1])]


def load_curriculum(content_dir: Path, lessons: list[Lesson]) -> CurriculumOrder:
    """``curriculum.yaml`` expanded to one position per lesson. Explicit ``lessons`` ids come
    first in each week, then every not-yet-placed lesson of the week's ``units`` in ordinal
    order. A lesson placed twice, an unknown id, or a lesson the file never places is an error:
    the curriculum is the study order, so it must be complete. No file → every lesson unplaced
    (the plan then falls back to blueprint order and ``tests/test_content.py`` fails)."""
    path = content_dir / "curriculum.yaml"
    weeks = _load_list(path, CurriculumWeek, "week")
    by_id = {lesson.id: lesson for lesson in lessons}
    placement: dict[str, tuple[int, int]] = {}
    numbers = [week.week for week in weeks]
    if len(numbers) != len(set(numbers)):
        raise ContentError(f"{path}: duplicate week numbers")
    ordered = sorted(weeks, key=lambda item: item.week)
    positions: dict[int, int] = {week.week: 0 for week in ordered}
    # Explicit ids first across every week, so a lesson named in week 10 is not swept up by a
    # ``units:`` entry for its unit in week 4.
    for week in ordered:
        for lesson_id in week.lessons:
            if lesson_id not in by_id:
                raise ContentError(f"{path}: week {week.week}: lesson {lesson_id!r} does not exist")
            if lesson_id in placement:
                raise ContentError(
                    f"{path}: week {week.week}: lesson {lesson_id} is already placed in week {placement[lesson_id][0]}"
                )
            placement[lesson_id] = (week.week, positions[week.week])
            positions[week.week] += 1
    for week in ordered:
        for unit_code in week.units:
            remaining = sorted(
                (lesson for lesson in lessons if lesson.unit == unit_code and lesson.id not in placement),
                key=lambda lesson: lesson.ordinal,
            )
            for lesson in remaining:
                placement[lesson.id] = (week.week, positions[week.week])
                positions[week.week] += 1
    return CurriculumOrder(weeks=sorted(weeks, key=lambda item: item.week), placement=placement)


def unplaced_lessons(lessons: list[Lesson], order: CurriculumOrder) -> list[str]:
    return sorted(lesson.id for lesson in lessons if lesson.id not in order.placement)


# ---------------------------------------------------------------- question → lesson
@dataclass(frozen=True)
class LessonKey:
    """What the assignment needs to know about a lesson, from the files or from the cache tables."""

    id: str
    unit: str
    objectives: frozenset[str]
    refs: tuple[str, ...]


def lesson_keys_of(lessons: list[Lesson]) -> list[LessonKey]:
    return [
        LessonKey(lesson.id, lesson.unit, frozenset(lesson.front.objectives), tuple(lesson.front.refs))
        for lesson in lessons
    ]


def lesson_keys(connection: sqlite3.Connection) -> list[LessonKey]:
    """The same keys read back from the cache, for callers that insert after a load (the importer)."""
    objectives: dict[str, set[str]] = {}
    for row in connection.execute("SELECT lesson_id, objective_code FROM lesson_objective"):
        objectives.setdefault(row["lesson_id"], set()).add(row["objective_code"])
    return [
        LessonKey(
            row["id"],
            row["unit_code"],
            frozenset(objectives.get(row["id"], ())),
            tuple(orjson.loads(row["refs"])),
        )
        for row in connection.execute("SELECT id, unit_code, refs FROM lesson")
    ]


def _ref_score(question_refs: list[str], lesson_refs: tuple[str, ...]) -> int:
    """How specifically a lesson's refs cover a question's refs. An exact section match beats a
    lesson chapter that contains the question's subsection ("ADM §3" ⊇ "ADM §3.2"), which beats a
    lesson subsection under the question's chapter; a deeper matching section beats a shallower one."""
    best = 0
    for question_ref in question_refs:
        for lesson_ref in lesson_refs:
            depth = lesson_ref.count(".")
            if question_ref == lesson_ref:
                score = 100 + depth * 10
            elif question_ref.startswith(lesson_ref + "."):
                score = 50 + depth * 10
            elif lesson_ref.startswith(question_ref + "."):
                score = 10
            else:
                continue
            best = max(best, score)
    return best


def assign_lessons(
    lessons: list[LessonKey], questions: list[Question], path: Path
) -> tuple[dict[str, str], list[str]]:
    """One lesson per question, so a question is checked in exactly one lesson.

    An explicit ``lesson`` on the question wins and must name a lesson of the question's unit that
    carries its objective (anything else is a ContentError). Otherwise the lesson is derived: among
    the unit's lessons that carry the objective, the one whose refs cover the question's refs most
    specifically. A tie is not guessed: the question gets no lesson and a warning names the tied
    lessons, so ``tests/test_content.py`` fails until the author records ``lesson:`` in the file.
    A unit with no lessons yet maps nothing and warns nothing."""
    by_id = {lesson.id: lesson for lesson in lessons}
    mapping: dict[str, str] = {}
    warnings: list[str] = []
    for question in questions:
        candidates = [
            lesson
            for lesson in lessons
            if lesson.unit == question.unit and question.objective in lesson.objectives
        ]
        if question.lesson is not None:
            lesson = by_id.get(question.lesson)
            if lesson is None:
                raise ContentError(
                    f"{path}: question {question.id}: lesson {question.lesson!r} does not exist"
                )
            if lesson.unit != question.unit or question.objective not in lesson.objectives:
                raise ContentError(
                    f"{path}: question {question.id}: lesson {question.lesson!r} is not a lesson of unit"
                    f" {question.unit} carrying objective {question.objective}"
                )
            mapping[question.id] = lesson.id
            continue
        if not any(lesson.unit == question.unit for lesson in lessons):
            continue
        if not candidates:
            warnings.append(
                f"{path}: question {question.id}: no lesson of unit {question.unit} carries objective"
                f" {question.objective}; it will not appear in any check-yourself"
            )
            continue
        scored = sorted(
            ((_ref_score(question.refs, lesson.refs), lesson.id) for lesson in candidates), reverse=True
        )
        if len(scored) > 1 and scored[0][0] == scored[1][0]:
            tied = [lesson_id for score, lesson_id in scored if score == scored[0][0]]
            warnings.append(
                f"{path}: question {question.id}: lessons {tied} cite its sections equally; set lesson: to one of them"
            )
            continue
        mapping[question.id] = scored[0][1]
    return mapping, warnings


# ---------------------------------------------------------------- write the cache
_CACHE_TABLES = (
    "lesson_question",
    "question_option",
    "question",
    "question_set",
    "example_document",
    "adm_artefact",
    "adm_technique",
    "adm_phase",
    "glossary_term",
    "lesson_week",
    "curriculum_week",
    "lesson_objective",
    "lesson",
    "objective",
    "learning_unit",
)


def load_all(connection: sqlite3.Connection, content_dir: Path) -> LoadReport:
    blueprint = load_blueprint(content_dir)
    summaries = _load_units(content_dir, blueprint)
    lessons = load_lessons(content_dir, blueprint)
    terms = load_glossary(content_dir, blueprint)
    phases, techniques, artefacts = load_adm(content_dir, {lesson.id for lesson in lessons})
    examples = load_examples(content_dir)
    curriculum = load_curriculum(content_dir, lessons)
    sets = load_question_sets(content_dir, blueprint)
    report = LoadReport()
    for lesson_id in unplaced_lessons(lessons, curriculum):
        report.warnings.append(f"curriculum.yaml does not place lesson {lesson_id}; it is appended after the braid")

    with transaction(connection):
        for table in _CACHE_TABLES:
            connection.execute(f"DELETE FROM {table}")
        for ordinal, unit in enumerate(blueprint.units, start=1):
            scoring = blueprint.exam(unit.exam).scoring if unit.exam else ""
            connection.execute(
                "INSERT INTO learning_unit(code, exam, track, scoring, name, ordinal, weight, summary_md) VALUES (?,?,?,?,?,?,?,?)",
                (
                    unit.code,
                    unit.exam or "",
                    unit.track,
                    scoring,
                    unit.name,
                    ordinal,
                    unit.weight,
                    summaries.get(unit.code, ""),
                ),
            )
            report.units += 1
            for index, spec in enumerate(unit.objectives, start=1):
                connection.execute(
                    "INSERT INTO objective(code, unit_code, text, ordinal) VALUES (?,?,?,?)",
                    (spec.code, unit.code, spec.text, index),
                )
                report.objectives += 1
        for lesson in lessons:
            connection.execute(
                "INSERT INTO lesson(id, unit_code, slug, title, body_md, reading_minutes, ordinal, refs, source, status, content_hash)"
                " VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                (
                    lesson.id,
                    lesson.unit,
                    lesson.slug,
                    lesson.front.title,
                    lesson.body_md,
                    lesson.front.reading_minutes,
                    lesson.ordinal,
                    _json(lesson.front.refs),
                    lesson.front.source,
                    lesson.front.status,
                    lesson.hash(),
                ),
            )
            for objective_code in lesson.front.objectives:
                connection.execute(
                    "INSERT INTO lesson_objective(lesson_id, objective_code) VALUES (?,?)",
                    (lesson.id, objective_code),
                )
            report.lessons += 1
        for week in curriculum.weeks:
            connection.execute(
                "INSERT INTO curriculum_week(week, theme, exercise_draw, exercise_justify) VALUES (?,?,?,?)",
                (week.week, week.theme, week.exercises.draw, week.exercises.justify),
            )
            report.weeks += 1
        for lesson_id, (week_number, position) in curriculum.placement.items():
            connection.execute(
                "INSERT INTO lesson_week(lesson_id, week, position) VALUES (?,?,?)",
                (lesson_id, week_number, position),
            )
        for term in terms:
            connection.execute(
                "INSERT INTO glossary_term(id, term, definition, document, section, confusable_with, objectives, source, status)"
                " VALUES (?,?,?,?,?,?,?,?,?)",
                (
                    term.id,
                    term.term,
                    term.definition,
                    term.document,
                    term.section,
                    _json(term.confusable_with),
                    _json(term.objectives),
                    term.source,
                    term.status,
                ),
            )
            report.terms += 1
        for ordinal, phase in enumerate(phases, start=1):
            connection.execute(
                "INSERT INTO adm_phase(code, name, objective, approach, inputs, steps, outputs, artefacts, deliverables, refs, traps, crosswalk, ordinal)"
                " VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (
                    phase.code,
                    phase.name,
                    _json(phase.objective),
                    phase.approach,
                    _json(phase.inputs),
                    _json(phase.steps),
                    _json(phase.outputs),
                    _json(phase.artefacts),
                    _json(phase.deliverables),
                    _json(phase.refs),
                    _json(phase.traps),
                    _json(phase.crosswalk.model_dump()) if phase.crosswalk else "",
                    ordinal,
                ),
            )
            if phase.crosswalk:
                report.crosswalks += 1
            report.phases += 1
        for technique in techniques:
            connection.execute(
                "INSERT INTO adm_technique(code, name, purpose, phases, artefacts, traps, refs) VALUES (?,?,?,?,?,?,?)",
                (
                    technique.code,
                    technique.name,
                    technique.purpose,
                    _json(technique.phases),
                    _json(technique.artefacts),
                    _json(technique.traps),
                    _json(technique.refs),
                ),
            )
            report.techniques += 1
        for artefact in artefacts:
            connection.execute(
                "INSERT INTO adm_artefact(code, name, kind, phase_code, domain, purpose, refs, archimate) VALUES (?,?,?,?,?,?,?,?)",
                (
                    artefact.code,
                    artefact.name,
                    artefact.kind,
                    artefact.phase,
                    artefact.domain,
                    artefact.purpose,
                    _json(artefact.refs),
                    _json(artefact.archimate.model_dump()) if artefact.archimate else "",
                ),
            )
            report.artefacts += 1
        for example in examples:
            connection.execute(
                "INSERT INTO example_document(id, deliverable, title, phase_code, kind, track, figure, viewpoint, artefacts,"
                " summary, body_md, ordinal, refs, source, status, content_hash) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (
                    example.id,
                    example.front.deliverable,
                    example.front.title,
                    example.front.phase,
                    example.front.kind,
                    example.front.track,
                    example.front.figure or "",
                    example.front.viewpoint or "",
                    _json(example.front.artefacts),
                    example.front.summary,
                    example.body_md,
                    example.ordinal,
                    _json(example.front.refs),
                    example.front.source,
                    example.front.status,
                    example.hash(),
                ),
            )
            report.examples += 1
        keys = lesson_keys_of(lessons)
        for question_set in sets:
            lesson_of, warnings = assign_lessons(
                keys, question_set.questions(), content_dir / "questions" / f"{question_set.code}"
            )
            report.warnings.extend(warnings)
            insert_question_set(connection, question_set, lesson_of)
            report.sets += 1
            report.questions += question_set.count()

    for warning in report.warnings:
        logger.warning(warning)
    logger.info(f"content loaded from {content_dir}: {report.summary()}")
    return report


def insert_question_set(
    connection: sqlite3.Connection,
    question_set: QuestionSetFile,
    lesson_of: dict[str, str],
    file_name: str | None = None,
    imported_at: str | None = None,
) -> None:
    """Insert one set, its questions and their lesson mapping (``lesson_of`` from ``assign_lessons``).
    Callers hold the transaction. Used by the loader and the importer."""
    connection.execute(
        "INSERT INTO question_set(code, exam, name, source, kind, question_count, file_name, imported_at) VALUES (?,?,?,?,?,?,?,?)",
        (
            question_set.code,
            question_set.exam,
            question_set.name,
            question_set.source,
            question_set.kind,
            question_set.count(),
            file_name,
            imported_at,
        ),
    )
    for question in question_set.single:
        connection.execute(
            "INSERT INTO question(id, exam, track, scoring, unit_code, objective_code, set_code, source, status, figure_id, stem_or_scenario,"
            " question_text, explanation, open_book_hint, refs, difficulty, tags, content_hash)"
            " VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (
                question.id,
                question_set.exam,
                question_set.track,
                "single",
                question.unit,
                question.objective,
                question_set.code,
                question.source,
                question.status,
                question.figure,
                question.stem,
                "",
                question.explanation,
                "",
                _json(question.refs),
                question.difficulty,
                _json(question.tags),
                question.hash(),
            ),
        )
        for ordinal, option in enumerate(question.options, start=1):
            connection.execute(
                "INSERT INTO question_option(question_id, key, text, points, why, ordinal) VALUES (?,?,?,?,?,?)",
                (question.id, option.key, option.text, 1 if option.correct else 0, option.why, ordinal),
            )
    for scenario in question_set.gradient:
        connection.execute(
            "INSERT INTO question(id, exam, track, scoring, unit_code, objective_code, set_code, source, status, figure_id, stem_or_scenario,"
            " question_text, explanation, open_book_hint, refs, difficulty, tags, content_hash)"
            " VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (
                scenario.id,
                question_set.exam,
                question_set.track,
                "gradient",
                scenario.unit,
                scenario.objective,
                question_set.code,
                scenario.source,
                scenario.status,
                scenario.figure,
                scenario.scenario,
                scenario.question,
                "",
                scenario.open_book_hint,
                _json(scenario.refs),
                scenario.difficulty,
                _json(scenario.tags),
                scenario.hash(),
            ),
        )
        for ordinal, answer in enumerate(scenario.answers, start=1):
            connection.execute(
                "INSERT INTO question_option(question_id, key, text, points, why, ordinal) VALUES (?,?,?,?,?,?)",
                (scenario.id, answer.key, answer.text, answer.points, answer.why, ordinal),
            )
    for question_id, lesson_id in lesson_of.items():
        connection.execute(
            "INSERT INTO lesson_question(question_id, lesson_id) VALUES (?, ?)", (question_id, lesson_id)
        )
