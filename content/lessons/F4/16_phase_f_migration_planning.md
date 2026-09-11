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

> **Trap.** Phase F is where "draft" becomes "finalized" and "approved". Any option that has
> the Architecture Definition Document, Architecture Requirements Specification or Architecture
> Roadmap *finalized* in Phase E or D is wrong. Equally, the Implementation Governance Model is a
> Phase F output (optional) and a Phase G input — not the other way round.

> **Trap.** Step 4's wording is "cost/benefit assessment **and risk assessment**" — the exam may
> offer "risk validation" or "benefit realization" as near-miss wording. And Phase F's business
> value technique is the Business Value and Risk Matrix (step 2), not the Benefits Diagram.

## Check yourself

1. Which two Phase E outputs enter Phase F as drafts, and what does Phase F call them on the way out?
2. Which four management frameworks does step 1 co-ordinate?
3. Where are lessons learned captured after Phase F documents them?
4. Which two tables support step 5?
