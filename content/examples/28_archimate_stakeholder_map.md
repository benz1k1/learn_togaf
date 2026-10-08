---
title: "Stakeholder Map as an ArchiMate Stakeholder view — Digital Channels"
deliverable: Stakeholder Map Matrix as an ArchiMate view
phase: A
kind: MODEL
track: ARCHIMATE
summary: "The five Digital Channels stakeholders, the concerns that move them, the assessments Phase A made and the goals those assessments push, drawn in the Stakeholder viewpoint."
refs: ["ARCHIMATE §C.2", "CONTENT §3.6.3"]
figure: STAKEHOLDER_MAP_MATRIX.svg
viewpoint: Stakeholder
artefacts: [STAKEHOLDER_MAP_MATRIX]
source: authored
status: draft
---

> **What to notice.** The Stakeholder viewpoint is the analyst's tool for the first weeks of an engagement: who has a stake, what drives them, what we found when we looked, and what goal follows (ARCHIMATE §C.2). Its allowed content is Stakeholder, Driver, Assessment and Goal plus association and influence. The exam trap is the concern: a stakeholder's *concern* is modelled as a Driver, not as a Requirement and not as a Goal — a driver is something that creates motivation, and "card authorisation latency" motivates the Card Ops Lead before anyone has decided what to do about it.

## How to read the view

Each row is one row of the TOGAF matrix, read left to right: the Stakeholder, the Driver that is their key concern, the Assessment Phase A made of that concern, and the Goal the assessment pushes. Plain lines are associations; dashed lines with an open head and a "−" are influence relationships carrying a negative sign, because every assessment here is a finding that works *against* the goal it points at. Two stakeholders share findings: the Compliance Officer and the Card Ops Lead both land on "fraud is scored overnight", and the CIO and the Branch Manager both push "lower cost to serve" — which the matrix could not show because each row was independent.

## Elements and why each type was chosen

| Element | ArchiMate type | Aspect / layer | Why that type |
|---|---|---|---|
| Head of Retail, CIO, Compliance Officer, Card Ops Lead, Branch Manager | Stakeholder | Motivation | A role with an interest in the outcome; not a Business Actor, which would put it in the business layer where it would have to *perform* something (ARCHIMATE §6.2.1) |
| Mobile adoption and cost to serve; Fit with the Core Banking roadmap; KYC and fraud controls; Card authorisation latency; Branch workload | Driver | Motivation | The matrix's "key concern" column — an external or internal condition that motivates, not yet a decision (ARCHIMATE §6.2.2) |
| The app can show but not do; Every channel is wired to Core Banking; Fraud is scored overnight; Counter onboarding takes 45 minutes | Assessment | Motivation | The result of analysing a driver: a SWOT-style finding, not a goal and not a requirement (ARCHIMATE §6.2.3) |
| Grow mobile adoption, Lower cost to serve, Reduce fraud losses | Goal | Motivation | The end state the finding argues for |

The matrix's *class* (key player, keep satisfied, keep informed) and *involvement* columns are written into the Stakeholder names in brackets. They are attributes, not elements; there is no ArchiMate concept for "power/interest class" and inventing one is exactly what the language customisation chapter warns against.

## Relationships used

| From → to | Relationship | What it says |
|---|---|---|
| Stakeholder — Driver | Association | This stakeholder holds this concern; the language has no stronger relationship for it |
| Driver — Assessment | Association | The assessment is *of* this driver |
| Assessment → Goal | Influence (−) | The finding counts against the goal; the sign is the relationship's name (ARCHIMATE §5.2.3) |

## What changed from the TOGAF drawing

The matrix had a fourth column, "artefacts needed", which is gone: which views a stakeholder receives is the viewpoint mechanism's job, so the Value Chain and Business Footprint that the Head of Retail asked for are simply the views drawn *from* this stakeholder's concerns (ARCHIMATE §14). The matrix also let two rows name overlapping concerns without noticing; the view forces a shared Driver or a shared Assessment, which is why one finding now has two stakeholders on it. Finally, the matrix stopped at concerns; the notation makes you say where each concern leads, so three goals appear that the matrix never listed.

## Draw it yourself

1. Create a Stakeholder view in Archi and add one Stakeholder per matrix row; put the class and involvement in the name or a property.
2. Add a Driver for each key concern and connect it to its stakeholder with an association.
3. For each driver, add the Assessment Phase A produced — a sentence of fact, not an aspiration.
4. Add the goals from the Business Goals deliverable and draw influence from each assessment to the goal it bears on, naming the relationship "−" or "+".
5. Check for duplicates: if two rows produce the same finding, merge the assessments so the shared concern is visible.
