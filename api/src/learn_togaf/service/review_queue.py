"""
The review queue (learn_togaf.md §1.5, §5.1): generated drafts waiting under ``content/review/``.

A draft is either a question set in the native YAML shape or a lesson ``.md`` with front
matter; either may carry a ``verify:`` block ``{passed: bool, reason: str}`` written by the
verifier (set-level, per item, or in the lesson front matter). ``accept`` validates the draft
with the loader's models, writes it to its destination with ``status: reviewed`` and
``reviewed_at`` on every item, removes the draft and reloads the content cache; ``reject``
moves it to ``content/review/rejected/``. The cache is reloaded only after the files are in
place, and a reload failure puts the files back, so a bad accept never leaves the loader
broken.
"""

import re
import shutil
import sqlite3
from dataclasses import dataclass, field
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import yaml
from loguru import logger
from pydantic import ValidationError

from learn_togaf.content.loader import (
    ContentError,
    load_all,
    load_blueprint,
    parse_question_set,
    split_front_matter,
)
from learn_togaf.content.models import LessonFrontMatter

REJECTED_DIR = "rejected"
_LESSON_NAME_RE = re.compile(r"^(?:(?P<unit>[A-Z][A-Z0-9_]*)__)?(?P<nn>\d{2})_(?P<slug>[a-z0-9_\-]+)\.md$")
_DRAFT_ID_RE = re.compile(r"^[A-Za-z0-9_\-./]+$")


@dataclass
class Verify:
    passed: bool | None
    reason: str


@dataclass
class DraftItem:
    id: str
    title: str
    verify: Verify | None = None


@dataclass
class Draft:
    id: str
    kind: str  # questions | lesson
    path: Path
    title: str
    exam: str = ""
    unit: str = ""
    set_code: str = ""
    model: str = ""
    generated_at: str = ""
    modified_at: str = ""
    verify: Verify | None = None
    items: list[DraftItem] = field(default_factory=list)
    error: str = ""
    body_preview: str = ""

    @property
    def failed(self) -> bool:
        if self.verify is not None and self.verify.passed is False:
            return True
        return any(item.verify is not None and item.verify.passed is False for item in self.items)


def review_dir(content_dir: Path) -> Path:
    return content_dir / "review"


def _verify(raw: Any) -> Verify | None:
    if not isinstance(raw, dict):
        return None
    passed = raw.get("passed")
    return Verify(passed if isinstance(passed, bool) else None, str(raw.get("reason", "")).strip())


def _draft_path(content_dir: Path, draft_id: str) -> Path:
    if not _DRAFT_ID_RE.match(draft_id) or ".." in draft_id.split("/"):
        raise ContentError(f"invalid draft id {draft_id!r}")
    path = (review_dir(content_dir) / draft_id).resolve()
    if review_dir(content_dir).resolve() not in path.parents:
        raise ContentError(f"invalid draft id {draft_id!r}")
    if not path.is_file():
        raise FileNotFoundError(f"draft {draft_id} is not in {review_dir(content_dir)}")
    return path


def _modified(path: Path) -> str:
    return datetime.fromtimestamp(path.stat().st_mtime, tz=UTC).isoformat(timespec="seconds")


def _read_question_draft(path: Path, draft_id: str) -> Draft:
    draft = Draft(id=draft_id, kind="questions", path=path, title=path.name, modified_at=_modified(path))
    try:
        with open(path, encoding="utf-8") as handle:
            data = yaml.safe_load(handle)
    except yaml.YAMLError as exc:
        draft.error = f"invalid YAML: {exc}"
        return draft
    if not isinstance(data, dict):
        draft.error = "a question draft is a set mapping with code/exam/name and a questions list"
        return draft
    draft.title = str(data.get("name") or path.stem)
    draft.exam = str(data.get("exam", "")).upper()
    draft.set_code = str(data.get("code", ""))
    draft.model = str(data.get("model", "") or "")
    draft.generated_at = str(data.get("generated_at", "") or "")
    draft.verify = _verify(data.get("verify"))
    for question in data.get("questions") or []:
        if not isinstance(question, dict):
            continue
        title = str(question.get("stem") or question.get("question") or "")[:160]
        draft.items.append(DraftItem(str(question.get("id", "?")), title, _verify(question.get("verify"))))
        if not draft.unit:
            draft.unit = str(question.get("unit", ""))
    return draft


def _read_lesson_draft(path: Path, draft_id: str) -> Draft:
    draft = Draft(id=draft_id, kind="lesson", path=path, title=path.name, modified_at=_modified(path))
    try:
        front, body = split_front_matter(path.read_text(encoding="utf-8"), path)
    except ContentError as exc:
        draft.error = str(exc)
        return draft
    draft.title = str(front.get("title") or path.stem)
    draft.unit = str(front.get("unit", ""))
    draft.model = str(front.get("model", "") or "")
    draft.generated_at = str(front.get("generated_at", "") or "")
    draft.verify = _verify(front.get("verify"))
    draft.body_preview = body.strip()[:600]
    draft.items = [DraftItem(draft_id, draft.title)]
    return draft


def list_drafts(content_dir: Path) -> list[Draft]:
    root = review_dir(content_dir)
    if not root.is_dir():
        return []
    drafts: list[Draft] = []
    for path in sorted(root.rglob("*")):
        if not path.is_file() or REJECTED_DIR in path.relative_to(root).parts:
            continue
        draft_id = path.relative_to(root).as_posix()
        if path.suffix.lower() in (".yaml", ".yml"):
            drafts.append(_read_question_draft(path, draft_id))
        elif path.suffix.lower() == ".md":
            drafts.append(_read_lesson_draft(path, draft_id))
    return drafts


def get_draft(content_dir: Path, draft_id: str) -> Draft:
    path = _draft_path(content_dir, draft_id)
    if path.suffix.lower() in (".yaml", ".yml"):
        return _read_question_draft(path, draft_id)
    if path.suffix.lower() == ".md":
        return _read_lesson_draft(path, draft_id)
    raise ContentError(f"{draft_id}: not a YAML set or a Markdown lesson")


# ---------------------------------------------------------------- accept / reject
def _now() -> str:
    return datetime.now(UTC).isoformat(timespec="seconds")


def _accept_questions(content_dir: Path, path: Path, reviewed_at: str) -> tuple[Path, str | None]:
    """Returns (destination, previous destination text or None) so a failed reload can revert."""
    blueprint = load_blueprint(content_dir)
    with open(path, encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ContentError(
            f"{path}: a question draft is a set mapping with code/exam/name and a questions list"
        )
    data.pop("verify", None)
    questions = data.get("questions") or []
    for question in questions:
        if isinstance(question, dict):
            question.pop("verify", None)
            question["status"] = "reviewed"
            question["reviewed_at"] = reviewed_at
    exam = str(data.get("exam", "")).upper()
    if exam not in blueprint.exams:
        raise ContentError(f"{path}: exam must be one of {', '.join(blueprint.exams)}, got {exam!r}")
    code = str(data.get("code", "")).strip()
    if not code:
        raise ContentError(f"{path}: the set has no code")
    destination = content_dir / "questions" / exam / f"{code}.yaml"
    previous: str | None = None
    if destination.is_file():
        previous = destination.read_text(encoding="utf-8")
        existing = yaml.safe_load(previous) or {}
        if not isinstance(existing, dict):
            raise ContentError(f"{destination}: existing set file is not a mapping")
        merged = {str(q.get("id")): q for q in existing.get("questions") or [] if isinstance(q, dict)}
        for question in questions:
            if isinstance(question, dict):
                merged[str(question.get("id"))] = question
        existing["questions"] = list(merged.values())
        data = existing
    parse_question_set(data, destination, blueprint)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(
        yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=110), encoding="utf-8"
    )
    return destination, previous


def _accept_lesson(content_dir: Path, path: Path, reviewed_at: str) -> tuple[Path, str | None]:
    front, body = split_front_matter(path.read_text(encoding="utf-8"), path)
    front.pop("verify", None)
    front["status"] = "reviewed"
    front["reviewed_at"] = reviewed_at
    try:
        LessonFrontMatter.model_validate(front)
    except ValidationError as exc:
        raise ContentError(f"{path}: {exc}") from exc
    unit = str(front.get("unit", "")).strip()
    match = _LESSON_NAME_RE.match(path.name)
    if not match:
        raise ContentError(f"{path.name}: a lesson draft is named <nn>_<slug>.md (or <unit>__<nn>_<slug>.md)")
    if not unit:
        unit = match.group("unit") or ""
    if not unit:
        raise ContentError(f"{path}: the front matter has no unit")
    destination = content_dir / "lessons" / unit / f"{match.group('nn')}_{match.group('slug')}.md"
    previous = destination.read_text(encoding="utf-8") if destination.is_file() else None
    destination.parent.mkdir(parents=True, exist_ok=True)
    text = (
        "---\n" + yaml.safe_dump(front, sort_keys=False, allow_unicode=True) + "---\n" + body.strip() + "\n"
    )
    destination.write_text(text, encoding="utf-8")
    return destination, previous


def accept_draft(connection: sqlite3.Connection, content_dir: Path, draft_id: str) -> Path:
    path = _draft_path(content_dir, draft_id)
    reviewed_at = _now()
    if path.suffix.lower() in (".yaml", ".yml"):
        destination, previous = _accept_questions(content_dir, path, reviewed_at)
    elif path.suffix.lower() == ".md":
        destination, previous = _accept_lesson(content_dir, path, reviewed_at)
    else:
        raise ContentError(f"{draft_id}: not a YAML set or a Markdown lesson")
    draft_text = path.read_text(encoding="utf-8")
    path.unlink()
    try:
        load_all(connection, content_dir)
    except ContentError:
        if previous is None:
            destination.unlink(missing_ok=True)
        else:
            destination.write_text(previous, encoding="utf-8")
        path.write_text(draft_text, encoding="utf-8")
        logger.error(f"accepting draft {draft_id} broke the content load; files restored")
        raise
    logger.info(f"draft {draft_id} accepted -> {destination}")
    return destination


def reject_draft(content_dir: Path, draft_id: str) -> Path:
    path = _draft_path(content_dir, draft_id)
    target_dir = review_dir(content_dir) / REJECTED_DIR
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / path.name
    shutil.move(str(path), str(target))
    logger.info(f"draft {draft_id} rejected -> {target}")
    return target
