---
title: "Modelling a Northgate Bank artefact as an ArchiMate view, in Archi"
unit: X1
objectives: ["X1.2"]
refs: ["ARCHIMATE §C.1", "ARCHIMATE §9.2", "ARCHIMATE §9.4", "ARCHIMATE §5.2", "ARCHIMATE §5.3", "ARCHIMATE §13.4", "ARCHIMATE §D.1", "WP:w14c §4"]
reading_minutes: 10
source: authored
status: draft
---
## The artefact we will model

Northgate Bank's Phase C work produced an Architecture Definition Document chapter with a target Application Architecture: a new API layer replacing eleven point-to-point interfaces, a Mobile App v4 that can pay and onboard, a bought Identity Verification service, a bought Fraud Engine scoring in real time, and an SMS gateway to be retired at Transition 1. The TOGAF artefact that shows components and what flows between them is the **Application Communication Diagram**. Its `archimate` mapping on `/artefact` says: viewpoint *Application Cooperation*; elements Application Component, Application Interface, Data Object; relationships Flow, Serving, Access. This lesson builds that view (ARCHIMATE §C.1; WP:w14c §4).

The finished models of the case enterprise are collected under `/example?track=ARCHIMATE`; this lesson is the method behind them.

## Step 1 — choose the viewpoint before touching the tool

An ArchiMate viewpoint fixes the stakeholders, the concerns, the abstraction level and the permitted element types. The Application Cooperation viewpoint is for application architects and the concerns are dependencies and information exchange between applications; its elements are the application layer's active and passive structure plus the relationships between them. Choosing it first stops the diagram absorbing every element someone mentions. If a needed concept is not in the viewpoint's element set — a Node, say — that is a signal to make a second view, not to widen the first (ARCHIMATE §13.4, §C.1).

**Trap:** a view is not a diagram file. The *model* holds the elements once; a view is a selection of them drawn for one concern. In Archi, elements live in the model tree and can appear in many views; deleting an element from a view (remove from view) is not deleting it from the model (delete from model). Confusing the two either loses model content or leaves orphaned elements (ARCHIMATE §13.3).

## Step 2 — create the elements in the model tree

In Archi (the free, open-source ArchiMate tool from the Archi project), create a new model, then under *Application* add the components. Use the content-metamodel mapping from lesson 1: a TOGAF Logical Application Component is an ArchiMate Application Component.

| TOGAF entity in the ADD | ArchiMate element | Name |
|---|---|---|
| Logical Application Component | Application Component | Mobile App v4 |
| Logical Application Component | Application Component | API Layer |
| Logical Application Component | Application Component | Identity Verification Service (bought) |
| Logical Application Component | Application Component | Fraud Engine (bought) |
| Logical Application Component | Application Component | Core Banking |
| Logical Application Component (baseline, eliminated) | Application Component | SMS Gateway |
| Interface in the Interface Catalog | Application Interface | Payments API, Onboarding API |
| Logical Data Component | Data Object | Journey-State Token, Identity Evidence, Fraud Score |

(ARCHIMATE §9.2, §9.4; WP:w14c §3.)

Give each element a *documentation* property with the ADD reference (for example "ADD-2026-01 v0.2 ch. 5c") so that the model is traceable to the deliverable it draws. Archi's Properties tab takes free key–value pairs, which is the ArchiMate language-customization mechanism of adding attributes (ARCHIMATE §14.1).

## Step 3 — draw the relationships, and only the permitted ones

Create a view, set its viewpoint to Application Cooperation in the view's properties (Archi then greys out elements the viewpoint excludes), and drag the elements in. Now the relationships — and this is where the ArchiMate discipline pays for itself.

| From | Relationship | To | Why this one |
|---|---|---|---|
| API Layer | Composition | Payments API, Onboarding API | An interface is part of the component that exposes it |
| API Layer | Serving | Mobile App v4 | The layer provides services the app uses |
| Identity Verification Service | Serving | API Layer | Likewise, one level down |
| Fraud Engine | Serving | API Layer | |
| API Layer | Access (write) | Journey-State Token | The component creates and updates the token |
| Identity Verification Service | Access (read/write) | Identity Evidence | |
| Fraud Engine | Access (write) | Fraud Score | |
| Mobile App v4 | Flow | API Layer | The *what flows* label: payment instruction, onboarding data |
| Core Banking | Flow | Fraud Engine | Transaction events for scoring |

(ARCHIMATE §5.2, §5.3.)

Use **Serving** for "provides functionality to" and **Flow** for "information passes from A to B"; the two are the commonest confusion on Part 1 papers. Use **Access** only from behaviour or active structure to a passive element, never between two components. Archi enforces the relationship table: if it refuses a connection, the model, not the tool, is telling you the concept is wrong (ARCHIMATE §5.2, §5.3, §B.5).

**Trap:** do not draw Association because you are unsure. Association is the weakest relationship and carries no meaning the reader can rely on. If the meaning is "serves", draw Serving; if it is "flows", draw Flow; if you truly cannot say, the artefact is not finished (ARCHIMATE §5.4).

## Step 4 — show baseline, target and the gap without a second diagram

The ADD's application gap table lists *New*, *Changed* and *Eliminated* items. ArchiMate has elements for exactly this: two **Plateaus** (Baseline 2026, Transition 1) and a **Gap** between them, with the SMS Gateway associated to the Gap as the thing eliminated and the API Layer as the thing new. In Archi, add the Plateaus and Gap from the *Implementation & Migration* palette; the Application Cooperation viewpoint does not include them, so this becomes a second view — the **Migration** view of the same model — which is the Phase E viewpoint from lesson 1 (ARCHIMATE §12.2, §C.4).

## Step 5 — check against the TOGAF artefact and export

Read the finished view against the Application Communication Diagram's purpose: does every component the ADD names appear; is every point-to-point interface either drawn or shown as replaced by the API Layer; does each Flow carry a label that names the data? Then export: Archi's *Report → HTML* gives the stakeholder-readable view, and *File → Export → Model to Open Exchange File* produces the ArchiMate Model Exchange Format file that any conforming tool can import — which is what makes the model, rather than the picture, the deliverable (ARCHIMATE §D.1, §13.3).

## The same method for any artefact

| Artefact | Viewpoint | Start with |
|---|---|---|
| Stakeholder Map Matrix | Stakeholder | one Stakeholder per row, Drivers for the concerns |
| Process Flow Diagram | Business Process Cooperation | Processes chained by Triggering, Roles assigned |
| Platform Decomposition Diagram | Technology | Nodes with System Software assigned, Technology Services realized |
| Project Context Diagram | Project | Work Package assigned to Roles, realizing Deliverables |

Every row is on `/artefact` with its full mapping, and the ADM phase page names the viewpoints; the walk-through above is the same five steps each time (ARCHIMATE §C.1–C.4; WP:w14c §4).

## Check yourself

- Why choose the viewpoint before drawing, and what does Archi do with that choice?
- Which relationship says "provides functionality to" and which says "information passes"?
- How are baseline, target and gap shown, and in which viewpoint?
