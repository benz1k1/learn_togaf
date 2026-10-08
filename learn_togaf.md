# Learn TOGAF — project plan

A single-user study application for the **TOGAF® Standard, 10th Edition** certification exams:
**TOGAF Enterprise Architecture Foundation** (Part 1, OGEA-101) and **TOGAF Enterprise
Architecture Practitioner** (Part 2, OGEA-102), or the combined **OGEA-103**. Python + htmx, no
build step, runs on a laptop from one command. The goal is not to be a pretty reader; it is to
get one person through both exams, which means it has to carry **the whole syllabus**, drill it
the way the exams ask it, and tell the learner honestly when they are not ready.

Every lesson, glossary entry, flashcard, figure and practice question is **generated from the
official TOGAF publications** — the Digital Edition HTML at `pubs.opengroup.org` and the
licensed PDFs — fetched with the learner's own Open Group account, indexed by section, with the
diagrams downloaded (§1.4), and then reviewed before it counts (§1.5). Nothing is written from
memory, and every generated item cites the section it came from.

Sibling of `loylty_program/` and `learn_chinese/`; same conventions (§10). This document is the
plan. **Status (2026-09-10):** the skeleton, content loader, all pages (§4), the practice engine,
flashcards, import wizard, review queue, coverage page, `sources.py` and `generate.py` are built and
tested (`api/tests`, 117 live-server tests). Not yet done: a real crawl of the Digital Edition (needs
the learner's Open Group login), the generated content, and the §6 bank targets — `test_bank_targets.py`
fails until they are met. See `README.md` for the first run and `CLAUDE.md` for the module contract.

---

## 0. The exams, precisely

Everything in the app is shaped by how the two exams actually work. Verify the numbers below
against the current *Conformance Requirements* documents on The Open Group site before authoring
the question bank, and keep them in `resources/blueprint.yaml`, not in code.

| | Part 1 — Foundation (OGEA-101) | Part 2 — Practitioner (OGEA-102) |
|---|---|---|
| Format | 40 multiple-choice questions, one correct answer of four | 8 complex scenario questions, four answers each |
| Time | 60 minutes | 90 minutes |
| Scoring | 1 point each; pass at **60% = 24 / 40** | **gradient**: best answer 5, second 3, third 1, distractor 0; pass at **60% = 24 / 40** |
| Book | closed | **open book** — the TOGAF Standard is available in the exam; the skill is knowing *where* to look and *what* the answer must reference |
| Tests | knowledge and comprehension of the standard's terms, structure, ADM phases, techniques, content framework, capability and governance | applying the ADM and the Series Guides to a situation: choosing the right technique, artefact, stakeholder action, governance step, in the right phase, for the right reason |
| Combined | OGEA-103 sits both back to back (150 minutes); Part 2 is only marked if Part 1 is passed | |

**Part 1 blueprint** (questions per learning unit; confirm against the conformance document):

| Unit | Learning unit | Questions |
|---|---|---|
| 1 | Concepts | 3 |
| 2 | Definitions | 3 |
| 3 | Introduction to the ADM | 3 |
| 4 | ADM Phases | 9 |
| 5 | ADM Techniques | 6 |
| 6 | Applying the ADM | 4 |
| 7 | Architecture Content Framework | 5 |
| 8 | Enterprise Architecture Capability and Governance | 7 |
| | | **40** |

**Part 2 blueprint**: eight scenarios drawn across the Practitioner learning units — Context for
EA, Stakeholder Management, Architecture Vision and Phase A, Architecture Development (B, C, D),
Implementing the Architecture (E, F, G), Architecture Change Management (H), Requirements
Management, and Supporting the ADM Work (the Series Guides: business scenarios, capabilities,
value streams, information and organization maps, risk and security, agile, digital). The exact
per-unit counts are in the conformance document and go into `blueprint.yaml`.

What that means for the app: Part 1 drilling is **recall at speed** (definitions, phase
objectives, inputs and outputs, which technique belongs where), and Part 2 drilling is **ranked
judgement** with the book open — so the practitioner mode must reproduce the 5/3/1/0 scoring,
show *why* the second-best answer is second-best, and let the learner search the reference
while answering.

---

## 1. Syllabus coverage — what "complete" means

The 10th Edition is a set of documents, not one book. The app's content tree mirrors it so a
learner can always answer "where in the standard is this", which is exactly the Part 2 skill.

### 1.1 The TOGAF Fundamental Content (both exams)

| Document | Chapters the app must carry | Exam weight |
|---|---|---|
| **Introduction and Core Concepts** | what enterprise architecture is; the TOGAF document set; architecture domains (BDAT); ADM overview; deliverables, artefacts, building blocks; Enterprise Continuum; Architecture Repository; EA Capability; every term in the *Definitions* chapter | Part 1 units 1–3 |
| **Architecture Development Method** | Preliminary; Phases A–H; Requirements Management — for each: objectives, approach, inputs, steps, outputs; iteration and the ADM cycle | Part 1 unit 4 (9 of 40); Part 2 throughout |
| **ADM Techniques** | Architecture Principles; Stakeholder Management (stakeholder map, power/interest grid); Architecture Patterns; Business Scenarios (overview here, guide below); Gap Analysis; Migration Planning techniques (Implementation Factor catalog, Consolidated Gaps/Solutions/Dependencies matrix, Architecture Definition Increments table, Transition Architecture State Evolution table, Business Value Assessment); Interoperability Requirements; Business Transformation Readiness Assessment; Risk Management; Capability-Based Planning | Part 1 unit 5; Part 2 |
| **Applying the ADM** | Architecture iteration (Architecture Capability, Development, Transition Planning, Governance iterations); applying the ADM across the Architecture Landscape (strategic, segment, capability levels); Architecture Partitioning; Security in the ADM (summary); using the ADM with agile | Part 1 unit 6; Part 2 |
| **Architecture Content** | Content Framework and metamodel (core and extensions); deliverables, artefacts (catalogs, matrices, diagrams) **per phase**; building blocks (ABB, SBB); Architecture Repository (Architecture Landscape, Reference Library, Standards Library, Governance Repository, Architecture Requirements Repository, Solutions Landscape, Architecture Capability); Enterprise Continuum and Architecture/Solutions Continuum | Part 1 unit 7; Part 2 |
| **EA Capability and Governance** | establishing an Architecture Capability; Architecture Board; Architecture Governance framework (conceptual and organisational); Architecture Compliance (reviews, checklists); Architecture Contracts; Architecture Maturity Models; Architecture Skills Framework | Part 1 unit 8 (7 of 40); Part 2 |

### 1.2 The TOGAF Series Guides (Practitioner)

Practitioner scenarios reach into the guides; a learner who knows only the Fundamental Content
loses the "which guide would you apply" questions. Each guide gets a unit with a summary lesson
and scenario-style questions.

- The TOGAF Leader's Guide to Establishing and Evolving an EA Capability
- A Practitioners' Approach to Developing Enterprise Architecture Following the TOGAF ADM
- Business Scenarios
- Business Capabilities · Value Streams · Information Mapping · Organization Mapping
- Business Models
- Digital Business Reference Model · Digital Technology Adoption · The TOGAF Standard and Digital
- Enterprise Agility · Using the TOGAF Standard in the Digital Enterprise · Applying the ADM in an agile sprint context
- Integrating Risk and Security within a TOGAF Enterprise Architecture · Security Architecture
- Architecture Project Management
- Architecture Maturity Models · Architecture Skills Framework
- Architecture Partitioning · Architecture Repository patterns
- Government Reference Model; the TRM and III-RM (reference models)
- Microservices Architecture; SOA reference (as far as the conformance document lists them)

Coverage is tracked, not assumed: every lesson, glossary term and question carries the
learning-unit and objective codes from the conformance documents, and the coverage page (§4.9)
shows which objectives have no lesson, no flashcards or fewer than *n* questions.

### 1.3 Copyright — what the app may and may not contain

The TOGAF Standard is copyright The Open Group; the official practice exams ship only with the
Open Group's own self-study materials. So:

- **Lessons are original paraphrase and structure**, written for recall — never reproduced text.
  Quotations are short and attributed with the document and section.
- **The question bank is authored here**, in the exam's shape, by us. The app ships with its own
  sets and **imports** others (§4.7) — the learner's own, published sample questions they have
  rights to use, or a purchased set they own. The app never bundles a third-party bank.
- Section references point *into* the standard ("ADM, Phase B, step 4") so the learner uses
  their own licensed copy in open-book practice. The app keeps a **local, private** copy of the
  fetched publications for the one account that fetched them (§1.4) — gitignored, never
  packaged, never served to anyone else — and shows the standard's own figures only from that
  local store.

### 1.4 Sources — the official HTML publication and the PDFs

The syllabus above is not authored from memory. It is derived from the publications themselves,
which the learner has a licence to read, fetched once into a local source store and indexed by
document, chapter, section and figure. Everything downstream — lessons, glossary, ADM explorer,
flashcards, the question bank — is generated from that index and cites it.

**Official entry points** (verified 2026-09-10; the HTML publication is behind The Open Group's
free single sign-on, so every fetch runs with the learner's own account):

| Source | URL | Access |
|---|---|---|
| TOGAF Standard, 10th Edition — Digital Edition (HTML) | `https://pubs.opengroup.org/togaf-standard/` — index; the six documents under it, e.g. `…/togaf-standard/adm/index.html`, `…/introduction/`, `…/adm-techniques/`, `…/applying-the-adm/`, `…/architecture-content/`, `…/ea-capability-and-governance/`; the Series Guides under `…/togaf-standard/guides/` | Open Group account login (redirects to `identity.opengroup.org`); free registration |
| TOGAF Standard, 10th Edition — publication page and PDF | `https://publications.opengroup.org/c220` | licensed PDF download, personal use |
| TOGAF Series Guides — listing | `https://publications.opengroup.org/guides/togaf` | each guide has its own G-number page and PDF |
| TOGAF Library | `https://publications.opengroup.org/togaf-library` | white papers and reference material, optional |
| Licensed downloads | `https://www.opengroup.org/togaf-licensed-downloads` | the PDF bundle, under the personal-use licence |
| Certification, conformance requirements, exam datasheets | `https://www.opengroup.org/certifications/togaf-certification-portfolio` (and the OGEA-101 / OGEA-102 / OGEA-103 pages linked from it) | public; the conformance documents are what `blueprint.yaml` is transcribed from |
| Self-study materials (official Study Guides, practice tests) | `https://shop.opengroup.org/study-materials/togaf` | purchase; imported through §4.7 if owned, never bundled |

The exact page slugs inside the Digital Edition are **discovered by crawling the index after
login**, not hardcoded: `resources/sources/manifest.yaml` is written by the first crawl and
checked in with URLs, titles and content hashes only — no text.

**The source store** — `resources/sources/` (gitignored except `manifest.yaml`):

```
resources/sources/
  manifest.yaml                 # document → pages → sections → figures; hashes; fetched_at; licence note
  html/<doc>/<page>.html        # the Digital Edition pages as fetched
  pdf/<doc>.pdf                 # the licensed PDFs the learner places here (C220, the guides' G-numbers)
  figures/<doc>/<figure_id>.<ext>   # every diagram, downloaded — see below
  text/<doc>/<section_id>.md    # extracted section text, one file per section, with heading path
```

**Fetching.** `python sources.py login` opens the Open Group login in Playwright once and stores
the session cookie locally; `python sources.py fetch` crawls the index with that session over
`httpx`, saving every page, following only `pubs.opengroup.org/togaf-standard/**`, politely (one
request at a time, a delay, a `User-Agent` naming the tool and the account). `python sources.py
pdf` registers the PDFs placed under `pdf/` (the tool does not download purchases). Re-running
fetches only pages whose `ETag` or hash changed.

**Parsing.** HTML: `selectolax` walks each page into a heading tree; every `h1`–`h4` with its
anchor becomes a `source_section` with the document code, the numbered heading path
("ADM › 6. Phase A › 6.3 Inputs"), the anchor URL and the extracted text. PDF: `pymupdf`
extracts text by page with the heading outline (bookmarks) mapped onto the same section ids, so
a section knows both its HTML anchor and its PDF page — the open-book panel offers either.
Tables are kept as Markdown tables; the ADM phase chapters' *inputs / steps / outputs* lists
are additionally parsed into `adm/phases.yaml` (§2) rather than typed by hand, and diffed on
every re-fetch so a changed step is noticed.

**Figures and diagrams are downloaded, all of them.** The standard is taught through its
diagrams — the ADM cycle, the Content Metamodel, the Architecture Repository, the Enterprise
Continuum, the stakeholder power/interest grid, the Governance framework, the Capability-Based
Planning figure, the migration-planning tables — and the exams reproduce them ("which phase is
highlighted", "what does this box in the metamodel contain"). So the crawl saves every `<img>`
in a `figure` context (and every image the PDF pages carry, extracted at native resolution
with `pymupdf`), with its caption ("Figure 6-1: Phase A") and the section it sits in, into
`figures/` and `source_figure`. A figure is then:

- shown on the lesson and the ADM explorer page it belongs to, served from the local store only;
- the subject of **figure questions** — "identify the phase", "name the missing element", "which
  repository part holds X" — generated with the image sent to the model (§1.5) and rendered in
  the quiz from the local file;
- a flashcard kind of its own (`FIGURE`: front is the diagram with a label blanked, back the
  label);
- listed on the coverage page, so a figure with no lesson and no question is a visible gap.

The important ones get a hand-kept `figures/important.yaml` (id, why it matters, which
objectives it serves) so the study plan schedules them explicitly; the rest are still stored
and searchable.

**Licence.** The fetched text, PDFs and figures are the learner's personal copy under The Open
Group's terms. They live only under `resources/sources/`, which is gitignored, excluded from the
wheel and the state export, and served by the app only on `127.0.0.1` to the account that
fetched them. The generated lessons and questions are original work that cites sections; the
figures are shown, never redistributed.

### 1.5 Generation — lessons, glossary, cards and the question bank from the sources

Generation is a pipeline over `source_section` and `source_figure`, run by the author from the
command line, writing **draft** files into `content/` that the loader validates like any other
and the app marks *draft* until reviewed. It calls Claude through the official Python SDK
(`anthropic`), model `claude-opus-5`, adaptive thinking, streaming for long outputs, prompt
caching on the section text, and the Batches API for the bank (half price, no latency need).

| Stage | Input | Output | Grounding rule |
|---|---|---|---|
| `generate lessons <unit>` | the sections mapped to the unit's objectives (from `blueprint.yaml` × `manifest.yaml`), plus their figures | one lesson per objective group: original paraphrase, "check yourself" stubs, `refs[]` | the model receives only the cited sections; every paragraph ends with a section id; a lesson citing a section outside its input is rejected |
| `generate glossary` | the Definitions chapter and every section that defines a term | `glossary.yaml`: paraphrased definition, document, section, `confusable_with[]` | definition must be traceable to one section; the source sentence is stored beside it for review, not shipped |
| `generate adm` | the ADM phase chapters and the techniques document | `adm/phases.yaml`, `techniques.yaml`, `artefacts.yaml` | parsed lists, not prose; the model only fills `exam traps` and cross-references |
| `generate questions foundation <unit>` | a section (or a section + figure), the unit's objective, the blueprint weight, the questions already in the bank for that objective | 4-option MCQs with explanation naming each distractor's error, `refs[]`, difficulty | structured output (`output_config.format` with the §2 schema); exactly one correct option; the **correct option must be entailed by the cited section text** — checked in the next stage |
| `generate questions practitioner <unit>` | 3–6 sections across documents and guides, the objective, a scenario brief (industry, size, stage) | scenario + four ranked answers with `why` per answer, `refs[]`, `open_book_hint` | the 5-point answer must be justified from the cited sections; the 3 and 1 are near-misses that violate one cited statement each; the 0 contradicts one |
| `generate figure-questions` | a figure with its caption and section | identify / missing-element / which-part questions | the figure image is sent as a document block; answers must appear in the figure's caption or section text |
| `verify` | every generated item + its cited sections | pass / fail with a reason | a second call, as an independent judge, answers: is the correct answer supported by these sections, and is each distractor actually wrong? Fails go to `review/`, never into a mock |
| `review` (human) | the draft and the verifier's note | `status: reviewed` in the file's front matter | the author reads it against the section; the app draws mocks from reviewed items only; drills may include drafts with a badge |

Two rules keep the bank honest. **Nothing is generated without a section id in hand** — the
pipeline refuses a unit whose objectives have no mapped sections, which is also how a coverage
gap surfaces before a question is written. **Nothing reaches a mock without passing `verify`
and a human review**, and the coverage page counts reviewed items only.

Costs are small and cached: a section is sent once per stage with a cache breakpoint, the
question stages run in batches, and a full regeneration of the Foundation bank is a few hundred
calls. Model, effort and batch size are settings in the env YAML through `_require()`, so a
different model is a config change.

---

## 2. Content model

Content is **files, not rows**: Markdown lessons and YAML question sets under `content/`, loaded
into SQLite at start-up and on demand. Authoring is a text editor; the database is a cache of
the files plus the learner's own state (attempts, reviews, notes), and only that state is ever
worth backing up.

```
content/
  blueprint.yaml                 # exam formats, unit weights, pass marks (§0)
  units/
    F1_concepts.md ... F8_capability_governance.md      # Foundation learning units
    P1_context.md ... P9_supporting_the_adm.md          # Practitioner learning units
    G_*.md                                              # one per Series Guide
  lessons/<unit>/<nn>_<slug>.md   # front matter: unit, objectives[], refs[], reading_minutes
  adm/
    phases.yaml                   # Preliminary, A–H, Requirements Mgmt: objective, approach, inputs, steps, outputs, artefacts, deliverables
    techniques.yaml               # each technique: purpose, phase(s) used, artefacts produced, exam traps
    artefacts.yaml                # every catalog / matrix / diagram: phase, domain, purpose
  glossary.yaml                   # every defined term: definition (paraphrase), document, section, confusable_with[]
  examples/<nn>_<slug>.md         # worked example documents: every deliverable of CONTENT ch. 4 written out for one fictional enterprise (§4.3)
  questions/
    foundation/<set>.yaml         # Part 1 shape
    practitioner/<set>.yaml       # Part 2 shape, gradient answers
    figures/<set>.yaml            # §1.4 figure questions; the image is referenced by figure id
    imported/                     # what the learner loads (§4.7), never committed
  review/                       # generated drafts that failed `verify` or await review (§1.5)
```

Every generated file carries `source: generated`, `status: draft | reviewed`, `model`, `generated_at`
and the `refs[]` it was grounded on, in its front matter or per item. Hand-written files carry
`source: authored`. Both go through the same validators.

**A Foundation question** (`questions/foundation/*.yaml`):

```yaml
- id: F4-017
  unit: F4                       # ADM Phases
  objective: "4.3"               # objective code from the conformance document
  lesson: F4/04_phase_a_architecture_vision   # the ONE lesson whose "check yourself" asks it (§4.2)
  stem: "Which of the following is an output of Phase A?"
  options:
    - {key: A, text: "Architecture Definition Document"}
    - {key: B, text: "Approved Statement of Architecture Work", correct: true}
    - {key: C, text: "Implementation and Migration Plan"}
    - {key: D, text: "Architecture Contract"}
  explanation: "…why B, and what phase each distractor belongs to…"
  refs: ["ADM §6.5"]             # a source_section id (§1.4); the loader rejects unknown refs
  figure: null                   # or a source_figure id for figure questions
  difficulty: 2                  # 1–3
  tags: [outputs, phase-a]
  source: generated              # generated | authored | imported
  status: reviewed               # draft until a human review (§1.5)
```

**A Practitioner question** (`questions/practitioner/*.yaml`) — one scenario, four ranked
answers, each with the reason it earns what it earns:

```yaml
- id: P3-004
  unit: P3                       # Architecture Vision / Phase A
  objective: "3.2"
  lesson: P3/01_phase_a_in_practice
  scenario: |
    …600–900 words: the enterprise, the sponsor, the situation, the constraints,
    what has been done, what is being asked…
  question: "Refer to the scenario. You have been asked to recommend an approach. Based on the TOGAF Standard, which of the following is the best answer?"
  answers:
    - {key: A, points: 5, text: "…", why: "…names the technique, the phase and the stakeholder concern the scenario planted…"}
    - {key: B, points: 3, text: "…", why: "…right technique, wrong sequence…"}
    - {key: C, points: 1, text: "…", why: "…plausible but skips governance…"}
    - {key: D, points: 0, text: "…", why: "…the distractor, and the misconception it tests…"}
  refs: ["ADM §6", "Series Guide: Business Scenarios §3"]
  open_book_hint: "Where to look: …"
```

Loading validates every file with Pydantic v2: exactly one correct option on Foundation
questions; points exactly `{5, 3, 1, 0}` on Practitioner ones; every `unit` and `objective` in
the blueprint; every `ref` in a known-document form. A file that fails validation fails the
load, with the file and the id — never a partially loaded bank.

---

## 3. Data model (SQLite)

Two kinds of table, kept apart: **content cache** (rebuilt from files, never edited in the DB)
and **learner state** (the only thing the learner owns).

```sql
-- source index (§1.4) — rebuilt from resources/sources/, text never leaves the machine
source_document(code PK, title, kind, html_url, pdf_path, fetched_at, content_hash)         -- kind: STANDARD | GUIDE | CONFORMANCE
source_section(id PK, document_code, heading_path, anchor_url, pdf_page, ordinal, text, content_hash)
source_figure(id PK, document_code, section_id, caption, file_path, width, height, important, content_hash)
objective_source(objective_code, section_id)                 -- the mapping generation runs on

-- content cache
learning_unit(code PK, exam, name, ordinal, weight)          -- F1..F8, P1..P9, G_*
objective(code PK, unit_code, text)
lesson(id PK, unit_code, slug, title, body_md, reading_minutes, ordinal)
lesson_objective(lesson_id, objective_code)
glossary_term(id PK, term, definition, document, section, confusable_with)
adm_phase(code PK, name, objective, approach, inputs, steps, outputs, ordinal)  -- JSON columns
adm_technique(code PK, name, purpose, phases, artefacts, traps)
adm_artefact(code PK, name, kind, phase_code, domain, purpose)                  -- CATALOG | MATRIX | DIAGRAM
question(id PK, exam, unit_code, objective_code, set_code, source, status, figure_id, stem_or_scenario,
         question_text, explanation, refs, difficulty, tags, content_hash, verified_at, reviewed_at)
question_option(question_id, key, text, points, why, ordinal)                   -- Foundation: points 1/0
question_set(code PK, exam, name, source, kind, question_count)                 -- kind: DRILL | MOCK | IMPORTED

-- learner state
attempt(id PK, exam, mode, set_code, started_at, finished_at, time_limit_s, score, max_score, passed)
attempt_answer(attempt_id, question_id, chosen_key, points, answered_at, flagged, seconds)
card_review(id PK, card_kind, card_ref, due_at, interval_days, ease, reps, lapses, last_grade)   -- SM-2 state; card_kind: TERM | PHASE_IO | TECHNIQUE | ARTEFACT | FIGURE | QUESTION
note(id PK, ref_kind, ref_id, body_md, updated_at)
study_session(id PK, started_at, ended_at, lessons_read, cards_reviewed, questions_answered)
```

`content_hash` on `question` is how imports dedupe (§4.7) and how a re-load knows a file changed.
The learner state references content by stable ids (`F4-017`, `ADM.B`, glossary term id), so a
content reload never orphans a review or an attempt.

---

## 4. Features

Ordered by how directly each one moves a learner toward a pass.

### 4.1 Dashboard — `/`

Readiness per exam and per learning unit: the estimated Part 1 score from the last 200 answered
Foundation questions weighted by the blueprint; the estimated Part 2 score from the last three
mocks; cards due today; the weakest three objectives with a one-click drill; the next lesson in
the study plan; days to the exam date the learner set. A single honest line at the top —
"Foundation: 31/40 on recent form, ready. Practitioner: 19/40, not yet." — is the product.

### 4.2 Lessons — `/unit/{code}`, `/lesson/{id}`

Rendered Markdown with the unit's objectives in the margin and the section references as
links to the glossary and the ADM explorer. Each lesson ends with "check yourself": five
questions from the bank mapped to that lesson, answered inline (htmx swap), which also
seeds flashcards for anything missed. Progress is per lesson (read, checked, mastered).

Every question belongs to exactly one lesson (`lesson_question`, rebuilt by the loader): the
question's `lesson:` field, or, when it is absent, the unit's lesson carrying the objective whose
`refs` cover the question's `refs` most specifically. A tie is reported at load and fails
`tests/test_content.py`; the author settles it with `lesson:`, code never guesses. A question
answered in any lesson check, right or wrong, is never offered by check-yourself again; drills
and mocks (§4.6) still draw from the whole bank.

### 4.3 ADM explorer — `/adm`, `/adm/{phase}`

The single most-tested structure in both exams, so it gets its own interactive page: the ADM
cycle as an SVG, one phase per click, and for each phase **objectives, approach, inputs, steps,
outputs, and the artefacts and deliverables produced**, side by side with the previous and
next phase so the hand-offs are visible, with the standard's own figures for that phase from
the local source store (§1.4) and a link to the section's HTML anchor and PDF page. A "quiz me on this phase" button drills inputs versus
outputs, which is where Part 1 loses most marks. The same page pattern serves the techniques
(`/adm/technique/{code}`: where it is used, what it produces) and the artefact catalogue
(`/artefact`: filter by phase, domain, kind).

**Worked examples — `/example`, `/example/{id}`.** The standard defines each deliverable by purpose
and a contents list but never shows one filled in, and the lessons could not either. `content/examples/`
holds every deliverable of the Content Framework's Table 4-1 (plus the Business Scenario and an ACMM
maturity scorecard) written out for one fictional enterprise — Northgate Bank, the retail bank the
artefact drawings already use — following one project from a Request for Architecture Work in the
Preliminary Phase round the cycle to a second request issued from Phase H. Each document follows its
defining section's contents list, opens with a "what to notice" callout naming the exam traps it
illustrates, and cites the sections it is grounded on (`refs`, resolved at load like a lesson's). The
list page groups them by producing phase; each phase page links its own. Notes attach with
`ref_kind = EXAMPLE`.

### 4.4 Glossary — `/glossary`

Every defined term, searchable, with the document and section it comes from and the terms it
is commonly confused with (artefact / deliverable / building block; Architecture Vision /
Architecture Definition Document; Enterprise Continuum / Architecture Repository). Each term is
a flashcard. Part 1 unit 2 is literally this page.

### 4.5 Flashcards — `/review`

SM-2 spaced repetition over six card kinds: glossary terms, phase inputs/outputs, technique →
phase, artefact → phase and kind, **figures** (a diagram with a label blanked), and previously
missed questions. Grades 0–5, due queue, daily
cap, keyboard-driven (1–5 to grade, space to flip), htmx swaps one card at a time. Cards are
generated from content, so a new lesson or term becomes cards without authoring them twice.

### 4.6 Practice — `/practice`

Three modes, all the same engine:

| Mode | What it is | Scoring |
|---|---|---|
| **Drill** | *n* questions from chosen units/objectives, untimed, explanation after each answer | per question |
| **Foundation mock** | 40 questions drawn by the blueprint weights, 60-minute clock, review only at the end, flag-for-review, exam-style navigation | 1 / 0, pass at 24 |
| **Practitioner mock** | 8 scenarios drawn across the Practitioner units, 90-minute clock, **open-book panel** (the section index of §1.4 searched by heading and text, with the HTML anchor and PDF page, plus the glossary, ADM explorer and artefact catalogue, the way the standard is available in the real exam), review at the end with all four answers explained | 5 / 3 / 1 / 0, pass at 24 |

Mock draws are seeded and recorded so a mock can be retaken identically or freshly. Timed modes
keep the clock server-side (an `attempt.started_at` plus limit), so a refresh does not reset it.
Review pages show per-objective breakdown, time per question, and "you changed a correct answer
to a wrong one" — the habit worth breaking.

### 4.7 Load practice questions — `/import`

The feature the user asked for by name: bring question sets into the bank from files, in this
app's YAML (§2) and in the shapes other sets commonly come in.

- **Formats.** The native YAML; CSV with a documented header
  (`id,exam,unit,objective,stem,option_a..d,correct,explanation,refs`) for Foundation;
  JSON arrays of either shape; a Markdown convention (`### Q`, `- [x] answer`) for hand-typed
  sets. Anything else is converted with a one-file adapter under `importers/`.
- **Wizard.** Upload → detect format → map columns (the mapping is saved per source) → validate
  with the same Pydantic models the loader uses → preview with the errors listed per row →
  confirm. Nothing lands in the bank before the confirm; a set with errors imports the valid
  rows only when the learner ticks "import what validates".
- **Dedupe and provenance.** `content_hash` over the normalised stem and options; a duplicate is
  reported, not re-imported. Every question keeps its `source` (file name, imported-at) and set
  code, so a source can be removed as a unit, and mocks can be limited to "our sets" or "all".
- **Unit mapping.** A set without unit codes is mapped by keyword to units and flagged
  *unverified* until the learner confirms it, so the blueprint weighting stays meaningful.
- **Not a scraper.** Files only, from disk. See §1.3.

### 4.8 Study plan — `/plan`

The learner sets an exam date; the app spreads the units over the days (Foundation units first,
weighted by blueprint, then Practitioner and the guides), places a mock every week, and keeps
the daily flashcard budget realistic. The plan re-flows when a day is missed. It is a schedule,
not a nag: one line on the dashboard.

### 4.9 Coverage and question quality — `/coverage`

For the author (the same person): objectives with no mapped source section (§1.4), no lesson,
no cards, or fewer than 8 Foundation / 2 Practitioner **reviewed** questions; figures with no
lesson and no question; drafts waiting in `review/`; questions everyone gets right (too easy) or that are
answered in under 5 seconds (guessable); Practitioner answers whose 3-point option is chosen
more often than the 5-point one across attempts (the "why" needs work). This page is how the
bank gets to "complete".

### 4.10 Notes and export

A note on any lesson, term, phase or question; export the learner state (attempts, reviews,
notes) as one JSON file and re-import it, so the SQLite file is never the only copy.

---

## 5. Architecture

```
learn_togaf/
  learn_togaf.md               # this plan
  start.py                     # uvicorn --reload on 5014; --load-content; --stop
  content/                     # §2 — the syllabus and the question bank (generated + authored)
  sources.py                   # §1.4: login | fetch | pdf | index | figures — the source store CLI
  generate.py                  # §1.5: lessons | glossary | adm | questions | figure-questions | verify
  resources/
    env/dev/.env               # YAML config (PROGRAM-style), not dotenv; anthropic model/effort/batch here
    sources/                   # §1.4 source store — gitignored except manifest.yaml
    learn_togaf.db             # SQLite; learner state lives here
  api/
    pyproject.toml             # uv; fastapi, jinja2, pydantic v2, pyyaml, markdown-it-py, loguru, orjson, polars,
                               # httpx, selectolax, pymupdf, playwright (login only), anthropic
    src/learn_togaf/
      config.py                # _require() over the env YAML; content dir, db path, port
      main.py                  # create_app(): routes, static, lifespan (open db, load content if empty)
      db.py                    # sqlite3 connection per request, WAL, foreign keys on, schema.sql applied at start
      sources/                 # §1.4: session.py (Playwright login → cookie), fetch.py (httpx crawl), parse_html.py,
                               # parse_pdf.py, figures.py, index.py (→ source_* tables), manifest.py
      generate/                # §1.5: client.py (anthropic, caching, batches), lessons.py, glossary.py, adm.py,
                               # questions.py, figure_questions.py, verify.py, prompts/ (one file per stage)
      content/                 # loader + validators: markdown, yaml → cache tables
        models.py              # Pydantic models for every file shape (§2)
        loader.py              # load_all(), reload_changed()
      importers/               # §4.7: yaml.py csv.py json.py markdown.py, one function each → list[Question]
      service/                 # one module per feature: lessons, adm, glossary, review (SM-2), practice, plan, coverage, notes
      pages/                   # controller per page + templates/ + static/ (htmx 2, Alpine 3, Tailwind, daisyUI, vendored)
    tests/                     # live-server pytest over httpx; Playwright for the practice flow
```

- **One process.** FastAPI serving htmx pages and a small `/api` used only by the pages (timer
  polling, review grading). No Celery, no Redis, no build step. SQLite in WAL mode.
- **Pages are the product.** Every screen is a Jinja template plus a controller; htmx swaps
  fragments (`_question.html`, `_card.html`, `_timer.html`); Alpine handles keyboard shortcuts
  and the flip animation. Charts are inline SVG or Chart.js vendored, as in `loylty_program`.
- **Content is loaded, not migrated.** `start.py --load-content` rebuilds the cache tables from
  `content/`; the app also reloads a changed file on request in dev. Learner state tables are
  never touched by a content load.
- **Single user, no auth.** It binds to `127.0.0.1` by default; a `bind` setting exists for a
  LAN. If it ever grows a second user, the learner-state tables get a `user_id` and Ten Tail
  JWT via `lr_lib`, the way the sibling repos do — not before.
- **Port 5014**, chosen against the workspace map (loylty_program 5012, clowreed 5000, ten_tail
  5002, rocket 5006, media_box 5007, MOS 5008).

### 5.1 Pages and routes

| Page | Route | Fragments |
|---|---|---|
| Dashboard | `/` | `_readiness.html`, `_due.html`, `_weakest.html` |
| Unit, lesson | `/unit/{code}`, `/lesson/{id}` | `_check_yourself.html` |
| ADM explorer | `/adm`, `/adm/{phase}`, `/adm/technique/{code}`, `/artefact` | `_phase_panel.html` |
| Worked examples | `/example`, `/example/{id}` | — |
| Glossary | `/glossary?q=` | `_term_list.html` |
| Review | `/review`, `POST /review/{card_id}/grade` | `_card.html` |
| Practice | `/practice`, `POST /practice` (new attempt), `/attempt/{id}`, `POST /attempt/{id}/answer`, `POST /attempt/{id}/finish`, `/attempt/{id}/review` | `_question.html`, `_scenario.html`, `_timer.html`, `_open_book.html` |
| Import | `/import`, `POST /import/preview`, `POST /import/confirm` | `_import_preview.html` |
| Plan | `/plan`, `POST /plan` | — |
| Coverage | `/coverage` | — |
| Sources | `/source`, `/source/{section_id}`, `/figure/{id}` | `_section.html`; local-store only, `127.0.0.1` |
| Review queue | `/review-queue`, `POST /review-queue/{id}/accept` | `_draft.html` |
| Notes, export | `POST /note`, `/export`, `POST /import/state` | `_note.html` |

REST paths singular; every page `POST` carries the CSRF token the way `loylty_program/pages`
does; the `/api` surface is the handful of JSON endpoints the timer and the grader need.

---

## 6. The question bank — targets

"Complete" is a number. The bank ships when it reaches these, by unit, tracked on `/coverage`:

| Exam | Target | Shape |
|---|---|---|
| Foundation | **≥ 400** questions: ≥ 10 per objective, unit totals ≥ 10× the blueprint weight (F4 ADM Phases ≥ 90, F8 ≥ 70) | so five mocks can be drawn with no repeats |
| Practitioner | **≥ 48** scenarios: ≥ 5 per learning unit, ≥ 1 per Series Guide named in the conformance document | six mocks of eight with no repeats |
| Flashcards | every glossary term; every phase's inputs and outputs; every technique; every artefact; every important figure | generated, not authored |
| Figures | every figure in the six core documents downloaded and indexed; every `important.yaml` figure with ≥ 1 lesson and ≥ 3 questions | from the source store |

All counts are of **reviewed** items (§1.5). Generation order follows the exam weight and the
failure pattern: Part 1 units 4 and 8 first
(16 of 40 marks), then 5 and 7, then 1–3 and 6; Practitioner scenarios per unit in the
blueprint order. Every question has an explanation that names the distractors' errors — a
question without one is not accepted by the loader.

---

## 7. Delivery phases

**Phase 0 — sources (1 week).** `sources.py`: login, crawl of the Digital Edition, PDF
registration, HTML and PDF parsing into the section index, **every figure downloaded** with its
caption and section, `manifest.yaml`, the objective → section mapping from the conformance
documents. Deliverable: `/source` shows every section and figure of the six core documents and
the in-scope guides, searchable, and the coverage page shows objectives with no mapped section.

**Phase 1 — skeleton and the syllabus (2 weeks).** `start.py`, config, SQLite schema, content
loader and validators, the unit and lesson pages, the glossary, the ADM explorer with phases,
techniques and artefacts **parsed from the sources** and their figures. `generate.py` for
lessons, glossary and adm; Foundation units 1–8 generated, verified and reviewed. Deliverable: a
learner can read the whole Foundation syllabus with the standard's diagrams and click through
the ADM.

**Phase 2 — drill and recall (2 weeks).** Flashcards with SM-2 over all six card kinds;
practice engine in drill mode; `generate questions foundation` and `verify` with the review
queue; Foundation bank to ≥ 200 reviewed, figure questions on every important figure; check-yourself on every lesson;
dashboard readiness for Part 1. Deliverable: Foundation mocks at the real format and clock.

**Phase 3 — Practitioner (3 weeks).** Practitioner and Series Guide lessons generated from the
guides; scenario generation and verification; gradient scoring; open-book side panel over the
section index; Practitioner mocks; Practitioner bank to ≥ 48 reviewed scenarios; review pages with "why the 3-point answer is not the 5". Deliverable: the
combined OGEA-103 rehearsal, both parts, 150 minutes, one report.

**Phase 4 — import, plan, coverage (1 week).** The import wizard with all four formats and the
dedupe; study plan; coverage page; state export/import. Deliverable: the learner can load a
purchased or hand-typed set and drill it alongside ours.

**Phase 5 — bank to target (ongoing).** Foundation to ≥ 400, Practitioner to the per-unit floor,
driven by the coverage page and by the learner's own weak-objective data.

**Phases 6–10 — ArchiMate and SABSA** are specified in `learn_sabsa_archimate.md` §4.8 and were
delivered 2026-09-25: exams as data (five exam codes in `blueprint.exams`), the ArchiMate crawl,
the A1–A9, S1–S7 and X1–X3 units, the crosswalk on the ADM explorer, ArchiMate views on the
artefact catalogue and the worked examples, and the 16-week braid as the study plan.

---

## 8. Testing

Tests live in `api/tests/`, drive a **running** server over `httpx` (never `TestClient`), and
`pytest.fail()` on unmet preconditions.

- **Source index**: the crawl is replayed against saved HTML fixtures (a few pages, our own
  fixture files, not the standard's text) and must produce the expected heading tree, anchors
  and figure list; every `refs[]` in `content/` resolves to a `source_section`; every figure
  referenced by a question exists in the store; `resources/sources/` is absent from the wheel.
- **Generation**: prompts are golden-tested against recorded responses (no live calls in the
  suite); the validators reject a generated question whose `refs` are outside its input
  sections; `verify` failures land in `review/` and never in a mock draw.
- **Content validity** is a test, not a hope: every file under `content/` loads; every question
  has exactly one correct option (Foundation) or points `{5,3,1,0}` (Practitioner); every unit
  and objective is in the blueprint; coverage floors (§6) are asserted per unit and fail the
  build when the bank is below target — the same gate pattern as `loylty_program`.
- **Practice engine**: a Foundation mock draws exactly the blueprint counts; the clock is
  server-side and survives a reload; scoring and pass marks match §0; Practitioner scoring is
  the gradient; a retake with the same seed draws the same questions.
- **SM-2**: interval and ease sequences for grades 0–5 match the reference algorithm.
- **Import**: each format round-trips; duplicates are reported not inserted; a broken row does
  not block valid ones only when the learner asked for that.
- **Pages** (Playwright): read a lesson, answer a check-yourself, run a 3-question drill, review
  five cards by keyboard, import a CSV.

---

## 9. Risks

| Risk | Mitigation |
|---|---|
| Copyright — reproducing the standard or an official practice test | §1.3–1.4: the fetched text and figures stay in the gitignored local store for the account that fetched them; lessons and questions are paraphrase with section refs; no bundled third-party banks; import is files-from-disk only |
| The Digital Edition changes its URLs or login flow | `manifest.yaml` is discovered by crawl, not hardcoded; the Playwright login is one small module; the PDFs are the fallback source for every section |
| Generated content drifts from the standard (plausible but wrong) | every item cites sections it was given; `verify` is an independent judge call; nothing reaches a mock unreviewed; the coverage page counts reviewed items only |
| Figures missed by the crawl (CSS backgrounds, SVG, PDF-only figures) | the PDF pass extracts page images too; the figure count per document is compared between HTML and PDF and a mismatch is listed on the coverage page |
| The bank tests our reading of the standard, not the exam's | Questions carry section refs; the coverage page flags questions with anomalous pass rates; the learner's real-mock results calibrate difficulty over time |
| Practitioner scenarios are hard to write well | A scenario template with the four-answer rationale mandatory; write the 5 and the 0 first, then the 3 and the 1 as deliberate near-misses of the 5 |
| Exam version drift (a new edition or a revised conformance document) | Blueprint, unit codes and weights in `blueprint.yaml`; content tagged by objective code, so a re-mapping is a file edit |
| Studying the app instead of the standard | Open-book mode points into the standard by section; the plan schedules reading of the standard itself alongside lessons |

---

## 10. Conventions

From the workspace `CLAUDE.md` files, applied here unchanged: **uv only** from `api/`; Pydantic
v2 for every file shape and request; `orjson`, `polars`, `ruff`; imports at module scope,
stdlib → third party → local; **config from the env YAML through `_require()`**, no defaults for
required keys, no `os.getenv(...) or "<literal>"`; loguru with **f-strings only**; global
exception handler, `try/except` only at I/O boundaries; singular REST paths; pages and `/api`
authorised separately even with one user; CSRF on page `POST`s, pure-ASGI middleware; vendored
static assets registered in `MANIFEST.in` and `package-data`; no `pytest.skip()`; no
`TestClient`.

---

## 11. Open questions

1. **Which conformance document revision** to pin the blueprint to — the 10th Edition Part 1
   and Part 2 conformance requirements at the date authoring starts; record the revision in
   `blueprint.yaml`.
2. **Series Guide breadth**: the conformance document names the guides in scope for Part 2;
   guides outside it get a summary lesson only, no scenario floor. Confirm the list.
3. **Whether to model the 9th Edition differences** for learners transferring from TOGAF 9.2
   (bridge exam is retired). Proposed: a single "what changed" lesson, no separate track.
4. **Scenario length**: real Part 2 scenarios run long; lessons should train reading them under
   time. Proposed: a reading-time gauge on each scenario in review.
5. **Whether the lesson corpus is authored here or generated from an outline** and then edited.
   Resolved by §1.5: generated from the mapped sections, verified, then reviewed by hand.
6. **Which Series Guides to fetch.** All of them are cheap to crawl; only the ones the Part 2
   conformance document names get lessons and scenario floors. The rest are indexed for the
   open-book panel only.
7. **Figure question style.** Blanked-label images need editing of the downloaded figure;
   proposed: an overlay drawn by the page (SVG rectangle over the label's bounding box, stored
   in `important.yaml`), so the source file is never modified.
