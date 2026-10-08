---
title: "The SABSA Matrix: six layers, six columns, thirty-six cells"
unit: S1
objectives: ["S1.2"]
refs: ["SABSA §2", "SABSA §2.1", "SABSA §2.2", "SABSA §2.3", "GUIDE:integrating-risk-and-security §3", "GUIDE:integrating-risk-and-security §5"]
reading_minutes: 12
source: authored
status: draft
---
## The two axes

The SABSA Matrix is the spine of the framework. Its **rows** are the six layers of abstraction,
each written for a different audience; its **columns** are the six interrogatives — *what, why,
how, who, where, when* — that SABSA names **Assets, Motivation, Process, People, Location and
Time**. A cell is the answer to one question at one level of abstraction, and the whole matrix is
the complete security architecture. The SCF paper drills the cells, so the table below is the one
thing in this unit to memorise (SABSA §2.1).

## The six layers and their views

| Layer | Whose view | What it holds |
|---|---|---|
| **Contextual** | The business | The business itself: its assets, goals, risks, processes, organisation, geography and time dependencies |
| **Conceptual** | The architect | The security strategy: business attributes, control and enablement objectives, process-assurance strategies, roles, the domain framework, the through-life risk framework |
| **Logical** | The designer | The design: information assets, policies, services and process maps, entities and trust, domain maps, calendars |
| **Physical** | The builder | The build: data, practices and procedures, mechanisms, human interfaces, infrastructure, schedules |
| **Component** | The tradesman | The parts: products, tools, standards, protocols, identities, locators, timers |
| **Service Management** | The facilities manager | Operations across every other layer: service delivery, operational risk, process delivery, personnel, environment, time and performance |

> **Trap.** The "designer's view" is the **Logical** layer; the "architect's view" is the
> **Conceptual** layer; the "builder's view" is **Physical**; the "tradesman's view" is
> **Component**. The paper likes to ask these the other way round ("which layer is the tradesman's
> view?"). The Service Management layer is drawn as a sixth row but is described as *cutting
> across* the other five, because operations touch every level (SABSA §2.1).

## The full matrix, cell by cell

| | **Assets (What)** | **Motivation (Why)** | **Process (How)** | **People (Who)** | **Location (Where)** | **Time (When)** |
|---|---|---|---|---|---|---|
| **Contextual** | The business: business decisions, goals and assets | Business risk: opportunities and threats | Business processes | Business governance: organisation and relationships | Business geography | Business time dependencies |
| **Conceptual** | Business knowledge and risk strategy: the **Business Attributes Profile** | Risk management objectives: **enablement and control objectives** | Strategies for process assurance: the process-mapping framework | Roles and responsibilities: owners, custodians, users; providers and customers | **Domain framework**: security-domain concepts and the domain model | Time management framework: the through-life risk framework |
| **Logical** | Information assets: the inventory of information | Risk management **policies**: domain policies | Process maps and **security services** | Entity and **trust framework**: entity schema, privilege profiles, trust relationships | **Domain maps**: domain definitions and inter-domain associations | Calendar and timetable: start times, lifetimes, deadlines |
| **Physical** | Data assets: data dictionary and data inventory | Risk management **practices**: rules and procedures | Process mechanisms: applications, middleware, **security mechanisms** | Human interface: user interfaces, identity and access-control systems | ICT infrastructure: platforms, networks, layout of devices | Processing schedule: timing and sequencing of processes and sessions |
| **Component** | ICT components: products, repositories, processors | Risk management **tools and standards**: analysis tools, risk registers, reporting tools | Process tools and standards: tools and protocols | Personnel management tools and standards: identities, job descriptions, roles, ACLs | Locator tools and standards: nodes, addresses, other locators | Step timing and sequencing tools: clocks, timers, interrupts, schedules |
| **Service Management** | Service delivery management: assurance of operational continuity and excellence | **Operational risk management**: assessment, monitoring, reporting, treatment | Process delivery management: management and support of systems, applications and services | Personnel management: account provisioning, user support | Management of environment: buildings, sites, platforms, networks | Time and performance management: management of the calendar and timetable |

(SABSA §2.2)

## How to read a column

Read down a column and the same question is answered at falling levels of abstraction. Take
**Location**: the business has *geography* (Contextual); the architect turns it into a *domain
framework* (Conceptual); the designer draws *domain maps* with their inter-domain associations
(Logical); the builder lays out *platforms and networks* (Physical); the tradesman assigns
*addresses and locators* (Component); the facilities manager *runs the sites and networks*
(Service Management). Nothing in the Component cell should exist without a Logical-layer domain
above it, and nothing in the Logical cell without Contextual geography above it (SABSA §2.3).

Read **Motivation** the same way: business *risk* becomes risk-management *objectives*, which
become *policies*, which become *practices and procedures*, which are supported by *tools and
registers*, and are run as *operational risk management*. That column is the SABSA risk model,
covered in S3, laid out top to bottom (SABSA §2.3).

> **Trap.** The Business Attributes Profile sits in the **Assets (What)** column of the
> **Conceptual** layer — it describes what the business needs its assets to *be*. The
> **Motivation** cell beside it holds the control and enablement *objectives* derived from the
> profile. The security **domain model** is at Conceptual × Location (the framework) and
> Logical × Location (the maps). The **trust framework** is Logical × People.

## How to read a row

Read across a row and you have one complete architecture for one audience. The Logical row is
the designer's whole design: what information exists, what policy governs it, which services
protect it, which entities may act on it and how they trust each other, which domains hold it
and when it is valid. A row with an empty cell is an incomplete architecture, which is why the
matrix is also a completeness checklist (SABSA §2.3).

## In TOGAF terms

The TOGAF guide's phase-by-phase artefacts are Matrix cells with TOGAF names. Preliminary and
Phase A fill the Contextual and Conceptual rows (business drivers, risk appetite, security
principles, the Business Attribute Profile); Phase B fills Logical × Motivation, People and
Location (security policy architecture, trust framework, security domain model); Phase C fills
Logical and Physical × Assets and Process (security classification, security services
catalogue); Phase D fills Physical and Component; Phases G and H are the Service Management row.
The app's `/adm/{phase}` crosswalk names the cells for each phase
(GUIDE:integrating-risk-and-security §5).

*Source note: written from the SABSA framework as published by the SABSA Institute; section numbers refer to the SABSA White Paper and are to be verified against the registered PDF.*
