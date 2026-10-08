"""
Format detection and the shared normalise step for imported question files (learn_togaf.md §4.7).

``detect_format`` sniffs the extension first and the content second. ``normalise`` turns
whatever a format module produced into the §2 file shape: option lists with ``key``/``text``/
``correct``, list-valued ``refs`` and ``tags``, integer ``difficulty``, generated ids where the
file had none. It does not validate — that is ``content.models``, applied once, by the service.
"""

import re
from pathlib import PurePath
from typing import Any, Literal

Format = Literal["yaml", "csv", "json", "markdown"]

_EXTENSIONS: dict[str, Format] = {
    ".yaml": "yaml",
    ".yml": "yaml",
    ".csv": "csv",
    ".json": "json",
    ".md": "markdown",
    ".markdown": "markdown",
}
_CSV_HEADER_RE = re.compile(r"^[\w ]+(,[\w ]+){3,}\s*$")
_MARKDOWN_QUESTION_RE = re.compile(r"^###\s+Q\d+", re.MULTILINE)
_OPTION_KEYS = ("A", "B", "C", "D")

# Alternative column/field names other sets commonly use, mapped onto the native keys.
FIELD_ALIASES: dict[str, tuple[str, ...]] = {
    "id": ("id", "question_id", "qid", "number", "no"),
    "unit": ("unit", "unit_code", "learning_unit"),
    "objective": ("objective", "objective_code", "lo"),
    "stem": ("stem", "question", "question_text", "prompt", "text"),
    "explanation": ("explanation", "rationale", "feedback", "why"),
    "refs": ("refs", "ref", "reference", "references", "source_ref"),
    "correct": ("correct", "answer", "correct_option", "correct_answer", "key"),
    "difficulty": ("difficulty", "level"),
    "tags": ("tags", "tag", "topics"),
    "option_a": ("option_a", "a", "optiona", "choice_a", "answer_a"),
    "option_b": ("option_b", "b", "optionb", "choice_b", "answer_b"),
    "option_c": ("option_c", "c", "optionc", "choice_c", "answer_c"),
    "option_d": ("option_d", "d", "optiond", "choice_d", "answer_d"),
}


def detect_format(text: str, file_name: str) -> Format:
    suffix = PurePath(file_name).suffix.lower()
    if suffix in _EXTENSIONS:
        return _EXTENSIONS[suffix]
    stripped = text.lstrip()
    if stripped.startswith(("[", "{")):
        return "json"
    if _MARKDOWN_QUESTION_RE.search(text):
        return "markdown"
    first_line = stripped.split("\n", 1)[0]
    if _CSV_HEADER_RE.match(first_line) and "," in first_line and ":" not in first_line:
        return "csv"
    return "yaml"


def canonical_field(name: str) -> str:
    """The native key a column or field name stands for, or the name itself (lower-cased)."""
    key = name.strip().lower().replace(" ", "_").replace("-", "_")
    for native, aliases in FIELD_ALIASES.items():
        if key in aliases:
            return native
    return key


def split_list(value: Any, separator: str = ";") -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    text = str(value).strip()
    if not text:
        return []
    return [part.strip() for part in re.split(rf"[{re.escape(separator)}\n]", text) if part.strip()]


def _clean(value: Any) -> Any:
    return value.strip() if isinstance(value, str) else value


def _options_from_row(row: dict[str, Any]) -> list[dict[str, Any]]:
    """Options in the native list shape from any of: the native list; a mapping key → text
    plus ``correct``; flat ``option_a``..``option_d`` columns plus ``correct``."""
    raw = row.get("options")
    correct = str(row.get("correct", "") or "").strip().upper()
    if isinstance(raw, list):
        options = []
        for index, item in enumerate(raw):
            if isinstance(item, dict):
                option = {
                    "key": str(item.get("key", _OPTION_KEYS[index] if index < 4 else "")).strip().upper(),
                    "text": _clean(item.get("text", "")),
                    "correct": bool(item.get("correct", False)),
                }
                if "why" in item:
                    option["why"] = _clean(item["why"])
            else:
                key = _OPTION_KEYS[index] if index < 4 else ""
                option = {"key": key, "text": _clean(item), "correct": key == correct}
            options.append(option)
        if correct and not any(option["correct"] for option in options):
            for option in options:
                option["correct"] = option["key"] == correct
        return options
    if isinstance(raw, dict):
        return [
            {
                "key": str(key).strip().upper(),
                "text": _clean(text),
                "correct": str(key).strip().upper() == correct,
            }
            for key, text in raw.items()
        ]
    options = []
    for key in _OPTION_KEYS:
        column = f"option_{key.lower()}"
        if column in row:
            options.append({"key": key, "text": _clean(row[column]), "correct": key == correct})
    return options


def _answers_from_row(row: dict[str, Any]) -> list[dict[str, Any]]:
    raw = row.get("answers")
    if not isinstance(raw, list):
        return []
    answers = []
    for index, item in enumerate(raw):
        if not isinstance(item, dict):
            continue
        answers.append(
            {
                "key": str(item.get("key", _OPTION_KEYS[index] if index < 4 else "")).strip().upper(),
                "points": item.get("points"),
                "text": _clean(item.get("text", "")),
                "why": _clean(item.get("why", "")),
            }
        )
    return answers


def normalise(rows: list[dict[str, Any]], scoring: str, set_code: str) -> list[dict[str, Any]]:
    """The §2 shape for every row. Keys the models do not know are dropped; nothing is validated."""
    normalised: list[dict[str, Any]] = []
    for index, raw in enumerate(rows, start=1):
        row = {canonical_field(str(key)): value for key, value in raw.items()}
        question: dict[str, Any] = {
            "id": str(row.get("id") or "").strip() or f"{set_code}-{index:03d}",
            "unit": str(row.get("unit") or "").strip().upper(),
            "objective": str(row.get("objective") or "").strip(),
            "refs": split_list(row.get("refs")),
            "tags": split_list(row.get("tags"), separator=","),
            "difficulty": row.get("difficulty") if row.get("difficulty") not in (None, "") else 2,
            "source": "imported",
            "status": str(row.get("status") or "reviewed").strip(),
        }
        if row.get("figure"):
            question["figure"] = str(row["figure"]).strip()
        if scoring == "gradient":
            question["scenario"] = _clean(row.get("scenario", "")) or ""
            question["question"] = _clean(row.get("question", row.get("stem", ""))) or ""
            question["answers"] = _answers_from_row(row)
            question["open_book_hint"] = _clean(row.get("open_book_hint", "")) or ""
        else:
            question["stem"] = _clean(row.get("stem", "")) or ""
            question["options"] = _options_from_row(row)
            question["explanation"] = _clean(row.get("explanation", "")) or ""
        normalised.append(question)
    return normalised
