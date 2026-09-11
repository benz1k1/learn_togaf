"""The review queue (learn_togaf.md §1.5, §5.1): drafts under content/review/."""

import sqlite3
from urllib.parse import urlencode

from fastapi import Depends, HTTPException
from fastapi.responses import RedirectResponse
from starlette.requests import Request

from learn_togaf.config import CONTENT_DIR
from learn_togaf.deps import get_db
from learn_togaf.pages.context import base_context
from learn_togaf.pages.templating import templates
from learn_togaf.service import review_queue as queue_service


def _back(text: str, kind: str = "success") -> RedirectResponse:
    return RedirectResponse(
        "/review-queue?" + urlencode({"flash": text, "flash_kind": kind}), status_code=303
    )


async def queue_page(request: Request, connection: sqlite3.Connection = Depends(get_db)):
    drafts = queue_service.list_drafts(CONTENT_DIR)
    return templates.TemplateResponse(
        request,
        "review_queue.html",
        base_context(
            request,
            connection,
            drafts=drafts,
            review_dir=queue_service.review_dir(CONTENT_DIR),
            failed=sum(1 for draft in drafts if draft.failed),
        ),
    )


async def accept_draft(request: Request, draft_id: str, connection: sqlite3.Connection = Depends(get_db)):
    try:
        destination = queue_service.accept_draft(connection, CONTENT_DIR, draft_id)
    except FileNotFoundError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    return _back(f"Accepted {draft_id} → {destination.relative_to(CONTENT_DIR)}; content reloaded")


async def reject_draft(request: Request, draft_id: str, connection: sqlite3.Connection = Depends(get_db)):
    try:
        target = queue_service.reject_draft(CONTENT_DIR, draft_id)
    except FileNotFoundError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    return _back(f"Rejected {draft_id} → {target.relative_to(CONTENT_DIR)}", kind="warning")
