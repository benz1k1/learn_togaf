---
title: "Application Communication Diagram as an ArchiMate Application Cooperation view — Digital Channels"
deliverable: Application Communication Diagram as an ArchiMate view
phase: C
kind: MODEL
track: ARCHIMATE
summary: "The six baseline components and the interfaces IF-01 to IF-06 between them as labelled Flows, the entities carried as Data Objects, and the one interface whose boundary matters as an Application Interface."
refs: ["ARCHIMATE §C.1", "CONTENT §3.6.6"]
figure: APPLICATION_COMMUNICATION_DIAGRAM.svg
viewpoint: Application Cooperation
artefacts: [APPLICATION_COMMUNICATION_DIAGRAM]
source: authored
status: draft
---

> **What to notice.** A TOGAF interface arrow becomes an ArchiMate **flow**: dashed line, filled arrowhead, labelled with what passes along it (ARCHIMATE §5.3.2). Flow is a *dynamic* relationship — it says something is transferred, not that one element depends on another — which is exactly the semantics of an application communication line. Every flow here carries the Interface catalog id and the data in transit, so the diagram and the catalog stay one artefact in two forms (CONTENT §3.6.6).

## How to read the view

The six **application components** are the ones on the TOGAF drawing, in the same positions: Mobile App and Core Banking across the top with the Data Warehouse to the right; the Card network, the Card Switch and the Fraud Engine along the bottom. The Card network is drawn as a component because, for this view, it is an external system that sends and receives messages; nothing about its inside is modelled.

Follow the flows in catalog order. IF-01 is the Mobile App calling Core Banking; IF-05 is the push alert going the other way, routed over the top so the two directions do not overprint. IF-02 is the Card Switch's queue to Core Banking, IF-03 the nightly batch to the warehouse, IF-04 the Card Switch calling the Fraud Engine, IF-06 the ISO 8583 link from the network. The unnamed *freeze card* flow is the one line that has no catalog row yet — a finding the target architecture fixes by routing it through the API layer.

**Transaction** and **Card** sit between the components as **data objects** with dotted **access** lines: Core Banking and the Card Switch write Transaction, the Fraud Engine and the warehouse read it. The **Scoring API** is the only **application interface** drawn, because it is the boundary the 150 ms latency budget of RQ-18 is measured at.

## Elements

| Element | ArchiMate type | Aspect / layer | Why that type |
|---|---|---|---|
| Mobile App, Core Banking, Card Switch, Fraud Engine, Data Warehouse, Card network | Application Component | active, Application | Encapsulated systems that communicate |
| Transaction, Card | Data Object | passive, Application | What the communication carries and stores |
| Scoring API (REST) | Application Interface | active, Application | The point of access where a contract and a latency budget apply |

## Relationships used

| Relationship | Notation | What it says here |
|---|---|---|
| Flow, labelled | dashed, filled arrowhead | Information transferred from sender to receiver; the label is the catalog row |
| Access (read / write) | dotted, small arrowhead | Which component reads or writes the entity in transit |
| Serving (interface → Card Switch) | solid, open arrowhead | The Fraud Engine's interface is what the Card Switch consumes |

## What changed from the TOGAF drawing

The TOGAF drawing draws the business service "Transfer funds" as a dashed association to the components; the Application Cooperation viewpoint has no business elements, so that link lives on the Application Usage views instead. The interface arrows become flows with the same labels; the entity names that were in the labels are now also elements, so the same Transaction object appears here and on the data views. The Scoring API is the one addition: the generator cannot nest an interface inside its component, so the composition that would normally tie it to the Fraud Engine is implied by placement and stated in this text rather than drawn.

## Draw it yourself

1. Create an *Application Cooperation* view and add the six components in the two rows shown.
2. Draw a Flow for each Interface catalog row, from sender to receiver, and name it `IF-nn type: data`.
3. Add the Transaction and Card Data Objects and draw Access from each component that reads or writes them, setting the access type.
4. Add the Scoring API as an Application Interface nested inside the Fraud Engine (Archi creates the composition for you) and draw Serving from it to the Card Switch.
5. Use bend-points to lift IF-05 above IF-01 so opposite-direction flows stay readable.
