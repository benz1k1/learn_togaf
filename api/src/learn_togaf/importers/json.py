"""JSON: an array of questions in either §2 shape, or a set object with a ``questions`` array."""

from typing import Any

import orjson

from learn_togaf.importers.yaml import ImportParseError, split_document


def load_document(text: str) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    try:
        data = orjson.loads(text)
    except orjson.JSONDecodeError as exc:
        raise ImportParseError(f"invalid JSON: {exc}") from exc
    return split_document(data)


def parse(text: str, file_name: str) -> list[dict[str, Any]]:
    return load_document(text)[1]
