"""Study plan (learn_togaf.md §4.8; learn_sabsa_archimate.md §4.6): one date per exam, the braid's weeks and exercises."""

import sqlite3
from datetime import UTC, date, datetime

from fastapi import Depends, Form, HTTPException
from fastapi.responses import RedirectResponse
from starlette.requests import Request

from learn_togaf.config import CONTENT_DIR
from learn_togaf.content.loader import load_blueprint
from learn_togaf.db import transaction
from learn_togaf.deps import get_db
from learn_togaf.pages.context import EXAM_DATE_PREFIX, base_context, exam_dates, get_setting, set_setting
from learn_togaf.pages.templating import templates
from learn_togaf.service import plan


async def plan_page(request: Request, connection: sqlite3.Connection = Depends(get_db)):
    today = datetime.now(UTC).date()
    plan_json = get_setting(connection, "plan_json")
    dates = exam_dates(connection)
    blueprint = load_blueprint(CONTENT_DIR)
    return templates.TemplateResponse(
        request,
        "plan.html",
        base_context(
            request,
            connection,
            exams=[
                {"code": exam.code, "label": exam.label, "track": exam.track, "date": dates.get(exam.code, "")}
                for exam in blueprint.exams.values()
            ],
            daily_card_cap=get_setting(connection, "daily_card_cap", str(plan.DEFAULT_CARD_CAP)),
            has_plan=bool(plan_json),
            days=plan.rendered_plan(connection, plan_json, today),
            weeks=plan.weeks(connection),
            exercises=plan.exercise_state(connection),
            today=today.isoformat(),
        ),
    )


async def save_plan(
    request: Request,
    daily_card_cap: int = Form(...),
    connection: sqlite3.Connection = Depends(get_db),
):
    """One ``exam_date:<code>`` field per exam (blank clears it); the plan runs to the latest date set."""
    form = await request.form()
    blueprint = load_blueprint(CONTENT_DIR)
    today = datetime.now(UTC).date()
    dates: dict[str, date] = {}
    for code in blueprint.exams:
        raw = str(form.get(f"{EXAM_DATE_PREFIX}{code}", "")).strip()
        if raw:
            dates[code] = date.fromisoformat(raw)
    if not dates:
        return RedirectResponse("/plan?flash=Set+at+least+one+exam+date&flash_kind=error", status_code=303)
    if any(when <= today for when in dates.values()):
        return RedirectResponse("/plan?flash=Every+exam+date+must+be+after+today&flash_kind=error", status_code=303)
    horizon = max(dates.values())
    with transaction(connection):
        for code in blueprint.exams:
            set_setting(connection, f"{EXAM_DATE_PREFIX}{code}", dates[code].isoformat() if code in dates else "")
        set_setting(connection, "daily_card_cap", str(daily_card_cap))
        generated = plan.build_and_store(connection, horizon, daily_card_cap, today)
    return RedirectResponse(f"/plan?flash=Plan+regenerated+over+{len(generated)}+days", status_code=303)


async def toggle_exercise(
    request: Request,
    week: int,
    kind: str,
    done: str = Form(""),
    connection: sqlite3.Connection = Depends(get_db),
):
    """Tick or untick a week's draw-it / justify-it exercise (stored as ``exercise:<week>:<kind>``)."""
    try:
        key = plan.exercise_key(week, kind)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    with transaction(connection):
        set_setting(connection, key, "1" if done in ("on", "1", "true") else "0")
    if request.headers.get("HX-Request"):
        return templates.TemplateResponse(
            request,
            "_exercise.html",
            base_context(request, connection, week=week, kind=kind, done=done in ("on", "1", "true")),
        )
    return RedirectResponse("/plan", status_code=303)
