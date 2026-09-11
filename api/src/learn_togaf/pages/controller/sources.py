"""
The source index pages (learn_togaf.md §1.4, §5.1). The learner's private copy of the
publications is served on the loopback only: every route here refuses a client whose address is
not in ``config.LOCAL_ONLY_HOSTS`` — the check is the peer address, never a header.
"""

import sqlite3

from fastapi import Depends, HTTPException
from fastapi.responses import FileResponse
from starlette.requests import Request

from learn_togaf.config import LOCAL_ONLY_HOSTS
from learn_togaf.deps import get_db
from learn_togaf.pages.context import base_context
from learn_togaf.pages.templating import templates
from learn_togaf.service import sources as sources_service


def _require_local(request: Request) -> None:
    host = request.client.host if request.client else ""
    if host not in LOCAL_ONLY_HOSTS:
        raise HTTPException(
            status_code=403, detail="The source store is served on 127.0.0.1 only (learn_togaf.md §1.3)"
        )


async def source_index(request: Request, q: str = "", connection: sqlite3.Connection = Depends(get_db)):
    _require_local(request)
    q = q.strip()
    results = sources_service.search_sections(connection, q) if q else []
    context = base_context(
        request,
        connection,
        q=q,
        results=results,
        documents=sources_service.list_documents(connection),
        counts=sources_service.counts(connection),
    )
    template = "_section.html" if request.headers.get("hx-request") else "source_index.html"
    return templates.TemplateResponse(request, template, context)


async def section_page(request: Request, section_id: str, connection: sqlite3.Connection = Depends(get_db)):
    _require_local(request)
    section = sources_service.get_section(connection, section_id)
    if section is None:
        raise HTTPException(
            status_code=404, detail=f"No source section {section_id!r}. Run: python sources.py fetch"
        )
    questions, lessons = sources_service.citing_content(connection, section)
    return templates.TemplateResponse(
        request,
        "source_section.html",
        base_context(
            request,
            connection,
            section=section,
            ref=sources_service.ref_form(section),
            figures=sources_service.section_figures(connection, section_id),
            questions=questions,
            lessons=lessons,
        ),
    )


async def figure_file(request: Request, figure_id: str, connection: sqlite3.Connection = Depends(get_db)):
    _require_local(request)
    figure = sources_service.get_figure(connection, figure_id)
    if figure is None:
        raise HTTPException(
            status_code=404, detail=f"No source figure {figure_id!r}. Run: python sources.py figures"
        )
    try:
        path = sources_service.figure_path(figure)
    except PermissionError as exc:
        raise HTTPException(status_code=403, detail=str(exc)) from exc
    if not path.is_file():
        raise HTTPException(
            status_code=404, detail=f"figure file {figure['file_path']} is missing from the source store"
        )
    return FileResponse(path)
