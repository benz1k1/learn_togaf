---
title: "Principles Catalog as an ArchiMate Motivation view — Digital Channels"
deliverable: Principles Catalog as an ArchiMate view
phase: PRELIM
kind: MODEL
track: ARCHIMATE
summary: "Northgate Bank's five architecture principles drawn as Principle elements that realize the goals they serve and are realized by the requirements their implications become."
refs: ["ARCHIMATE §6.4", "CONTENT §3.6.2"]
figure: PRINCIPLES_CATALOG.svg
viewpoint: Motivation
artefacts: [PRINCIPLES_CATALOG]
source: authored
status: draft
---

> **What to notice.** The Motivation viewpoint exists to show *why* an architecture is the way it is: which stakeholders, drivers, goals, principles and requirements sit behind it (ARCHIMATE §C.2). The exam asks you to tell the motivation elements apart — a Principle is a general property that applies to *any* system in a context, a Requirement is a property a *specific* system must have — and to know that the relationships between them are realization and influence, never assignment or serving. A catalog row becomes a chain of three elements; the statement, rationale and implication text does not disappear, it moves into the elements' documentation.

## How to read the view

Three purple rows, all in the motivation aspect. The top row holds four goals from the Business Principles, Goals and Drivers deliverable. The middle row holds the five principles of the catalog, PR-01 to PR-05, in the order that keeps the lines short. The bottom row holds one requirement per principle: the "implications" column of the catalog, turned into something a system can be checked against. Dashed lines with a hollow triangle are realization; read them upwards: the requirement realizes the principle, the principle realizes the goal. The two dashed lines with an open arrowhead and a "+" are influence — a principle that helps a second goal without being what achieves it (ARCHIMATE §5.2.3).

## Elements and why each type was chosen

| Element | ArchiMate type | Aspect / layer | Why that type |
|---|---|---|---|
| Stay compliant, Lower cost to serve, Grow mobile adoption, Reduce fraud losses | Goal | Motivation | An end state the bank intends to reach; the catalog's principles exist to serve these (ARCHIMATE §6.3.3) |
| PR-01 Data is an asset … PR-05 Channel independence | Principle | Motivation | A general, normative property of *all* Northgate systems — the definition of Principle, and exactly what a TOGAF principle is (ARCHIMATE §6.3.5) |
| Every data entity has a steward; Core Banking masters the customer record; Build only the Mobile App; One API per service; Threat model per change | Requirement | Motivation | The implication of a principle is a statement of need for a *specific* system, so it is a Requirement, not a second Principle (ARCHIMATE §6.3.6) |

The catalog's *statement* and *rationale* columns are not elements. In Archi they go into the Principle's documentation field; a rationale is not a Driver, and turning it into one would invent motivation the bank never recorded.

## Relationships used

| From → to | Relationship | What it says |
|---|---|---|
| Requirement → Principle | Realization | Meeting the requirement is how the principle is put into effect in one system |
| Principle → Goal | Realization | The principle is critical to reaching the goal; without it the goal is not achieved |
| PR-02 → Stay compliant, PR-05 → Reduce fraud losses | Influence (+) | The principle contributes to a goal it was not written for; the goal would still be reachable without it |

The choice between realization and influence is the one the exam tests: the specification says to use realization for relationships that are *critical* to the target and influence for those that are not (ARCHIMATE §5.2.3). One customer record helps compliance, but compliance does not depend on it — so influence.

## What changed from the TOGAF drawing

The TOGAF catalog is a table with four text columns and no links. The notation forces three things into the open. First, every principle must now point at a goal: a principle with no goal to realize is a warning that it is a preference, not a principle. Second, "implications" turns out to be two different things — a Requirement on a system (drawn) and advice to the architect (kept as text). Third, the sign matters: PR-03 *Buy before build* is drawn as realizing "lower cost to serve" but has no line to "grow mobile adoption", which is deliberate — the rationale says to build only where the bank differentiates, so the principle is neutral to that goal, and the view says so by leaving the line out.

## Draw it yourself

1. In Archi, create a Motivation view and add the four goals along the top from the Business Goals deliverable.
2. Add the five principles beneath; paste each catalog statement and rationale into the element's documentation.
3. Turn each implication into a Requirement, place it under its principle, and draw realization upwards.
4. Draw realization from each principle to the goal it exists for; add influence only where a principle helps a second goal, and set the "+" as the relationship's name.
5. Validate: every principle has exactly one realization to a goal, and no principle is realized by nothing.
