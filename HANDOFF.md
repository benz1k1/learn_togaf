# Handoff — content authoring from the real source store (2026-09-11; three-framework pass 2026-09-25)

The crawl is done: 33 documents, 2,100 sections, 295 figures, all 58 objectives mapped
(`resources/sources/`, index in `resources/learn_togaf.db`). Content is being authored IN
SESSION by Claude (no Anthropic key needed), grounded on the section text, following the
same grounding rules as `generate.py` (learn_togaf.md §1.3, §1.5).

## Status per unit

| Unit(s) | Status |
|---|---|
| F1–F3 | DONE 2026-09-11: 10 lessons, 176 questions (f1.yaml, f2.yaml, f3.yaml) |
| F4 | DONE 2026-09-11: 11 lessons, 129 questions (f4.yaml), phases.yaml corrected from the standard |
| F5–F6 | DONE 2026-09-11: 10 lessons, 153 questions (f5.yaml, f6.yaml), techniques.yaml corrected |
| F7–F8 | NOT started |
| Glossary (INTRO §4) + `content/adm/artefacts.yaml` from CONTENT ch. 3–4 | NOT started |
| P1–P4 scenarios + guide lessons G1–G4 | NOT started |
| P5–P9 scenarios + guide lessons G5–G8 | NOT started |
| Worked examples (`content/examples/`, page `/example`) | DONE 2026-09-24: 26 documents, every CONTENT Table 4-1 deliverable + Business Scenario + ACMM scorecard, one enterprise (Northgate Bank) through all phases |
| A1–A9 ArchiMate (OGA-031 bank, OGA-032 scenarios) | DONE 2026-09-25: 33 lessons, 449 single-answer questions (≥ 10 per objective), 24 scenarios; grounded on the crawled specification (ARCHIMATE, 287 sections, 117 figures) |
| S1–S7 SABSA (SCF bank) | DONE 2026-09-25: 22 lessons, 480 questions; written from recollection of the framework — SABSA §n refs are placeholders until `sources.py pdf` registers the White Paper; the open factual checks are listed in learn_sabsa_archimate.md (status header) |
| X1–X3 crosswalk units | DONE 2026-09-25: 6 lessons, no bank; `content/adm/crosswalk.yaml` drives the /adm panels |
| ArchiMate views (`content/archimate/`, `/artefact` Example panel, `/example?track=ARCHIMATE`) | DONE 2026-09-25: 27 Northgate Bank views + the notation sampler, one MODEL worked example each (27–38, 41–55) |
| SABSA worked examples (`/example?track=SABSA`) | DONE 2026-09-25: 10 documents (60–69): contextual/conceptual cells, Business Attributes Profile, risk assessment, domain and trust model, services, mechanisms, control gaps, service management, traceability matrix |
| Glossary | 113 terms (47 TOGAF + 46 ArchiMate + 19 SABSA + `architecture_domain`), confusables linked across frameworks (§3.4) |

Check what landed: `ls content/lessons/*/ content/questions/*/` and
`cd api && LEARN_TOGAF_ENV=dev PYTHONPATH=src .venv/bin/python -m pytest tests/test_content.py -q`.

## The brief to give each authoring agent (reuse verbatim, change the unit list)

Read CLAUDE.md; learn_togaf.md §0, §1.3 (ORIGINAL PARAPHRASE ONLY, every item cites its
section), §1.5, §2, §6 (≥ 10–12 questions per objective; unit total ≥ 10 × blueprint weight);
content/blueprint.yaml; the existing lessons and content/questions/foundation/starter.yaml
(exact YAML shape; starter ids <UNIT>-001… are taken — new ids start at <UNIT>-101);
api/src/learn_togaf/content/models.py (validators). Sections for an objective:

```
cd /home/benz3k3/workspace/benz3k3/learn_togaf && LEARN_TOGAF_ENV=dev api/.venv/bin/python - <<'PY'
import sys; sys.path.insert(0,"api/src")
from learn_togaf.db import connect
c = connect()
for r in c.execute("SELECT s.id, s.heading_path, s.document_code, s.text FROM objective_source o JOIN source_section s ON s.id=o.section_id WHERE o.objective_code=? ORDER BY s.ordinal", ("7.1",)):
    print("\n####", r["id"], "|", r["heading_path"], "\n", r["text"][:8000])
PY
```

Refs are "<DOC> §<heading number>" ("CONTENT §3.4", "GUIDE:business-scenarios §2.1") and
every ref must resolve via `learn_togaf.sources.index.resolve_ref(connection, ref)`.
Lessons: `content/lessons/<UNIT>/<nn>_<slug>.md` numbered with the next free number, front matter as the
examples, `source: authored`, `status: draft`, tables + trap callouts, a ref per paragraph.
Questions: `content/questions/foundation/<unit>.yaml` (code <UNIT>_BANK, exam FOUNDATION,
kind DRILL; every question carries `lesson: <lesson id>` naming the ONE lesson that teaches
it — a lesson of the same unit carrying the question's objective — because check-yourself shows
each question in exactly one lesson) or `content/questions/practitioner/<unit>.yaml` (exam PRACTITIONER; scenario
600–900 words, four answers with points exactly 5/3/1/0, a `why` per answer, `open_book_hint`,
≥ 5 per Practitioner unit). Validate with tests/test_content.py. New or edited files show in the app only after a reload:
`python start.py --load-content` (restarts the server) or, with the server up, run the loader
in-process (see CLAUDE.md, "Commands"). Do not touch other units.

## 10th Edition chapter map (the mapping already encodes it)

INTRO 1 Introduction, 2 Documentation Set, 3 Core Concepts, 4 Definitions. ADM 2 Preliminary,
3 A, 4 B, 5–7 C (Data, Application), 8 D, 9 E, 10 F, 11 G, 12 H, 13 Requirements Management.
TECH 2 Principles, 3 Stakeholder Management, 4 Patterns, 5 Gap Analysis, 6 Interoperability,
7 Readiness, 8 Risk, 9 Alternatives and Trade-Offs. APPLY 2 Iteration, 3 Landscape,
4 Partitioning. CONTENT 2 Content Framework/Metamodel, 3 Artifacts, 4 Deliverables,
5 Building Blocks, 6 Enterprise Continuum, 7 Repository. GOV 2 Establishing a Capability,
3 Governance, 4 Architecture Board, 5 Contracts, 6 Compliance. Business scenarios, capability
planning, security, agile, maturity models and the skills framework are Series Guides
(`GUIDE:<slug>`, see `resources/sources/objective_sections.yaml`).

## After authoring

Review drafts on `/review-queue` or flip `status: reviewed` by hand; mocks draw reviewed
items only. `tests/test_bank_targets.py` is the §6 gate. Open items: the ADM diff
(`content/review/adm_phases.parsed.yaml`) misses inputs, Phase C sub-chapters and chapter 13;
no PDFs under `resources/sources/pdf/`; generation via the API needs `anthropic.api_key`.

## The three-framework pass (2026-09-25)

Exams are data now (`blueprint.exams`, five codes) and question sets live in
`content/questions/<exam code>/` — see CLAUDE.md. Everything authored on 2026-09-25 is
`status: draft`. Next steps, in order: (1) register the SABSA White Paper and W117/W14C/W172
under `resources/sources/pdf/` (`sources.py pdf && sources.py index`), then re-point the
`SABSA §n` / `WP:… §n` placeholder refs and settle the Business Attributes Profile cell
(learn_sabsa_archimate.md status header); (2) map the S* objectives in
`resources/sources/objective_sections.yaml`; (3) review the banks on /review-queue or flip
`status: reviewed` so `tests/test_bank_targets.py` (the per-exam gate) can pass; (4) fill the
`lessons:` links in `content/adm/crosswalk.yaml` now that A9/03, X1/01, X2/01, S6/03 exist.
