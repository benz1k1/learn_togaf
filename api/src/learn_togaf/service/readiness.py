"""
Readiness maths for the dashboard (learn_togaf.md §4.1; learn_sabsa_archimate.md §4.7): one
estimate per exam in the blueprint.

A single-answer exam is estimated from the last 200 answers to its questions: per-unit accuracy
weighted by the blueprint weight of that unit, scaled to the exam's ``max_score``. A gradient
exam is the mean score of the last three finished mocks of it. Both are ``None`` when there is
nothing to estimate from, and the summary line says so rather than printing 0/40.
"""

import sqlite3
from datetime import UTC, date, datetime
from typing import Any

import orjson

from learn_togaf.config import CONTENT_DIR
from learn_togaf.content.loader import load_blueprint
from learn_togaf.content.models import Blueprint, ExamFormat

RECENT_ANSWERS = 200
RECENT_MOCKS = 3


def _now_iso() -> str:
    return datetime.now(UTC).isoformat(timespec="seconds")


def recent_answers(
    connection: sqlite3.Connection, exam: str, limit: int = RECENT_ANSWERS
) -> list[sqlite3.Row]:
    return connection.execute(
        """
        SELECT aa.question_id, aa.points, q.unit_code, q.objective_code
        FROM attempt_answer aa
        JOIN attempt a ON a.id = aa.attempt_id
        JOIN question q ON q.id = aa.question_id
        WHERE q.exam = ? AND aa.answered_at IS NOT NULL AND aa.chosen_key IS NOT NULL
        ORDER BY aa.answered_at DESC
        LIMIT ?
        """,
        (exam, limit),
    ).fetchall()


def exam_units(connection: sqlite3.Connection, exam: ExamFormat) -> list[sqlite3.Row]:
    """The units an exam's readiness table lists: its own units, plus (for a gradient exam whose
    scenarios attach to another exam's units, as OGA-032 does to A1–A9) any unit of the track
    that carries its questions."""
    return connection.execute(
        """
        SELECT code, name, weight, ordinal FROM learning_unit
        WHERE exam = ? OR (track = ? AND EXISTS (SELECT 1 FROM question q WHERE q.unit_code = learning_unit.code AND q.exam = ?))
        ORDER BY ordinal
        """,
        (exam.code, exam.track, exam.code),
    ).fetchall()


def unit_readiness(connection: sqlite3.Connection, exam: ExamFormat) -> list[dict[str, Any]]:
    """Per unit: answered, earned/max points, accuracy (None without answers), blueprint weight."""
    earned: dict[str, int] = {}
    answered: dict[str, int] = {}
    for row in recent_answers(connection, exam.code):
        answered[row["unit_code"]] = answered.get(row["unit_code"], 0) + 1
        earned[row["unit_code"]] = earned.get(row["unit_code"], 0) + (row["points"] or 0)
    result = []
    for unit in exam_units(connection, exam):
        count = answered.get(unit["code"], 0)
        accuracy = earned.get(unit["code"], 0) / (count * exam.max_points) if count else None
        result.append(
            {
                "code": unit["code"],
                "name": unit["name"],
                "weight": unit["weight"],
                "answered": count,
                "accuracy": accuracy,
                "estimate": round(accuracy * unit["weight"], 1)
                if accuracy is not None and unit["weight"]
                else None,
            }
        )
    return result


def weighted_estimate(units: list[dict[str, Any]], max_score: int) -> int | None:
    """Weighted accuracy over the units that have answers, scaled to the exam's max score."""
    weighted = [
        (unit["weight"], unit["accuracy"])
        for unit in units
        if unit["accuracy"] is not None and unit["weight"]
    ]
    if not weighted:
        return None
    total_weight = sum(weight for weight, _ in weighted)
    accuracy = sum(weight * acc for weight, acc in weighted) / total_weight
    return round(accuracy * max_score)


def mock_estimate(connection: sqlite3.Connection, exam: str) -> int | None:
    rows = connection.execute(
        """
        SELECT score FROM attempt
        WHERE exam = ? AND mode = 'MOCK' AND finished_at IS NOT NULL AND score IS NOT NULL
        ORDER BY finished_at DESC LIMIT ?
        """,
        (exam, RECENT_MOCKS),
    ).fetchall()
    if not rows:
        return None
    return round(sum(row["score"] for row in rows) / len(rows))


def exam_readiness(connection: sqlite3.Connection, exam: ExamFormat, exam_date: str, today: date) -> dict[str, Any]:
    units = unit_readiness(connection, exam)
    if exam.scoring == "single":
        estimate = weighted_estimate(units, exam.max_score)
        basis = f"accuracy over the last {RECENT_ANSWERS} answered questions, weighted by the blueprint"
    else:
        estimate = mock_estimate(connection, exam.code)
        basis = f"mean of the last {RECENT_MOCKS} finished mocks"
    return {
        "code": exam.code,
        "name": exam.name,
        "label": exam.label,
        "track": exam.track,
        "scoring": exam.scoring,
        "pass_mark": exam.pass_mark,
        "max_score": exam.max_score,
        "estimate": estimate,
        "ready": estimate is not None and estimate >= exam.pass_mark,
        "basis": basis,
        "units": units,
        "exam_date": exam_date,
        "days_to_exam": days_to_exam(exam_date, today),
    }


def _exam_phrase(entry: dict[str, Any]) -> str:
    if entry["estimate"] is None:
        return f"{entry['code']}: no data yet."
    verdict = "ready" if entry["ready"] else "not yet"
    qualifier = " on recent form" if entry["scoring"] == "single" else ""
    return f"{entry['code']}: {entry['estimate']}/{entry['max_score']}{qualifier}, {verdict}."


def summary_line(exams: list[dict[str, Any]]) -> str:
    """The one honest line: "OGEA-101: 31/40 on recent form, ready. OGEA-102: 19/40, not yet. …" """
    return " ".join(_exam_phrase(entry) for entry in exams)


def cards_due(connection: sqlite3.Connection, now: str | None = None) -> int:
    return connection.execute(
        "SELECT COUNT(*) FROM card_review WHERE due_at <= ?", (now or _now_iso(),)
    ).fetchone()[0]


def weakest_objectives(
    connection: sqlite3.Connection, limit: int = 3, min_answers: int = 3
) -> list[dict[str, Any]]:
    rows = connection.execute(
        """
        SELECT q.objective_code AS code, o.text, o.unit_code,
               COUNT(*) AS answered,
               SUM(COALESCE(aa.points, 0)) AS earned,
               SUM(CASE q.scoring WHEN 'gradient' THEN 5 ELSE 1 END) AS possible
        FROM attempt_answer aa
        JOIN question q ON q.id = aa.question_id
        JOIN objective o ON o.code = q.objective_code
        WHERE aa.answered_at IS NOT NULL AND aa.chosen_key IS NOT NULL
        GROUP BY q.objective_code
        HAVING COUNT(*) >= ?
        """,
        (min_answers,),
    ).fetchall()
    scored = [
        {
            "code": row["code"],
            "text": row["text"],
            "unit_code": row["unit_code"],
            "answered": row["answered"],
            "accuracy": row["earned"] / row["possible"],
        }
        for row in rows
    ]
    scored.sort(key=lambda item: (item["accuracy"], -item["answered"], item["code"]))
    return scored[:limit]


def next_lesson(connection: sqlite3.Connection, plan_json: str, today: date) -> dict[str, Any] | None:
    """The first planned, unread lesson on or after today; otherwise the first unread lesson in
    curriculum order (blueprint order for a lesson the curriculum does not place)."""
    read = {
        row["lesson_id"] for row in connection.execute("SELECT lesson_id FROM lesson_progress").fetchall()
    }
    if plan_json:
        for day in orjson.loads(plan_json):
            if day["date"] < today.isoformat():
                continue
            for item in day["items"]:
                if item["kind"] == "LESSON" and item["ref"] not in read:
                    return {"id": item["ref"], "title": item["title"], "date": day["date"]}
    row = connection.execute(
        """
        SELECT l.id, l.title FROM lesson l
        JOIN learning_unit u ON u.code = l.unit_code
        LEFT JOIN lesson_week w ON w.lesson_id = l.id
        LEFT JOIN lesson_progress p ON p.lesson_id = l.id
        WHERE p.lesson_id IS NULL
        ORDER BY w.week IS NULL, w.week, w.position, u.ordinal, l.ordinal LIMIT 1
        """
    ).fetchone()
    return {"id": row["id"], "title": row["title"], "date": None} if row else None


def days_to_exam(exam_date: str, today: date) -> int | None:
    if not exam_date:
        return None
    return (date.fromisoformat(exam_date[:10]) - today).days


def dashboard_data(
    connection: sqlite3.Connection, exam_dates: dict[str, str], plan_json: str, blueprint: Blueprint | None = None
) -> dict[str, Any]:
    today = datetime.now(UTC).date()
    blueprint = blueprint or load_blueprint(CONTENT_DIR)
    exams = [
        exam_readiness(connection, exam, exam_dates.get(exam.code, ""), today) for exam in blueprint.exams.values()
    ]
    tracks: list[dict[str, Any]] = []
    for entry in exams:
        group = next((track for track in tracks if track["track"] == entry["track"]), None)
        if group is None:
            group = {"track": entry["track"], "exams": []}
            tracks.append(group)
        group["exams"].append(entry)
    return {
        "summary": summary_line(exams),
        "exams": exams,
        "tracks": tracks,
        "cards_due": cards_due(connection),
        "weakest": weakest_objectives(connection),
        "next_lesson": next_lesson(connection, plan_json, today),
    }
