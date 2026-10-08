---
title: "The Strategy, Capability Map, Value Stream and Outcome Realization viewpoints"
unit: A3
objectives: ["A3.3"]
refs: ["ARCHIMATE §C.3", "ARCHIMATE §C.3.1", "ARCHIMATE §C.3.2", "ARCHIMATE §C.3.3", "ARCHIMATE §C.3.4", "ARCHIMATE §C.3.5", "ARCHIMATE §13.4.1", "ARCHIMATE §7.3.1", "ARCHIMATE §7.3.2", "ARCHIMATE §7.4"]
reading_minutes: 8
source: authored
status: draft
---
## What a viewpoint description contains

Each example viewpoint in Appendix C is described the same way: the stakeholders it addresses,
their concerns, its purpose (a selection from *designing*, *deciding*, *informing*), its scope,
and the list of elements it admits. The strategy viewpoints each take a different perspective on
the high-level direction and make-up of the enterprise, and each uses only a subset of the
strategy and motivation elements (ARCHIMATE §C.3, §13.4.1).

Five strategy viewpoints are defined. The objective names four; the fifth, Resource Map, is
included because it is the obvious distractor (ARCHIMATE §C.3).

| Viewpoint | Elements | Purpose | Stakeholders | Concern |
|---|---|---|---|---|
| **Strategy** | Course of Action, Capability, Value Stream, Resource, Outcome | designing, deciding | CxOs, business managers, enterprise and business architects | strategy development |
| **Capability Map** | Outcome, Capability, Resource | designing, deciding | business managers, enterprise and business architects | architecture strategy and tactics, motivation |
| **Value Stream** | Value Stream, Capability, Outcome, Stakeholder | designing, deciding | business managers, enterprise and business architects | architecture strategy and tactics, motivation |
| **Outcome Realization** | Capability, Value Stream, Resource, Outcome, Value, Meaning, core elements | designing, deciding | business managers, enterprise and business architects | business-oriented results |
| **Resource Map** | Resource, Capability, Work Package | designing, deciding | business managers, enterprise and business architects | architecture strategy and tactics, motivation |

All five share the scope *Strategy* and the purposes *designing* and *deciding*; none is an
*informing* viewpoint (ARCHIMATE §C.3.1–§C.3.5).

## Strategy viewpoint

The Strategy viewpoint gives the Business Architect a high-level overview of the enterprise's
strategies — its courses of action — together with the capabilities, value streams and resources
that support them and the outcomes envisaged. It is the only one of the five that admits Course of
Action, and the one to pick when the question is "how do we get from our goals to what we will do"
(ARCHIMATE §C.3.1). Its natural content is the specification's first strategy example: courses of
action realized by capabilities, resources assigned to them, outcomes produced (ARCHIMATE §7.4).

**Trap:** "Which viewpoint shows courses of action?" — Strategy, and only Strategy, among the
strategy viewpoints (ARCHIMATE §C.3.1).

## Capability Map viewpoint

A capability map is a structured overview of the enterprise's capabilities, typically two or three
levels deep across the whole enterprise, built with composition or aggregation of capabilities. Its
best-known use is as a **heat map** for identifying areas of investment; it may also show the
outcomes specific capabilities deliver, and resources. Elements: Outcome, Capability, Resource
(ARCHIMATE §C.3.2). Capability names should say *what* the enterprise does, not how — compound
nouns or gerunds (ARCHIMATE §7.3.1).

**Trap:** which viewpoint is used as a heat map to find where to invest? Capability Map — and the
Resource Map says the same thing about resources. If the option mentions capabilities, it is the
Capability Map (ARCHIMATE §C.3.2, §C.3.5).

## Value Stream viewpoint

The Value Stream viewpoint gives a structured overview of one value stream: its stages, the
capabilities that support each stage, the value created, and the stakeholders involved. Elements:
Value Stream, Capability, Outcome, Stakeholder. Stages are value stream elements linked by flow;
capabilities *serve* stages; the end of the stream realizes an outcome for a stakeholder — the
cross-mapping pattern of the specification's insurance example (ARCHIMATE §C.3.3, §7.3.2, §7.4).

**Trap:** this viewpoint is about a *value stream*, not a business process. If a scenario asks for
the time-ordered steps with decision points for handling one case, the answer is a business process
view, not the Value Stream viewpoint (ARCHIMATE §7.3.2).

## Outcome Realization viewpoint

The Outcome Realization viewpoint shows how the highest-level, business-oriented results are
produced by the capabilities and the core elements beneath them. It is the widest of the five: it
admits Capability, Value Stream, Resource and Outcome, plus **Value** and **Meaning** from the
motivation aspect, plus **core elements** — the processes, actors and applications that realize
the capabilities. Its concern is business-oriented results, its purpose designing and deciding
(ARCHIMATE §C.3.4).

**Trap:** which of the strategy viewpoints admits core elements? Only Outcome Realization. Which
admits Value and Meaning? Only Outcome Realization (ARCHIMATE §C.3.4).

## Resource Map viewpoint

A resource map mirrors the capability map for resources: two or three levels of resources across
the enterprise, usable as a heat map, and optionally showing the capabilities the resources are
assigned to. It is the only strategy viewpoint that admits **Work Package**, so an option listing
"Resource, Capability, Work Package" is the Resource Map (ARCHIMATE §C.3.5).

## Choosing between them

| The question asks for… | Pick |
|---|---|
| the enterprise's strategies and what supports them | Strategy |
| where to invest, by capability, as a heat map | Capability Map |
| how value flows through stages and which capabilities enable each | Value Stream |
| how a business outcome is actually produced, down to the core | Outcome Realization |
| an inventory of assets and the capabilities they are assigned to | Resource Map |

(ARCHIMATE §C.3)

## Classifying them on the purpose and content dimensions

The viewpoint mechanism classifies viewpoints by *purpose* — designing (diagrams for architects),
deciding (cross-domain insight for managers), informing (explaining to any stakeholder) — and by
*content* — details (one layer, one aspect), coherence (several layers or aspects), overview
(several of both). All five strategy viewpoints are designing/deciding; the Outcome Realization
viewpoint, spanning strategy, motivation and core, is the overview-level one (ARCHIMATE §13.4.1,
§C.3.4).
