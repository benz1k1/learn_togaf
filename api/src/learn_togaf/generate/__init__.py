"""
The generation pipeline's shared layer (learn_togaf.md §1.5): grounding lookups over
``objective_source`` / ``source_section`` / ``source_figure``, the prompt files, the cache-able
system blocks, the ref check that rejects an item citing a section outside its input, and the
draft writers for ``content/review/``. Each stage module builds :class:`Request` objects from
this and hands them to :mod:`learn_togaf.generate.client`.

Two rules live here so no stage can skip them: **nothing is generated without a section id in
hand** (:func:`grounding_for_objective` refuses an objective with no ``objective_source`` row),
and **an item whose refs cite a section outside its input is rejected** (:func:`check_refs`).
"""

import base64
import re
import sqlite3
from dataclasses import dataclass, field
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import orjson
import pymupdf
import yaml
from loguru import logger

from learn_togaf.content.models import Blueprint
from learn_togaf.sources.index import section_ref

PROMPTS_DIR = Path(__file__).with_name("prompts")
IMAGE_MEDIA_TYPES = {
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".gif": "image/gif",
    ".webp": "image/webp",
}
_INLINE_REF_RE = re.compile(r"\[(?P<ref>[A-Z]+(?::[A-Za-z0-9_\-]+)?\s+§[0-9][0-9A-Za-z.\-]*)\]")


class GroundingError(SystemExit):
    """An objective has no mapped sections: the stage refuses to run (§1.5)."""


class RefsOutsideInput(ValueError):
    """A generated item cites a section it was not given."""


@dataclass
class FigureInput:
    id: str
    caption: str
    file_path: Path
    section_id: str | None


@dataclass
class SectionInput:
    id: str
    ref: str
    heading_path: str
    text: str
    anchor_url: str
    figures: list[FigureInput] = field(default_factory=list)


@dataclass
class Grounding:
    objective_code: str
    objective_text: str
    unit_code: str
    sections: list[SectionInput]

    @property
    def refs(self) -> list[str]:
        return [section.ref for section in self.sections]

    @property
    def section_ids(self) -> list[str]:
        return [section.id for section in self.sections]

    @property
    def figures(self) -> list[FigureInput]:
        return [figure for section in self.sections for figure in section.figures]


def now_iso() -> str:
    return datetime.now(UTC).isoformat(timespec="seconds")


def today() -> str:
    return datetime.now(UTC).date().isoformat()


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")[:60] or "lesson"


def load_prompt(stage: str) -> str:
    path = PROMPTS_DIR / f"{stage}.md"
    if not path.is_file():
        raise FileNotFoundError(f"prompt file {path} is missing")
    return path.read_text(encoding="utf-8")


# ---------------------------------------------------------------- grounding
def _figures_for_section(connection: sqlite3.Connection, section_id: str) -> list[FigureInput]:
    rows = connection.execute(
        "SELECT id, caption, file_path, section_id FROM source_figure WHERE section_id = ? ORDER BY id",
        (section_id,),
    ).fetchall()
    return [FigureInput(row["id"], row["caption"], Path(row["file_path"]), row["section_id"]) for row in rows]


def sections_by_ids(connection: sqlite3.Connection, section_ids: list[str]) -> list[SectionInput]:
    """Sections in reading order. A section whose heading has no number cannot be cited in
    the ``"<DOC> §<n>"`` ref grammar, so it is left out with a log line."""
    if not section_ids:
        return []
    placeholders = ",".join("?" * len(section_ids))
    rows = connection.execute(
        f"SELECT * FROM source_section WHERE id IN ({placeholders}) ORDER BY document_code, ordinal",
        section_ids,
    ).fetchall()
    sections: list[SectionInput] = []
    for row in rows:
        ref = section_ref(row["document_code"], row["heading_path"])
        if ref is None:
            logger.info(
                f"section {row['id']} has an unnumbered heading and cannot be cited; left out of the input"
            )
            continue
        sections.append(
            SectionInput(
                id=row["id"],
                ref=ref,
                heading_path=row["heading_path"],
                text=row["text"],
                anchor_url=row["anchor_url"] or "",
                figures=_figures_for_section(connection, row["id"]),
            )
        )
    return sections


def grounding_for_objective(
    connection: sqlite3.Connection, blueprint: Blueprint, objective_code: str
) -> Grounding:
    unit_code = blueprint.objective_unit().get(objective_code)
    if unit_code is None:
        raise ValueError(f"objective {objective_code!r} is not in blueprint.yaml")
    objective_text = next(o.text for u in blueprint.units for o in u.objectives if o.code == objective_code)
    ids = [
        row["section_id"]
        for row in connection.execute(
            "SELECT section_id FROM objective_source WHERE objective_code = ? ORDER BY section_id",
            (objective_code,),
        )
    ]
    sections = sections_by_ids(connection, ids)
    if not sections:
        raise GroundingError(
            f"objective {objective_code} ({unit_code}) has no objective_source rows: nothing is generated without a "
            f"section id in hand. Map it in resources/sources/objective_sections.yaml and run: python sources.py index"
        )
    return Grounding(
        objective_code=objective_code, objective_text=objective_text, unit_code=unit_code, sections=sections
    )


def grounding_for_unit(
    connection: sqlite3.Connection, blueprint: Blueprint, unit_code: str
) -> list[Grounding]:
    unit = next((u for u in blueprint.units if u.code == unit_code), None)
    if unit is None:
        raise SystemExit(f"unit {unit_code!r} is not in blueprint.yaml ({', '.join(blueprint.unit_codes())})")
    if not unit.objectives:
        raise SystemExit(f"unit {unit_code} has no objectives in blueprint.yaml")
    return [grounding_for_objective(connection, blueprint, objective.code) for objective in unit.objectives]


# ---------------------------------------------------------------- prompt assembly
def sections_text(sections: list[SectionInput]) -> str:
    parts = []
    for section in sections:
        figures = "".join(f"\n[figure {figure.id}: {figure.caption}]" for figure in section.figures)
        parts.append(f"### [{section.ref}] {section.heading_path}\n{section.text}{figures}")
    return "\n\n".join(parts)


def system_blocks(prompt: str, sections: list[SectionInput]) -> list[dict[str, Any]]:
    """The stage prompt, then the section text as one cached block (prompt caching, §1.5).
    The section block is the stable, large part; the per-item instruction goes in the user turn."""
    return [
        {"type": "text", "text": prompt},
        {
            "type": "text",
            "text": "SOURCE SECTIONS (cite by the [ref] in brackets):\n\n" + sections_text(sections),
            "cache_control": {"type": "ephemeral"},
        },
    ]


def image_block(figure: FigureInput) -> dict[str, Any]:
    """An image content block for a stored figure; SVG is rasterised through pymupdf."""
    suffix = figure.file_path.suffix.lower()
    if suffix == ".svg":
        with pymupdf.open(figure.file_path) as document:
            data = document[0].get_pixmap(dpi=144).tobytes("png")
        media_type = "image/png"
    else:
        if suffix not in IMAGE_MEDIA_TYPES:
            raise ValueError(
                f"figure {figure.id}: {figure.file_path.suffix} is not an image type the API accepts"
            )
        data = figure.file_path.read_bytes()
        media_type = IMAGE_MEDIA_TYPES[suffix]
    return {
        "type": "image",
        "source": {"type": "base64", "media_type": media_type, "data": base64.b64encode(data).decode()},
    }


def parse_json(text: str) -> Any:
    try:
        return orjson.loads(text)
    except orjson.JSONDecodeError as exc:
        raise ValueError(f"model output is not JSON: {exc}: {text[:200]!r}") from exc


# ---------------------------------------------------------------- the ref gate
def check_refs(refs: list[str], allowed: list[str], what: str) -> list[str]:
    """Every ref must be one the item was given. Returns the refs, normalised."""
    cleaned = [ref.strip() for ref in refs]
    outside = sorted(set(cleaned) - set(allowed))
    if outside:
        raise RefsOutsideInput(f"{what} cites sections outside its input: {outside} (allowed: {allowed})")
    if not cleaned:
        raise RefsOutsideInput(f"{what} cites no section at all")
    return cleaned


def inline_refs(body: str) -> list[str]:
    return [match.group("ref") for match in _INLINE_REF_RE.finditer(body)]


# ---------------------------------------------------------------- draft files
def review_dir(content_dir: Path) -> Path:
    path = content_dir / "review"
    path.mkdir(parents=True, exist_ok=True)
    return path


def set_code(unit_code: str, date: str | None = None) -> str:
    return f"G_{unit_code}_{date or today()}"


def write_yaml(path: Path, comment: str, data: Any) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(f"# {comment}\n")
        yaml.safe_dump(data, handle, sort_keys=False, allow_unicode=True, width=110)
    return path


def write_markdown(path: Path, front: dict[str, Any], body: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    front_text = yaml.safe_dump(front, sort_keys=False, allow_unicode=True, width=110).rstrip()
    path.write_text(f"---\n{front_text}\n---\n{body.strip()}\n", encoding="utf-8")
    return path
