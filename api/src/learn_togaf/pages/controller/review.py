"""Flashcards page (learn_togaf.md §4.5): /review, /review/next, /review/{id}/grade, /review/rebuild, /api/review/due."""

import sqlite3
from typing import Any

from fastapi import Depends, Form, HTTPException
from fastapi.responses import JSONResponse, RedirectResponse
from loguru import logger
from starlette.requests import Request

from learn_togaf.db import transaction
from learn_togaf.deps import get_db
from learn_togaf.pages.context import base_context, get_setting
from learn_togaf.pages.templating import templates
from learn_togaf.service import review as review_service

DAILY_CAP_DEFAULT = "50"  # the one tuning value with a default (§4.5); everything else is content


def _daily_cap(connection: sqlite3.Connection) -> int:
    return int(get_setting(connection, "daily_card_cap", DAILY_CAP_DEFAULT))


def _ensure_cards(connection: sqlite3.Connection) -> int:
    """First visit with an empty table: generate the deck. Never touches existing rows."""
    if connection.execute("SELECT COUNT(*) FROM card_review").fetchone()[0]:
        return 0
    with transaction(connection):
        added = review_service.rebuild_cards(connection, review_service.now_utc())
    logger.info(f"flashcards generated on first visit: {added} cards")
    return added


def _stats(connection: sqlite3.Connection) -> dict[str, Any]:
    now = review_service.now_utc()
    counts: dict[str, Any] = dict(review_service.card_counts(connection, now))
    cap = _daily_cap(connection)
    counts["cap"] = cap
    counts["remaining_today"] = max(0, cap - counts["reviewed_today"])
    counts["kinds"] = review_service.kind_counts(connection, now)
    return counts


def _card_context(connection: sqlite3.Connection) -> dict[str, Any]:
    stats = _stats(connection)
    if stats["remaining_today"] <= 0:
        return {"card": None, "content": None, "stats": stats, "reason": "cap"}
    card = review_service.next_due_card(connection, review_service.now_utc())
    if card is None:
        return {"card": None, "content": None, "stats": stats, "reason": "none_due"}
    return {
        "card": card,
        "content": review_service.card_content(connection, card),
        "stats": stats,
        "reason": None,
    }


async def review_page(request: Request, connection: sqlite3.Connection = Depends(get_db)):
    _ensure_cards(connection)
    return templates.TemplateResponse(
        request, "review.html", base_context(request, connection, stats=_stats(connection))
    )


async def next_card(request: Request, connection: sqlite3.Connection = Depends(get_db)):
    return templates.TemplateResponse(
        request, "_card.html", base_context(request, connection, **_card_context(connection))
    )


async def grade_card(
    request: Request,
    card_id: int,
    grade: int = Form(...),
    connection: sqlite3.Connection = Depends(get_db),
):
    if not 0 <= grade <= 5:
        raise HTTPException(status_code=422, detail="grade must be 0..5")
    card = review_service.get_card(connection, card_id)
    if card is None:
        raise HTTPException(status_code=404, detail=f"card {card_id} not found")
    with transaction(connection):
        state = review_service.grade_card(connection, card, grade, review_service.now_utc())
    logger.info(
        f"card {card_id} ({card['card_kind']} {card['card_ref']}) graded {grade}: interval={state.interval_days} ease={state.ease:.2f}"
    )
    if request.headers.get("hx-request") != "true":
        return RedirectResponse("/review", status_code=303)
    return templates.TemplateResponse(
        request, "_card.html", base_context(request, connection, **_card_context(connection))
    )


async def rebuild_cards(request: Request, connection: sqlite3.Connection = Depends(get_db)):
    with transaction(connection):
        added = review_service.rebuild_cards(connection, review_service.now_utc())
    logger.info(f"flashcards rebuilt: {added} new cards")
    return RedirectResponse(f"/review?flash={added}+new+cards+added&flash_kind=success", status_code=303)


async def due_json(request: Request, connection: sqlite3.Connection = Depends(get_db)):
    counts = review_service.card_counts(connection, review_service.now_utc())
    return JSONResponse({"due": counts["due"], "total": counts["total"]})
