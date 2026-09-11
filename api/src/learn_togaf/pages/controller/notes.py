"""Notes and the learner-state export (learn_togaf.md §4.10)."""

import sqlite3

import orjson
from fastapi import Depends, Form
from fastapi.responses import StreamingResponse
from starlette.requests import Request

from learn_togaf.db import transaction
from learn_togaf.deps import get_db
from learn_togaf.pages.context import base_context
from learn_togaf.pages.templating import templates
from learn_togaf.service import notes


async def export_page(request: Request, connection: sqlite3.Connection = Depends(get_db)):
    counts = {
        table: connection.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
        for table in (
            "attempt",
            "attempt_answer",
            "card_review",
            "note",
            "lesson_progress",
            "setting",
            "study_session",
        )
    }
    return templates.TemplateResponse(
        request, "export.html", base_context(request, connection, counts=counts)
    )


async def export_state(request: Request, connection: sqlite3.Connection = Depends(get_db)):
    payload = notes.export_state(connection)
    stamp = payload["exported_at"].replace(":", "").replace("-", "")
    body = orjson.dumps(payload, option=orjson.OPT_INDENT_2)
    chunks = (body[offset : offset + 65536] for offset in range(0, len(body), 65536))
    return StreamingResponse(
        chunks,
        media_type="application/json",
        headers={"Content-Disposition": f'attachment; filename="learn_togaf_state_{stamp}.json"'},
    )


async def save_note(
    request: Request,
    ref_kind: str = Form(...),
    ref_id: str = Form(...),
    body_md: str = Form(""),
    connection: sqlite3.Connection = Depends(get_db),
):
    with transaction(connection):
        note = notes.save_note(connection, ref_kind, ref_id, body_md)
    return templates.TemplateResponse(
        request,
        "_note.html",
        base_context(request, connection, note=note, ref_kind=ref_kind, ref_id=ref_id, saved=True),
    )
