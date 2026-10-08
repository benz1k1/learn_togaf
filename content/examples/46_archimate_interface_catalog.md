---
title: "Interface Catalog as an ArchiMate Application Cooperation view — Digital Channels"
deliverable: Interface Catalog as an ArchiMate view
phase: C
kind: MODEL
track: ARCHIMATE
summary: "Four rows of Northgate's Interface catalog drawn as the pattern component composes interface, interface is assigned to service, service serves consumer, with the catalog's frequency column as the serving label."
refs: ["ARCHIMATE §9.2", "CONTENT §3.6.6"]
figure: INTERFACE_CATALOG.svg
viewpoint: Application Cooperation
artefacts: [INTERFACE_CATALOG]
source: authored
status: draft
---

> **What to notice.** A catalog row has six columns — id, from, to, type, data, frequency — and the ArchiMate rendering spreads them over a four-element chain. *From* is the component that **composes** the interface; the interface is **assigned** to the service it exposes; the service **serves** the *to* component; the id and type go in the interface name, the data in the service name, the frequency on the serving line. This is the language's own definition of an interface: "a point of access where application services are made available" (ARCHIMATE §9.2.3).

## How to read the view

Each column is one catalog row. On the left, **Core Banking** composes **IF-01 REST API** (filled diamond at the owner), which is assigned (dot-and-arrow) to the service **Account balance and transfer**, which serves the **Mobile App** in real time. Beside it, IF-02 is the settlement queue that serves the **Card Switch** "real time / nightly". On the right, the **Fraud Engine** exposes IF-04, the scoring API, whose service also serves the Card Switch.

The bottom row turns the chain sideways because the Card Switch is both a consumer and a provider: it composes **IF-06**, the ISO 8583 endpoint, assigned to **Card authorisation**, which serves the external **Card network**. Reading the diamonds tells you who owns each interface — and therefore who has to sign the change when RQ-07 requires every interface to be described in OpenAPI before build.

## Elements

| Element | ArchiMate type | Aspect / layer | Why that type |
|---|---|---|---|
| Core Banking, Fraud Engine, Card Switch, Mobile App, Card network | Application Component | active, Application | Providers and consumers — the *from* and *to* columns |
| IF-01 REST API, IF-02 settlement queue, IF-04 scoring REST API, IF-06 ISO 8583 endpoint | Application Interface | active, Application | The access point; its name carries the catalog id and type |
| Account balance and transfer; Authorisation and settlement posting; Card transaction scoring; Card authorisation | Application Service | behaviour, Application | What the interface exposes — the *data exchanged* column |

## Relationships used

| Relationship | Notation | What it says here |
|---|---|---|
| Composition (component → interface) | filled diamond at the component | The provider owns the interface; it cannot exist without the component |
| Assignment (interface → service) | dot at the interface, filled arrowhead | The interface is where this service is made available |
| Serving (service → consumer), labelled | solid, open arrowhead | The consumer depends on the service; the label is the frequency |

## What changed from the TOGAF drawing

The TOGAF artefact is a table and the ArchiMate view is a diagram, so this is the one pair where the notations are furthest apart. Two catalog rows are not drawn: IF-03 (the nightly batch to the Data Warehouse) and IF-05 (the push alert), because the pattern needs a provider and a push notification has none in the same sense — the Mobile App does not expose an interface, it registers for one. Both remain flows on the Application Communication view. The frequency column becomes a label rather than a property because it is what the operations team reads first. Nothing was invented: every name is a cell of the catalog.

## Draw it yourself

1. Create an *Application Cooperation* view and add the provider components.
2. For each catalog row, add an Application Interface named `IF-nn type` and nest it inside its provider — Archi records the composition.
3. Add an Application Service named from the *data exchanged* cell and draw Assignment from the interface to it.
4. Add the consumer component and draw Serving from the service to it; name the relationship with the frequency so it renders as a label.
5. Generate the catalog back out of the model with Archi's *Report* or a jArchi script listing every Application Interface with its composition source and serving targets — the table and the view stay in step because they are one model.
