"""
Markdown convention for hand-typed Foundation sets (learn_togaf.md §4.7):

    ## unit F4 objective 4.3
    ### Q1 Which of the following is an output of Phase A?
    - [ ] Architecture Definition Document
    - [x] Approved Statement of Architecture Work
    - [ ] Implementation and Migration Plan
    - [ ] Architecture Contract
    > Phase A ends with the approved Statement of Architecture Work.
    refs: ADM §6.5; ADM §6

A ``##`` heading sets ``unit`` / ``objective`` for the questions after it; a ``### Q<n>`` line
starts a question whose stem is the rest of the line (continued by following plain lines);
``- [ ]`` / ``- [x]`` are the options in order A–D; ``>`` is the explanation; ``refs:`` and
``tags:`` are ``;`` / ``,`` separated; ``id:`` overrides the generated id.
"""

import re
from typing import Any

_UNIT_RE = re.compile(r"^##\s+(?P<body>.+?)\s*$")
_UNIT_FIELD_RE = re.compile(r"\b(unit|objective)\s+([A-Za-z0-9.]+)", re.IGNORECASE)
_QUESTION_RE = re.compile(r"^###\s+Q(?P<number>\d+)\s*(?P<stem>.*)$")
_OPTION_RE = re.compile(r"^-\s+\[(?P<mark>[ xX])\]\s+(?P<text>.+?)\s*$")
_FIELD_RE = re.compile(r"^(?P<name>id|refs|tags|difficulty|figure):\s*(?P<value>.*)$", re.IGNORECASE)
_KEYS = ("A", "B", "C", "D")


def parse(text: str, file_name: str) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    defaults: dict[str, str] = {}
    current: dict[str, Any] | None = None

    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        if not line.strip():
            continue
        heading = _UNIT_RE.match(line)
        if heading:
            defaults = {}
            for name, value in _UNIT_FIELD_RE.findall(heading.group("body")):
                defaults[name.lower()] = value
            continue
        question = _QUESTION_RE.match(line)
        if question:
            current = {
                "number": int(question.group("number")),
                "stem": question.group("stem").strip(),
                "options": [],
                "explanation": "",
                "refs": [],
                "tags": [],
                **defaults,
            }
            rows.append(current)
            continue
        if current is None:
            continue
        option = _OPTION_RE.match(line)
        if option:
            key = _KEYS[len(current["options"])] if len(current["options"]) < 4 else ""
            current["options"].append(
                {"key": key, "text": option.group("text"), "correct": option.group("mark").lower() == "x"}
            )
            continue
        if line.startswith(">"):
            explanation = line[1:].strip()
            current["explanation"] = f"{current['explanation']} {explanation}".strip()
            continue
        field = _FIELD_RE.match(line.strip())
        if field:
            name = field.group("name").lower()
            value = field.group("value").strip()
            if name == "refs":
                current["refs"] = [part.strip() for part in value.split(";") if part.strip()]
            elif name == "tags":
                current["tags"] = [part.strip() for part in value.split(",") if part.strip()]
            else:
                current[name] = value
            continue
        if not current["options"]:
            current["stem"] = f"{current['stem']} {line.strip()}".strip()
    for row in rows:
        row.pop("number", None)
    return rows
