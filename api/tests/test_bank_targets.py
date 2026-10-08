"""
The coverage floors (learn_togaf.md §6; learn_sabsa_archimate.md §4.3), asserted per exam. This
module is EXPECTED to fail until every bank reaches target — it is the build gate, not a bug.
Run the rest of the suite with `-k "not bank_targets"` while the banks are being built.

Single-answer exams: ≥ 10 reviewed questions per objective, ≥ 10 × weight per unit, total
≥ 10 × the paper. Gradient exams: ≥ 5 reviewed scenarios per weighted unit of the track, total
≥ 6 × the paper (48 for an eight-scenario exam).
"""

from collections import Counter

import pytest

from learn_togaf.config import CONTENT_DIR
from learn_togaf.content.loader import load_blueprint, load_question_sets

SINGLE_PER_OBJECTIVE = 10
SINGLE_UNIT_MULTIPLIER = 10
SINGLE_TOTAL_MULTIPLIER = 10
GRADIENT_PER_UNIT = 5
GRADIENT_TOTAL_MULTIPLIER = 6


def _reviewed_by_exam():
    blueprint = load_blueprint(CONTENT_DIR)
    sets = load_question_sets(CONTENT_DIR, blueprint)
    by_exam: dict[str, list] = {code: [] for code in blueprint.exams}
    for question_set in sets:
        by_exam[question_set.exam].extend(q for q in question_set.questions() if q.status == "reviewed")
    return blueprint, by_exam


@pytest.mark.parametrize("code", ["OGEA-101", "OGEA-102", "OGA-031", "OGA-032", "SCF"])
def test_bank_reaches_target(code: str) -> None:
    blueprint, by_exam = _reviewed_by_exam()
    exam = blueprint.exam(code)
    questions = by_exam[code]
    shortfalls = []
    by_unit = Counter(q.unit for q in questions)
    by_objective = Counter(q.objective for q in questions)
    if exam.scoring == "single":
        total = SINGLE_TOTAL_MULTIPLIER * exam.questions
        if len(questions) < total:
            shortfalls.append(f"total reviewed {len(questions)} < {total}")
        for unit in blueprint.units:
            if unit.exam != code:
                continue
            floor = unit.weight * SINGLE_UNIT_MULTIPLIER
            if by_unit[unit.code] < floor:
                shortfalls.append(f"{unit.code}: {by_unit[unit.code]} < {floor}")
            for objective in unit.objectives:
                if by_objective[objective.code] < SINGLE_PER_OBJECTIVE:
                    shortfalls.append(
                        f"objective {objective.code}: {by_objective[objective.code]} < {SINGLE_PER_OBJECTIVE}"
                    )
    else:
        total = GRADIENT_TOTAL_MULTIPLIER * exam.questions
        if len(questions) < total:
            shortfalls.append(f"total reviewed {len(questions)} < {total}")
        for unit in blueprint.units:
            if unit.track == exam.track and unit.weight > 0 and unit.code[0] != "G":
                if unit.exam == code or exam.track != "TOGAF":
                    if by_unit[unit.code] < GRADIENT_PER_UNIT:
                        shortfalls.append(f"{unit.code}: {by_unit[unit.code]} < {GRADIENT_PER_UNIT}")
    if shortfalls:
        pytest.fail(f"{exam.label} bank below target: " + "; ".join(shortfalls))
