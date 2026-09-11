"""Native YAML (learn_togaf.md §2): a set file with a header and ``questions``, or a bare list."""

from typing import Any

import yaml as pyyaml

_HEADER_KEYS = ("code", "exam", "name", "kind", "source")


class ImportParseError(ValueError):
    """The uploaded file could not be read in the detected format."""


def load_document(text: str) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    """(set header, question rows). A bare list has an empty header."""
    try:
        data = pyyaml.safe_load(text)
    except pyyaml.YAMLError as exc:
        raise ImportParseError(f"invalid YAML: {exc}") from exc
    return split_document(data)


def split_document(data: Any) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    if data is None:
        return {}, []
    rows: Any
    if isinstance(data, list):
        rows = data
        header: dict[str, Any] = {}
    elif isinstance(data, dict):
        rows = data.get("questions")
        if rows is None:
            rows = data.get("foundation") or data.get("practitioner") or []
        header = {key: data[key] for key in _HEADER_KEYS if key in data}
    else:
        raise ImportParseError("expected a question set mapping or a list of questions")
    if not isinstance(rows, list):
        raise ImportParseError("'questions' must be a list")
    for index, row in enumerate(rows, start=1):
        if not isinstance(row, dict):
            raise ImportParseError(f"row {index} is not a mapping")
    return header, rows


def parse(text: str, file_name: str) -> list[dict[str, Any]]:
    return load_document(text)[1]
