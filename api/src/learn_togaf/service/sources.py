"""
The source index pages' data (learn_togaf.md §1.4, §5.1): documents with their section and
figure counts, a LIKE search over heading paths and text, one section with its figures and the
content that cites it, and the figure file path — resolved under ``config.SOURCES_DIR`` and
refused outside it. The tables are filled by ``python sources.py fetch``; empty is normal.
"""

import re
import sqlite3
from pathlib import Path

import orjson

from learn_togaf.config import SOURCES_DIR

_HEADING_NUMBER_RE = re.compile(r"^\s*(?P<number>\d+(?:\.\d+)*)\b")
_REF_RE = re.compile(r"^(?P<doc>[A-Z]+(?::[A-Za-z0-9_\-]+)?)\s+§(?P<section>[0-9][0-9A-Za-z.\-]*)")


def list_documents(connection: sqlite3.Connection) -> list[sqlite3.Row]:
    return connection.execute(
        "SELECT d.code, d.title, d.kind, d.html_url, d.pdf_path, d.fetched_at,"
        " (SELECT COUNT(*) FROM source_section s WHERE s.document_code = d.code) AS sections,"
        " (SELECT COUNT(*) FROM source_figure f WHERE f.document_code = d.code) AS figures"
        " FROM source_document d ORDER BY d.kind, d.code"
    ).fetchall()


def counts(connection: sqlite3.Connection) -> dict[str, int]:
    return {
        "documents": connection.execute("SELECT COUNT(*) FROM source_document").fetchone()[0],
        "sections": connection.execute("SELECT COUNT(*) FROM source_section").fetchone()[0],
        "figures": connection.execute("SELECT COUNT(*) FROM source_figure").fetchone()[0],
    }


def search_sections(connection: sqlite3.Connection, q: str, limit: int = 100) -> list[sqlite3.Row]:
    pattern = f"%{q.strip()}%"
    return connection.execute(
        "SELECT id, document_code, heading_path, anchor_url, pdf_page, substr(text, 1, 240) AS snippet"
        " FROM source_section WHERE heading_path LIKE ? OR text LIKE ?"
        " ORDER BY document_code, ordinal LIMIT ?",
        (pattern, pattern, limit),
    ).fetchall()


def get_section(connection: sqlite3.Connection, section_id: str) -> sqlite3.Row | None:
    return connection.execute(
        "SELECT s.*, d.title AS document_title FROM source_section s"
        " JOIN source_document d ON d.code = s.document_code WHERE s.id = ?",
        (section_id,),
    ).fetchone()


def section_figures(connection: sqlite3.Connection, section_id: str) -> list[sqlite3.Row]:
    return connection.execute(
        "SELECT id, caption, file_path, width, height, important FROM source_figure WHERE section_id = ? ORDER BY id",
        (section_id,),
    ).fetchall()


def ref_form(section: sqlite3.Row) -> str:
    """The "<DOC> §<n>" form refs use (§2), best-effort from the heading path's last number, else the
    id after the document code."""
    last = str(section["heading_path"]).split("›")[-1]
    match = _HEADING_NUMBER_RE.match(last)
    number = match.group("number") if match else str(section["id"]).split(":", 1)[-1]
    return f"{section['document_code']} §{number}"


def _cites(refs_json: str, doc: str, number: str) -> bool:
    for ref in orjson.loads(refs_json or "[]"):
        match = _REF_RE.match(str(ref).strip())
        if (
            match
            and match.group("doc") == doc
            and (match.group("section") == number or match.group("section").startswith(number + "."))
        ):
            return True
    return False


def citing_content(
    connection: sqlite3.Connection, section: sqlite3.Row
) -> tuple[list[sqlite3.Row], list[sqlite3.Row]]:
    """(questions, lessons) whose refs cite this section or a subsection of it."""
    doc, number = ref_form(section).split(" §", 1)
    like = f'%"{doc} §{number}%'
    questions = [
        row
        for row in connection.execute(
            "SELECT id, exam, unit_code, objective_code, set_code, status, substr(stem_or_scenario, 1, 160) AS stem, refs"
            " FROM question WHERE refs LIKE ? ORDER BY id",
            (like,),
        ).fetchall()
        if _cites(row["refs"], doc, number)
    ]
    lessons = [
        row
        for row in connection.execute(
            "SELECT id, unit_code, title, status, refs FROM lesson WHERE refs LIKE ? ORDER BY id", (like,)
        ).fetchall()
        if _cites(row["refs"], doc, number)
    ]
    return questions, lessons


def get_figure(connection: sqlite3.Connection, figure_id: str) -> sqlite3.Row | None:
    return connection.execute("SELECT * FROM source_figure WHERE id = ?", (figure_id,)).fetchone()


def figure_path(figure: sqlite3.Row) -> Path:
    """The file under SOURCES_DIR; a path that resolves outside the store is refused."""
    root = SOURCES_DIR.resolve()
    path = (root / str(figure["file_path"])).resolve()
    if root not in path.parents:
        raise PermissionError(f"figure {figure['id']} file_path escapes the source store")
    return path
