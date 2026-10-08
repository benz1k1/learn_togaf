"""``generate figure-questions`` (learn_togaf.md §1.4, §1.5): for every stored figure that
sits in a mapped section (the important ones first), the image goes to the model with its
caption and section; identify / missing-element / which-part questions come back as a
Foundation-shaped set with ``figure`` set, into ``content/review/questions/figures/``."""

import sqlite3
from pathlib import Path
from typing import Any

from loguru import logger

from learn_togaf.content.loader import load_blueprint, parse_question_set
from learn_togaf.content.models import Blueprint
from learn_togaf.generate import (
    FigureInput,
    Grounding,
    client,
    image_block,
    load_prompt,
    review_dir,
    sections_by_ids,
    system_blocks,
    today,
    write_yaml,
)
from learn_togaf.generate.questions import questions_from_response
from learn_togaf.generate.schemas import FOUNDATION_QUESTIONS

STAGE = "figure_questions"


def figure_groundings(
    connection: sqlite3.Connection, blueprint: Blueprint
) -> list[tuple[FigureInput, Grounding]]:
    """A figure is generated for only when its section is mapped to an objective — the same
    section-id-in-hand rule as every other stage. Important figures come first."""
    rows = connection.execute(
        "SELECT f.id, f.caption, f.file_path, f.section_id, o.objective_code FROM source_figure f"
        " JOIN objective_source o ON o.section_id = f.section_id"
        " ORDER BY f.important DESC, f.id"
    ).fetchall()
    objective_unit = blueprint.objective_unit()
    seen: set[str] = set()
    result: list[tuple[FigureInput, Grounding]] = []
    for row in rows:
        if row["id"] in seen:
            continue
        seen.add(row["id"])
        figure = FigureInput(row["id"], row["caption"], Path(row["file_path"]), row["section_id"])
        if not figure.file_path.is_file():
            logger.warning(f"figure {figure.id}: {figure.file_path} is not in the store; skipped")
            continue
        sections = sections_by_ids(connection, [row["section_id"]])
        if not sections:
            continue
        objective_code = row["objective_code"]
        text = next(o.text for u in blueprint.units for o in u.objectives if o.code == objective_code)
        result.append((figure, Grounding(objective_code, text, objective_unit[objective_code], sections)))
    unmapped = connection.execute(
        "SELECT COUNT(*) FROM source_figure f WHERE f.section_id IS NULL OR f.section_id NOT IN (SELECT section_id FROM objective_source)"
    ).fetchone()[0]
    if unmapped:
        logger.info(
            f"{unmapped} stored figure(s) sit in sections no objective maps to; nothing is generated for them"
        )
    return result


def build_requests(
    pairs: list[tuple[FigureInput, Grounding]], per_figure: int
) -> list[tuple[Grounding, client.Request]]:
    prompt = load_prompt(STAGE)
    requests = []
    for figure, grounding in pairs:
        user: list[dict[str, Any]] = [
            image_block(figure),
            {
                "type": "text",
                "text": (
                    f'Figure {figure.id}: "{figure.caption}". Write {per_figure} figure questions for objective '
                    f'{grounding.objective_code}: "{grounding.objective_text}". Refs you may cite (and no others): '
                    f"{', '.join(grounding.refs)}."
                ),
            },
        ]
        requests.append(
            (
                grounding,
                client.Request(
                    stage=STAGE,
                    system=system_blocks(prompt, grounding.sections),
                    user=user,
                    schema=FOUNDATION_QUESTIONS,
                    custom_id=f"figure-{figure.id}",
                    section_ids=grounding.section_ids,
                ),
            )
        )
    return requests


def run(
    connection: sqlite3.Connection,
    content_dir: Path,
    dry_run: bool,
    limit: int | None,
    batch: bool,
    per_figure: int = 2,
) -> Path | None:
    blueprint = load_blueprint(content_dir)
    pairs = figure_groundings(connection, blueprint)
    if not pairs:
        raise SystemExit(
            "no stored figure sits in a mapped section: run `python sources.py figures` and map its section in objective_sections.yaml"
        )
    pairs = pairs[:limit]
    requests = build_requests(pairs, per_figure)
    if dry_run:
        for _, request in requests:
            print(request.describe())
        return None
    responses = client.complete_many([request for _, request in requests], batch=batch)
    questions: list[dict[str, Any]] = []
    next_index = 1
    for (figure, grounding), (_, request) in zip(pairs, requests, strict=True):
        if request.custom_id not in responses:
            continue
        accepted, next_index = questions_from_response(
            responses[request.custom_id], "OGEA-101", grounding, next_index
        )
        for question in accepted:
            question["figure"] = figure.id
        questions.extend(accepted)
    if not questions:
        raise SystemExit("no figure question survived validation; nothing written")
    code = f"G_FIG_{today()}"
    data = {
        "code": code,
        "exam": "OGEA-101",
        "name": f"Generated figure questions, {today()}",
        "kind": "FIGURE",
        "source": "generated",
        "questions": questions,
    }
    path = review_dir(content_dir) / "questions" / "figures" / f"{code}.yaml"
    parse_question_set(data, path, blueprint)
    return write_yaml(
        path,
        "Generated figure-question draft (learn_togaf.md §1.5). Verify and review before moving into questions/figures/.",
        data,
    )
