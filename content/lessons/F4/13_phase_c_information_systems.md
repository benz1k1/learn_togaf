---
title: Phase C, Information Systems Architectures (Data and Application), in depth
unit: F4
objectives: ["4.3", "4.4"]
refs: ["ADM §5", "ADM §5.1", "ADM §5.2", "ADM §6", "ADM §6.1", "ADM §6.2", "ADM §6.2.1", "ADM §6.2.2", "ADM §6.2.3", "ADM §6.3", "ADM §6.3.1", "ADM §6.3.7", "ADM §6.3.9", "ADM §6.4", "ADM §6.5", "ADM §6.5.1", "ADM §6.5.2", "ADM §6.5.3", "ADM §7", "ADM §7.1", "ADM §7.2", "ADM §7.2.1", "ADM §7.2.2", "ADM §7.2.3", "ADM §7.3", "ADM §7.3.1", "ADM §7.3.7", "ADM §7.4", "ADM §7.5", "ADM §7.5.1"]
reading_minutes: 12
source: authored
status: draft
---
## One phase, two chapters

Phase C covers the Data and Application Architectures for the project (ADM §5). The standard
gives the objectives and approach once (chapter 5), then describes inputs, steps and outputs
separately for the Data part (chapter 6) and the Application part (chapter 7).

Objectives (ADM §5.1):

| Objective | Pattern |
|---|---|
| Develop the **Target Information Systems Architectures**, describing how they will enable the Business Architecture and the Architecture Vision, addressing the Statement of Architecture Work and stakeholder concerns | develop the target |
| Identify candidate Architecture Roadmap components from the gaps between Baseline and Target Information Systems (Data and Application) Architectures | gaps → roadmap components |

The Data part restates them for the Target Data Architecture (ADM §6.1) and the Application part
for the Target Application Architecture (ADM §7.1).

## Approach

Phase C is "some combination of Data and Application Architecture, **in either order**"
(ADM §5.2). A data-driven approach (Spewak's Enterprise Architecture Planning) starts with data;
an application-driven approach starts from core packaged applications (ERP, CRM) that underpin
mission-critical processes and treats their implementation and integration as the main focus.

The Data approach (ADM §6.5): a Data Architecture should handle **data at rest, data in motion,
data in use and open data** (ADM §6.5.1), and is built from three metamodel entities — data
entity, logical data component and physical data component. Key considerations are **data
management** (systems of record, enterprise-wide standards, where data is created, stored,
transported and reported), **data migration** (transformation, weeding and cleansing when an
application is replaced) and **data governance** (structure, management system, people)
(ADM §6.5.2). The repository supplies generic data models for the industry vertical (ADM §6.5.3).

The Application approach is shorter: consider what application resources the repository holds —
industry business and application models, models for common functions such as e-commerce and
supply chain, and the Integrated Information Infrastructure Reference Model (III-RM)
(ADM §7.5.1).

## Inputs

Both parts share the standard set; the differences are the domain-specific principles, the
reference guides and what has already been produced.

| Group | Data part (ADM §6.2) | Application part (ADM §7.2) |
|---|---|---|
| External | architecture reference materials **plus** the Information Architecture Series Guides (customer master data management; BI and analytics and metadata management reference models) (ADM §6.2.1) | architecture reference materials (ADM §7.2.1) |
| Non-architectural | Request for Architecture Work; Capability Assessment; Communications Plan (ADM §6.2.2) | the same three (ADM §7.2.2) |
| Architectural | Organizational Model; Tailored Framework; **data principles**, if existing; Statement of Architecture Work; Architecture Vision; Architecture Repository (in particular definitions of current data); draft Architecture Definition Document; draft Architecture Requirements Specification with gap results **from Business Architecture**; **Business Architecture** components of the roadmap (ADM §6.2.3) | the same, with **application principles**; gap results from Business **and Data** Architecture, if available; Business **and Data** roadmap components, if available (ADM §7.2.3) |

## Steps

Each part runs the nine development steps (ADM §6.3, ADM §7.3): select reference models,
viewpoints and tools; develop the Baseline description; develop the Target description; perform
gap analysis; define candidate roadmap components; resolve impacts across the Architecture
Landscape; conduct formal stakeholder review; finalize the Data (or Application) Architecture;
create/update the Architecture Definition Document.

Domain-specific detail inside step 1:

- Data (ADM §6.3.1): review or generate the data principles; example modeling techniques are the
  entity relationship diagram and the class diagram; the recommended process collects data models
  from Business and Application material, rationalizes them into a data inventory, builds
  matrices relating data to business service, capability, function, access rights and
  application, then examines how data is created, distributed, migrated, secured and archived.
- Application (ADM §7.3.1): review or generate the application principles; consider
  platform-independent descriptions of business logic (the OMG Model-Driven Architecture is the
  example); the recommended process lists required applications, decomposes complicated ones,
  removes duplicated functionality, identifies logical and physical applications, builds
  matrices to business services, capabilities, data and processes, and elaborates views.

Step 7 in both parts includes an impact analysis on the *other* architectures: the Data review
asks whether Business and Application Architectures must change and identifies constraints on
the Technology Architecture about to be designed (ADM §6.3.7); the Application review does the
same for Business and Data and flags constraints on the Technology Architecture, especially
infrastructure (ADM §7.3.7). Either may "drop into a short iteration" of the other part.

## Outputs

| Output | Data part (ADM §6.4) | Application part (ADM §7.4) |
|---|---|---|
| Refined Architecture Vision phase deliverables | Statement of Architecture Work; validated or new **data principles** | Statement of Architecture Work; validated or new **application principles** |
| Draft Architecture Definition Document | Baseline and Target Data Architecture: business data model, logical data model, data management process models, **Data Entity/Business Function matrix**, views | Baseline and Target Application Architecture, views |
| Draft Architecture Requirements Specification | gap results, **data interoperability requirements**, technical requirements, **constraints on the Technology Architecture** about to be designed, updated business and application requirements | gap results, **application interoperability requirements**, technical requirements, constraints on the Technology Architecture, updated business and data requirements |
| Roadmap components | Data Architecture components of an Architecture Roadmap | Application Architecture components of an Architecture Roadmap |

The Data sections of the Architecture Definition Document are spelled out in step 9: business
data model, logical data model, data management process model, Data Entity/Business Function
matrix and data interoperability requirements (ADM §6.3.9).

> **Trap.** Phase C is *one* phase. An option that lists "Phase C: Data Architecture" and "Phase
> C: Application Architecture" as two of the ADM's phases is wrong; there are two chapters, not
> two phases, and the standard allows either order.

> **Trap.** Data principles and application principles enter Phase C as inputs "if existing" and
> are reviewed or generated in step 1 of the relevant part. They are not Preliminary Phase steps.

## Check yourself

1. What are the four kinds of data a Data Architecture must handle?
2. Which extra external reference materials does the Data part list that the Application part does not?
3. Which two other domains does the Application stakeholder review check for impact, and which domain does it constrain?
4. What three dimensions does data governance cover?
