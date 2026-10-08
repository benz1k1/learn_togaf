"""
Import wizard back end (learn_togaf.md §4.7): parse → map → validate → preview → confirm.

Nothing lands before ``confirm_import``. ``build_preview`` parses and normalises the upload,
stores the normalised rows under ``setting`` ``import_pending:<token>`` and returns the
analysis; ``confirm_import`` re-runs the same analysis with the learner's final unit mapping
(so what was previewed is what is inserted), inserts the set through
``content.loader.insert_question_set`` inside one transaction and writes the set to
``content/questions/imported/<code>.yaml`` in the native shape so ``--load-content`` keeps it.

Validation is the loader's own: every row goes through ``FoundationQuestion`` /
``PractitionerQuestion`` individually (so errors are listed per row) and the surviving rows
through ``parse_question_set`` (the set-level rules). Dedupe is ``content_hash`` against the
``question`` table: a duplicate is reported with the id it duplicates, never re-imported.

Imported rows default to ``status: reviewed`` — the learner chose to bring them in, and §4.7
says mocks may draw from "our sets" or "all"; a file that says ``status: draft`` keeps it.
"""

import re
import secrets
import sqlite3
from dataclasses import dataclass, field
from datetime import UTC, datetime, timedelta
from pathlib import Path
from typing import Any

import orjson
import yaml
from loguru import logger
from pydantic import ValidationError

from learn_togaf.config import CONTENT_DIR
from learn_togaf.content.loader import (
    ContentError,
    assign_lessons,
    insert_question_set,
    lesson_keys,
    parse_question_set,
)
from learn_togaf.content.models import Blueprint, FoundationQuestion, PractitionerQuestion
from learn_togaf.db import transaction
from learn_togaf.importers import ImportParseError, normalise, parse_file
from learn_togaf.pages.context import get_setting, set_setting

PENDING_PREFIX = "import_pending:"
MAPPING_PREFIX = "import_mapping:"
UNVERIFIED_TAG = "unit-unverified"
_PENDING_TTL = timedelta(hours=12)
_CODE_RE = re.compile(r"[^A-Z0-9]+")
_WORD_RE = re.compile(r"[a-z][a-z0-9\-]{3,}")
_STOP_WORDS = frozenset(
    "which what that this with from into about their there these those does have been being "
    "following describe describes best answer question togaf standard architecture enterprise".split()
)


def _now() -> str:
    return datetime.now(UTC).isoformat(timespec="seconds")


def sanitise_code(code: str, file_name: str) -> str:
    raw = code.strip() or Path(file_name).stem
    cleaned = _CODE_RE.sub("_", raw.upper()).strip("_")
    if not cleaned:
        raise ContentError(f"cannot derive a set code from {file_name!r}; enter one")
    return cleaned


# ---------------------------------------------------------------- analysis result
@dataclass
class RowError:
    index: int
    id: str
    stem: str
    errors: list[str]


@dataclass
class Duplicate:
    index: int
    id: str
    stem: str
    duplicate_of: str


@dataclass
class UnitGroup:
    key: str  # the unit value as it appeared in the file ("" = none)
    count: int
    unit: str  # the unit that will be used
    guessed: bool  # True when the app chose it by keyword


@dataclass
class Preview:
    token: str
    file_name: str
    format: str
    set_code: str
    exam: str
    name: str
    total: int
    valid: list[dict[str, Any]] = field(default_factory=list)
    errors: list[RowError] = field(default_factory=list)
    duplicates: list[Duplicate] = field(default_factory=list)
    groups: list[UnitGroup] = field(default_factory=list)
    unverified_ids: list[str] = field(default_factory=list)
    set_errors: list[str] = field(default_factory=list)
    columns: list[str] = field(default_factory=list)

    @property
    def importable(self) -> int:
        return len(self.valid)


# ---------------------------------------------------------------- keyword unit mapping
def _words(text: str) -> set[str]:
    return {word for word in _WORD_RE.findall(text.lower()) if word not in _STOP_WORDS}


def _question_text(row: dict[str, Any]) -> str:
    parts = [str(row.get("stem", "")), str(row.get("scenario", "")), str(row.get("question", ""))]
    parts += [str(option.get("text", "")) for option in row.get("options", []) if isinstance(option, dict)]
    parts += [str(answer.get("text", "")) for answer in row.get("answers", []) if isinstance(answer, dict)]
    parts += [str(tag) for tag in row.get("tags", [])]
    return " ".join(parts)


def suggest_objective(blueprint: Blueprint, exam: str, text: str, unit: str = "") -> tuple[str, str]:
    """(unit, objective) chosen by keyword overlap with unit names and objective texts.
    With ``unit`` given, only that unit's objectives compete."""
    words = _words(text)
    best: tuple[int, str, str] | None = None
    for spec in blueprint.units:
        if spec.exam != exam or (unit and spec.code != unit):
            continue
        unit_words = _words(spec.name)
        for objective in spec.objectives:
            score = 2 * len(words & _words(objective.text)) + len(words & unit_words)
            if best is None or score > best[0]:
                best = (score, spec.code, objective.code)
    if best is None:
        raise ContentError(
            f"no unit in the blueprint for exam {exam}" + (f" with code {unit}" if unit else "")
        )
    return best[1], best[2]


# ---------------------------------------------------------------- mapping settings
def load_mapping(connection: sqlite3.Connection, file_name: str) -> dict[str, Any]:
    raw = get_setting(connection, f"{MAPPING_PREFIX}{file_name}")
    if not raw:
        return {"columns": {}, "units": {}}
    mapping = orjson.loads(raw)
    return {"columns": dict(mapping.get("columns", {})), "units": dict(mapping.get("units", {}))}


def save_mapping(
    connection: sqlite3.Connection, file_name: str, columns: dict[str, str], units: dict[str, str]
) -> None:
    set_setting(
        connection,
        f"{MAPPING_PREFIX}{file_name}",
        orjson.dumps({"columns": columns, "units": units}).decode(),
    )


def _purge_stale_pending(connection: sqlite3.Connection) -> None:
    cutoff = (datetime.now(UTC) - _PENDING_TTL).isoformat(timespec="seconds")
    for row in connection.execute(
        "SELECT key, value FROM setting WHERE key LIKE ?", (f"{PENDING_PREFIX}%",)
    ).fetchall():
        if orjson.loads(row["value"]).get("created_at", "") < cutoff:
            connection.execute("DELETE FROM setting WHERE key = ?", (row["key"],))


def load_pending(connection: sqlite3.Connection, token: str) -> dict[str, Any]:
    raw = get_setting(connection, f"{PENDING_PREFIX}{token}")
    if not raw:
        raise ContentError("this import preview has expired; upload the file again")
    return orjson.loads(raw)


# ---------------------------------------------------------------- analysis
def _row_errors(exc: ValidationError) -> list[str]:
    errors = []
    for error in exc.errors():
        location = ".".join(str(part) for part in error["loc"]) or "row"
        errors.append(f"{location}: {error['msg']}")
    return errors


def _validate_row(row: dict[str, Any], exam: str, blueprint: Blueprint) -> tuple[Any, list[str]]:
    model = PractitionerQuestion if blueprint.exam(exam).scoring == "gradient" else FoundationQuestion
    try:
        question = model.model_validate(row)
    except ValidationError as exc:
        return None, _row_errors(exc)
    errors = []
    if question.unit not in blueprint.unit_codes():
        errors.append(f"unit: {question.unit!r} is not in the blueprint")
    elif blueprint.objective_unit().get(question.objective) != question.unit:
        errors.append(f"objective: {question.objective!r} is not an objective of unit {question.unit}")
    return question, errors


def _apply_mapping(
    rows: list[dict[str, Any]], exam: str, blueprint: Blueprint, unit_map: dict[str, str]
) -> tuple[list[UnitGroup], set[str]]:
    """Fill unit/objective on every row in place. Returns the groups (by the unit value the
    file carried) and the ids whose unit the app guessed by keyword."""
    objective_unit = blueprint.objective_unit()
    unit_codes = {spec.code for spec in blueprint.units if spec.exam == exam}
    groups: dict[str, UnitGroup] = {}
    unverified: set[str] = set()
    for row in rows:
        original = str(row.get("unit", "")).strip().upper()
        group = groups.get(original)
        if group is None:
            if original in unit_map and unit_map[original] in unit_codes:
                chosen, guessed = unit_map[original], False
            elif original in unit_codes:
                chosen, guessed = original, False
            else:
                chosen, guessed = "", True
            group = groups[original] = UnitGroup(key=original, count=0, unit=chosen, guessed=guessed)
        group.count += 1
        objective = str(row.get("objective", "")).strip()
        if group.unit:
            # The unit came from the file or the learner: only the objective is guessed, which
            # does not touch the blueprint weighting, so the row is not flagged.
            row["unit"] = group.unit
            if objective_unit.get(objective) != group.unit:
                row["objective"] = suggest_objective(blueprint, exam, _question_text(row), group.unit)[1]
        elif objective_unit.get(objective) in unit_codes:
            row["unit"] = objective_unit[objective]
        else:
            row["unit"], row["objective"] = suggest_objective(blueprint, exam, _question_text(row))
            unverified.add(row["id"])
    for group in groups.values():
        if not group.unit:
            counts: dict[str, int] = {}
            for row in rows:
                if str(row.get("_original_unit", "")) == group.key:
                    counts[row["unit"]] = counts.get(row["unit"], 0) + 1
            group.unit = max(counts, key=counts.get) if counts else ""  # type: ignore[arg-type]
    return list(groups.values()), unverified


def analyse(
    connection: sqlite3.Connection, blueprint: Blueprint, pending: dict[str, Any], unit_map: dict[str, str]
) -> Preview:
    exam = pending["exam"]
    set_code = pending["set_code"]
    rows = [dict(row) for row in pending["rows"]]
    for row in rows:
        row["_original_unit"] = str(row.get("unit", "")).strip().upper()
    groups, unverified = _apply_mapping(rows, exam, blueprint, unit_map)
    for row in rows:
        row.pop("_original_unit", None)

    preview = Preview(
        token=pending["token"],
        file_name=pending["file_name"],
        format=pending["format"],
        set_code=set_code,
        exam=exam,
        name=pending["name"],
        total=len(rows),
        groups=groups,
        columns=pending.get("columns", []),
    )
    if connection.execute("SELECT 1 FROM question_set WHERE code = ?", (set_code,)).fetchone():
        preview.set_errors.append(
            f"a question set with code {set_code} already exists; remove it first or choose another code"
        )

    seen_ids: dict[str, int] = {}
    seen_hashes: dict[str, str] = {}
    for index, row in enumerate(rows, start=1):
        stem = str(row.get("stem") or row.get("question") or "")[:120]
        question, errors = _validate_row(row, exam, blueprint)
        if row["id"] in seen_ids:
            errors.append(f"id: {row['id']} appears twice in the file (row {seen_ids[row['id']]})")
        seen_ids.setdefault(row["id"], index)
        if question is None or errors:
            preview.errors.append(RowError(index, row["id"], stem, errors))
            continue
        digest = question.hash()
        existing = connection.execute("SELECT id FROM question WHERE content_hash = ?", (digest,)).fetchone()
        if existing:
            preview.duplicates.append(Duplicate(index, row["id"], stem, existing["id"]))
            continue
        if digest in seen_hashes:
            preview.duplicates.append(
                Duplicate(index, row["id"], stem, f"row {seen_hashes[digest]} of this file")
            )
            continue
        seen_hashes[digest] = row["id"]
        if connection.execute("SELECT 1 FROM question WHERE id = ?", (row["id"],)).fetchone():
            preview.errors.append(
                RowError(index, row["id"], stem, [f"id: {row['id']} already exists in the bank"])
            )
            continue
        if row["id"] in unverified:
            preview.unverified_ids.append(row["id"])
            tags = [str(tag) for tag in row.get("tags", [])]
            if UNVERIFIED_TAG not in tags:
                row["tags"] = [*tags, UNVERIFIED_TAG]
        preview.valid.append(row)

    if preview.valid:
        try:
            parse_question_set(_set_document(preview, preview.valid), Path(preview.file_name), blueprint)
        except ContentError as exc:
            preview.set_errors.append(str(exc))
    return preview


def _set_document(
    preview: Preview, rows: list[dict[str, Any]], imported_at: str | None = None
) -> dict[str, Any]:
    document: dict[str, Any] = {
        "code": preview.set_code,
        "exam": preview.exam,
        "name": preview.name,
        "kind": "IMPORTED",
        "source": "imported",
        "file_name": preview.file_name,
    }
    if imported_at:
        document["imported_at"] = imported_at
    document["questions"] = rows
    return document


# ---------------------------------------------------------------- the wizard steps
def build_preview(
    connection: sqlite3.Connection,
    blueprint: Blueprint,
    text: str,
    file_name: str,
    exam: str,
    name: str,
    set_code: str,
    unit_overrides: dict[str, str],
) -> Preview:
    exam = exam.strip().upper()
    if exam not in blueprint.exams:
        raise ContentError(f"exam must be one of {', '.join(blueprint.exams)}, got {exam!r}")
    mapping = load_mapping(connection, file_name)
    try:
        parsed = parse_file(text, file_name, mapping["columns"])
    except ImportParseError as exc:
        raise ContentError(f"{file_name}: {exc}") from exc
    header_exam = str(parsed.header.get("exam", "")).upper()
    if header_exam and header_exam != exam:
        raise ContentError(f"{file_name} says exam {header_exam}, the form says {exam}")
    code = sanitise_code(set_code or str(parsed.header.get("code", "")), file_name)
    set_name = name.strip() or str(parsed.header.get("name", "")).strip() or Path(file_name).stem
    rows = normalise(parsed.rows, blueprint.exam(exam).scoring, code)
    if not rows:
        raise ContentError(f"{file_name}: no questions found ({parsed.format})")
    token = secrets.token_urlsafe(16)
    pending = {
        "token": token,
        "created_at": _now(),
        "file_name": file_name,
        "format": parsed.format,
        "exam": exam,
        "set_code": code,
        "name": set_name,
        "columns": parsed.columns,
        "column_map": mapping["columns"],
        "rows": rows,
    }
    with transaction(connection):
        _purge_stale_pending(connection)
        set_setting(connection, f"{PENDING_PREFIX}{token}", orjson.dumps(pending).decode())
    unit_map = {**mapping["units"], **unit_overrides}
    preview = analyse(connection, blueprint, pending, unit_map)
    logger.info(
        f"import preview {file_name} ({parsed.format}) set={code}: valid={len(preview.valid)} "
        f"errors={len(preview.errors)} duplicates={len(preview.duplicates)} unverified={len(preview.unverified_ids)}"
    )
    return preview


@dataclass
class ImportResult:
    set_code: str
    inserted: int
    skipped_duplicates: int
    skipped_errors: int
    unverified: int
    file_path: Path


def confirm_import(
    connection: sqlite3.Connection,
    blueprint: Blueprint,
    token: str,
    import_partial: bool,
    unit_overrides: dict[str, str],
) -> ImportResult:
    pending = load_pending(connection, token)
    preview = analyse(connection, blueprint, pending, unit_overrides)
    if preview.set_errors:
        raise ContentError("; ".join(preview.set_errors))
    if preview.errors and not import_partial:
        raise ContentError(
            f"{len(preview.errors)} row(s) failed validation; fix the file, or tick 'import what validates' to import the {len(preview.valid)} valid row(s)"
        )
    if not preview.valid:
        raise ContentError("nothing to import: every row is a duplicate or invalid")
    imported_at = _now()
    document = _set_document(preview, preview.valid, imported_at)
    question_set = parse_question_set(document, Path(preview.file_name), blueprint)
    target_dir = CONTENT_DIR / "questions" / "imported"
    target = target_dir / f"{preview.set_code}.yaml"
    lesson_of, lesson_warnings = assign_lessons(
        lesson_keys(connection), question_set.questions(), target
    )
    for warning in lesson_warnings:
        logger.warning(warning)
    with transaction(connection):
        insert_question_set(
            connection, question_set, lesson_of, file_name=preview.file_name, imported_at=imported_at
        )
        for question_id in preview.unverified_ids:
            connection.execute("UPDATE question SET unit_unverified = 1 WHERE id = ?", (question_id,))
        save_mapping(connection, preview.file_name, pending.get("column_map", {}), unit_overrides)
        connection.execute("DELETE FROM setting WHERE key = ?", (f"{PENDING_PREFIX}{token}",))
        target_dir.mkdir(parents=True, exist_ok=True)
        target.write_text(
            "# Imported through /import (learn_togaf.md §4.7). Native shape; never committed.\n"
            + yaml.safe_dump(document, sort_keys=False, allow_unicode=True, width=110),
            encoding="utf-8",
        )
    logger.info(
        f"imported set {preview.set_code} from {preview.file_name}: {len(preview.valid)} questions, "
        f"{len(preview.duplicates)} duplicates skipped, {len(preview.errors)} invalid skipped -> {target}"
    )
    return ImportResult(
        preview.set_code,
        len(preview.valid),
        len(preview.duplicates),
        len(preview.errors),
        len(preview.unverified_ids),
        target,
    )


def list_imported_sets(connection: sqlite3.Connection) -> list[sqlite3.Row]:
    return connection.execute(
        "SELECT s.code, s.exam, s.name, s.question_count, s.file_name, s.imported_at,"
        " (SELECT COUNT(*) FROM question q WHERE q.set_code = s.code AND q.unit_unverified = 1) AS unverified"
        " FROM question_set s WHERE s.source = 'imported' ORDER BY s.imported_at DESC, s.code"
    ).fetchall()


def remove_set(connection: sqlite3.Connection, set_code: str) -> bool:
    row = connection.execute(
        "SELECT code FROM question_set WHERE code = ? AND source = 'imported'", (set_code,)
    ).fetchone()
    if row is None:
        return False
    with transaction(connection):
        connection.execute("DELETE FROM question_set WHERE code = ?", (set_code,))
        target = CONTENT_DIR / "questions" / "imported" / f"{set_code}.yaml"
        if target.is_file():
            target.unlink()
    logger.info(f"removed imported set {set_code}")
    return True


def unit_choices(blueprint: Blueprint, exam: str) -> list[tuple[str, str]]:
    """Units a question of ``exam`` may belong to: every unit of the exam's track that has one."""
    track = blueprint.exam(exam).track
    return [(spec.code, spec.name) for spec in blueprint.units if spec.exam and spec.track == track]
