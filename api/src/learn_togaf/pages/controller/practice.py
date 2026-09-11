"""
Practice (learn_togaf.md §4.6): /practice, /attempt/{id} and its fragments, /open-book, and the
timer JSON. Draws, the clock and scoring live in service/practice.py; this module only maps
HTTP to them.
"""

import sqlite3
from typing import Any

from fastapi import Depends, Form, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from loguru import logger
from starlette.requests import Request

from learn_togaf.db import transaction
from learn_togaf.deps import get_db
from learn_togaf.pages.context import base_context
from learn_togaf.pages.templating import templates
from learn_togaf.service import open_book as open_book_service
from learn_togaf.service import practice as engine


def _is_htmx(request: Request) -> bool:
    return request.headers.get("hx-request") == "true"


def _attempt_or_404(connection: sqlite3.Connection, attempt_id: int) -> sqlite3.Row:
    attempt = engine.get_attempt(connection, attempt_id)
    if attempt is None:
        raise HTTPException(status_code=404, detail=f"attempt {attempt_id} not found")
    return attempt


def _auto_finish_if_expired(connection: sqlite3.Connection, attempt: sqlite3.Row) -> sqlite3.Row:
    if attempt["finished_at"] is None and engine.is_expired(attempt, engine.utc_now()):
        with transaction(connection):
            attempt = engine.finish_attempt(connection, attempt, engine.utc_now())
        logger.info(f"attempt {attempt['id']} auto-finished: clock ran out")
    return attempt


def _attempt_context(connection: sqlite3.Connection, attempt: sqlite3.Row) -> dict[str, Any]:
    ids = engine.question_ids(attempt)
    answers = engine.answers_by_question(connection, attempt["id"])
    navigator = [
        {
            "index": index,
            "number": index + 1,
            "question_id": question_id,
            "answered": bool(answers[question_id]["chosen_key"]) if question_id in answers else False,
            "flagged": bool(answers[question_id]["flagged"]) if question_id in answers else False,
        }
        for index, question_id in enumerate(ids)
    ]
    return {
        "attempt": attempt,
        "mode_label": engine.mode_label(attempt),
        "question_count": len(ids),
        "navigator": navigator,
        "answered_count": sum(1 for entry in navigator if entry["answered"]),
        "filters": engine.attempt_filters(attempt),
        "open_book": engine.open_book_allowed(attempt),
        "remaining_s": engine.remaining_seconds(attempt, engine.utc_now()),
    }


def _question_context(
    connection: sqlite3.Connection, attempt: sqlite3.Row, index: int, reveal: bool
) -> dict[str, Any]:
    ids = engine.question_ids(attempt)
    if not 0 <= index < len(ids):
        raise HTTPException(status_code=404, detail=f"question index {index} out of range")
    detail = engine.question_with_options(connection, ids[index])
    answer = connection.execute(
        "SELECT * FROM attempt_answer WHERE attempt_id = ? AND question_id = ?", (attempt["id"], ids[index])
    ).fetchone()
    answered = answer is not None and answer["chosen_key"] is not None
    context = _attempt_context(connection, attempt)
    context.update(
        {
            "index": index,
            "number": index + 1,
            "question": detail["question"],
            "options": detail["options"],
            "refs": detail["refs"],
            "tags": detail["tags"],
            "correct_key": detail["correct_key"],
            "max_points": detail["max_points"],
            "chosen_key": answer["chosen_key"] if answer else None,
            "flagged": bool(answer["flagged"]) if answer else False,
            "answered": answered,
            # A drill reveals the explanation as soon as the question is answered; a mock never
            # does until the review page.
            "reveal": reveal
            or (attempt["mode"] == "DRILL" and answered)
            or attempt["finished_at"] is not None,
            "has_prev": index > 0,
            "has_next": index + 1 < len(ids),
        }
    )
    return context


def _render_question(
    request: Request, connection: sqlite3.Connection, attempt: sqlite3.Row, index: int, reveal: bool = False
):
    context = _question_context(connection, attempt, index, reveal)
    template = "_scenario.html" if context["question"]["exam"] == "PRACTITIONER" else "_question.html"
    return templates.TemplateResponse(request, template, base_context(request, connection, **context))


# ---------------------------------------------------------------- /practice
async def practice_page(request: Request, connection: sqlite3.Connection = Depends(get_db)):
    params = request.query_params
    context = {
        "units": engine.units_for_form(connection),
        "recent": engine.recent_attempts(connection),
        "preselect_objective": params.get("objective", ""),
        "preselect_phase": params.get("phase", ""),
        "preselect_kind": params.get("kind", ""),
        "modes": engine.MODES,
    }
    preselect_exam = "FOUNDATION"
    if context["preselect_objective"]:
        row = connection.execute(
            "SELECT unit_code FROM objective WHERE code = ?", (context["preselect_objective"],)
        ).fetchone()
        if row is None:
            raise HTTPException(
                status_code=404, detail=f"objective {context['preselect_objective']} not found"
            )
        context["preselect_unit"] = row["unit_code"]
        unit = connection.execute(
            "SELECT exam FROM learning_unit WHERE code = ?", (row["unit_code"],)
        ).fetchone()
        preselect_exam = unit["exam"]
    else:
        context["preselect_unit"] = ""
    context["preselect_exam"] = preselect_exam
    return templates.TemplateResponse(request, "practice.html", base_context(request, connection, **context))


async def start_attempt(
    request: Request,
    mode: str = Form(...),
    exam: str = Form("FOUNDATION"),
    units: list[str] = Form(default=[]),
    objectives: list[str] = Form(default=[]),
    count: int = Form(10),
    include_drafts: str = Form(""),
    sources: str = Form("all"),
    seed: str = Form(""),
    phase: str = Form(""),
    kind: str = Form(""),
    connection: sqlite3.Connection = Depends(get_db),
):
    if mode not in engine.MODES:
        raise HTTPException(status_code=422, detail=f"mode must be one of {', '.join(engine.MODES)}")
    if exam not in ("FOUNDATION", "PRACTITIONER"):
        raise HTTPException(status_code=422, detail="exam must be FOUNDATION or PRACTITIONER")
    draw_seed = int(seed) if seed.strip() else engine.new_seed()
    try:
        if mode == "FOUNDATION_MOCK":
            draw = engine.draw_foundation_mock(connection, draw_seed)
        elif mode == "PRACTITIONER_MOCK":
            draw = engine.draw_practitioner_mock(connection, draw_seed)
        elif phase and kind == "io":
            draw = engine.draw_phase_io_drill(connection, phase, count, draw_seed)
        else:
            draw = engine.draw_drill(
                connection, exam, units, objectives, count, include_drafts == "on", sources, draw_seed
            )
    except engine.DrawError as exc:
        logger.warning(f"practice draw refused: {exc}")
        return RedirectResponse(f"/practice?flash={str(exc)}&flash_kind=warning", status_code=303)
    with transaction(connection):
        attempt_id = engine.create_attempt(connection, draw, engine.utc_now())
    logger.info(
        f"attempt {attempt_id} started: {mode} exam={draw.exam} questions={len(draw.question_ids)} seed={draw.seed}"
        + (f" short_units={draw.short_units}" if draw.short_units else "")
    )
    return RedirectResponse(f"/attempt/{attempt_id}", status_code=303)


# ---------------------------------------------------------------- /attempt/{id}
async def attempt_page(request: Request, attempt_id: int, connection: sqlite3.Connection = Depends(get_db)):
    attempt = _auto_finish_if_expired(connection, _attempt_or_404(connection, attempt_id))
    if attempt["finished_at"]:
        return RedirectResponse(f"/attempt/{attempt_id}/review", status_code=303)
    context = _attempt_context(connection, attempt)
    first_unanswered = next((entry["index"] for entry in context["navigator"] if not entry["answered"]), 0)
    context["start_index"] = first_unanswered
    return templates.TemplateResponse(request, "attempt.html", base_context(request, connection, **context))


async def question_fragment(
    request: Request, attempt_id: int, index: int, connection: sqlite3.Connection = Depends(get_db)
):
    attempt = _auto_finish_if_expired(connection, _attempt_or_404(connection, attempt_id))
    if attempt["finished_at"] and _is_htmx(request):
        return HTMLResponse("", headers={"HX-Redirect": f"/attempt/{attempt_id}/review"})
    return _render_question(request, connection, attempt, index)


async def answer(
    request: Request,
    attempt_id: int,
    index: int = Form(...),
    question_id: str = Form(...),
    key: str = Form(...),
    seconds: int = Form(0),
    connection: sqlite3.Connection = Depends(get_db),
):
    attempt = _attempt_or_404(connection, attempt_id)
    try:
        with transaction(connection):
            result = engine.record_answer(connection, attempt, question_id, key, seconds, engine.utc_now())
    except engine.AttemptClosed as exc:
        attempt = _auto_finish_if_expired(connection, attempt)
        logger.info(f"attempt {attempt_id} answer refused for {question_id}: {exc}")
        headers = (
            {"HX-Redirect": f"/attempt/{attempt_id}/review"}
            if attempt["finished_at"] and _is_htmx(request)
            else {}
        )
        return JSONResponse({"success": False, "error": str(exc)}, status_code=409, headers=headers)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    logger.info(
        f"attempt {attempt_id} q{index + 1} {question_id} -> {key} ({result['points']}/{result['max_points']})"
    )
    if not _is_htmx(request):
        return RedirectResponse(f"/attempt/{attempt_id}", status_code=303)
    ids = engine.question_ids(attempt)
    if attempt["mode"] == "DRILL":
        return _render_question(request, connection, attempt, index, reveal=True)
    next_index = index + 1 if index + 1 < len(ids) else index
    return _render_question(request, connection, attempt, next_index)


async def flag(
    request: Request,
    attempt_id: int,
    index: int = Form(...),
    question_id: str = Form(...),
    connection: sqlite3.Connection = Depends(get_db),
):
    attempt = _attempt_or_404(connection, attempt_id)
    try:
        with transaction(connection):
            engine.toggle_flag(connection, attempt, question_id)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    if not _is_htmx(request):
        return RedirectResponse(f"/attempt/{attempt_id}", status_code=303)
    return _render_question(request, connection, attempt, index)


async def finish(request: Request, attempt_id: int, connection: sqlite3.Connection = Depends(get_db)):
    attempt = _attempt_or_404(connection, attempt_id)
    with transaction(connection):
        attempt = engine.finish_attempt(connection, attempt, engine.utc_now())
    logger.info(
        f"attempt {attempt_id} finished: {attempt['score']}/{attempt['max_score']} passed={attempt['passed']}"
    )
    if _is_htmx(request):
        return HTMLResponse("", headers={"HX-Redirect": f"/attempt/{attempt_id}/review"})
    return RedirectResponse(f"/attempt/{attempt_id}/review", status_code=303)


async def review_attempt(request: Request, attempt_id: int, connection: sqlite3.Connection = Depends(get_db)):
    attempt = _auto_finish_if_expired(connection, _attempt_or_404(connection, attempt_id))
    if attempt["finished_at"] is None:
        return RedirectResponse(f"/attempt/{attempt_id}", status_code=303)
    context = _attempt_context(connection, attempt)
    context["review"] = engine.review_data(connection, attempt)
    context["pass_mark"] = engine.pass_mark_for(attempt["exam"]) if attempt["mode"] == "MOCK" else None
    return templates.TemplateResponse(
        request, "attempt_review.html", base_context(request, connection, **context)
    )


async def timer_fragment(request: Request, attempt_id: int, connection: sqlite3.Connection = Depends(get_db)):
    attempt = _auto_finish_if_expired(connection, _attempt_or_404(connection, attempt_id))
    context = {
        "attempt": attempt,
        "remaining_s": engine.remaining_seconds(attempt, engine.utc_now()),
        "finished": attempt["finished_at"] is not None,
    }
    return templates.TemplateResponse(request, "_timer.html", base_context(request, connection, **context))


async def timer_json(request: Request, attempt_id: int, connection: sqlite3.Connection = Depends(get_db)):
    attempt = _auto_finish_if_expired(connection, _attempt_or_404(connection, attempt_id))
    return JSONResponse(
        {
            "remaining_s": engine.remaining_seconds(attempt, engine.utc_now()),
            "finished": attempt["finished_at"] is not None,
        }
    )


# ---------------------------------------------------------------- /open-book
async def open_book(request: Request, connection: sqlite3.Connection = Depends(get_db)):
    query = request.query_params.get("q", "")
    results = open_book_service.search(connection, query)
    context = {"q": query, "results": results, "fragment_only": _is_htmx(request)}
    return templates.TemplateResponse(
        request, "_open_book.html", base_context(request, connection, **context)
    )
