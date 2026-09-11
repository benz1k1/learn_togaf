"""
The §6 coverage floors, asserted per unit. This module is EXPECTED to fail until the bank
reaches target — it is the build gate, not a bug. Run the rest of the suite with
`-k "not bank_targets"` while the bank is being built.
"""

from collections import Counter

import pytest

from learn_togaf.config import CONTENT_DIR
from learn_togaf.content.loader import load_blueprint, load_question_sets

FOUNDATION_TOTAL = 400
FOUNDATION_PER_OBJECTIVE = 10
FOUNDATION_UNIT_MULTIPLIER = 10
PRACTITIONER_TOTAL = 48
PRACTITIONER_PER_UNIT = 5


def _reviewed():
    blueprint = load_blueprint(CONTENT_DIR)
    sets = load_question_sets(CONTENT_DIR, blueprint)
    foundation = [q for s in sets for q in s.foundation if q.status == "reviewed"]
    practitioner = [q for s in sets for q in s.practitioner if q.status == "reviewed"]
    return blueprint, foundation, practitioner


def test_foundation_bank_reaches_target() -> None:
    blueprint, foundation, _ = _reviewed()
    shortfalls = []
    if len(foundation) < FOUNDATION_TOTAL:
        shortfalls.append(f"total reviewed {len(foundation)} < {FOUNDATION_TOTAL}")
    by_unit = Counter(q.unit for q in foundation)
    by_objective = Counter(q.objective for q in foundation)
    for unit in blueprint.units:
        if unit.exam != "FOUNDATION":
            continue
        floor = unit.weight * FOUNDATION_UNIT_MULTIPLIER
        if by_unit[unit.code] < floor:
            shortfalls.append(f"{unit.code}: {by_unit[unit.code]} < {floor}")
        for objective in unit.objectives:
            if by_objective[objective.code] < FOUNDATION_PER_OBJECTIVE:
                shortfalls.append(
                    f"objective {objective.code}: {by_objective[objective.code]} < {FOUNDATION_PER_OBJECTIVE}"
                )
    if shortfalls:
        pytest.fail("Foundation bank below target: " + "; ".join(shortfalls))


def test_practitioner_bank_reaches_target() -> None:
    blueprint, _, practitioner = _reviewed()
    shortfalls = []
    if len(practitioner) < PRACTITIONER_TOTAL:
        shortfalls.append(f"total reviewed {len(practitioner)} < {PRACTITIONER_TOTAL}")
    by_unit = Counter(q.unit for q in practitioner)
    for unit in blueprint.units:
        if unit.exam == "PRACTITIONER" and unit.weight > 0 and by_unit[unit.code] < PRACTITIONER_PER_UNIT:
            shortfalls.append(f"{unit.code}: {by_unit[unit.code]} < {PRACTITIONER_PER_UNIT}")
    if shortfalls:
        pytest.fail("Practitioner bank below target: " + "; ".join(shortfalls))
