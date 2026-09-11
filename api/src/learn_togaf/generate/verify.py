"""``generate verify`` (learn_togaf.md §1.5): every draft under ``content/review/`` goes back
to the model as an independent judge with only its cited sections — is the correct answer
supported, is each distractor actually wrong — and the verdict is written into the file:
``verify: {passed, reason, at}`` in a lesson's front matter, per question and as a set-level
summary in a set's header. Nothing is moved: a failure stays in ``review/`` for the author, a
pass waits for the human review that sets ``status: reviewed``."""

import sqlite3
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml
from loguru import logger

from learn_togaf.content.loader import split_front_matter
from learn_togaf.generate import (
    SectionInput,
    client,
    load_prompt,
    now_iso,
    parse_json,
    review_dir,
    sections_by_ids,
    system_blocks,
    write_markdown,
    write_yaml,
)
from learn_togaf.generate.schemas import VERIFY
from learn_togaf.sources.index import resolve_ref, section_with_descendants

STAGE = "verify"


@dataclass
class Verdict:
    passed: bool
    reason: str
    at: str = field(default_factory=now_iso)

    def as_dict(self) -> dict[str, Any]:
        return {"passed": self.passed, "reason": self.reason, "at": self.at}


@dataclass
class Item:
    path: Path
    kind: str  # lesson | question
    label: str
    refs: list[str]
    payload: dict[str, Any]


def cited_sections(connection: sqlite3.Connection, refs: list[str]) -> list[SectionInput]:
    """The sections a ref names, each with its descendants (a chapter ref means the chapter)."""
    ids: list[str] = []
    for ref in refs:
        for row in resolve_ref(connection, ref):
            for section in section_with_descendants(connection, row["id"]):
                if section["id"] not in ids:
                    ids.append(section["id"])
    return sections_by_ids(connection, ids)


def find_items(content_dir: Path) -> list[Item]:
    items: list[Item] = []
    root = review_dir(content_dir)
    for path in sorted(root.rglob("*.md")):
        front, body = split_front_matter(path.read_text(encoding="utf-8"), path)
        if front.get("source") != "generated":
            continue
        items.append(
            Item(
                path,
                "lesson",
                str(path.relative_to(root)),
                list(front.get("refs") or []),
                {"front": front, "body": body},
            )
        )
    for path in sorted((root / "questions").rglob("*.yaml")) if (root / "questions").is_dir() else []:
        with open(path, encoding="utf-8") as handle:
            data = yaml.safe_load(handle) or {}
        for question in data.get("questions") or []:
            items.append(
                Item(
                    path,
                    "question",
                    f"{path.relative_to(root)}#{question['id']}",
                    list(question.get("refs") or []),
                    question,
                )
            )
    return items


def build_request(item: Item, sections: list[SectionInput]) -> client.Request:
    if item.kind == "lesson":
        subject = f"LESSON (front matter then body):\n{yaml.safe_dump(item.payload['front'], sort_keys=False)}\n{item.payload['body']}"
    else:
        subject = "QUESTION:\n" + yaml.safe_dump(item.payload, sort_keys=False, allow_unicode=True)
    return client.Request(
        stage=STAGE,
        system=system_blocks(load_prompt(STAGE), sections),
        user=f"{subject}\n\nJudge this item against the SOURCE SECTIONS only.",
        schema=VERIFY,
        custom_id=f"verify-{item.label}",
        section_ids=[section.id for section in sections],
    )


def verdict_from_response(text: str) -> Verdict:
    data = parse_json(text)
    return Verdict(passed=bool(data["passed"]), reason=str(data["reason"]))


def write_verdicts(root: Path, items: list[Item], verdicts: dict[str, Verdict]) -> None:
    """Write each verdict into its file. Set files are rewritten once with every question's
    verdict and a header summary; lesson files get a front-matter block."""
    by_path: dict[Path, list[Item]] = {}
    for item in items:
        by_path.setdefault(item.path, []).append(item)
    for path, path_items in by_path.items():
        if path_items[0].kind == "lesson":
            item = path_items[0]
            front = dict(item.payload["front"])
            front["verify"] = verdicts[item.label].as_dict()
            write_markdown(path, front, item.payload["body"])
            continue
        with open(path, encoding="utf-8") as handle:
            data = yaml.safe_load(handle) or {}
        labelled = {item.label: item for item in path_items}
        all_passed = True
        for question in data.get("questions") or []:
            label = f"{path.relative_to(root)}#{question['id']}"
            verdict = verdicts.get(label)
            if verdict is None or label not in labelled:
                continue
            question["verify"] = verdict.as_dict()
            all_passed = all_passed and verdict.passed
        data["verify"] = Verdict(
            all_passed,
            "every question passed"
            if all_passed
            else "one or more questions failed; see each question's verify block",
        ).as_dict()
        write_yaml(
            path,
            "Generated draft set; verified by `generate.py verify` (learn_togaf.md §1.5). Failures stay here until fixed.",
            data,
        )


def run(
    connection: sqlite3.Connection, content_dir: Path, dry_run: bool, limit: int | None, batch: bool
) -> dict[str, int]:
    items = find_items(content_dir)[:limit]
    if not items:
        raise SystemExit(f"nothing to verify under {review_dir(content_dir)}")
    requests: list[tuple[Item, client.Request]] = []
    for item in items:
        sections = cited_sections(connection, item.refs)
        if not sections:
            logger.warning(
                f"{item.label}: none of its refs {item.refs} resolves to an indexed section; it fails verification"
            )
            continue
        requests.append((item, build_request(item, sections)))
    if dry_run:
        for _, request in requests:
            print(request.describe())
        return {"items": len(items), "requests": len(requests)}
    responses = client.complete_many([request for _, request in requests], batch=batch)
    verdicts: dict[str, Verdict] = {
        item.label: Verdict(False, f"no indexed section for refs {item.refs}") for item in items
    }
    for item, request in requests:
        if request.custom_id in responses:
            verdicts[item.label] = verdict_from_response(responses[request.custom_id])
    write_verdicts(review_dir(content_dir), items, verdicts)
    passed = sum(1 for verdict in verdicts.values() if verdict.passed)
    logger.info(
        f"verify: {passed} passed, {len(verdicts) - passed} failed, all left in {review_dir(content_dir)}"
    )
    return {"items": len(items), "passed": passed, "failed": len(verdicts) - passed}
