"""Glossary search and term pages (learn_togaf.md §4.4)."""

import sqlite3

from fastapi import Depends, HTTPException
from starlette.requests import Request

from learn_togaf.deps import get_db
from learn_togaf.pages.context import base_context
from learn_togaf.pages.templating import templates
from learn_togaf.service import glossary, notes


async def glossary_page(
    request: Request, q: str = "", track: str = "", connection: sqlite3.Connection = Depends(get_db)
):
    track = track.upper()
    if track and track not in glossary.TRACKS:
        raise HTTPException(404, f"No glossary track {track}")
    context = base_context(
        request,
        connection,
        q=q,
        track=track,
        tracks=glossary.TRACKS,
        counts=glossary.track_counts(connection),
        terms=glossary.search(connection, q, track),
    )
    template = "_term_list.html" if request.headers.get("HX-Request") else "glossary.html"
    return templates.TemplateResponse(request, template, context)


async def term_page(request: Request, term_id: str, connection: sqlite3.Connection = Depends(get_db)):
    term = glossary.term(connection, term_id)
    if term is None:
        raise HTTPException(404, f"No glossary term {term_id}")
    note = notes.get_note(connection, "TERM", term_id)
    return templates.TemplateResponse(
        request, "glossary_term.html", base_context(request, connection, term=term, note=note)
    )
