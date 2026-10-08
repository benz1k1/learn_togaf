"""Worked examples: the ADM deliverables written out for one fictional enterprise (learn_togaf.md §4.3)."""

import sqlite3

from fastapi import Depends, HTTPException
from starlette.requests import Request

from learn_togaf.deps import get_db
from learn_togaf.pages.context import base_context
from learn_togaf.pages.templating import render_markdown, templates
from learn_togaf.service import examples, notes


async def example_list(request: Request, track: str = "", connection: sqlite3.Connection = Depends(get_db)):
    track = track.upper()
    if track and track not in examples.TRACKS:
        raise HTTPException(404, f"No worked-example track {track}")
    groups = examples.examples_by_phase(connection, track)
    return templates.TemplateResponse(
        request,
        "example_list.html",
        base_context(
            request,
            connection,
            groups=groups,
            total=sum(len(g["examples"]) for g in groups),
            track=track,
            tracks=examples.TRACKS,
            counts=examples.track_counts(connection),
        ),
    )


async def example_page(request: Request, example_id: str, connection: sqlite3.Connection = Depends(get_db)):
    document = examples.example(connection, example_id)
    if document is None:
        raise HTTPException(404, f"No worked example {example_id}")
    previous, following = examples.neighbours(connection, example_id)
    phase = connection.execute(
        "SELECT code, name FROM adm_phase WHERE code = ?", (document["phase_code"],)
    ).fetchone()
    return templates.TemplateResponse(
        request,
        "example.html",
        base_context(
            request,
            connection,
            document=document,
            body_html=render_markdown(document["body_md"]),
            phase=phase,
            prev=previous,
            next=following,
            artefact_rows=examples.artefact_rows(connection, document["artefacts"]),
            related=examples.related(connection, document),
            figure_url=f"/static/archimate/{document['figure']}" if document["figure"] else None,
            note=notes.get_note(connection, "EXAMPLE", example_id),
        ),
    )
