---
title: "Application Use-Case Diagram as an ArchiMate Application Usage view — Digital Channels"
deliverable: Application Use-Case Diagram as an ArchiMate view
phase: C
kind: MODEL
track: ARCHIMATE
summary: "Use cases as Application Services serving the Customer, the Cards Operations Analyst and the card network, realized by the Mobile App, Core Banking and Card Switch; channel services consume back-end services through the component."
refs: ["ARCHIMATE §C.1", "CONTENT §3.6.6"]
figure: APPLICATION_USE_CASE_DIAGRAM.svg
viewpoint: Application Usage
artefacts: [APPLICATION_USE_CASE_DIAGRAM]
source: authored
status: draft
---

> **What to notice.** ArchiMate has no use-case element. A use case is a unit of externally visible behaviour offered to an actor, and the language already has that: an **application service** (ARCHIMATE §9.3.5). The UML ellipse becomes a rounded rectangle with the service icon, the actor stick-figure becomes a Business Actor or Business Role, and the "uses" line becomes **serving** pointing from the service to whoever it serves. The system boundary box becomes the component that **realizes** the services.

## How to read the view

Top to bottom is consumer to provider. The **Customer** at the top is served by three application services — View balance, Transfer funds, Freeze card — and those three are realized by the **Mobile App** beneath them (dashed realization lines with hollow triangles). The Mobile App in turn is served by three Core Banking and Card Switch services: Read account, Post transaction, Update card status. That is the "a service in one component may consume a service in another" rule of the TOGAF drawing, expressed as serving into the *component*, which is what the language permits: a service serves an active structure element that needs it.

Two more consumers sit to the right. The **Cards Operations Analyst** is a Business Role, not an actor, because the person filling it changes with the shift; the role is served by Update card status directly — the analyst works in the Card Switch console, not through the app. The **Card network** is an actor served by Authorise card transaction, realized by the Card Switch.

## Elements

| Element | ArchiMate type | Aspect / layer | Why that type |
|---|---|---|---|
| Customer, Card network | Business Actor | active, Business | Parties outside the systems that use the services |
| Cards Operations Analyst | Business Role | active, Business | A responsibility filled by different people; the UML actor was really a role |
| View balance, Transfer funds, Freeze card, Read account, Post transaction, Update card status, Authorise card transaction | Application Service | behaviour, Application | The use cases: externally visible units of application behaviour |
| Mobile App, Core Banking, Card Switch | Application Component | active, Application | The systems whose boundary the UML diagram drew |

## Relationships used

| Relationship | Notation | What it says here |
|---|---|---|
| Serving (service → actor or role) | solid, open arrowhead | The actor uses the service — the UML association |
| Serving (service → component) | solid, open arrowhead | The channel component consumes a back-end service — the UML «consumes» |
| Realization (component → service) | dashed, hollow triangle | The component provides the service — the UML system boundary |

## What changed from the TOGAF drawing

The TOGAF drawing's two boundary boxes ("Mobile App" and "Core Banking / Card Switch") become three components, because Core Banking and the Card Switch are separate systems and the realization must point to one of them. The «consumes» dependencies between ellipses become serving relationships into the Mobile App component rather than between services; ArchiMate does allow service-to-service serving, but drawing it to the component makes the dependency the impact analysis needs — change Post transaction and the Mobile App is affected. The analyst is promoted from actor to role, which is what will let the Application/Organization matrix count seats.

## Draw it yourself

1. Create an *Application Usage* view; add Customer as a Business Actor and Cards Operations Analyst as a Business Role.
2. Add one Application Service per use case, named with a verb phrase.
3. Draw Serving from each service to the actor or role that uses it.
4. Add the three Application Components and draw Realization from each to the services it provides.
5. Draw Serving from Read account, Post transaction and Update card status to the Mobile App; check with *Validate* that no service is left without a realizing component.
