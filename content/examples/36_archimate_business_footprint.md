---
title: "Business Footprint Diagram as an ArchiMate Layered view — Digital Channels"
deliverable: Business Footprint Diagram as an ArchiMate view
phase: B
kind: MODEL
track: ARCHIMATE
summary: "One goal traced down through the services that realize it, the functions that realize the services, the unit assigned to them and the application components that serve them."
refs: ["ARCHIMATE §C.1", "CONTENT §3.6.4"]
figure: BUSINESS_FOOTPRINT_DIAGRAM.svg
viewpoint: Layered
artefacts: [BUSINESS_FOOTPRINT_DIAGRAM]
source: authored
status: draft
---

> **What to notice.** The Business Footprint is TOGAF's CxO traceability picture: one goal, and the organisation, functions, services and technical components that deliver it. ArchiMate has no footprint viewpoint; the Layered viewpoint fits because it is defined for exactly this — several layers in one view, with realization and serving between them (ARCHIMATE §C.1). The exam tests the two cross-layer relationships: a business function *realizes* a business service (behaviour to the service it exposes), and an application component *serves* a business function (a lower layer providing to a higher one). Neither is assignment.

## How to read the view

Top-down. The purple Goal is the one the Head of Retail sponsors. Two yellow pill shapes are the business services that realize it (dashed, hollow triangle, pointing up). Below them, two rounded yellow boxes are the business functions that realize the services, with the Retail Banking actor between them and assignment lines (dot to filled head) to both. The bottom row is the three application components; open serving arrows point up to the functions they support. Core Banking serves both functions, the Mobile App serves onboarding and the Card Switch serves payments.

## Elements and why each type was chosen

| Element | ArchiMate type | Aspect / layer | Why that type |
|---|---|---|---|
| Grow mobile adoption: 60% of transfers via the Mobile App by 2027 | Goal | Motivation | The footprint starts from a goal; the objective's measure is kept in the name so the CxO sees the number |
| Open account, Transfer funds | Business Service | Business, behaviour | What the bank exposes to the customer; services are realized, never assigned (ARCHIMATE §8.3.5) |
| Onboarding, Payments | Business Function | Business, behaviour | The functions TOGAF's footprint names; behaviour grouped by skill, not by sequence (ARCHIMATE §8.3.2) |
| Retail Banking | Business Actor | Business, active | The organisation unit that owns the functions; an actor because it performs, not a stakeholder |
| Mobile App, Core Banking, Card Switch | Application Component | Application, active | The "technical components" of the footprint are software, so application components rather than nodes |

## Relationships used

| From → to | Relationship | What it says |
|---|---|---|
| Business Service → Goal | Realization | Delivering the service is how the goal is reached (ARCHIMATE §6.5) |
| Business Function → Business Service | Realization | The function is the internal behaviour behind the exposed service |
| Business Actor → Business Function | Assignment | Retail Banking performs both functions (ARCHIMATE §5.1.3) |
| Application Component → Business Function | Serving | The component supports the function; it does not perform it |

## What changed from the TOGAF drawing

TOGAF's footprint labelled its connectors "is owned by / pursued by" and "is delivered by". Each of those had to become one of the eleven relationship types, and the first split in two: "pursued by" between the goal and the unit has *no* direct ArchiMate relationship, because an actor does not realize a goal — the services do, and the actor is assigned to the functions behind them. The goal therefore connects to Retail Banking only through the chain, which is a better statement of accountability than the arrow was. "Is delivered by" split into realization (function to service) and serving (component to function), and the fact that the Mobile App does not serve the Payments function on this view is a gap the Phase C Application Cooperation view has to close.

## Draw it yourself

1. Open a Layered view in Archi; put the Goal at the top with its measure in the name.
2. Add the business services that realize it and draw realization upward.
3. Add the business functions beneath; draw realization from function to service.
4. Add the organisation unit as a Business Actor and assign it to each function.
5. Add the application components and draw serving up to the functions they support; stop there — the footprint is a summary, and the Phase C views carry the detail.
