"""
JSON schemas for the structured-output stages (learn_togaf.md §1.5), matching the file shapes
in ``content/models.py``. The model returns only what it authors; the pipeline adds ``id``,
``unit``, ``objective``, ``source``, ``status``, ``model`` and ``generated_at`` before the
Pydantic models validate the result. Every object is closed (``additionalProperties: false``)
with every property required, the shape the API's ``output_config.format`` expects.
"""

from typing import Any


def _object(properties: dict[str, Any]) -> dict[str, Any]:
    return {
        "type": "object",
        "properties": properties,
        "required": list(properties),
        "additionalProperties": False,
    }


def _array(items: dict[str, Any]) -> dict[str, Any]:
    return {"type": "array", "items": items}


_STRING = {"type": "string"}
_STRINGS = _array(_STRING)
_KEY = {"type": "string", "enum": ["A", "B", "C", "D"]}
_DIFFICULTY = {"type": "integer", "minimum": 1, "maximum": 3}

FOUNDATION_OPTION = _object({"key": _KEY, "text": _STRING, "correct": {"type": "boolean"}, "why": _STRING})

FOUNDATION_QUESTION = _object(
    {
        "stem": _STRING,
        "options": _array(FOUNDATION_OPTION),
        "explanation": _STRING,
        "refs": _STRINGS,
        "difficulty": _DIFFICULTY,
        "tags": _STRINGS,
    }
)
FOUNDATION_QUESTIONS = _object({"questions": _array(FOUNDATION_QUESTION)})

PRACTITIONER_ANSWER = _object(
    {"key": _KEY, "points": {"type": "integer", "enum": [5, 3, 1, 0]}, "text": _STRING, "why": _STRING}
)
PRACTITIONER_QUESTION = _object(
    {
        "scenario": _STRING,
        "question": _STRING,
        "answers": _array(PRACTITIONER_ANSWER),
        "refs": _STRINGS,
        "open_book_hint": _STRING,
        "difficulty": _DIFFICULTY,
        "tags": _STRINGS,
    }
)
PRACTITIONER_QUESTIONS = _object({"questions": _array(PRACTITIONER_QUESTION)})

LESSON = _object(
    {
        "title": _STRING,
        "slug": _STRING,
        "reading_minutes": {"type": "integer", "minimum": 1, "maximum": 60},
        "body_md": _STRING,
        "refs": _STRINGS,
        "check_yourself": _array(_object({"question": _STRING, "answer": _STRING, "ref": _STRING})),
    }
)

GLOSSARY_TERM = _object(
    {
        "id": _STRING,
        "term": _STRING,
        "definition": _STRING,
        "document": _STRING,
        "section": _STRING,
        "confusable_with": _STRINGS,
        "source_sentence": _STRING,
    }
)
GLOSSARY = _object({"terms": _array(GLOSSARY_TERM)})

ADM_FILL = _object(
    {
        "phases": _array(_object({"code": _STRING, "traps": _STRINGS, "cross_references": _STRINGS})),
        "techniques": _array(_object({"code": _STRING, "traps": _STRINGS, "refs": _STRINGS})),
    }
)

VERIFY = _object({"passed": {"type": "boolean"}, "reason": _STRING})
