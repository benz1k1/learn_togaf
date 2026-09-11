"""
``create_app()`` and the module-level ``app`` (learn_togaf.md §5).

One process: FastAPI serving htmx pages plus the handful of ``/api`` JSON endpoints the pages
use. The lifespan opens the database, applies the schema and loads ``content/`` when the cache
is empty. Because ``lifespan=`` is set, ``@app.on_event`` does not run — start-up work goes here.
"""

import sys
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from loguru import logger
from starlette.exceptions import HTTPException as StarletteHTTPException

from learn_togaf.config import CONTENT_DIR, LOG_DIR, LOG_LEVEL, SOURCES_DIR
from learn_togaf.content.loader import ContentError, load_all
from learn_togaf.db import apply_schema, connect
from learn_togaf.pages.security import CsrfMiddleware
from learn_togaf.pages.static_files import CachedStaticFiles
from learn_togaf.pages.templating import templates
from learn_togaf.pages.urls import register_page_routes

_STATIC_DIR = Path(__file__).with_name("pages") / "static"


def _configure_logging() -> None:
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    logger.remove()
    logger.add(sys.stderr, level=LOG_LEVEL)
    logger.add(LOG_DIR / "learn_togaf.log", level=LOG_LEVEL, rotation="10 MB", retention=5)
    logger.add(LOG_DIR / "learn_togaf_errors.log", level="ERROR", rotation="10 MB", retention=5)


@asynccontextmanager
async def lifespan(app: FastAPI):
    _configure_logging()
    SOURCES_DIR.mkdir(parents=True, exist_ok=True)
    connection = connect()
    try:
        apply_schema(connection)
        units = connection.execute("SELECT COUNT(*) FROM learning_unit").fetchone()[0]
        if units == 0:
            load_all(connection, CONTENT_DIR)
    finally:
        connection.close()
    logger.info("learn_togaf ready")
    yield


def _wants_html(request: Request) -> bool:
    return not request.url.path.startswith("/api/") and "text/html" in request.headers.get("accept", "")


def create_app() -> FastAPI:
    app = FastAPI(title="Learn TOGAF", lifespan=lifespan, docs_url=None, redoc_url=None)
    app.mount("/static", CachedStaticFiles(directory=str(_STATIC_DIR)), name="static")
    register_page_routes(app)

    @app.exception_handler(ContentError)
    async def content_error(request: Request, exc: ContentError):
        logger.error(f"content error: {exc}")
        if _wants_html(request):
            return templates.TemplateResponse(
                request, "error.html", {"request": request, "message": str(exc)}, status_code=422
            )
        return JSONResponse({"success": False, "error": str(exc)}, status_code=422)

    @app.exception_handler(StarletteHTTPException)
    async def http_error(request: Request, exc: StarletteHTTPException):
        if _wants_html(request) and exc.status_code in (403, 404):
            return templates.TemplateResponse(
                request,
                "error.html",
                {"request": request, "message": exc.detail or "Not found"},
                status_code=exc.status_code,
            )
        return JSONResponse({"success": False, "error": exc.detail}, status_code=exc.status_code)

    @app.exception_handler(RequestValidationError)
    async def validation_error(request: Request, exc: RequestValidationError):
        return JSONResponse({"success": False, "error": exc.errors()}, status_code=422)

    @app.exception_handler(Exception)
    async def unhandled(request: Request, exc: Exception):
        logger.exception(f"unhandled error on {request.method} {request.url.path}: {exc}")
        if _wants_html(request):
            return templates.TemplateResponse(
                request, "error.html", {"request": request, "message": str(exc)}, status_code=500
            )
        return JSONResponse({"success": False, "error": str(exc)}, status_code=500)

    # add_middleware puts the last-added outermost; CSRF is the only one, so it wraps everything.
    app.add_middleware(CsrfMiddleware)
    return app


app = create_app()
