---
title: "Benefits Diagram as an ArchiMate Outcome Realization view — Digital Channels"
deliverable: Benefits Diagram as an ArchiMate view
phase: E
kind: MODEL
track: ARCHIMATE
summary: "The six opportunities of the bubble chart as Work Packages and Deliverables that realize measurable Outcomes, which in turn realize or influence the four programme Goals."
refs: ["ARCHIMATE §C.2", "CONTENT §3.6.8"]
figure: BENEFITS_DIAGRAM.svg
viewpoint: Outcome Realization
artefacts: [BENEFITS_DIAGRAM]
source: authored
status: draft
---

> **What to notice.** A benefit is an **Outcome**: an end result, stated so it can be measured (ARCHIMATE §6.3.4). The TOGAF Benefits diagram (CONTENT §3.6.8) plots opportunities by size, benefit and complexity; the Outcome Realization viewpoint (ARCHIMATE §C.2) asks a different question of the same opportunities — *which goal does each one move, and by how much?* — and answers it with realization for the major projects and influence, with a sign, for the small ones.

## How to read the view

Three rows. The top row is the **Goals** from the Architecture Vision: grow the digital share of transfers, cut cost to serve, cut card fraud losses, retire end-of-life platforms. The middle row is the **Outcomes**, each named with its success measure from the Requirements Specification: SM-02 (60% of transfers in the app), SM-01 (ten-minute onboarding), SM-03 (fraud loss index from 100 to 70), and the Oracle warehouse retired in 2028. The bottom row is what delivers them: **Work Packages** WP-3, WP-2 and WP-4 from the roadmap and the warehouse replacement of the next cycle.

Solid columns are the major projects: each work package **realizes** its outcome and the outcome **realizes** its goal. The two opportunities the bubble chart placed in *quick wins* and *fill-ins* — statement e-delivery and branch tablets — are **Deliverables** with dashed **influence** lines marked `+`: they help the cost goal and the onboarding outcome but do not by themselves achieve either. The one cross-column line, SM-02 influencing cost to serve, is the £2.3m/yr lower cost of serving transfers in the app, a side benefit of a revenue project.

## Elements

| Element | ArchiMate type | Aspect / layer | Why that type |
|---|---|---|---|
| Grow digital share of transfers; Cut cost to serve; Cut card fraud losses; Retire end-of-life platforms | Goal | motivation | High-level intent from the Architecture Vision |
| SM-02, SM-01, SM-03, warehouse retired | Outcome | motivation | Measured end results — the benefits |
| WP-3, WP-2, WP-4, Warehouse replacement | Work Package | behaviour, Implementation & Migration | The projects that deliver the benefits |
| Statement e-delivery, Branch tablets | Deliverable | passive, Implementation & Migration | Small, bounded results that contribute without owning an outcome |

## Relationships used

| Relationship | Notation | What it says here |
|---|---|---|
| Realization (work package → outcome, outcome → goal) | dashed, hollow triangle | This is what achieves it |
| Influence `+` (outcome or deliverable → goal or outcome) | dashed, open arrowhead, signed | Contributes positively without being sufficient |

## What changed from the TOGAF drawing

The bubble chart's axes — complexity, benefit — and its bubble size have no ArchiMate notation and stay on the TOGAF tab; the quadrant a bubble sits in becomes the *kind of relationship* it gets (realize versus influence). Colour, which encoded benefit class (revenue, cost, risk, end-of-life), becomes the goal column. "Core Banking upgrade", a major project on the chart, is left off: it is an existing programme that enables WP-1 rather than a Digital Channels benefit, and the Implementation and Migration Plan records it as a dependency. The success-measure ids are added to the outcome names so the Board report and the model use one vocabulary.

## Draw it yourself

1. Create an *Outcome Realization* view; add the four Goals across the top.
2. Add an Outcome per success measure under the goal it serves and draw Realization upward.
3. Add the Work Packages and draw Realization to their outcomes.
4. Add the quick wins as Deliverables and draw Influence to the goal or outcome they help; set the relationship's *strength* to `+`.
5. For each influence, ask whether the contribution could be measured; if it can, promote it to an Outcome with its own realization — that is how a fill-in earns a row in the plan.
