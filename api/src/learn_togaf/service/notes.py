"""Notes on any lesson, term, phase or question, and the learner-state export (learn_togaf.md §4.10)."""

import sqlite3
from datetime import UTC, datetime
from typing import Any

import orjson

NOTE_KINDS = ("LESSON", "TERM", "PHASE", "QUESTION")
EXPORT_VERSION = 1


def _now_iso() -> str:
    return datetime.now(UTC).isoformat(timespec="seconds")


def get_note(connection: sqlite3.Connection, ref_kind: str, ref_id: str) -> sqlite3.Row | None:
    return connection.execute(
        "SELECT * FROM note WHERE ref_kind = ? AND ref_id = ?", (ref_kind, ref_id)
    ).fetchone()


def save_note(connection: sqlite3.Connection, ref_kind: str, ref_id: str, body_md: str) -> sqlite3.Row:
    if ref_kind not in NOTE_KINDS:
        raise ValueError(f"note ref_kind must be one of {NOTE_KINDS}, got {ref_kind!r}")
    connection.execute(
        """
        INSERT INTO note(ref_kind, ref_id, body_md, updated_at) VALUES (?, ?, ?, ?)
        ON CONFLICT(ref_kind, ref_id) DO UPDATE SET body_md = excluded.body_md, updated_at = excluded.updated_at
        """,
        (ref_kind, ref_id, body_md, _now_iso()),
    )
    row = get_note(connection, ref_kind, ref_id)
    assert row is not None
    return row


def _rows(connection: sqlite3.Connection, sql: str) -> list[dict[str, Any]]:
    return [dict(row) for row in connection.execute(sql).fetchall()]


def export_state(connection: sqlite3.Connection) -> dict[str, Any]:
    attempts = _rows(connection, "SELECT * FROM attempt ORDER BY id")
    answers: dict[int, list[dict[str, Any]]] = {}
    for answer in _rows(connection, "SELECT * FROM attempt_answer ORDER BY attempt_id, answered_at"):
        answers.setdefault(answer["attempt_id"], []).append(answer)
    for attempt in attempts:
        attempt["question_ids"] = orjson.loads(attempt["question_ids"])
        attempt["filters"] = orjson.loads(attempt["filters"])
        attempt["answers"] = answers.get(attempt["id"], [])
    return {
        "version": EXPORT_VERSION,
        "exported_at": _now_iso(),
        "attempts": attempts,
        "card_reviews": _rows(connection, "SELECT * FROM card_review ORDER BY id"),
        "notes": _rows(connection, "SELECT * FROM note ORDER BY id"),
        "lesson_progress": _rows(connection, "SELECT * FROM lesson_progress ORDER BY lesson_id"),
        "settings": _rows(connection, "SELECT * FROM setting ORDER BY key"),
        "study_sessions": _rows(connection, "SELECT * FROM study_session ORDER BY id"),
    }
