"""The import wizard pages (learn_togaf.md §4.7) and the learner-state re-import (§4.10)."""

import sqlite3
from urllib.parse import urlencode

import orjson
from fastapi import Depends, File, Form, HTTPException, UploadFile
from fastapi.responses import RedirectResponse, Response
from starlette.requests import Request

from learn_togaf.config import CONTENT_DIR
from learn_togaf.content.loader import ContentError, load_blueprint
from learn_togaf.deps import get_db
from learn_togaf.pages.context import base_context
from learn_togaf.pages.templating import templates
from learn_togaf.service import importer as importer_service
from learn_togaf.service import state as state_service

UNIT_MAP_PREFIX = "unit_map:"


def _redirect(request: Request, url: str) -> Response:
    """303 for a browser form; ``HX-Redirect`` for htmx, which would otherwise swap the
    redirected page into the fragment target."""
    if request.headers.get("hx-request"):
        return Response(status_code=200, headers={"HX-Redirect": url})
    return RedirectResponse(url, status_code=303)


def _flash(text: str, kind: str = "success") -> str:
    return "/import?" + urlencode({"flash": text, "flash_kind": kind})


def _decode(payload: bytes, file_name: str) -> str:
    try:
        return payload.decode("utf-8-sig")
    except UnicodeDecodeError as exc:
        raise ContentError(f"{file_name}: not UTF-8 text ({exc})") from exc


def _unit_overrides(form) -> dict[str, str]:
    overrides: dict[str, str] = {}
    for key, value in form.multi_items():
        if key.startswith(UNIT_MAP_PREFIX) and str(value).strip():
            overrides[key[len(UNIT_MAP_PREFIX) :]] = str(value).strip().upper()
    return overrides


async def import_page(request: Request, connection: sqlite3.Connection = Depends(get_db)):
    blueprint = load_blueprint(CONTENT_DIR)
    return templates.TemplateResponse(
        request,
        "import.html",
        base_context(
            request,
            connection,
            sets=importer_service.list_imported_sets(connection),
            units=[(unit.code, unit.exam, unit.name) for unit in blueprint.units if unit.exam],
            exams=list(blueprint.exams.values()),
        ),
    )


async def preview(
    request: Request,
    file: UploadFile = File(...),
    exam: str = Form(...),
    name: str = Form(""),
    set_code: str = Form(""),
    default_unit: str = Form(""),
    connection: sqlite3.Connection = Depends(get_db),
):
    file_name = file.filename or "upload"
    text = _decode(await file.read(), file_name)
    blueprint = load_blueprint(CONTENT_DIR)
    overrides = {"": default_unit.strip().upper()} if default_unit.strip() else {}
    result = importer_service.build_preview(
        connection, blueprint, text, file_name, exam, name, set_code, overrides
    )
    context = base_context(
        request,
        connection,
        preview=result,
        unit_choices=importer_service.unit_choices(blueprint, result.exam),
        sets=importer_service.list_imported_sets(connection),
        units=[(unit.code, unit.exam, unit.name) for unit in blueprint.units if unit.exam],
        exams=list(blueprint.exams.values()),
    )
    template = "_import_preview.html" if request.headers.get("hx-request") else "import.html"
    return templates.TemplateResponse(request, template, context)


async def confirm(
    request: Request,
    token: str = Form(...),
    import_partial: str = Form(""),
    connection: sqlite3.Connection = Depends(get_db),
):
    form = await request.form()
    blueprint = load_blueprint(CONTENT_DIR)
    result = importer_service.confirm_import(
        connection, blueprint, token, import_partial in ("on", "1", "true"), _unit_overrides(form)
    )
    text = (
        f"Imported set {result.set_code}: {result.inserted} question(s) added, "
        f"{result.skipped_duplicates} duplicate(s) and {result.skipped_errors} invalid row(s) skipped"
    )
    if result.unverified:
        text += f"; {result.unverified} unit mapping(s) unverified"
    return _redirect(request, _flash(text))


async def remove_set(request: Request, set_code: str, connection: sqlite3.Connection = Depends(get_db)):
    if not importer_service.remove_set(connection, set_code):
        raise HTTPException(status_code=404, detail=f"imported set {set_code} not found")
    return _redirect(request, _flash(f"Removed set {set_code}"))


async def import_state(
    request: Request,
    file: UploadFile = File(...),
    connection: sqlite3.Connection = Depends(get_db),
):
    file_name = file.filename or "state.json"
    raw = await file.read()
    try:
        payload = orjson.loads(raw)
    except orjson.JSONDecodeError as exc:
        raise ContentError(f"{file_name}: not JSON ({exc})") from exc
    if not isinstance(payload, dict):
        raise ContentError(f"{file_name}: a state export is a JSON object")
    report = state_service.import_state(connection, payload)
    return _redirect(request, _flash(f"State imported: {report.summary()}"))
