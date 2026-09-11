"""Dashboard, lessons, ADM explorer, glossary, plan, coverage, notes and export (learn_togaf.md §4.1–4.4, §4.8–4.10)."""

import re
import sqlite3
from datetime import UTC, date, datetime, timedelta

import orjson
import pytest
from tests.conftest import post

from learn_togaf.config import DB_PATH
from learn_togaf.service import plan as plan_service
from learn_togaf.service import readiness

LESSON_ID = "F4/01_preliminary_and_phase_a"


def _db() -> sqlite3.Connection:
    connection = sqlite3.connect(DB_PATH, timeout=30)
    connection.row_factory = sqlite3.Row
    return connection


def _one(sql: str, *params):
    with _db() as connection:
        return connection.execute(sql, params).fetchone()


# ---------------------------------------------------------------- dashboard


def test_dashboard_renders_summary_and_sections(client):
    response = client.get("/")
    assert response.status_code == 200
    body = response.text
    assert 'id="summary-line"' in body
    assert "Foundation:" in body and "Practitioner:" in body
    assert "Cards due" in body and "Weakest objectives" in body and "Next lesson" in body


def test_summary_line_wording():
    assert readiness.summary_line(None, None) == "Foundation: no data yet. Practitioner: no data yet."
    assert (
        readiness.summary_line(31, 19)
        == "Foundation: 31/40 on recent form, ready. Practitioner: 19/40, not yet."
    )
    assert readiness.summary_line(24, 24).count("ready") == 2


def test_foundation_estimate_is_weight_scaled():
    units = [
        {"code": "F4", "weight": 9, "accuracy": 1.0},
        {"code": "F8", "weight": 7, "accuracy": 0.0},
        {"code": "F1", "weight": 3, "accuracy": None},
    ]
    assert readiness.foundation_estimate(units) == round(9 / 16 * 40)
    assert readiness.foundation_estimate([{"code": "F1", "weight": 3, "accuracy": None}]) is None


def test_reload_content_returns_report(client):
    response = post(client, "/api/content/reload")
    assert response.status_code == 200, response.text
    payload = response.json()
    assert payload["success"] is True
    assert payload["report"]["units"] == 25
    assert payload["report"]["lessons"] >= 11


def test_post_without_csrf_is_403(client):
    response = client.post("/note", data={"ref_kind": "LESSON", "ref_id": LESSON_ID, "body_md": "x"})
    assert response.status_code == 403


# ---------------------------------------------------------------- units and lessons


def test_unit_list_groups_by_exam(client):
    body = client.get("/unit").text
    assert "Foundation" in body and "Practitioner" in body
    assert 'href="/unit/F4"' in body and 'href="/unit/P3"' in body


def test_unit_page_lists_lessons_and_objectives(client):
    body = client.get("/unit/F4").text
    assert f'href="/lesson/{LESSON_ID}"' in body
    assert "4.3" in body
    assert client.get("/unit/NOPE").status_code == 404


def test_lesson_page_renders_markdown_links_and_marks_read(client):
    with _db() as connection:
        connection.execute("DELETE FROM lesson_progress WHERE lesson_id = ?", (LESSON_ID,))
    response = client.get(f"/lesson/{LESSON_ID}")
    assert response.status_code == 200
    body = response.text
    assert '<div class="prose-lesson">' in body
    assert 'href="/glossary/' in body, "glossary terms in the text should be auto-linked"
    assert 'href="/source/' in body, "refs should link to the source pages"
    assert 'hx-get="/lesson-check/' in body
    assert 'hx-post="/note"' in body
    row = _one("SELECT state FROM lesson_progress WHERE lesson_id = ?", LESSON_ID)
    assert row is not None and row["state"] == "READ"
    assert client.get("/lesson/F4/99_missing").status_code == 404


def test_auto_read_does_not_downgrade(client):
    assert post(client, f"/lesson-progress/{LESSON_ID}", {"state": "MASTERED"}).status_code == 303
    client.get(f"/lesson/{LESSON_ID}")
    assert _one("SELECT state FROM lesson_progress WHERE lesson_id = ?", LESSON_ID)["state"] == "MASTERED"
    fragment = post(
        client, f"/lesson-progress/{LESSON_ID}", {"state": "CHECKED"}, headers={"HX-Request": "true"}
    )
    assert fragment.status_code == 200 and 'id="lesson-progress"' in fragment.text
    assert _one("SELECT state FROM lesson_progress WHERE lesson_id = ?", LESSON_ID)["state"] == "CHECKED"
    assert post(client, f"/lesson-progress/{LESSON_ID}", {"state": "BOGUS"}).status_code == 422


def test_check_yourself_serves_questions_and_records_answers(client):
    available = _one(
        "SELECT COUNT(*) AS n FROM question WHERE objective_code IN (SELECT objective_code FROM lesson_objective WHERE lesson_id = ?)",
        LESSON_ID,
    )["n"]
    assert available > 0, "the F4 lesson has questions tagged to its objectives in the seed content"
    fragment = client.get(f"/lesson-check/{LESSON_ID}")
    assert fragment.status_code == 200
    assert fragment.text.count('name="question_id"') == min(5, available)
    assert "draft" in fragment.text, "draft questions are allowed in a lesson check and badged"

    wrong = _one(
        """
        SELECT q.id, o.key FROM question q JOIN question_option o ON o.question_id = q.id
        WHERE q.objective_code IN (SELECT objective_code FROM lesson_objective WHERE lesson_id = ?) AND o.points = 0
        LIMIT 1
        """,
        LESSON_ID,
    )
    right = _one("SELECT key FROM question_option WHERE question_id = ? AND points = 1", wrong["id"])
    with _db() as connection:
        connection.execute(
            "DELETE FROM card_review WHERE card_kind = 'QUESTION' AND card_ref = ?", (wrong["id"],)
        )

    response = post(client, f"/lesson-check/{LESSON_ID}", {"question_id": wrong["id"], "key": wrong["key"]})
    assert response.status_code == 200 and "Incorrect" in response.text
    attempt = _one(
        "SELECT * FROM attempt WHERE mode = 'CHECK' AND json_extract(filters, '$.lesson') = ?", LESSON_ID
    )
    assert attempt is not None and attempt["set_code"] is None
    assert wrong["id"] in orjson.loads(attempt["question_ids"])
    answer = _one(
        "SELECT * FROM attempt_answer WHERE attempt_id = ? AND question_id = ?", attempt["id"], wrong["id"]
    )
    assert answer["chosen_key"] == wrong["key"] and answer["points"] == 0
    card = _one("SELECT * FROM card_review WHERE card_kind = 'QUESTION' AND card_ref = ?", wrong["id"])
    assert card is not None and card["due_at"] <= datetime.now(UTC).isoformat(timespec="seconds")

    response = post(client, f"/lesson-check/{LESSON_ID}", {"question_id": wrong["id"], "key": right["key"]})
    assert response.status_code == 200 and "Correct" in response.text
    answer = _one(
        "SELECT * FROM attempt_answer WHERE attempt_id = ? AND question_id = ?", attempt["id"], wrong["id"]
    )
    assert answer["points"] == 1, "re-answering upserts the same attempt_answer row"
    assert (
        _one(
            "SELECT COUNT(*) AS n FROM attempt WHERE mode = 'CHECK' AND json_extract(filters, '$.lesson') = ?",
            LESSON_ID,
        )["n"]
        == 1
    )


# ---------------------------------------------------------------- ADM explorer


def test_adm_page_has_clickable_cycle(client):
    body = client.get("/adm").text
    assert "<svg" in body
    for code in ("PRELIM", "A", "B", "C", "D", "E", "F", "G", "H", "REQ"):
        assert f'hx-get="/adm-panel/{code}"' in body
        assert f'href="/adm/{code}"' in body
    assert 'href="/adm/technique/GAP_ANALYSIS"' in body


def test_phase_panel_and_page(client):
    panel = client.get("/adm-panel/A")
    assert panel.status_code == 200 and "<html" not in panel.text
    assert "Inputs" in panel.text and "Outputs" in panel.text and 'href="/adm/A"' in panel.text

    page = client.get("/adm/A").text
    assert 'href="/adm/PRELIM"' in page and 'href="/adm/B"' in page, (
        "previous and next phase in the hand-off strip"
    )
    assert 'href="/practice?phase=A&kind=io"' in page
    assert 'href="/artefact?phase=A' in page
    assert "Statement of Architecture Work" in page
    assert 'hx-post="/note"' in page
    assert 'href="/adm/A"' in client.get("/adm/H").text, "H hands off to A around the cycle"
    assert client.get("/adm/REQ").status_code == 200
    assert client.get("/adm/ZZ").status_code == 404


def test_technique_and_artefact_pages(client):
    technique = client.get("/adm/technique/GAP_ANALYSIS")
    assert technique.status_code == 200 and "Gap Analysis" in technique.text
    assert client.get("/adm/technique/NOPE").status_code == 404

    everything = client.get("/artefact").text
    assert "STAKEHOLDER_MAP_MATRIX" not in everything and "Stakeholder Map" in everything
    filtered = client.get("/artefact?phase=A&kind=DIAGRAM", headers={"HX-Request": "true"}).text
    assert "<html" not in filtered and 'id="artefact-table"' in filtered
    assert "Value Chain Diagram" in filtered and "Stakeholder Map" not in filtered


# ---------------------------------------------------------------- glossary


def test_glossary_search_and_fragment(client):
    page = client.get("/glossary?q=artifact")
    assert page.status_code == 200 and 'href="/glossary/artifact"' in page.text
    fragment = client.get("/glossary?q=artifact", headers={"HX-Request": "true"})
    assert "<html" not in fragment.text and 'id="term-list"' in fragment.text
    assert "INTRO §3" in fragment.text
    assert 'href="/glossary/deliverable"' in fragment.text, "confusable-with links"
    assert "No term matches" in client.get("/glossary?q=zzzzqqq", headers={"HX-Request": "true"}).text


def test_term_page_shows_confusables_side_by_side(client):
    body = client.get("/glossary/artifact").text
    assert "side by side" in body
    assert 'href="/glossary/deliverable"' in body and 'href="/glossary/building_block"' in body
    assert 'name="ref_kind" value="TERM"' in body
    assert client.get("/glossary/not_a_term").status_code == 404


# ---------------------------------------------------------------- notes and export


def test_note_upserts_and_returns_fragment(client):
    first = post(client, "/note", {"ref_kind": "TERM", "ref_id": "artifact", "body_md": "first **draft**"})
    assert first.status_code == 200 and "<html" not in first.text and "saved" in first.text
    second = post(client, "/note", {"ref_kind": "TERM", "ref_id": "artifact", "body_md": "second"})
    assert second.status_code == 200 and "<strong>" not in second.text
    assert _one("SELECT COUNT(*) AS n FROM note WHERE ref_kind = 'TERM' AND ref_id = 'artifact'")["n"] == 1
    assert (
        _one("SELECT body_md FROM note WHERE ref_kind = 'TERM' AND ref_id = 'artifact'")["body_md"]
        == "second"
    )
    assert "second" in client.get("/glossary/artifact").text


def test_export_page_and_state_json(client):
    page = client.get("/export")
    assert (
        page.status_code == 200 and 'href="/export/state.json"' in page.text and 'href="/import"' in page.text
    )
    response = client.get("/export/state.json")
    assert response.status_code == 200
    assert response.headers["content-type"].startswith("application/json")
    assert "attachment" in response.headers["content-disposition"]
    question = _one(
        "SELECT q.id, o.key FROM question q JOIN question_option o ON o.question_id = q.id"
        " WHERE q.objective_code IN (SELECT objective_code FROM lesson_objective WHERE lesson_id = ?) LIMIT 1",
        LESSON_ID,
    )
    assert (
        post(
            client, f"/lesson-check/{LESSON_ID}", {"question_id": question["id"], "key": question["key"]}
        ).status_code
        == 200
    )
    response = client.get("/export/state.json")
    state = response.json()
    assert state["version"] == 1 and state["exported_at"]
    for key in ("attempts", "card_reviews", "notes", "lesson_progress", "settings", "study_sessions"):
        assert isinstance(state[key], list), key
    check = next(
        a for a in state["attempts"] if a["mode"] == "CHECK" and a["filters"].get("lesson") == LESSON_ID
    )
    assert check["answers"], "attempts carry their answers"
    assert any(n["ref_kind"] == "TERM" and n["ref_id"] == "artifact" for n in state["notes"])


# ---------------------------------------------------------------- plan


def _lessons(n: int, exam: str, weight: int) -> list[dict]:
    return [
        {
            "id": f"{exam[0]}/{i}",
            "title": f"L{i}",
            "unit_code": "U",
            "exam": exam,
            "weight": weight,
            "ordinal": i,
        }
        for i in range(n)
    ]


def test_generate_plan_spreads_lessons_and_places_mocks():
    lessons = _lessons(6, "FOUNDATION", 9) + _lessons(2, "PRACTITIONER", 1)
    start = date(2026, 1, 1)
    plan = plan_service.generate_plan(lessons, start, start + timedelta(days=16), card_cap=20)
    assert len(plan) == 16
    assert plan[0]["date"] == "2026-01-01" and plan[-1]["date"] == "2026-01-16"
    scheduled = [item["ref"] for day in plan for item in day["items"] if item["kind"] == "LESSON"]
    assert scheduled == [lesson["id"] for lesson in lessons], "every lesson once, in plan order"
    foundation_days = {day["date"] for day in plan for item in day["items"] if item["ref"].startswith("F/")}
    practitioner_days = {day["date"] for day in plan for item in day["items"] if item["ref"].startswith("P/")}
    assert max(foundation_days) < min(practitioner_days)
    assert len(foundation_days) > len(practitioner_days), "heavier units take more of the days"
    mocks = [(day["date"], item) for day in plan for item in day["items"] if item["kind"] == "MOCK"]
    assert [d for d, _ in mocks] == ["2026-01-08", "2026-01-15"]
    assert all(
        any(item["kind"] == "REVIEW" and "20" in item["title"] for item in day["items"]) for day in plan
    )


def test_generate_plan_with_exam_tomorrow_is_one_day():
    start = date(2026, 1, 1)
    plan = plan_service.generate_plan(
        _lessons(3, "FOUNDATION", 3), start, start + timedelta(days=1), card_cap=10
    )
    assert len(plan) == 1 and sum(1 for item in plan[0]["items"] if item["kind"] == "LESSON") == 3


def test_reflow_moves_unread_past_lessons_forward():
    plan = [
        {
            "date": "2026-01-01",
            "items": [
                {"kind": "LESSON", "ref": "a", "title": "a"},
                {"kind": "LESSON", "ref": "b", "title": "b"},
            ],
        },
        {"date": "2026-01-02", "items": [{"kind": "MOCK", "ref": "FOUNDATION", "title": "mock"}]},
        {"date": "2026-01-03", "items": [{"kind": "LESSON", "ref": "c", "title": "c"}]},
        {"date": "2026-01-04", "items": [{"kind": "LESSON", "ref": "d", "title": "d"}]},
    ]
    flowed = plan_service.reflow(plan, date(2026, 1, 3), read_ids={"a"})
    assert [item["ref"] for item in flowed[0]["items"]] == ["a"], "read lessons stay where they were"
    assert [item["ref"] for item in flowed[1]["items"]] == ["FOUNDATION"], "past mocks are left alone"
    assert [item["ref"] for item in flowed[2]["items"]] == ["b", "c"], (
        "the unread one lands at the front of today"
    )
    assert [item["ref"] for item in flowed[3]["items"]] == ["d"]
    assert plan_service.reflow(plan, date(2025, 12, 1), set()) == plan
    past_everything = plan_service.reflow(plan, date(2026, 2, 1), set())
    assert past_everything[-1]["date"] == "2026-02-01" and len(past_everything[-1]["items"]) == 4


def test_upcoming_window():
    plan = [{"date": (date(2026, 1, 1) + timedelta(days=i)).isoformat(), "items": []} for i in range(30)]
    window = plan_service.upcoming(plan, date(2026, 1, 10))
    assert len(window) == 14 and window[0]["date"] == "2026-01-10" and window[-1]["date"] == "2026-01-23"


def test_plan_page_saves_settings_and_generates(client):
    exam = (datetime.now(UTC).date() + timedelta(days=30)).isoformat()
    response = post(client, "/plan", {"exam_date": exam, "daily_card_cap": "25"})
    assert response.status_code == 303 and response.headers["location"].startswith("/plan?flash=")
    assert _one("SELECT value FROM setting WHERE key = 'exam_date'")["value"] == exam
    assert _one("SELECT value FROM setting WHERE key = 'daily_card_cap'")["value"] == "25"
    stored = orjson.loads(_one("SELECT value FROM setting WHERE key = 'plan_json'")["value"])
    assert len(stored) == 30 and stored[0]["date"] == datetime.now(UTC).date().isoformat()
    assert {item["kind"] for day in stored for item in day["items"]} == {"LESSON", "MOCK", "REVIEW"}

    page = client.get("/plan").text
    assert f'value="{exam}"' in page and 'value="25"' in page and "today" in page
    assert page.count("card-body p-3") == 14, "the coming 14 days are rendered"
    assert "Foundation mock" in page

    dashboard = client.get("/").text
    assert "Days to exam" in dashboard and re.search(r">\s*30\s*<", dashboard)

    yesterday = (datetime.now(UTC).date() - timedelta(days=1)).isoformat()
    rejected = post(client, "/plan", {"exam_date": yesterday, "daily_card_cap": "25"})
    assert rejected.status_code == 303 and "flash_kind=error" in rejected.headers["location"]


# ---------------------------------------------------------------- coverage


def test_coverage_page_reports_shortfalls(client):
    body = client.get("/coverage").text
    assert "Coverage and question quality" in body
    assert "no source" in body, "the source store is not indexed, so every objective lacks a mapped section"
    assert "reviewed Foundation 0/8" in body
    assert "reviewed Practitioner 0/2" in body
    assert "Drafts waiting" in body and "Too easy" in body and "Guessable" in body


@pytest.fixture(scope="module", autouse=True)
def _cleanup():
    yield
    with _db() as connection:
        connection.execute("DELETE FROM note WHERE ref_kind = 'TERM' AND ref_id = 'artifact'")
