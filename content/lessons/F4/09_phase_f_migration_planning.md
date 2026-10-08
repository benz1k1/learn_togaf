---
title: Phase F, Migration Planning, in depth
unit: F4
objectives: ["4.3", "4.5"]
refs: ["ADM §10", "ADM §10.1", "ADM §10.2", "ADM §10.2.1", "ADM §10.2.2", "ADM §10.2.3", "ADM §10.3", "ADM §10.3.1", "ADM §10.3.2", "ADM §10.3.3", "ADM §10.3.4", "ADM §10.3.5", "ADM §10.3.6", "ADM §10.3.7", "ADM §10.4", "ADM §10.5"]
reading_minutes: 10
source: authored
status: draft
---
## What the phase is for

Phase F is about how to move from Baseline to Target by finalizing a detailed Implementation and
Migration Plan (ADM §10). Three objectives (ADM §10.1):

| Objective | In plain words |
|---|---|
| **Finalize** the Architecture Roadmap and the supporting Implementation and Migration Plan | turn Phase E's drafts into approved plans |
| Ensure the plan is **co-ordinated with the enterprise's approach** to managing and implementing change in its overall change portfolio | fit into the portfolio, not beside it |
| Ensure the **business value and cost** of work packages and Transition Architectures is understood by key stakeholders | make the value explicit |

## Approach

The focus is creating the Implementation and Migration Plan **in co-operation with the project
and portfolio managers** (ADM §10.5). Phase E hands over an incomplete roadmap and plan that
address the Statement of Architecture Work; Phase F integrates them with the enterprise's other
change activity, assessing the dependencies, costs and benefits of the migration projects in that
wider context, and adds portfolio- and project-level detail. Then the architecture development
cycle is completed and lessons learned are documented for continuous process improvement.

## Inputs

| Group | Inputs |
|---|---|
| External (ADM §10.2.1) | architecture reference materials |
| Non-architectural (ADM §10.2.2) | Request for Architecture Work; Capability Assessment; Communications Plan |
| Architectural (ADM §10.2.3) | Organizational Model; governance models and frameworks; Tailored Framework; Statement of Architecture Work; Architecture Vision; Architecture Repository; draft Architecture Definition Document (now possibly with Transition Architectures); draft Architecture Requirements Specification; Change Requests for existing programs and projects; **Architecture Roadmap, Draft** (work packages, Transition Architectures, Implementation Factor catalog); Capability Assessment (Business and IT); **Implementation and Migration Plan, Draft** with the high-level strategy |

The last two lines are the Phase E outputs arriving as inputs.

## Steps

Seven steps; everything is closed in step 7 (ADM §10.3).

| # | Step | Key point |
|---|---|---|
| 1 | Confirm management framework interactions for the Implementation and Migration Plan | four frameworks must work together: **Business Planning, Enterprise Architecture, Project/Portfolio Management, Operations Management**; the plan may end up as part of another framework's plan (ADM §10.3.1) |
| 2 | Assign a business value to each work package | performance evaluation criteria, return-on-investment criteria, a definition of business value, critical success factors, measures of effectiveness, strategic fit; risks are aggregated from the Consolidated Gaps, Solutions and Dependencies matrix; estimate value with the **Business Value and Risk Matrix** (ADM §10.3.2) |
| 3 | Estimate resource requirements, project timings and availability/delivery vehicle | costs split into **capital** and **operations and maintenance**; offset new costs by decommissioning (ADM §10.3.3) |
| 4 | Prioritize the migration projects by conducting a cost/benefit assessment and risk assessment | net benefit of the SBBs delivered; verify risks are mitigated; stakeholders agree a prioritized list; a project may rank high because it is on the path to a large benefit (ADM §10.3.4) |
| 5 | Confirm Architecture Roadmap and update Architecture Definition Document | revise the roadmap and Transition Architecture spacing; the **Transition Architecture State Evolution Table** and the **Architecture Definition Increments Table** are used here (ADM §10.3.5) |
| 6 | Complete the Implementation and Migration Plan | bring it all together with accepted planning techniques; Transition Architectures act as portfolio milestones (ADM §10.3.6) |
| 7 | Complete the architecture development cycle and document lessons learned | governance transitions from development to realization; an **Implementation Governance Model** may be produced if maturity warrants; lessons learned are captured by the governance process in Phase H (ADM §10.3.7) |

## Outputs

(ADM §10.4)

| Output | Note |
|---|---|
| **Implementation and Migration Plan, Approved** | strategy, project and portfolio breakdown, milestones and timing, work breakdown structure, optional project charters |
| **Finalized** Architecture Definition Document | including finalized Transition Architectures, if any |
| **Finalized** Architecture Requirements Specification | |
| **Finalized** Architecture Roadmap | |
| Re-usable ABBs | |
| Requests for Architecture Work for a new iteration of the ADM cycle | if any |
| Implementation Governance Model | if any |
| Change Requests for the Architecture Capability arising from lessons learned | |

<figure class="my-4">
<svg viewBox="0 0 760 288" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="Phase F: its inputs, seven steps and outputs, with the Implementation Governance Model marked as first produced here">
  <defs><marker id="arr-f4-16" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
  <text x="107.5" y="18" text-anchor="middle" font-size="12" font-weight="bold" fill="#345">Inputs</text><text x="652.5" y="18" text-anchor="middle" font-size="12" font-weight="bold" fill="#345">Outputs</text><text x="380" y="18" text-anchor="middle" font-size="12" font-weight="bold" fill="#345">Steps</text><rect x="235" y="34" width="290" height="220" rx="8" fill="#fff1d6" stroke="#e0b060"/><text x="380" y="52" text-anchor="middle" font-size="12" font-weight="bold">Phase F: Migration Planning</text><text x="245" y="106.5" font-size="11">1 Confirm management framework interactions</text><text x="245" y="121.5" font-size="11">2 Assign a business value to each work package</text><text x="245" y="136.5" font-size="11">3 Estimate resources, timings, delivery vehicle</text><text x="245" y="151.5" font-size="11">4 Prioritize projects: cost/benefit and risk</text><text x="245" y="166.5" font-size="11">5 Confirm Roadmap; update the ADD</text><text x="245" y="181.5" font-size="11">6 Complete the Implementation and Migration Plan</text><text x="245" y="196.5" font-size="11">7 Complete the cycle; document lessons learned</text><rect x="10" y="34" width="195" height="46" rx="6" fill="#e0ecff" stroke="#7aa2e3"/><text x="107.5" y="54.5" text-anchor="middle" font-size="10.5">Architecture Roadmap, draft</text><text x="107.5" y="67.5" text-anchor="middle" font-size="10.5">(from Phase E)</text><line x1="205" y1="57" x2="233" y2="57" stroke="#555" marker-end="url(#arr-f4-16)"/><rect x="10" y="92" width="195" height="46" rx="6" fill="#e0ecff" stroke="#7aa2e3"/><text x="107.5" y="112.5" text-anchor="middle" font-size="10.5">Implementation and Migration Plan,</text><text x="107.5" y="125.5" text-anchor="middle" font-size="10.5">draft, with the strategy (Phase E)</text><line x1="205" y1="115" x2="233" y2="115" stroke="#555" marker-end="url(#arr-f4-16)"/><rect x="10" y="150" width="195" height="46" rx="6" fill="#e0ecff" stroke="#7aa2e3"/><text x="107.5" y="164" text-anchor="middle" font-size="10.5">Draft Architecture Definition Doc.</text><text x="107.5" y="177" text-anchor="middle" font-size="10.5">(with Transition Architectures) and</text><text x="107.5" y="190" text-anchor="middle" font-size="10.5">draft Requirements Specification</text><line x1="205" y1="173" x2="233" y2="173" stroke="#555" marker-end="url(#arr-f4-16)"/><rect x="10" y="208" width="195" height="46" rx="6" fill="#e0ecff" stroke="#7aa2e3"/><text x="107.5" y="228.5" text-anchor="middle" font-size="10.5">Change Requests for existing</text><text x="107.5" y="241.5" text-anchor="middle" font-size="10.5">programs and projects</text><line x1="205" y1="231" x2="233" y2="231" stroke="#555" marker-end="url(#arr-f4-16)"/><rect x="555" y="34" width="195" height="46" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/><text x="652.5" y="54.5" text-anchor="middle" font-size="10.5">Implementation and Migration Plan,</text><text x="652.5" y="67.5" text-anchor="middle" font-size="10.5">approved</text><rect x="689.4" y="26" width="56.6" height="15" rx="7" fill="#f3e3f7" stroke="#b58ac9"/><text x="717.7" y="37" text-anchor="middle" font-size="9.5" fill="#5b2d6e">finalized</text><line x1="525" y1="57" x2="553" y2="57" stroke="#555" marker-end="url(#arr-f4-16)"/><rect x="555" y="92" width="195" height="46" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/><text x="652.5" y="106" text-anchor="middle" font-size="10.5">Finalized Architecture Definition</text><text x="652.5" y="119" text-anchor="middle" font-size="10.5">Document, Requirements</text><text x="652.5" y="132" text-anchor="middle" font-size="10.5">Specification and Roadmap</text><rect x="689.4" y="84" width="56.6" height="15" rx="7" fill="#f3e3f7" stroke="#b58ac9"/><text x="717.7" y="95" text-anchor="middle" font-size="9.5" fill="#5b2d6e">finalized</text><line x1="525" y1="115" x2="553" y2="115" stroke="#555" marker-end="url(#arr-f4-16)"/><rect x="555" y="150" width="195" height="46" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/><text x="652.5" y="170.5" text-anchor="middle" font-size="10.5">Implementation Governance Model</text><text x="652.5" y="183.5" text-anchor="middle" font-size="10.5">(if any)</text><rect x="711" y="142" width="35" height="15" rx="7" fill="#f3e3f7" stroke="#b58ac9"/><text x="728.5" y="153" text-anchor="middle" font-size="9.5" fill="#5b2d6e">first</text><line x1="525" y1="173" x2="553" y2="173" stroke="#555" marker-end="url(#arr-f4-16)"/><rect x="555" y="208" width="195" height="46" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/><text x="652.5" y="222" text-anchor="middle" font-size="10.5">Request for Architecture Work for a</text><text x="652.5" y="235" text-anchor="middle" font-size="10.5">new iteration; Change Requests for</text><text x="652.5" y="248" text-anchor="middle" font-size="10.5">the Architecture Capability</text><line x1="525" y1="231" x2="553" y2="231" stroke="#555" marker-end="url(#arr-f4-16)"/><text x="380" y="272" text-anchor="middle" font-size="11" fill="#666">Drafts go in, finalized and approved versions come out — nothing is finalized before F (ADM §10.4)</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">Inputs, steps and outputs of Phase F. Original drawing; inputs and outputs per ADM §10.2 and ADM §10.4, steps per ADM §10.3.</figcaption>
</figure>

> **Trap.** Phase F is where "draft" becomes "finalized" and "approved". Any option that has
> the Architecture Definition Document, Architecture Requirements Specification or Architecture
> Roadmap *finalized* in Phase E or D is wrong. Equally, the Implementation Governance Model is a
> Phase F output (optional) and a Phase G input — not the other way round.

> **Trap.** Step 4's wording is "cost/benefit assessment **and risk assessment**" — the exam may
> offer "risk validation" or "benefit realization" as near-miss wording. And Phase F's business
> value technique is the Business Value and Risk Matrix (step 2), not the Benefits Diagram.

<!-- figures:start -->
## Figures from the standard

The diagrams the cited sections carry, from your local copy of the publication. The exam reproduces these; know what each box is.

<div class="grid gap-4 md:grid-cols-2">
<figure class="max-w-lg"><img src="/figure/ADM:fig-10-1" alt="Figure 10-1: Phase F: Migration Planning" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 10-1: Phase F: Migration Planning (ADM)</figcaption></figure>
</div>
<!-- figures:end -->

## Check yourself

1. Which two Phase E outputs enter Phase F as drafts, and what does Phase F call them on the way out?
2. Which four management frameworks does step 1 co-ordinate?
3. Where are lessons learned captured after Phase F documents them?
4. Which two tables support step 5?
