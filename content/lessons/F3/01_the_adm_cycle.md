---
title: The ADM cycle, the nine development steps, and how the method is adapted
unit: F3
objectives: ["3.1", "3.2", "3.3"]
refs: ["ADM §1.1", "ADM §1.2", "ADM §1.3", "ADM §1.5", "ADM §4.3", "ADM §6.3", "ADM §7.3", "ADM §8.3", "ADM §13", "ADM §13.1", "ADM §1.1.1"]
reading_minutes: 9
source: authored
status: draft
---
## 1. What the ADM is

The Architecture Development Method is the core of the standard: a repeatable method for
developing an enterprise architecture and managing its realisation, built from a set of phases
that are run as a cycle (ADM §1.1). It is generic on purpose. It does not say what your
architecture should contain; it says in what order to do the work, what each phase needs and
what it produces, and where the reusable assets live (ADM §1.1.1).

## 2. The cycle

The ADM is drawn as a circle. The Preliminary Phase sits outside the ring, Phases A to H run
round it, and Requirements Management sits in the centre, connected to every phase (ADM §1.2.2).

<figure class="my-4 max-w-md">
  <img src="/figure/ADM:fig-1-1" alt="The Architecture Development Cycle: the Preliminary Phase above a ring of Phases A to H, with Requirements Management in the centre" class="rounded border border-base-300">
  <figcaption class="text-xs text-base-content/60 mt-1">The standard's own drawing of the cycle, Figure 1-1 (ADM §1.2), from your local copy of the publication.</figcaption>
</figure>

| Phase | Name | What it is for |
|---|---|---|
| Preliminary | Preliminary Phase | Set up the Architecture Capability: scope the enterprise, confirm governance, establish the team, define principles, tailor the framework. Runs before the cycle proper and again whenever the capability changes. |
| A | Architecture Vision | Start a cycle: scope, stakeholders and concerns, the Architecture Vision, and the Statement of Architecture Work for the sponsor to approve. |
| B | Business Architecture | The first of three development phases. Baseline and Target Business Architecture, gap analysis, candidate roadmap components. |
| C | Information Systems Architectures | The second development phase, in two parts: Data Architecture and Application Architecture. Same steps as B. |
| D | Technology Architecture | The third development phase. Same steps as B. |
| E | Opportunities and Solutions | Consolidate the gaps into work packages; the first complete Architecture Roadmap; decide whether Transition Architectures are needed. |
| F | Migration Planning | Finalise the Implementation and Migration Plan and the Roadmap; hand over to portfolio and project management. |
| G | Implementation Governance | Govern implementation: the Architecture Contract, compliance reviews, change requests from projects. |
| H | Architecture Change Management | Keep the architecture alive after deployment; classify change and decide when a new cycle starts. |
| Centre | Requirements Management | Continuous, not a phase in the sequence: store, assess and route requirements to every phase (ADM §13.1). |

**Trap.** Phase C is one phase with two parts. The diagram shows one circle for it, and a
question that lists "Data Architecture" as a phase of its own is wrong (ADM §1.2.2).

**Trap.** Requirements Management is at the centre because every phase both produces and
consumes requirements; it manages the flow, and the *phases* dispose of them (ADM §13.1).

<figure class="my-4 max-w-md">
  <img src="/figure/ADM:fig-13-1" alt="Requirements Management at the centre of the ADM, exchanging requirements with every phase" class="rounded border border-base-300">
  <figcaption class="text-xs text-base-content/60 mt-1">Figure 13-1 (ADM §13): requirements flow between the centre and every phase, in both directions.</figcaption>
</figure>

## 3. The nine steps of a development phase

Phases B, C and D each run the same sequence. The standard spells it out for Phase B
(ADM §4.3) and repeats it for the Data, Application and Technology Architectures, so learning
it once covers three phases, and the order is a favourite exam question.

| # | Step | What happens |
|---|---|---|
| 1 | Select reference models, viewpoints and tools (ADM §4.3.1) | Choose the reference models, the viewpoints that address the stakeholders' concerns, and the modelling tools and techniques for this phase. |
| 2 | Develop the Baseline Architecture description (ADM §4.3.2) | Describe what exists today, to the level of detail needed to find the gaps. |
| 3 | Develop the Target Architecture description (ADM §4.3.3) | Describe the future state that delivers the Architecture Vision. |
| 4 | Perform gap analysis (ADM §4.3.4) | Compare baseline and target: what is new, what is eliminated, what carries over. |
| 5 | Define candidate roadmap components (ADM §4.3.5) | Turn the gaps into candidate work for the Architecture Roadmap; Phase E consolidates them. |
| 6 | Resolve impacts across the Architecture Landscape (ADM §4.3.6) | Check what this architecture changes for other architectures in progress or in use. |
| 7 | Conduct formal stakeholder review (ADM §4.3.7) | Review against the Vision and the requirements; go back a step if the review demands it. |
| 8 | Finalize the architecture (ADM §4.3.8) | Select the building blocks, complete the artefacts, confirm the requirements are met. |
| 9 | Create or update the Architecture Definition Document (ADM §4.3.9) | Record the result in the document that spans all four domains. |


<figure class="my-4">
<svg viewBox="0 0 760 250" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="The nine development steps grouped as choose, describe, compare, record">
  <defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
  <!-- group bands -->
  <rect x="10" y="10" width="110" height="60" rx="8" fill="#e0ecff" stroke="#7aa2e3"/><text x="65" y="35" text-anchor="middle" font-weight="bold">choose</text><text x="65" y="55" text-anchor="middle" fill="#345">step 1</text>
  <rect x="140" y="10" width="200" height="60" rx="8" fill="#e3f5e1" stroke="#7fbf7a"/><text x="240" y="35" text-anchor="middle" font-weight="bold">describe</text><text x="240" y="55" text-anchor="middle" fill="#345">steps 2–3</text>
  <rect x="360" y="10" width="250" height="60" rx="8" fill="#fff1d6" stroke="#e0b060"/><text x="485" y="35" text-anchor="middle" font-weight="bold">compare</text><text x="485" y="55" text-anchor="middle" fill="#345">steps 4–7</text>
  <rect x="630" y="10" width="120" height="60" rx="8" fill="#f3e3f7" stroke="#b58ac9"/><text x="690" y="35" text-anchor="middle" font-weight="bold">record</text><text x="690" y="55" text-anchor="middle" fill="#345">steps 8–9</text>
  <!-- the nine steps -->
  <g fill="#fff" stroke="#666">
    <rect x="15" y="100" width="100" height="44" rx="6"/>
    <rect x="145" y="100" width="90" height="44" rx="6"/><rect x="245" y="100" width="90" height="44" rx="6"/>
    <rect x="365" y="100" width="55" height="44" rx="6"/><rect x="428" y="100" width="55" height="44" rx="6"/><rect x="491" y="100" width="55" height="44" rx="6"/><rect x="554" y="100" width="52" height="44" rx="6"/>
    <rect x="635" y="100" width="52" height="44" rx="6"/><rect x="695" y="100" width="52" height="44" rx="6"/>
  </g>
  <g text-anchor="middle" font-size="11">
    <text x="65" y="118">1 select models,</text><text x="65" y="133">viewpoints, tools</text>
    <text x="190" y="118">2 baseline</text><text x="190" y="133">description</text>
    <text x="290" y="118">3 target</text><text x="290" y="133">description</text>
    <text x="392" y="118">4 gap</text><text x="392" y="133">analysis</text>
    <text x="455" y="118">5 roadmap</text><text x="455" y="133">candidates</text>
    <text x="518" y="118">6 resolve</text><text x="518" y="133">impacts</text>
    <text x="580" y="118">7 review</text>
    <text x="661" y="118">8 finalize</text>
    <text x="721" y="118">9 ADD</text><text x="721" y="133">create/update</text>
  </g>
  <!-- flow -->
  <line x1="115" y1="122" x2="145" y2="122" stroke="#555" marker-end="url(#arr)"/>
  <line x1="235" y1="122" x2="245" y2="122" stroke="#555" marker-end="url(#arr)"/>
  <line x1="335" y1="122" x2="365" y2="122" stroke="#555" marker-end="url(#arr)"/>
  <line x1="606" y1="122" x2="635" y2="122" stroke="#555" marker-end="url(#arr)"/>
  <line x1="687" y1="122" x2="695" y2="122" stroke="#555" marker-end="url(#arr)"/>
  <!-- the review loop back -->
  <path d="M580 144 L580 190 L190 190 L190 144" fill="none" stroke="#c0392b" stroke-dasharray="5 4" marker-end="url(#arr)"/>
  <text x="385" y="205" text-anchor="middle" fill="#c0392b" font-size="11">7 → back to 2 or 3 when the stakeholder review demands a change</text>
  <text x="380" y="240" text-anchor="middle" fill="#666" font-size="11">Phase B runs this once; Phase C runs it for Data and again for Application; Phase D runs it once (ADM §4.3, §6.3, §7.3, §8.3)</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">The nine steps as four moves. Original drawing; the step names follow ADM §4.3.</figcaption>
</figure>

A memory aid in four words: **choose, describe, compare, record**. Steps 1 chooses the
models and views; 2 and 3 describe baseline and target; 4 to 7 compare, resolve and review;
8 and 9 finalise and record.

**Trap.** Gap analysis is step 4 in every development phase; the *consolidated* gaps,
solutions and dependencies across all three phases are Phase E's work, not B's.

**Trap.** Step 9 is create *or update*: Phase B starts the Architecture Definition Document,
Phases C and D add their domains to the same document.

## 4. Adapting the ADM

The method is meant to be tailored, and the standard lists the reasons (ADM §1.3): the
organisation may already use other frameworks or process models; its maturity may call for a
lighter or fuller method; the work may be at enterprise, segment or capability scope; it may be
a single project or a programme; and reusable assets already in the Architecture Repository may
let some phases be shortened. Tailoring is done in the Preliminary Phase and recorded in the
Tailored Architecture Framework.

Scope is set along four dimensions (ADM §1.5): **breadth** (how much of the enterprise),
**depth** (level of detail), **time period** (the horizon of the Target Architecture) and
**architecture domains** (which of business, data, application and technology).

## 5. Iteration and the repository

Iteration happens at three levels (ADM §1.2.1): around the whole cycle, between phases
(going back from C to B when a new requirement demands it), and within a phase. The four named
iteration cycles are covered in unit F6.

Every phase draws on the Architecture Repository for reusable assets (reference models,
patterns, standards, the Architecture Landscape) and writes its results back into it, and the
Enterprise Continuum is the classification used to find and place those assets (ADM §1.1.1).
That is why the Preliminary Phase creates the initial repository before Phase A starts: a cycle
that begins with an empty repository has nothing to reuse.

## Check yourself

- Name the nine steps in order without looking. Which one does Phase C run twice?
- Which document records the result of tailoring the ADM?
- Why is Requirements Management drawn in the centre rather than as a phase?
