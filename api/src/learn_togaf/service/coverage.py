"""Coverage and question quality for the author (learn_togaf.md §4.9, §6)."""

import sqlite3
import statistics
from pathlib import Path
from typing import Any

SINGLE_FLOOR = 8  # reviewed single-answer questions per objective
GRADIENT_FLOOR = 2  # reviewed scenarios per objective of a gradient exam
MIN_ANSWERS = 5
GUESSABLE_SECONDS = 5


def objectives(connection: sqlite3.Connection) -> list[dict[str, Any]]:
    rows = connection.execute(
        """
        SELECT o.code, o.text, o.unit_code, u.exam, u.track, u.scoring,
               (SELECT COUNT(*) FROM objective_source os WHERE os.objective_code = o.code) AS sources,
               (SELECT COUNT(*) FROM lesson_objective lo WHERE lo.objective_code = o.code) AS lessons,
               (SELECT COUNT(*) FROM glossary_term g, json_each(g.objectives) j WHERE j.value = o.code) AS terms,
               (SELECT COUNT(*) FROM question q WHERE q.objective_code = o.code) AS questions,
               (SELECT COUNT(*) FROM question q WHERE q.objective_code = o.code AND q.scoring = 'single' AND q.status = 'reviewed') AS reviewed_single,
               (SELECT COUNT(*) FROM question q WHERE q.objective_code = o.code AND q.scoring = 'gradient' AND q.status = 'reviewed') AS reviewed_gradient
        FROM objective o JOIN learning_unit u ON u.code = o.unit_code
        ORDER BY u.ordinal, o.ordinal
        """
    ).fetchall()
    result = []
    for row in rows:
        item = dict(row)
        item["cards"] = item["terms"] + item["questions"]
        flags = []
        if not item["sources"]:
            flags.append("no source")
        if not item["lessons"]:
            flags.append("no lesson")
        if not item["cards"]:
            flags.append("no cards")
        if item["scoring"] == "single" and item["reviewed_single"] < SINGLE_FLOOR:
            flags.append(f"reviewed single-answer {item['reviewed_single']}/{SINGLE_FLOOR}")
        if item["scoring"] == "gradient" and item["reviewed_gradient"] < GRADIENT_FLOOR:
            flags.append(f"reviewed scenarios {item['reviewed_gradient']}/{GRADIENT_FLOOR}")
        item["flags"] = flags
        result.append(item)
    return result


def orphan_figures(connection: sqlite3.Connection) -> list[sqlite3.Row]:
    return connection.execute(
        """
        SELECT f.id, f.caption, f.document_code, f.important FROM source_figure f
        WHERE NOT EXISTS (SELECT 1 FROM question q WHERE q.figure_id = f.id)
          AND NOT EXISTS (SELECT 1 FROM lesson l WHERE instr(l.body_md, f.id) > 0)
        ORDER BY f.important DESC, f.id
        """
    ).fetchall()


def drafts_waiting(content_dir: Path) -> int:
    review_dir = content_dir / "review"
    if not review_dir.is_dir():
        return 0
    return sum(1 for path in review_dir.rglob("*") if path.is_file() and not path.name.startswith("."))


def question_quality(connection: sqlite3.Connection) -> dict[str, list[dict[str, Any]]]:
    answers = connection.execute(
        """
        SELECT aa.question_id, aa.points, aa.seconds, q.exam, q.scoring, q.objective_code
        FROM attempt_answer aa JOIN question q ON q.id = aa.question_id
        WHERE aa.answered_at IS NOT NULL AND aa.chosen_key IS NOT NULL
        """
    ).fetchall()
    grouped: dict[str, list[sqlite3.Row]] = {}
    for row in answers:
        grouped.setdefault(row["question_id"], []).append(row)
    too_easy, guessable, weak_why = [], [], []
    for question_id, rows in grouped.items():
        scoring = rows[0]["scoring"]
        max_points = 5 if scoring == "gradient" else 1
        if len(rows) >= MIN_ANSWERS and all(row["points"] == max_points for row in rows):
            too_easy.append({"id": question_id, "answers": len(rows), "objective": rows[0]["objective_code"]})
        seconds = [row["seconds"] for row in rows if row["seconds"] is not None]
        if len(seconds) >= MIN_ANSWERS and statistics.median(seconds) < GUESSABLE_SECONDS:
            guessable.append(
                {"id": question_id, "answers": len(rows), "median_seconds": statistics.median(seconds)}
            )
        if scoring == "gradient":
            three = sum(1 for row in rows if row["points"] == 3)
            five = sum(1 for row in rows if row["points"] == 5)
            if three > five:
                weak_why.append({"id": question_id, "answers": len(rows), "three": three, "five": five})
    return {"too_easy": too_easy, "guessable": guessable, "weak_why": weak_why}


def report(connection: sqlite3.Connection, content_dir: Path) -> dict[str, Any]:
    objective_rows = objectives(connection)
    return {
        "objectives": objective_rows,
        "flagged": sum(1 for item in objective_rows if item["flags"]),
        "orphan_figures": orphan_figures(connection),
        "drafts_waiting": drafts_waiting(content_dir),
        "quality": question_quality(connection),
        "single_floor": SINGLE_FLOOR,
        "gradient_floor": GRADIENT_FLOOR,
    }
