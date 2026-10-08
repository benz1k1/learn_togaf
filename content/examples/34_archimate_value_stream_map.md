---
title: "Value Stream Map as an ArchiMate Value Stream view — Digital Channels"
deliverable: Value Stream Map as an ArchiMate view
phase: A
kind: MODEL
track: ARCHIMATE
summary: "The \"Obtain a loan\" value stream as five triggered stages, each realizing the outcome it adds and each served by the capabilities that enable it."
refs: ["ARCHIMATE §C.3", "CONTENT §3.6.3"]
figure: VALUE_STREAM_MAP.svg
viewpoint: Value Stream
artefacts: [VALUE_STREAM_MAP]
source: authored
status: draft
---

> **What to notice.** The Value Stream viewpoint shows a value stream, its stages, the capabilities that support each stage and the value created (ARCHIMATE §C.3). Two exam points live here. First, a stage's "value item" is an Outcome the stage *realizes* — the specification's own example ends its value stream at a business outcome (ARCHIMATE §7.4, Example 22). Second, a capability *serves* a stage; it does not realize it, because the stage is not made of the capability, it uses it.

## How to read the view

The middle row is the value stream: five chevrons from Apply to Service, joined by triggering arrows left to right. Above each stage is the purple Outcome it adds — application captured, credit decision made, offer accepted, funds credited, repayments collected — reached by a dashed realization line. Below each stage is the capability that enables it, with an open serving arrow pointing up; a second row of capabilities serves the first where the TOGAF map listed two per stage. The whole stream's trigger (the customer) and the value received (money in the account and a repayment plan) are in the note, because neither is an element the mapping allows here.

## Elements and why each type was chosen

| Element | ArchiMate type | Aspect / layer | Why that type |
|---|---|---|---|
| Apply, Assess, Approve, Disburse, Service | Value Stream | Strategy, behaviour | Stages are themselves value streams — a value-adding step from the customer's side, not a process with steps and roles (ARCHIMATE §7.2.3) |
| Application captured, Credit decision made, Offer accepted, Funds credited, Repayments collected | Outcome | Motivation | The value item each stage adds is an achieved result, so an Outcome; not a Value, which would say what it is *worth* rather than what it *is* (ARCHIMATE §6.3.4) |
| Customer Onboarding, Credit Assessment, Loan Origination, Payments, Loan Servicing, Identity Verification, Risk Management, Transfers | Capability | Strategy, behaviour | The same elements as the Capability Map, cross-mapped to the stages they enable |

## Relationships used

| From → to | Relationship | What it says |
|---|---|---|
| Stage → next stage | Triggering | The stage's completion starts the next |
| Stage → Outcome | Realization | The stage produces this result |
| Capability → Stage | Serving | The stage draws on the capability (ARCHIMATE §5.2.1) |
| Capability → Capability | Serving | Identity Verification serves Customer Onboarding, Risk Management serves Credit Assessment, Transfers serves Payments — the second enabler serves through the first |

The whole-stream element and its composition of stages are left out on purpose: composition is not in this artefact's mapping, and the Value Chain view already shows the same stages composed into the chain.

## What changed from the TOGAF drawing

TOGAF's map wrote "value: application captured" under each stage as text; the view makes each one an Outcome that can be traced to a goal in the Goal Realization view, so "funds credited" now has a path to "grow lending". The map listed capabilities under a stage with no relationship; the view forces a direction, and serving from capability to stage is the only one that fits. Where the map put two capabilities under one stage, the view had to say how they relate to each other as well, which produced the second row and three capability-to-capability serving lines — a small architectural decision the flat list never asked for. The trigger and the value received became a note, which is the honest answer when an artefact's element list has no place for them.

## Draw it yourself

1. Open a Value Stream view and add one Value Stream element per stage; connect them with triggering left to right.
2. Add an Outcome above each stage for its value item and draw realization from the stage to it.
3. Drag the enabling capabilities in from the Capability Map model — reuse the elements, do not recreate them — and draw serving from each to its stage.
4. Where two capabilities enable one stage, decide which one serves which and draw that instead of two lines to the stage.
5. Write the trigger and the end value in the view's documentation or a note.
