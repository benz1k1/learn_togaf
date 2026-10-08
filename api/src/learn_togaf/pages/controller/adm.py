"""ADM explorer: cycle, phases, techniques, artefact catalogue (learn_togaf.md §4.3)."""

import sqlite3

from fastapi import Depends, HTTPException
from starlette.requests import Request

from learn_togaf.deps import get_db
from learn_togaf.pages.context import base_context
from learn_togaf.pages.static_files import ARCHIMATE_DIR, ARTEFACT_EXAMPLE_DIR
from learn_togaf.pages.templating import templates
from learn_togaf.service import adm, examples, notes


async def adm_page(request: Request, connection: sqlite3.Connection = Depends(get_db)):
    phases = adm.phases(connection)
    return templates.TemplateResponse(
        request,
        "adm.html",
        base_context(
            request,
            connection,
            phases=phases,
            layout=adm.cycle_layout(phases),
            techniques=adm.techniques(connection),
            crosswalk=adm.crosswalk_rows(connection),
        ),
    )


def _phase_context(connection: sqlite3.Connection, code: str) -> dict:
    phase = adm.phase(connection, code)
    if phase is None:
        raise HTTPException(404, f"No ADM phase {code}")
    previous, following = adm.neighbours(connection, code)
    return {
        "phase": phase,
        "previous": previous,
        "following": following,
        "artefacts": adm.phase_artefacts(connection, phase),
        "techniques": adm.phase_techniques(connection, code),
        "figures": adm.phase_figures(connection, phase),
        "examples": examples.phase_examples(connection, code),
    }


async def phase_panel(request: Request, phase: str, connection: sqlite3.Connection = Depends(get_db)):
    return templates.TemplateResponse(
        request, "_phase_panel.html", base_context(request, connection, **_phase_context(connection, phase))
    )


async def phase_page(request: Request, phase: str, connection: sqlite3.Connection = Depends(get_db)):
    context = _phase_context(connection, phase)
    context["note"] = notes.get_note(connection, "PHASE", phase)
    return templates.TemplateResponse(request, "adm_phase.html", base_context(request, connection, **context))


async def technique_page(request: Request, code: str, connection: sqlite3.Connection = Depends(get_db)):
    technique = adm.technique(connection, code)
    if technique is None:
        raise HTTPException(404, f"No ADM technique {code}")
    return templates.TemplateResponse(
        request, "adm_technique.html", base_context(request, connection, technique=technique)
    )


async def artefact_page(
    request: Request,
    phase: str = "",
    domain: str = "",
    kind: str = "",
    archimate: str = "",
    connection: sqlite3.Connection = Depends(get_db),
):
    rows = adm.artefacts(connection, phase, domain, kind, archimate_only=archimate == "1")
    views = {row["code"] for row in rows if (ARCHIMATE_DIR / f"{row['code']}.svg").is_file()}
    context = base_context(
        request,
        connection,
        rows=rows,
        views=views,
        filters=adm.artefact_filters(connection),
        phase_names={p["code"]: p["name"] for p in adm.phases(connection)},
        selected={"phase": phase, "domain": domain, "kind": kind, "archimate": archimate},
    )
    template = "_artefact_table.html" if request.headers.get("HX-Request") else "artefact.html"
    return templates.TemplateResponse(request, template, context)


async def artefact_example(request: Request, code: str, connection: sqlite3.Connection = Depends(get_db)):
    """Fragment showing the original example drawing shipped for one artefact under static/artefact/."""
    artefact = adm.artefact(connection, code)
    if artefact is None or not (ARTEFACT_EXAMPLE_DIR / f"{code}.svg").is_file():
        raise HTTPException(404, f"No example drawing for artefact {code}")
    section_ref = artefact["refs"][0]
    has_view = (ARCHIMATE_DIR / f"{code}.svg").is_file()
    return templates.TemplateResponse(
        request,
        "_artefact_example.html",
        base_context(
            request,
            connection,
            artefact=artefact,
            svg_url=f"/static/artefact/{code}.svg",
            archimate_url=f"/static/archimate/{code}.svg" if has_view else None,
            examples=adm.artefact_examples(connection, code),
            section_ref=section_ref,
        ),
    )
