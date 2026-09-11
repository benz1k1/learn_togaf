"""
CSV for Foundation sets (learn_togaf.md §4.7). Documented header:

    id,exam,unit,objective,stem,option_a,option_b,option_c,option_d,correct,explanation,refs

``refs`` are separated by ``;``. Column names are matched through ``detect.FIELD_ALIASES`` so
``question``/``answer``/``a``..``d`` headers work too; a saved column mapping (per source file)
is applied by the service before parsing.
"""

import csv as stdcsv
import io
from typing import Any

from learn_togaf.importers.detect import canonical_field
from learn_togaf.importers.yaml import ImportParseError

REQUIRED_COLUMNS = ("stem", "option_a", "option_b", "option_c", "option_d", "correct")


def columns(text: str) -> list[str]:
    reader = stdcsv.reader(io.StringIO(text))
    for row in reader:
        return [cell.strip() for cell in row]
    return []


def parse(text: str, file_name: str, column_map: dict[str, str] | None = None) -> list[dict[str, Any]]:
    """Rows keyed by native field. ``column_map`` is native key → source column name."""
    reader = stdcsv.DictReader(io.StringIO(text))
    if not reader.fieldnames:
        raise ImportParseError("the CSV has no header row")
    mapping = {source.strip(): canonical_field(source) for source in reader.fieldnames}
    for native, source in (column_map or {}).items():
        if source in mapping:
            mapping[source] = native
    missing = [column for column in REQUIRED_COLUMNS if column not in mapping.values()]
    if missing:
        raise ImportParseError(
            f"CSV is missing column(s) {', '.join(missing)}; the header is "
            "id,exam,unit,objective,stem,option_a,option_b,option_c,option_d,correct,explanation,refs"
        )
    rows: list[dict[str, Any]] = []
    for raw in reader:
        if not any((value or "").strip() for value in raw.values() if isinstance(value, str)):
            continue
        row = {
            mapping[source.strip()]: (value or "").strip()
            for source, value in raw.items()
            if source is not None
        }
        rows.append(row)
    return rows
