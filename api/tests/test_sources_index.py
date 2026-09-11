"""
Source index (learn_togaf.md §8): the crawl parser replayed against fixture pages — our own
fixture HTML in the Digital Edition's shape, not the standard's text — must give the expected
heading tree, anchors, section ids, text and figures; the index writes to a temporary SQLite and
every ref in content/ that names a fixture section resolves; the objective mapping starter
loads and applies; the PDF outline maps section numbers to pages. No network anywhere.
"""

import sqlite3
from pathlib import Path

import pymupdf
import pytest
import yaml

from learn_togaf.content.loader import load_blueprint, load_lessons, load_question_sets, split_front_matter
from learn_togaf.content.models import validate_ref
from learn_togaf.db import apply_schema, connect
from learn_togaf.sources import index
from learn_togaf.sources.fetch import classify_url, html_path
from learn_togaf.sources.figures import figure_file_name, record_figures
from learn_togaf.sources.parse_html import figure_number, page_links, parse_page, split_heading
from learn_togaf.sources.parse_pdf import outline_pages, register_pdf, sections_from_outline

REPO_ROOT = Path(__file__).resolve().parents[2]
CONTENT_DIR = REPO_ROOT / "content"
SOURCES_DIR = REPO_ROOT / "resources" / "sources"
FIXTURES = Path(__file__).with_name("fixtures") / "sources"
BASE_URL = "https://pubs.opengroup.org/togaf-standard/"


def _page(segment: str, page: str, code: str):
    return parse_page(
        (FIXTURES / segment / page).read_text(encoding="utf-8"), code, f"{BASE_URL}{segment}/{page}"
    )


@pytest.fixture
def connection(tmp_path: Path) -> sqlite3.Connection:
    connection = connect(tmp_path / "index.db")
    apply_schema(connection)
    index.index_document(
        connection,
        "ADM",
        [_page("adm", "index.html", "ADM"), _page("adm", "chap03.html", "ADM")],
        pdf_pages={"3": 40, "3.3": 42},
    )
    index.index_document(connection, "INTRO", [_page("introduction", "index.html", "INTRO")])
    index.index_document(
        connection,
        "GUIDE:business-scenarios",
        [_page("guides/business-scenarios", "index.html", "GUIDE:business-scenarios")],
    )
    yield connection
    connection.close()


# ---------------------------------------------------------------- parse_html
def test_heading_tree_anchors_and_ids():
    page = _page("adm", "chap03.html", "ADM")
    assert [section.id for section in page.sections] == [
        "ADM:chap-03",
        "ADM:sec-3-1",
        "ADM:sec-3-2",
        "ADM:sec-3-3",
        "ADM:sec-3-4",
        "ADM:sec-3-5",
    ]
    assert [section.level for section in page.sections] == [2, 3, 3, 3, 3, 3]
    assert page.sections[3].heading_path == "ADM › 3. Phase A: Fixture Vision › 3.3 Inputs"
    assert page.sections[3].anchor_url == f"{BASE_URL}adm/chap03.html#sec-3-3"
    assert page.sections[3].ref == "ADM §3.3"
    assert page.title == "Fixture ADM: Phase A"


def test_heading_path_uses_numbered_headings_only():
    page = _page("adm", "index.html", "ADM")
    by_id = {section.id: section for section in page.sections}
    assert by_id["ADM:adm-title"].number is None and by_id["ADM:adm-title"].ref is None
    assert (
        by_id["ADM:sec-1-1"].heading_path
        == "ADM › 1. Introduction to the fixture method › 1.1 Structure of each phase chapter"
    )
    assert by_id["ADM:chap-01"].anchor == "chap-01"  # anchor from an empty <a id> inside the heading


def test_section_text_lists_tables_and_anchorless_headings():
    page = _page("adm", "chap03.html", "ADM")
    by_id = {section.id: section for section in page.sections}
    assert by_id["ADM:sec-3-4"].text == (
        "1. Establish the project\n2. Identify stakeholders and their concerns\n  - use a stakeholder map\n"
        "3. Define scope\n4. Develop the vision and the statement of work"
    )
    outputs = by_id["ADM:sec-3-5"].text
    assert outputs.startswith("- Approved statement of fixture work\n- Fixture vision")
    assert (
        "| Output | Where it goes |\n| --- | --- |\n| Statement of work | Sponsor \\| governance board |"
        in outputs
    )
    assert "**A heading without an anchor**" in outputs
    assert "This paragraph belongs to 3.5" in outputs
    assert outputs.count("Figure 3-1") == 1  # the caption is recorded once, with the figure
    assert (
        by_id["ADM:chap-03"].text
        == "Phase A of the fixture turns a request into an approved statement of work."
    )


def test_figure_list():
    chap = _page("adm", "chap03.html", "ADM")
    assert [(f.id, f.section_id, f.number) for f in chap.figures] == [("ADM:fig-3-1", "ADM:sec-3-5", "3-1")]
    assert chap.figures[0].src == f"{BASE_URL}adm/images/fig-3-1.png"
    assert chap.figures[0].caption == "Figure 3-1: Stakeholder power and interest grid (fixture)"
    intro = _page("introduction", "index.html", "INTRO")
    assert [f.id for f in intro.figures] == ["INTRO:fig-3-2"]
    assert intro.figures[0].src == f"{BASE_URL}adm/images/fig-3-2.svg"
    assert [f.id for f in _page("adm", "index.html", "ADM").figures] == ["ADM:fig-1-1"]
    assert figure_number("Figure 12-3: X") == "12-3" and figure_number("no caption") is None


def test_split_heading():
    assert split_heading("3.3 Inputs") == ("3.3", "Inputs")
    assert split_heading("3. Phase A: Vision") == ("3", "Phase A: Vision")
    assert split_heading("Preface") == (None, "Preface")


def test_page_links_and_crawl_scope():
    links = page_links(
        (FIXTURES / "introduction/index.html").read_text(), f"{BASE_URL}introduction/index.html"
    )
    assert links == [
        "https://example.org/outside",
        f"{BASE_URL}adm/index.html",
        f"{BASE_URL}guides/business-scenarios/index.html",
    ]
    assert classify_url(f"{BASE_URL}adm/chap03.html", BASE_URL) == ("adm", "chap03.html")
    assert classify_url(f"{BASE_URL}guides/business-scenarios/", BASE_URL) == (
        "guides/business-scenarios",
        "index.html",
    )
    assert classify_url(BASE_URL, BASE_URL) == ("root", "index.html")
    assert classify_url(f"{BASE_URL}adm/images/x.png", BASE_URL) is None
    assert classify_url("https://example.org/outside", BASE_URL) is None
    assert html_path(Path("/store"), "guides/business-scenarios", "index.html") == Path(
        "/store/html/guides/business-scenarios/index.html"
    )


def test_document_codes():
    assert index.document_code("adm") == "ADM"
    assert index.document_code("guides/business-scenarios") == "GUIDE:business-scenarios"
    assert index.document_code("root") is None
    assert index.segment_for_code("GUIDE:business-scenarios") == "business-scenarios"
    assert index.segment_for_code("GOV") == "ea-capability-and-governance"


# ---------------------------------------------------------------- index → SQLite
def test_index_writes_documents_and_sections(connection: sqlite3.Connection):
    docs = {row["code"]: row for row in connection.execute("SELECT * FROM source_document")}
    assert set(docs) == {"ADM", "INTRO", "GUIDE:business-scenarios"}
    assert docs["ADM"]["kind"] == "STANDARD" and docs["GUIDE:business-scenarios"]["kind"] == "GUIDE"
    rows = connection.execute(
        "SELECT id, ordinal, pdf_page FROM source_section WHERE document_code='ADM' ORDER BY ordinal"
    ).fetchall()
    assert [row["id"] for row in rows][:3] == ["ADM:adm-title", "ADM:chap-01", "ADM:sec-1-1"]
    assert [row["ordinal"] for row in rows] == list(range(1, 12))  # ordinals run across pages
    by_id = {row["id"]: row for row in rows}
    assert by_id["ADM:sec-3-3"]["pdf_page"] == 42 and by_id["ADM:chap-03"]["pdf_page"] == 40
    assert by_id["ADM:sec-3-1"]["pdf_page"] is None


def test_reindex_is_idempotent_and_drops_vanished_sections(connection: sqlite3.Connection):
    index.index_document(connection, "ADM", [_page("adm", "chap03.html", "ADM")])
    ids = [
        row["id"]
        for row in connection.execute(
            "SELECT id FROM source_section WHERE document_code='ADM' ORDER BY ordinal"
        )
    ]
    assert ids == ["ADM:chap-03", "ADM:sec-3-1", "ADM:sec-3-2", "ADM:sec-3-3", "ADM:sec-3-4", "ADM:sec-3-5"]


def test_resolve_ref_both_ways(connection: sqlite3.Connection):
    assert [row["id"] for row in index.resolve_ref(connection, "ADM §3.3")] == ["ADM:sec-3-3"]
    assert [row["id"] for row in index.resolve_ref(connection, "ADM §3 Phase A")] == ["ADM:chap-03"]
    assert [row["id"] for row in index.resolve_ref(connection, "GUIDE:business-scenarios §1")] == [
        "GUIDE:business-scenarios:chap-01"
    ]
    assert index.resolve_ref(connection, "ADM §99") == []
    row = connection.execute("SELECT * FROM source_section WHERE id='ADM:sec-3-3'").fetchone()
    assert index.section_ref(row["document_code"], row["heading_path"]) == "ADM §3.3"
    assert validate_ref(index.section_ref("ADM", row["heading_path"]))


def test_section_with_descendants(connection: sqlite3.Connection):
    ids = [row["id"] for row in index.section_with_descendants(connection, "ADM:chap-03")]
    assert ids == ["ADM:chap-03", "ADM:sec-3-1", "ADM:sec-3-2", "ADM:sec-3-3", "ADM:sec-3-4", "ADM:sec-3-5"]
    assert [row["id"] for row in index.section_with_descendants(connection, "ADM:sec-3-3")] == ["ADM:sec-3-3"]


def test_content_refs_that_name_fixture_sections_resolve(connection: sqlite3.Connection):
    """Every ref under content/ whose document and number exist in the fixture index resolves
    to a source_section; a ref outside the fixtures is not a failure of the resolver."""
    blueprint = load_blueprint(CONTENT_DIR)
    refs: set[str] = set()
    for lesson in load_lessons(CONTENT_DIR, blueprint):
        refs.update(lesson.front.refs)
    for question_set in load_question_sets(CONTENT_DIR, blueprint):
        for question in [*question_set.foundation, *question_set.practitioner]:
            refs.update(question.refs)
    fixture_refs = {
        index.section_ref(row["document_code"], row["heading_path"])
        for row in connection.execute("SELECT document_code, heading_path FROM source_section")
    }
    fixture_refs.discard(None)
    overlapping = sorted(
        ref for ref in refs if index.parse_ref(ref) in {index.parse_ref(f) for f in fixture_refs}
    )
    assert overlapping, (
        "content/ carries no ref into the fixture index; the fixtures should cover at least ADM §3"
    )
    for ref in overlapping:
        assert index.resolve_ref(connection, ref), f"{ref} did not resolve"


def test_text_files(connection: sqlite3.Connection, tmp_path: Path):
    written = index.write_text_files(connection, tmp_path)
    assert written == 16
    path = tmp_path / "text" / "adm" / "ADM:sec-3-3.md"
    text = path.read_text(encoding="utf-8")
    assert text.startswith(
        "# ADM › 3. Phase A: Fixture Vision › 3.3 Inputs\n\n- id: ADM:sec-3-3\n- ref: ADM §3.3\n"
    )
    assert "- pdf_page: 42" in text and "- Request for fixture work" in text
    assert (
        tmp_path / "text" / "business-scenarios" / "GUIDE:business-scenarios:chap-01.md"
    ).is_file()


# ---------------------------------------------------------------- objective mapping
def test_objective_mapping_starter_loads_and_applies(connection: sqlite3.Connection):
    mapping = index.load_objective_mapping(SOURCES_DIR / index.OBJECTIVE_MAPPING_FILE)
    blueprint = load_blueprint(CONTENT_DIR)
    foundation = {o.code for u in blueprint.units if u.exam == "FOUNDATION" for o in u.objectives}
    assert foundation <= set(mapping), (
        f"Foundation objectives missing from the starter: {sorted(foundation - set(mapping))}"
    )
    counts = index.apply_objective_mapping(connection, mapping, blueprint.objective_codes())
    assert counts["4.2"] == 6  # "ADM › 3" is the chapter and every 3.x
    assert counts["1.3"] == 1  # "INTRO › 2"
    rows = connection.execute(
        "SELECT section_id FROM objective_source WHERE objective_code='4.2' ORDER BY section_id"
    ).fetchall()
    assert [row["section_id"] for row in rows] == [
        "ADM:chap-03",
        "ADM:sec-3-1",
        "ADM:sec-3-2",
        "ADM:sec-3-3",
        "ADM:sec-3-4",
        "ADM:sec-3-5",
    ]
    with pytest.raises(ValueError, match="not in blueprint"):
        index.apply_objective_mapping(connection, {"9.9": ["ADM › 3"]}, blueprint.objective_codes())


def test_match_sections_specs(connection: sqlite3.Connection):
    assert index.match_sections(connection, "ADM › 3.3") == ["ADM:sec-3-3"]
    assert index.match_sections(connection, "ADM:sec-2-1") == ["ADM:sec-2-1"]
    assert index.match_sections(connection, "ADM › Fixture") == ["ADM:adm-title"]
    assert index.match_sections(connection, "ADM › 7") == []


# ---------------------------------------------------------------- ADM phase lists
def test_adm_phase_parse_and_diff(connection: sqlite3.Connection, tmp_path: Path):
    parsed = index.parse_adm_phases(connection)
    assert set(parsed) == {"PRELIM", "A"}
    phase = parsed["A"]
    assert phase.inputs == ["Request for fixture work", "Fixture principles", "Populated fixture repository"]
    assert phase.steps == [
        "Establish the project",
        "Identify stakeholders and their concerns",
        "Define scope",
        "Develop the vision and the statement of work",
    ]
    assert phase.outputs == ["Approved statement of fixture work", "Fixture vision"]
    assert phase.approach.startswith("Start from the request")
    assert phase.refs == ["ADM §3"]
    with open(CONTENT_DIR / "adm" / "phases.yaml", encoding="utf-8") as handle:
        authored = yaml.safe_load(handle)
    differences = index.diff_adm_phases(parsed, authored)
    assert any(line.startswith("A.inputs: + Request for fixture work") for line in differences)
    assert any(line.startswith("B: in phases.yaml but no ADM chapter parsed") for line in differences)
    path = index.write_parsed_phases(tmp_path, parsed)
    assert path == tmp_path / "review" / "adm_phases.parsed.yaml"
    assert [phase["code"] for phase in yaml.safe_load(path.read_text())] == ["PRELIM", "A"]


# ---------------------------------------------------------------- PDF outline
def test_pdf_outline_maps_numbers_to_pages(tmp_path: Path):
    path = tmp_path / "adm.pdf"
    document = pymupdf.open()
    for text in (
        "Fixture ADM cover",
        "1. Introduction to the fixture method",
        "3. Phase A: Fixture Vision",
        "3.3 Inputs\nRequest for fixture work",
    ):
        page = document.new_page()
        page.insert_text((72, 72), text)
    document.set_toc(
        [
            [1, "1. Introduction to the fixture method", 2],
            [1, "3. Phase A: Fixture Vision", 3],
            [2, "3.3 Inputs", 4],
        ]
    )
    document.set_metadata({"title": "Fixture ADM"})
    document.save(path)
    document.close()
    info = register_pdf(path)
    assert info.title == "Fixture ADM" and info.page_count == 4 and len(info.hash) == 64
    assert outline_pages(info) == {"1": 2, "3": 3, "3.3": 4}
    sections = sections_from_outline(path, "ADM", info)
    assert [section.id for section in sections] == ["ADM:1", "ADM:3", "ADM:3.3"]
    assert sections[2].heading_path == "ADM › 3. Phase A: Fixture Vision › 3.3 Inputs"
    assert "Request for fixture work" in sections[2].text


# ---------------------------------------------------------------- figures store
def test_record_figures_and_important(connection: sqlite3.Connection, tmp_path: Path):
    from learn_togaf.sources.figures import FigureRecord

    records = [
        FigureRecord(
            "ADM:fig-3-1",
            "ADM",
            "ADM:sec-3-5",
            "Figure 3-1: grid",
            tmp_path / "ADM_fig-3-1.png",
            10,
            10,
            "h1",
        ),
        FigureRecord(
            "ADM:fig-9-9", "ADM", "ADM:missing", "orphan", tmp_path / "ADM_fig-9-9.png", 10, 10, "h2"
        ),
    ]
    assert record_figures(connection, records, {"ADM:fig-3-1"}) == 2
    rows = {row["id"]: row for row in connection.execute("SELECT * FROM source_figure")}
    assert rows["ADM:fig-3-1"]["important"] == 1 and rows["ADM:fig-3-1"]["section_id"] == "ADM:sec-3-5"
    assert rows["ADM:fig-9-9"]["section_id"] is None
    assert (
        figure_file_name("GUIDE:business-scenarios:fig-1-1", "png") == "GUIDE_business-scenarios_fig-1-1.png"
    )


def test_important_figures_starter_loads():
    from learn_togaf.content.loader import load_important_figures

    figures = load_important_figures(SOURCES_DIR)
    assert len(figures) >= 8
    blueprint = load_blueprint(CONTENT_DIR)
    for figure in figures:
        assert figure.id.split(":")[0] in {"ADM", "INTRO", "TECH", "APPLY", "CONTENT", "GOV"}
        assert ":fig-" in figure.id
        assert set(figure.objectives) <= blueprint.objective_codes(), figure.id


def test_review_dir_drafts_have_front_matter_shape(tmp_path: Path):
    text = "---\ntitle: x\nunit: F4\nobjectives: ['4.2']\n---\nbody\n"
    front, body = split_front_matter(text, tmp_path / "x.md")
    assert front["unit"] == "F4" and body.strip() == "body"
