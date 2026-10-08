"""Worked example documents (learn_togaf.md §4.3): every deliverable written out for one fictional enterprise."""

import sqlite3
from typing import Any

import orjson

PHASE_ORDER = ("PRELIM", "A", "B", "C", "D", "E", "F", "G", "H", "REQ")


TRACKS = ("TOGAF", "ARCHIMATE", "SABSA")


def _decode(row: sqlite3.Row) -> dict[str, Any]:
    data = dict(row)
    data["refs"] = orjson.loads(data["refs"])
    data["artefacts"] = orjson.loads(data["artefacts"] or "[]")
    return data


def examples(connection: sqlite3.Connection, track: str = "") -> list[dict[str, Any]]:
    if track:
        return [
            _decode(row)
            for row in connection.execute("SELECT * FROM example_document WHERE track = ? ORDER BY ordinal", (track,))
        ]
    return [_decode(row) for row in connection.execute("SELECT * FROM example_document ORDER BY ordinal")]


def track_counts(connection: sqlite3.Connection) -> dict[str, int]:
    counts = {track: 0 for track in TRACKS}
    for row in connection.execute("SELECT track, COUNT(*) AS n FROM example_document GROUP BY track"):
        counts[row["track"]] = row["n"]
    return counts


def examples_by_phase(connection: sqlite3.Connection, track: str = "") -> list[dict[str, Any]]:
    """One group per ADM phase in cycle order, each with the documents that phase produces
    (optionally one track only: the TOGAF deliverables, the ArchiMate views, the SABSA cells)."""
    names = {
        row["code"]: row["name"] for row in connection.execute("SELECT code, name FROM adm_phase").fetchall()
    }
    groups: dict[str, list[dict[str, Any]]] = {code: [] for code in PHASE_ORDER}
    for example in examples(connection, track):
        groups[example["phase_code"]].append(example)
    return [
        {"code": code, "name": names[code], "examples": documents}
        for code, documents in groups.items()
        if documents
    ]


def phase_examples(connection: sqlite3.Connection, phase_code: str) -> list[dict[str, Any]]:
    return [
        _decode(row)
        for row in connection.execute(
            "SELECT * FROM example_document WHERE phase_code = ? ORDER BY ordinal", (phase_code,)
        )
    ]


def example(connection: sqlite3.Connection, example_id: str) -> dict[str, Any] | None:
    row = connection.execute("SELECT * FROM example_document WHERE id = ?", (example_id,)).fetchone()
    return _decode(row) if row else None


def artefact_rows(connection: sqlite3.Connection, codes: list[str]) -> list[sqlite3.Row]:
    if not codes:
        return []
    placeholders = ",".join("?" for _ in codes)
    return connection.execute(
        f"SELECT code, name, kind, phase_code FROM adm_artefact WHERE code IN ({placeholders}) ORDER BY name", codes
    ).fetchall()


def related(connection: sqlite3.Connection, document: dict[str, Any]) -> list[dict[str, Any]]:
    """Examples of the other tracks that share an artefact or the phase with this one: the TOGAF
    deliverable next to its ArchiMate view next to its SABSA cell, one enterprise throughout."""
    rows = connection.execute(
        "SELECT * FROM example_document WHERE id != ? AND track != ? AND (phase_code = ? OR EXISTS ("
        " SELECT 1 FROM json_each(example_document.artefacts) WHERE value IN (SELECT value FROM json_each(?))))"
        " ORDER BY track, ordinal",
        (document["id"], document["track"], document["phase_code"], orjson.dumps(document["artefacts"]).decode()),
    ).fetchall()
    return [_decode(row) for row in rows]


def neighbours(
    connection: sqlite3.Connection, example_id: str
) -> tuple[dict[str, Any] | None, dict[str, Any] | None]:
    ordered = examples(connection)
    ids = [item["id"] for item in ordered]
    index = ids.index(example_id)
    previous = ordered[index - 1] if index > 0 else None
    following = ordered[index + 1] if index + 1 < len(ordered) else None
    return previous, following
