---
title: Phase B, Business Architecture, in depth
unit: F4
objectives: ["4.3", "4.4"]
refs: ["ADM §4", "ADM §4.1", "ADM §4.2", "ADM §4.2.1", "ADM §4.2.2", "ADM §4.2.3", "ADM §4.3", "ADM §4.3.1", "ADM §4.3.2", "ADM §4.3.3", "ADM §4.3.4", "ADM §4.3.5", "ADM §4.3.6", "ADM §4.3.7", "ADM §4.3.8", "ADM §4.3.9", "ADM §4.4", "ADM §4.5", "ADM §4.5.1", "ADM §4.5.2", "ADM §4.5.3", "ADM §4.5.4", "ADM §4.5.5", "ADM §4.5.6", "ADM §4.5.7", "ADM §4.5.8"]
reading_minutes: 12
source: authored
status: draft
---
## What the phase is for

Phase B develops a Business Architecture that supports the agreed Architecture Vision (ADM §4).
Its two objectives (ADM §4.1) set the pattern every development phase follows:

| Objective | Pattern |
|---|---|
| Develop the **Target Business Architecture** that describes how the enterprise needs to operate to achieve its goals and respond to the drivers in the Architecture Vision, in a way that addresses the Statement of Architecture Work and stakeholder concerns | "develop the Target *X* Architecture" |
| Identify **candidate Architecture Roadmap components** based on the gaps between Baseline and Target Business Architectures | "identify candidate roadmap components from the gaps" |

## Approach

The standard defines Business Architecture as a holistic, multi-dimensional set of business
views — capabilities, end-to-end value delivery, information and organizational structure — and
the relationships among them and with strategies, products, policies, initiatives and
stakeholders (ADM §4.5).

Why B comes first: knowledge of the Business Architecture is a prerequisite for work in any other
domain, and it is often the means of showing business value to stakeholders (ADM §4.5.1). The
scope of Phase B is set by the Architecture Vision. The business strategy says *what* and *why*;
the Business Architecture says *how* to get there. Re-use is a key objective: where Architecture
Descriptions exist they become the Baseline (ADM §4.5.2). Gather only the information needed for
the decisions in scope.

The approach then applies the Phase A artifacts in turn: **business capabilities** with
relationship and heat mapping (ADM §4.5.3), **value streams** mapped to capabilities
(ADM §4.5.4), the **organization map** as a web of working relationships rather than a reporting
chart (ADM §4.5.5), and **information maps** linking information domains to capabilities
(ADM §4.5.6). Other modeling techniques are activity (business process) models, use-case models
and logical data/class models, all expressible in UML (ADM §4.5.7). The Architecture Repository
supplies industry reference models, enterprise-specific views and building blocks, and standards
(ADM §4.5.8).

## Inputs

| Group | Inputs |
|---|---|
| External (ADM §4.2.1) | architecture reference materials |
| Non-architectural (ADM §4.2.2) | Request for Architecture Work; business principles, goals and drivers; **Capability Assessment**; **Communications Plan** |
| Architectural (ADM §4.2.3) | Organizational Model for EA; Tailored Architecture Framework; **approved Statement of Architecture Work**; Architecture Principles including business principles; **Enterprise Continuum**; Architecture Repository; **Architecture Vision**; draft Architecture Definition Document |

Notice what is *not* there: no Architecture Requirements Specification. Phase B is where the
draft Architecture Requirements Specification is first produced, so it cannot be an input.

## Steps

The nine steps (ADM §4.3). Whether to do Baseline or Target first is decided per situation;
activities started in the steps are closed in step 8 and published in step 9.

| # | Step | What happens |
|---|---|---|
| 1 | Select reference models, viewpoints and tools | select resources from the repository and the viewpoints that answer stakeholder concerns; decide the modeling process; identify required **catalogs, matrices and diagrams**; identify the types of requirement to collect (ADM §4.3.1) |
| 2 | Develop Baseline Business Architecture Description | only to the extent needed to support the Target (ADM §4.3.2) |
| 3 | Develop Target Business Architecture Description | to the extent needed to support the vision; consider alternatives with the Architecture Alternatives and Trade-offs technique (ADM §4.3.3) |
| 4 | Perform gap analysis | verify models for consistency; identify gaps between Baseline and Target with the gap analysis technique (ADM §4.3.4) |
| 5 | Define candidate roadmap components | an initial business roadmap, raw material for the consolidated roadmap in Phase E (ADM §4.3.5) |
| 6 | Resolve impacts across the Architecture Landscape | does this architecture affect, or get affected by, other architectures and projects (ADM §4.3.6) |
| 7 | Conduct formal stakeholder review | check the original motivation and the Statement of Architecture Work against the proposal (ADM §4.3.7) |
| 8 | Finalize the Business Architecture | select standards per building block, document each block, cross-check against goals, requirements traceability report, publish re-usable blocks to the repository (ADM §4.3.8) |
| 9 | Create/Update the Architecture Definition Document | document the rationale for building block decisions; prepare the business sections; route for review (ADM §4.3.9) |

## Outputs

(ADM §4.4)

| Output | Contents |
|---|---|
| Refined and updated Architecture Vision phase deliverables | Statement of Architecture Work (updated if necessary), validated business principles, goals and drivers, Architecture Principles |
| **Draft Architecture Definition Document** | Baseline and Target Business Architecture: organization structure, goals and objectives, functions, capabilities, services, products, processes, roles, business data model, the capability/organization correlation, and the views for the selected viewpoints |
| **Draft Architecture Requirements Specification** | gap analysis results, technical requirements for the remaining domains, updated business requirements |
| **Business Architecture components of an Architecture Roadmap** | |

> **Trap.** Steps and outputs are identical in shape across B, C and D; the exam swaps the
> domain word. Learn the nine steps once and the three "draft/draft/components" outputs once. The
> one B-specific fact worth holding is that the draft Architecture Requirements Specification
> *starts* here.

> **Trap.** Step 9 says "Create/**Update**" — Phase A may already have started the Architecture
> Definition Document, so Phase B does not always create it from nothing.

## Check yourself

1. Why does the standard put Business Architecture before the other domains?
2. Which step turns the initial business roadmap into Phase E's raw material?
3. Which three groups of business techniques from Phase A does Phase B apply?
4. Which document appears as a Phase B output but not as a Phase B input?
