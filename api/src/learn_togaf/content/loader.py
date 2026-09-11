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
    FoundationQuestion,
    GlossaryTerm,
    ImportantFigure,
    Lesson,
    LessonFrontMatter,
    PractitionerQuestion,
    QuestionSetFile,
)
from learn_togaf.db import transaction

ModelT = TypeVar("ModelT", bound=BaseModel)

_FRONT_MATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", re.DOTALL)
_LESSON_FILE_RE = re.compile(r"^(?P<nn>\d{2})_(?P<slug>[a-z0-9_\-]+)\.md$")


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
    sets: int = 0
    questions: int = 0
    warnings: list[str] = field(default_factory=list)

    def summary(self) -> str:
        return (
            f"units={self.units} objectives={self.objectives} lessons={self.lessons} terms={self.terms} "
            f"phases={self.phases} techniques={self.techniques} artefacts={self.artefacts} "
            f"sets={self.sets} questions={self.questions} warnings={len(self.warnings)}"
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


def load_adm(content_dir: Path) -> tuple[list[AdmPhase], list[AdmTechnique], list[AdmArtefact]]:
    adm_dir = content_dir / "adm"
    phases = _load_list(adm_dir / "phases.yaml", AdmPhase, "phase")
    techniques = _load_list(adm_dir / "techniques.yaml", AdmTechnique, "technique")
    artefacts = _load_list(adm_dir / "artefacts.yaml", AdmArtefact, "artefact")
    phase_codes = {phase.code for phase in phases}
    artefact_codes = {artefact.code for artefact in artefacts}
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
    exam = str(data.get("exam", "")).upper()
    data["exam"] = exam
    if exam == "FOUNDATION":
        data["foundation"] = questions
    elif exam == "PRACTITIONER":
        data["practitioner"] = questions
    try:
        question_set = QuestionSetFile.model_validate(data)
    except ValidationError as exc:
        raise ContentError(f"{path}: {exc}") from exc
    objective_unit = blueprint.objective_unit()
    parsed: list[FoundationQuestion | PractitionerQuestion] = [
        *question_set.foundation,
        *question_set.practitioner,
    ]
    for question in parsed:
        if question.unit not in blueprint.unit_codes():
            raise ContentError(
                f"{path}: question {question.id}: unit {question.unit!r} is not in blueprint.yaml"
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
    for sub in ("foundation", "practitioner", "figures", "imported"):
        for path in sorted((questions_dir / sub).glob("*.yaml")):
            sets.append(parse_question_set(_read_yaml(path), path, blueprint))
    codes = [question_set.code for question_set in sets]
    if len(codes) != len(set(codes)):
        raise ContentError(
            f"duplicate question set codes: {sorted({c for c in codes if codes.count(c) > 1})}"
        )
    ids = [q.id for s in sets for q in s.foundation] + [q.id for s in sets for q in s.practitioner]
    duplicates = sorted({i for i in ids if ids.count(i) > 1})
    if duplicates:
        raise ContentError(f"duplicate question ids across sets: {duplicates[:10]}")
    return sets


def load_important_figures(sources_dir: Path) -> list[ImportantFigure]:
    return _load_list(sources_dir / "figures" / "important.yaml", ImportantFigure, "figure")


# ---------------------------------------------------------------- write the cache
_CACHE_TABLES = (
    "question_option",
    "question",
    "question_set",
    "adm_artefact",
    "adm_technique",
    "adm_phase",
    "glossary_term",
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
    phases, techniques, artefacts = load_adm(content_dir)
    sets = load_question_sets(content_dir, blueprint)
    report = LoadReport()

    with transaction(connection):
        for table in _CACHE_TABLES:
            connection.execute(f"DELETE FROM {table}")
        for ordinal, unit in enumerate(blueprint.units, start=1):
            connection.execute(
                "INSERT INTO learning_unit(code, exam, name, ordinal, weight, summary_md) VALUES (?,?,?,?,?,?)",
                (unit.code, unit.exam, unit.name, ordinal, unit.weight, summaries.get(unit.code, "")),
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
                "INSERT INTO adm_phase(code, name, objective, approach, inputs, steps, outputs, artefacts, deliverables, refs, traps, ordinal)"
                " VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
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
                    ordinal,
                ),
            )
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
                "INSERT INTO adm_artefact(code, name, kind, phase_code, domain, purpose, refs) VALUES (?,?,?,?,?,?,?)",
                (
                    artefact.code,
                    artefact.name,
                    artefact.kind,
                    artefact.phase,
                    artefact.domain,
                    artefact.purpose,
                    _json(artefact.refs),
                ),
            )
            report.artefacts += 1
        for question_set in sets:
            insert_question_set(connection, question_set)
            report.sets += 1
            report.questions += question_set.count()

    logger.info(f"content loaded from {content_dir}: {report.summary()}")
    return report


def insert_question_set(
    connection: sqlite3.Connection,
    question_set: QuestionSetFile,
    file_name: str | None = None,
    imported_at: str | None = None,
) -> None:
    """Insert one set and its questions. Callers hold the transaction. Used by the loader and the importer."""
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
    for question in question_set.foundation:
        connection.execute(
            "INSERT INTO question(id, exam, unit_code, objective_code, set_code, source, status, figure_id, stem_or_scenario,"
            " question_text, explanation, open_book_hint, refs, difficulty, tags, content_hash)"
            " VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (
                question.id,
                "FOUNDATION",
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
    for scenario in question_set.practitioner:
        connection.execute(
            "INSERT INTO question(id, exam, unit_code, objective_code, set_code, source, status, figure_id, stem_or_scenario,"
            " question_text, explanation, open_book_hint, refs, difficulty, tags, content_hash)"
            " VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (
                scenario.id,
                "PRACTITIONER",
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
