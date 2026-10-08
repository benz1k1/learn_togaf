---
title: "Organization Decomposition Diagram as an ArchiMate Organization view — Digital Channels"
deliverable: Organization Decomposition Diagram as an ArchiMate view
phase: B
kind: MODEL
track: ARCHIMATE
summary: "Northgate's chain of command as a composition tree of business actors, each assigned to the roles it holds, nested in the location that houses it."
refs: ["ARCHIMATE §C.1", "CONTENT §3.6.4"]
figure: ORGANIZATION_DECOMPOSITION_DIAGRAM.svg
viewpoint: Organization
artefacts: [ORGANIZATION_DECOMPOSITION_DIAGRAM]
source: authored
status: draft
---

> **What to notice.** The Organization viewpoint shows the internal organisation of a company or department as actors, roles, collaborations and locations, usually as a nested or tree diagram (ARCHIMATE §C.1). The exam point is actor versus role: an actor is an *entity* that performs behaviour (Northgate Bank, Retail Banking, a teller as a person), a role is the *responsibility* it performs (Head of Retail, Teller). The org chart's boxes are actors; the job titles printed inside them are roles, joined by assignment; and the "@ Head Office" annotation is a Location.

## How to read the view

Pink areas are Locations, drawn behind the units they house: Head Office, the Operations Centre and the 42 branch sites. Inside them, yellow rectangles with the stick figure are business actors and the ones with the cylinder icon are roles. Filled diamonds are composition: Northgate Bank is composed of Retail Banking, Lending and Cards Operations; Retail Banking is composed of the Branch Network. The one hollow diamond is aggregation: the Branch Network aggregates the branch staff, who are people rather than a sub-unit. Lines with a dot at one end and a filled head at the other are assignment, from an actor to the role it holds.

## Elements and why each type was chosen

| Element | ArchiMate type | Aspect / layer | Why that type |
|---|---|---|---|
| Northgate Bank, Retail Banking, Lending, Cards Operations, Branch Network, Branch staff | Business Actor | Business, active | Organisational entities that perform behaviour; departments and groups of people are actors (ARCHIMATE §8.2.1) |
| Chief Executive, Head of Retail, Loan Officer, Card Ops Analyst, Branch Manager, Teller | Business Role | Business, active | Responsibilities an actor is assigned to; a role can be reassigned, an actor cannot (ARCHIMATE §8.2.2) |
| Head Office, Operations Centre, Branch (42 sites) | Location | Composite | A place; drawn as a container because nesting in a Location stands for the aggregation "site houses unit" (ARCHIMATE §4.5.2) |

The TOGAF diagram listed "actors: executive board, retail leadership, ops-centre staff, lending staff" per unit. Those are collective actors that would each aggregate into a unit the way Branch staff does; only the branch one is drawn because it is the one the Digital Channels programme changes, and the rest are named in the note.

## Relationships used

| From → to | Relationship | What it says |
|---|---|---|
| Unit → sub-unit | Composition | The chain of command: the sub-unit exists only inside its parent (ARCHIMATE §5.1.1) |
| Branch Network → Branch staff | Aggregation | The people are part of the network but exist independently of it |
| Actor → Role | Assignment | The unit holds this responsibility; the role's behaviour is drawn in the process views (ARCHIMATE §5.1.3) |
| Location ⊃ Actor | Aggregation by nesting | Drawn as containment rather than a line, which is the notation the specification allows for aggregation |

## What changed from the TOGAF drawing

The org chart mixed three things in one box — the unit, its site and its job titles — and the notation separates them into three element types with two relationship kinds between them. That separation shows something the chart hid: the Teller role is held by the branch staff, not by the Branch Network as a unit, which is exactly the role the target architecture changes (Teller loses Identity Checker and gains Assisted Onboarder). The chain-of-command lines, which the chart drew as plain connectors, had to be classified, and composition was the right answer for every one except the staff.

## Draw it yourself

1. Open an Organization view and add three Locations as large boxes for the sites.
2. Add a Business Actor per organisation unit inside its Location; nest sub-units or draw composition from parent to child.
3. Add a Business Role for each job title and draw assignment from the unit (or the staff actor) that holds it.
4. Where a unit contains people rather than a sub-unit, add a collective actor and use aggregation.
5. Check that every role has exactly one assignment in this view; a role nobody holds is a finding for Phase B's gap analysis.
