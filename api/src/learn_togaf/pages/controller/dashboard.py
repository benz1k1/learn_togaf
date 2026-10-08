"""Dashboard (learn_togaf.md §4.1) and the content-reload endpoint."""

import sqlite3
from dataclasses import asdict

from fastapi import Depends
from fastapi.responses import JSONResponse
from loguru import logger
from starlette.requests import Request

from learn_togaf.config import CONTENT_DIR
from learn_togaf.content.loader import load_all
from learn_togaf.deps import get_db
from learn_togaf.pages.context import base_context, exam_dates, get_setting
from learn_togaf.pages.templating import templates
from learn_togaf.service import readiness


async def dashboard(request: Request, connection: sqlite3.Connection = Depends(get_db)):
    data = readiness.dashboard_data(connection, exam_dates(connection), get_setting(connection, "plan_json"))
    return templates.TemplateResponse(request, "dashboard.html", base_context(request, connection, **data))


async def reload_content(request: Request, connection: sqlite3.Connection = Depends(get_db)):
    report = load_all(connection, CONTENT_DIR)
    logger.info(f"content reloaded from the dashboard: {report.summary()}")
    return JSONResponse({"success": True, "report": asdict(report)})
