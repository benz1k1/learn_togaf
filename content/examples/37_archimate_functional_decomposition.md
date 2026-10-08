---
title: "Functional Decomposition Diagram as an ArchiMate Business Process Cooperation view — Digital Channels"
deliverable: Functional Decomposition Diagram as an ArchiMate view
phase: B
kind: MODEL
track: ARCHIMATE
summary: "Northgate Retail's functions as a three-level tree of Business Function elements, each composed of the ones beneath it."
refs: ["ARCHIMATE §8.3", "CONTENT §3.6.4"]
figure: FUNCTIONAL_DECOMPOSITION_DIAGRAM.svg
viewpoint: Business Process Cooperation
artefacts: [FUNCTIONAL_DECOMPOSITION_DIAGRAM]
source: authored
status: draft
---

> **What to notice.** A functional decomposition shows *what* the organisation does, not how — one page, a few levels, no sequence. ArchiMate's element for "what an organisation does, grouped by skill or resource" is the Business Function (ARCHIMATE §8.3.2), and a function may be composed of functions. The exam distinction is function versus process: a process is a sequence of behaviours producing a result and has a trigger; a function is behaviour grouped by criteria such as skill, and has none. A decomposition has no arrows of time in it, so every box is a function.

## How to read the view

A tree, top down. The root, "Northgate Bank — Retail", is composed of three level-1 functions; each of those is composed of three level-2 functions listed beneath it. Every line is composition: the filled diamond sits at the parent's edge. The lines to the second and third child turn a corner in the empty column so that they do not cross the first child. "(phase 1)" in a name replaces the heat-map colour: those five functions are in scope for the first phase of the change programme.

## Elements and why each type was chosen

| Element | ArchiMate type | Aspect / layer | Why that type |
|---|---|---|---|
| Northgate Bank — Retail | Business Function | Business, behaviour | The root of a functional tree is itself a function — everything the retail line does — not an actor, because the tree is about behaviour, not who performs it |
| Onboarding, Payments, Lending | Business Function | Business, behaviour | Level-1 groupings by skill |
| Identity verification, Account opening, KYC review, Transfers, Card authorisation, Settlement, Loan origination, Credit assessment, Loan servicing | Business Function | Business, behaviour | Level-2; still functions, because none of them has a start, an end or a sequence here |

Why not Capability? The Business Capability Map in Phase A used capabilities for a similar-looking tree. The difference is the question asked: the capability map asks what the enterprise *can* do and sits in the strategy layer; the functional decomposition asks what the organisation *does*, is owned by units and realizes services, and sits in the business layer. TOGAF keeps both artefacts, and so does the notation.

## Relationships used

| From → to | Relationship | What it says |
|---|---|---|
| Parent function → child function | Composition | The child is part of exactly one parent and does not exist outside it (ARCHIMATE §5.1.1) |

That is the whole list. A decomposition that needed serving or triggering would be a process map, not a decomposition.

## What changed from the TOGAF drawing

The TOGAF diagram nested boxes with no lines; ArchiMate allows nesting to stand for composition, but drawing the lines made one thing checkable that nesting did not: each child appears once and has one parent. The heat-map overlay, which said "phase 1" in colour, moved into the names. The other change is the root: TOGAF drew the enterprise as the outer box, and the notation asks what type that box is — an actor would be wrong because the tree is behaviour, so the root is a function too, and the Retail Banking actor that performs it is assigned to it in the Business Footprint view rather than here.

## Draw it yourself

1. Open a Business Process Cooperation view in Archi and add a Business Function for the root.
2. Add the level-1 functions and draw composition from the root to each.
3. Add the level-2 functions under their parent; nest them or draw composition from parent to child.
4. Give the functions in scope a property `phase = 1` and show it in the name or by colour rule.
5. Resist adding triggering between siblings; if you need it, the diagram you want is the Process Flow.
