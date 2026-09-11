"""
Every diagram, downloaded (learn_togaf.md §1.4). The HTML pass re-parses the saved pages for
``<img>`` in a figure context and fetches each one through the learner's session, politely;
the PDF pass extracts every page image at native resolution. Both land in
``resources/sources/figures/<doc>/<figure_id>.<ext>`` (``:`` in the id becomes ``_`` on disk)
and in ``source_figure``; ``important=1`` when the id is listed in ``figures/important.yaml``.
"""

import hashlib
import sqlite3
import time
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlsplit

import httpx
from loguru import logger

from learn_togaf.content.loader import load_important_figures
from learn_togaf.db import transaction
from learn_togaf.sources.manifest import Manifest
from learn_togaf.sources.parse_html import ParsedFigure, parse_page
from learn_togaf.sources.parse_pdf import image_size, page_images
from learn_togaf.sources.session import LoginRequired, is_login_redirect


@dataclass
class FigureRecord:
    id: str
    document_code: str
    section_id: str | None
    caption: str
    file_path: Path
    width: int
    height: int
    content_hash: str


def figure_file_name(figure_id: str, ext: str) -> str:
    return f"{figure_id.replace(':', '_')}.{ext.lstrip('.')}"


def important_ids(sources_dir: Path) -> set[str]:
    return {figure.id for figure in load_important_figures(sources_dir)}


def html_figures(sources_dir: Path, manifest: Manifest, code_for_segment) -> dict[str, list[ParsedFigure]]:
    """Re-parse every saved page: segment → figures, in page order."""
    figures: dict[str, list[ParsedFigure]] = {}
    for segment, document in manifest.documents.items():
        code = code_for_segment(segment)
        if code is None:
            continue
        for page, entry in document.pages.items():
            path = sources_dir / "html" / segment / page
            if not path.is_file():
                continue
            parsed = parse_page(path.read_text(encoding="utf-8", errors="replace"), code, entry.url)
            figures.setdefault(segment, []).extend(parsed.figures)
    return figures


def download_figure(client: httpx.Client, figure: ParsedFigure, target_dir: Path) -> FigureRecord | None:
    ext = Path(urlsplit(figure.src).path).suffix.lstrip(".").lower() or "png"
    path = target_dir / figure_file_name(figure.id, ext)
    if path.is_file():
        data = path.read_bytes()
    else:
        response = client.get(figure.src)
        if is_login_redirect(response):
            raise LoginRequired(
                f"{figure.src} redirected to the identity provider. Run: python sources.py login"
            )
        if response.status_code != 200:
            logger.warning(f"figure {figure.id}: {figure.src} returned {response.status_code}; skipped")
            return None
        data = response.content
        target_dir.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
    width, height = image_size(path)
    return FigureRecord(
        id=figure.id,
        document_code=figure.document_code,
        section_id=figure.section_id,
        caption=figure.caption,
        file_path=path,
        width=width,
        height=height,
        content_hash=hashlib.sha256(data).hexdigest(),
    )


def download_figures(
    client: httpx.Client, figures: list[ParsedFigure], target_dir: Path, delay_seconds: float
) -> list[FigureRecord]:
    records: list[FigureRecord] = []
    for figure in figures:
        already = (target_dir / figure_file_name(figure.id, "png")).is_file()
        record = download_figure(client, figure, target_dir)
        if record is not None:
            records.append(record)
        if not already:
            time.sleep(delay_seconds)
    return records


def pdf_figures(pdf_path: Path, document_code: str, target_dir: Path) -> list[FigureRecord]:
    records: list[FigureRecord] = []
    for image in page_images(pdf_path):
        figure_id = f"{document_code}:pdf-p{image.page}-{image.index}"
        path = target_dir / figure_file_name(figure_id, image.ext)
        target_dir.mkdir(parents=True, exist_ok=True)
        path.write_bytes(image.data)
        records.append(
            FigureRecord(
                id=figure_id,
                document_code=document_code,
                section_id=None,
                caption=f"PDF page {image.page}, image {image.index}",
                file_path=path,
                width=image.width,
                height=image.height,
                content_hash=hashlib.sha256(image.data).hexdigest(),
            )
        )
    return records


def record_figures(connection: sqlite3.Connection, records: list[FigureRecord], important: set[str]) -> int:
    """Upsert into ``source_figure``. A section id the index does not know is stored as NULL
    rather than failing the whole run — the figure is still in the store and on the coverage page."""
    known = {row["id"] for row in connection.execute("SELECT id FROM source_section")}
    with transaction(connection):
        for record in records:
            connection.execute(
                "INSERT INTO source_figure(id, document_code, section_id, caption, file_path, width, height, important, content_hash)"
                " VALUES (?,?,?,?,?,?,?,?,?)"
                " ON CONFLICT(id) DO UPDATE SET section_id=excluded.section_id, caption=excluded.caption,"
                " file_path=excluded.file_path, width=excluded.width, height=excluded.height,"
                " important=excluded.important, content_hash=excluded.content_hash",
                (
                    record.id,
                    record.document_code,
                    record.section_id if record.section_id in known else None,
                    record.caption,
                    str(record.file_path),
                    record.width,
                    record.height,
                    1 if record.id in important else 0,
                    record.content_hash,
                ),
            )
    return len(records)
