"""``generate glossary`` (learn_togaf.md §1.5): every defined term from the Definitions
sections (objective 2.1's mapping plus any section whose heading says Definitions), paraphrased,
each traceable to one section, with the source sentence kept beside it for review only."""

import sqlite3
from pathlib import Path
from typing import Any

from loguru import logger
from pydantic import ValidationError

from learn_togaf.content.loader import load_blueprint
from learn_togaf.content.models import GlossaryTerm
from learn_togaf.generate import (
    RefsOutsideInput,
    SectionInput,
    check_refs,
    client,
    grounding_for_objective,
    load_prompt,
    now_iso,
    parse_json,
    review_dir,
    sections_by_ids,
    system_blocks,
    write_yaml,
)
from learn_togaf.generate.schemas import GLOSSARY

STAGE = "glossary"
DEFINITIONS_OBJECTIVE = "2.1"


def definition_sections(connection: sqlite3.Connection, content_dir: Path) -> list[SectionInput]:
    blueprint = load_blueprint(content_dir)
    grounding = grounding_for_objective(connection, blueprint, DEFINITIONS_OBJECTIVE)
    extra = [
        row["id"]
        for row in connection.execute(
            "SELECT id FROM source_section WHERE heading_path LIKE '%Definitions%' ORDER BY document_code, ordinal"
        )
        if row["id"] not in grounding.section_ids
    ]
    return grounding.sections + sections_by_ids(connection, extra)


def build_request(sections: list[SectionInput]) -> client.Request:
    refs = [section.ref for section in sections]
    return client.Request(
        stage=STAGE,
        system=system_blocks(load_prompt(STAGE), sections),
        user=f"Build the glossary from every term these sections define. Refs you may cite (and no others): {', '.join(refs)}.",
        schema=GLOSSARY,
        custom_id="glossary",
        section_ids=[section.id for section in sections],
    )


def terms_from_response(
    text: str, allowed_refs: list[str], objective_codes: set[str]
) -> list[dict[str, Any]]:
    data = parse_json(text)
    accepted: list[dict[str, Any]] = []
    for raw in data["terms"]:
        item = {**raw, "source": "generated", "status": "draft"}
        source_sentence = item.pop("source_sentence", "")
        try:
            check_refs([item["section"]], allowed_refs, f"term {item.get('id')}")
            term = GlossaryTerm.model_validate(item)
        except (RefsOutsideInput, ValidationError) as exc:
            logger.warning(f"glossary term {raw.get('id')!r} rejected: {exc}")
            continue
        entry = term.model_dump()
        entry["source_sentence"] = source_sentence  # review aid; strip before moving to glossary.yaml
        accepted.append(entry)
    ids = {entry["id"] for entry in accepted}
    for entry in accepted:
        entry["confusable_with"] = [other for other in entry["confusable_with"] if other in ids]
    return accepted


def run(connection: sqlite3.Connection, content_dir: Path, dry_run: bool, limit: int | None) -> Path | None:
    sections = definition_sections(connection, content_dir)[:limit]
    request = build_request(sections)
    if dry_run:
        print(request.describe())
        return None
    blueprint = load_blueprint(content_dir)
    terms = terms_from_response(
        client.complete(request), [section.ref for section in sections], blueprint.objective_codes()
    )
    if not terms:
        raise SystemExit("no glossary term survived validation; nothing written")
    path = review_dir(content_dir) / "glossary.generated.yaml"
    return write_yaml(
        path,
        f"Generated glossary draft, {now_iso()} (learn_togaf.md §1.5). source_sentence is for review only — drop it when moving entries into glossary.yaml.",
        terms,
    )
