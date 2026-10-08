"""
Generation (learn_togaf.md §8): the prompts are golden-tested against recorded responses under
fixtures/generate/ with a fake client (client.complete monkeypatched) — no live call, no
network. The lessons and questions stages must produce files the content loader's validators
accept; a generated question whose refs cite a section outside its input is rejected; a
stage refuses an objective with no objective_source row; a verify failure lands in review/ and
is never moved.
"""

import shutil
import sqlite3
from pathlib import Path

import orjson
import pytest
import yaml
from loguru import logger

from learn_togaf.content.loader import ContentError, load_blueprint, load_lessons, parse_question_set
from learn_togaf.content.models import LessonFrontMatter
from learn_togaf.db import apply_schema, connect
from learn_togaf.generate import (
    GroundingError,
    RefsOutsideInput,
    check_refs,
    client,
    grounding_for_unit,
    lessons,
    questions,
    verify,
)
from learn_togaf.generate.schemas import FOUNDATION_QUESTIONS, LESSON, PRACTITIONER_QUESTIONS, VERIFY
from learn_togaf.sources import index
from learn_togaf.sources.parse_html import parse_page

REPO_ROOT = Path(__file__).resolve().parents[2]
CONTENT_DIR = REPO_ROOT / "content"
FIXTURES = Path(__file__).with_name("fixtures")
BASE_URL = "https://pubs.opengroup.org/togaf-standard/"


def _recorded(name: str) -> str:
    return (FIXTURES / "generate" / name).read_text(encoding="utf-8")


@pytest.fixture
def content_dir(tmp_path: Path) -> Path:
    """A private copy of content/ so drafts land in a throwaway review/."""
    target = tmp_path / "content"
    shutil.copytree(CONTENT_DIR, target, ignore=shutil.ignore_patterns("review", "imported"))
    (target / "review").mkdir()
    return target


@pytest.fixture
def connection(tmp_path: Path) -> sqlite3.Connection:
    connection = connect(tmp_path / "gen.db")
    apply_schema(connection)
    pages = [
        parse_page((FIXTURES / "sources/adm/index.html").read_text(), "ADM", f"{BASE_URL}adm/index.html"),
        parse_page((FIXTURES / "sources/adm/chap03.html").read_text(), "ADM", f"{BASE_URL}adm/chap03.html"),
    ]
    index.index_document(connection, "ADM", pages)
    index.index_document(
        connection,
        "INTRO",
        [
            parse_page(
                (FIXTURES / "sources/introduction/index.html").read_text(),
                "INTRO",
                f"{BASE_URL}introduction/index.html",
            )
        ],
    )
    blueprint = load_blueprint(CONTENT_DIR)
    # Only 4.2, P3.1, P3.2 and 1.3 are mapped: 4.1 and the rest stay empty on purpose.
    index.apply_objective_mapping(
        connection,
        {"4.2": ["ADM › 3"], "P3.1": ["ADM › 3"], "P3.2": ["ADM › 3.2", "ADM:sec-3-4"], "1.3": ["INTRO › 2"]},
        blueprint.objective_codes(),
    )
    yield connection
    connection.close()


class FakeClient:
    """Replays recorded responses by custom_id and records what was asked."""

    def __init__(self, responses: dict[str, str]) -> None:
        self.responses = responses
        self.requests: list[client.Request] = []

    def complete(self, request: client.Request) -> str:
        self.requests.append(request)
        if request.custom_id not in self.responses:
            raise AssertionError(
                f"unexpected request {request.custom_id}; only {sorted(self.responses)} are recorded"
            )
        return self.responses[request.custom_id]


@pytest.fixture
def log_lines() -> list[str]:
    """loguru writes to the stderr object it bound at import, which pytest's capture does not
    own; a list sink is the deterministic way to read what a stage logged."""
    lines: list[str] = []
    handle = logger.add(lines.append, format="{message}", level="INFO")
    yield lines
    logger.remove(handle)


@pytest.fixture
def fake(monkeypatch: pytest.MonkeyPatch):
    def install(responses: dict[str, str]) -> FakeClient:
        fake_client = FakeClient(responses)
        monkeypatch.setattr(client, "complete", fake_client.complete)
        return fake_client

    return install


# ---------------------------------------------------------------- the refusal
def test_stage_refuses_unmapped_objective(connection: sqlite3.Connection, content_dir: Path, fake):
    fake({})
    with pytest.raises(GroundingError, match="objective 4.1 .* no objective_source rows.*sources.py index"):
        lessons.run(connection, content_dir, "F4", dry_run=False, limit=None)
    with pytest.raises(GroundingError):
        questions.run(connection, content_dir, "OGEA-101", "F4", dry_run=True, limit=None, batch=False)
    assert not list((content_dir / "review").rglob("*"))


def test_grounding_sends_only_mapped_sections(connection: sqlite3.Connection):
    blueprint = load_blueprint(CONTENT_DIR)
    groundings = grounding_for_unit(connection, blueprint, "P3")
    assert [g.objective_code for g in groundings] == ["P3.1", "P3.2"]
    assert groundings[1].section_ids == ["ADM:sec-3-2", "ADM:sec-3-4"]
    grounding = groundings[0]
    assert grounding.section_ids == [
        "ADM:chap-03",
        "ADM:sec-3-1",
        "ADM:sec-3-2",
        "ADM:sec-3-3",
        "ADM:sec-3-4",
        "ADM:sec-3-5",
    ]
    assert grounding.refs == ["ADM §3", "ADM §3.1", "ADM §3.2", "ADM §3.3", "ADM §3.4", "ADM §3.5"]


# ---------------------------------------------------------------- dry run
def test_dry_run_prints_prompt_and_section_ids_without_calling(connection, content_dir, fake, capsys):
    fake_client = fake({})
    result = questions.run(
        connection, content_dir, "OGEA-102", "P3", dry_run=True, limit=None, batch=False
    )
    assert result is None and fake_client.requests == []
    out = capsys.readouterr().out
    assert "input section ids: ADM:chap-03, ADM:sec-3-1" in out
    assert "Practitioner (OGEA-102) scenario questions" in out  # the stage prompt
    assert "Scenario brief: industry=" in out
    assert "structured=yes" in out


# ---------------------------------------------------------------- lessons
def test_lessons_stage_writes_a_draft_the_loader_accepts(connection, content_dir, fake):
    fake_client = fake({"lesson-4.2": _recorded("lesson_4.2.json")})
    # F4 has 4.1 first and it is unmapped; generate for a unit view that starts at 4.2 by mapping order:
    blueprint = load_blueprint(CONTENT_DIR)
    grounding = next(g for g in [index_grounding(connection, blueprint, "4.2")])
    path = lessons.lesson_from_response(fake_client.responses["lesson-4.2"], grounding, 1, content_dir)
    assert path == content_dir / "review" / "F4" / "01_phase_a_in_the_fixture.md"
    text = path.read_text(encoding="utf-8")
    assert text.startswith("---\ntitle: Phase A in the fixture method\nunit: F4\nobjectives:\n- '4.2'\n")
    assert (
        "source: generated" in text
        and "status: draft" in text
        and "model: " in text
        and "generated_at:" in text
    )
    assert "## Check yourself" in text and "[ADM §3.5]" in text
    # the loader validates it like any lesson: copy into lessons/F4 and load
    target = content_dir / "lessons" / "F4" / "09_phase_a_in_the_fixture.md"
    shutil.copy(path, target)
    loaded = {lesson.id: lesson for lesson in load_lessons(content_dir, blueprint)}
    assert loaded["F4/09_phase_a_in_the_fixture"].front.refs == [
        "ADM §3",
        "ADM §3.1",
        "ADM §3.3",
        "ADM §3.4",
        "ADM §3.5",
    ]
    assert loaded["F4/09_phase_a_in_the_fixture"].front.source == "generated"


def index_grounding(connection, blueprint, objective_code):
    from learn_togaf.generate import grounding_for_objective

    return grounding_for_objective(connection, blueprint, objective_code)


def test_lesson_citing_outside_section_is_rejected_and_not_written(connection, content_dir):
    blueprint = load_blueprint(CONTENT_DIR)
    grounding = index_grounding(connection, blueprint, "4.2")
    with pytest.raises(RefsOutsideInput, match=r"GOV §9"):
        lessons.lesson_from_response(_recorded("lesson_outside_refs.json"), grounding, 1, content_dir)
    assert not list((content_dir / "review").rglob("*.md"))


def test_lessons_run_end_to_end_via_fake_client(connection, content_dir, fake, monkeypatch):
    fake_client = fake(
        {
            "lesson-1.3": _recorded("lesson_4.2.json")
            .replace("ADM §3.1", "INTRO §2")
            .replace("ADM §3.3", "INTRO §2")
            .replace("ADM §3.4", "INTRO §2")
            .replace("ADM §3.5", "INTRO §2")
            .replace("ADM §3", "INTRO §2")
        }
    )
    blueprint = load_blueprint(CONTENT_DIR)
    # F1's first objective 1.1 is unmapped, so run() refuses the unit; drive the mapped one directly.
    grounding = index_grounding(connection, blueprint, "1.3")
    requests = lessons.build_requests([grounding])
    assert requests[0][1].system[1]["cache_control"] == {"type": "ephemeral"}
    assert "SOURCE SECTIONS" in requests[0][1].system[1]["text"]
    assert requests[0][1].schema is LESSON
    text = client.complete(requests[0][1])
    path = lessons.lesson_from_response(text, grounding, 1, content_dir)
    assert path.parent == content_dir / "review" / "F1"
    assert fake_client.requests[0].section_ids == ["INTRO:chap-02"]


# ---------------------------------------------------------------- questions
def test_foundation_questions_validate_reject_and_write(connection, content_dir, fake, log_lines):
    fake({"OGEA-101-4.2": _recorded("questions_foundation_4.2.json")})
    blueprint = load_blueprint(CONTENT_DIR)
    grounding = index_grounding(connection, blueprint, "4.2")
    requests = questions.build_requests("OGEA-101", [grounding], blueprint, 3, connection)
    assert requests[0][1].schema is FOUNDATION_QUESTIONS
    assert "ALREADY IN THE BANK" in requests[0][1].user
    responses = client.complete_many([requests[0][1]], batch=False)
    accepted, next_index = questions.questions_from_response(
        responses["OGEA-101-4.2"], "OGEA-101", grounding, 1
    )
    # four recorded: two good, one cites INTRO §2 (outside the input), one has two correct options
    assert len(accepted) == 2 and next_index == 3
    assert [q["objective"] for q in accepted] == ["4.2", "4.2"]
    assert all(q["source"] == "generated" and q["status"] == "draft" for q in accepted)
    logged = "\n".join(log_lines)
    assert "outside its input: ['INTRO §2']" in logged
    assert "exactly one correct option" in logged
    path = questions.write_set(content_dir, "OGEA-101", "F4", accepted, blueprint)
    assert path.parent == content_dir / "review" / "questions" / "OGEA-101"
    assert path.name.startswith("G_F4_") and path.suffix == ".yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    assert data["code"].startswith("G_F4_") and data["exam"] == "OGEA-101" and data["source"] == "generated"
    question_set = parse_question_set(data, path, blueprint)  # the loader's validator
    assert question_set.count() == 2 and question_set.single[0].refs == ["ADM §3.3", "ADM §3.5"]


def test_questions_run_writes_set_for_mapped_unit(connection, content_dir, fake):
    fake({"OGEA-102-P3.1": _recorded("questions_practitioner_P3.1.json")})
    blueprint = load_blueprint(CONTENT_DIR)
    with pytest.raises(GroundingError):  # F4's first objective 4.1 is unmapped, so the unit is refused
        questions.run(connection, content_dir, "OGEA-102", "F4", dry_run=False, limit=None, batch=False)
    grounding = index_grounding(connection, blueprint, "P3.1")
    requests = questions.build_requests("OGEA-102", [grounding], blueprint, 1, connection)
    assert requests[0][1].schema is PRACTITIONER_QUESTIONS
    accepted, _ = questions.questions_from_response(
        client.complete(requests[0][1]), "OGEA-102", grounding, 1
    )
    assert len(accepted) == 1 and sorted(a["points"] for a in accepted[0]["answers"]) == [0, 1, 3, 5]
    path = questions.write_set(content_dir, "OGEA-102", "P3", accepted, blueprint)
    parsed = parse_question_set(yaml.safe_load(path.read_text()), path, blueprint)
    assert parsed.gradient[0].open_book_hint.startswith("Where to look")


def test_check_refs_gate():
    assert check_refs(["ADM §3.3 "], ["ADM §3.3", "ADM §3"], "q") == ["ADM §3.3"]
    with pytest.raises(RefsOutsideInput):
        check_refs(["ADM §4"], ["ADM §3"], "q")
    with pytest.raises(RefsOutsideInput):
        check_refs([], ["ADM §3"], "q")


def test_bad_generated_set_fails_the_loader(content_dir):
    blueprint = load_blueprint(CONTENT_DIR)
    data = {
        "code": "G_X",
        "exam": "OGEA-101",
        "name": "x",
        "source": "generated",
        "questions": [
            {
                "id": "F4-X",
                "unit": "F4",
                "objective": "1.1",
                "stem": "s",
                "explanation": "e",
                "refs": ["ADM §3"],
                "options": [{"key": k, "text": k, "correct": k == "A"} for k in "ABCD"],
            }
        ],
    }
    with pytest.raises(ContentError, match="not an objective of unit F4"):
        parse_question_set(data, content_dir / "x.yaml", blueprint)


# ---------------------------------------------------------------- verify
def test_verify_failure_stays_in_review_and_is_never_moved(connection, content_dir, fake):
    blueprint = load_blueprint(CONTENT_DIR)
    grounding = index_grounding(connection, blueprint, "4.2")
    lesson_path = lessons.lesson_from_response(_recorded("lesson_4.2.json"), grounding, 1, content_dir)
    accepted, _ = questions.questions_from_response(
        _recorded("questions_foundation_4.2.json"), "OGEA-101", grounding, 1
    )
    set_path = questions.write_set(content_dir, "OGEA-101", "F4", accepted, blueprint)
    ids = [q["id"] for q in accepted]
    set_label = set_path.relative_to(content_dir / "review")
    fake_client = fake(
        {
            f"verify-{lesson_path.relative_to(content_dir / 'review')}": _recorded("verify_pass.json"),
            f"verify-{set_label}#{ids[0]}": _recorded("verify_pass.json"),
            f"verify-{set_label}#{ids[1]}": _recorded("verify_fail.json"),
        }
    )
    before = sorted(str(p.relative_to(content_dir)) for p in content_dir.rglob("*") if p.is_file())
    summary = verify.run(connection, content_dir, dry_run=False, limit=None, batch=False)
    assert summary == {"items": 3, "passed": 2, "failed": 1}
    after = sorted(str(p.relative_to(content_dir)) for p in content_dir.rglob("*") if p.is_file())
    assert before == after  # nothing moved, nothing created outside review/
    assert all(request.schema is VERIFY for request in fake_client.requests)
    assert fake_client.requests[0].section_ids[:2] == [
        "ADM:chap-03",
        "ADM:sec-3-1",
    ]  # the cited chapter with its descendants
    data = yaml.safe_load(set_path.read_text(encoding="utf-8"))
    assert data["verify"]["passed"] is False
    by_id = {q["id"]: q for q in data["questions"]}
    assert by_id[ids[0]]["verify"]["passed"] is True
    assert by_id[ids[1]]["verify"]["passed"] is False and "ADM §3.4" in by_id[ids[1]]["verify"]["reason"]
    assert by_id[ids[1]]["status"] == "draft"
    assert parse_question_set(data, set_path, blueprint).count() == 2  # still a valid set after the verdict
    from learn_togaf.content.loader import split_front_matter

    front, _ = split_front_matter(lesson_path.read_text(encoding="utf-8"), lesson_path)
    assert front["verify"]["passed"] is True and front["verify"]["at"]
    LessonFrontMatter.model_validate(front)  # the verify block does not break the front matter
    assert not (content_dir / "questions" / "OGEA-101" / set_path.name).exists()


def test_verify_dry_run_makes_no_call(connection, content_dir, fake, capsys):
    blueprint = load_blueprint(CONTENT_DIR)
    grounding = index_grounding(connection, blueprint, "4.2")
    lessons.lesson_from_response(_recorded("lesson_4.2.json"), grounding, 1, content_dir)
    fake_client = fake({})
    assert verify.run(connection, content_dir, dry_run=True, limit=None, batch=False) == {
        "items": 1,
        "requests": 1,
    }
    assert fake_client.requests == []
    assert "independent judge" in capsys.readouterr().out


# ---------------------------------------------------------------- client request shape
def test_request_params_use_adaptive_thinking_and_output_config():
    request = client.Request(
        stage="x",
        system=[
            {"type": "text", "text": "p"},
            {"type": "text", "text": "s", "cache_control": {"type": "ephemeral"}},
        ],
        user="u",
        schema=VERIFY,
        custom_id="c",
    )
    params = request.params()
    assert params["thinking"] == {"type": "adaptive"}
    assert params["output_config"]["format"] == {"type": "json_schema", "schema": VERIFY}
    assert params["output_config"]["effort"]
    assert "budget_tokens" not in orjson.dumps(params).decode()
    assert params["messages"] == [{"role": "user", "content": "u"}]
