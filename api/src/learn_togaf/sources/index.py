"""
The source index (learn_togaf.md §1.4, §3): saved HTML → ``source_document`` /
``source_section``, PDF outlines → ``pdf_page``, one Markdown file per section under
``text/``, ``objective_source`` from the hand-kept ``objective_sections.yaml``, and the ADM
phase-chapter lists parsed and diffed against ``content/adm/phases.yaml``.

Two id forms meet here. A section's id is ``"<DOC>:<anchor>"``; the refs that ``content/``
carries are ``"<DOC> §<number>"`` (``content/models.validate_ref``). :func:`section_ref` and
:func:`resolve_ref` translate between them using the number the heading starts with.
"""

import re
import sqlite3
from dataclasses import dataclass, field
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import yaml
from loguru import logger

from learn_togaf.content.models import DOCUMENT_CODES, content_hash
from learn_togaf.db import transaction
from learn_togaf.sources.parse_html import ParsedPage, ParsedSection, split_heading

# The Digital Edition publishes each document under two or three slugs: a short one ("adm",
# "business-scenarios"), a long one ("architecture-development-method",
# "togaf-series-guide-business-scenarios") and a one-page ".single" rendering. One slug per
# document is indexed; the aliases below fold the long core names onto the short ones, and every
# "togaf-series-guide-*" or ".single" segment is skipped as a duplicate of its short slug.
SEGMENT_CODES = {
    "introduction": "INTRO",
    "introduction-and-core-concepts": "INTRO",
    "adm": "ADM",
    "architecture-development-method": "ADM",
    "adm-techniques": "TECH",
    "applying-the-adm": "APPLY",
    "architecture-content": "CONTENT",
    "ea-capability-and-governance": "GOV",
    "capability-and-governance": "GOV",
}
CANONICAL_SEGMENTS = {"INTRO": "introduction", "ADM": "adm", "TECH": "adm-techniques", "APPLY": "applying-the-adm", "CONTENT": "architecture-content", "GOV": "ea-capability-and-governance"}
# Not documents: the publication root, its info and help pages, the guides listing, redirectors.
NON_DOCUMENT_SEGMENTS = {"root", "info", "v2022", "reference-models", "index.html"}
_REF_RE = re.compile(r"^(?P<doc>[A-Z]+)(?::(?P<guide>[A-Za-z0-9_\-]+))?\s+§(?P<number>[0-9][0-9A-Za-z.\-]*)")
_LIST_ITEM_RE = re.compile(r"^(?:-|\d+\.)\s+(?P<item>.+?)\s*$")  # top-level items only
_PHASE_TITLE_RE = re.compile(
    r"^(?:Preliminary Phase|Phase (?P<letter>[A-H])\b|(?:ADM Architecture )?Requirements Management)", re.IGNORECASE
)
PHASE_FIELDS = {
    "objectives": "objective",
    "approach": "approach",
    "inputs": "inputs",
    "steps": "steps",
    "outputs": "outputs",
}
OBJECTIVE_MAPPING_FILE = "objective_sections.yaml"


def document_code(segment: str) -> str | None:
    """``adm`` → ``ADM``; a guide's short slug → ``GUIDE:<slug>``; duplicates (the long
    ``togaf-series-guide-*`` names, ``.single`` renderings) and non-documents (root, info, the
    guides listing, ``*.html`` help pages) return None."""
    if segment.endswith(".single") or "." in segment or segment in NON_DOCUMENT_SEGMENTS:
        return None
    if segment.startswith("guides/"):
        return f"GUIDE:{segment.split('/', 1)[1]}"
    if segment in SEGMENT_CODES:
        code = SEGMENT_CODES[segment]
        return code if CANONICAL_SEGMENTS[code] == segment else None
    if segment.startswith("togaf-series-guide-"):
        return None
    return f"GUIDE:{segment}"


def segment_for_code(code: str) -> str:
    if code.startswith("GUIDE:"):
        return code.split(":", 1)[1]
    if code in CANONICAL_SEGMENTS:
        return CANONICAL_SEGMENTS[code]
    raise ValueError(f"{code!r} is not a source document code")


def document_kind(code: str) -> str:
    return "GUIDE" if code.startswith("GUIDE:") else "STANDARD"


def document_title(code: str, page_title: str) -> str:
    if code.startswith("GUIDE:"):
        return page_title or f"TOGAF Series Guide: {code.split(':', 1)[1]}"
    return DOCUMENT_CODES[code]


# ---------------------------------------------------------------- refs ↔ ids
def section_ref(document_code: str, heading_path: str) -> str | None:
    """The ``"<DOC> §<number>"`` ref of a section, from the number its heading starts with."""
    number, _ = split_heading(heading_path.rsplit(" › ", 1)[-1])
    return f"{document_code} §{number}" if number else None


def section_number(heading_path: str) -> str | None:
    return split_heading(heading_path.rsplit(" › ", 1)[-1])[0]


def parse_ref(ref: str) -> tuple[str, str]:
    """``"ADM §3.3 Inputs"`` → ``("ADM", "3.3")``; ``"GUIDE:business-scenarios §2"`` → ``("GUIDE:business-scenarios", "2")``."""
    match = _REF_RE.match(ref.strip())
    if not match:
        raise ValueError(f"ref {ref!r} is not '<DOC> §<number>'")
    doc = match.group("doc")
    if match.group("guide"):
        doc = f"{doc}:{match.group('guide')}"
    return doc, match.group("number")


def resolve_ref(connection: sqlite3.Connection, ref: str) -> list[sqlite3.Row]:
    """The sections a ref names: same document, heading number equal to the ref's number
    (or the anchor itself, for an unnumbered heading cited by anchor)."""
    doc, number = parse_ref(ref)
    rows = connection.execute(
        "SELECT * FROM source_section WHERE document_code = ? ORDER BY ordinal", (doc,)
    ).fetchall()
    return [
        row for row in rows if section_number(row["heading_path"]) == number or row["id"] == f"{doc}:{number}"
    ]


def section_with_descendants(connection: sqlite3.Connection, section_id: str) -> list[sqlite3.Row]:
    """The section and every section beneath it in the heading tree, in reading order — the
    spec's "text until the next heading of the same or a higher level"."""
    row = connection.execute("SELECT * FROM source_section WHERE id = ?", (section_id,)).fetchone()
    if row is None:
        raise ValueError(f"unknown section id {section_id!r}")
    prefix = row["heading_path"] + " › "
    rows = connection.execute(
        "SELECT * FROM source_section WHERE document_code = ? AND ordinal >= ? ORDER BY ordinal",
        (row["document_code"], row["ordinal"]),
    ).fetchall()
    return [
        candidate
        for candidate in rows
        if candidate["id"] == section_id or candidate["heading_path"].startswith(prefix)
    ]


# ---------------------------------------------------------------- HTML → tables
def upsert_document(
    connection: sqlite3.Connection, code: str, title: str, html_url: str, pdf_path: str | None, digest: str
) -> None:
    connection.execute(
        "INSERT INTO source_document(code, title, kind, html_url, pdf_path, fetched_at, content_hash) VALUES (?,?,?,?,?,?,?)"
        " ON CONFLICT(code) DO UPDATE SET title=excluded.title, html_url=COALESCE(excluded.html_url, html_url),"
        " pdf_path=COALESCE(excluded.pdf_path, pdf_path), fetched_at=excluded.fetched_at, content_hash=excluded.content_hash",
        (
            code,
            title,
            document_kind(code),
            html_url,
            pdf_path,
            datetime.now(UTC).isoformat(timespec="seconds"),
            digest,
        ),
    )


def index_document(
    connection: sqlite3.Connection,
    code: str,
    pages: list[ParsedPage],
    pdf_pages: dict[str, int] | None = None,
    pdf_path: str | None = None,
) -> list[ParsedSection]:
    """Upsert one document's sections from its pages (in crawl order); sections that vanished
    from the pages are deleted. Ordinals run across pages. Returns the sections written."""
    sections: list[ParsedSection] = []
    ordinal = 0
    for page in pages:
        for section in page.sections:
            ordinal += 1
            section.ordinal = ordinal
            sections.append(section)
    if not sections:
        # A slug with pages but no anchored headings is a listing or a redirector, not a document.
        logger.warning(f"document {code}: no anchored h1–h4 headings in {len(pages)} page(s); skipped")
        return 0
    title = document_title(code, pages[0].title)
    digest = content_hash(*(section.text for section in sections))
    pdf_pages = pdf_pages or {}
    with transaction(connection):
        upsert_document(connection, code, title, pages[0].url, pdf_path, digest)
        for section in sections:
            connection.execute(
                "INSERT INTO source_section(id, document_code, heading_path, anchor_url, pdf_page, ordinal, text, content_hash)"
                " VALUES (?,?,?,?,?,?,?,?)"
                " ON CONFLICT(id) DO UPDATE SET heading_path=excluded.heading_path, anchor_url=excluded.anchor_url,"
                " pdf_page=COALESCE(excluded.pdf_page, pdf_page), ordinal=excluded.ordinal, text=excluded.text,"
                " content_hash=excluded.content_hash",
                (
                    section.id,
                    code,
                    section.heading_path,
                    section.anchor_url,
                    pdf_pages.get(section.number) if section.number else None,
                    section.ordinal,
                    section.text,
                    content_hash(section.heading_path, section.text),
                ),
            )
        keep = [section.id for section in sections]
        placeholders = ",".join("?" * len(keep))
        connection.execute(
            f"DELETE FROM source_section WHERE document_code = ? AND id NOT IN ({placeholders})",
            (code, *keep),
        )
    logger.info(f"indexed {code}: {len(sections)} sections from {len(pages)} page(s)")
    return sections


def apply_pdf_pages(
    connection: sqlite3.Connection, code: str, pdf_pages: dict[str, int], pdf_path: str
) -> int:
    """Set ``pdf_page`` on the sections whose heading number is in the PDF outline."""
    updated = 0
    with transaction(connection):
        connection.execute("UPDATE source_document SET pdf_path = ? WHERE code = ?", (pdf_path, code))
        for row in connection.execute(
            "SELECT id, heading_path FROM source_section WHERE document_code = ?", (code,)
        ).fetchall():
            number = section_number(row["heading_path"])
            if number and number in pdf_pages:
                connection.execute(
                    "UPDATE source_section SET pdf_page = ? WHERE id = ?", (pdf_pages[number], row["id"])
                )
                updated += 1
    return updated


# ---------------------------------------------------------------- text files
def write_text_files(connection: sqlite3.Connection, sources_dir: Path) -> int:
    """``text/<doc>/<section_id>.md`` — one file per section, heading path first."""
    written = 0
    for row in connection.execute("SELECT * FROM source_section ORDER BY document_code, ordinal"):
        directory = sources_dir / "text" / segment_for_code(row["document_code"])
        directory.mkdir(parents=True, exist_ok=True)
        ref = section_ref(row["document_code"], row["heading_path"]) or ""
        header = [
            f"# {row['heading_path']}",
            "",
            f"- id: {row['id']}",
            f"- ref: {ref}",
            f"- anchor: {row['anchor_url'] or ''}",
            f"- pdf_page: {row['pdf_page'] if row['pdf_page'] is not None else ''}",
            "",
        ]
        (directory / f"{row['id']}.md").write_text("\n".join(header) + row["text"] + "\n", encoding="utf-8")
        written += 1
    return written


# ---------------------------------------------------------------- objective mapping
def load_objective_mapping(path: Path) -> dict[str, list[str]]:
    """``objective code → [section id | "<DOC> › <number>" heading-path prefix]``."""
    if not path.is_file():
        raise FileNotFoundError(f"{path} is missing; it maps blueprint objectives to source sections")
    with open(path, encoding="utf-8") as handle:
        raw = yaml.safe_load(handle) or {}
    if not isinstance(raw, dict):
        raise ValueError(f"{path}: expected a mapping of objective code → list of section specs")
    mapping: dict[str, list[str]] = {}
    for code, specs in raw.items():
        if not isinstance(specs, list) or not all(isinstance(spec, str) for spec in specs):
            raise ValueError(f"{path}: objective {code!r}: expected a list of strings")
        mapping[str(code)] = specs
    return mapping


def match_sections(connection: sqlite3.Connection, spec: str) -> list[str]:
    """Section ids for one mapping entry. ``"ADM:sec-3-3"`` is an exact id. ``"ADM › 3"`` matches
    every section of ADM whose heading number is ``3`` or ``3.x…``; ``"ADM › 3.3"`` likewise
    below it. A spec with no number (``"ADM › Preface"``) is a plain heading-path prefix."""
    if " › " not in spec:
        row = connection.execute("SELECT id FROM source_section WHERE id = ?", (spec,)).fetchone()
        if row:
            return [row["id"]]
        # A bare document code ("GUIDE:business-scenarios") is the whole document.
        return [
            r["id"]
            for r in connection.execute(
                "SELECT id FROM source_section WHERE document_code = ? ORDER BY ordinal", (spec,)
            ).fetchall()
        ]
    doc, rest = spec.split(" › ", 1)
    rows = connection.execute(
        "SELECT id, heading_path FROM source_section WHERE document_code = ? ORDER BY ordinal", (doc,)
    ).fetchall()
    number, _ = split_heading(rest + " x") if rest and rest[0].isdigit() else (None, rest)
    if number:
        return [
            row["id"]
            for row in rows
            if (own := section_number(row["heading_path"]))
            and (own == number or own.startswith(number + "."))
        ]
    return [row["id"] for row in rows if row["heading_path"].startswith(spec)]


def apply_objective_mapping(
    connection: sqlite3.Connection, mapping: dict[str, list[str]], objective_codes: set[str]
) -> dict[str, int]:
    """Rewrite ``objective_source`` from the mapping. Returns objective → sections matched;
    an objective in the mapping that the blueprint does not know is an error."""
    unknown = sorted(set(mapping) - objective_codes)
    if unknown:
        raise ValueError(f"objective_sections.yaml names objectives not in blueprint.yaml: {unknown}")
    counts: dict[str, int] = {}
    with transaction(connection):
        connection.execute("DELETE FROM objective_source")
        for code, specs in mapping.items():
            ids: list[str] = []
            for spec in specs:
                ids.extend(
                    section_id for section_id in match_sections(connection, spec) if section_id not in ids
                )
            for section_id in ids:
                connection.execute(
                    "INSERT INTO objective_source(objective_code, section_id) VALUES (?,?)",
                    (code, section_id),
                )
            counts[code] = len(ids)
    return counts


# ---------------------------------------------------------------- ADM phase lists
@dataclass
class ParsedPhase:
    code: str
    name: str
    objective: list[str] = field(default_factory=list)
    approach: str = ""
    inputs: list[str] = field(default_factory=list)
    steps: list[str] = field(default_factory=list)
    outputs: list[str] = field(default_factory=list)
    refs: list[str] = field(default_factory=list)

    def as_dict(self) -> dict[str, Any]:
        return {
            "code": self.code,
            "name": self.name,
            "objective": self.objective,
            "approach": self.approach,
            "inputs": self.inputs,
            "steps": self.steps,
            "outputs": self.outputs,
            "refs": self.refs,
        }


def phase_code(title: str) -> str | None:
    match = _PHASE_TITLE_RE.match(title)
    if not match:
        return None
    if title.lower().startswith("preliminary"):
        return "PRELIM"
    if title.lower().startswith("requirements"):
        return "REQ"
    return match.group("letter").upper()


def list_items(text: str) -> list[str]:
    return [match.group("item") for line in text.splitlines() if (match := _LIST_ITEM_RE.match(line))]


def parse_adm_phases(connection: sqlite3.Connection) -> dict[str, ParsedPhase]:
    """The ADM chapters whose title names a phase, with their Objectives / Approach / Inputs /
    Steps / Outputs sub-sections read as lists."""
    phases: dict[str, ParsedPhase] = {}
    rows = connection.execute(
        "SELECT * FROM source_section WHERE document_code = 'ADM' ORDER BY ordinal"
    ).fetchall()
    for row in rows:
        _, title = split_heading(row["heading_path"].rsplit(" › ", 1)[-1])
        code = phase_code(title)
        if code is None or code in phases:
            continue
        phase = ParsedPhase(
            code=code, name=title, refs=[ref for ref in [section_ref("ADM", row["heading_path"])] if ref]
        )
        for child in section_with_descendants(connection, row["id"])[1:]:
            _, child_title = split_heading(child["heading_path"].rsplit(" › ", 1)[-1])
            fieldname = PHASE_FIELDS.get(child_title.lower())
            if fieldname == "approach":
                phase.approach = " ".join(line for line in child["text"].splitlines() if line.strip())
            elif fieldname:
                setattr(phase, fieldname, list_items(child["text"]))
        phases[code] = phase
    return phases


def diff_adm_phases(parsed: dict[str, ParsedPhase], authored: list[dict[str, Any]]) -> list[str]:
    """Human-readable differences between the parsed lists and ``adm/phases.yaml``."""
    lines: list[str] = []
    by_code = {str(phase.get("code")): phase for phase in authored}
    for code in sorted(set(parsed) | set(by_code)):
        if code not in parsed:
            lines.append(f"{code}: in phases.yaml but no ADM chapter parsed for it")
            continue
        if code not in by_code:
            lines.append(f"{code}: parsed from the ADM but not in phases.yaml")
            continue
        for fieldname in ("objective", "inputs", "steps", "outputs"):
            ours = [str(item) for item in by_code[code].get(fieldname, [])]
            theirs = getattr(parsed[code], fieldname)
            for item in theirs:
                if item not in ours:
                    lines.append(f"{code}.{fieldname}: + {item}")
            for item in ours:
                if item not in theirs:
                    lines.append(f"{code}.{fieldname}: - {item}")
    return lines


def write_parsed_phases(content_dir: Path, parsed: dict[str, ParsedPhase]) -> Path:
    path = content_dir / "review" / "adm_phases.parsed.yaml"
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(
            "# Parsed from the ADM phase chapters by `python sources.py index`. Review against adm/phases.yaml; not loaded.\n"
        )
        yaml.safe_dump(
            [phase.as_dict() for phase in parsed.values()],
            handle,
            sort_keys=False,
            allow_unicode=True,
            width=110,
        )
    return path
