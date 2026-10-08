"""``generate questions <exam code> <unit>`` (learn_togaf.md §1.5): single-answer questions or
gradient scenarios per objective — the exam's ``scoring`` in the blueprint decides which —
structured output, optionally over the Batches API, written as one draft set
``G_<unit>_<date>`` into ``content/review/questions/<exam code>/``."""

import sqlite3
from pathlib import Path
from typing import Any

from loguru import logger
from pydantic import ValidationError

from learn_togaf import config
from learn_togaf.content.loader import load_blueprint, parse_question_set
from learn_togaf.content.models import Blueprint, FoundationQuestion, PractitionerQuestion
from learn_togaf.generate import (
    Grounding,
    RefsOutsideInput,
    check_refs,
    client,
    grounding_for_unit,
    load_prompt,
    now_iso,
    parse_json,
    review_dir,
    set_code,
    system_blocks,
    today,
    write_yaml,
)
from learn_togaf.generate.schemas import FOUNDATION_QUESTIONS, PRACTITIONER_QUESTIONS

DEFAULT_PER_OBJECTIVE = 3
# Scenario briefs rotate per objective so a unit's scenarios differ in setting (§1.5).
SCENARIO_BRIEFS = [
    ("regional water utility", "1,400 staff", "Preliminary Phase complete, first Phase A starting"),
    ("national retail bank", "22,000 staff", "Phase B underway, board impatient for a roadmap"),
    ("public hospital group", "6,000 staff", "Phase E: choosing transition architectures"),
    ("mid-size logistics company", "900 staff", "Phase G: first projects in implementation"),
    ("government agency", "3,500 staff", "Phase H: a regulatory change request has arrived"),
    ("software-as-a-service vendor", "400 staff", "establishing an EA capability from scratch"),
]


def existing_questions(connection: sqlite3.Connection, objective_code: str) -> list[str]:
    rows = connection.execute(
        "SELECT stem_or_scenario FROM question WHERE objective_code = ? ORDER BY id", (objective_code,)
    ).fetchall()
    return [row["stem_or_scenario"][:160] for row in rows]


def build_requests(
    exam: str,
    groundings: list[Grounding],
    blueprint: Blueprint,
    per_objective: int,
    connection: sqlite3.Connection,
) -> list[tuple[Grounding, client.Request]]:
    fmt = blueprint.exam(exam)
    stage = f"questions_{fmt.scoring}"
    prompt = load_prompt(stage)
    requests = []
    for index, grounding in enumerate(groundings):
        unit = next(u for u in blueprint.units if u.code == grounding.unit_code)
        already = existing_questions(connection, grounding.objective_code)
        if fmt.scoring == "single":
            user = (
                f"Write {per_objective} single-answer questions for the {fmt.label} exam, objective {grounding.objective_code} "
                f"(unit {unit.code} {unit.name}, blueprint weight {unit.weight} of {fmt.questions}): "
                f'"{grounding.objective_text}".\n'
                f"Refs you may cite (and no others): {', '.join(grounding.refs)}.\n"
                f"ALREADY IN THE BANK for this objective ({len(already)}):\n"
                + ("\n".join(f"- {stem}" for stem in already) or "- (none)")
            )
            schema = FOUNDATION_QUESTIONS
        else:
            industry, size, stage_text = SCENARIO_BRIEFS[index % len(SCENARIO_BRIEFS)]
            user = (
                f"Write {per_objective} scenario question(s) for the {fmt.label} exam, objective {grounding.objective_code} "
                f'(unit {unit.code} {unit.name}): "{grounding.objective_text}".\n'
                f"Scenario brief: industry={industry}; size={size}; stage={stage_text}; horizon=18 months.\n"
                f"Refs you may cite (and no others): {', '.join(grounding.refs)}.\n"
                f"ALREADY IN THE BANK for this objective ({len(already)}):\n"
                + ("\n".join(f"- {stem}" for stem in already) or "- (none)")
            )
            schema = PRACTITIONER_QUESTIONS
        requests.append(
            (
                grounding,
                client.Request(
                    stage=stage,
                    system=system_blocks(prompt, grounding.sections),
                    user=user,
                    schema=schema,
                    custom_id=f"{exam}-{grounding.objective_code}",
                    section_ids=grounding.section_ids,
                ),
            )
        )
    return requests


def questions_from_response(
    text: str, exam: str, grounding: Grounding, next_index: int
) -> tuple[list[dict[str, Any]], int]:
    """Validate each generated question with the content model and the ref gate; a question
    that fails is logged and dropped, the rest survive. Returns (question dicts, next index)."""
    scoring = load_blueprint(config.CONTENT_DIR).exam(exam).scoring
    data = parse_json(text)
    accepted: list[dict[str, Any]] = []
    stamp = today().replace("-", "")[2:]
    for raw in data["questions"]:
        question_id = f"{grounding.unit_code}-G{stamp}{next_index:02d}"
        item = {
            "id": question_id,
            "unit": grounding.unit_code,
            "objective": grounding.objective_code,
            **raw,
            "source": "generated",
            "status": "draft",
            "model": config.ANTHROPIC_MODEL,
            "generated_at": now_iso(),
        }
        try:
            item["refs"] = check_refs(list(raw.get("refs") or []), grounding.refs, f"question {question_id}")
            model = PractitionerQuestion if scoring == "gradient" else FoundationQuestion
            validated = model.model_validate(item)
        except (RefsOutsideInput, ValidationError) as exc:
            logger.warning(f"question for {grounding.objective_code} rejected: {exc}")
            continue
        accepted.append(validated.model_dump(exclude_none=True))
        next_index += 1
    return accepted, next_index


def write_set(
    content_dir: Path, exam: str, unit_code: str, questions: list[dict[str, Any]], blueprint: Blueprint
) -> Path:
    code = set_code(unit_code)
    data = {
        "code": code,
        "exam": exam,
        "name": f"Generated {exam} set for {unit_code}, {today()}",
        "kind": "DRILL",
        "source": "generated",
        "questions": questions,
    }
    path = review_dir(content_dir) / "questions" / exam / f"{code}.yaml"
    parse_question_set(data, path, blueprint)  # the same validator the loader runs
    return write_yaml(
        path,
        f"Generated draft set (learn_togaf.md §1.5). Run `generate.py verify`, then review before moving into questions/{exam}/.",
        data,
    )


def run(
    connection: sqlite3.Connection,
    content_dir: Path,
    exam: str,
    unit_code: str,
    dry_run: bool,
    limit: int | None,
    batch: bool,
    per_objective: int = DEFAULT_PER_OBJECTIVE,
) -> Path | None:
    blueprint = load_blueprint(content_dir)
    if exam not in blueprint.exams:
        raise SystemExit(f"exam must be one of {', '.join(blueprint.exams)}, not {exam!r}")
    groundings = grounding_for_unit(connection, blueprint, unit_code)[:limit]
    requests = build_requests(exam, groundings, blueprint, per_objective, connection)
    if dry_run:
        for _, request in requests:
            print(request.describe())
        return None
    responses = client.complete_many([request for _, request in requests], batch=batch)
    questions: list[dict[str, Any]] = []
    next_index = 1
    for grounding, request in requests:
        if request.custom_id not in responses:
            logger.warning(f"{request.custom_id}: no response")
            continue
        accepted, next_index = questions_from_response(
            responses[request.custom_id], exam, grounding, next_index
        )
        questions.extend(accepted)
    if not questions:
        raise SystemExit("no question survived validation; nothing written")
    return write_set(content_dir, exam, unit_code, questions, blueprint)
