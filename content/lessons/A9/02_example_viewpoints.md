---
title: "The example viewpoints and when to use each"
unit: A9
objectives: ["A9.2"]
refs: ["ARCHIMATE §C.1", "ARCHIMATE §C.1.1", "ARCHIMATE §C.1.5", "ARCHIMATE §C.1.7", "ARCHIMATE §C.1.8", "ARCHIMATE §C.1.11", "ARCHIMATE §C.1.12", "ARCHIMATE §C.2", "ARCHIMATE §C.2.1", "ARCHIMATE §C.2.2", "ARCHIMATE §C.2.3", "ARCHIMATE §C.3", "ARCHIMATE §C.3.2", "ARCHIMATE §C.4", "ARCHIMATE §13.5"]
reading_minutes: 12
source: authored
status: draft
---
## Examples, not a catalogue

Appendix C is a set of *example* viewpoints: useful subsets of the metamodel, each aimed at
named stakeholders and concerns, with a purpose and a scope. The specification is explicit that
they are starting points — organisations should pick from them, modify them or define new ones —
and that they are tuned for architects, so other stakeholders may want a different representation
of the same content. In every viewpoint the grouping element and the two junctions may be used
even if unlisted (ARCHIMATE §C.1, ARCHIMATE §13.5).

## The basic viewpoints, in four categories

The basic viewpoints are grouped by the *direction* they look in (ARCHIMATE §C.1):

| Category | Looking at | Viewpoints | Scope |
|---|---|---|---|
| **Composition** | what elements are made of | Organization; Application Structure; Information Structure; Technology; Layered; Physical | single layer single aspect (Organization) up to multiple/multiple (Layered, Physical) |
| **Support** | what is supported by what, one layer up | Product; Application Usage; Technology Usage | multiple layers, multiple aspects |
| **Cooperation** | peers working together, across aspects | Business Process Cooperation; Application Cooperation | multiple/multiple; Application Cooperation is application layer only |
| **Realization** | what realizes what, one layer down | Service Realization; Implementation and Deployment | multiple layers, multiple aspects |

Each viewpoint is easiest to remember by the question it answers and the stakeholder who asks it
(ARCHIMATE §C.1):

| Viewpoint | Answers | For | Purpose |
|---|---|---|---|
| **Organization** | who are the departments, roles and collaborations, and where | enterprise, process and domain architects; managers | designing, deciding, informing |
| **Application Structure** | what components, interfaces and data make up an application | application and solution architects | designing |
| **Information Structure** | how business objects, data objects, artifacts and representations relate | domain and information architects | designing |
| **Technology** | what nodes, devices, system software, networks and paths exist | infrastructure architects, operational managers | designing |
| **Layered** | the whole stack: technology serving applications serving business | enterprise and all domain architects | designing, deciding, informing |
| **Physical** | equipment, facilities, distribution networks and materials, and how IT sits in them | infrastructure architects, operational managers | designing |
| **Product** | what services, contract and value a product bundles | product developers and managers, process and domain architects | designing, deciding |
| **Application Usage** | which application services serve which business processes | enterprise, process and application architects; operational managers | designing, deciding |
| **Technology Usage** | which technology services serve which applications | application and infrastructure architects; operational managers | designing |
| **Business Process Cooperation** | how processes depend on each other and their environment | process and domain architects, operational managers | designing, deciding |
| **Application Cooperation** | the application landscape: components, flows and services between them | enterprise, process, application and domain architects | designing |
| **Service Realization** | how business services are realized by processes (and applications) | process and domain architects, product and operational managers | designing, deciding |
| **Implementation and Deployment** | how applications map onto artifacts and technology | application and domain architects | designing, deciding |

**Trap — Application Structure versus Application Cooperation:** Structure looks *inside* one
application (its components, interfaces, data); Cooperation looks *between* applications (flows,
services offered and used). "Overview of the application landscape" is Cooperation
(ARCHIMATE §C.1.11).

**Trap — Layered:** the Layered viewpoint alternates dedicated layers (who does what) and service
layers (what is offered upward), stacked from technology to business in one diagram. It is the
viewpoint for consistency, impact of change and reduction of complexity across the *whole*
architecture, and its purpose covers all three categories (ARCHIMATE §C.1.5).

**Trap — Product versus Service Realization:** Product shows what is *bundled* for a customer,
including the contract; Service Realization shows what is *behind* a service — the processes that
realize it. Service Realization is the bridge between the product view and the process view
(ARCHIMATE §C.1.12, ARCHIMATE §C.1.7).

## Motivation viewpoints

The motivation viewpoints each isolate a slice of the motivation aspect (ARCHIMATE §C.2):

| Viewpoint | Elements | Answers |
|---|---|---|
| **Stakeholder** | stakeholder, driver, assessment, goal, outcome | who cares, what drives them, how those drivers are assessed, what initial goals follow |
| **Goal Realization** | goal, outcome, principle, requirement, constraint | how high-level goals refine into sub-goals (aggregation) and then into requirements and constraints (realization) |
| **Requirements Realization** | requirements and constraints plus core elements, strategy elements, value, meaning | which core elements realize which requirements |
| **Motivation** | every motivation element | the complete motivation picture, from stakeholder to requirement |

The list in the appendix also names a goal contribution viewpoint (influence relationships among
goals and requirements) and a principles viewpoint (principles and the goals that motivate them),
even though only the four above are given full descriptions (ARCHIMATE §C.2).

**Trap:** the Stakeholder viewpoint stops at *goals*; requirements are not in it. Goal Realization
adds requirements and constraints but has no stakeholders or drivers. A question that wants
"drivers, assessments and the goals that address them" is asking for Stakeholder; one that wants
"goals decomposed to requirements" is asking for Goal Realization (ARCHIMATE §C.2.1, ARCHIMATE
§C.2.2).

## Strategy viewpoints

| Viewpoint | Elements | Answers | For |
|---|---|---|---|
| **Strategy** | course of action, capability, value stream, resource, outcome | the high-level strategic picture | CxOs, business managers, enterprise and business architects |
| **Capability Map** | capability, resource, outcome | two or three levels of capabilities across the enterprise, often as a heat map | business managers, enterprise and business architects |
| **Value Stream** | value stream, capability, outcome, stakeholder | the value-creating stages and the capabilities behind each | business managers, enterprise and business architects |
| **Outcome Realization** | outcome, value, meaning, capability, value stream, resource, core element | how business results are produced by capabilities and core elements | business managers, enterprise and business architects |
| **Resource Map** | resource, capability, work package | two or three levels of resources, with the capabilities they support | business managers, enterprise and business architects |

Capability Map and Resource Map are the two that double as *heat maps* for investment decisions;
both are "designing, deciding" with a strategy scope (ARCHIMATE §C.3, ARCHIMATE §C.3.2).

## Implementation and migration viewpoints

Project (work packages, events, deliverables, actors, roles, goals, outcomes), Migration (plateaus
and gaps only) and Implementation and Migration (everything, including core elements) are treated
in the A8 lessons; here it is enough to recall that Migration is the only one whose purpose includes
designing and the only one with a two-element list (ARCHIMATE §C.4).

## Choosing a viewpoint: a method

1. Name the stakeholder and write down the concern in their words.
2. Fix the **purpose** — are they designing, deciding or being informed?
3. Fix the **content** — which layers and aspects the concern spans.
4. Match against the categories: inside one thing → Composition; what supports what → Support; peers → Cooperation; what is behind a service or application → Realization; why → Motivation; strategic direction → Strategy; change → Implementation and Migration.
5. Check the candidate's element list contains what the stakeholder needs and nothing they would find noise (ARCHIMATE §C.1).

## Worked choices

- A process owner asks which applications her order-to-cash process depends on: coherence,
  designing/deciding, business behaviour plus application services → **Application Usage**.
- An infrastructure architect asks whether the database cluster can carry the new applications:
  dependencies, performance, scalability → **Technology Usage**.
- A product manager asks what the "Gold Account" actually includes: services, contract, value →
  **Product**.
- A CFO asks where to invest: capabilities coloured by maturity → **Capability Map** as a heat map.
- A requirements manager asks which components satisfy the 24×7 availability requirement →
  **Requirements Realization** (ARCHIMATE §C.2.3).

## Check yourself

- Which basic viewpoint has single-layer, single-aspect scope?
- Which motivation viewpoint contains drivers and assessments but no requirements?
- Which two strategy viewpoints are commonly drawn as heat maps?
