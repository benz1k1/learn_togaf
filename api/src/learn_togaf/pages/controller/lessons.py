"""Units, lessons, progress and check-yourself (learn_togaf.md §4.2)."""

import sqlite3

from fastapi import Depends, Form, HTTPException
from fastapi.responses import RedirectResponse
from starlette.requests import Request

from learn_togaf.db import transaction
from learn_togaf.deps import get_db
from learn_togaf.pages.context import base_context
from learn_togaf.pages.templating import render_markdown, templates
from learn_togaf.service import lessons, notes


async def unit_list(request: Request, connection: sqlite3.Connection = Depends(get_db)):
    return templates.TemplateResponse(
        request, "unit_list.html", base_context(request, connection, groups=lessons.units_by_exam(connection))
    )


async def unit_page(request: Request, code: str, connection: sqlite3.Connection = Depends(get_db)):
    detail = lessons.unit_detail(connection, code)
    if detail is None:
        raise HTTPException(404, f"No learning unit {code}")
    return templates.TemplateResponse(request, "unit.html", base_context(request, connection, **detail))


async def lesson_page(request: Request, lesson_id: str, connection: sqlite3.Connection = Depends(get_db)):
    detail = lessons.lesson_detail(connection, lesson_id)
    if detail is None:
        raise HTTPException(404, f"No lesson {lesson_id}")
    # Opening a lesson is not reading it: the learner marks it read with the button in
    # _progress.html, so an unread lesson stays "unread" until they say otherwise.
    body_html = lessons.autolink_terms(
        str(render_markdown(detail["lesson"]["body_md"])), lessons.glossary_terms(connection)
    )
    note = notes.get_note(connection, "LESSON", lesson_id)
    return templates.TemplateResponse(
        request,
        "lesson.html",
        base_context(
            request,
            connection,
            lesson_id=lesson_id,  # the progress fragment posts to /lesson-progress/{lesson_id}
            body_html=body_html,
            note=note,
            states=lessons.PROGRESS_STATES,
            **detail,
        ),
    )


async def check_yourself(request: Request, lesson_id: str, connection: sqlite3.Connection = Depends(get_db)):
    check = lessons.check_questions(connection, lesson_id)
    return templates.TemplateResponse(
        request,
        "_check_yourself.html",
        base_context(request, connection, lesson_id=lesson_id, **check),
    )


async def check_yourself_answer(
    request: Request,
    lesson_id: str,
    question_id: str = Form(...),
    key: str = Form(...),
    connection: sqlite3.Connection = Depends(get_db),
):
    with transaction(connection):
        result = lessons.record_check_answer(connection, lesson_id, question_id, key)
    return templates.TemplateResponse(
        request, "_check_yourself.html", base_context(request, connection, lesson_id=lesson_id, result=result)
    )


async def mark_progress(
    request: Request, lesson_id: str, state: str = Form(...), connection: sqlite3.Connection = Depends(get_db)
):
    if state not in lessons.PROGRESS_STATES:
        raise HTTPException(422, f"state must be one of {', '.join(lessons.PROGRESS_STATES)}")
    with transaction(connection):
        lessons.mark_progress(connection, lesson_id, state)
    if request.headers.get("HX-Request"):
        return templates.TemplateResponse(
            request,
            "_progress.html",
            base_context(
                request, connection, lesson_id=lesson_id, state=state, states=lessons.PROGRESS_STATES
            ),
        )
    return RedirectResponse(f"/lesson/{lesson_id}", status_code=303)
