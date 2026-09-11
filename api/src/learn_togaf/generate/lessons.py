"""``generate lessons <unit>`` (learn_togaf.md §1.5): one lesson per objective of the unit,
from the sections mapped to it, written as a draft into ``content/review/<unit>/``."""

import sqlite3
from pathlib import Path

from loguru import logger
from pydantic import ValidationError

from learn_togaf import config
from learn_togaf.content.loader import load_blueprint
from learn_togaf.content.models import LessonFrontMatter
from learn_togaf.generate import (
    Grounding,
    RefsOutsideInput,
    check_refs,
    client,
    grounding_for_unit,
    inline_refs,
    load_prompt,
    now_iso,
    parse_json,
    review_dir,
    slugify,
    system_blocks,
    write_markdown,
)
from learn_togaf.generate.schemas import LESSON

STAGE = "lessons"


def build_requests(groundings: list[Grounding]) -> list[tuple[Grounding, client.Request]]:
    prompt = load_prompt(STAGE)
    requests = []
    for grounding in groundings:
        user = (
            f"Write the lesson for objective {grounding.objective_code} of unit {grounding.unit_code}: "
            f'"{grounding.objective_text}".\n'
            f"Refs you may cite (and no others): {', '.join(grounding.refs)}."
        )
        requests.append(
            (
                grounding,
                client.Request(
                    stage=STAGE,
                    system=system_blocks(prompt, grounding.sections),
                    user=user,
                    schema=LESSON,
                    custom_id=f"lesson-{grounding.objective_code}",
                    section_ids=grounding.section_ids,
                ),
            )
        )
    return requests


def lesson_from_response(text: str, grounding: Grounding, ordinal: int, content_dir: Path) -> Path:
    """Validate the model's lesson against its input and the loader's front-matter model,
    then write the draft. Raises RefsOutsideInput / ValidationError rather than writing."""
    data = parse_json(text)
    body = str(data["body_md"]).strip()
    what = f"lesson {grounding.objective_code}"
    if not inline_refs(body):
        raise RefsOutsideInput(f"{what}: no paragraph ends with a [ref]")
    checks = data.get("check_yourself") or []
    cited = [*data["refs"], *inline_refs(body), *(check["ref"] for check in checks)]
    refs = check_refs(cited, grounding.refs, what)
    refs = sorted(set(refs), key=refs.index)
    if checks:
        body += "\n\n## Check yourself\n" + "\n".join(
            f"{index}. {check['question']}\n   - {check['answer']} [{check['ref']}]"
            for index, check in enumerate(checks, start=1)
        )
    front = LessonFrontMatter(
        title=str(data["title"]).strip(),
        unit=grounding.unit_code,
        objectives=[grounding.objective_code],
        refs=refs,
        reading_minutes=int(data["reading_minutes"]),
        source="generated",
        status="draft",
        model=config.ANTHROPIC_MODEL,
        generated_at=now_iso(),
    )
    slug = slugify(str(data.get("slug") or front.title))
    path = review_dir(content_dir) / grounding.unit_code / f"{ordinal:02d}_{slug}.md"
    return write_markdown(path, front.model_dump(exclude_none=True), body)


def run(
    connection: sqlite3.Connection, content_dir: Path, unit_code: str, dry_run: bool, limit: int | None
) -> list[Path]:
    blueprint = load_blueprint(content_dir)
    groundings = grounding_for_unit(connection, blueprint, unit_code)[:limit]
    requests = build_requests(groundings)
    if dry_run:
        for _, request in requests:
            print(request.describe())
        return []
    written: list[Path] = []
    for ordinal, (grounding, request) in enumerate(requests, start=1):
        text = client.complete(request)
        try:
            written.append(lesson_from_response(text, grounding, ordinal, content_dir))
        except (RefsOutsideInput, ValidationError, KeyError, ValueError) as exc:
            logger.warning(f"lesson {grounding.objective_code} rejected: {exc}")
    return written
