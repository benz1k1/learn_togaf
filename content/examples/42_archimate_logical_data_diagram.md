---
title: "Logical Data Diagram as an ArchiMate Information Structure view — Digital Channels"
deliverable: Logical Data Diagram as an ArchiMate view
phase: C
kind: MODEL
track: ARCHIMATE
summary: "The logical records with their keys drawn as Data Objects realizing the conceptual Business Objects, plus the three data objects Phase C adds for evidence, journey state and fraud score."
refs: ["ARCHIMATE §C.1", "CONTENT §3.6.5"]
figure: LOGICAL_DATA_DIAGRAM.svg
viewpoint: Information Structure
artefacts: [LOGICAL_DATA_DIAGRAM]
source: authored
status: draft
---

> **What to notice.** Two rows, two colours, one relationship between them. The yellow row is the *conceptual* model from the previous view; the blue row is the *logical* model; and every blue element **realizes** exactly one yellow one. That single dashed line with a hollow triangle is how ArchiMate says "this record is how that business concept is represented in an information system" (ARCHIMATE §5.2.4). The TOGAF Logical Data diagram (CONTENT §3.6.5) shows only the blue row; the ArchiMate view keeps the trace back to the concept.

## How to read the view

Read a column top to bottom: **Customer** is realized by **Customer record**, whose name carries the keys and attributes that matter to a designer (`customer_id PK`, `kyc_status`). The logical row then repeats the conceptual structure at the record level — Customer record aggregates Account records (`1..*`), Account record aggregates Card records (`0..*`), and Card record is associated with Transaction record with the `0..1` that says a transaction may or may not have a card behind it.

The third row is what Phase C *added*, taken straight from the Definition Document's data chapter: **Identity Evidence** with its 30-day expiry (RQ-06), **Onboarding Journey** with its 24-hour token so a journey can move between counter and app (RQ-05), and **Fraud Score** holding the score and its reasons. Each is associated with the record it describes and with nothing else — none of them realizes a new Business Object, because none of them is a new business concept; they are working data of a service.

## Elements

| Element | ArchiMate type | Aspect / layer | Why that type |
|---|---|---|---|
| Customer, Account, Card, Transaction | Business Object | passive, Business | The concept the record represents |
| Customer record, Account record, Card record, Transaction record | Data Object | passive, Application | A logical record: keys, attributes, held by an application |
| Identity Evidence, Onboarding Journey, Fraud Score | Data Object | passive, Application | New logical entities; derived or transient, owned by one component |

## Relationships used

| Relationship | Notation | What it says here |
|---|---|---|
| Realization (Data Object → Business Object) | dashed, hollow triangle | The record is the application-level representation of the concept |
| Aggregation (Customer record → Account record, Account record → Card record) | hollow diamond | The logical structure mirrors the conceptual one |
| Association, labelled | plain line | Foreign-key relationships and the new objects' attachment points |

## What changed from the TOGAF drawing

The TOGAF drawing is a class-diagram style table per entity with PK/FK columns and crow's-foot cardinalities. ArchiMate has no attribute compartment, so the keys move into the element name — a deliberate compromise that keeps the view readable and leaves column-level detail to the physical model. The conceptual row is new: the TOGAF artefact treats the conceptual and logical diagrams as two documents, whereas ArchiMate treats them as two views of one model joined by realization. The three target additions are also new here; the TOGAF drawing shows the baseline only.

## Draw it yourself

1. Open the model from the Conceptual Data view; the four Business Objects already exist — drag them onto a new Information Structure view rather than creating them again.
2. Add a Data Object per record and give it a name of the form `Customer record: customer_id PK, kyc_status`.
3. Draw Realization from each Data Object to its Business Object.
4. Repeat the aggregations and associations at the record level, with cardinalities as relationship names.
5. Add the three new Data Objects and associate each with one record; use the Properties tab to note the retention rule (30 days, 24 hours) so the constraint travels with the element.
