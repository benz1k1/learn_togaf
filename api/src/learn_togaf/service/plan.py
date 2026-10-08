"""
Study plan (learn_togaf.md §4.8; learn_sabsa_archimate.md §4.6): pure functions over plain data
so they are unit-testable.

A plan is ``[{date, items: [{kind, ref, title, week?, theme?}]}]`` stored as ``setting
plan_json``. Lessons are spread over the days until the last exam date in curriculum order —
the braid in ``content/curriculum.yaml``, one theme a week across the three tracks; a lesson
the curriculum does not place is appended in blueprint order — each lesson taking a share of
the days proportional to its unit's blueprint weight, with a mock every seven days (of the exam
the day's lessons belong to) and a flashcard REVIEW item each day. Rendering re-flows past-due
unread lessons forward over the days that remain.
"""

import sqlite3
from datetime import date, timedelta
from typing import Any

import orjson

MOCK_EVERY_DAYS = 7
UPCOMING_DAYS = 14
DEFAULT_CARD_CAP = 30
EXERCISE_KINDS = ("draw", "justify")


def lesson_rows(connection: sqlite3.Connection) -> list[dict[str, Any]]:
    """Every lesson in plan order: the curriculum's week and position first, then any unplaced
    lesson by unit ordinal (single-answer units before gradient ones, guides last)."""
    rows = connection.execute(
        """
        SELECT l.id, l.title, l.unit_code, u.exam, u.track, u.weight, u.ordinal AS unit_ordinal, l.ordinal,
               w.week, w.position, c.theme
        FROM lesson l
        JOIN learning_unit u ON u.code = l.unit_code
        LEFT JOIN lesson_week w ON w.lesson_id = l.id
        LEFT JOIN curriculum_week c ON c.week = w.week
        ORDER BY w.week IS NULL, w.week, w.position,
                 CASE WHEN u.scoring = 'single' THEN 0 WHEN u.code LIKE 'G\\_%' ESCAPE '\\' THEN 2 ELSE 1 END,
                 u.ordinal, l.ordinal
        """
    ).fetchall()
    return [dict(row) for row in rows]


def weeks(connection: sqlite3.Connection) -> list[dict[str, Any]]:
    """The curriculum weeks with their lessons (in order) and exercises, for the plan page."""
    rows = connection.execute(
        "SELECT week, theme, exercise_draw, exercise_justify FROM curriculum_week ORDER BY week"
    ).fetchall()
    result = []
    for row in rows:
        lessons = connection.execute(
            """
            SELECT l.id, l.title, l.unit_code, u.track, p.state
            FROM lesson_week w JOIN lesson l ON l.id = w.lesson_id
            JOIN learning_unit u ON u.code = l.unit_code
            LEFT JOIN lesson_progress p ON p.lesson_id = l.id
            WHERE w.week = ? ORDER BY w.position
            """,
            (row["week"],),
        ).fetchall()
        result.append({**dict(row), "lessons": [dict(lesson) for lesson in lessons]})
    return result


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
        item: dict[str, Any] = {"kind": "LESSON", "ref": lesson["id"], "title": lesson["title"]}
        if lesson.get("week") is not None:
            item["week"] = lesson["week"]
            item["theme"] = lesson.get("theme") or ""
        by_day[offset].append(item)
        cumulative += weight
    plan = []
    latest_exam = next((lesson["exam"] for lesson in lessons if lesson.get("exam")), "")
    for offset in range(days):
        items = list(by_day[offset])
        for item in items:
            latest_exam = next(
                (lesson["exam"] for lesson in lessons if lesson["id"] == item["ref"] and lesson.get("exam")),
                latest_exam,
            )
        if offset and offset % MOCK_EVERY_DAYS == 0 and latest_exam:
            items.append({"kind": "MOCK", "ref": latest_exam, "title": f"{latest_exam} mock"})
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


def exercise_key(week: int, kind: str) -> str:
    if kind not in EXERCISE_KINDS:
        raise ValueError(f"exercise kind must be one of {EXERCISE_KINDS}, got {kind!r}")
    return f"exercise:{week}:{kind}"


def exercise_state(connection: sqlite3.Connection) -> dict[str, bool]:
    """``{"3:draw": True, …}`` for every ticked exercise."""
    rows = connection.execute("SELECT key, value FROM setting WHERE key LIKE 'exercise:%'").fetchall()
    return {row["key"].split(":", 1)[1]: row["value"] == "1" for row in rows}
