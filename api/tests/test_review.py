"""Flashcards (learn_togaf.md §4.5, §8): SM-2 reference sequences, generated cards, the due queue over HTTP."""

import re
from datetime import UTC, datetime, timedelta

import pytest
from conftest import get, post

from learn_togaf.db import transaction
from learn_togaf.pages.context import get_setting, set_setting
from learn_togaf.service import review as review_service
from learn_togaf.service.review import Sm2State, sm2, sm2_sequence

FRESH = Sm2State(interval_days=0.0, ease=2.5, reps=0, lapses=0)


def _ease_after(ease: float, grade: int) -> float:
    return max(1.3, ease + 0.1 - (5 - grade) * (0.08 + (5 - grade) * 0.02))


# ---------------------------------------------------------------- SM-2 (pure)
@pytest.mark.parametrize("grade", [0, 1, 2, 3, 4, 5])
def test_sm2_single_grade_from_fresh(grade: int) -> None:
    state = sm2(FRESH, grade)
    assert state.ease == pytest.approx(_ease_after(2.5, grade))
    if grade < 3:
        assert (state.reps, state.lapses, state.interval_days) == (0, 1, 1.0)
    else:
        assert (state.reps, state.lapses, state.interval_days) == (1, 0, 1.0)


def test_sm2_reference_sequence_easy_then_lapse() -> None:
    states = sm2_sequence([5, 5, 5, 4, 2, 3, 3, 3])
    intervals = [state.interval_days for state in states]
    reps = [state.reps for state in states]
    lapses = [state.lapses for state in states]
    # 1, 6, round(6 × 2.8)=17, round(17 × 2.8)=48, lapse → 1, then 1, 6, round(6 × 2.06)=12
    assert intervals == [1.0, 6.0, 17.0, 48.0, 1.0, 1.0, 6.0, 12.0]
    assert reps == [1, 2, 3, 4, 0, 1, 2, 3]
    assert lapses == [0, 0, 0, 0, 1, 1, 1, 1]
    assert states[0].ease == pytest.approx(2.6)
    assert states[3].ease == pytest.approx(2.8)
    assert states[4].ease == pytest.approx(2.48)
    assert states[7].ease == pytest.approx(2.06)


def test_sm2_ease_floor_and_rejects_bad_grade() -> None:
    state = FRESH
    for _ in range(10):
        state = sm2(state, 0)
    assert state.ease == pytest.approx(1.3)
    assert state.lapses == 10
    with pytest.raises(ValueError):
        sm2(FRESH, 6)


# ---------------------------------------------------------------- generated deck
def test_review_page_generates_the_deck_from_content(client, db) -> None:
    assert client.get("/review").status_code == 200
    expected = {
        "TERM": db.execute("SELECT COUNT(*) FROM glossary_term").fetchone()[0],
        "PHASE_IO": 3 * db.execute("SELECT COUNT(*) FROM adm_phase").fetchone()[0],
        "TECHNIQUE": db.execute("SELECT COUNT(*) FROM adm_technique").fetchone()[0],
        "ARTEFACT": db.execute("SELECT COUNT(*) FROM adm_artefact").fetchone()[0],
        "FIGURE": db.execute("SELECT COUNT(*) FROM source_figure WHERE important = 1").fetchone()[0],
    }
    assert expected["TERM"] > 0, "content must be loaded (glossary empty)"
    for kind, count in expected.items():
        actual = db.execute("SELECT COUNT(*) FROM card_review WHERE card_kind = ?", (kind,)).fetchone()[0]
        assert actual == count, f"{kind}: {actual} cards for {count} content items"
    refs = db.execute("SELECT card_ref FROM card_review WHERE card_kind = 'PHASE_IO'").fetchall()
    facets = {row["card_ref"].split(":")[1] for row in refs}
    assert facets == {"inputs", "outputs", "objectives"}
    payload = client.get("/api/review/due").json()
    assert set(payload) == {"due", "total"}
    assert payload["total"] >= sum(expected.values())


def test_rebuild_adds_nothing_twice_and_keeps_state(client, db) -> None:
    before = db.execute("SELECT COUNT(*) FROM card_review").fetchone()[0]
    sample = db.execute(
        "SELECT id, ease, reps, interval_days FROM card_review ORDER BY id LIMIT 1"
    ).fetchone()
    response = post(client, "/review/rebuild")
    assert response.status_code == 303
    assert response.headers["location"].startswith("/review?flash=0+new+cards")
    assert db.execute("SELECT COUNT(*) FROM card_review").fetchone()[0] == before
    after = db.execute(
        "SELECT id, ease, reps, interval_days FROM card_review WHERE id = ?", (sample["id"],)
    ).fetchone()
    assert tuple(after) == tuple(sample)


def test_every_card_kind_renders_front_and_back(db) -> None:
    kinds = [row["card_kind"] for row in db.execute("SELECT DISTINCT card_kind FROM card_review")]
    assert {"TERM", "PHASE_IO", "TECHNIQUE", "ARTEFACT"} <= set(kinds)
    for kind in kinds:
        card = db.execute(
            "SELECT * FROM card_review WHERE card_kind = ? ORDER BY id LIMIT 1", (kind,)
        ).fetchone()
        content = review_service.card_content(db, card)
        assert content is not None, f"{kind} card {card['card_ref']} has no content"
        assert content["front"] or content["front_image"], f"{kind} card has an empty front"
        assert content["back_lines"] and all(content["back_lines"]), f"{kind} card has an empty back"
    term = db.execute("SELECT * FROM card_review WHERE card_kind = 'TERM' ORDER BY id LIMIT 1").fetchone()
    content = review_service.card_content(db, term)
    assert "§" in content["back_note"], "a TERM back names document and section"


def test_card_for_removed_content_is_skipped_not_deleted(db) -> None:
    ghost = {"id": -1, "card_kind": "TERM", "card_ref": "no-such-term-xyz"}
    assert review_service.card_content(db, ghost) is None


# ---------------------------------------------------------------- queue over HTTP
def test_next_card_then_grade_reschedules(client, db) -> None:
    response = get(client, "/review/next", htmx=True)
    assert response.status_code == 200
    match = re.search(r'data-card-id="(\d+)"', response.text)
    if match is None:
        pytest.fail(f"no due card rendered (daily cap reached or nothing due): {response.text[:300]}")
    card_id = int(match.group(1))
    assert f'hx-post="/review/{card_id}/grade"' in response.text
    assert "x-data" in response.text and 'x-ref="g5"' in response.text, (
        "the card is an Alpine component with grade refs"
    )
    before = db.execute("SELECT * FROM card_review WHERE id = ?", (card_id,)).fetchone()
    expected = sm2(Sm2State(before["interval_days"], before["ease"], before["reps"], before["lapses"]), 4)

    graded = post(client, f"/review/{card_id}/grade", {"grade": 4}, htmx=True)
    assert graded.status_code == 200
    assert 'id="review-stats"' in graded.text and "hx-swap-oob" in graded.text
    after = db.execute("SELECT * FROM card_review WHERE id = ?", (card_id,)).fetchone()
    assert after["last_grade"] == 4
    assert after["reps"] == expected.reps
    assert after["interval_days"] == expected.interval_days
    assert after["ease"] == pytest.approx(expected.ease)
    due_at = datetime.fromisoformat(after["due_at"])
    assert due_at > datetime.now(UTC) + timedelta(hours=23), "graded ≥ 3 is due at least a day out"
    assert after["last_reviewed_at"] is not None

    payload = client.get("/api/review/due").json()
    assert payload["due"] < payload["total"]


def test_grade_validation(client, db) -> None:
    card_id = db.execute("SELECT id FROM card_review ORDER BY id LIMIT 1").fetchone()["id"]
    assert post(client, f"/review/{card_id}/grade", {"grade": 9}, htmx=True).status_code == 422
    assert post(client, "/review/999999999/grade", {"grade": 3}, htmx=True).status_code == 404
    assert client.post(f"/review/{card_id}/grade", data={"grade": 3}).status_code == 403, "CSRF is enforced"


def test_daily_cap_setting_stops_the_queue(client, db) -> None:
    previous = get_setting(db, "daily_card_cap", "")
    with transaction(db):
        set_setting(db, "daily_card_cap", "0")
    try:
        response = get(client, "/review/next", htmx=True)
        assert response.status_code == 200
        assert 'data-testid="review-done"' in response.text and 'data-reason="cap"' in response.text
    finally:
        with transaction(db):
            if previous:
                set_setting(db, "daily_card_cap", previous)
            else:
                db.execute("DELETE FROM setting WHERE key = 'daily_card_cap'")
    assert get(client, "/review/next", htmx=True).status_code == 200
