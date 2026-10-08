"""
Sources pages (learn_togaf.md §1.4, §5.1) and the review queue (§1.5) against the live server.

The source tables are empty until ``python sources.py fetch`` runs, so the index must render an
honest empty state and an unknown section or figure is a 404. The loopback rule is checked by
the peer address (``request.client.host``), which a test on 127.0.0.1 cannot spoof, so it is not
asserted here. The review queue is exercised with drafts the test writes under
``content/review/`` and removes again.
"""

import textwrap
from pathlib import Path

import httpx
import pytest
from conftest import post

from learn_togaf.config import CONTENT_DIR

REVIEW_DIR = CONTENT_DIR / "review"
DRAFT_SET = "TEST_RQ_SET"
DRAFT_FILE = f"{DRAFT_SET}.yaml"
LESSON_FILE = "F4__97_test_review_queue.md"


def test_source_index_renders(client: httpx.Client):
    response = client.get("/source")
    assert response.status_code == 200
    assert "Sources" in response.text
    assert "python sources.py fetch" in response.text or "<table" in response.text


def test_source_search_fragment(client: httpx.Client):
    full = client.get("/source", params={"q": "phase"})
    assert full.status_code == 200
    assert "<html" in full.text
    fragment = client.get("/source", params={"q": "phase"}, headers={"HX-Request": "true"})
    assert fragment.status_code == 200
    assert "<html" not in fragment.text
    assert "phase" in fragment.text.lower()


def test_unknown_section_is_404(client: httpx.Client):
    response = client.get("/source/NOPE:99.99")
    assert response.status_code == 404
    assert "sources.py fetch" in response.text


def test_unknown_figure_is_404(client: httpx.Client):
    response = client.get("/figure/NOPE:fig-0-0")
    assert response.status_code == 404


# ---------------------------------------------------------------- review queue
def _cleanup() -> None:
    for path in (
        REVIEW_DIR / DRAFT_FILE,
        REVIEW_DIR / "rejected" / DRAFT_FILE,
        REVIEW_DIR / LESSON_FILE,
        REVIEW_DIR / "rejected" / LESSON_FILE,
        CONTENT_DIR / "questions" / "OGEA-101" / DRAFT_FILE,
        CONTENT_DIR / "lessons" / "F4" / "97_test_review_queue.md",
    ):
        path.unlink(missing_ok=True)


@pytest.fixture
def _drafts(client: httpx.Client):
    _cleanup()
    (REVIEW_DIR / DRAFT_FILE).write_text(
        textwrap.dedent(
            f"""\
            code: {DRAFT_SET}
            exam: OGEA-101
            name: Review queue test set
            source: generated
            model: test-model
            generated_at: "2026-09-10T00:00:00+00:00"
            verify: {{passed: true, reason: "TEST_RQ verifier note: entailed by ADM §5"}}
            questions:
              - id: {DRAFT_SET}-001
                unit: F4
                objective: "4.1"
                stem: "TEST_RQ: which phase establishes the architecture capability?"
                options:
                  - {{key: A, text: "Phase A"}}
                  - {{key: B, text: "Preliminary Phase", correct: true}}
                  - {{key: C, text: "Phase B"}}
                  - {{key: D, text: "Phase H"}}
                explanation: "The Preliminary Phase sets up the capability."
                refs: ["ADM §5"]
                verify: {{passed: true, reason: "ok"}}
            """
        ),
        encoding="utf-8",
    )
    (REVIEW_DIR / LESSON_FILE).write_text(
        textwrap.dedent(
            """\
            ---
            title: TEST_RQ lesson
            unit: F4
            objectives: ["4.1"]
            refs: ["ADM §5"]
            source: generated
            verify: {passed: false, reason: "TEST_RQ lesson cites a section outside its input"}
            ---
            Body of the test lesson.
            """
        ),
        encoding="utf-8",
    )
    yield
    _cleanup()
    reload = post(client, "/api/content/reload")
    if reload.status_code != 200:
        pytest.fail(f"content reload after cleanup returned {reload.status_code}: {reload.text[:200]}")


def test_review_queue_empty_state(client: httpx.Client):
    _cleanup()
    response = client.get("/review-queue")
    assert response.status_code == 200
    assert "Nothing waiting for review" in response.text or "Accept as reviewed" in response.text


@pytest.mark.usefixtures("_drafts")
def test_review_queue_lists_drafts_with_verifier_notes(client: httpx.Client):
    response = client.get("/review-queue")
    assert response.status_code == 200
    assert "TEST_RQ verifier note" in response.text
    assert "TEST_RQ lesson cites a section outside its input" in response.text
    assert "verify failed" in response.text
    assert f"/review-queue/{DRAFT_FILE}/accept" in response.text


@pytest.mark.usefixtures("_drafts")
def test_accept_moves_set_and_marks_reviewed(client: httpx.Client):
    response = post(client, f"/review-queue/{DRAFT_FILE}/accept")
    assert response.status_code == 303
    assert "Accepted" in response.headers["location"]
    destination = CONTENT_DIR / "questions" / "OGEA-101" / DRAFT_FILE
    assert destination.is_file()
    assert not (REVIEW_DIR / DRAFT_FILE).exists()
    text = destination.read_text(encoding="utf-8")
    assert "status: reviewed" in text and "reviewed_at:" in text
    assert "verify:" not in text
    assert DRAFT_SET not in client.get("/review-queue").text
    # the cache was reloaded: the question is now in the bank as reviewed
    page = client.get("/practice")
    assert page.status_code == 200


@pytest.mark.usefixtures("_drafts")
def test_reject_moves_draft_to_rejected(client: httpx.Client):
    response = post(client, f"/review-queue/{LESSON_FILE}/reject")
    assert response.status_code == 303
    assert (REVIEW_DIR / "rejected" / LESSON_FILE).is_file()
    assert not (REVIEW_DIR / LESSON_FILE).exists()
    assert "TEST_RQ lesson cites" not in client.get("/review-queue").text


def test_unknown_draft_is_404(client: httpx.Client):
    assert post(client, "/review-queue/no_such_draft.yaml/accept").status_code == 404
    assert post(client, "/review-queue/no_such_draft.md/reject").status_code == 404


def test_draft_id_cannot_escape_review_dir(client: httpx.Client):
    response = post(client, "/review-queue/../questions/OGEA-101/starter.yaml/accept")
    assert response.status_code in (404, 422)
    assert Path(CONTENT_DIR / "questions" / "OGEA-101" / "starter.yaml").is_file()
