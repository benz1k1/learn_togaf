"""ADM explorer data (learn_togaf.md §4.3): phases, techniques, artefacts, figures and the SVG layout."""

import math
import sqlite3
from typing import Any

import orjson

_JSON_PHASE_COLUMNS = (
    "objective",
    "inputs",
    "steps",
    "outputs",
    "artefacts",
    "deliverables",
    "refs",
    "traps",
)
_JSON_TECHNIQUE_COLUMNS = ("phases", "artefacts", "traps", "refs")
CYCLE = ("A", "B", "C", "D", "E", "F", "G", "H")


def _decode(row: sqlite3.Row, columns: tuple[str, ...]) -> dict[str, Any]:
    data = dict(row)
    for column in columns:
        data[column] = orjson.loads(data[column])
    return data


def phases(connection: sqlite3.Connection) -> list[dict[str, Any]]:
    return [
        _decode(row, _JSON_PHASE_COLUMNS)
        for row in connection.execute("SELECT * FROM adm_phase ORDER BY ordinal").fetchall()
    ]


def phase(connection: sqlite3.Connection, code: str) -> dict[str, Any] | None:
    row = connection.execute("SELECT * FROM adm_phase WHERE code = ?", (code,)).fetchone()
    return _decode(row, _JSON_PHASE_COLUMNS) if row else None


def neighbours(
    connection: sqlite3.Connection, code: str
) -> tuple[dict[str, Any] | None, dict[str, Any] | None]:
    """Previous and next phase around the cycle: PRELIM → A … H → A; Requirements Management sits in the middle."""
    if code == "REQ":
        return None, None
    order = ["PRELIM", *CYCLE]
    index = order.index(code)
    previous = order[index - 1] if index > 0 else None
    following = order[index + 1] if index + 1 < len(order) else "A"
    return (phase(connection, previous) if previous else None), (
        phase(connection, following) if following else None
    )


def phase_artefacts(connection: sqlite3.Connection, phase_data: dict[str, Any]) -> list[sqlite3.Row]:
    codes = list(phase_data["artefacts"])
    placeholders = ",".join("?" for _ in codes) or "''"
    return connection.execute(
        f"SELECT * FROM adm_artefact WHERE code IN ({placeholders}) OR phase_code = ? ORDER BY kind, name",
        (*codes, phase_data["code"]),
    ).fetchall()


def phase_techniques(connection: sqlite3.Connection, code: str) -> list[sqlite3.Row]:
    return connection.execute(
        "SELECT code, name FROM adm_technique WHERE EXISTS (SELECT 1 FROM json_each(adm_technique.phases) WHERE value = ?) ORDER BY name",
        (code,),
    ).fetchall()


def phase_figures(connection: sqlite3.Connection, phase_data: dict[str, Any]) -> list[sqlite3.Row]:
    """Figures from the ADM document whose caption names the phase. Empty until the source store is indexed."""
    needles = [part.strip() for part in phase_data["name"].split(":") if part.strip()]
    clauses = " OR ".join("f.caption LIKE ?" for _ in needles)
    return connection.execute(
        f"""
        SELECT f.id, f.caption, f.width, f.height FROM source_figure f
        JOIN source_section s ON s.id = f.section_id
        WHERE s.document_code = 'ADM' AND ({clauses})
        ORDER BY f.id
        """,
        tuple(f"%{needle}%" for needle in needles),
    ).fetchall()


def technique(connection: sqlite3.Connection, code: str) -> dict[str, Any] | None:
    row = connection.execute("SELECT * FROM adm_technique WHERE code = ?", (code,)).fetchone()
    if row is None:
        return None
    data = _decode(row, _JSON_TECHNIQUE_COLUMNS)
    names = {p["code"]: p["name"] for p in phases(connection)}
    data["phase_links"] = [{"code": c, "name": names.get(c, c)} for c in data["phases"]]
    codes = data["artefacts"]
    placeholders = ",".join("?" for _ in codes) or "''"
    data["artefact_rows"] = connection.execute(
        f"SELECT * FROM adm_artefact WHERE code IN ({placeholders}) ORDER BY name", tuple(codes)
    ).fetchall()
    return data


def techniques(connection: sqlite3.Connection) -> list[sqlite3.Row]:
    return connection.execute("SELECT code, name FROM adm_technique ORDER BY name").fetchall()


def artefacts(
    connection: sqlite3.Connection, phase_code: str = "", domain: str = "", kind: str = ""
) -> list[sqlite3.Row]:
    clauses, params = [], []
    if phase_code:
        clauses.append("phase_code = ?")
        params.append(phase_code)
    if domain:
        clauses.append("domain = ?")
        params.append(domain)
    if kind:
        clauses.append("kind = ?")
        params.append(kind)
    where = f"WHERE {' AND '.join(clauses)}" if clauses else ""
    return connection.execute(
        f"SELECT * FROM adm_artefact {where} ORDER BY phase_code, kind, name", params
    ).fetchall()


def artefact_filters(connection: sqlite3.Connection) -> dict[str, list[str]]:
    return {
        "phases": [
            row[0]
            for row in connection.execute("SELECT DISTINCT phase_code FROM adm_artefact ORDER BY phase_code")
        ],
        "domains": [
            row[0] for row in connection.execute("SELECT DISTINCT domain FROM adm_artefact ORDER BY domain")
        ],
        "kinds": [
            row[0] for row in connection.execute("SELECT DISTINCT kind FROM adm_artefact ORDER BY kind")
        ],
    }


def cycle_layout(phase_rows: list[dict[str, Any]]) -> dict[str, Any]:
    """Coordinates for the inline SVG: Preliminary above, A–H clockwise from the top, REQ in the centre.
    Labels sit outside the ring, anchored away from the circle so the long ones do not cross it."""
    names = {p["code"]: p["name"] for p in phase_rows}
    width, height = 760, 660
    centre_x, centre_y, radius = width / 2, 380.0, 230.0
    nodes = []
    for index, code in enumerate(CYCLE):
        angle = -math.pi / 2 + index * (2 * math.pi / len(CYCLE))
        cos, sin = math.cos(angle), math.sin(angle)
        anchor = "start" if cos > 0.3 else "end" if cos < -0.3 else "middle"
        nodes.append(
            {
                "code": code,
                "label": names[code].split(":", 1)[-1].strip(),
                "x": round(centre_x + radius * cos, 1),
                "y": round(centre_y + radius * sin, 1),
                "label_x": round(centre_x + (radius + 56) * cos, 1),
                "label_y": round(
                    centre_y + (radius + 56) * sin + (4 if anchor != "middle" else (14 if sin > 0 else -6)), 1
                ),
                "anchor": anchor,
            }
        )
    return {
        "width": width,
        "height": height,
        "centre": {"x": centre_x, "y": centre_y, "radius": radius},
        "prelim": {"code": "PRELIM", "label": names["PRELIM"], "x": centre_x, "y": 48},
        "req": {"code": "REQ", "label": names["REQ"], "x": centre_x, "y": centre_y},
        "nodes": nodes,
    }
