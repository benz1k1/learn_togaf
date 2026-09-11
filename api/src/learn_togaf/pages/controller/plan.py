"""Study plan (learn_togaf.md §4.8)."""

import sqlite3
from datetime import UTC, date, datetime

from fastapi import Depends, Form
from fastapi.responses import RedirectResponse
from starlette.requests import Request

from learn_togaf.db import transaction
from learn_togaf.deps import get_db
from learn_togaf.pages.context import base_context, get_setting, set_setting
from learn_togaf.pages.templating import templates
from learn_togaf.service import plan


async def plan_page(request: Request, connection: sqlite3.Connection = Depends(get_db)):
    today = datetime.now(UTC).date()
    plan_json = get_setting(connection, "plan_json")
    return templates.TemplateResponse(
        request,
        "plan.html",
        base_context(
            request,
            connection,
            daily_card_cap=get_setting(connection, "daily_card_cap", str(plan.DEFAULT_CARD_CAP)),
            has_plan=bool(plan_json),
            days=plan.rendered_plan(connection, plan_json, today),
            today=today.isoformat(),
        ),
    )


async def save_plan(
    request: Request,
    exam_date: str = Form(...),
    daily_card_cap: int = Form(...),
    connection: sqlite3.Connection = Depends(get_db),
):
    exam = date.fromisoformat(exam_date)
    today = datetime.now(UTC).date()
    if exam <= today:
        return RedirectResponse(
            "/plan?flash=The+exam+date+must+be+after+today&flash_kind=error", status_code=303
        )
    with transaction(connection):
        set_setting(connection, "exam_date", exam.isoformat())
        set_setting(connection, "daily_card_cap", str(daily_card_cap))
        generated = plan.build_and_store(connection, exam, daily_card_cap, today)
    return RedirectResponse(f"/plan?flash=Plan+regenerated+over+{len(generated)}+days", status_code=303)
