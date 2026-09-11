"""
Study plan (learn_togaf.md §4.8): pure functions over plain data so they are unit-testable.

A plan is ``[{date, items: [{kind, ref, title}]}]`` stored as ``setting plan_json``. Lessons
are spread over the days until the exam — Foundation units first in blueprint order, each
unit taking a share of the days proportional to its blueprint weight, then Practitioner units,
then the guides — with a mock every seven days and a flashcard REVIEW item each day. Rendering
re-flows past-due unread lessons forward over the days that remain.
"""

import sqlite3
from datetime import date, timedelta
from typing import Any

import orjson

MOCK_EVERY_DAYS = 7
UPCOMING_DAYS = 14
DEFAULT_CARD_CAP = 30


def lesson_rows(connection: sqlite3.Connection) -> list[dict[str, Any]]:
    """Every lesson in plan order: Foundation units by ordinal, then Practitioner P*, then guides."""
    rows = connection.execute(
        """
        SELECT l.id, l.title, l.unit_code, u.exam, u.weight, u.ordinal AS unit_ordinal, l.ordinal
        FROM lesson l JOIN learning_unit u ON u.code = l.unit_code
        ORDER BY CASE WHEN u.exam = 'FOUNDATION' THEN 0 WHEN u.code LIKE 'G_%' THEN 2 ELSE 1 END, u.ordinal, l.ordinal
        """
    ).fetchall()
    return [dict(row) for row in rows]


def _read_ids(connection: sqlite3.Connection) -> set[str]:
    return {
        row["lesson_id"] for row in connection.execute("SELECT lesson_id FROM lesson_progress").fetchall()
    }


def generate_plan(
    lessons: list[dict[str, Any]], start: date, exam_date: date, card_cap: int
) -> list[dict[str, Any]]:
    """Spread ``lessons`` (already in plan order) over the days from ``start`` up to the day before the exam."""
    days = max((exam_date - start).days, 1)
    weights = [max(int(lesson["weight"]), 1) for lesson in lessons]
    total = sum(weights) or 1
    by_day: dict[int, list[dict[str, Any]]] = {offset: [] for offset in range(days)}
    cumulative = 0
    for lesson, weight in zip(lessons, weights, strict=True):
        offset = min(int(cumulative / total * days), days - 1)
        by_day[offset].append({"kind": "LESSON", "ref": lesson["id"], "title": lesson["title"]})
        cumulative += weight
    plan = []
    latest_exam = "FOUNDATION"
    for offset in range(days):
        items = list(by_day[offset])
        for item in items:
            latest_exam = next(
                (lesson["exam"] for lesson in lessons if lesson["id"] == item["ref"]), latest_exam
            )
        if offset and offset % MOCK_EVERY_DAYS == 0:
            label = latest_exam.capitalize()
            items.append({"kind": "MOCK", "ref": latest_exam, "title": f"{label} mock"})
        items.append({"kind": "REVIEW", "ref": "due", "title": f"Flashcards due (up to {card_cap})"})
        plan.append({"date": (start + timedelta(days=offset)).isoformat(), "items": items})
    return plan


def reflow(plan: list[dict[str, Any]], today: date, read_ids: set[str]) -> list[dict[str, Any]]:
    """Move past-due unread lessons forward, spread evenly over the days from today to the end of the plan."""
    today_iso = today.isoformat()
    overdue: list[dict[str, Any]] = []
    past, future = [], []
    for day in plan:
        if day["date"] < today_iso:
            kept = []
            for item in day["items"]:
                if item["kind"] == "LESSON" and item["ref"] not in read_ids:
                    overdue.append(item)
                else:
                    kept.append(item)
            past.append({"date": day["date"], "items": kept})
        else:
            future.append({"date": day["date"], "items": list(day["items"])})
    if not overdue:
        return past + future
    if not future:
        future = [{"date": today_iso, "items": []}]
    per_day = -(-len(overdue) // len(future))
    for index, day in enumerate(future):
        chunk = overdue[index * per_day : (index + 1) * per_day]
        day["items"] = chunk + day["items"]
    return past + future


def upcoming(plan: list[dict[str, Any]], today: date, days: int = UPCOMING_DAYS) -> list[dict[str, Any]]:
    start, end = today.isoformat(), (today + timedelta(days=days)).isoformat()
    return [day for day in plan if start <= day["date"] < end]


def build_and_store(
    connection: sqlite3.Connection, exam_date: date, card_cap: int, today: date
) -> list[dict[str, Any]]:
    unread = [lesson for lesson in lesson_rows(connection) if lesson["id"] not in _read_ids(connection)]
    plan = generate_plan(unread, today, exam_date, card_cap)
    connection.execute(
        "INSERT INTO setting(key, value) VALUES ('plan_json', ?) ON CONFLICT(key) DO UPDATE SET value = excluded.value",
        (orjson.dumps(plan).decode(),),
    )
    return plan


def rendered_plan(connection: sqlite3.Connection, plan_json: str, today: date) -> list[dict[str, Any]]:
    if not plan_json:
        return []
    plan = reflow(orjson.loads(plan_json), today, _read_ids(connection))
    return upcoming(plan, today)
