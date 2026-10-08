---
title: "Two-way traceability: top-down justification and bottom-up completeness"
unit: S7
objectives: ["S7.1"]
refs: ["SABSA §6", "SABSA §3.3", "SABSA §5", "GUIDE:integrating-risk-and-security §5.10.1", "GUIDE:integrating-risk-and-security §5.10.2"]
reading_minutes: 9
source: authored
status: draft
---
## What traceability means in SABSA

SABSA claims that a security architecture is *business-driven*, and traceability is how the claim is checked. Every element in every layer of the Matrix must be connected to the layer above it and the layer below it, so that a reader can start anywhere — a business driver, an attribute, a service, a mechanism, a product, an operational procedure — and walk the chain in either direction. When the chain runs unbroken from the Contextual layer to the Component and Service Management layers, the architecture is **traceable** (SABSA §6, §3.3).

The chain is read in two directions, and each direction answers a different question:

| Direction | Question | Failure it catches |
|---|---|---|
| **Top-down** (justification) | *Why does this control exist?* Walk from a component up through mechanism, service and attribute to a business driver | Controls with no business reason: legacy products, checklist items, gold-plating |
| **Bottom-up** (completeness) | *Is every requirement actually met?* Walk from a business attribute down to the service, mechanism, component and operational measurement that satisfy it | Requirements with no control: attributes that were agreed and never delivered; targets nothing measures |

(SABSA §6.)

**Trap:** one direction is not enough. A top-down check can pass on an architecture that omits half its attributes, because it only inspects what exists; a bottom-up check can pass on an architecture stuffed with unjustified controls, because it only inspects what was asked for. SABSA requires *both*, which is why it says two-way (SABSA §6).

## Top-down: justification

Start at any control and ask "because of what?" repeatedly:

1. *Why this log-management product?* Because the design calls for tamper-evident access logging (mechanism).
2. *Why that mechanism?* Because the Logical layer specifies an audit service over identity evidence (service).
3. *Why that service?* Because the Business Attributes Profile contains *Auditable* with a target of every access reconstructable for two years (attribute).
4. *Why that attribute?* Because a regulator requires it and the business has chosen to be *Compliant* (driver, Contextual layer).

A control that cannot reach step 4 is unjustified. The cure is either to find the driver it serves and record the link, or to remove the control. This is also SABSA's answer to "why does security cost so much": with top-down traceability, every cost line has a business reason attached (SABSA §6, §5).

## Bottom-up: completeness

Start at each attribute in the profile and ask "delivered by what?" until you reach something operational:

1. *Available* — target 99.9 % — delivered by which service? Resilience and recovery.
2. Delivered by which mechanisms? Clustered hosting; replicated storage; tested restore procedure.
3. Realised by which components? Named platform features, backup product, runbook.
4. Measured by what in Service Management? Uptime monitoring and monthly restore tests.

An attribute that stops at step 1 is a promise the architecture does not keep. An attribute that reaches step 3 but not step 4 is delivered but unproven, and the assurance framework (next lesson) will have nothing to report (SABSA §6, §3.6).

**Trap:** completeness is checked per *attribute*, not per *layer*. "We have a full Physical layer" says nothing about whether *Recoverable* is covered. The bottom-up walk always starts from the Business Attributes Profile because that is where the business's requirements are (SABSA §5, §6).

## The traceability chain as the TOGAF guide sees it

The TOGAF risk and security guide describes the same chain from the Requirements Management side: business attribute profiling translates goals and drivers into requirements with metrics and targets, and *control objectives* are derived from business objectives so that each control can be traced back to something the business wanted. Read that alongside SABSA and the vocabulary lines up (GUIDE:integrating-risk-and-security §5.10.1, §5.10.2):

| SABSA | TOGAF risk and security guide |
|---|---|
| Business driver (Contextual) | Business driver / business objective |
| Business attribute with target (Conceptual) | Requirement from Business Attribute Profiling, with metric and target |
| Security service (Logical) | Control objective; security service as an ABB |
| Mechanism and component | Control; SBB |
| Measurement (Service Management) | Compliance review; performance measurement in the Governance Log |

## Traceability and change

Traceability is worth most when something changes. A new regulation arrives: walk top-down from the driver to see which attributes, services and controls it touches. A product is retired: walk bottom-up from the attributes its mechanisms served to see what must be replaced before it goes. A change request in Phase H: its impact is the set of chain links it breaks. Without the recorded chain each of these becomes an investigation; with it, each is a query (SABSA §6, §4; GUIDE:integrating-risk-and-security §5.9).

## Recording the chain

SABSA does not mandate a tool, but it does expect the links to be *written down*, not held in an architect's head. Practical forms are a traceability matrix (attributes as rows, services as columns, then services × mechanisms, mechanisms × components), a requirements repository with parent links, or an ArchiMate model in which Requirement elements are realised by the core elements that satisfy them — unit X3 draws exactly that (SABSA §6).

## Check yourself

- State the question each traceability direction answers and the failure it catches.
- Why is a top-down check alone insufficient?
- What does the bottom-up walk always start from, and where must it end?

*Source note: written from the SABSA framework as published by the SABSA Institute; section numbers refer to the SABSA White Paper and are to be verified against the registered PDF.*
