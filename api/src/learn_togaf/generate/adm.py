"""``generate adm`` (learn_togaf.md §1.5): the phase lists come from the parser (``sources.py
index``), not the model; the model fills only the exam traps and cross-references for the
phases and the techniques, from the ADM chapters and the techniques sections. Drafts go to
``content/review/adm/``."""

import sqlite3
from pathlib import Path
from typing import Any

import yaml
from loguru import logger
from pydantic import ValidationError

from learn_togaf.content.loader import load_blueprint
from learn_togaf.content.models import AdmPhase, AdmTechnique
from learn_togaf.generate import (
    RefsOutsideInput,
    SectionInput,
    check_refs,
    client,
    grounding_for_objective,
    inline_refs,
    load_prompt,
    now_iso,
    parse_json,
    review_dir,
    sections_by_ids,
    system_blocks,
    write_yaml,
)
from learn_togaf.generate.schemas import ADM_FILL
from learn_togaf.sources.index import parse_adm_phases

STAGE = "adm"
TECHNIQUE_OBJECTIVES = ("5.1", "5.2", "5.3", "5.4", "5.5")


def adm_sections(
    connection: sqlite3.Connection, content_dir: Path
) -> tuple[list[SectionInput], dict[str, Any]]:
    """The ADM phase chapters (every section of them) plus the technique sections mapped to
    the F5 objectives. Refuses when no ADM phase chapter is indexed."""
    parsed = parse_adm_phases(connection)
    if not parsed:
        raise SystemExit(
            "no ADM phase chapters in the index: run `python sources.py fetch` then `python sources.py index`"
        )
    blueprint = load_blueprint(content_dir)
    ids = [
        row["id"]
        for row in connection.execute(
            "SELECT id FROM source_section WHERE document_code = 'ADM' ORDER BY ordinal"
        )
    ]
    for objective in TECHNIQUE_OBJECTIVES:
        if objective in blueprint.objective_codes():
            ids.extend(
                section_id
                for section_id in grounding_for_objective(connection, blueprint, objective).section_ids
                if section_id not in ids
            )
    return sections_by_ids(connection, ids), {code: phase.as_dict() for code, phase in parsed.items()}


def build_request(
    sections: list[SectionInput], parsed: dict[str, Any], techniques: list[dict[str, Any]]
) -> client.Request:
    refs = [section.ref for section in sections]
    user = (
        "PARSED PHASE LISTS (data, do not rewrite):\n"
        + yaml.safe_dump(list(parsed.values()), sort_keys=False, allow_unicode=True)
        + "\nTECHNIQUES (fill traps and refs):\n"
        + yaml.safe_dump([{"code": t["code"], "name": t["name"]} for t in techniques], sort_keys=False)
        + f"\nRefs you may cite (and no others): {', '.join(refs)}."
    )
    return client.Request(
        stage=STAGE,
        system=system_blocks(load_prompt(STAGE), sections),
        user=user,
        schema=ADM_FILL,
        custom_id="adm",
        section_ids=[section.id for section in sections],
    )


def merge_response(
    text: str,
    parsed: dict[str, Any],
    authored_phases: list[dict[str, Any]],
    techniques: list[dict[str, Any]],
    allowed_refs: list[str],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    data = parse_json(text)
    by_code = {phase["code"]: phase for phase in authored_phases}
    fills = {phase["code"]: phase for phase in data["phases"]}
    phases: list[dict[str, Any]] = []
    for code, lists in parsed.items():
        base = dict(by_code.get(code, {"code": code, "name": lists["name"]}))
        base.update(
            {key: lists[key] for key in ("objective", "approach", "inputs", "steps", "outputs", "refs")}
        )
        fill = fills.get(code, {"traps": [], "cross_references": []})
        try:
            for trap in fill["traps"]:
                check_refs(inline_refs(trap), allowed_refs, f"phase {code} trap")
            check_refs(
                fill["cross_references"] or base["refs"], allowed_refs, f"phase {code} cross-references"
            )
            base["traps"] = list(fill["traps"])
            base["refs"] = sorted(set(base["refs"]) | set(fill["cross_references"]), key=str)
            phases.append(AdmPhase.model_validate(base).model_dump())
        except (RefsOutsideInput, ValidationError) as exc:
            logger.warning(f"phase {code} fill rejected, kept parsed lists only: {exc}")
            base["traps"] = []
            phases.append(AdmPhase.model_validate(base).model_dump())
    technique_fills = {item["code"]: item for item in data["techniques"]}
    filled: list[dict[str, Any]] = []
    for technique in techniques:
        base = dict(technique)
        fill = technique_fills.get(technique["code"])
        if fill is not None:
            try:
                check_refs(fill["refs"], allowed_refs, f"technique {technique['code']}")
                base["traps"] = list(fill["traps"])
                base["refs"] = list(fill["refs"])
            except (RefsOutsideInput, ValidationError) as exc:
                logger.warning(f"technique {technique['code']} fill rejected: {exc}")
        filled.append(AdmTechnique.model_validate(base).model_dump())
    return phases, filled


def run(connection: sqlite3.Connection, content_dir: Path, dry_run: bool, limit: int | None) -> list[Path]:
    sections, parsed = adm_sections(connection, content_dir)
    sections = sections[:limit]
    with open(content_dir / "adm" / "phases.yaml", encoding="utf-8") as handle:
        authored_phases = yaml.safe_load(handle) or []
    with open(content_dir / "adm" / "techniques.yaml", encoding="utf-8") as handle:
        techniques = yaml.safe_load(handle) or []
    request = build_request(sections, parsed, techniques)
    if dry_run:
        print(request.describe())
        return []
    phases, filled = merge_response(
        client.complete(request), parsed, authored_phases, techniques, [s.ref for s in sections]
    )
    out = review_dir(content_dir) / "adm"
    comment = f"Generated draft, {now_iso()} (learn_togaf.md §1.5): lists parsed from the ADM, traps and refs filled by the model. Review against adm/*.yaml."
    return [
        write_yaml(out / "phases.generated.yaml", comment, phases),
        write_yaml(out / "techniques.generated.yaml", comment, filled),
    ]
