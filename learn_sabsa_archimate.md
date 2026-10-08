# Learn SABSA + ArchiMate — extending Learn TOGAF to three frameworks

Companion to `learn_togaf.md`. That document stays the source of truth for the app; this one
covers what SABSA and ArchiMate are, how they fit the app's existing content model, and how a
learner studies all three at once without doubling the hours. Section numbers here are
independent of `learn_togaf.md`; cross-references say "TOGAF plan §n".

Status: **implemented 2026-09-25** (phases 6–10 of §4.8, in one pass): exams as data, the
ArchiMate crawl and figure store, the A/S/X units with their banks, the crosswalk on the ADM
explorer, ArchiMate views on the artefact catalogue and the worked examples, the SABSA worked
examples, the glossary confusables, and the braid as the study plan. Every exam fact below is
still transcribed from memory and marked *(verify)*; `blueprint.yaml` carries a `revision` per
exam saying so. Corrections found while implementing: the ArchiMate specification sits behind
the same Open Group SSO as the Digital Edition (§4.2 said no login was needed — the saved
session is reused, `sources.py fetch --root archimate`); the specification's appendices are
numbered by letter (`ARCHIMATE §B.5`, `§C.1`, `§D.1`) and its TOGAF appendix is **D.1**; the
SABSA white paper and the W117/W14C/W172 PDFs are not yet in the store, so SABSA and WP refs are
form-valid but unresolved and that content stays `status: draft` until `sources.py pdf`
registers them. Open factual check from authoring: §2.1 below places the Business Attributes
Profile at Conceptual × Motivation, whereas the S1–S4 lessons and bank (written from
recollection of the 2009 Matrix) place it at Conceptual × Assets ("business knowledge and risk
strategy") with the control/enablement objectives at Conceptual × Motivation; the crosswalk
lists both cells for Phase A. Settle it against the registered White Paper and flip whichever
side is wrong (about six SCF questions assert Assets).

---

## 0. Why three frameworks, and why together

The three answer three different questions about the same enterprise:

| Framework | The question it answers | Owner | Certification |
|---|---|---|---|
| TOGAF 10 | **How** is architecture work done and governed? (the ADM, the content framework, the capability) | The Open Group | OGEA-101 Foundation, OGEA-102 Practitioner (already in the app) |
| ArchiMate 3.2 | **In what language** is the architecture described so that people and tools agree on what a box and an arrow mean? | The Open Group | OGA-031 Part 1 Foundation, OGA-032 Part 2 Practitioner, OGA-033 combined *(verify codes)* |
| SABSA | **Why** does the architecture exist, in the business's own risk terms, and how is security traceable from strategy to operations? | The SABSA Institute | SABSA Chartered Foundation (SCF), then Practitioner (SCP), Master (SCM) |

They are designed to be combined. The Open Group publishes the bridges itself:

- **W117** *TOGAF and SABSA Integration* (2011, joint with the SABSA Institute): maps the SABSA
  Business Attributes Profile and the SABSA Matrix onto the ADM phases.
- **G152** *Integrating Risk and Security within a TOGAF Enterprise Architecture* (joint with
  the SABSA Institute): already in the app as the `G_RISK_SECURITY` unit — it is the SABSA
  entry point the learner has already read.
- **W14C** *TOGAF Framework and ArchiMate Modeling Language Harmonization*: which ArchiMate
  elements express which TOGAF content-metamodel entities.
- **W172** *Modeling Enterprise Risk Management and Security with the ArchiMate Language*:
  how SABSA-style risk concepts (asset, threat, vulnerability, risk, control) are drawn in
  ArchiMate's Motivation and Core elements.
- The ArchiMate specification's own **Appendix on TOGAF** (3.2 spec, "Relationship to the
  TOGAF Framework", *(verify appendix letter)*): the phase-by-viewpoint table.

So the study order is not "three books one after another" — it is one enterprise walked through
the ADM, described in ArchiMate, justified in SABSA. §3 turns that into a week plan.

---

## 1. ArchiMate 3.2 — the high-level topics

The ArchiMate Specification (Open Group C226, 2022) is free to read online at
`pubs.opengroup.org/architecture/archimate3-doc/`, which is the same publishing platform as the
TOGAF Digital Edition, so `sources.py` can crawl it with a second root (see §4.2).

### 1.1 Language structure (Part 1 syllabus core)

- **Three aspects** — passive structure (things acted on), behaviour (what happens), active
  structure (who or what acts). Every core element sits in exactly one aspect. *Trap:* Part 1
  asks the aspect of an element, e.g. Business Object = passive, Business Process = behaviour,
  Business Role = active.
- **The core layers** — Business, Application, Technology, each with the same three-aspect
  pattern (actor/role/collaboration/interface; process/function/interaction/event/service;
  object/representation). Technology adds Node, Device, System Software, Communication
  Network, Path, Artifact.
- **Physical elements** (3.x) — Equipment, Facility, Distribution Network, Material — as an
  extension of the Technology layer.
- **Motivation elements** — Stakeholder, Driver, Assessment, Goal, Outcome, Principle,
  Requirement, Constraint, Meaning, Value. This is where TOGAF Phase A and SABSA's Contextual
  layer land when modelled.
- **Strategy elements** — Resource, Capability, Value Stream, Course of Action. The TOGAF
  Business Architecture guides (`G_BUSINESS_ARCH`) are drawn with exactly these.
- **Implementation and Migration elements** — Work Package, Deliverable, Implementation Event,
  Plateau, Gap. TOGAF Phases E–F land here: a Plateau is a transition architecture, a Gap is
  gap-analysis output.
- **Composite elements** — Grouping, Location. Junction (And/Or) for combining relationships.
- **The generic metamodel and the full-framework picture** — the layered grid with aspects
  across the top; the exam shows fragments of it.

### 1.2 Relationships (the part most learners fail)

- **Structural** — Composition, Aggregation, Assignment, Realization.
- **Dependency** — Serving, Access (read/write/read-write), Influence (+/−), Association.
- **Dynamic** — Triggering, Flow.
- **Other** — Specialization, and the Junction.
- **Derivation rules** — the "chain" rules that let you infer a permitted relationship between
  two elements that are not directly related; potential vs. valid derivations. Part 1 tests
  whether a given derived relationship is permitted; Part 2 tests whether you drew it.
- **Cross-layer dependencies** — Application serves Business, Technology serves Application,
  Realization upward across layers, Business object realized by Data object realized by
  Artifact.
- **The relationship table** (Appendix B, *(verify)*) is the exam's reference: which
  relationship is allowed between any two element types.

### 1.3 Viewpoints and the viewpoint mechanism

- A **view** is what a stakeholder sees; a **viewpoint** is the specification of it
  (purpose, content, and the elements and relationships allowed). Same words as TOGAF's ISO
  42010 vocabulary — this is deliberate and the exams both test it.
- Classification: **purpose** (designing, deciding, informing) × **content** (details,
  coherence, overview).
- The **example viewpoints** in the spec (Organization, Application Cooperation, Layered,
  Motivation, Strategy, Capability Map, Value Stream, Outcome Realization, Migration,
  Implementation and Migration, Physical, …). Part 2 scenarios ask you to pick and populate
  one.

### 1.4 Language customization and tooling

- **Specialization** of elements and relationships, **attributes/profiles**, and how a tool
  stores them. The **ArchiMate Model Exchange File Format** (XML) for moving models between
  tools.
- **Archi** (free, open source) is the tool the learner should model in from week one — the
  app links out to it; it does not embed it.

### 1.5 The exams *(verify all figures against The Open Group's current datasheet)*

| | Part 1 (OGA-031) | Part 2 (OGA-032) |
|---|---|---|
| Questions | 40 single-answer | 8 scenario, gradient 5/3/1/0 |
| Time | 60 min | 90 min |
| Pass | 60 % (24/40) | 60 % (24/40) |
| Open book | No | Yes (the specification) |

Identical shape to OGEA-101/102, which is the whole reason the app's engine needs no new
question kind — only new exam codes (§4.1).

---

## 2. SABSA — the high-level topics

SABSA has no HTML publication. The primary sources are the **SABSA White Paper** (free, from
sabsa.org after registration) and the "Blue Book", *Enterprise Security Architecture: A
Business-Driven Approach* (Sherwood, Clark, Lynas — purchased). Both register through the
existing `sources.py pdf` path as `SABSA` and `SABSA:bluebook` (§4.2). The framework itself is
open-use with attribution; the training material is not, and the SCF exam is sat only through
an accredited training provider at the end of the course *(verify — the app can rehearse the
syllabus, it cannot replace the course)*.

### 2.1 The SABSA Matrix — the spine of the whole framework

Six **layers** (views), each a full architecture at its level of abstraction, stacked
top-down:

| Layer | View of | TOGAF neighbour |
|---|---|---|
| Contextual | The business | Preliminary + Phase A vision, business scenarios |
| Conceptual | The architect (business attributes, strategy, policy) | Phase A principles, requirements |
| Logical | The designer (services, information, trust) | Phases B–C |
| Physical | The builder (mechanisms, data structures, platforms) | Phases C–D |
| Component | The tradesman (products, tools, standards) | Phase D, SBBs, Solutions Continuum |
| Service Management (Operational) | The facilities manager — cuts across all layers | Phases G–H, governance |

Six **columns**, the Zachman interrogatives: Assets (What), Motivation (Why), Process (How),
People (Who), Location (Where), Time (When). The exam drills the cell contents — e.g.
Conceptual × Motivation = Business Attributes Profile; Logical × Location = security domain
model; Physical × Time = control-structure execution timing.

### 2.2 The Business Attributes Profile

SABSA's signature idea. A taxonomy of **business attributes** (Available, Confidential,
Accurate, Auditable, Recoverable, Legal, Reputable, …) grouped into families (User, Management,
Operational, Risk-management, Legal/Regulatory, Technical Strategy, Business Strategy). Each
attribute in a profile carries a **metric type**, a **measurement approach** and a
**performance target**. It is the conceptual-layer hinge: every control below it must trace up
to an attribute, every business driver above it must map down to one. In the TOGAF crosswalk
it is *what Phase A requirements look like when a security architect writes them* (W117's
central argument).

### 2.3 Risk and opportunity — the SABSA risk model

Risk is two-sided: **threat** (loss) and **opportunity** (gain). Controls are not only
"protect"; they are enhance / protect / detect / recover / correct. Risk appetite and attribute
performance targets are the same thing viewed twice. The **Operational Risk Management**
framework and the "SABSA Risk Assessment" (impact × likelihood over business attributes) feed
the TOGAF risk technique (`F5` objective 5.4, G152 §3).

### 2.4 The Domain Model and trust

**Security domains** (a set of elements under one **policy authority**), **sub-domains**,
**multi-tiered** domains, and **trust relationships** between domains (one-way, two-way,
transitive, and the *inter-domain* service that spans them). This is the logical layer's
answer to "who is allowed to trust whom", and it maps cleanly onto ArchiMate's Grouping /
Location plus Business Role and Interface elements (W172).

### 2.5 The SABSA Lifecycle and Service Management

**Strategy & Planning → Design → Implement → Manage & Measure**, with the Manage & Measure
loop feeding attribute metrics back into Strategy. Service management runs across the matrix's
sixth row: security services, incident and change, assurance and audit. TOGAF's Phase G–H and
the Architecture Contract are the same governance loop with different names.

### 2.6 Traceability, assurance and layering

**Two-way traceability**: top-down (every control justified by a business attribute) and
bottom-up (every attribute covered by a control — the completeness check). **Assurance
framework**: the evidence that traceability holds. **Security services vs. mechanisms vs.
components**: logical → physical → component, same three-step drop as ABB → SBB → product.

### 2.7 The SCF exam *(verify with the SABSA Institute)*

Two modules, F1 *Security Strategy & Planning* and F2 *Security Service Management*; one
multiple-choice paper (recalled as 48 questions, 90 minutes, pass 75 % — **verify**). Single
correct answer, closed book. The app models it as a Foundation-shaped exam with its own pass
mark (§4.1).

---

## 3. Learning all three at once — the braid

### 3.1 The principle: interleave by theme, never by book

Reading TOGAF end-to-end, then ArchiMate, then SABSA takes three passes over the same ideas
(stakeholder, principle, requirement, capability, gap, plateau, governance) and the learner
meets each idea cold three times. Interleaving by **theme** means each week has one enterprise
question and three answers to it. Cost: roughly 1.3× the hours of TOGAF alone, not 3×, because
ArchiMate and SABSA vocabulary largely re-labels what the ADM already taught.

Every braided week ends with the same three exercises:

1. **Draw it** — the week's TOGAF artefact modelled in Archi with the week's ArchiMate elements
   (exported PNG lands in `content/questions/figures/` as the learner's own figure).
2. **Justify it** — the week's SABSA cell(s) filled for the same case (one paragraph per cell).
3. **Drill it** — check-yourself on all three tracks' lessons for the week; the study plan
   (§4.6) schedules cards from all three.

### 3.2 The 16-week braid

The case enterprise is the one the P-series scenarios already use, so nothing new is invented.
Lesson ids for the new tracks are the ones §4.3 proposes.

| Wk | Theme (one question) | TOGAF (existing units) | ArchiMate (new `A*`) | SABSA (new `S*`) |
|---|---|---|---|---|
| 1 | What is architecture, and what is a framework? | F1, F2 | A1 language overview, aspects, layers | S1 what SABSA is, business-driven, the Matrix at a glance |
| 2 | Who cares, and why? | F5 (5.2 stakeholders), F3 | A2 Motivation elements | S2 Contextual layer, business drivers |
| 3 | What must be true? Principles and requirements | F5 (5.1), P7 | A2 Principle, Requirement, Constraint, Influence | S3 Business Attributes Profile |
| 4 | What can we do? Strategy and capability | G_BUSINESS_ARCH, F5 (5.5) | A3 Strategy elements, Capability Map viewpoint | S2 Conceptual layer: strategy and risk appetite |
| 5 | How is the work run? | F3, F4 (Preliminary, A) | A9 the TOGAF appendix: phase ↔ viewpoint | S6 the SABSA Lifecycle vs the ADM (W117) |
| 6 | The business layer | F4 (Phase B) | A4 Business layer elements, Organization and Business Process viewpoints | S4 Logical layer: security services, trust, domains |
| 7 | The information and application layers | F4 (Phase C) | A5 Application layer, Access, Application Cooperation viewpoint | S4 Logical: information security domains, data classification attributes |
| 8 | The technology layer | F4 (Phase D) | A6 Technology + Physical, Layered viewpoint | S5 Physical and Component layers: mechanisms, products |
| 9 | Relationships and derivation — consolidation week | F7 content metamodel | A7 the full relationship set and derivation rules | S7 traceability top-down and bottom-up |
| 10 | Where are the gaps, and how do we get there? | F4 (E, F), F5 (5.3) | A8 Implementation & Migration, Plateau, Gap, Migration viewpoints | S6 Design → Implement, control gap analysis |
| 11 | Risk | F5 (5.4), G_RISK_SECURITY | W172 risk modelling in ArchiMate | S3/S5 risk model, threat and opportunity, ORM |
| 12 | Governance and operations | F8, F4 (G, H), P5, P6 | A8 Work Package, Deliverable; viewpoint mechanism | S6 Service Management layer, assurance, metrics |
| 13 | Views, viewpoints and the audience | P2, F7 | A9 viewpoint classification and the example viewpoints | S1/S7 the Matrix as a viewpoint catalogue |
| 14 | TOGAF mock week | Foundation mock + Practitioner mock | Part 1 mock | SCF drill on F1 module |
| 15 | ArchiMate mock week | Practitioner scenarios re-drawn in Archi | Part 2 mock (open book) | SCF drill on F2 module |
| 16 | Integration week | P8, P9 scenarios | Model the P-scenarios end to end | SCF full mock; W117 crosswalk drill |

### 3.3 Exam sequencing

Sit them in the order the vocabulary builds: **OGEA-101 → OGA-031 → OGEA-102 → OGA-032 →
SCF.** The two Foundation papers share format and half their vocabulary, so back-to-back is
cheap; both Practitioner papers are open-book scenarios and the ArchiMate one is easier once the
TOGAF one has taught you to read a scenario for the planted concern. SCF last, because it is
course-gated *(verify)* and because its "business attribute" thinking is what the TOGAF
Practitioner scenarios already rehearse under the name "requirements and risk".

### 3.4 The confusables — one glossary, three frameworks

The same word means different things across the three, and every exam tests it. These become
`confusable_with[]` entries in `content/glossary.yaml` with the `document` field naming the
framework:

| Word | TOGAF | ArchiMate | SABSA |
|---|---|---|---|
| Domain | Business / Data / Application / Technology architecture | (no element; use layer) | Security domain under a policy authority |
| Capability | Business capability (guide); EA Capability (the function) | Strategy element `Capability` | Not a first-class term; "service" is |
| Principle | Governing statement with rationale and implications | Motivation element `Principle` | Policy at the Conceptual layer |
| Service | Business/IS/technology service in the metamodel | Behaviour element in each layer, exposed via Interface | Security service (Logical layer) |
| Artifact | A work product (catalog, matrix, diagram) | Technology-layer passive element (a file) | (not used) |
| Requirement | Managed by Requirements Management across the ADM | Motivation element `Requirement` | Business attribute + performance target |
| View / Viewpoint | ISO 42010 sense | ISO 42010 sense, plus the viewpoint mechanism | The six Matrix rows are "views" |
| Gap | Gap-analysis output, roadmap component | Implementation & Migration element `Gap` | Control gap |
| Plateau / Transition | Transition Architecture | `Plateau` | Not used; lifecycle phases |
| Risk | Technique in Phase A and G; residual vs initial | Modelled per W172 (Assessment + Driver) | Two-sided: threat and opportunity |

---

## 4. Technical plan — how the app grows from one framework to three

Governing rule: **nothing changes shape, only the enumerations widen.** A SABSA lesson is a
Markdown file with front matter; an ArchiMate Part 2 question is a Practitioner-shaped YAML
item. New content families and new exam codes, no new page kinds until §4.7.

### 4.1 Exams become data, not two fixed fields

Today `Blueprint` has `foundation` and `practitioner` as named fields and `Exam` is a two-value
`Literal` (`content/models.py`). Change:

- `blueprint.yaml`: replace the two named blocks with `exams:` keyed by exam code; each entry
  keeps the existing `ExamFormat` shape plus `track: TOGAF | ARCHIMATE | SABSA` and
  `shape: single | gradient`.
  ```yaml
  exams:
    OGEA-101: {track: TOGAF, name: "TOGAF Foundation", questions: 40, time_minutes: 60, pass_mark: 24, max_score: 40, open_book: false, scoring: single}
    OGEA-102: {track: TOGAF, name: "TOGAF Practitioner", questions: 8, time_minutes: 90, pass_mark: 24, max_score: 40, open_book: true, scoring: gradient}
    OGA-031:  {track: ARCHIMATE, ... scoring: single}
    OGA-032:  {track: ARCHIMATE, ... scoring: gradient}
    SCF:      {track: SABSA, questions: 48, time_minutes: 90, pass_mark: 36, max_score: 48, open_book: false, scoring: single}   # verify
  ```
- Units carry `exam: <code>` instead of `FOUNDATION | PRACTITIONER`. `Exam` becomes
  `str` validated against `blueprint.exams` keys; the weight-sum validator runs per
  `scoring: single` exam, not just "FOUNDATION".
- Question set files move to `questions/<exam code>/` (`questions/OGEA-101/f4.yaml`). The
  `QuestionSetFile.exam` field validates the same way; the "foundation vs practitioner list"
  branch becomes "single vs gradient", driven by the exam's `scoring`.
- `schema.sql`: `exam TEXT` columns already hold free text; add a `track` column to
  `learning_unit` and `question` so the dashboard and coverage pages can group. Content cache
  tables are rebuilt by the loader, so this is a loader change, not a migration.
- This is a **one-shot rename** of the existing content (`FOUNDATION → OGEA-101`,
  `PRACTITIONER → OGEA-102`, directories renamed) — no compatibility branch, per the no-fallback
  rule. `tests/test_content.py` catches anything missed.

### 4.2 Sources — two new roots and two PDFs

- `sources/fetch.py` gets a second crawl root, `pubs.opengroup.org/architecture/archimate3-doc/`,
  with `document_code()` returning `ARCHIMATE` for it (add to `SEGMENT_CODES` /
  `CANONICAL_SEGMENTS`) and the appendices as `ARCHIMATE §B` etc. The Digital Edition login
  session is not needed for it. `sources.py figures` then downloads every diagram in the spec —
  the element notation tables and the example viewpoints are the figure bank for `A*` figure
  questions.
- The bridging documents (W117, W14C, W172) are PDFs the learner downloads with their own
  Open Group account into `resources/sources/pdf/guides/` and registers with `sources.py pdf`;
  codes `WP:w117`, `WP:w14c`, `WP:w172` (extend `document_code()` with a `WP:` prefix
  alongside `GUIDE:`).
- SABSA: `resources/sources/pdf/sabsa.pdf` (white paper) → `SABSA`; the Blue Book, if owned,
  → `SABSA:bluebook`. Refs look like `SABSA §3.2`; `resolve_ref()` already handles the
  `DOC:sub §n` form.
- `objective_sections.yaml` grows the new objectives' mappings; `/coverage` then shows
  unmapped ones exactly as it does today.

### 4.3 Content families

```
content/units/
  A1_language_overview.md … A9_viewpoints_and_togaf.md          # ArchiMate, exam OGA-031 / OGA-032
  S1_sabsa_overview.md … S7_traceability_and_assurance.md       # SABSA, exam SCF
  X1_togaf_archimate.md, X2_togaf_sabsa.md, X3_archimate_sabsa.md   # crosswalk units, no exam, weight 0
content/lessons/A1/…, S1/…, X1/…
content/questions/OGA-031/a1.yaml …   OGA-032/a_scenarios.yaml   SCF/s1.yaml …
content/adm/crosswalk.yaml            # §4.5
content/curriculum.yaml               # §4.6 — the braid
```

Unit ids and objective codes follow the existing pattern (`A1`, objective `A1.1`; `S1`,
`S1.1`). Lessons keep `source: authored`, a ref per paragraph, and the HANDOFF brief applies
verbatim with the unit list changed. Practitioner-shape ArchiMate scenarios carry a `figure:`
(the learner-drawn PNG or a spec figure) because Part 2 questions are read off a diagram.

Coverage floors (TOGAF plan §6 style): ≥ 10 questions per objective; OGA-031 bank ≥ 200,
OGA-032 ≥ 24 scenarios, SCF ≥ 150 *(sized once the SCF syllabus is verified)*.

### 4.4 Glossary

`glossary.yaml` items already carry `document` and `confusable_with[]`. Add the §3.4 rows as
terms with the document set to `ARCHIMATE` / `SABSA`, and `confusable_with` pointing across
frameworks. The glossary page gets a track filter chip; the flashcard "confusable" card kind
already exists and needs nothing.

### 4.5 The crosswalk — extend the ADM explorer, do not add a page

`content/adm/crosswalk.yaml`, one entry per ADM phase:

```yaml
- phase: A
  archimate:
    viewpoints: [MOTIVATION, STRATEGY, OUTCOME_REALIZATION]
    elements: [Stakeholder, Driver, Assessment, Goal, Outcome, Principle, Requirement]
    ref: "ARCHIMATE §C"            # the TOGAF appendix — verify letter
  sabsa:
    layers: [CONTEXTUAL, CONCEPTUAL]
    cells: ["Contextual/Motivation", "Conceptual/Motivation"]
    artefacts: [BUSINESS_ATTRIBUTES_PROFILE, RISK_APPETITE]
    ref: "WP:w117 §4"
```

`AdmPhase` gets an optional `crosswalk` and `/adm/{phase}` renders two extra panels. Each
panel item links into the lesson that teaches it. Cards: a new card kind "crosswalk"
(phase → viewpoint / phase → SABSA layer) is worth adding only after the bank exists.

### 4.6 The braid drives the study plan

`service/plan.py` currently orders lessons Foundation → Practitioner → guides by a SQL
`CASE`. Replace that ordering with `content/curriculum.yaml`, the §3.2 table as data:

```yaml
- week: 2
  theme: "Who cares, and why?"
  lessons: [F5/02_stakeholder_management, F3/01_…, A2/01_motivation_elements, S2/01_contextual_layer]
  exercises:
    draw: "Stakeholder map of the case enterprise as a Motivation view"
    justify: "Contextual × People and Contextual × Motivation cells"
```

`lesson_rows()` reads the curriculum order (a lesson not in the curriculum is appended in the
old order, and `test_content.py` fails if any lesson is missing from it — that is the
completeness gate). `generate_plan()` is unchanged; `reflow()` is unchanged. The `/plan` page
shows the week theme as a heading and the two exercises as checkboxes stored in `setting`.

### 4.7 Practice, mocks and readiness

- `service/practice.py` mock builder takes an exam code and reads its format from the
  blueprint; today it has the two branches hard-coded. Gradient vs. single stays the only real
  branch.
- Combined rehearsals: OGA-033 (Part 1 + Part 2, 150 min) is the ArchiMate twin of the OGEA-103
  rehearsal that already exists.
- `service/readiness.py` reports per exam; the dashboard shows five readiness tiles grouped by
  track, and the plan's target dates become one `exam_date:<code>` setting each.
- The **open-book side panel** (`service/open_book.py`) already searches the section index; with
  `ARCHIMATE` sections indexed it works for OGA-032 unchanged.

### 4.8 Delivery phases (continuing TOGAF plan §7)

| Phase | Scope | Deliverable |
|---|---|---|
| 6 (1 wk) | §4.1 exam-as-data refactor, content rename, tests green | App identical to today, five exam codes in the blueprint |
| 7 (1 wk) | §4.2 ArchiMate crawl + figures, W117/W14C/W172 PDFs, `document_code` prefixes | `/source` lists ARCHIMATE sections and figures; coverage shows `A*` objectives unmapped |
| 8 (3 wk) | `A1–A9` units, lessons, OGA-031 bank ≥ 200, OGA-032 ≥ 24 | ArchiMate mocks at real format |
| 9 (2 wk) | `S1–S7` units, lessons, SCF bank ≥ 150 (after syllabus verification) | SCF drills and a full mock |
| 10 (1 wk) | `crosswalk.yaml`, `curriculum.yaml`, plan page themes, glossary confusables, `X*` units | The braid is the default study plan |

### 4.9 Risks

- **Exam facts are recalled, not verified.** Every *(verify)* above must be checked against
  the certifying body before its mock is authored; record the revision in `blueprint.yaml` as
  the TOGAF entry already does.
- **SABSA source thinness.** The white paper is ~60 pages; a 150-question bank grounded only
  on it will be repetitive. The Blue Book is the real source and must be owned.
- **Copyright.** Same rule as TOGAF plan §1.3: paraphrase, cite, private source store. SABSA
  training material is not a source; the framework documents are.
- **Scope creep on ArchiMate tooling.** The app links to Archi and stores exported PNGs. It
  does not render ArchiMate, validate models or parse the exchange format. Say no to that
  until every bank is at target.
- **The rename in §4.1 touches every content file.** Do it in one commit with the tests, on a
  day nothing else is being authored; HANDOFF.md's unit table must be updated in the same
  commit.
