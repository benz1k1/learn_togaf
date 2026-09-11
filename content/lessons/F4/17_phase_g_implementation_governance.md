---
title: Phase G, Implementation Governance, in depth
unit: F4
objectives: ["4.3", "4.6"]
refs: ["ADM §11", "ADM §11.1", "ADM §11.2", "ADM §11.2.1", "ADM §11.2.2", "ADM §11.2.3", "ADM §11.3", "ADM §11.3.1", "ADM §11.3.2", "ADM §11.3.3", "ADM §11.3.4", "ADM §11.3.5", "ADM §11.3.6", "ADM §11.4", "ADM §11.5"]
reading_minutes: 9
source: authored
status: draft
---
## What the phase is for

Phase G provides architectural oversight of the implementation (ADM §11). Two objectives
(ADM §11.1):

| Objective | In plain words |
|---|---|
| Ensure **conformance with the Target Architecture** by implementation projects | keep the projects on the architecture |
| Perform appropriate **Architecture Governance functions** for the solution and any implementation-driven architecture **Change Requests** | govern the solution and the changes it raises |

## Approach

Phase G is where all the information for managing the implementation projects is brought
together. The *actual* development happens in a parallel, organization-specific development
process (ADM §11.5). The favored approach is to deploy the Target Architecture as a **series of
transitions**, each an incremental step that delivers business benefit in its own right. The
overall approach: establish an implementation program to deliver the Transition Architectures
agreed in Migration Planning; adopt a phased deployment schedule reflecting the Architecture
Roadmap; follow the organization's corporate, IT and Architecture Governance standards; use the
established portfolio/program management approach; and define an operations framework for the
long life of the deployed solution.

Two sentences to remember: Phase G **establishes the connection between architecture and the
implementation organization through the Architecture Contract**, and a key aspect is ensuring
compliance **not only by the implementation projects but also by other ongoing projects**.

## Inputs

| Group | Inputs |
|---|---|
| External (ADM §11.2.1) | architecture reference materials |
| Non-architectural (ADM §11.2.2) | Request for Architecture Work; Capability Assessment |
| Architectural (ADM §11.2.3) | Organizational Model; Tailored Framework; Statement of Architecture Work; Architecture Vision; Architecture Repository; Architecture Definition Document; Architecture Requirements Specification; Architecture Roadmap; **Architecture Governance Framework**; **Implementation Governance Model**; **Architecture Contract (standard)**; Request for Architecture Work identified during Phases E and F; Implementation and Migration Plan |

Two things to notice. The Communications Plan, an input to every phase from B to F, is *not*
listed for G. And the Architecture Contract arrives as a **standard** (a template) — it leaves
signed.

## Steps

Six steps (ADM §11.3).

| # | Step | Key point |
|---|---|---|
| 1 | Confirm scope and priorities for deployment with development management | review migration planning outputs, identify priorities and deployment issues, identify building blocks for replacement or update, gap analysis between the Enterprise Architecture and the solutions framework — the SBBs to fill those gaps are identified by the Solution Architects; produce a gap analysis report (ADM §11.3.1) |
| 2 | Identify deployment resources and skills | educate development resources; choose system development methods that interoperate with the architecture outputs and feed designs back (ADM §11.3.2) |
| 3 | Guide development of solutions deployment | per project, document scope, strategic requirements, Change Requests, conformance rules and timeline in an impact analysis; **document the Architecture Contract and obtain signatures** from the developing and sponsoring organizations; update the Enterprise Continuum directory and repository; guide business and IT operating models; produce the Implementation Plan (ADM §11.3.3) |
| 4 | Perform Enterprise Architecture Compliance reviews | review ongoing governance and compliance per building block; post-development reviews; close the development part of the projects (ADM §11.3.4) |
| 5 | Implement business and IT operations | carry out the deployment projects; **publish new Baseline Architectures** to the Architecture Repository (ADM §11.3.5) |
| 6 | Perform post-implementation review and close the implementation | publish reviews and close projects; closure of Phase G is when the solutions are **fully deployed once** (ADM §11.3.6) |

## Outputs

(ADM §11.4)

| Output | Note |
|---|---|
| **Architecture Contract (signed)** | |
| **Compliance Assessments** | |
| **Change Requests** | |
| Architecture-compliant solutions deployed | the implemented system (really an output of the development process, listed here because it matters); populated Architecture Repository; compliance recommendations and dispensations; recommendations on service delivery requirements and performance metrics; SLAs; Architecture Vision and Architecture Definition Document updated post-implementation; business and IT operating models; ABBs |

> **Trap.** The Architecture Contract is the Phase G signature item. It is an *input* as a
> standard and an *output* when signed, and it is signed in step 3, "Guide development of
> solutions deployment", not in a separate "sign the contract" step. Phase H then receives the
> signed contract and may update it.

> **Trap.** "Compliance reviews" are a Phase G *step* and "Compliance Assessments" a Phase G
> *output*. The compliance review *process*, checklists and the Architecture Board belong to the
> EA Capability and Governance document, not to the ADM chapter.

## Check yourself

1. Through which deliverable does Phase G connect the architecture to the implementation organization?
2. Which every-phase input is missing from Phase G's list?
3. When does Phase G close?
4. Who identifies the SBBs that fill the gaps found in step 1?
