---
title: "Implementation and Migration Plan as an ArchiMate Implementation and Migration view — Digital Channels"
deliverable: Implementation and Migration Plan as an ArchiMate view
phase: F
kind: MODEL
track: ARCHIMATE
summary: "Five Work Packages in triggering order, the Deliverables each realizes, the two dated transition Implementation Events, and the Plateaus the deliverables realize."
refs: ["ARCHIMATE §C.4", "CONTENT §4.2.14", "ADM §10.4"]
figure: northgate_implementation_migration.svg
viewpoint: Implementation and Migration
artefacts: []
source: authored
status: draft
---

> **What to notice.** This is the Migration view with the *work* put back in. The Implementation and Migration viewpoint (ARCHIMATE §C.4) allows every implementation-and-migration element at once — Work Package, Deliverable, Implementation Event, Plateau, Gap — plus the core elements they touch, and the plan (CONTENT §4.2.14; ADM §10.4) needs all of them: the project breakdown is the work packages, the milestones are the events, and the two releases are the plateaus. Read the dashed lines upward and the solid lines left to right.

## How to read the view

The middle band is the schedule. **WP-1 Platform and API layer** (Oct 2026 – Mar 2027) **triggers** WP-3 Mobile payments and, diagonally below, WP-5 Dual-homing and pre-prod — the roadmap's "WP-1 → WP-3 and WP-5 in parallel". WP-3 triggers the **Implementation Event** "Transition 1 complete, 30 June 2027", which triggers WP-2 Digital onboarding; WP-5 triggers WP-4 Fraud scoring, because the regulator's DR rule says scoring may not go live on a single-homed link. WP-2 and WP-4 both trigger the second event, "Transition 2 complete, 15 December 2027". The dates in the package names are the plan's start and finish columns.

Above the schedule are the **Deliverables**, one per package, each **realized** by its package (dashed line, hollow triangle upward): the Payments and Card Management APIs, Mobile App v4 with the SMS gateway retired, the Identity Verification service, the Fraud Engine scoring before authorisation. WP-5's deliverable — the dual-homed link and pre-prod environment — sits below so its line does not cross the schedule.

At the top, the **Plateaus** from the Migration view. The two Transition 1 deliverables realize **Transition 1 — Q2 2027**; the two Transition 2 deliverables realize **Transition 2 — Q4 2027**; the plateaus trigger each other through to the Target. The event and the plateau with the same name are different things: the event is the *moment* the state is reached, the plateau is the *state*.

## Elements

| Element | ArchiMate type | Aspect / layer | Why that type |
|---|---|---|---|
| WP-1 to WP-5 | Work Package | behaviour, Implementation & Migration | The plan's projects, with dates |
| Five deliverables | Deliverable | passive, Implementation & Migration | The results the projects are charged to produce |
| Transition 1 complete, Transition 2 complete | Implementation Event | behaviour, Implementation & Migration | The milestones with a day attached |
| Transition 1, Transition 2, Target | Plateau | passive, Implementation & Migration | The states the deliverables bring about |

## Relationships used

| Relationship | Notation | What it says here |
|---|---|---|
| Triggering (work package → work package or event; event → work package; plateau → plateau) | solid, filled arrowhead | Sequence: this cannot start until that has finished |
| Realization (work package → deliverable) | dashed, hollow triangle | The package produces the deliverable |
| Realization (deliverable → plateau) | dashed, hollow triangle | The deliverable is part of what makes the state exist |

## What changed from the TOGAF drawing

The plan is prose and tables: strategy, then a project and portfolio breakdown with start, finish and milestones, then charters. The view is the breakdown table with the dependency column drawn instead of written. What the tables carry that the view does not — cost, resources, the PRINCE2 stage structure — stays in them; ArchiMate is not a scheduling notation, and the plan says so by keeping the Gantt in the PMO. The one addition is the realization from deliverable to plateau, which the plan implies by grouping projects under a release and the view states outright.

## Draw it yourself

1. Create an *Implementation and Migration* view; drag in the Plateaus from the Migration view rather than creating new ones.
2. Add the five Work Packages with dates in the name and draw Triggering along the plan's dependency column.
3. Add the two Implementation Events and wire them into the sequence.
4. Add a Deliverable per package; draw Realization from package to deliverable and from deliverable to its plateau.
5. Check that every deliverable reaches a plateau and every plateau is reached by at least one — an unreached plateau is a release with no content, an unreaching deliverable is scope creep.
