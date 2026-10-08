---
title: "Platform Decomposition Diagram as an ArchiMate Technology view — Digital Channels"
deliverable: Platform Decomposition Diagram as an ArchiMate view
phase: D
kind: MODEL
track: ARCHIMATE
summary: "The platform eye-chart bottom-up: a hardware platform Node composed of four Nodes, System Software assigned to the node it runs on and realizing the four Technology Services the applications consume."
refs: ["ARCHIMATE §C.1", "CONTENT §3.6.7"]
figure: PLATFORM_DECOMPOSITION_DIAGRAM.svg
viewpoint: Technology
artefacts: [PLATFORM_DECOMPOSITION_DIAGRAM]
source: authored
status: draft
---

> **What to notice.** The TOGAF eye-chart pairs a *logical* platform component with the *physical* product that realises it ("Relational database — PostgreSQL 16, 2 nodes"). ArchiMate splits that dash into two elements and one relationship: a **Technology Service** for the logical need and **System Software** for the product, joined by **realization** (ARCHIMATE §10.3.5). The service is what the applications depend on; the product is what the operations team patches. Swapping Kong for another gateway changes the bottom of a column and leaves the service — and every application that uses it — untouched.

## How to read the view

Read a column from the bottom. The **Primary data centre hardware platform** is one Node **composed** of four: application servers, storage, database servers and network. **OpenJDK 21 on Tomcat 10** is System Software **assigned** to the application server (dot at the node, arrowhead at the software); it **realizes** the **Application runtime** service at the top. The same pattern gives Kafka on the application servers realizing Event streaming, and PostgreSQL on the database servers realizing the Relational database service.

The gateway column has one extra element. **Kong 3.6** is assigned to a **Technology Function**, "Route, authenticate and rate-limit API calls", and it is the function that realizes the **API gateway** service. That is the full ArchiMate pattern — active structure assigned to behaviour, behaviour realizing a service — and it is drawn once so the shortcut used in the other three columns (system software realizing the service directly, a derived relationship) is visibly a shortcut.

## Elements

| Element | ArchiMate type | Aspect / layer | Why that type |
|---|---|---|---|
| Application runtime, Event streaming, Relational database, API gateway | Technology Service | behaviour, Technology | The logical platform capabilities the applications need |
| Route, authenticate and rate-limit API calls | Technology Function | behaviour, Technology | What the gateway software does, drawn once to show the full pattern |
| OpenJDK 21 on Tomcat 10; Apache Kafka 3.7; PostgreSQL 16; Kong 3.6 | System Software | active, Technology | The products and versions that realise the services |
| Application server, Storage, Database server, Network, hardware platform | Node | active, Technology | The hardware resources, with sizing in the name |

## Relationships used

| Relationship | Notation | What it says here |
|---|---|---|
| Composition (platform → node) | filled diamond at the platform | The four nodes are parts of one physical platform |
| Assignment (node → system software, software → function) | dot and filled arrowhead | The software runs on that node; the software performs that function |
| Realization (software or function → service) | dashed, hollow triangle | The product delivers the logical service |

## What changed from the TOGAF drawing

The TOGAF drawing is three horizontal bands — applications, software platform, hardware platform — with a dash between logical and physical inside each cell. The ArchiMate view keeps the bands as rows but turns the dash into a realization and the "sits on" into an assignment, so the dependency between bands is a relationship rather than vertical adjacency. The application band is dropped: components belong on an Application Usage view, and the Technology viewpoint stops at the technology services they consume. The TOGAF cross-platform line (MPLS WAN, DMZ, telephony) moves to the Networked Computing view, where it is drawn as communication networks.

## Draw it yourself

1. Create a *Technology* view and add the four Technology Services across the top.
2. Add the System Software elements with product and version in the name; draw Realization from each to its service.
3. Add the four hardware Nodes with sizing in the name and draw Assignment from each node to the software it runs.
4. Add the platform Node and draw Composition to the four; alternatively nest them and let Archi create it.
5. For the gateway, insert a Technology Function between Kong and the service: Assignment from Kong to the function, Realization from the function to the service — then compare with the direct shortcut in the other columns.
