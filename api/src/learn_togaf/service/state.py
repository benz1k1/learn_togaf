"""
Re-import of the learner state (learn_togaf.md §4.10): the JSON ``/export/state.json``
produced is merged, never replaced. Attempts and study sessions are appended with new ids
(answers re-keyed to the new attempt id); card reviews are upserted by (card_kind, card_ref)
keeping the later ``last_reviewed_at``; notes by (ref_kind, ref_id) keeping the later
``updated_at``; lesson progress by lesson keeping the later ``updated_at``; settings by key.

Row keys are checked against the table's columns and an unknown key fails the import — a
renamed column in the export is a bug to surface, not a field to drop.
"""

import sqlite3
from dataclasses import dataclass
from typing import Any

import orjson
from loguru import logger
from pydantic import BaseModel, ConfigDict, Field, ValidationError, field_validator

from learn_togaf.content.loader import ContentError
from learn_togaf.db import transaction


class StatePayload(BaseModel):
    model_config = ConfigDict(extra="forbid")

    version: int
    exported_at: str = ""
    attempts: list[dict[str, Any]] = Field(default_factory=list)
    card_reviews: list[dict[str, Any]] = Field(default_factory=list)
    notes: list[dict[str, Any]] = Field(default_factory=list)
    lesson_progress: list[dict[str, Any]] = Field(default_factory=list)
    settings: dict[str, Any] = Field(default_factory=dict)
    study_sessions: list[dict[str, Any]] = Field(default_factory=list)

    @field_validator("version")
    @classmethod
    def _version(cls, version: int) -> int:
        if version != 1:
            raise ValueError(f"unsupported state export version {version}; this app reads version 1")
        return version


@dataclass
class StateImportReport:
    attempts: int = 0
    answers: int = 0
    card_reviews: int = 0
    notes: int = 0
    lesson_progress: int = 0
    settings: int = 0
    study_sessions: int = 0

    def summary(self) -> str:
        return (
            f"{self.attempts} attempts ({self.answers} answers), {self.card_reviews} card reviews, "
            f"{self.notes} notes, {self.lesson_progress} lesson progress rows, {self.settings} settings, "
            f"{self.study_sessions} study sessions"
        )


def _columns(connection: sqlite3.Connection, table: str) -> list[str]:
    return [row["name"] for row in connection.execute(f"PRAGMA table_info({table})").fetchall()]


def _row_values(
    table: str, row: dict[str, Any], columns: list[str], drop: tuple[str, ...] = ()
) -> dict[str, Any]:
    values = {key: value for key, value in row.items() if key not in drop}
    unknown = sorted(set(values) - set(columns))
    if unknown:
        raise ContentError(
            f"{table} row has unknown field(s) {unknown}; the export does not match this schema"
        )
    return {key: _sql_value(value) for key, value in values.items()}


def _sql_value(value: Any) -> Any:
    if isinstance(value, (list, dict)):
        return orjson.dumps(value).decode()
    if isinstance(value, bool):
        return int(value)
    return value


def _insert(connection: sqlite3.Connection, table: str, values: dict[str, Any]) -> int:
    keys = list(values)
    placeholders = ",".join("?" for _ in keys)
    cursor = connection.execute(
        f"INSERT INTO {table}({','.join(keys)}) VALUES ({placeholders})", [values[k] for k in keys]
    )
    return int(cursor.lastrowid or 0)


def _upsert_keep_later(
    connection: sqlite3.Connection,
    table: str,
    values: dict[str, Any],
    conflict: tuple[str, ...],
    later_column: str,
) -> None:
    keys = list(values)
    updates = ", ".join(f"{key} = excluded.{key}" for key in keys if key not in conflict)
    connection.execute(
        f"INSERT INTO {table}({','.join(keys)}) VALUES ({','.join('?' for _ in keys)})"
        f" ON CONFLICT({','.join(conflict)}) DO UPDATE SET {updates}"
        f" WHERE COALESCE(excluded.{later_column}, '') > COALESCE({table}.{later_column}, '')",
        [values[k] for k in keys],
    )


def import_state(connection: sqlite3.Connection, payload: dict[str, Any]) -> StateImportReport:
    try:
        state = StatePayload.model_validate(payload)
    except ValidationError as exc:
        raise ContentError(f"state export: {exc}") from exc
    report = StateImportReport()
    attempt_columns = _columns(connection, "attempt")
    answer_columns = _columns(connection, "attempt_answer")
    review_columns = _columns(connection, "card_review")
    note_columns = _columns(connection, "note")
    progress_columns = _columns(connection, "lesson_progress")
    session_columns = _columns(connection, "study_session")

    with transaction(connection):
        for attempt in state.attempts:
            answers = attempt.get("answers", [])
            values = _row_values("attempt", attempt, attempt_columns, drop=("id", "answers"))
            attempt_id = _insert(connection, "attempt", values)
            report.attempts += 1
            for answer in answers:
                answer_values = _row_values("attempt_answer", answer, answer_columns, drop=("attempt_id",))
                answer_values["attempt_id"] = attempt_id
                _insert(connection, "attempt_answer", answer_values)
                report.answers += 1
        for review in state.card_reviews:
            values = _row_values("card_review", review, review_columns, drop=("id",))
            _upsert_keep_later(
                connection, "card_review", values, ("card_kind", "card_ref"), "last_reviewed_at"
            )
            report.card_reviews += 1
        for note in state.notes:
            values = _row_values("note", note, note_columns, drop=("id",))
            _upsert_keep_later(connection, "note", values, ("ref_kind", "ref_id"), "updated_at")
            report.notes += 1
        for progress in state.lesson_progress:
            values = _row_values("lesson_progress", progress, progress_columns)
            _upsert_keep_later(connection, "lesson_progress", values, ("lesson_id",), "updated_at")
            report.lesson_progress += 1
        for key, value in state.settings.items():
            connection.execute(
                "INSERT INTO setting(key, value) VALUES (?, ?) ON CONFLICT(key) DO UPDATE SET value = excluded.value",
                (key, _sql_value(value) if not isinstance(value, str) else value),
            )
            report.settings += 1
        for session in state.study_sessions:
            values = _row_values("study_session", session, session_columns, drop=("id",))
            _insert(connection, "study_session", values)
            report.study_sessions += 1
    logger.info(f"learner state imported: {report.summary()}")
    return report
