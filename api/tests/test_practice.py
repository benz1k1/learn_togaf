"""Practice engine (learn_togaf.md §0, §4.6, §8): blueprint draws, seeded retakes, the server-side clock, scoring."""

import re
from datetime import UTC, datetime, timedelta

import orjson
import pytest
from conftest import get, post

from learn_togaf.db import transaction
from learn_togaf.service import practice as engine

CREATED: list[int] = []


@pytest.fixture(scope="module", autouse=True)
def _cleanup_attempts(db):
    yield
    if CREATED:
        with transaction(db):
            db.execute(f"DELETE FROM attempt WHERE id IN ({','.join('?' * len(CREATED))})", CREATED)


def _start(client, data: dict) -> int:
    response = post(client, "/practice", data)
    assert response.status_code == 303, response.text
    location = response.headers["location"]
    match = re.fullmatch(r"/attempt/(\d+)", location)
    if match is None:
        pytest.fail(f"POST /practice redirected to {location}, expected /attempt/<id>")
    attempt_id = int(match.group(1))
    CREATED.append(attempt_id)
    return attempt_id


def _ids(db, attempt_id: int) -> list[str]:
    return orjson.loads(
        db.execute("SELECT question_ids FROM attempt WHERE id = ?", (attempt_id,)).fetchone()[0]
    )


def _keys(db, question_id: str) -> dict[int, str]:
    """points → option key for a question."""
    return {
        row["points"]: row["key"]
        for row in db.execute("SELECT key, points FROM question_option WHERE question_id = ?", (question_id,))
    }


def _answer(client, attempt_id: int, index: int, question_id: str, key: str, seconds: int = 5):
    return post(
        client,
        f"/attempt/{attempt_id}/answer",
        {"index": index, "question_id": question_id, "key": key, "seconds": seconds},
        htmx=True,
    )


# ---------------------------------------------------------------- draws (pure, over the connection)
def test_foundation_mock_draws_the_blueprint_counts(db) -> None:
    units = db.execute(
        "SELECT code, weight FROM learning_unit WHERE exam = 'OGEA-101' AND weight > 0"
    ).fetchall()
    assert sum(unit["weight"] for unit in units) == 40
    draw = engine.draw_mock(db, "OGEA-101", seed=42)
    assert draw.exam == "OGEA-101" and draw.mode == "MOCK" and draw.time_limit_s == 3600
    assert len(draw.question_ids) == len(set(draw.question_ids)), "no question twice"
    by_unit: dict[str, int] = {}
    for question_id in draw.question_ids:
        unit = db.execute("SELECT unit_code FROM question WHERE id = ?", (question_id,)).fetchone()[
            "unit_code"
        ]
        by_unit[unit] = by_unit.get(unit, 0) + 1
    for unit in units:
        available = db.execute(
            "SELECT COUNT(*) FROM question WHERE exam = 'OGEA-101' AND unit_code = ?", (unit["code"],)
        ).fetchone()[0]
        reviewed = db.execute(
            "SELECT COUNT(*) FROM question WHERE exam = 'OGEA-101' AND unit_code = ? AND status = 'reviewed'",
            (unit["code"],),
        ).fetchone()[0]
        assert by_unit.get(unit["code"], 0) == min(unit["weight"], available), f"unit {unit['code']}"
        if reviewed < unit["weight"]:
            assert unit["code"] in draw.short_units, (
                f"{unit['code']} lacks reviewed questions and must be flagged"
            )
        else:
            assert unit["code"] not in draw.short_units
    if draw.short_units:
        assert draw.filters == {"short_units": draw.short_units}
    else:
        assert len(draw.question_ids) == 40


def test_same_seed_same_paper_different_seed_differs(db) -> None:
    first = engine.draw_mock(db, "OGEA-101", seed=7)
    again = engine.draw_mock(db, "OGEA-101", seed=7)
    assert first.question_ids == again.question_ids
    other = engine.draw_mock(db, "OGEA-101", seed=8)
    assert set(other.question_ids) != set(first.question_ids) or other.question_ids != first.question_ids
    drill = engine.draw_drill(db, "OGEA-101", ["F4"], [], 5, True, "all", seed=3)
    assert (
        drill.question_ids
        == engine.draw_drill(db, "OGEA-101", ["F4"], [], 5, True, "all", seed=3).question_ids
    )
    assert len(drill.question_ids) == 5 and drill.time_limit_s is None


def test_drill_filters_and_empty_draw(db) -> None:
    drill = engine.draw_drill(db, "OGEA-101", ["F1", "F2"], ["1.3"], 10, True, "all", seed=1)
    for question_id in drill.question_ids:
        row = db.execute(
            "SELECT unit_code, objective_code FROM question WHERE id = ?", (question_id,)
        ).fetchone()
        assert row["objective_code"] == "1.3"
    with pytest.raises(engine.DrawError):
        engine.draw_drill(db, "OGEA-101", ["F1"], [], 5, True, "imported", seed=1)
    reviewed = db.execute(
        "SELECT COUNT(*) FROM question WHERE exam = 'OGEA-101' AND status = 'reviewed'"
    ).fetchone()[0]
    if reviewed:
        strict = engine.draw_drill(db, "OGEA-101", [], [], 5, False, "all", seed=1)
        assert len(strict.question_ids) == min(5, reviewed)
    else:
        with pytest.raises(engine.DrawError):
            engine.draw_drill(db, "OGEA-101", [], [], 5, False, "all", seed=1)


def test_phase_io_drill_is_foundation_f4(db) -> None:
    drill = engine.draw_phase_io_drill(db, "A", 10, seed=2)
    assert drill.filters["phase"] == "A" and drill.filters["kind"] == "io"
    for question_id in drill.question_ids:
        row = db.execute("SELECT unit_code, exam FROM question WHERE id = ?", (question_id,)).fetchone()
        assert (row["exam"], row["unit_code"]) == ("OGEA-101", "F4")
    with pytest.raises(engine.DrawError):
        engine.draw_phase_io_drill(db, "Z", 10, seed=2)


def test_practitioner_mock_draw(db) -> None:
    draw = engine.draw_mock(db, "OGEA-102", seed=5)
    assert draw.exam == "OGEA-102" and draw.time_limit_s == 5400
    available = db.execute("SELECT COUNT(*) FROM question WHERE exam = 'OGEA-102'").fetchone()[0]
    assert len(draw.question_ids) == min(8, available)
    assert draw.question_ids == engine.draw_mock(db, "OGEA-102", seed=5).question_ids


# ---------------------------------------------------------------- scoring (pure)
def test_scoring_matches_the_exam_formats() -> None:
    assert engine.score_answers([1, 0, None, 1]) == 2
    assert engine.score_answers([5, 3, 1, 0, None]) == 9
    assert engine.max_score_for("OGEA-101", "MOCK", 38) == 40, (
        "a mock is out of 40 even when the paper is short"
    )
    assert engine.max_score_for("OGEA-102", "MOCK", 8) == 40
    assert engine.max_score_for("OGEA-101", "DRILL", 7) == 7
    assert engine.max_score_for("OGEA-102", "DRILL", 2) == 10
    assert engine.pass_mark_for("OGEA-101") == 24
    assert engine.pass_mark_for("OGEA-102") == 24


def test_clock_is_pure_over_the_row() -> None:
    started = datetime(2026, 9, 10, 12, 0, tzinfo=UTC)
    row = {"time_limit_s": 3600, "started_at": started.isoformat(timespec="seconds"), "finished_at": None}
    assert engine.remaining_seconds(row, started + timedelta(minutes=10)) == 3000
    assert engine.remaining_seconds(row, started + timedelta(hours=2)) == 0
    assert engine.is_expired(row, started + timedelta(hours=1, seconds=1))
    assert engine.remaining_seconds({"time_limit_s": None, "started_at": row["started_at"]}, started) is None


# ---------------------------------------------------------------- HTTP: drill
def test_practice_page_and_preselects(client) -> None:
    page = client.get("/practice").text
    for mode in engine.MODES:
        assert f'name="mode" value="{mode}"' in page
    assert 'name="include_drafts"' in page and "checked" in page
    objective_page = client.get("/practice?objective=4.3").text
    assert re.search(r'name="objectives" value="4\.3"[^>]*checked', objective_page)
    io_page = client.get("/practice?phase=A&kind=io").text
    assert 'name="phase" value="A"' in io_page and 'name="kind" value="io"' in io_page
    assert client.get("/practice?objective=nope").status_code == 404


def test_drill_reveals_explanation_and_locks(client, db) -> None:
    attempt_id = _start(
        client,
        {
            "mode": "DRILL",
            "exam": "OGEA-101",
            "units": "F4",
            "count": 3,
            "include_drafts": "on",
            "sources": "all",
            "seed": 11,
        },
    )
    ids = _ids(db, attempt_id)
    assert len(ids) == 3
    page = client.get(f"/attempt/{attempt_id}")
    assert page.status_code == 200 and "untimed" in page.text
    assert 'data-testid="open-book"' not in page.text, "Foundation is closed book"

    fragment = get(client, f"/attempt/{attempt_id}/question/0", htmx=True)
    assert fragment.status_code == 200
    assert f'data-question-id="{ids[0]}"' in fragment.text
    assert 'data-testid="explanation"' not in fragment.text
    assert 'id="navigator"' in fragment.text and "hx-swap-oob" in fragment.text

    correct = _keys(db, ids[0])[1]
    revealed = _answer(client, attempt_id, 0, ids[0], correct, seconds=9)
    assert revealed.status_code == 200
    assert 'data-testid="explanation"' in revealed.text and "Correct" in revealed.text
    assert 'data-index="0"' in revealed.text, "a drill stays on the question to show the explanation"
    assert _answer(client, attempt_id, 0, ids[0], "A").status_code == 409, (
        "a drill locks an answered question"
    )

    wrong = _keys(db, ids[1])[0]
    assert "Not quite" in _answer(client, attempt_id, 1, ids[1], wrong).text

    flagged = post(client, f"/attempt/{attempt_id}/flag", {"index": 2, "question_id": ids[2]}, htmx=True)
    assert flagged.status_code == 200 and 'data-flagged="1"' in flagged.text

    finished = post(client, f"/attempt/{attempt_id}/finish", htmx=True)
    assert finished.status_code == 200 and finished.headers["hx-redirect"] == f"/attempt/{attempt_id}/review"
    row = db.execute("SELECT * FROM attempt WHERE id = ?", (attempt_id,)).fetchone()
    assert (row["score"], row["max_score"], row["passed"]) == (1, 3, None)
    review = client.get(f"/attempt/{attempt_id}/review").text
    assert "1 / 3" in review and "drill — no pass mark" in review
    assert 'data-testid="retake-identical"' in review and f'name="seed" value="{row["seed"]}"' in review
    assert client.get(f"/attempt/{attempt_id}").headers["location"] == f"/attempt/{attempt_id}/review"
    cards = {
        r["card_ref"] for r in db.execute("SELECT card_ref FROM card_review WHERE card_kind = 'QUESTION'")
    }
    assert {ids[1], ids[2]} <= cards, "the wrong and the unanswered question become QUESTION cards"


# ---------------------------------------------------------------- HTTP: mocks and the clock
def test_foundation_mock_flow_with_short_units_warning(client, db) -> None:
    attempt_id = _start(client, {"mode": "MOCK", "exam": "OGEA-101", "seed": 42})
    row = db.execute("SELECT * FROM attempt WHERE id = ?", (attempt_id,)).fetchone()
    assert row["time_limit_s"] == 3600 and row["mode"] == "MOCK"
    ids = _ids(db, attempt_id)
    assert ids == engine.draw_mock(db, "OGEA-101", 42).question_ids, "the recorded paper is the seeded draw"
    page = client.get(f"/attempt/{attempt_id}")
    filters = orjson.loads(row["filters"])
    if filters.get("short_units"):
        assert 'data-testid="short-units-warning"' in page.text
    else:
        assert len(ids) == 40 and 'data-testid="short-units-warning"' not in page.text

    first = client.get(f"/api/attempt/{attempt_id}/timer").json()
    second = client.get(f"/api/attempt/{attempt_id}/timer").json()
    assert 3500 < second["remaining_s"] <= first["remaining_s"] <= 3600 and not second["finished"]
    fragment = client.get(f"/attempt/{attempt_id}/timer")
    assert fragment.status_code == 200 and 'hx-trigger="every 15s"' in fragment.text

    keys = _keys(db, ids[0])
    moved = _answer(client, attempt_id, 0, ids[0], keys[1])
    assert moved.status_code == 200 and 'data-index="1"' in moved.text, "a mock records and moves on"
    assert 'data-testid="explanation"' not in moved.text
    changed = _answer(client, attempt_id, 0, ids[0], keys[0])
    assert changed.status_code == 200
    answer = db.execute(
        "SELECT * FROM attempt_answer WHERE attempt_id = ? AND question_id = ?", (attempt_id, ids[0])
    ).fetchone()
    assert (answer["chosen_key"], answer["points"], answer["changed_from_correct"]) == (keys[0], 0, 1)
    assert answer["seconds"] == 10, "seconds accumulate across changes"

    for index in range(1, 25):
        _answer(client, attempt_id, index, ids[index], _keys(db, ids[index])[1])
    finished = post(client, f"/attempt/{attempt_id}/finish")
    assert finished.status_code == 303
    row = db.execute("SELECT * FROM attempt WHERE id = ?", (attempt_id,)).fetchone()
    assert (row["score"], row["max_score"], row["passed"]) == (24, 40, 1)
    review = client.get(f"/attempt/{attempt_id}/review").text
    assert "24 / 40" in review and "PASS" in review and "pass mark 24" in review
    assert re.search(r'data-testid="changed-from-correct">1<', review)
    assert 'data-testid="per-unit"' in review and 'data-testid="per-objective"' in review


def test_clock_is_enforced_server_side(client, db) -> None:
    attempt_id = _start(client, {"mode": "MOCK", "exam": "OGEA-101", "seed": 43})
    ids = _ids(db, attempt_id)
    with transaction(db):
        db.execute(
            "UPDATE attempt SET started_at = ? WHERE id = ?",
            ((datetime.now(UTC) - timedelta(hours=2)).isoformat(timespec="seconds"), attempt_id),
        )
    refused = _answer(client, attempt_id, 0, ids[0], "A")
    assert refused.status_code == 409 and refused.json()["success"] is False
    assert refused.headers["hx-redirect"] == f"/attempt/{attempt_id}/review"
    timer = client.get(f"/api/attempt/{attempt_id}/timer").json()
    assert timer == {"remaining_s": 0, "finished": True}
    row = db.execute("SELECT score, max_score, passed FROM attempt WHERE id = ?", (attempt_id,)).fetchone()
    assert tuple(row) == (0, 40, 0)


def test_practitioner_mock_gradient_and_open_book(client, db) -> None:
    attempt_id = _start(client, {"mode": "MOCK", "exam": "OGEA-102", "seed": 5})
    row = db.execute("SELECT * FROM attempt WHERE id = ?", (attempt_id,)).fetchone()
    assert row["time_limit_s"] == 5400 and row["exam"] == "OGEA-102"
    ids = _ids(db, attempt_id)
    page = client.get(f"/attempt/{attempt_id}").text
    assert 'data-testid="open-book"' in page, "Part 2 is open book"
    fragment = get(client, f"/attempt/{attempt_id}/question/0", htmx=True).text
    assert 'data-testid="scenario"' in fragment and "5 / 3 / 1 / 0" in fragment
    keys = _keys(db, ids[0])
    assert set(keys) == {5, 3, 1, 0}
    _answer(client, attempt_id, 0, ids[0], keys[3], seconds=40)
    assert post(client, f"/attempt/{attempt_id}/finish").status_code == 303
    row = db.execute("SELECT * FROM attempt WHERE id = ?", (attempt_id,)).fetchone()
    assert (row["score"], row["max_score"], row["passed"]) == (3, 40, 0)
    review = client.get(f"/attempt/{attempt_id}/review").text
    assert (
        review.count(">5 pts<") >= len(ids)
        and ">3 pts<" in review
        and ">1 pts<" in review
        and ">0 pts<" in review
    )
    assert "FAIL" in review
    cards = {
        r["card_ref"] for r in db.execute("SELECT card_ref FROM card_review WHERE card_kind = 'QUESTION'")
    }
    assert set(ids) <= cards, "anything under 5 points becomes a QUESTION card"


def test_retake_identical_over_http(client, db) -> None:
    first = _start(
        client,
        {
            "mode": "DRILL",
            "exam": "OGEA-101",
            "units": "F5",
            "count": 4,
            "include_drafts": "on",
            "sources": "all",
            "seed": 99,
        },
    )
    second = _start(
        client,
        {
            "mode": "DRILL",
            "exam": "OGEA-101",
            "units": "F5",
            "count": 4,
            "include_drafts": "on",
            "sources": "all",
            "seed": 99,
        },
    )
    assert _ids(db, first) == _ids(db, second)


def test_empty_draw_bounces_with_a_flash(client) -> None:
    response = post(
        client,
        "/practice",
        {
            "mode": "DRILL",
            "exam": "OGEA-101",
            "units": "F1",
            "count": 5,
            "include_drafts": "on",
            "sources": "imported",
        },
    )
    assert response.status_code == 303 and response.headers["location"].startswith("/practice?flash=")
    assert post(client, "/practice", {"mode": "NOPE", "exam": "OGEA-101"}).status_code == 422
    assert post(client, "/practice", {"mode": "DRILL", "exam": "NOPE"}).status_code == 422
    assert client.get("/attempt/999999999").status_code == 404


def test_open_book_search(client) -> None:
    results = get(client, "/open-book?q=stakeholder", htmx=True).text
    assert "/glossary/" in results and 'id="open-book"' not in results, "htmx gets the result rows only"
    panel = client.get("/open-book?q=phase").text
    assert 'id="open-book"' in panel and "/adm/" in panel
    assert get(client, "/open-book?q=x", htmx=True).text.strip() == ""
