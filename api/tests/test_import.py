"""
Import wizard (learn_togaf.md §4.7, §8): each format round-trips through preview + confirm
against the live server; a duplicate of an existing question is reported, not inserted; a broken
row blocks the set unless "import what validates" is ticked; remove deletes the set and its
file; the learner-state re-import (§4.10) merges and reports counts.

Every set this suite creates is removed again through ``POST /import/remove/<code>``.
"""

import re
import sqlite3
from pathlib import Path
from urllib.parse import parse_qs, urlparse

import httpx
import orjson
import pytest
from conftest import post

from learn_togaf.config import CONTENT_DIR, DB_PATH

FIXTURES = Path(__file__).with_name("fixtures")
IMPORTED_DIR = CONTENT_DIR / "questions" / "imported"
TOKEN_RE = re.compile(r'name="token" value="([^"]+)"')

FORMATS = [
    ("import_foundation.yaml", "OGEA-101", "TEST_IMPORT_YAML", 2),
    ("import_foundation.csv", "OGEA-101", "TEST_IMPORT_CSV", 2),
    ("import_foundation.json", "OGEA-101", "TEST_IMPORT_JSON", 1),
    ("import_foundation.md", "OGEA-101", "TEST_IMPORT_MD", 2),
    ("import_practitioner.yaml", "OGEA-102", "TEST_IMPORT_P", 1),
]
ALL_CODES = [code for _, _, code, _ in FORMATS] + ["TEST_IMPORT_BROKEN"]


def _remove(client: httpx.Client, code: str) -> None:
    post(client, f"/import/remove/{code}")


@pytest.fixture(autouse=True)
def _clean_sets(client: httpx.Client):
    for code in ALL_CODES:
        _remove(client, code)
    yield
    for code in ALL_CODES:
        _remove(client, code)


def _preview(
    client: httpx.Client, file_name: str, exam: str, set_code: str, **fields: str
) -> tuple[httpx.Response, str]:
    payload = (FIXTURES / file_name).read_bytes()
    response = post(
        client,
        "/import/preview",
        {"exam": exam, "set_code": set_code, "name": f"Test {set_code}", **fields},
        files={"file": (file_name, payload, "application/octet-stream")},
    )
    if response.status_code != 200:
        pytest.fail(f"preview of {file_name} returned {response.status_code}: {response.text[:300]}")
    match = TOKEN_RE.search(response.text)
    if not match:
        pytest.fail(f"preview of {file_name} rendered no confirm token")
    return response, match.group(1)


def _flash(response: httpx.Response) -> str:
    if response.status_code != 303:
        pytest.fail(f"expected a 303 redirect, got {response.status_code}: {response.text[:300]}")
    return parse_qs(urlparse(response.headers["location"]).query)["flash"][0]


def _listed(client: httpx.Client, code: str) -> bool:
    response = client.get("/import")
    assert response.status_code == 200
    return f"/import/remove/{code}" in response.text


def test_import_page_renders(client: httpx.Client):
    response = client.get("/import")
    assert response.status_code == 200
    assert 'action="/import/preview"' in response.text
    assert 'action="/import/state"' in response.text


@pytest.mark.parametrize(("file_name", "exam", "set_code", "count"), FORMATS)
def test_format_round_trips(client: httpx.Client, file_name: str, exam: str, set_code: str, count: int):
    page, token = _preview(client, file_name, exam, set_code)
    assert f"{count} valid" in page.text
    assert "0 invalid" in page.text
    assert not _listed(client, set_code), "nothing lands before confirm"
    assert not (IMPORTED_DIR / f"{set_code}.yaml").exists()

    flash = _flash(post(client, "/import/confirm", {"token": token}))
    assert f"Imported set {set_code}: {count} question(s) added" in flash
    assert _listed(client, set_code)
    written = IMPORTED_DIR / f"{set_code}.yaml"
    assert written.is_file(), "the set is written back in the native shape for --load-content"
    text = written.read_text(encoding="utf-8")
    assert f"code: {set_code}" in text and "kind: IMPORTED" in text and "source: imported" in text
    assert f"{set_code}-001" in text or "TEST_IMPORT_P-001" in text

    # a second confirm on the same token must not double-insert: the token was consumed
    again = post(client, "/import/confirm", {"token": token})
    assert again.status_code == 422


def test_csv_row_without_unit_is_mapped_and_flagged(client: httpx.Client):
    page, token = _preview(client, "import_foundation.csv", "OGEA-101", "TEST_IMPORT_CSV")
    assert "1 unit guessed" in page.text
    assert 'name="unit_map:"' in page.text, "the no-unit group gets a mapping select"
    flash = _flash(post(client, "/import/confirm", {"token": token}))
    assert "1 unit mapping(s) unverified" in flash
    text = (IMPORTED_DIR / "TEST_IMPORT_CSV.yaml").read_text(encoding="utf-8")
    assert "unit-unverified" in text


def test_unit_mapping_override_confirms_unit(client: httpx.Client):
    _, token = _preview(client, "import_foundation.csv", "OGEA-101", "TEST_IMPORT_CSV")
    flash = _flash(post(client, "/import/confirm", {"token": token, "unit_map:": "F3"}))
    assert "unverified" not in flash
    text = (IMPORTED_DIR / "TEST_IMPORT_CSV.yaml").read_text(encoding="utf-8")
    assert "unit: F3" in text


def test_duplicate_is_reported_not_inserted(client: httpx.Client):
    page, token = _preview(client, "import_broken.csv", "OGEA-101", "TEST_IMPORT_BROKEN")
    assert "1 duplicate" in page.text
    assert "<code>F4-002</code>" in page.text, "the duplicate names the question it duplicates"
    flash = _flash(post(client, "/import/confirm", {"token": token, "import_partial": "on"}))
    assert "1 question(s) added, 1 duplicate(s) and 1 invalid row(s) skipped" in flash
    text = (IMPORTED_DIR / "TEST_IMPORT_BROKEN.yaml").read_text(encoding="utf-8")
    assert "output of Phase A, Architecture Vision" not in text


def test_broken_row_blocks_unless_partial(client: httpx.Client):
    page, token = _preview(client, "import_broken.csv", "OGEA-101", "TEST_IMPORT_BROKEN")
    assert "1 invalid" in page.text
    assert "explanation" in page.text.lower()
    blocked = post(client, "/import/confirm", {"token": token})
    assert blocked.status_code == 422
    assert "import what validates" in blocked.text
    assert not _listed(client, "TEST_IMPORT_BROKEN")
    assert not (IMPORTED_DIR / "TEST_IMPORT_BROKEN.yaml").exists()

    flash = _flash(post(client, "/import/confirm", {"token": token, "import_partial": "on"}))
    assert "1 invalid row(s) skipped" in flash
    assert _listed(client, "TEST_IMPORT_BROKEN")


def test_existing_set_code_is_refused(client: httpx.Client):
    _, token = _preview(client, "import_foundation.json", "OGEA-101", "TEST_IMPORT_JSON")
    _flash(post(client, "/import/confirm", {"token": token}))
    page, token = _preview(client, "import_foundation.json", "OGEA-101", "TEST_IMPORT_JSON")
    assert "already exists" in page.text
    assert post(client, "/import/confirm", {"token": token}).status_code == 422


def test_remove_deletes_set_and_file(client: httpx.Client):
    _, token = _preview(client, "import_foundation.md", "OGEA-101", "TEST_IMPORT_MD")
    _flash(post(client, "/import/confirm", {"token": token}))
    assert _listed(client, "TEST_IMPORT_MD")
    flash = _flash(post(client, "/import/remove/TEST_IMPORT_MD"))
    assert "Removed set TEST_IMPORT_MD" in flash
    assert not _listed(client, "TEST_IMPORT_MD")
    assert not (IMPORTED_DIR / "TEST_IMPORT_MD.yaml").exists()
    assert post(client, "/import/remove/TEST_IMPORT_MD").status_code == 404


def test_exam_mismatch_is_refused(client: httpx.Client):
    response = post(
        client,
        "/import/preview",
        {"exam": "OGEA-102", "set_code": "TEST_IMPORT_YAML"},
        files={"file": ("import_foundation.yaml", (FIXTURES / "import_foundation.yaml").read_bytes())},
    )
    assert response.status_code == 422
    assert "says exam OGEA-101" in response.text


def test_post_without_csrf_is_refused(client: httpx.Client):
    response = client.post("/import/confirm", data={"token": "x"})
    assert response.status_code == 403


# ---------------------------------------------------------------- learner state (§4.10)
_STATE_MARK = "test_import_state"


def _db() -> sqlite3.Connection:
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


@pytest.fixture
def _clean_state():
    def wipe() -> None:
        with _db() as connection:
            connection.execute("DELETE FROM attempt WHERE filters LIKE ?", (f"%{_STATE_MARK}%",))
            connection.execute("DELETE FROM note WHERE ref_id = ?", (_STATE_MARK,))
            connection.execute("DELETE FROM card_review WHERE card_ref = ?", (_STATE_MARK,))
            connection.execute("DELETE FROM lesson_progress WHERE lesson_id = ?", (_STATE_MARK,))
            connection.execute("DELETE FROM setting WHERE key = ?", (_STATE_MARK,))
            connection.execute(
                "DELETE FROM study_session WHERE started_at = ?", ("2001-01-01T00:00:00+00:00",)
            )

    wipe()
    yield
    wipe()


def _state(note_body: str, note_updated: str) -> dict:
    return {
        "version": 1,
        "exported_at": "2026-09-10T00:00:00+00:00",
        "attempts": [
            {
                "id": 12345,
                "exam": "OGEA-101",
                "mode": "DRILL",
                "set_code": None,
                "seed": 7,
                "question_ids": ["F1-001"],
                "started_at": "2001-01-01T00:00:00+00:00",
                "finished_at": "2001-01-01T00:05:00+00:00",
                "time_limit_s": None,
                "score": 1,
                "max_score": 1,
                "passed": 1,
                "filters": {"marker": _STATE_MARK},
                "answers": [
                    {
                        "attempt_id": 12345,
                        "question_id": "F1-001",
                        "chosen_key": "A",
                        "points": 1,
                        "answered_at": "2001-01-01T00:01:00+00:00",
                        "flagged": 0,
                        "seconds": 9,
                        "changed_from_correct": 0,
                    }
                ],
            }
        ],
        "card_reviews": [
            {
                "id": 1,
                "card_kind": "TERM",
                "card_ref": _STATE_MARK,
                "due_at": "2001-01-02T00:00:00+00:00",
                "interval_days": 1,
                "ease": 2.5,
                "reps": 1,
                "lapses": 0,
                "last_grade": 4,
                "last_reviewed_at": note_updated,
            }
        ],
        "notes": [
            {
                "id": 1,
                "ref_kind": "LESSON",
                "ref_id": _STATE_MARK,
                "body_md": note_body,
                "updated_at": note_updated,
            }
        ],
        "lesson_progress": [{"lesson_id": _STATE_MARK, "state": "READ", "updated_at": note_updated}],
        "settings": {_STATE_MARK: note_body},
        "study_sessions": [
            {
                "id": 1,
                "started_at": "2001-01-01T00:00:00+00:00",
                "ended_at": None,
                "lessons_read": 1,
                "cards_reviewed": 0,
                "questions_answered": 1,
            }
        ],
    }


def _import_state(client: httpx.Client, payload: dict) -> httpx.Response:
    return post(
        client, "/import/state", files={"file": ("state.json", orjson.dumps(payload), "application/json")}
    )


@pytest.mark.usefixtures("_clean_state")
def test_state_import_merges_and_reports(client: httpx.Client):
    flash = _flash(_import_state(client, _state("newer", "2001-01-05T00:00:00+00:00")))
    assert (
        "1 attempts (1 answers), 1 card reviews, 1 notes, 1 lesson progress rows, 1 settings, 1 study sessions"
        in flash
    )

    with _db() as connection:
        attempt = connection.execute(
            "SELECT id FROM attempt WHERE filters LIKE ?", (f"%{_STATE_MARK}%",)
        ).fetchone()
        assert attempt is not None and attempt["id"] != 12345, "attempts get new ids"
        answer = connection.execute(
            "SELECT points FROM attempt_answer WHERE attempt_id = ?", (attempt["id"],)
        ).fetchone()
        assert answer is not None and answer["points"] == 1, "answers are re-keyed to the new attempt"

    # an OLDER copy of the same note must not overwrite; attempts are appended again
    flash = _flash(_import_state(client, _state("older", "2001-01-02T00:00:00+00:00")))
    assert "1 attempts" in flash
    with _db() as connection:
        note = connection.execute("SELECT body_md FROM note WHERE ref_id = ?", (_STATE_MARK,)).fetchone()
        assert note["body_md"] == "newer"
        review = connection.execute(
            "SELECT last_reviewed_at FROM card_review WHERE card_ref = ?", (_STATE_MARK,)
        ).fetchone()
        assert review["last_reviewed_at"] == "2001-01-05T00:00:00+00:00"
        assert (
            connection.execute(
                "SELECT COUNT(*) FROM attempt WHERE filters LIKE ?", (f"%{_STATE_MARK}%",)
            ).fetchone()[0]
            == 2
        )
        assert (
            connection.execute("SELECT COUNT(*) FROM note WHERE ref_id = ?", (_STATE_MARK,)).fetchone()[0]
            == 1
        )


@pytest.mark.usefixtures("_clean_state")
def test_state_import_rejects_unknown_shape(client: httpx.Client):
    bad = _state("x", "2001-01-01T00:00:00+00:00")
    bad["attempts"][0]["bogus_column"] = 1
    response = _import_state(client, bad)
    assert response.status_code == 422
    assert "bogus_column" in response.text
    with _db() as connection:
        assert (
            connection.execute("SELECT COUNT(*) FROM note WHERE ref_id = ?", (_STATE_MARK,)).fetchone()[0]
            == 0
        ), "nothing lands on failure"

    response = _import_state(client, {"version": 2})
    assert response.status_code == 422
    response = post(client, "/import/state", files={"file": ("state.json", b"not json", "application/json")})
    assert response.status_code == 422
