"""Coverage and question quality (learn_togaf.md §4.9)."""

import sqlite3

from fastapi import Depends
from starlette.requests import Request

from learn_togaf.config import CONTENT_DIR
from learn_togaf.deps import get_db
from learn_togaf.pages.context import base_context
from learn_togaf.pages.templating import templates
from learn_togaf.service import coverage


async def coverage_page(request: Request, connection: sqlite3.Connection = Depends(get_db)):
    return templates.TemplateResponse(
        request,
        "coverage.html",
        base_context(request, connection, **coverage.report(connection, CONTENT_DIR)),
    )
