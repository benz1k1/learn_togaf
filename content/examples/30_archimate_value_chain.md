---
title: "Value Chain Diagram as an ArchiMate Value Stream view — Digital Channels"
deliverable: Value Chain Diagram as an ArchiMate view
phase: A
kind: MODEL
track: ARCHIMATE
summary: "Northgate's primary activities as the stages of one value stream, the support activities as capabilities that serve them, and the outside parties as actors at the edges."
refs: ["ARCHIMATE §7.3", "CONTENT §3.6.3"]
figure: VALUE_CHAIN_DIAGRAM.svg
viewpoint: Value Stream
artefacts: [VALUE_CHAIN_DIAGRAM]
source: authored
status: draft
---

> **What to notice.** ArchiMate has no "value chain" element; Porter's chain is drawn with the Value Stream element and the Value Stream viewpoint (ARCHIMATE §7.3, §C.3). The exam distinction is Value Stream versus Business Process: a value stream is a sequence of *value-adding stages* seen from the customer, with no owner, no roles and no control flow; a process has all three. A support activity is not a stage — it is a Capability that *serves* the stages, which is why the diagram has two element types and not one.

## How to read the view

The wide chevron at the top is the whole value stream, "Serve a retail customer". Filled diamonds on its edge are compositions: it is made of the five stages beneath it, and the stages are chevrons too. The solid filled arrows between stages are triggering, left to right. The two rounded tan boxes below are capabilities — Porter's support activities — and the open arrows from them up to the stages are serving. Yellow rectangles are business actors: the market on the left, served customers on the right, and the Regulator and Card network where they touch the support capabilities. Plain lines to actors are associations.

## Elements and why each type was chosen

| Element | ArchiMate type | Aspect / layer | Why that type |
|---|---|---|---|
| Serve a retail customer | Value Stream | Strategy, behaviour | The chain as a whole; the stages compose into it (ARCHIMATE §7.2.3) |
| Attract customers, Onboarding, Payments, Lending, Service and retain | Value Stream | Strategy, behaviour | Each primary activity is a value-adding stage, not a process with steps |
| Risk and compliance; Technology and people | Capability | Strategy, behaviour | Support activities are abilities the bank possesses that the stages draw on; they are not stages in the customer's sequence (ARCHIMATE §7.2.2) |
| Customers (market), Customers (served), Regulator, Card network | Business Actor | Business, active structure | Parties outside the chain; drawn as actors because they act, they are not stakeholders with concerns here |

Choosing Capability for the support activities is the mapping decision that matters. TOGAF's chain shows them as long horizontal bars, which invites drawing them as a sixth and seventh stage. They are not sequential and the customer never sees them; a capability that serves every stage says that correctly.

## Relationships used

| From → to | Relationship | What it says |
|---|---|---|
| Whole → stage | Composition | The stage exists only as part of this chain |
| Stage → next stage | Triggering | One stage's completion starts the next |
| Capability → stage | Serving | The stage uses the capability; the capability does not know which stage calls it (ARCHIMATE §5.2.1) |
| Actor — stream / capability | Association | A party is involved; the language offers nothing stronger between an actor and a value stream |

## What changed from the TOGAF drawing

TOGAF's Phase A value chain is explicitly presentational: an orientation picture with no metamodel entity behind it. The view keeps that role but is now made of real elements, so the same Onboarding and Payments stages are the ones the Value Stream Map and the Capability Map refine. The support bars had to be split by *which* stages they serve — the risk capability serves onboarding and payments, technology serves payments, lending and service — a question the bars never asked. And the outside parties, which sat as free text at the edges, now need a relationship each; the honest answer is association, and admitting that is better than inventing a serving relationship the specification does not allow.

## Draw it yourself

1. In Archi, open a Value Stream view; add one Value Stream element for the whole chain and one per primary activity.
2. Nest the stages inside the whole or draw composition from the whole to each stage; connect consecutive stages with triggering.
3. Add a Capability for each support activity and draw serving from it to every stage that uses it — no more.
4. Add Business Actors for the market, the served customer, the regulator and the card network; connect with association.
5. Keep it to one screen: this is an orientation view and the Business Architecture phase will refine it.
