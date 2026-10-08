---
title: Phase E in practice, from consolidated gaps to a first roadmap
unit: P5
objectives: ["P5.1"]
refs: ["ADM §9", "ADM §9.1", "ADM §9.3", "ADM §9.3.3", "ADM §9.3.5", "ADM §9.3.7", "ADM §9.3.8", "ADM §9.3.9", "ADM §9.3.10", "ADM §9.3.11", "ADM §9.5", "CONTENT §3.6.8", "TECH §6.6", "TECH §7.5", "TECH §8.4"]
reading_minutes: 10
source: authored
status: draft
---
## What a Phase E scenario looks like

The Phases B to D work is finished: the scenario hands you approved Target Architectures in
several domains, a pile of gap analysis results, and a sponsor who wants "the projects" by
Friday. It then plants three or four facts: two commercial packages whose embedded processes
disagree, a readiness finding from Phase A that nobody has revisited, a line of business
that cannot absorb change until after its peak season, and a budget holder who wants value
early. Phase E exists to turn that pile into an Architecture Roadmap and a draft
Implementation and Migration Plan, and the exam is testing whether you know the order in
which the standard does it (ADM §9.1, ADM §9.5).

The five-point answer follows the Phase E steps: confirm the change attributes and business
constraints, consolidate the gaps from B to D into one matrix, reconcile interoperability,
refine dependencies, confirm readiness and risk, agree an Implementation and Migration
Strategy, group work packages, identify Transition Architectures that each deliver
measurable value, then draft the roadmap and plan (ADM §9.3). The three-point answer has the
right deliverables but skips the consolidation and goes straight to work packages; the
one-point answer selects products; the zero-point answer starts building.

## The artefacts the scenario is really asking for

| Planted fact | Step | Artefact or technique |
|---|---|---|
| Culture, capacity of business units, "our people are change-weary" | 9.3.1 Determine key corporate change attributes | Implementation Factor catalog: risks, issues, assumptions, dependencies, actions, impacts (CONTENT §3.6.8) |
| Peak season, budget cycle, strategic plan constraint | 9.3.2 Determine business constraints | Review of business and strategic plans and the maturity assessment |
| Gaps in three domains that overlap | 9.3.3 Review and consolidate gap analysis results | Consolidated Gaps, Solutions, and Dependencies matrix; SBBs identified against ABBs (ADM §9.3.3) |
| Several lines of business raising the same need | 9.3.4 Review consolidated requirements | Shared Business and Application Services in one work package |
| Two packages whose processes conflict | 9.3.5 Consolidate and reconcile interoperability | Either a translating building block or a change to the conflicting specification (ADM §9.3.5) |
| "Project X cannot start until the data platform exists" | 9.3.6 Refine and validate dependencies | Dependencies drive sequencing and grouping; the basis of most migration planning |
| Phase A readiness findings | 9.3.7 Confirm readiness and risk | Risks recorded in the matrix (TECH §7.5) |

**Trap.** Interoperability conflicts introduced by re-used SBBs, COTS products and third-party
providers must be resolved *in the architecture*, across all four domains, and a change to
business interoperability needs a revised Statement of Architecture Work signed by the
Business Architects and sponsors (TECH §6.6). An answer that leaves the conflict "for the
project to sort out" loses points.

<figure class="my-4">
<svg viewBox="0 0 760 300" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="11" role="img" aria-label="Phase E as four moves: assess the enterprise, consolidate gaps and dependencies, decide the strategy, package and draft the roadmap">
<defs><marker id="arr-p5e" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
<rect x="10" y="12" width="165" height="62" rx="8" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="92" y="34" text-anchor="middle" font-weight="bold">assess</text>
<text x="92" y="50" text-anchor="middle">9.3.1 change attributes</text>
<text x="92" y="64" text-anchor="middle">9.3.2 business constraints</text>
<rect x="195" y="12" width="200" height="62" rx="8" fill="#e3f5e1" stroke="#7fbf7a"/>
<text x="295" y="34" text-anchor="middle" font-weight="bold">consolidate</text>
<text x="295" y="50" text-anchor="middle">9.3.3 gaps  9.3.4 requirements</text>
<text x="295" y="64" text-anchor="middle">9.3.5 interoperability  9.3.6 dependencies</text>
<rect x="415" y="12" width="150" height="62" rx="8" fill="#fff1d6" stroke="#e0b060"/>
<text x="490" y="34" text-anchor="middle" font-weight="bold">decide</text>
<text x="490" y="50" text-anchor="middle">9.3.7 readiness and risk</text>
<text x="490" y="64" text-anchor="middle">9.3.8 strategy</text>
<rect x="585" y="12" width="165" height="62" rx="8" fill="#f3e3f7" stroke="#b58ac9"/>
<text x="667" y="34" text-anchor="middle" font-weight="bold">package</text>
<text x="667" y="50" text-anchor="middle">9.3.9 work packages  9.3.10 transitions</text>
<text x="667" y="64" text-anchor="middle">9.3.11 roadmap and plan, draft</text>
<line x1="175" y1="43" x2="195" y2="43" stroke="#555" marker-end="url(#arr-p5e)"/>
<line x1="395" y1="43" x2="415" y2="43" stroke="#555" marker-end="url(#arr-p5e)"/>
<line x1="565" y1="43" x2="585" y2="43" stroke="#555" marker-end="url(#arr-p5e)"/>
<rect x="60" y="110" width="640" height="46" rx="6" fill="#fff" stroke="#666"/>
<text x="380" y="129" text-anchor="middle" font-weight="bold">Consolidated Gaps, Solutions, and Dependencies matrix</text>
<text x="380" y="146" text-anchor="middle">one row per gap: domain, gap, potential solution, dependencies, risks (filled in as the steps run)</text>
<line x1="295" y1="74" x2="295" y2="110" stroke="#555" marker-end="url(#arr-p5e)"/>
<line x1="490" y1="74" x2="490" y2="110" stroke="#555" stroke-dasharray="4 3" marker-end="url(#arr-p5e)"/>
<line x1="667" y1="74" x2="667" y2="110" stroke="#555" stroke-dasharray="4 3" marker-end="url(#arr-p5e)"/>
<rect x="60" y="190" width="200" height="46" rx="6" fill="#fff" stroke="#666"/>
<text x="160" y="209" text-anchor="middle" font-weight="bold">Implementation Factor catalog</text>
<text x="160" y="226" text-anchor="middle">risks, issues, assumptions, dependencies, actions</text>
<rect x="280" y="190" width="200" height="46" rx="6" fill="#fff" stroke="#666"/>
<text x="380" y="209" text-anchor="middle" font-weight="bold">Architecture Roadmap, draft</text>
<text x="380" y="226" text-anchor="middle">work packages and Transition Architectures on a timeline</text>
<rect x="500" y="190" width="200" height="46" rx="6" fill="#fff" stroke="#666"/>
<text x="600" y="209" text-anchor="middle" font-weight="bold">Implementation and Migration Plan, draft</text>
<text x="600" y="226" text-anchor="middle">strategy plus the activity to realise the roadmap</text>
<line x1="160" y1="156" x2="160" y2="190" stroke="#555" marker-end="url(#arr-p5e)"/>
<line x1="380" y1="156" x2="380" y2="190" stroke="#555" marker-end="url(#arr-p5e)"/>
<line x1="600" y1="156" x2="600" y2="190" stroke="#555" marker-end="url(#arr-p5e)"/>
<text x="380" y="275" text-anchor="middle" fill="#666">Phase E delivers a draft; Phase F finalises it with the portfolio and project managers (ADM §9.5, §10.5)</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">Phase E as four moves feeding one matrix and three outputs. Original drawing; the step numbers follow ADM §9.3 and the artefacts CONTENT §3.6.8.</figcaption>
</figure>

## The decisions the answer must name

**Strategy first, then work packages.** The Implementation and Migration Strategy chooses an
overall approach, greenfield, revolutionary (switch on, switch off) or evolutionary
(convergence, parallel running, phased), and a method for realising value, quick win,
achievable targets or value chain. Those choices and the dependencies become the basis of
the work packages, and the step ends with *agreement* on the strategy (ADM §9.3.8). A
scenario that describes a nervous, change-averse enterprise with a hard regulatory date is
steering you to an evolutionary approach with a quick-win increment, not a big bang.

**Classify what you already have.** Every current system under consideration is classified
as mainstream (part of the future), contain (to be replaced or modified within the planning
horizon of about three years) or replace; solutions are marked as new development, existing
product or purchase; and top-level work packages are decomposed into increments and grouped
into portfolios and projects (ADM §9.3.9).

**Transition Architectures earn their place by value.** They are needed only where the
change requires an incremental approach; each must deliver measurable business value, the
gaps between them need not be equal, and the difficult activities go after the ones that
most easily deliver missing capability unless there is a compelling reason otherwise
(ADM §9.3.10).

**Draft, at the same level of detail as the Architecture Definition Document.** The roadmap
must show how the chosen transitions and work packages realise the target; if much more
detail is needed before anything can be built, the work is moving to a lower architecture
level and the standard points you at iteration guidance rather than at padding the roadmap
(ADM §9.3.11). Finally the Vision, Definition Document and Requirements Specification are
updated with what Phase E learned.

## How the 5, 3 and 1 differ

| Answer | What it does | Why it scores that |
|---|---|---|
| 5 | Consolidates gaps into the matrix, reconciles the package conflict in the architecture, confirms Phase A readiness and records risk, agrees an evolutionary strategy with the sponsor, groups work packages and defines two value-bearing Transition Architectures, drafts roadmap and plan | Every planted fact is handled by the step the standard assigns to it (ADM §9.3) |
| 3 | Produces a roadmap and plan of work packages straight from the domain gap lists, with one big transition | Right outputs, but the gaps were never consolidated and dependencies never validated, so the interoperability conflict and shared-service opportunity are missed (ADM §9.3.3, §9.3.4) |
| 1 | Runs a procurement to select the packages, then plans around the vendors' delivery dates | Phase E selects solutions *after* the strategy and dependencies are understood, and the interoperability conflict must be addressed in the architecture first (TECH §6.6) |
| 0 | Lets the implementation teams start on the most urgent gaps now and "roadmap later" | Contradicts the purpose of the phase: the roadmap frames migration planning, and readiness and risk must be confirmed before work is committed (ADM §9.3.7, §9.5) |

**Trap.** Phase E is the *initial* step in creating the Implementation and Migration Plan; the
plan is completed in Phase F. An answer that calls the Phase E plan "approved" or hands it to
portfolio management as final has mislabelled the phase (ADM §9.5).

**Trap.** Risk in Phase E is classified by effect and frequency and mitigated to a residual
level; the risk worksheet is a governance artefact kept up to date in Phase G, not a one-off
list (TECH §8.4).

## Where to look in the book

Open the ADM document at chapter 9. Section 9.3 lists the eleven steps in order and the
sub-sections 9.3.3 to 9.3.11 hold the wording the answers reuse ("Consolidated Gaps,
Solutions, and Dependencies", "greenfield, revolutionary, evolutionary", "mainstream,
contain, replace"). Section 9.4 lists outputs and 9.5 the approach with the four key
concepts. Architecture Content §3.6.8 describes the Phase E artefacts, ADM Techniques §6.6
the interoperability reconciliation, §7.5 readiness in migration planning and §8.4 the risk
classification scheme.

## Check yourself

- Which artefact do you create in step 9.3.1, and what does it hold?
- Name the three implementation approaches and the three value methods of step 9.3.8.
- What is the rule for where the difficult activities go on the roadmap?
