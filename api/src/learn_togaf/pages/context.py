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


def base_context(request: Request, connection: sqlite3.Connection, **extra: Any) -> dict[str, Any]:
    context: dict[str, Any] = {
        "request": request,
        "exam_date": get_setting(connection, "exam_date"),
        "flash": None,
    }
    flash = request.query_params.get("flash")
    if flash:
        context["flash"] = {"kind": request.query_params.get("flash_kind", "info"), "text": flash}
    context.update(extra)
    return context
