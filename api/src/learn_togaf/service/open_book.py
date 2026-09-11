"""
The open-book panel (learn_togaf.md §0, §4.6): the reference the learner may search while
answering a Practitioner scenario, the way the standard is available in the real exam.

One LIKE search over the source index (heading path and text), the glossary, and the ADM
phases, techniques and artefacts by name. Every hit carries the page it links to.
"""

import sqlite3
from typing import Any

MAX_RESULTS = 25


def _like(term: str) -> str:
    return f"%{term}%"


def search(connection: sqlite3.Connection, query: str, limit: int = MAX_RESULTS) -> list[dict[str, Any]]:
    term = " ".join(query.split())
    if len(term) < 2:
        return []
    pattern = _like(term)
    results: list[dict[str, Any]] = []
    for row in connection.execute(
        "SELECT id, document_code, heading_path, pdf_page, substr(text, 1, 200) AS snippet FROM source_section"
        " WHERE heading_path LIKE ? OR text LIKE ? ORDER BY document_code, ordinal LIMIT ?",
        (pattern, pattern, limit),
    ):
        results.append(
            {
                "kind": "section",
                "title": row["heading_path"],
                "subtitle": f"{row['document_code']}"
                + (f" · PDF p.{row['pdf_page']}" if row["pdf_page"] else ""),
                "snippet": row["snippet"],
                "href": f"/source/{row['id']}",
            }
        )
    for row in connection.execute(
        "SELECT id, term, definition, document, section FROM glossary_term WHERE term LIKE ? OR definition LIKE ?"
        " ORDER BY term LIMIT ?",
        (pattern, pattern, limit),
    ):
        results.append(
            {
                "kind": "term",
                "title": row["term"],
                "subtitle": f"{row['document']} §{row['section']}",
                "snippet": row["definition"][:200],
                "href": f"/glossary/{row['id']}",
            }
        )
    for row in connection.execute(
        "SELECT code, name, approach FROM adm_phase WHERE name LIKE ? OR code LIKE ? ORDER BY ordinal LIMIT ?",
        (pattern, pattern, limit),
    ):
        results.append(
            {
                "kind": "phase",
                "title": row["name"],
                "subtitle": "ADM phase",
                "snippet": row["approach"][:200],
                "href": f"/adm/{row['code']}",
            }
        )
    for row in connection.execute(
        "SELECT code, name, purpose FROM adm_technique WHERE name LIKE ? OR purpose LIKE ? ORDER BY name LIMIT ?",
        (pattern, pattern, limit),
    ):
        results.append(
            {
                "kind": "technique",
                "title": row["name"],
                "subtitle": "ADM technique",
                "snippet": row["purpose"][:200],
                "href": f"/adm/technique/{row['code']}",
            }
        )
    for row in connection.execute(
        "SELECT code, name, kind, phase_code, purpose FROM adm_artefact WHERE name LIKE ? ORDER BY name LIMIT ?",
        (pattern, limit),
    ):
        results.append(
            {
                "kind": "artefact",
                "title": row["name"],
                "subtitle": f"{row['kind'].title()} · Phase {row['phase_code']}",
                "snippet": row["purpose"][:200],
                "href": f"/artefact#{row['code']}",
            }
        )
    return results[:limit]
