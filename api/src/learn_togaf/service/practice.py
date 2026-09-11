"""
Practice engine (learn_togaf.md §0, §4.6): one engine for DRILL, FOUNDATION_MOCK and
PRACTITIONER_MOCK.

Draws are seeded (``random.Random(seed)`` over a sorted candidate list) and the drawn ids are
stored on the attempt in order, so a retake with the same seed is the same paper. The clock is
``started_at + time_limit_s`` on the row: a reload asks the server how much is left and an
answer after the deadline is refused (``AttemptClosed``) and the attempt auto-finished.

Scoring follows §0 exactly: Foundation 1/0 per option, Practitioner the option's 5/3/1/0;
mocks are out of 40 with the blueprint pass mark; a drill has no pass mark (``passed`` NULL).
"""

import random
import sqlite3
from dataclasses import dataclass, field
from datetime import UTC, datetime, timedelta
from typing import Any

import orjson

from learn_togaf.config import CONTENT_DIR
from learn_togaf.content.loader import load_blueprint
from learn_togaf.service.review import iso, upsert_question_cards

MODES = ("DRILL", "FOUNDATION_MOCK", "PRACTITIONER_MOCK")
SOURCE_FILTERS = {
    "all": None,
    "own": ("authored", "generated"),
    "imported": ("imported",),
}
MOCK_QUESTION_CARD_THRESHOLD = {"FOUNDATION": 1, "PRACTITIONER": 5}
PRACTITIONER_MOCK_UNITS = ("P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8")


class DrawError(ValueError):
    """The filters match no questions; the learner is told, nothing is created."""


class AttemptClosed(ValueError):
    """The clock ran out or the attempt is finished; the answer was not recorded."""


@dataclass
class Draw:
    exam: str
    mode: str  # DRILL | MOCK (attempt.mode)
    question_ids: list[str]
    seed: int
    time_limit_s: int | None
    filters: dict[str, Any] = field(default_factory=dict)
    short_units: list[str] = field(default_factory=list)


def _blueprint():
    return load_blueprint(CONTENT_DIR)


def new_seed() -> int:
    return random.SystemRandom().randrange(1, 2**31 - 1)


def _shuffled(ids: list[str], rng: random.Random) -> list[str]:
    ordered = sorted(ids)
    rng.shuffle(ordered)
    return ordered


# ---------------------------------------------------------------- draws
def draw_drill(
    connection: sqlite3.Connection,
    exam: str,
    units: list[str],
    objectives: list[str],
    count: int,
    include_drafts: bool,
    sources: str,
    seed: int,
) -> Draw:
    if sources not in SOURCE_FILTERS:
        raise DrawError(f"unknown sources filter {sources!r}")
    if count < 1:
        raise DrawError("a drill needs at least one question")
    sql = "SELECT id FROM question WHERE exam = ?"
    params: list[Any] = [exam]
    if units:
        sql += f" AND unit_code IN ({','.join('?' * len(units))})"
        params += units
    if objectives:
        sql += f" AND objective_code IN ({','.join('?' * len(objectives))})"
        params += objectives
    if not include_drafts:
        sql += " AND status = 'reviewed'"
    allowed = SOURCE_FILTERS[sources]
    if allowed:
        sql += f" AND source IN ({','.join('?' * len(allowed))})"
        params += list(allowed)
    candidates = [row["id"] for row in connection.execute(sql, params)]
    if not candidates:
        raise DrawError("no questions match those filters — widen the units or include drafts")
    rng = random.Random(seed)
    ids = _shuffled(candidates, rng)[:count]
    filters = {
        "units": units,
        "objectives": objectives,
        "count": count,
        "include_drafts": include_drafts,
        "sources": sources,
    }
    return Draw(exam=exam, mode="DRILL", question_ids=ids, seed=seed, time_limit_s=None, filters=filters)


def draw_phase_io_drill(connection: sqlite3.Connection, phase_code: str, count: int, seed: int) -> Draw:
    """Best effort (§4.5 → §4.6 link from the ADM explorer): Foundation questions in unit F4
    about inputs/outputs, narrowed to the phase when any question names it (tag ``phase-a`` or
    the phase name in the stem); otherwise every F4 input/output question."""
    phase = connection.execute("SELECT code, name FROM adm_phase WHERE code = ?", (phase_code,)).fetchone()
    if phase is None:
        raise DrawError(f"unknown ADM phase {phase_code!r}")
    io_sql = (
        "SELECT id, stem_or_scenario, tags FROM question WHERE exam = 'FOUNDATION' AND unit_code = 'F4'"
        " AND (tags LIKE '%\"inputs\"%' OR tags LIKE '%\"outputs\"%'"
        " OR stem_or_scenario LIKE '%input%' OR stem_or_scenario LIKE '%output%')"
    )
    rows = connection.execute(io_sql).fetchall()
    if not rows:
        raise DrawError("no Foundation questions about phase inputs and outputs yet")
    short_name = phase["name"].split(":")[0]  # "Phase A: Architecture Vision" → "Phase A"
    tag = f"phase-{phase_code.lower()}"
    matching = [
        row["id"]
        for row in rows
        if tag in orjson.loads(row["tags"]) or short_name.lower() in row["stem_or_scenario"].lower()
    ]
    candidates = matching or [row["id"] for row in rows]
    rng = random.Random(seed)
    ids = _shuffled(candidates, rng)[:count]
    filters = {"phase": phase_code, "kind": "io", "phase_specific": bool(matching), "count": count}
    return Draw(
        exam="FOUNDATION", mode="DRILL", question_ids=ids, seed=seed, time_limit_s=None, filters=filters
    )


def _unit_pool(connection: sqlite3.Connection, exam: str, unit: str, status: str) -> list[str]:
    return [
        row["id"]
        for row in connection.execute(
            "SELECT id FROM question WHERE exam = ? AND unit_code = ? AND status = ?", (exam, unit, status)
        )
    ]


def _take_for_unit(
    connection: sqlite3.Connection, exam: str, unit: str, need: int, rng: random.Random
) -> tuple[list[str], bool]:
    """Reviewed questions first; drafts only to make up the number. Returns (ids, short) where
    short means drafts were needed or the unit still lacks questions."""
    chosen = _shuffled(_unit_pool(connection, exam, unit, "reviewed"), rng)[:need]
    short = len(chosen) < need
    if short:
        drafts = _shuffled(_unit_pool(connection, exam, unit, "draft"), rng)
        chosen += drafts[: need - len(chosen)]
    return chosen, short


def draw_foundation_mock(connection: sqlite3.Connection, seed: int) -> Draw:
    """Exactly the blueprint weight per Foundation unit from reviewed questions. A unit without
    enough reviewed questions is filled from drafts and named in ``short_units`` so the attempt
    carries a warning — the paper is never silently smaller than the blueprint."""
    blueprint = _blueprint()
    rng = random.Random(seed)
    ids: list[str] = []
    short_units: list[str] = []
    units = connection.execute(
        "SELECT code, weight FROM learning_unit WHERE exam = 'FOUNDATION' AND weight > 0 ORDER BY ordinal"
    ).fetchall()
    for unit in units:
        chosen, short = _take_for_unit(connection, "FOUNDATION", unit["code"], unit["weight"], rng)
        ids += chosen
        if short:
            short_units.append(unit["code"])
    if not ids:
        raise DrawError("the Foundation bank is empty — load or import questions first")
    rng.shuffle(ids)
    return Draw(
        exam="FOUNDATION",
        mode="MOCK",
        question_ids=ids,
        seed=seed,
        time_limit_s=blueprint.foundation.time_minutes * 60,
        filters={"short_units": short_units} if short_units else {},
        short_units=short_units,
    )


def draw_practitioner_mock(connection: sqlite3.Connection, seed: int) -> Draw:
    """Eight scenarios across P1–P8: one per unit where possible (reviewed first), then the
    remaining slots filled from whatever Practitioner questions are left."""
    blueprint = _blueprint()
    rng = random.Random(seed)
    ids: list[str] = []
    short_units: list[str] = []
    for unit in PRACTITIONER_MOCK_UNITS:
        chosen, short = _take_for_unit(connection, "PRACTITIONER", unit, 1, rng)
        ids += chosen
        if short:
            short_units.append(unit)
    target = blueprint.practitioner.questions
    if len(ids) < target:
        rest = [
            row["id"]
            for row in connection.execute(
                "SELECT id FROM question WHERE exam = 'PRACTITIONER' ORDER BY CASE status WHEN 'reviewed' THEN 0 ELSE 1 END, id"
            )
            if row["id"] not in ids
        ]
        ids += _shuffled(rest, rng)[: target - len(ids)]
    if not ids:
        raise DrawError("the Practitioner bank is empty — load or import scenarios first")
    rng.shuffle(ids)
    return Draw(
        exam="PRACTITIONER",
        mode="MOCK",
        question_ids=ids,
        seed=seed,
        time_limit_s=blueprint.practitioner.time_minutes * 60,
        filters={"short_units": short_units} if short_units else {},
        short_units=short_units,
    )


# ---------------------------------------------------------------- attempts
def create_attempt(connection: sqlite3.Connection, draw: Draw, now: datetime) -> int:
    cursor = connection.execute(
        "INSERT INTO attempt(exam, mode, set_code, seed, question_ids, started_at, time_limit_s, filters)"
        " VALUES (?, ?, NULL, ?, ?, ?, ?, ?)",
        (
            draw.exam,
            draw.mode,
            draw.seed,
            orjson.dumps(draw.question_ids).decode(),
            iso(now),
            draw.time_limit_s,
            orjson.dumps(draw.filters).decode(),
        ),
    )
    if cursor.lastrowid is None:
        raise ValueError("attempt insert returned no row id")
    attempt_id = int(cursor.lastrowid)
    for question_id in draw.question_ids:
        connection.execute(
            "INSERT INTO attempt_answer(attempt_id, question_id) VALUES (?, ?)", (attempt_id, question_id)
        )
    return attempt_id


def get_attempt(connection: sqlite3.Connection, attempt_id: int) -> sqlite3.Row | None:
    return connection.execute("SELECT * FROM attempt WHERE id = ?", (attempt_id,)).fetchone()


def question_ids(attempt: sqlite3.Row) -> list[str]:
    return orjson.loads(attempt["question_ids"])


def attempt_filters(attempt: sqlite3.Row) -> dict[str, Any]:
    return orjson.loads(attempt["filters"] or "{}")


def mode_label(attempt: sqlite3.Row) -> str:
    if attempt["mode"] == "DRILL":
        return "DRILL"
    return f"{attempt['exam']}_MOCK"


def open_book_allowed(attempt: sqlite3.Row) -> bool:
    """Part 1 is closed book; anything Practitioner has the standard open (§0)."""
    return attempt["exam"] == "PRACTITIONER"


def parse_iso(value: str) -> datetime:
    return datetime.fromisoformat(value)


def remaining_seconds(attempt: sqlite3.Row, now: datetime) -> int | None:
    """Seconds left on the clock; ``None`` for an untimed drill; never negative."""
    if attempt["time_limit_s"] is None:
        return None
    deadline = parse_iso(attempt["started_at"]) + timedelta(seconds=attempt["time_limit_s"])
    return max(0, int((deadline - now).total_seconds()))


def is_expired(attempt: sqlite3.Row, now: datetime) -> bool:
    remaining = remaining_seconds(attempt, now)
    return remaining is not None and remaining <= 0


def answers_by_question(connection: sqlite3.Connection, attempt_id: int) -> dict[str, sqlite3.Row]:
    rows = connection.execute("SELECT * FROM attempt_answer WHERE attempt_id = ?", (attempt_id,)).fetchall()
    return {row["question_id"]: row for row in rows}


def question_with_options(connection: sqlite3.Connection, question_id: str) -> dict[str, Any]:
    question = connection.execute("SELECT * FROM question WHERE id = ?", (question_id,)).fetchone()
    if question is None:
        raise ValueError(f"question {question_id} is not in the content cache")
    options = connection.execute(
        "SELECT * FROM question_option WHERE question_id = ? ORDER BY ordinal", (question_id,)
    ).fetchall()
    max_points = max(option["points"] for option in options)
    return {
        "question": question,
        "options": options,
        "max_points": max_points,
        "correct_key": next(option["key"] for option in options if option["points"] == max_points),
        "refs": orjson.loads(question["refs"] or "[]"),
        "tags": orjson.loads(question["tags"] or "[]"),
    }


def record_answer(
    connection: sqlite3.Connection,
    attempt: sqlite3.Row,
    question_id: str,
    key: str,
    seconds: int,
    now: datetime,
) -> dict[str, Any]:
    """Store the chosen option and its points. In a mock an answer can be changed until finish;
    a drill locks each question once answered (the explanation is already on screen).
    Raises AttemptClosed after finish or when the clock has run out (caller auto-finishes)."""
    if attempt["finished_at"]:
        raise AttemptClosed("this attempt is finished")
    if is_expired(attempt, now):
        raise AttemptClosed("time is up")
    if question_id not in question_ids(attempt):
        raise ValueError(f"question {question_id} is not part of attempt {attempt['id']}")
    option = connection.execute(
        "SELECT points FROM question_option WHERE question_id = ? AND key = ?", (question_id, key)
    ).fetchone()
    if option is None:
        raise ValueError(f"option {key!r} is not an option of {question_id}")
    previous = connection.execute(
        "SELECT * FROM attempt_answer WHERE attempt_id = ? AND question_id = ?", (attempt["id"], question_id)
    ).fetchone()
    if attempt["mode"] == "DRILL" and previous is not None and previous["chosen_key"] is not None:
        raise AttemptClosed("already answered — a drill shows the explanation, so the answer is locked")
    max_points = connection.execute(
        "SELECT MAX(points) AS m FROM question_option WHERE question_id = ?", (question_id,)
    ).fetchone()["m"]
    changed_from_correct = previous["changed_from_correct"] if previous else 0
    if previous is not None and previous["points"] == max_points and option["points"] < max_points:
        changed_from_correct = 1
    connection.execute(
        "UPDATE attempt_answer SET chosen_key = ?, points = ?, answered_at = ?, seconds = COALESCE(seconds, 0) + ?,"
        " changed_from_correct = ? WHERE attempt_id = ? AND question_id = ?",
        (key, option["points"], iso(now), max(0, seconds), changed_from_correct, attempt["id"], question_id),
    )
    return {
        "points": option["points"],
        "max_points": max_points,
        "changed_from_correct": changed_from_correct,
    }


def toggle_flag(connection: sqlite3.Connection, attempt: sqlite3.Row, question_id: str) -> bool:
    row = connection.execute(
        "SELECT flagged FROM attempt_answer WHERE attempt_id = ? AND question_id = ?",
        (attempt["id"], question_id),
    ).fetchone()
    if row is None:
        raise ValueError(f"question {question_id} is not part of attempt {attempt['id']}")
    flagged = 0 if row["flagged"] else 1
    connection.execute(
        "UPDATE attempt_answer SET flagged = ? WHERE attempt_id = ? AND question_id = ?",
        (flagged, attempt["id"], question_id),
    )
    return bool(flagged)


# ---------------------------------------------------------------- scoring
def score_answers(points: list[int | None]) -> int:
    """Unanswered scores 0; nothing else is inferred."""
    return sum(point for point in points if point is not None)


def max_score_for(exam: str, mode: str, question_count: int) -> int:
    if mode == "MOCK":
        blueprint = _blueprint()
        return blueprint.foundation.max_score if exam == "FOUNDATION" else blueprint.practitioner.max_score
    return question_count * MOCK_QUESTION_CARD_THRESHOLD[exam]


def pass_mark_for(exam: str) -> int:
    blueprint = _blueprint()
    return blueprint.foundation.pass_mark if exam == "FOUNDATION" else blueprint.practitioner.pass_mark


def finish_attempt(connection: sqlite3.Connection, attempt: sqlite3.Row, now: datetime) -> sqlite3.Row:
    """Score, pass/fail (mocks only), finished_at, and QUESTION cards for every miss. Idempotent:
    a finished attempt is returned as is."""
    if attempt["finished_at"]:
        return attempt
    ids = question_ids(attempt)
    answers = answers_by_question(connection, attempt["id"])
    score = score_answers([answers[qid]["points"] if qid in answers else None for qid in ids])
    max_score = max_score_for(attempt["exam"], attempt["mode"], len(ids))
    passed = int(score >= pass_mark_for(attempt["exam"])) if attempt["mode"] == "MOCK" else None
    connection.execute(
        "UPDATE attempt SET finished_at = ?, score = ?, max_score = ?, passed = ? WHERE id = ?",
        (iso(now), score, max_score, passed, attempt["id"]),
    )
    threshold = MOCK_QUESTION_CARD_THRESHOLD[attempt["exam"]]
    missed = [qid for qid in ids if qid not in answers or (answers[qid]["points"] or 0) < threshold]
    upsert_question_cards(connection, missed, now)
    refreshed = get_attempt(connection, attempt["id"])
    if refreshed is None:
        raise ValueError(f"attempt {attempt['id']} vanished during finish")
    return refreshed


# ---------------------------------------------------------------- review data
def review_data(connection: sqlite3.Connection, attempt: sqlite3.Row) -> dict[str, Any]:
    ids = question_ids(attempt)
    answers = answers_by_question(connection, attempt["id"])
    items = []
    per_unit: dict[str, dict[str, Any]] = {}
    per_objective: dict[str, dict[str, Any]] = {}
    changed = 0
    for index, question_id in enumerate(ids):
        detail = question_with_options(connection, question_id)
        answer = answers.get(question_id)
        points = answer["points"] if answer and answer["points"] is not None else 0
        chosen = answer["chosen_key"] if answer else None
        changed += answer["changed_from_correct"] if answer else 0
        unit = detail["question"]["unit_code"]
        objective = detail["question"]["objective_code"]
        for bucket, code in ((per_unit, unit), (per_objective, objective)):
            entry = bucket.setdefault(
                code, {"code": code, "score": 0, "max": 0, "questions": 0, "correct": 0}
            )
            entry["score"] += points
            entry["max"] += detail["max_points"]
            entry["questions"] += 1
            entry["correct"] += int(chosen == detail["correct_key"])
        items.append(
            {
                "index": index,
                "number": index + 1,
                "question": detail["question"],
                "options": detail["options"],
                "refs": detail["refs"],
                "correct_key": detail["correct_key"],
                "max_points": detail["max_points"],
                "chosen_key": chosen,
                "points": points,
                "seconds": answer["seconds"] if answer else None,
                "flagged": bool(answer["flagged"]) if answer else False,
                "changed_from_correct": bool(answer["changed_from_correct"]) if answer else False,
                "correct": chosen == detail["correct_key"],
            }
        )
    unit_names = {
        row["code"]: row["name"] for row in connection.execute("SELECT code, name FROM learning_unit")
    }
    objective_texts = {
        row["code"]: row["text"] for row in connection.execute("SELECT code, text FROM objective")
    }
    for entry in per_unit.values():
        entry["name"] = unit_names.get(entry["code"], entry["code"])
    for entry in per_objective.values():
        entry["name"] = objective_texts.get(entry["code"], entry["code"])
    total_seconds = sum(item["seconds"] or 0 for item in items)
    return {
        "items": items,
        "per_unit": sorted(per_unit.values(), key=lambda e: e["code"]),
        "per_objective": sorted(per_objective.values(), key=lambda e: e["code"]),
        "changed_from_correct": changed,
        "total_seconds": total_seconds,
        "answered": sum(1 for item in items if item["chosen_key"]),
        "correct": sum(1 for item in items if item["correct"]),
    }


def recent_attempts(connection: sqlite3.Connection, limit: int = 12) -> list[sqlite3.Row]:
    return connection.execute(
        "SELECT * FROM attempt ORDER BY started_at DESC, id DESC LIMIT ?", (limit,)
    ).fetchall()


def units_for_form(connection: sqlite3.Connection) -> list[dict[str, Any]]:
    units = connection.execute(
        "SELECT code, exam, name, weight FROM learning_unit WHERE code NOT LIKE 'G_%' ORDER BY ordinal"
    ).fetchall()
    counts = {
        (row["unit_code"], row["status"]): row["n"]
        for row in connection.execute(
            "SELECT unit_code, status, COUNT(*) AS n FROM question GROUP BY unit_code, status"
        )
    }
    result = []
    for unit in units:
        objectives = connection.execute(
            "SELECT code, text FROM objective WHERE unit_code = ? ORDER BY ordinal", (unit["code"],)
        ).fetchall()
        result.append(
            {
                "code": unit["code"],
                "exam": unit["exam"],
                "name": unit["name"],
                "weight": unit["weight"],
                "reviewed": counts.get((unit["code"], "reviewed"), 0),
                "drafts": counts.get((unit["code"], "draft"), 0),
                "objectives": objectives,
            }
        )
    return result


def utc_now() -> datetime:
    return datetime.now(UTC)
