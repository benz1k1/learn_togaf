"""
Readiness maths for the dashboard (learn_togaf.md §4.1).

Part 1 is estimated from the last 200 answered Foundation answers: per-unit accuracy weighted
by the blueprint weight of that unit, scaled to /40. Part 2 is the mean score of the last three
finished Practitioner mocks. Both are ``None`` when there is nothing to estimate from, and the
summary line says so rather than printing 0/40.
"""

import sqlite3
from datetime import UTC, date, datetime
from typing import Any

import orjson

PASS_MARK = 24
MAX_SCORE = 40
RECENT_ANSWERS = 200
RECENT_MOCKS = 3
MAX_POINTS = {"FOUNDATION": 1, "PRACTITIONER": 5}


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
        WHERE a.exam = ? AND aa.answered_at IS NOT NULL AND aa.chosen_key IS NOT NULL
        ORDER BY aa.answered_at DESC
        LIMIT ?
        """,
        (exam, limit),
    ).fetchall()


def unit_readiness(connection: sqlite3.Connection, exam: str) -> list[dict[str, Any]]:
    """Per unit: answered, earned/max points, accuracy (None without answers), blueprint weight."""
    units = connection.execute(
        "SELECT code, name, weight, ordinal FROM learning_unit WHERE exam = ? ORDER BY ordinal", (exam,)
    ).fetchall()
    max_points = MAX_POINTS[exam]
    earned: dict[str, int] = {}
    answered: dict[str, int] = {}
    for row in recent_answers(connection, exam):
        answered[row["unit_code"]] = answered.get(row["unit_code"], 0) + 1
        earned[row["unit_code"]] = earned.get(row["unit_code"], 0) + (row["points"] or 0)
    result = []
    for unit in units:
        count = answered.get(unit["code"], 0)
        accuracy = earned.get(unit["code"], 0) / (count * max_points) if count else None
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


def foundation_estimate(units: list[dict[str, Any]]) -> int | None:
    """Weighted accuracy over the units that have answers, scaled to /40."""
    weighted = [
        (unit["weight"], unit["accuracy"])
        for unit in units
        if unit["accuracy"] is not None and unit["weight"]
    ]
    if not weighted:
        return None
    total_weight = sum(weight for weight, _ in weighted)
    accuracy = sum(weight * acc for weight, acc in weighted) / total_weight
    return round(accuracy * MAX_SCORE)


def practitioner_estimate(connection: sqlite3.Connection) -> int | None:
    rows = connection.execute(
        """
        SELECT score FROM attempt
        WHERE exam = 'PRACTITIONER' AND mode = 'MOCK' AND finished_at IS NOT NULL AND score IS NOT NULL
        ORDER BY finished_at DESC LIMIT ?
        """,
        (RECENT_MOCKS,),
    ).fetchall()
    if not rows:
        return None
    return round(sum(row["score"] for row in rows) / len(rows))


def _exam_phrase(label: str, estimate: int | None, qualifier: str = "") -> str:
    if estimate is None:
        return f"{label}: no data yet."
    verdict = "ready" if estimate >= PASS_MARK else "not yet"
    return f"{label}: {estimate}/{MAX_SCORE}{qualifier}, {verdict}."


def summary_line(foundation: int | None, practitioner: int | None) -> str:
    """The one honest line: "Foundation: 31/40 on recent form, ready. Practitioner: 19/40, not yet." """
    return f"{_exam_phrase('Foundation', foundation, ' on recent form')} {_exam_phrase('Practitioner', practitioner)}"


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
               SUM(CASE q.exam WHEN 'FOUNDATION' THEN 1 ELSE 5 END) AS possible
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
    """The first planned, unread lesson on or after today; otherwise the first unread lesson in blueprint order."""
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
        LEFT JOIN lesson_progress p ON p.lesson_id = l.id
        WHERE p.lesson_id IS NULL
        ORDER BY u.ordinal, l.ordinal LIMIT 1
        """
    ).fetchone()
    return {"id": row["id"], "title": row["title"], "date": None} if row else None


def days_to_exam(exam_date: str, today: date) -> int | None:
    if not exam_date:
        return None
    return (date.fromisoformat(exam_date[:10]) - today).days


def dashboard_data(connection: sqlite3.Connection, exam_date: str, plan_json: str) -> dict[str, Any]:
    today = datetime.now(UTC).date()
    foundation_units = unit_readiness(connection, "FOUNDATION")
    practitioner_units = unit_readiness(connection, "PRACTITIONER")
    foundation = foundation_estimate(foundation_units)
    practitioner = practitioner_estimate(connection)
    return {
        "summary": summary_line(foundation, practitioner),
        "foundation": foundation,
        "practitioner": practitioner,
        "pass_mark": PASS_MARK,
        "max_score": MAX_SCORE,
        "foundation_units": foundation_units,
        "practitioner_units": practitioner_units,
        "cards_due": cards_due(connection),
        "weakest": weakest_objectives(connection),
        "next_lesson": next_lesson(connection, plan_json, today),
        "days_to_exam": days_to_exam(exam_date, today),
    }
