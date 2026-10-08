#!/usr/bin/env python3
"""
Render ArchiMate views for the worked examples and the artefact catalogue (learn_sabsa_archimate.md
§4.3, §4.5): ``content/archimate/<id>.yaml`` → ``api/src/learn_togaf/pages/static/archimate/<id>.svg``.

    python draw_archimate.py            # render every model whose SVG is missing or stale
    python draw_archimate.py --check    # exit 1 if any SVG is missing or stale (tests call this)
    python draw_archimate.py --force    # re-render everything

An authoring-time tool, like add_figures.py: the app serves the SVGs as static files and never
parses or renders ArchiMate itself (plan §4.9). The notation follows the ArchiMate 3.2
Specification's summary of language notation — element shapes by aspect, the standard layer
colours, the eleven relationship line-and-arrowhead styles — so the learner sees on the page
what the Part 1 exam shows them. Layout is a grid the author chooses; nothing is auto-placed.

Model file shape::

    id: northgate_motivation
    title: "Northgate Bank — Motivation view"
    viewpoint: Motivation
    elements:
      - {id: cio, type: stakeholder, name: "CIO", col: 0, row: 0}
      - {id: g1, type: goal, name: "Mobile payments live before Q3 2027", col: 1, row: 0, w: 2}
    groups:                       # optional; a dashed Grouping (or Location) drawn behind its cells
      - {id: prog, type: grouping, name: "Digital Channels", from: [0, 0], to: [2, 1]}
    relations:
      - {from: cio, to: g1, type: association}
      - {from: r1, to: g1, type: realization}
      - {from: a1, to: g1, type: influence, label: "+"}
      - {from: f1, to: d1, type: access, access: write}     # read | write | readwrite | none
      - {from: a, to: b, type: serving, via: [[2, 1]]}        # optional waypoints in grid cells
    notes:                        # optional callouts
      - {text: "Read top-down: who wants what, and why", col: 0, row: 3, w: 3}
"""

from __future__ import annotations

import argparse
import hashlib
import html
import math
import sys
from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parent
MODELS_DIR = REPO / "content" / "archimate"
OUT_DIR = REPO / "api" / "src" / "learn_togaf" / "pages" / "static" / "archimate"

# ---------------------------------------------------------------- notation tables
# aspect: active (rectangle, icon top right) | behaviour (rounded) | passive (rectangle) |
# motivation (chamfered) | composite | other. Colours are the specification's layer defaults.
COLOURS = {
    "motivation": "#ccccff",
    "strategy": "#f5deaa",
    "business": "#ffffb5",
    "application": "#b5ffff",
    "technology": "#c9e7b7",
    "physical": "#c9e7b7",
    "implementation": "#ffe0e0",
    "plateau": "#e0ffe0",
    "composite": "#ffffff",
    "location": "#fbb",
    "other": "#ffffff",
}
ELEMENTS: dict[str, tuple[str, str]] = {  # type → (layer, aspect)
    # motivation
    "stakeholder": ("motivation", "motivation"),
    "driver": ("motivation", "motivation"),
    "assessment": ("motivation", "motivation"),
    "goal": ("motivation", "motivation"),
    "outcome": ("motivation", "motivation"),
    "principle": ("motivation", "motivation"),
    "requirement": ("motivation", "motivation"),
    "constraint": ("motivation", "motivation"),
    "meaning": ("motivation", "motivation"),
    "value": ("motivation", "motivation"),
    # strategy
    "resource": ("strategy", "passive"),
    "capability": ("strategy", "behaviour"),
    "value_stream": ("strategy", "behaviour"),
    "course_of_action": ("strategy", "behaviour"),
    # business
    "business_actor": ("business", "active"),
    "business_role": ("business", "active"),
    "business_collaboration": ("business", "active"),
    "business_interface": ("business", "active"),
    "business_process": ("business", "behaviour"),
    "business_function": ("business", "behaviour"),
    "business_interaction": ("business", "behaviour"),
    "business_event": ("business", "behaviour"),
    "business_service": ("business", "behaviour"),
    "business_object": ("business", "passive"),
    "contract": ("business", "passive"),
    "representation": ("business", "passive"),
    "product": ("business", "passive"),
    # application
    "application_component": ("application", "active"),
    "application_collaboration": ("application", "active"),
    "application_interface": ("application", "active"),
    "application_function": ("application", "behaviour"),
    "application_interaction": ("application", "behaviour"),
    "application_process": ("application", "behaviour"),
    "application_event": ("application", "behaviour"),
    "application_service": ("application", "behaviour"),
    "data_object": ("application", "passive"),
    # technology
    "node": ("technology", "active"),
    "device": ("technology", "active"),
    "system_software": ("technology", "active"),
    "technology_collaboration": ("technology", "active"),
    "technology_interface": ("technology", "active"),
    "path": ("technology", "active"),
    "communication_network": ("technology", "active"),
    "technology_function": ("technology", "behaviour"),
    "technology_process": ("technology", "behaviour"),
    "technology_interaction": ("technology", "behaviour"),
    "technology_event": ("technology", "behaviour"),
    "technology_service": ("technology", "behaviour"),
    "artifact": ("technology", "passive"),
    # physical
    "equipment": ("physical", "active"),
    "facility": ("physical", "active"),
    "distribution_network": ("physical", "active"),
    "material": ("physical", "passive"),
    # implementation and migration
    "work_package": ("implementation", "behaviour"),
    "deliverable": ("implementation", "passive"),
    "implementation_event": ("implementation", "behaviour"),
    "plateau": ("plateau", "passive"),
    "gap": ("plateau", "passive"),
    # composite
    "grouping": ("composite", "composite"),
    "location": ("location", "composite"),
    "junction": ("other", "other"),
    "or_junction": ("other", "other"),
}
RELATIONS = {
    # type → (dash, start marker, end marker, stroke width)
    "composition": ("", "filled-diamond", "", 1.5),
    "aggregation": ("", "hollow-diamond", "", 1.5),
    "assignment": ("", "dot", "filled-arrow", 1.5),
    "realization": ("6 4", "", "hollow-triangle", 1.5),
    "serving": ("", "", "open-arrow", 1.5),
    "access": ("2 3", "", "small-open-arrow", 1.2),
    "influence": ("6 4", "", "open-arrow", 1.5),
    "association": ("", "", "", 1.5),
    "triggering": ("", "", "filled-arrow", 1.5),
    "flow": ("6 4", "", "filled-arrow", 1.5),
    "specialization": ("", "", "hollow-triangle", 1.5),
}
CELL_W, CELL_H, GAP_X, GAP_Y, MARGIN, TITLE_H = 170, 72, 44, 44, 30, 68  # TITLE_H leaves room for a group tab on row 0
FONT = "font-family='Segoe UI, Helvetica Neue, Arial, sans-serif'"
STROKE = "#333"


def esc(text: str) -> str:
    return html.escape(str(text), quote=True)


# ---------------------------------------------------------------- geometry
class Box:
    def __init__(self, x: float, y: float, w: float, h: float) -> None:
        self.x, self.y, self.w, self.h = x, y, w, h

    @property
    def cx(self) -> float:
        return self.x + self.w / 2

    @property
    def cy(self) -> float:
        return self.y + self.h / 2

    def edge_point(self, towards: tuple[float, float]) -> tuple[float, float]:
        """Where the segment from the centre towards ``towards`` leaves the rectangle (with a
        small margin so arrowheads sit on the border, not inside it)."""
        dx, dy = towards[0] - self.cx, towards[1] - self.cy
        if dx == 0 and dy == 0:
            return self.cx, self.cy
        scale_x = (self.w / 2) / abs(dx) if dx else math.inf
        scale_y = (self.h / 2) / abs(dy) if dy else math.inf
        scale = min(scale_x, scale_y)
        return self.cx + dx * scale, self.cy + dy * scale


def cell_box(col: float, row: float, w: float = 1, h: float = 1, grid: dict[str, float] | None = None) -> Box:
    g = grid or {}
    cw, ch, gx, gy = g.get("cell_w", CELL_W), g.get("cell_h", CELL_H), g.get("gap_x", GAP_X), g.get("gap_y", GAP_Y)
    x = MARGIN + col * (cw + gx)
    y = MARGIN + TITLE_H + row * (ch + gy)
    return Box(x, y, w * cw + (w - 1) * gx, h * ch + (h - 1) * gy)


def wrap(text: str, width_px: float, font_px: float = 12.5) -> list[str]:
    max_chars = max(6, int(width_px / (font_px * 0.55)))
    words, lines, current = text.split(), [], ""
    for word in words:
        candidate = f"{current} {word}".strip()
        if len(candidate) > max_chars and current:
            lines.append(current)
            current = word
        else:
            current = candidate
    if current:
        lines.append(current)
    return lines or [""]


# ---------------------------------------------------------------- icons (top-right glyphs, 16 px)
def icon(kind: str, x: float, y: float) -> str:
    """A 16×16 glyph whose top-left is (x, y); the specification's notation icons, simplified."""
    s = f"stroke='{STROKE}' stroke-width='1.2' fill='none'"
    p = f"stroke='{STROKE}' stroke-width='1.2' fill='#fff'"
    match kind:
        case "business_actor":
            return (f"<g {s}><circle cx='{x+8}' cy='{y+3}' r='2.5'/><line x1='{x+8}' y1='{y+5.5}' x2='{x+8}' y2='{y+11}'/>"
                    f"<line x1='{x+3}' y1='{y+8}' x2='{x+13}' y2='{y+8}'/><line x1='{x+8}' y1='{y+11}' x2='{x+4}' y2='{y+16}'/>"
                    f"<line x1='{x+8}' y1='{y+11}' x2='{x+12}' y2='{y+16}'/></g>")
        case "business_role":
            return (f"<g {p}><rect x='{x+1}' y='{y+4}' width='12' height='8' rx='4'/>"
                    f"<ellipse cx='{x+13}' cy='{y+8}' rx='2.5' ry='4'/></g>")
        case "business_collaboration" | "application_collaboration" | "technology_collaboration":
            return f"<g {s}><circle cx='{x+6}' cy='{y+8}' r='4.5'/><circle cx='{x+11}' cy='{y+8}' r='4.5'/></g>"
        case "business_interface" | "application_interface" | "technology_interface":
            return f"<g {p}><line x1='{x+1}' y1='{y+8}' x2='{x+9}' y2='{y+8}'/><circle cx='{x+12}' cy='{y+8}' r='3.5'/></g>"
        case "business_process" | "application_process" | "technology_process":
            return f"<path d='M{x+1} {y+5} h9 v-3 l5 6 l-5 6 v-3 h-9 z' {p}/>"
        case "business_function" | "application_function" | "technology_function":
            return f"<path d='M{x+2} {y+15} v-8 l6 -6 l6 6 v8 l-6 -6 z' {p}/>"
        case "business_interaction" | "application_interaction" | "technology_interaction":
            return (f"<g {p}><path d='M{x+7} {y+2} a6 6 0 0 0 0 12 z'/>"
                    f"<path d='M{x+9} {y+2} a6 6 0 0 1 0 12 z'/></g>")
        case "business_event" | "application_event" | "technology_event" | "implementation_event":
            return f"<path d='M{x+1} {y+4} h10 l4 4 l-4 4 h-10 l3 -4 z' {p}/>"
        case "business_service" | "application_service" | "technology_service":
            return f"<rect x='{x+1}' y='{y+4}' width='14' height='8' rx='4' {p}/>"
        case "business_object" | "data_object" | "contract":
            return f"<g {p}><rect x='{x+1}' y='{y+2}' width='14' height='12'/><line x1='{x+1}' y1='{y+6}' x2='{x+15}' y2='{y+6}'/></g>"
        case "representation":
            return f"<path d='M{x+1} {y+3} h14 v9 q-3.5 3 -7 0 t-7 0 z' {p}/>"
        case "product":
            return f"<g {p}><rect x='{x+1}' y='{y+2}' width='14' height='12'/><rect x='{x+1}' y='{y+2}' width='7' height='4'/></g>"
        case "application_component":
            return (f"<g {p}><rect x='{x+4}' y='{y+1}' width='11' height='14'/>"
                    f"<rect x='{x+1}' y='{y+4}' width='6' height='3'/><rect x='{x+1}' y='{y+9}' width='6' height='3'/></g>")
        case "node" | "equipment":
            return f"<path d='M{x+1} {y+5} l4 -4 h10 v10 l-4 4 h-10 z M{x+1} {y+5} h10 v10 M{x+11} {y+5} l4 -4' {p}/>"
        case "device":
            return f"<g {p}><rect x='{x+2}' y='{y+2}' width='12' height='8' rx='1'/><path d='M{x+5} {y+10} l-3 4 h12 l-3 -4'/></g>"
        case "system_software":
            return f"<g {p}><circle cx='{x+8}' cy='{y+8}' r='6'/><circle cx='{x+10}' cy='{y+6}' r='4'/></g>"
        case "communication_network" | "distribution_network":
            return f"<g {p}><circle cx='{x+3}' cy='{y+8}' r='2'/><circle cx='{x+13}' cy='{y+8}' r='2'/><line x1='{x+5}' y1='{y+8}' x2='{x+11}' y2='{y+8}'/></g>"
        case "path":
            return f"<g {s}><line x1='{x+1}' y1='{y+8}' x2='{x+15}' y2='{y+8}' stroke-dasharray='3 2'/><path d='M{x+4} {y+5} l-3 3 l3 3 M{x+12} {y+5} l3 3 l-3 3'/></g>"
        case "artifact":
            return f"<path d='M{x+2} {y+1} h8 l4 4 v10 h-12 z M{x+10} {y+1} v4 h4' {p}/>"
        case "facility":
            return f"<path d='M{x+1} {y+15} v-7 l4 3 v-3 l4 3 v-3 l4 3 v-9 h2 v13 z' {p}/>"
        case "material":
            return f"<g {p}><path d='M{x+8} {y+1} l7 4 v6 l-7 4 l-7 -4 v-6 z'/><path d='M{x+8} {y+1} v14 M{x+1} {y+5} l7 4 l7 -4'/></g>"
        case "stakeholder":
            return f"<g {p}><rect x='{x+1}' y='{y+4}' width='12' height='8' rx='4'/><ellipse cx='{x+13}' cy='{y+8}' rx='2.5' ry='4'/></g>"
        case "driver":
            return (f"<g {s}><circle cx='{x+8}' cy='{y+8}' r='6'/><circle cx='{x+8}' cy='{y+8}' r='1.5'/>"
                    f"<line x1='{x+8}' y1='{y+2}' x2='{x+8}' y2='{y+14}'/><line x1='{x+2}' y1='{y+8}' x2='{x+14}' y2='{y+8}'/>"
                    f"<line x1='{x+3.8}' y1='{y+3.8}' x2='{x+12.2}' y2='{y+12.2}'/><line x1='{x+12.2}' y1='{y+3.8}' x2='{x+3.8}' y2='{y+12.2}'/></g>")
        case "assessment":
            return f"<g {s}><circle cx='{x+10}' cy='{y+6}' r='4.5'/><line x1='{x+6.5}' y1='{y+9.5}' x2='{x+1}' y2='{y+15}'/></g>"
        case "goal":
            return f"<g {s}><circle cx='{x+8}' cy='{y+8}' r='6.5'/><circle cx='{x+8}' cy='{y+8}' r='3.8'/><circle cx='{x+8}' cy='{y+8}' r='1.2' fill='{STROKE}'/></g>"
        case "outcome":
            return (f"<g {s}><circle cx='{x+7}' cy='{y+9}' r='6'/><circle cx='{x+7}' cy='{y+9}' r='3'/>"
                    f"<line x1='{x+7}' y1='{y+9}' x2='{x+15}' y2='{y+1}'/><path d='M{x+11} {y+1} h4 v4'/></g>")
        case "principle":
            return f"<g {s}><rect x='{x+2}' y='{y+1}' width='12' height='14' rx='1'/><line x1='{x+8}' y1='{y+4}' x2='{x+8}' y2='{y+10}' stroke-width='2'/><circle cx='{x+8}' cy='{y+12.5}' r='1' fill='{STROKE}'/></g>"
        case "requirement":
            return f"<path d='M{x+5} {y+3} h10 l-4 10 h-10 z' {p}/>"
        case "constraint":
            return f"<g {p}><path d='M{x+5} {y+3} h10 l-4 10 h-10 z'/><line x1='{x+7.5}' y1='{y+3}' x2='{x+3.5}' y2='{y+13}'/></g>"
        case "meaning":
            return f"<path d='M{x+3} {y+6} q0 -4 5 -4 q3 0 4 2 q4 0 3 4 q1 4 -3 4 q-1 2 -4 2 q-4 0 -4 -3 q-3 0 -1 -5 z' {p}/>"
        case "value":
            return f"<ellipse cx='{x+8}' cy='{y+8}' rx='7' ry='4.5' {p}/>"
        case "resource":
            return f"<g {p}><rect x='{x+1}' y='{y+4}' width='12' height='8'/><line x1='{x+4}' y1='{y+6}' x2='{x+4}' y2='{y+10}'/><line x1='{x+7}' y1='{y+6}' x2='{x+7}' y2='{y+10}'/><line x1='{x+10}' y1='{y+6}' x2='{x+10}' y2='{y+10}'/><rect x='{x+13}' y='{y+6}' width='2' height='4'/></g>"
        case "capability":
            return f"<path d='M{x+1} {y+15} v-4 h4 v-4 h4 v-4 h4 v-3 h2 v15 z' {p}/>"
        case "value_stream":
            return f"<path d='M{x+1} {y+4} h9 l4 4 l-4 4 h-9 l3 -4 z' {p}/>"
        case "course_of_action":
            return f"<g {s}><circle cx='{x+10}' cy='{y+10}' r='5'/><circle cx='{x+10}' cy='{y+10}' r='2'/><path d='M{x+1} {y+1} q6 0 6 6'/><path d='M{x+5} {y+5} l2 2 l-3 1'/></g>"
        case "work_package":
            return f"<rect x='{x+1}' y='{y+4}' width='14' height='8' rx='4' {p}/>"
        case "deliverable":
            return f"<path d='M{x+1} {y+3} h14 v9 q-3.5 3 -7 0 t-7 0 z' {p}/>"
        case "plateau":
            return f"<g stroke='{STROKE}' stroke-width='1.6' fill='none'><line x1='{x+2}' y1='{y+5}' x2='{x+14}' y2='{y+5}'/><line x1='{x+3}' y1='{y+8.5}' x2='{x+13}' y2='{y+8.5}'/><line x1='{x+4}' y1='{y+12}' x2='{x+12}' y2='{y+12}'/></g>"
        case "gap":
            return f"<g {s}><circle cx='{x+8}' cy='{y+8}' r='5'/><line x1='{x+1}' y1='{y+6}' x2='{x+15}' y2='{y+6}'/><line x1='{x+1}' y1='{y+10}' x2='{x+15}' y2='{y+10}'/></g>"
        case "location":
            return f"<path d='M{x+8} {y+15} q-6 -7 -6 -10 a6 6 0 0 1 12 0 q0 3 -6 10 z M{x+8} {y+7} m-2 0 a2 2 0 1 0 4 0 a2 2 0 1 0 -4 0' {p}/>"
    return ""


# ---------------------------------------------------------------- element shapes
def element_svg(element: dict[str, Any], box: Box) -> str:
    kind = element["type"]
    if kind not in ELEMENTS:
        raise SystemExit(f"element {element.get('id')}: unknown ArchiMate type {kind!r}")
    layer, aspect = ELEMENTS[kind]
    fill = COLOURS[layer]
    x, y, w, h = box.x, box.y, box.w, box.h
    if kind in ("junction", "or_junction"):
        r = 7
        inner = "fill='#fff'" if kind == "or_junction" else f"fill='{STROKE}'"
        return f"<circle cx='{box.cx}' cy='{box.cy}' r='{r}' stroke='{STROKE}' stroke-width='1.5' {inner}/>"
    shape: str
    if aspect == "motivation":
        c = 10
        shape = (f"<path d='M{x+c} {y} h{w-2*c} l{c} {c} v{h-2*c} l-{c} {c} h-{w-2*c} l-{c} -{c} v-{h-2*c} z'"
                 f" fill='{fill}' stroke='{STROKE}' stroke-width='1.5'/>")
    elif kind.endswith("_service") or kind in ("work_package",):
        shape = f"<rect x='{x}' y='{y}' width='{w}' height='{h}' rx='{min(h/2, 22)}' fill='{fill}' stroke='{STROKE}' stroke-width='1.5'/>"
    elif kind.endswith("_event") or kind == "implementation_event":
        n = 14
        shape = (f"<path d='M{x} {y} h{w-n} l{n} {h/2} l-{n} {h/2} h-{w-n} l{n} -{h/2} z'"
                 f" fill='{fill}' stroke='{STROKE}' stroke-width='1.5'/>")
    elif kind == "value_stream":
        n = 16
        shape = (f"<path d='M{x} {y} h{w-n} l{n} {h/2} l-{n} {h/2} h-{w-n} l{n} -{h/2} z'"
                 f" fill='{fill}' stroke='{STROKE}' stroke-width='1.5'/>")
    elif kind == "deliverable" or kind == "representation":
        shape = (f"<path d='M{x} {y} h{w} v{h-10} q-{w/4} 8 -{w/2} 0 t-{w/2} 0 z'"
                 f" fill='{fill}' stroke='{STROKE}' stroke-width='1.5'/>")
    elif kind == "grouping":
        shape = (f"<path d='M{x} {y+18} v-18 h{min(w/2.5, 120)} v18' fill='{fill}' stroke='{STROKE}' stroke-width='1.2' stroke-dasharray='5 3'/>"
                 f"<rect x='{x}' y='{y+18}' width='{w}' height='{h-18}' fill='{fill}' fill-opacity='0.35' stroke='{STROKE}' stroke-width='1.2' stroke-dasharray='5 3'/>")
    elif aspect == "behaviour":
        shape = f"<rect x='{x}' y='{y}' width='{w}' height='{h}' rx='8' fill='{fill}' stroke='{STROKE}' stroke-width='1.5'/>"
    else:
        shape = f"<rect x='{x}' y='{y}' width='{w}' height='{h}' fill='{fill}' stroke='{STROKE}' stroke-width='1.5'/>"
        if kind in ("business_object", "data_object", "contract", "product", "material"):
            shape += f"<line x1='{x}' y1='{y+14}' x2='{x+w}' y2='{y+14}' stroke='{STROKE}' stroke-width='1.2'/>"
    if kind in ("grouping", "location") and element.get("_group"):
        label = f"<text x='{x+8}' y='{y+13}' font-size='12' font-weight='600' fill='#222' {FONT}>{esc(element['name'])}</text>"
        return shape + label + icon(kind, x + w - 22, y + 20)
    text_width = w - 30
    lines = wrap(element["name"], text_width)
    line_h = 14
    start_y = box.cy - (len(lines) - 1) * line_h / 2 + 4
    text = "".join(
        f"<text x='{box.cx - 8 if aspect != 'motivation' else box.cx}' y='{start_y + index * line_h}' text-anchor='middle'"
        f" font-size='12.5' fill='#222' {FONT}>{esc(line)}</text>"
        for index, line in enumerate(lines)
    )
    return shape + text + icon(kind, x + w - 20, y + 4)


# ---------------------------------------------------------------- relations
def marker_defs() -> str:
    m = f"stroke='{STROKE}' stroke-width='1'"
    return f"""<defs>
<marker id='filled-arrow' viewBox='0 0 10 10' refX='9' refY='5' markerWidth='9' markerHeight='9' orient='auto-start-reverse'><path d='M0 0 L10 5 L0 10 z' fill='{STROKE}'/></marker>
<marker id='open-arrow' viewBox='0 0 10 10' refX='9' refY='5' markerWidth='9' markerHeight='9' orient='auto-start-reverse'><path d='M0 0 L10 5 L0 10' fill='none' {m}/></marker>
<marker id='small-open-arrow' viewBox='0 0 10 10' refX='9' refY='5' markerWidth='7' markerHeight='7' orient='auto-start-reverse'><path d='M1 1 L9 5 L1 9' fill='none' {m}/></marker>
<marker id='hollow-triangle' viewBox='0 0 12 12' refX='11' refY='6' markerWidth='11' markerHeight='11' orient='auto-start-reverse'><path d='M0 0 L12 6 L0 12 z' fill='#fff' {m}/></marker>
<marker id='filled-diamond' viewBox='0 0 14 10' refX='1' refY='5' markerWidth='12' markerHeight='9' orient='auto'><path d='M0 5 L7 0 L14 5 L7 10 z' fill='{STROKE}'/></marker>
<marker id='hollow-diamond' viewBox='0 0 14 10' refX='1' refY='5' markerWidth='12' markerHeight='9' orient='auto'><path d='M0 5 L7 0 L14 5 L7 10 z' fill='#fff' {m}/></marker>
<marker id='dot' viewBox='0 0 8 8' refX='2' refY='4' markerWidth='7' markerHeight='7' orient='auto'><circle cx='4' cy='4' r='3' fill='{STROKE}'/></marker>
</defs>"""


def relation_svg(relation: dict[str, Any], boxes: dict[str, Box], grid: dict[str, float]) -> str:
    kind = relation["type"]
    if kind not in RELATIONS:
        raise SystemExit(f"relation {relation.get('from')}→{relation.get('to')}: unknown type {kind!r}")
    dash, start_marker, end_marker, width = RELATIONS[kind]
    source, target = boxes[relation["from"]], boxes[relation["to"]]
    waypoints = [cell_box(c, r, grid=grid) for c, r in relation.get("via", [])]
    waypoints = [(b.cx, b.cy) for b in waypoints]
    first_towards = waypoints[0] if waypoints else (target.cx, target.cy)
    last_from = waypoints[-1] if waypoints else (source.cx, source.cy)
    start = source.edge_point(first_towards)
    end = target.edge_point(last_from)
    if kind == "access":
        mode = relation.get("access", "write")
        if mode == "read":
            start_marker, end_marker = "small-open-arrow", ""
        elif mode == "readwrite":
            start_marker = end_marker = "small-open-arrow"
        elif mode == "none":
            start_marker = end_marker = ""
    if kind == "association" and relation.get("directed"):
        end_marker = "small-open-arrow"
    points = " ".join(f"{px:.1f},{py:.1f}" for px, py in [start, *waypoints, end])
    attrs = f"fill='none' stroke='{STROKE}' stroke-width='{width}'"
    if dash:
        attrs += f" stroke-dasharray='{dash}'"
    if start_marker:
        attrs += f" marker-start='url(#{start_marker})'"
    if end_marker:
        attrs += f" marker-end='url(#{end_marker})'"
    svg = f"<polyline points='{points}' {attrs}/>"
    label = relation.get("label")
    if label:
        mid_x = (start[0] + end[0]) / 2 if not waypoints else waypoints[len(waypoints) // 2][0]
        mid_y = (start[1] + end[1]) / 2 if not waypoints else waypoints[len(waypoints) // 2][1]
        svg += (f"<rect x='{mid_x-len(str(label))*3.6-3}' y='{mid_y-14}' width='{len(str(label))*7.2+6}' height='15' fill='#fff' fill-opacity='0.9'/>"
                f"<text x='{mid_x}' y='{mid_y-3}' text-anchor='middle' font-size='11' fill='#333' {FONT}>{esc(label)}</text>")
    return svg


# ---------------------------------------------------------------- the view
def render(model: dict[str, Any]) -> str:
    grid = model.get("grid", {}) or {}
    elements = model.get("elements", []) or []
    groups = model.get("groups", []) or []
    relations = model.get("relations", []) or []
    notes = model.get("notes", []) or []
    boxes: dict[str, Box] = {}
    max_col = max_row = 0.0
    body: list[str] = []
    for group in groups:
        (c0, r0), (c1, r1) = group["from"], group["to"]
        box = cell_box(c0, r0, c1 - c0 + 1, r1 - r0 + 1, grid)
        pad = 14
        box = Box(box.x - pad, box.y - pad - 18, box.w + 2 * pad, box.h + 2 * pad + 18)
        boxes[group["id"]] = box
        body.append(element_svg({**group, "_group": True}, box))
        max_col, max_row = max(max_col, c1), max(max_row, r1)
    for element in elements:
        w, h = element.get("w", 1), element.get("h", 1)
        box = cell_box(element["col"], element["row"], w, h, grid)
        if element["id"] in boxes:
            raise SystemExit(f"duplicate element id {element['id']}")
        boxes[element["id"]] = box
        body.append(element_svg(element, box))
        max_col, max_row = max(max_col, element["col"] + w - 1), max(max_row, element["row"] + h - 1)
    for note in notes:
        w = note.get("w", 1)
        box = cell_box(note["col"], note["row"], w, note.get("h", 1), grid)
        lines = wrap(note["text"], box.w - 16, 11.5)
        body.append(
            f"<path d='M{box.x} {box.y} h{box.w-12} l12 12 v{box.h-12} h-{box.w} z' fill='#fffbe6' stroke='#999' stroke-width='1'/>"
            + "".join(
                f"<text x='{box.x+8}' y='{box.y+18+i*14}' font-size='11.5' fill='#444' {FONT}>{esc(line)}</text>"
                for i, line in enumerate(lines)
            )
        )
        max_col, max_row = max(max_col, note["col"] + w - 1), max(max_row, note["row"] + note.get("h", 1) - 1)
    for relation in relations:
        for end in ("from", "to"):
            if relation[end] not in boxes:
                raise SystemExit(f"relation refers to unknown element {relation[end]!r}")
        body.append(relation_svg(relation, boxes, grid))
    extent = cell_box(max_col, max_row, grid=grid)
    width = extent.x + extent.w + MARGIN
    height = extent.y + extent.h + MARGIN + 22
    title = model.get("title", model["id"])
    viewpoint = model.get("viewpoint", "")
    head = (
        f"<text x='{MARGIN}' y='{MARGIN}' font-size='16' font-weight='700' fill='#222' {FONT}>{esc(title)}</text>"
        f"<text x='{MARGIN}' y='{MARGIN+18}' font-size='11.5' fill='#666' {FONT}>"
        f"{esc(viewpoint + ' viewpoint · ' if viewpoint else '')}ArchiMate® 3.2 notation · original drawing for study, Northgate Bank is fictional</text>"
    )
    return (
        f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {width:.0f} {height:.0f}' width='{width:.0f}' height='{height:.0f}' role='img' aria-label='{esc(title)}'>\n"
        f"<!-- generated by draw_archimate.py from content/archimate/{model['id']}.yaml; do not edit by hand -->\n"
        f"<rect width='100%' height='100%' fill='#fff'/>\n{marker_defs()}\n{head}\n" + "\n".join(body) + "\n</svg>\n"
    )


def model_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes() + Path(__file__).read_bytes()).hexdigest()[:16]


def stamp(svg: str, digest: str) -> str:
    return svg.replace("do not edit by hand -->", f"do not edit by hand; source-hash {digest} -->", 1)


def is_stale(path: Path, out: Path) -> bool:
    if not out.is_file():
        return True
    return f"source-hash {model_hash(path)}" not in out.read_text(encoding="utf-8")[:600]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--check", action="store_true", help="report stale or missing SVGs and exit 1")
    parser.add_argument("--force", action="store_true", help="re-render every model")
    parser.add_argument("models", nargs="*", help="model ids to render (default: all)")
    args = parser.parse_args()
    paths = sorted(MODELS_DIR.glob("*.yaml"))
    if args.models:
        paths = [p for p in paths if p.stem in args.models]
    if not paths:
        raise SystemExit(f"no models under {MODELS_DIR}")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    stale = []
    for path in paths:
        with open(path, encoding="utf-8") as handle:
            model = yaml.safe_load(handle)
        if not isinstance(model, dict) or model.get("id") != path.stem:
            raise SystemExit(f"{path}: id must equal the file name ({path.stem})")
        out = OUT_DIR / f"{path.stem}.svg"
        if args.check:
            if is_stale(path, out):
                stale.append(path.stem)
            continue
        if not args.force and not is_stale(path, out):
            continue
        out.write_text(stamp(render(model), model_hash(path)), encoding="utf-8")
        print(f"rendered {out.relative_to(REPO)}")
    if args.check:
        if stale:
            print(f"stale or missing: {', '.join(stale)} — run python draw_archimate.py")
            sys.exit(1)
        print(f"{len(paths)} model(s) up to date")


if __name__ == "__main__":
    main()
