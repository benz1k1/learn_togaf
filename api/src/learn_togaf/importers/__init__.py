"""
Importers (learn_togaf.md §4.7): one module per format, each exposing
``parse(text, file_name) -> list[dict]`` in the §2 file shape. ``parse_file`` detects the
format, parses, and returns the set header the file carried (native YAML / JSON only) beside
the rows; ``detect.normalise`` then makes every row the same shape before validation.
"""

from dataclasses import dataclass, field
from typing import Any

from learn_togaf.importers import csv as csv_format
from learn_togaf.importers import json as json_format
from learn_togaf.importers import markdown as markdown_format
from learn_togaf.importers import yaml as yaml_format
from learn_togaf.importers.detect import Format, detect_format, normalise
from learn_togaf.importers.yaml import ImportParseError

__all__ = ["ImportParseError", "Parsed", "detect_format", "normalise", "parse_file"]


@dataclass
class Parsed:
    format: Format
    header: dict[str, Any] = field(default_factory=dict)
    rows: list[dict[str, Any]] = field(default_factory=list)
    columns: list[str] = field(default_factory=list)


def parse_file(text: str, file_name: str, column_map: dict[str, str] | None = None) -> Parsed:
    fmt = detect_format(text, file_name)
    if fmt == "yaml":
        header, rows = yaml_format.load_document(text)
        return Parsed(fmt, header, rows)
    if fmt == "json":
        header, rows = json_format.load_document(text)
        return Parsed(fmt, header, rows)
    if fmt == "csv":
        return Parsed(fmt, {}, csv_format.parse(text, file_name, column_map), csv_format.columns(text))
    return Parsed(fmt, {}, markdown_format.parse(text, file_name))
