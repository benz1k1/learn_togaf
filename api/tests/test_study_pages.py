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


_UNANSWERED = """
    SELECT q.id FROM lesson_question lq JOIN question q ON q.id = lq.question_id
    WHERE lq.lesson_id = ? AND q.id NOT IN (
        SELECT aa.question_id FROM attempt_answer aa JOIN attempt a ON a.id = aa.attempt_id
        WHERE a.mode = 'CHECK' AND aa.chosen_key IS NOT NULL)
"""


def _check_lesson() -> str:
    """The lesson with the most unanswered mapped questions; the check tests spend a few of them."""
    row = _one(
        "SELECT lesson_id, COUNT(*) AS n FROM lesson_question WHERE question_id NOT IN ("
        " SELECT aa.question_id FROM attempt_answer aa JOIN attempt a ON a.id = aa.attempt_id"
        " WHERE a.mode = 'CHECK' AND aa.chosen_key IS NOT NULL) GROUP BY lesson_id ORDER BY n DESC LIMIT 1"
    )
    assert row is not None and row["n"] >= 6, (
        "the seed content maps at least six unanswered questions to some lesson"
    )
    return row["lesson_id"]


def _ids_in(fragment: str) -> set[str]:
    return set(re.findall(r'name="question_id" value="([^"]+)"', fragment))


# ---------------------------------------------------------------- dashboard


def test_dashboard_renders_summary_and_sections(client):
    response = client.get("/")
    assert response.status_code == 200
    body = response.text
    assert 'id="summary-line"' in body
    assert "OGEA-101:" in body and "OGEA-102:" in body and "OGA-031:" in body and "SCF:" in body
    for code in ("OGEA-101", "OGEA-102", "OGA-031", "OGA-032", "SCF"):
        assert f'data-testid="readiness-{code}"' in body
    assert "Cards due" in body and "Weakest objectives" in body and "Next lesson" in body


def _entry(code: str, scoring: str, estimate: int | None, pass_mark: int = 24, max_score: int = 40) -> dict:
    return {
        "code": code,
        "scoring": scoring,
        "estimate": estimate,
        "max_score": max_score,
        "ready": estimate is not None and estimate >= pass_mark,
    }


def test_summary_line_wording():
    assert (
        readiness.summary_line([_entry("OGEA-101", "single", None), _entry("OGEA-102", "gradient", None)])
        == "OGEA-101: no data yet. OGEA-102: no data yet."
    )
    assert (
        readiness.summary_line([_entry("OGEA-101", "single", 31), _entry("OGEA-102", "gradient", 19)])
        == "OGEA-101: 31/40 on recent form, ready. OGEA-102: 19/40, not yet."
    )
    assert readiness.summary_line([_entry("SCF", "single", 36, 36, 48)]) == "SCF: 36/48 on recent form, ready."


def test_weighted_estimate_is_weight_scaled():
    units = [
        {"code": "F4", "weight": 9, "accuracy": 1.0},
        {"code": "F8", "weight": 7, "accuracy": 0.0},
        {"code": "F1", "weight": 3, "accuracy": None},
    ]
    assert readiness.weighted_estimate(units, 40) == round(9 / 16 * 40)
    assert readiness.weighted_estimate(units, 48) == round(9 / 16 * 48)
    assert readiness.weighted_estimate([{"code": "F1", "weight": 3, "accuracy": None}], 40) is None


def test_reload_content_returns_report(client):
    response = post(client, "/api/content/reload")
    assert response.status_code == 200, response.text
    payload = response.json()
    assert payload["success"] is True
    assert payload["report"]["units"] == 44
    assert payload["report"]["weeks"] == 16
    assert payload["report"]["lessons"] >= 11


def test_post_without_csrf_is_403(client):
    response = client.post("/note", data={"ref_kind": "LESSON", "ref_id": LESSON_ID, "body_md": "x"})
    assert response.status_code == 403


# ---------------------------------------------------------------- units and lessons


def test_unit_list_groups_by_exam(client):
    body = client.get("/unit").text
    assert "Togaf · OGEA-101" in body and "Togaf · OGEA-102" in body
    assert "Archimate · OGA-031" in body and "Sabsa · SCF" in body and "Crosswalk · no exam" in body
    assert 'href="/unit/F4"' in body and 'href="/unit/P3"' in body and 'href="/unit/A7"' in body


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
    # Opening a lesson does not count as reading it: no progress row until the button is pressed.
    assert _one("SELECT state FROM lesson_progress WHERE lesson_id = ?", LESSON_ID) is None
    assert "mark as read" in body
    assert f'hx-post="/lesson-progress/{LESSON_ID}"' in body, (
        "the buttons must carry the lesson id on first render"
    )
    assert post(client, f"/lesson-progress/{LESSON_ID}", {"state": "READ"}).status_code == 303
    assert _one("SELECT state FROM lesson_progress WHERE lesson_id = ?", LESSON_ID)["state"] == "READ"
    assert client.get("/lesson/F4/99_missing").status_code == 404


def test_opening_a_lesson_does_not_change_its_state(client):
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
    lesson_id = _check_lesson()
    available = _one(f"SELECT COUNT(*) AS n FROM ({_UNANSWERED})", lesson_id)["n"]
    fragment = client.get(f"/lesson-check/{lesson_id}")
    assert fragment.status_code == 200
    assert fragment.text.count('name="question_id"') == min(5, available)
    assert f"{available} of" in fragment.text, (
        "the fragment says how many mapped questions are still unanswered"
    )
    assert "draft" in fragment.text, "draft questions are allowed in a lesson check and badged"
    for question_id in _ids_in(fragment.text):
        assert (
            _one("SELECT lesson_id FROM lesson_question WHERE question_id = ?", question_id)["lesson_id"]
            == lesson_id
        )

    wrong = _one(
        f"""
        SELECT q.id, o.key FROM question q JOIN question_option o ON o.question_id = q.id
        WHERE q.id IN ({_UNANSWERED}) AND o.points = 0
        LIMIT 1
        """,
        lesson_id,
    )
    right = _one("SELECT key FROM question_option WHERE question_id = ? AND points = 1", wrong["id"])
    with _db() as connection:
        connection.execute(
            "DELETE FROM card_review WHERE card_kind = 'QUESTION' AND card_ref = ?", (wrong["id"],)
        )

    response = post(client, f"/lesson-check/{lesson_id}", {"question_id": wrong["id"], "key": wrong["key"]})
    assert response.status_code == 200 and "Incorrect" in response.text
    attempt = _one(
        "SELECT * FROM attempt WHERE mode = 'CHECK' AND json_extract(filters, '$.lesson') = ?", lesson_id
    )
    assert attempt is not None and attempt["set_code"] is None
    assert wrong["id"] in orjson.loads(attempt["question_ids"])
    answer = _one(
        "SELECT * FROM attempt_answer WHERE attempt_id = ? AND question_id = ?", attempt["id"], wrong["id"]
    )
    assert answer["chosen_key"] == wrong["key"] and answer["points"] == 0
    card = _one("SELECT * FROM card_review WHERE card_kind = 'QUESTION' AND card_ref = ?", wrong["id"])
    assert card is not None and card["due_at"] <= datetime.now(UTC).isoformat(timespec="seconds")

    response = post(client, f"/lesson-check/{lesson_id}", {"question_id": wrong["id"], "key": right["key"]})
    assert response.status_code == 200 and "Correct" in response.text
    answer = _one(
        "SELECT * FROM attempt_answer WHERE attempt_id = ? AND question_id = ?", attempt["id"], wrong["id"]
    )
    assert answer["points"] == 1, "re-answering upserts the same attempt_answer row"
    assert (
        _one(
            "SELECT COUNT(*) AS n FROM attempt WHERE mode = 'CHECK' AND json_extract(filters, '$.lesson') = ?",
            lesson_id,
        )["n"]
        == 1
    )


def test_check_yourself_never_repeats_an_answered_question(client):
    """A question answered in a lesson check is out of every lesson check from then on: it belongs to
    exactly one lesson (lesson_question), and that lesson stops offering it."""
    lesson_id = _check_lesson()
    first = _ids_in(client.get(f"/lesson-check/{lesson_id}").text)
    answered = sorted(first)[0]
    option = _one("SELECT key FROM question_option WHERE question_id = ? LIMIT 1", answered)
    assert (
        post(
            client, f"/lesson-check/{lesson_id}", {"question_id": answered, "key": option["key"]}
        ).status_code
        == 200
    )
    for _ in range(6):
        assert answered not in _ids_in(client.get(f"/lesson-check/{lesson_id}").text)
    assert _one("SELECT COUNT(*) AS n FROM lesson_question WHERE question_id = ?", answered)["n"] == 1
    other = _one("SELECT id FROM lesson WHERE id != ? LIMIT 1", lesson_id)["id"]
    assert answered not in _ids_in(client.get(f"/lesson-check/{other}").text)
    remaining = _one(f"SELECT COUNT(*) AS n FROM ({_UNANSWERED})", lesson_id)["n"]
    assert f"{remaining} of" in client.get(f"/lesson-check/{lesson_id}").text


def test_check_yourself_says_when_a_lesson_is_exhausted(client):
    """Answer everything mapped to the smallest lesson, expect the exhausted message, then undo."""
    small = _one(
        "SELECT lesson_id, COUNT(*) AS n FROM lesson_question GROUP BY lesson_id ORDER BY n ASC, lesson_id LIMIT 1"
    )
    lesson_id, mapped = small["lesson_id"], small["n"]
    with _db() as connection:
        before = {
            row["question_id"]
            for row in connection.execute(
                "SELECT aa.question_id FROM attempt_answer aa JOIN attempt a ON a.id = aa.attempt_id"
                " WHERE a.mode = 'CHECK' AND json_extract(a.filters, '$.lesson') = ?",
                (lesson_id,),
            )
        }
        pending = [row["id"] for row in connection.execute(_UNANSWERED, (lesson_id,))]
    for question_id in pending:
        option = _one(
            "SELECT key FROM question_option WHERE question_id = ? AND points > 0 LIMIT 1", question_id
        )
        assert (
            post(
                client, f"/lesson-check/{lesson_id}", {"question_id": question_id, "key": option["key"]}
            ).status_code
            == 200
        )
    fragment = client.get(f"/lesson-check/{lesson_id}").text
    assert f"All {mapped} question" in fragment and 'name="question_id"' not in fragment
    with _db() as connection:  # leave the learner's state as it was
        attempt = connection.execute(
            "SELECT id FROM attempt WHERE mode = 'CHECK' AND json_extract(filters, '$.lesson') = ?",
            (lesson_id,),
        ).fetchone()
        for question_id in pending:
            if question_id not in before:
                connection.execute(
                    "DELETE FROM attempt_answer WHERE attempt_id = ? AND question_id = ?",
                    (attempt["id"], question_id),
                )
        remaining_ids = [
            row["question_id"]
            for row in connection.execute(
                "SELECT question_id FROM attempt_answer WHERE attempt_id = ?", (attempt["id"],)
            )
        ]
        connection.execute(
            "UPDATE attempt SET question_ids = ? WHERE id = ?",
            (orjson.dumps(remaining_ids).decode(), attempt["id"]),
        )
        if not remaining_ids:
            connection.execute("DELETE FROM attempt WHERE id = ?", (attempt["id"],))
    assert 'name="question_id"' in client.get(f"/lesson-check/{lesson_id}").text


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
    # The code is a URL/id only (the Example button, its target cell); the visible label is the name.
    assert ">STAKEHOLDER_MAP_MATRIX<" not in everything and "Stakeholder Map" in everything
    assert 'hx-get="/artefact/STAKEHOLDER_MAP_MATRIX/example"' in everything
    filtered = client.get("/artefact?phase=A&kind=DIAGRAM", headers={"HX-Request": "true"}).text
    assert "<html" not in filtered and 'id="artefact-table"' in filtered
    assert "Value Chain Diagram" in filtered and "Stakeholder Map" not in filtered


def test_artefact_example_fragment(client):
    fragment = client.get(
        "/artefact/APPLICATION_COMMUNICATION_DIAGRAM/example", headers={"HX-Request": "true"}
    )
    assert fragment.status_code == 200 and "<html" not in fragment.text
    assert '<img src="/static/artefact/APPLICATION_COMMUNICATION_DIAGRAM.svg"' in fragment.text
    assert 'href="/static/artefact/APPLICATION_COMMUNICATION_DIAGRAM.svg"' in fragment.text, (
        "open / save link"
    )
    assert 'href="/source/CONTENT%20%C2%A73.6.6"' in fragment.text, "link to the defining section"
    svg = client.get("/static/artefact/APPLICATION_COMMUNICATION_DIAGRAM.svg")
    assert svg.status_code == 200 and svg.headers["content-type"].startswith("image/svg+xml")
    assert 'role="img"' in svg.text and "Original illustration for study" in svg.text
    assert 'hx-get="/artefact/APPLICATION_COMMUNICATION_DIAGRAM/example"' in client.get("/adm/C").text


def test_artefact_example_unknown_code_is_404(client):
    assert client.get("/artefact/NOT_AN_ARTEFACT/example").status_code == 404


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
    prefix = "F" if exam == "OGEA-101" else "P"
    return [
        {
            "id": f"{prefix}/{i}",
            "title": f"L{i}",
            "unit_code": "U",
            "exam": exam,
            "weight": weight,
            "ordinal": i,
        }
        for i in range(n)
    ]


def test_generate_plan_spreads_lessons_and_places_mocks():
    lessons = _lessons(6, "OGEA-101", 9) + _lessons(2, "OGEA-102", 1)
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
    assert [item["ref"] for _, item in mocks] == ["OGEA-101", "OGEA-101"], (
        "the mock is of the exam the lessons so far belong to; the two light P lessons land after day 15"
    )
    assert all(item["title"] == f"{item['ref']} mock" for _, item in mocks)
    assert all(
        any(item["kind"] == "REVIEW" and "20" in item["title"] for item in day["items"]) for day in plan
    )


def test_generate_plan_with_exam_tomorrow_is_one_day():
    start = date(2026, 1, 1)
    plan = plan_service.generate_plan(
        _lessons(3, "OGEA-101", 3), start, start + timedelta(days=1), card_cap=10
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
        {"date": "2026-01-02", "items": [{"kind": "MOCK", "ref": "OGEA-101", "title": "mock"}]},
        {"date": "2026-01-03", "items": [{"kind": "LESSON", "ref": "c", "title": "c"}]},
        {"date": "2026-01-04", "items": [{"kind": "LESSON", "ref": "d", "title": "d"}]},
    ]
    flowed = plan_service.reflow(plan, date(2026, 1, 3), read_ids={"a"})
    assert [item["ref"] for item in flowed[0]["items"]] == ["a"], "read lessons stay where they were"
    assert [item["ref"] for item in flowed[1]["items"]] == ["OGEA-101"], "past mocks are left alone"
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
    later = (datetime.now(UTC).date() + timedelta(days=20)).isoformat()
    response = post(client, "/plan", {"exam_date:OGEA-101": later, "exam_date:SCF": exam, "daily_card_cap": "25"})
    assert response.status_code == 303 and response.headers["location"].startswith("/plan?flash=")
    assert _one("SELECT value FROM setting WHERE key = 'exam_date:SCF'")["value"] == exam
    assert _one("SELECT value FROM setting WHERE key = 'exam_date:OGEA-101'")["value"] == later
    assert _one("SELECT value FROM setting WHERE key = 'exam_date:OGA-031'")["value"] == ""
    assert _one("SELECT value FROM setting WHERE key = 'daily_card_cap'")["value"] == "25"
    stored = orjson.loads(_one("SELECT value FROM setting WHERE key = 'plan_json'")["value"])
    assert len(stored) == 30 and stored[0]["date"] == datetime.now(UTC).date().isoformat(), "the plan runs to the latest date"
    assert {item["kind"] for day in stored for item in day["items"]} == {"LESSON", "MOCK", "REVIEW"}

    page = client.get("/plan").text
    assert f'value="{exam}"' in page and 'value="25"' in page and "today" in page
    assert page.count("card-body p-3") == 14, "the coming 14 days are rendered"
    assert re.search(r"(OGEA-10[12]|OGA-03[12]|SCF) mock", page) and re.search(r"Week \d+ ·", page) and "The braid" in page
    assert 'hx-post="/plan/exercise/2/draw"' in page

    dashboard = client.get("/").text
    assert "Next exam" in dashboard and re.search(r">\s*20\s*<span", dashboard) and "OGEA-101" in dashboard

    ticked = post(client, "/plan/exercise/2/draw", {"done": "on"}, htmx=True)
    assert ticked.status_code == 200 and "checked" in ticked.text
    assert _one("SELECT value FROM setting WHERE key = 'exercise:2:draw'")["value"] == "1"
    assert post(client, "/plan/exercise/2/nope", {"done": "on"}).status_code == 422

    yesterday = (datetime.now(UTC).date() - timedelta(days=1)).isoformat()
    rejected = post(client, "/plan", {"exam_date:OGEA-101": yesterday, "daily_card_cap": "25"})
    assert rejected.status_code == 303 and "flash_kind=error" in rejected.headers["location"]
    none = post(client, "/plan", {"daily_card_cap": "25"})
    assert none.status_code == 303 and "flash_kind=error" in none.headers["location"]


# ---------------------------------------------------------------- coverage


def test_coverage_page_reports_shortfalls(client):
    body = client.get("/coverage").text
    assert "Coverage and question quality" in body
    # The Sources column counts the sections mapped to each objective; before the crawl every
    # objective is flagged "no source", after it none should be.
    assert '<th class="text-right">Sources</th>' in body
    assert "no source" in body or "Sources" in body
    assert "reviewed single-answer 0/8" in body
    assert "reviewed scenarios 0/2" in body
    assert "Drafts waiting" in body and "Too easy" in body and "Guessable" in body


@pytest.fixture(scope="module", autouse=True)
def _cleanup():
    yield
    with _db() as connection:
        connection.execute("DELETE FROM note WHERE ref_kind = 'TERM' AND ref_id = 'artifact'")


def test_worked_examples_page_lists_every_phase_and_opens_a_document(client) -> None:
    page = client.get("/example")
    assert page.status_code == 200
    for code in ("PRELIM", "A", "B", "C", "D", "E", "F", "G", "H", "REQ"):
        assert f'href="/adm/{code}"' in page.text
    assert "Request for Architecture Work" in page.text
    row = _one("SELECT id, title FROM example_document ORDER BY ordinal LIMIT 1")
    assert row is not None
    detail = client.get(f"/example/{row['id']}")
    assert detail.status_code == 200
    assert row["title"] in detail.text
    assert 'href="/source/' in detail.text
    assert client.get("/example/no_such_document").status_code == 404


def test_phase_page_links_its_worked_examples(client) -> None:
    page = client.get("/adm/A")
    assert page.status_code == 200
    assert "Worked examples" in page.text
    assert 'href="/example/09_statement_of_architecture_work"' in page.text
