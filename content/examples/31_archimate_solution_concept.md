---
title: "Solution Concept Diagram as an ArchiMate Layered view — Digital Channels"
deliverable: Solution Concept Diagram as an ArchiMate view
phase: A
kind: MODEL
track: ARCHIMATE
summary: "The Phase A pencil sketch redrawn as a Layered view: three business services, the new and existing components that realize and serve them, and the nodes underneath."
refs: ["ARCHIMATE §C.1", "CONTENT §3.6.3"]
figure: SOLUTION_CONCEPT_DIAGRAM.svg
viewpoint: Layered
artefacts: [SOLUTION_CONCEPT_DIAGRAM]
source: authored
status: draft
---

> **What to notice.** The Layered viewpoint is the one the exam shows most: several layers in one picture, each layer's services used by the layer above, structure realizing behaviour (ARCHIMATE §C.1). It is the natural home for a solution concept because a concept *is* a claim about which layers change. The two things to get right are the direction of realization (concrete component up to abstract service) and the direction of serving (provider to consumer, so the technology node points *up* at the component it hosts).

## How to read the view

Three dashed groupings label the layers. The Customer actor sits above the business layer, served by the three business services — one per objective on the sketch. In the application layer the top row holds the new components (and the one the sketch marked "buy or build — investigate in Phase C") and the bottom row the existing ones; dashed hollow-triangle lines from a component up to a service are realization, open arrows between components are serving. The technology layer holds three nodes, each serving the component above it. Everything the sketch marked "existing" or "new" keeps that word in its name, because the Layered viewpoint has no colour for state — that is what Phase E's Migration view is for.

## Elements and why each type was chosen

| Element | ArchiMate type | Aspect / layer | Why that type |
|---|---|---|---|
| Customer | Business Actor | Business, active | The person who uses the services; an actor, not a stakeholder, because here they act (ARCHIMATE §8.2.1) |
| Open an account in under 10 minutes; Pay from the phone; Block a fraudulent card within 5 seconds | Business Service | Business, behaviour | The sketch's objectives are things the bank exposes to the customer — services, each with its measure in the name |
| Mobile App (new), API layer (new), Fraud Engine (new), Identity verification (buy or build?), Core Banking (existing), Card Switch (existing) | Application Component | Application, active | Encapsulated pieces of software; "new" and "existing" are kept in the name, not in a type |
| Mainframe (existing), Bank private cloud (new), Card network gateway (external) | Node | Technology, active | Computational resources that host components; the gateway is a node because the bank only sees an endpoint |
| Business layer, Application layer, Technology layer | Grouping | Composite | Purely visual layer labels; a grouping carries no semantics of its own (ARCHIMATE §4.5) |

## Relationships used

| From → to | Relationship | What it says |
|---|---|---|
| Business Service → Customer | Serving | The customer uses the service |
| Application Component → Business Service | Realization | The component is (part of) what makes the service real — a derived realization across the layers (ARCHIMATE §5.7) |
| Component → Component | Serving | Core Banking, the Card Switch and identity verification serve the API layer; the API layer serves the Mobile App; the Fraud Engine serves the Card Switch |
| Node → Application Component | Serving | The technology hosts the component; ArchiMate 3 draws hosting as serving, not assignment |

## What changed from the TOGAF drawing

The sketch had a question mark and a dashed box for identity verification; the view cannot draw doubt, so the doubt moves into the element's name and the element itself is committed — that is the point where a Phase A picture starts becoming a Phase C model. The sketch's "REST" and "balances, transfers" labels on the lines vanish: interfaces and data are Phase C content, and a Layered view of a concept should say *which* components talk, not how. The constraints written on the sketch (keep Core Banking as the system of record, no new data stores) are not on the view either; they belong in the Motivation view as Constraint elements, and the Requirements Realization view will connect them.

## Draw it yourself

1. Create a Layered view in Archi and draw three Groupings named for the layers; put the Customer actor above them.
2. Add one Business Service per objective on the sketch, in the business grouping, and draw serving from each to the Customer.
3. Add the six application components; draw realization up to the service each helps deliver and serving between the components that call each other.
4. Add a Node per hosting platform and draw serving from node to component.
5. Do not colour anything for new/existing; put the state in the name and let Phase E's Migration view carry it.
