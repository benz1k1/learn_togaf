---
title: "Data Dissemination Diagram as an ArchiMate Application Usage view — Digital Channels"
deliverable: Data Dissemination Diagram as an ArchiMate view
phase: C
kind: MODEL
track: ARCHIMATE
summary: "Which component holds which data for which business service: three Business Services served by three Application Components that access four Data Objects, each access labelled master, copy or cache."
refs: ["ARCHIMATE §C.1", "CONTENT §3.6.5"]
figure: DATA_DISSEMINATION_DIAGRAM.svg
viewpoint: Application Usage
artefacts: [DATA_DISSEMINATION_DIAGRAM]
source: authored
status: draft
---

> **What to notice.** Every dotted line ends in a label, and the labels are the point of the view. ArchiMate's **access** relationship (ARCHIMATE §5.2.2) says a component reads or writes a data object; it does not by itself say whether that copy is authoritative. The TOGAF Data Dissemination diagram (CONTENT §3.6.5) is *about* authority — solid boxes for the master, dashed for a replica — so the view puts `master`, `copy` and `cache` on the access lines and lets the arrowheads (read, write, both) say what each copy is allowed to do.

## How to read the view

Three tiers. The top row is the **business services** the data serves: Transfer funds, Open account, Authorise card payment. The middle row is the **application components** that serve them — solid arrowheads pointing up are **serving**. The bottom row is the **data objects**, and the dotted lines from the components downward are **access**.

Core Banking is drawn wide because it is the centre of the story: it serves two of the three services and holds the *master* of Customer, Account and Transaction, with a read-write arrowhead at each end. The Card Switch masters Card but only *reads* Account — a copy kept for authorisation limits. The Mobile App holds a read-only *cache* of Customer. Reading the labels together gives the sizing and criticality analysis the TOGAF artefact is for: three masters in one system, two replicas, and no data object with two masters, which is constraint CN-01 made visible.

## Elements

| Element | ArchiMate type | Aspect / layer | Why that type |
|---|---|---|---|
| Transfer funds, Open account, Authorise card payment | Business Service | behaviour, Business | The externally visible behaviour the data exists to support |
| Mobile App, Core Banking, Card Switch | Application Component | active structure, Application | The systems that hold and serve data |
| Customer, Account, Transaction, Card | Data Object | passive structure, Application | The logical entities of the Logical Data view |

## Relationships used

| Relationship | Notation | What it says here |
|---|---|---|
| Serving (component → business service) | solid line, open arrowhead | The component's functionality is used to deliver the service |
| Access, read-write, labelled `master` | dotted, arrowheads both ends | The authoritative copy; this component may change it |
| Access, read, labelled `copy` or `cache` | dotted, arrowhead at the component | A non-authoritative holding that expires |

Realization is also permitted by the mapping (a component realizing an application service, or a data object realizing a business object) but is left off to keep the view to the one question it answers.

## What changed from the TOGAF drawing

The TOGAF drawing nests the entities *inside* the component boxes and uses box styling for master versus replica. ArchiMate draws each data object once and connects it to every component that holds it, so a replica is not a second box but a second access line — the model has one Customer, not three. Serving replaces the TOGAF "entities feed services" arrows: in ArchiMate a data object cannot serve anything, so the service dependency runs through the component that holds it. The row order is flipped from the TOGAF drawing (services on top) to match the layered convention the Application Usage viewpoint expects.

## Draw it yourself

1. Create an *Application Usage* view; drag in the four Data Objects from the Logical Data view.
2. Add the three Application Components and three Business Services.
3. Draw Serving from each component up to the services it delivers.
4. Draw Access from each component to each data object it holds; in the relationship properties set the access type (read, write, read/write) and name the relationship `master`, `copy` or `cache`.
5. Sort the view by selecting all data objects and checking that each has exactly one `master` access — that is the CN-01 check.
