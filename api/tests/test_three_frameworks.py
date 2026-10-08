"""
Three frameworks in one app (learn_sabsa_archimate.md §4): exams as data, the crosswalk on the
ADM explorer, ArchiMate views on the artefact catalogue and the worked examples, the glossary
track filter, the braid on the study plan. Live-server tests over httpx, like the rest.
"""

import re
import subprocess
import sys
from pathlib import Path

from conftest import get

from learn_togaf.config import CONTENT_DIR
from learn_togaf.content.loader import load_adm, load_blueprint, load_examples, load_lessons
from learn_togaf.db import connect

REPO = Path(__file__).resolve().parents[2]
ARCHIMATE_STATIC = REPO / "api" / "src" / "learn_togaf" / "pages" / "static" / "archimate"


# ---------------------------------------------------------------- content contracts
def test_every_artefact_has_an_archimate_mapping_that_resolves() -> None:
    _, _, artefacts = load_adm(CONTENT_DIR)
    connection = connect()
    from learn_togaf.sources.index import resolve_ref

    for artefact in artefacts:
        assert artefact.archimate is not None, f"{artefact.code} has no archimate: mapping"
        assert artefact.archimate.viewpoint and artefact.archimate.elements
        assert resolve_ref(connection, artefact.archimate.ref), f"{artefact.code}: {artefact.archimate.ref}"


def test_crosswalk_covers_every_phase_and_its_lessons_exist() -> None:
    blueprint = load_blueprint(CONTENT_DIR)
    lesson_ids = {lesson.id for lesson in load_lessons(CONTENT_DIR, blueprint)}
    phases, _, _ = load_adm(CONTENT_DIR, lesson_ids)
    for phase in phases:
        assert phase.crosswalk is not None, f"phase {phase.code} has no crosswalk entry"
        assert phase.crosswalk.archimate.viewpoints and phase.crosswalk.sabsa.cells


def test_archimate_models_are_rendered_and_up_to_date() -> None:
    """content/archimate/*.yaml → static/archimate/*.svg by draw_archimate.py; a stale SVG is a
    content error, not a runtime one, so the check runs here."""
    result = subprocess.run(
        [sys.executable, str(REPO / "draw_archimate.py"), "--check"], capture_output=True, text=True, check=False
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert (ARCHIMATE_STATIC / "notation_sampler.svg").is_file()


def test_model_examples_name_a_rendered_figure_and_a_real_artefact() -> None:
    _, _, artefacts = load_adm(CONTENT_DIR)
    codes = {artefact.code for artefact in artefacts}
    for example in load_examples(CONTENT_DIR):
        if example.front.kind == "MODEL":
            assert example.front.figure and (ARCHIMATE_STATIC / example.front.figure).is_file(), example.id
            assert example.front.viewpoint, example.id
        for code in example.front.artefacts:
            assert code in codes, f"{example.id}: artefact {code} is not in artefacts.yaml"


# ---------------------------------------------------------------- pages
def test_adm_explorer_shows_the_crosswalk(client) -> None:
    page = client.get("/adm").text
    assert 'data-testid="crosswalk-table"' in page and "Crosswalk" in page
    phase = client.get("/adm/A").text
    assert 'data-testid="crosswalk"' in phase
    assert "Business Attributes Profile".lower() in phase.lower() or "business attributes profile" in phase.lower()
    assert "Motivation" in phase and "Contextual" in phase
    panel = get(client, "/adm-panel/A", htmx=True).text
    assert "In the other frameworks" in panel


def test_artefact_catalogue_shows_archimate_column_and_views(client) -> None:
    page = client.get("/artefact").text
    assert "<th>ArchiMate</th>" in page
    assert 'data-testid="archimate-STAKEHOLDER_MAP_MATRIX"' in page and "Stakeholder" in page
    filtered = get(client, "/artefact?archimate=1", htmx=True).text
    assert 'id="artefact-table"' in filtered and "38 artefacts" in filtered
    fragment = get(client, "/artefact/STAKEHOLDER_MAP_MATRIX/example", htmx=True).text
    assert 'data-testid="archimate-mapping"' in fragment and "viewpoint" in fragment
    assert 'href="/source/ARCHIMATE%20%C2%A7C.2"' in fragment
    if (ARCHIMATE_STATIC / "STAKEHOLDER_MAP_MATRIX.svg").is_file():
        assert 'data-testid="archimate-view"' in fragment and 'data-testid="tab-archimate"' in fragment
        assert client.get("/static/archimate/STAKEHOLDER_MAP_MATRIX.svg").status_code == 200


def test_notation_sampler_is_served(client) -> None:
    response = client.get("/static/archimate/notation_sampler.svg")
    assert response.status_code == 200 and "<svg" in response.text
    assert "Business Actor" in response.text and "specialization" in response.text


def test_worked_examples_filter_by_track(client) -> None:
    page = client.get("/example").text
    assert 'data-testid="track-filter"' in page and "drawn in ArchiMate" in page
    for track in ("TOGAF", "ARCHIMATE", "SABSA"):
        response = client.get(f"/example?track={track}")
        assert response.status_code == 200
    assert client.get("/example?track=NOPE").status_code == 404
    connection = connect()
    model = connection.execute("SELECT id FROM example_document WHERE kind = 'MODEL' ORDER BY ordinal LIMIT 1").fetchone()
    if model is not None:
        detail = client.get(f"/example/{model['id']}").text
        assert 'data-testid="model-figure"' in detail and "/static/archimate/" in detail
        assert "TOGAF artefacts realised" in detail or "The same thing in the other frameworks" in detail


def test_glossary_filters_by_track(client) -> None:
    page = client.get("/glossary").text
    assert 'data-testid="track-filter"' in page
    for track in ("TOGAF", "ARCHIMATE", "SABSA"):
        response = client.get(f"/glossary?track={track}")
        assert response.status_code == 200
        assert re.search(rf"{track.capitalize()} \(\d+\)", response.text)
    assert client.get("/glossary?track=NOPE").status_code == 404
    fragment = get(client, "/glossary?q=&track=TOGAF", htmx=True).text
    assert 'id="term-list"' in fragment


def test_practice_offers_every_exam_and_mocks_by_code(client) -> None:
    page = client.get("/practice").text
    for code in ("OGEA-101", "OGEA-102", "OGA-031", "OGA-032", "SCF"):
        assert f'value="{code}"' in page, code
    assert 'value="MOCK"' in page
    assert client.get("/practice?exam=SCF&mode=MOCK").status_code == 200
    assert client.get("/practice?exam=NOPE").status_code == 404


def test_unit_list_groups_all_four_tracks(client) -> None:
    page = client.get("/unit").text
    for unit in ("A1", "A9", "S1", "S7", "X1", "X3"):
        assert f'href="/unit/{unit}"' in page, unit
    assert client.get("/unit/A7").status_code == 200 and client.get("/unit/X2").status_code == 200
