"""What every page template gets besides its own data (base.html reads exam_date, flash)."""

import sqlite3
from typing import Any

from starlette.requests import Request


def get_setting(connection: sqlite3.Connection, key: str, default: str = "") -> str:
    row = connection.execute("SELECT value FROM setting WHERE key = ?", (key,)).fetchone()
    return row["value"] if row else default


def set_setting(connection: sqlite3.Connection, key: str, value: str) -> None:
    connection.execute(
        "INSERT INTO setting(key, value) VALUES (?, ?) ON CONFLICT(key) DO UPDATE SET value = excluded.value",
        (key, value),
    )


EXAM_DATE_PREFIX = "exam_date:"


def exam_dates(connection: sqlite3.Connection) -> dict[str, str]:
    """``{"OGEA-101": "2026-11-03", …}`` — one ``exam_date:<code>`` setting per exam the learner dated."""
    rows = connection.execute(
        "SELECT key, value FROM setting WHERE key LIKE ? AND value != ''", (f"{EXAM_DATE_PREFIX}%",)
    ).fetchall()
    return {row["key"][len(EXAM_DATE_PREFIX) :]: row["value"] for row in rows}


def base_context(request: Request, connection: sqlite3.Connection, **extra: Any) -> dict[str, Any]:
    dates = exam_dates(connection)
    context: dict[str, Any] = {
        "request": request,
        "exam_dates": dates,
        "next_exam": min(dates.items(), key=lambda item: item[1]) if dates else None,
        "flash": None,
    }
    flash = request.query_params.get("flash")
    if flash:
        context["flash"] = {"kind": request.query_params.get("flash_kind", "info"), "text": flash}
    context.update(extra)
    return context
