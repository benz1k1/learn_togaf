"""
Units, lessons, progress and the "check yourself" drill (learn_togaf.md §4.2).

Check-yourself answers are recorded like any other answer: one attempt per lesson with
``mode = 'CHECK'`` and ``set_code NULL`` (``filters`` names the lesson), so the dashboard's
readiness estimate and the weakest-objective list see them. A wrong answer seeds a QUESTION
flashcard due now.
"""

import random
import re
import sqlite3
from datetime import UTC, datetime
from typing import Any

import orjson
from markupsafe import Markup

from learn_togaf.content.models import MAX_POINTS

PROGRESS_STATES = ("READ", "CHECKED", "MASTERED")
CHECK_QUESTIONS = 5


def _now_iso() -> str:
    return datetime.now(UTC).isoformat(timespec="seconds")


def units_by_exam(connection: sqlite3.Connection) -> list[dict[str, Any]]:
    """Units grouped by exam, each with its lesson count and how many are read/checked/mastered."""
    rows = connection.execute(
        """
        SELECT u.code, u.exam, u.track, u.name, u.weight, u.ordinal,
               COUNT(l.id) AS lesson_count,
               SUM(CASE WHEN p.lesson_id IS NOT NULL THEN 1 ELSE 0 END) AS done_count
        FROM learning_unit u
        LEFT JOIN lesson l ON l.unit_code = u.code
        LEFT JOIN lesson_progress p ON p.lesson_id = l.id
        GROUP BY u.code ORDER BY u.ordinal
        """
    ).fetchall()
    groups: dict[tuple[str, str], list[dict[str, Any]]] = {}
    for row in rows:
        groups.setdefault((row["track"], row["exam"]), []).append(dict(row))
    return [
        {"track": track, "exam": exam, "units": units} for (track, exam), units in groups.items()
    ]


def unit_detail(connection: sqlite3.Connection, code: str) -> dict[str, Any] | None:
    unit = connection.execute("SELECT * FROM learning_unit WHERE code = ?", (code,)).fetchone()
    if unit is None:
        return None
    objectives = connection.execute(
        "SELECT code, text FROM objective WHERE unit_code = ? ORDER BY ordinal", (code,)
    ).fetchall()
    lessons = connection.execute(
        """
        SELECT l.id, l.title, l.reading_minutes, l.ordinal, l.status, p.state, p.updated_at
        FROM lesson l LEFT JOIN lesson_progress p ON p.lesson_id = l.id
        WHERE l.unit_code = ? ORDER BY l.ordinal
        """,
        (code,),
    ).fetchall()
    return {"unit": unit, "objectives": objectives, "lessons": lessons}


def lesson_detail(connection: sqlite3.Connection, lesson_id: str) -> dict[str, Any] | None:
    lesson = connection.execute("SELECT * FROM lesson WHERE id = ?", (lesson_id,)).fetchone()
    if lesson is None:
        return None
    unit = connection.execute("SELECT * FROM learning_unit WHERE code = ?", (lesson["unit_code"],)).fetchone()
    objectives = connection.execute(
        """
        SELECT o.code, o.text FROM lesson_objective lo JOIN objective o ON o.code = lo.objective_code
        WHERE lo.lesson_id = ? ORDER BY o.ordinal
        """,
        (lesson_id,),
    ).fetchall()
    ordered = connection.execute(
        """
        SELECT l.id, l.title FROM lesson l JOIN learning_unit u ON u.code = l.unit_code
        ORDER BY u.ordinal, l.ordinal
        """
    ).fetchall()
    index = next(i for i, row in enumerate(ordered) if row["id"] == lesson_id)
    progress = connection.execute(
        "SELECT state FROM lesson_progress WHERE lesson_id = ?", (lesson_id,)
    ).fetchone()
    return {
        "lesson": lesson,
        "unit": unit,
        "objectives": objectives,
        "refs": orjson.loads(lesson["refs"]),
        "prev": ordered[index - 1] if index > 0 else None,
        "next": ordered[index + 1] if index + 1 < len(ordered) else None,
        "state": progress["state"] if progress else None,
    }


_TAG_SPLIT = re.compile(r"(<[^>]+>)")


def _term_pattern(term: str) -> re.Pattern[str]:
    return re.compile(r"(?<![\w-])" + re.escape(term) + r"(?![\w-])", re.IGNORECASE)


def _link_text(text: str, remaining: list[tuple[str, str]]) -> str:
    """Link the first occurrence of the first (longest) remaining term in ``text``, then recurse on both sides
    so no other term is linked inside the anchor just made."""
    for term_id, term in remaining:
        match = _term_pattern(term).search(text)
        if match is None:
            continue
        remaining.remove((term_id, term))
        link = f'<a class="link link-primary" href="/glossary/{term_id}">{match.group(0)}</a>'
        return (
            _link_text(text[: match.start()], remaining) + link + _link_text(text[match.end() :], remaining)
        )
    return text


def autolink_terms(html: str, terms: list[tuple[str, str]]) -> Markup:
    """Link the first occurrence of each glossary term in rendered HTML: text nodes only, never inside an
    existing anchor or a code span, case-insensitive, longest term first."""
    remaining = sorted(terms, key=lambda pair: -len(pair[1]))
    parts = _TAG_SPLIT.split(html)
    skip_depth = 0
    for index, part in enumerate(parts):
        if part.startswith("<"):
            tag = part[1:].lstrip("/").split(maxsplit=1)[0].rstrip(">").lower()
            if tag in ("a", "code", "pre"):
                skip_depth += -1 if part.startswith("</") else 1
            continue
        if skip_depth > 0 or not remaining or not part.strip():
            continue
        parts[index] = _link_text(part, remaining)
    return Markup("".join(parts))


def glossary_terms(connection: sqlite3.Connection) -> list[tuple[str, str]]:
    return [
        (row["id"], row["term"])
        for row in connection.execute("SELECT id, term FROM glossary_term").fetchall()
    ]


def auto_read(connection: sqlite3.Connection, lesson_id: str) -> None:
    """Mark READ on open, without downgrading CHECKED or MASTERED."""
    connection.execute(
        "INSERT INTO lesson_progress(lesson_id, state, updated_at) VALUES (?, 'READ', ?) ON CONFLICT(lesson_id) DO NOTHING",
        (lesson_id, _now_iso()),
    )


def mark_progress(connection: sqlite3.Connection, lesson_id: str, state: str) -> None:
    if state not in PROGRESS_STATES:
        raise ValueError(f"lesson progress state must be one of {PROGRESS_STATES}, got {state!r}")
    connection.execute(
        """
        INSERT INTO lesson_progress(lesson_id, state, updated_at) VALUES (?, ?, ?)
        ON CONFLICT(lesson_id) DO UPDATE SET state = excluded.state, updated_at = excluded.updated_at
        """,
        (lesson_id, state, _now_iso()),
    )


def check_questions(
    connection: sqlite3.Connection, lesson_id: str, count: int = CHECK_QUESTIONS
) -> dict[str, Any]:
    """Up to ``count`` random questions for THIS lesson that the learner has not answered yet.

    The pool is ``lesson_question`` (one lesson per question, built by the loader), so a question
    is never offered by two lessons. A question answered in any lesson check, right or wrong, is
    out for good: a wrong answer already seeded a flashcard, and drills on /practice re-ask
    everything. Drafts are included. Returns the questions plus the mapped and remaining counts
    so the fragment can say when the lesson is exhausted."""
    rows = connection.execute(
        """
        SELECT q.* FROM lesson_question lq JOIN question q ON q.id = lq.question_id
        WHERE lq.lesson_id = ?
          AND q.id NOT IN (
              SELECT aa.question_id FROM attempt_answer aa JOIN attempt a ON a.id = aa.attempt_id
              WHERE a.mode = 'CHECK' AND aa.chosen_key IS NOT NULL
          )
        """,
        (lesson_id,),
    ).fetchall()
    mapped = connection.execute(
        "SELECT COUNT(*) FROM lesson_question WHERE lesson_id = ?", (lesson_id,)
    ).fetchone()[0]
    result = []
    for question in random.sample(rows, min(count, len(rows))):
        options = connection.execute(
            "SELECT key, text FROM question_option WHERE question_id = ? ORDER BY ordinal", (question["id"],)
        ).fetchall()
        result.append({"question": question, "options": options})
    return {"questions": result, "mapped": mapped, "remaining": len(rows)}


def _check_attempt(connection: sqlite3.Connection, lesson_id: str, exam: str) -> sqlite3.Row:
    row = connection.execute(
        "SELECT * FROM attempt WHERE mode = 'CHECK' AND json_extract(filters, '$.lesson') = ?", (lesson_id,)
    ).fetchone()
    if row is not None:
        return row
    connection.execute(
        "INSERT INTO attempt(exam, mode, set_code, seed, question_ids, started_at, filters) VALUES (?, 'CHECK', NULL, ?, '[]', ?, ?)",
        (exam, random.randint(1, 2**31 - 1), _now_iso(), orjson.dumps({"lesson": lesson_id}).decode()),
    )
    return connection.execute(
        "SELECT * FROM attempt WHERE mode = 'CHECK' AND json_extract(filters, '$.lesson') = ?", (lesson_id,)
    ).fetchone()


def record_check_answer(
    connection: sqlite3.Connection, lesson_id: str, question_id: str, key: str
) -> dict[str, Any]:
    question = connection.execute("SELECT * FROM question WHERE id = ?", (question_id,)).fetchone()
    if question is None:
        raise ValueError(f"unknown question {question_id}")
    options = connection.execute(
        "SELECT key, text, points, why FROM question_option WHERE question_id = ? ORDER BY ordinal",
        (question_id,),
    ).fetchall()
    chosen = next((option for option in options if option["key"] == key), None)
    if chosen is None:
        raise ValueError(f"question {question_id} has no option {key!r}")
    max_points = MAX_POINTS[question["scoring"]]
    correct = chosen["points"] == max_points
    now = _now_iso()
    attempt = _check_attempt(connection, lesson_id, question["exam"])
    ids = orjson.loads(attempt["question_ids"])
    if question_id not in ids:
        ids.append(question_id)
        connection.execute(
            "UPDATE attempt SET question_ids = ? WHERE id = ?", (orjson.dumps(ids).decode(), attempt["id"])
        )
    connection.execute(
        """
        INSERT INTO attempt_answer(attempt_id, question_id, chosen_key, points, answered_at)
        VALUES (?, ?, ?, ?, ?)
        ON CONFLICT(attempt_id, question_id) DO UPDATE
        SET chosen_key = excluded.chosen_key, points = excluded.points, answered_at = excluded.answered_at
        """,
        (attempt["id"], question_id, key, chosen["points"], now),
    )
    if not correct:
        connection.execute(
            """
            INSERT INTO card_review(card_kind, card_ref, due_at) VALUES ('QUESTION', ?, ?)
            ON CONFLICT(card_kind, card_ref) DO UPDATE SET due_at = excluded.due_at
            """,
            (question_id, now),
        )
    best = max(options, key=lambda option: option["points"])
    return {
        "question": question,
        "options": options,
        "chosen": chosen,
        "best": best,
        "correct": correct,
        "points": chosen["points"],
        "max_points": max_points,
    }
