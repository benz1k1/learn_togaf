"""
Flashcards (learn_togaf.md §4.5): SM-2 scheduling over cards GENERATED from the content cache.

Nothing here is authored twice. A card is ``(card_kind, card_ref)`` where the ref is the stable
content id (§3): a glossary term id, ``<phase>:inputs|outputs|objectives``, a technique code,
an artefact code, a figure id, or a question id. ``rebuild_cards`` inserts a due-now row for
every content item that has none and never deletes learner state, so a content reload adds
cards and a removed term simply stops being rendered (``card_content`` returns ``None``).

The SM-2 step is a pure function so the reference sequences are unit-testable:

- grade < 3: reps → 0, interval → 1 day, lapses + 1
- grade ≥ 3: reps + 1; interval 1, then 6, then ``round(previous × ease)``
- ease += 0.1 − (5 − g) × (0.08 + (5 − g) × 0.02), floored at 1.3, applied on every grade and
  BEFORE the interval is computed (the common SM-2 reading: the new ease schedules the next rep)
"""

import sqlite3
from dataclasses import dataclass
from datetime import UTC, datetime, timedelta
from typing import Any

import orjson

CARD_KINDS = ("TERM", "PHASE_IO", "TECHNIQUE", "ARTEFACT", "FIGURE", "QUESTION")
PHASE_IO_FACETS = (("inputs", "Inputs of"), ("outputs", "Outputs of"), ("objectives", "Objectives of"))
MIN_EASE = 1.3


def iso(moment: datetime) -> str:
    return moment.astimezone(UTC).isoformat(timespec="seconds")


def now_utc() -> datetime:
    return datetime.now(UTC)


# ---------------------------------------------------------------- SM-2 (pure)
@dataclass(frozen=True)
class Sm2State:
    interval_days: float
    ease: float
    reps: int
    lapses: int


def sm2(state: Sm2State, grade: int) -> Sm2State:
    if not 0 <= grade <= 5:
        raise ValueError(f"SM-2 grade must be 0..5, got {grade}")
    ease = max(MIN_EASE, state.ease + 0.1 - (5 - grade) * (0.08 + (5 - grade) * 0.02))
    if grade < 3:
        return Sm2State(interval_days=1.0, ease=ease, reps=0, lapses=state.lapses + 1)
    reps = state.reps + 1
    if reps == 1:
        interval = 1.0
    elif reps == 2:
        interval = 6.0
    else:
        interval = float(round(state.interval_days * ease))
    return Sm2State(interval_days=interval, ease=ease, reps=reps, lapses=state.lapses)


def sm2_sequence(grades: list[int], start: Sm2State | None = None) -> list[Sm2State]:
    """Every state after each grade in turn — the shape the reference tests compare against."""
    state = start or Sm2State(0.0, 2.5, 0, 0)
    states = []
    for grade in grades:
        state = sm2(state, grade)
        states.append(state)
    return states


# ---------------------------------------------------------------- card generation
def _content_refs(connection: sqlite3.Connection) -> list[tuple[str, str]]:
    refs: list[tuple[str, str]] = []
    refs += [("TERM", row["id"]) for row in connection.execute("SELECT id FROM glossary_term ORDER BY id")]
    for row in connection.execute("SELECT code FROM adm_phase ORDER BY ordinal"):
        refs += [("PHASE_IO", f"{row['code']}:{facet}") for facet, _ in PHASE_IO_FACETS]
    refs += [
        ("TECHNIQUE", row["code"])
        for row in connection.execute("SELECT code FROM adm_technique ORDER BY code")
    ]
    refs += [
        ("ARTEFACT", row["code"]) for row in connection.execute("SELECT code FROM adm_artefact ORDER BY code")
    ]
    refs += [
        ("FIGURE", row["id"])
        for row in connection.execute("SELECT id FROM source_figure WHERE important = 1 ORDER BY id")
    ]
    return refs


def rebuild_cards(connection: sqlite3.Connection, now: datetime) -> int:
    """Insert a due-now card for every content item without one. Returns how many were added.
    Existing rows (and their SM-2 state) are untouched; callers hold the transaction."""
    added = 0
    due = iso(now)
    for kind, ref in _content_refs(connection):
        cursor = connection.execute(
            "INSERT OR IGNORE INTO card_review(card_kind, card_ref, due_at) VALUES (?, ?, ?)",
            (kind, ref, due),
        )
        added += cursor.rowcount
    return added


def upsert_question_cards(connection: sqlite3.Connection, question_ids: list[str], now: datetime) -> None:
    """Missed questions become QUESTION cards due now; an existing card is pulled forward, its
    ease and history kept. Called by the practice engine on finish."""
    due = iso(now)
    for question_id in question_ids:
        connection.execute(
            "INSERT INTO card_review(card_kind, card_ref, due_at) VALUES ('QUESTION', ?, ?)"
            " ON CONFLICT(card_kind, card_ref) DO UPDATE SET due_at = excluded.due_at",
            (question_id, due),
        )


# ---------------------------------------------------------------- queue
def card_counts(connection: sqlite3.Connection, now: datetime) -> dict[str, int]:
    day_start = now.astimezone(UTC).replace(hour=0, minute=0, second=0, microsecond=0)
    row = connection.execute(
        "SELECT COUNT(*) AS total,"
        " SUM(CASE WHEN due_at <= ? THEN 1 ELSE 0 END) AS due,"
        " SUM(CASE WHEN last_reviewed_at >= ? THEN 1 ELSE 0 END) AS reviewed_today"
        " FROM card_review",
        (iso(now), iso(day_start)),
    ).fetchone()
    return {"total": row["total"], "due": row["due"] or 0, "reviewed_today": row["reviewed_today"] or 0}


def kind_counts(connection: sqlite3.Connection, now: datetime) -> list[dict[str, Any]]:
    rows = connection.execute(
        "SELECT card_kind, COUNT(*) AS total, SUM(CASE WHEN due_at <= ? THEN 1 ELSE 0 END) AS due"
        " FROM card_review GROUP BY card_kind",
        (iso(now),),
    ).fetchall()
    by_kind = {row["card_kind"]: row for row in rows}
    return [
        {
            "kind": kind,
            "total": by_kind[kind]["total"] if kind in by_kind else 0,
            "due": (by_kind[kind]["due"] or 0) if kind in by_kind else 0,
        }
        for kind in CARD_KINDS
    ]


def next_due_card(connection: sqlite3.Connection, now: datetime) -> sqlite3.Row | None:
    """The most overdue card whose content still exists. A card for content that has been
    removed is skipped, never deleted."""
    rows = connection.execute(
        "SELECT * FROM card_review WHERE due_at <= ? ORDER BY due_at, id LIMIT 50", (iso(now),)
    ).fetchall()
    for row in rows:
        if card_content(connection, row) is not None:
            return row
    return None


def get_card(connection: sqlite3.Connection, card_id: int) -> sqlite3.Row | None:
    return connection.execute("SELECT * FROM card_review WHERE id = ?", (card_id,)).fetchone()


def grade_card(connection: sqlite3.Connection, card: sqlite3.Row, grade: int, now: datetime) -> Sm2State:
    state = sm2(Sm2State(card["interval_days"], card["ease"], card["reps"], card["lapses"]), grade)
    due_at = now + timedelta(days=state.interval_days)
    connection.execute(
        "UPDATE card_review SET due_at = ?, interval_days = ?, ease = ?, reps = ?, lapses = ?, last_grade = ?,"
        " last_reviewed_at = ? WHERE id = ?",
        (iso(due_at), state.interval_days, state.ease, state.reps, state.lapses, grade, iso(now), card["id"]),
    )
    return state


# ---------------------------------------------------------------- card content
def _loads(value: str | None) -> Any:
    return orjson.loads(value) if value else []


def card_content(connection: sqlite3.Connection, card: sqlite3.Row) -> dict[str, Any] | None:
    """Front/back for one card, resolved from the content cache. ``None`` if the content is gone.

    Returned keys: kind, ref, title, front (text), front_image (figure cards), back_lines
    (list of text), back_note (subtitle), link (where to read more)."""
    kind, ref = card["card_kind"], card["card_ref"]
    if kind == "TERM":
        return _term_card(connection, ref)
    if kind == "PHASE_IO":
        return _phase_io_card(connection, ref)
    if kind == "TECHNIQUE":
        return _technique_card(connection, ref)
    if kind == "ARTEFACT":
        return _artefact_card(connection, ref)
    if kind == "FIGURE":
        return _figure_card(connection, ref)
    if kind == "QUESTION":
        return _question_card(connection, ref)
    raise ValueError(f"unknown card kind {kind!r}")


def _term_card(connection: sqlite3.Connection, ref: str) -> dict[str, Any] | None:
    row = connection.execute("SELECT * FROM glossary_term WHERE id = ?", (ref,)).fetchone()
    if row is None:
        return None
    confusable = _loads(row["confusable_with"])
    names = []
    for other in confusable:
        other_row = connection.execute("SELECT term FROM glossary_term WHERE id = ?", (other,)).fetchone()
        names.append(other_row["term"] if other_row else other)
    return {
        "kind": "TERM",
        "ref": ref,
        "title": "Define the term",
        "front": row["term"],
        "front_image": None,
        "back_lines": [row["definition"]],
        "back_note": f"{row['document']} §{row['section']}"
        + (f" · confusable with: {', '.join(names)}" if names else ""),
        "link": f"/glossary/{ref}",
    }


def _phase_io_card(connection: sqlite3.Connection, ref: str) -> dict[str, Any] | None:
    code, _, facet = ref.partition(":")
    labels = dict(PHASE_IO_FACETS)
    if facet not in labels:
        raise ValueError(f"PHASE_IO card ref {ref!r} must be <phase>:inputs|outputs|objectives")
    row = connection.execute("SELECT * FROM adm_phase WHERE code = ?", (code,)).fetchone()
    if row is None:
        return None
    column = "objective" if facet == "objectives" else facet
    return {
        "kind": "PHASE_IO",
        "ref": ref,
        "title": f"ADM · {facet}",
        "front": f"{labels[facet]} {row['name']}?",
        "front_image": None,
        "back_lines": _loads(row[column]),
        "back_note": row["name"],
        "link": f"/adm/{code}",
    }


def _technique_card(connection: sqlite3.Connection, ref: str) -> dict[str, Any] | None:
    row = connection.execute("SELECT * FROM adm_technique WHERE code = ?", (ref,)).fetchone()
    if row is None:
        return None
    phases = _loads(row["phases"])
    return {
        "kind": "TECHNIQUE",
        "ref": ref,
        "title": "Technique → purpose and phases",
        "front": row["name"],
        "front_image": None,
        "back_lines": [row["purpose"]],
        "back_note": f"Used in: {', '.join(phases) if phases else 'no phase recorded'}",
        "link": f"/adm/technique/{ref}",
    }


def _artefact_card(connection: sqlite3.Connection, ref: str) -> dict[str, Any] | None:
    row = connection.execute("SELECT * FROM adm_artefact WHERE code = ?", (ref,)).fetchone()
    if row is None:
        return None
    return {
        "kind": "ARTEFACT",
        "ref": ref,
        "title": "Artefact → phase, kind, domain",
        "front": row["name"],
        "front_image": None,
        "back_lines": [
            f"Phase {row['phase_code']}",
            f"{row['kind'].title()} · {row['domain'].title()} domain",
        ],
        "back_note": row["purpose"],
        "link": f"/artefact#{ref}",
    }


def _figure_card(connection: sqlite3.Connection, ref: str) -> dict[str, Any] | None:
    row = connection.execute(
        "SELECT f.*, s.heading_path FROM source_figure f LEFT JOIN source_section s ON s.id = f.section_id WHERE f.id = ?",
        (ref,),
    ).fetchone()
    if row is None:
        return None
    return {
        "kind": "FIGURE",
        "ref": ref,
        "title": "What does this figure show?",
        "front": "",
        "front_image": f"/figure/{ref}",
        "back_lines": [row["caption"]],
        "back_note": row["heading_path"] or row["document_code"],
        "link": f"/source/{row['section_id']}" if row["section_id"] else "/source",
    }


def _question_card(connection: sqlite3.Connection, ref: str) -> dict[str, Any] | None:
    row = connection.execute("SELECT * FROM question WHERE id = ?", (ref,)).fetchone()
    if row is None:
        return None
    best = connection.execute(
        "SELECT * FROM question_option WHERE question_id = ? ORDER BY points DESC, ordinal LIMIT 1", (ref,)
    ).fetchone()
    front = row["stem_or_scenario"]
    if row["scoring"] == "gradient":
        front = f"{row['stem_or_scenario']}\n\n**{row['question_text']}**"
    explanation = row["explanation"] or (best["why"] if best else "")
    return {
        "kind": "QUESTION",
        "ref": ref,
        "title": f"Missed question · {row['unit_code']} · {row['objective_code']}",
        "front": front,
        "front_image": f"/figure/{row['figure_id']}" if row["figure_id"] else None,
        "back_lines": [f"{best['key']}. {best['text']}" if best else "(no options)", explanation],
        "back_note": ", ".join(_loads(row["refs"])),
        "link": None,
    }
