---
title: "The Logical layer: the designer's view, services, information and its six cells"
unit: S4
objectives: ["S4.1"]
refs: ["SABSA §2.2", "SABSA §6", "SABSA §6.1", "SABSA §6.2", "GUIDE:integrating-risk-and-security §5.3", "GUIDE:integrating-risk-and-security §5.4", "GUIDE:integrating-risk-and-security §5.4.1"]
reading_minutes: 10
source: authored
status: draft
---
## The designer's view

The Logical layer is the third row of the Matrix and is the **designer's view**. It takes the
strategy of the Conceptual layer and turns it into a *design*: what information exists and what
it needs, which policies govern it, which security services deliver the objectives, which
entities act and how they trust each other, how the enterprise is divided into domains, and when
things happen. It is technology-independent — it names *services* such as "entity
authentication" and "message confidentiality", not mechanisms such as passwords or TLS. Those
belong to the Physical layer below (SABSA §6).

The word to anchor on is **service**. A **security service** is a logical capability that
delivers a control or enablement objective, described by what it does and to what level, without
saying how. The same service may be realised by different mechanisms in different places, and one
mechanism may realise several services. This is the layer's version of the ABB-versus-SBB
distinction the learner knows from TOGAF: logical services are building blocks defined by
function, physical mechanisms are the solutions that implement them
(GUIDE:integrating-risk-and-security §5.4.1).

## The six cells

| Column | Logical cell | What goes in it |
|---|---|---|
| **Assets (What)** | Information assets | The inventory of information the business holds, classified by the attributes each item needs — the **security classification** of information |
| **Motivation (Why)** | Risk management policies | The **policies**, written per domain by its policy authority, that state what is required and permitted; the control and enablement objectives made into rules |
| **Process (How)** | Process maps and services | The business processes drawn as information flows and transformations, and the **security services** attached to them; the service-oriented view of security |
| **People (Who)** | Entity and trust framework | The **entity schema** (who and what can act: people, organisations, systems), their privilege profiles, and the **trust relationships** between them |
| **Location (Where)** | Domain maps | The **security domains** drawn out: domain definitions, their boundaries, super- and sub-domain structure, and the inter-domain associations and interactions |
| **Time (When)** | Calendar and timetable | Start times, lifetimes, deadlines and validity periods: when a policy applies, how long a credential lives, when a service must be available |

(SABSA §6.1)

> **Trap.** "Designer's view" is Logical. The paper pairs each view with a layer and asks for
> the odd one out; the sequence business → architect → designer → builder → tradesman →
> facilities manager maps to Contextual → Conceptual → Logical → Physical → Component → Service
> Management.

> **Trap.** Security **services** are Logical; security **mechanisms** are Physical; security
> **products** and standards are Component. "Encryption service" is Logical; "AES-256 in the
> database layer" is Physical; "the named HSM product" is Component.

## Information assets and classification

The Assets cell is where information is inventoried and **classified**. Classification in SABSA
means attaching to each information asset the attributes and targets it needs — not only a
confidentiality label but availability, integrity, retention, legal admissibility and so on. The
classification is the input to service selection: an asset classified as *non-repudiable* needs a
signing service; one classified *recoverable to four hours* needs a backup service with that
recovery objective. The TOGAF guide places security classification in Phase C beside the data
architecture for the same reason (GUIDE:integrating-risk-and-security §5.4).

## Services on the process map

The Process cell draws the business processes as flows and places services on them. A process
map shows where information enters, is transformed, is stored and leaves; a security service is
attached at each point where an attribute must be assured. Common logical services include
entity authentication, authorisation, message confidentiality, message integrity, non-repudiation
of origin and receipt, availability and continuity, audit and accountability, and — on the
enablement side — federation, delegation and provisioning services that make new business
possible. The catalogue of these services is a Logical-layer deliverable that the Physical layer
consumes (SABSA §6.2).

## Entities, trust and domains

The People and Location cells hold the two ideas that the rest of this unit examines. The
**entity and trust framework** defines who can act (entities), what they may do (privilege
profiles) and on what basis they are believed (trust relationships). The **domain maps** draw the
security domains that the Conceptual layer's domain framework anticipated, with their policy
authorities and the associations between them. Together they answer "who is allowed to trust
whom, and where" — the Logical layer's distinctive contribution, and the subject of lessons 2 and
3 (SABSA §6.1).

## The Logical layer as a completeness check

Because it is technology-independent, the Logical row is the best place to check coverage. Every
attribute in the profile should be visible as a classification on some asset, a policy statement
in some domain, a service on some process, a privilege in some entity profile, a domain
boundary and a calendar entry. An attribute with no Logical-layer footprint has not been designed
for, whatever the Physical layer contains (SABSA §6).

## In TOGAF terms

The Logical layer is Phases B and C. The TOGAF guide's Phase B artefacts — security policy
architecture, security domain model, trust framework, risk assessment and registers — are the
Motivation, Location and People cells of this row; its Phase C artefacts — the security services
catalogue, security classification and data quality — are the Process and Assets cells. The
services are Architecture Building Blocks; their Physical-layer mechanisms are the Solution
Building Blocks chosen in Phases C and D (GUIDE:integrating-risk-and-security §5.3).

*Source note: written from the SABSA framework as published by the SABSA Institute; section numbers refer to the SABSA White Paper and are to be verified against the registered PDF.*
