"""Glossary search and term pages (learn_togaf.md §4.4)."""

import sqlite3
from typing import Any

import orjson

from learn_togaf.content.models import document_track

TRACKS = ("TOGAF", "ARCHIMATE", "SABSA", "CROSSWALK")


def _names(connection: sqlite3.Connection, ids: list[str]) -> list[dict[str, str]]:
    if not ids:
        return []
    placeholders = ",".join("?" for _ in ids)
    rows = connection.execute(
        f"SELECT id, term FROM glossary_term WHERE id IN ({placeholders})", ids
    ).fetchall()
    by_id = {row["id"]: row["term"] for row in rows}
    return [{"id": term_id, "term": by_id.get(term_id, term_id)} for term_id in ids]


def _shape(connection: sqlite3.Connection, row: sqlite3.Row) -> dict[str, Any]:
    data = dict(row)
    data["confusable_with"] = _names(connection, orjson.loads(row["confusable_with"]))
    data["objectives"] = orjson.loads(row["objectives"])
    data["track"] = document_track(row["document"])
    return data


def search(connection: sqlite3.Connection, query: str, track: str = "") -> list[dict[str, Any]]:
    """Terms matching the query; ``track`` keeps one framework's terms (by the document they cite)."""
    needle = f"%{query.strip()}%"
    rows = connection.execute(
        "SELECT * FROM glossary_term WHERE term LIKE ? OR definition LIKE ? ORDER BY term COLLATE NOCASE",
        (needle, needle),
    ).fetchall()
    shaped = [_shape(connection, row) for row in rows]
    return [term for term in shaped if not track or term["track"] == track]


def track_counts(connection: sqlite3.Connection) -> dict[str, int]:
    counts = dict.fromkeys(TRACKS, 0)
    for row in connection.execute("SELECT document FROM glossary_term"):
        counts[document_track(row["document"])] += 1
    return counts


def term(connection: sqlite3.Connection, term_id: str) -> dict[str, Any] | None:
    row = connection.execute("SELECT * FROM glossary_term WHERE id = ?", (term_id,)).fetchone()
    if row is None:
        return None
    data = _shape(connection, row)
    ids = [item["id"] for item in data["confusable_with"]]
    placeholders = ",".join("?" for _ in ids) or "''"
    data["confusables"] = [
        _shape(connection, other)
        for other in connection.execute(
            f"SELECT * FROM glossary_term WHERE id IN ({placeholders})", ids
        ).fetchall()
    ]
    objective_placeholders = ",".join("?" for _ in data["objectives"]) or "''"
    data["objective_rows"] = connection.execute(
        f"SELECT code, text, unit_code FROM objective WHERE code IN ({objective_placeholders}) ORDER BY ordinal",
        data["objectives"],
    ).fetchall()
    return data
