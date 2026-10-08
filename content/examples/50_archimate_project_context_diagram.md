---
title: "Project Context Diagram as an ArchiMate Project view — WP-3 Mobile payments launch"
deliverable: Project Context Diagram as an ArchiMate view
phase: E
kind: MODEL
track: ARCHIMATE
summary: "Work package WP-3 at the centre: the roles and actors assigned to it, the deliverables it realizes, the work package that triggers it and the Transition 1 event it triggers."
refs: ["ARCHIMATE §C.4", "CONTENT §3.6.8"]
figure: PROJECT_CONTEXT_DIAGRAM.svg
viewpoint: Project
artefacts: [PROJECT_CONTEXT_DIAGRAM]
source: authored
status: draft
---

> **What to notice.** The TOGAF Project Context diagram puts one work package in the middle and surrounds it with everything it adds, changes or removes (CONTENT §3.6.8). The ArchiMate Project viewpoint (ARCHIMATE §C.4) has the same centre — a **Work Package** — but answers the question with three relationships instead of a colour legend: who is **assigned** to it, what it **realizes**, and what it **triggers**. Added, changed and removed become the *names of deliverables*; impacted units become the *actors assigned*.

## How to read the view

The middle row is the timeline. **WP-1 Platform and API layer** triggers **WP-3 Mobile payments launch** (solid line, filled arrowhead — WP-3 cannot start until the Payments API exists), and WP-3 triggers the **Implementation Event** "Transition 1 complete, 30 June 2027", the date fixed by the card re-issue.

The top row is who does the work. A **Business Role** (Product owner, Mobile) and two **Business Actors** (Retail IT delivery team, Cards Operations) are assigned to WP-3 — dot at the assignee, arrowhead at the package. Cards Operations is here because it owns the in-app card controls acceptance; the Branch Network, which the TOGAF drawing marks as impacted, is not assigned because it does no work on this package.

The bottom row is what comes out. WP-3 realizes three **Deliverables**: Mobile App v4 with transfers and card controls (the *added* application function), IF-01 re-pointed to the API layer (the *changed* interface), and the SMS gateway decommissioned (the *removed* component). WP-1's own deliverable, the Payments and Card Management APIs, is drawn so the trigger has a visible reason.

## Elements

| Element | ArchiMate type | Aspect / layer | Why that type |
|---|---|---|---|
| WP-1, WP-3 | Work Package | behaviour, Implementation & Migration | A series of actions with a start, an end and a result |
| Transition 1 complete | Implementation Event | behaviour, Implementation & Migration | A state change on the roadmap, dated |
| Product owner, Mobile | Business Role | active, Business | A responsibility, whoever fills it |
| Retail IT delivery team, Cards Operations | Business Actor | active, Business | Organisational units that do the work |
| Payments and Card Management APIs; Mobile App v4; IF-01 re-pointed; SMS gateway decommissioned | Deliverable | passive, Implementation & Migration | Precisely defined results of the work |

## Relationships used

| Relationship | Notation | What it says here |
|---|---|---|
| Assignment (role or actor → work package) | dot and filled arrowhead | Who performs the package |
| Realization (work package → deliverable) | dashed, hollow triangle | What the package produces |
| Triggering (work package → work package, → event) | solid, filled arrowhead | Sequence and dependency on the roadmap |

## What changed from the TOGAF drawing

The TOGAF drawing groups the surrounding elements by domain — organisation units, functions, applications, data and technology, processes — and tags each *added*, *impacted* or *removed*. The ArchiMate view cannot show those core elements here without leaving the Project viewpoint, so each becomes a deliverable whose name says what happens to it; the realization from deliverable to the architecture element (Mobile App v4 realizing the Mobile App component, say) is drawn on the Implementation and Migration view instead. The transition architecture the TOGAF drawing names in its subtitle becomes an event with a date, which is what the plan needs.

## Draw it yourself

1. Create a *Project* view and add WP-3 as a Work Package; add WP-1 to its left and the Transition 1 Implementation Event to its right.
2. Draw Triggering WP-1 → WP-3 → event.
3. Add the role and the two actors above and draw Assignment from each to WP-3.
4. Add a Deliverable for each added, changed or removed element and draw Realization from WP-3 to each.
5. Later, on the Implementation and Migration view, draw Realization from each deliverable to the application or technology element it changes — that closes the loop the TOGAF diagram draws with colours.
