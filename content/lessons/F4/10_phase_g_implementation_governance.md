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

<figure class="my-4">
<svg viewBox="0 0 760 288" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="Phase G: its inputs, six steps and outputs, with the signed Architecture Contract, Compliance Assessments and Change Requests marked as first produced here">
  <defs><marker id="arr-f4-17" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
  <text x="107.5" y="18" text-anchor="middle" font-size="12" font-weight="bold" fill="#345">Inputs</text><text x="652.5" y="18" text-anchor="middle" font-size="12" font-weight="bold" fill="#345">Outputs</text><text x="380" y="18" text-anchor="middle" font-size="12" font-weight="bold" fill="#345">Steps</text><rect x="235" y="34" width="290" height="220" rx="8" fill="#fff1d6" stroke="#e0b060"/><text x="380" y="52" text-anchor="middle" font-size="12" font-weight="bold">Phase G: Implementation Governance</text><text x="245" y="106.5" font-size="11">1 Confirm scope and priorities for deployment</text><text x="245" y="121.5" font-size="11">2 Identify deployment resources and skills</text><text x="245" y="136.5" font-size="11">3 Guide development of solutions deployment</text><text x="245" y="151.5" font-size="11">   (document the Contract; obtain signatures)</text><text x="245" y="166.5" font-size="11">4 Perform EA Compliance reviews</text><text x="245" y="181.5" font-size="11">5 Implement business and IT operations</text><text x="245" y="196.5" font-size="11">6 Post-implementation review; close</text><rect x="10" y="34" width="195" height="46" rx="6" fill="#e0ecff" stroke="#7aa2e3"/><text x="107.5" y="54.5" text-anchor="middle" font-size="10.5">Architecture Contract</text><text x="107.5" y="67.5" text-anchor="middle" font-size="10.5">(standard)</text><line x1="205" y1="57" x2="233" y2="57" stroke="#555" marker-end="url(#arr-f4-17)"/><rect x="10" y="92" width="195" height="46" rx="6" fill="#e0ecff" stroke="#7aa2e3"/><text x="107.5" y="112.5" text-anchor="middle" font-size="10.5">Implementation Governance Model;</text><text x="107.5" y="125.5" text-anchor="middle" font-size="10.5">Architecture Governance Framework</text><line x1="205" y1="115" x2="233" y2="115" stroke="#555" marker-end="url(#arr-f4-17)"/><rect x="10" y="150" width="195" height="46" rx="6" fill="#e0ecff" stroke="#7aa2e3"/><text x="107.5" y="170.5" text-anchor="middle" font-size="10.5">Implementation and Migration Plan;</text><text x="107.5" y="183.5" text-anchor="middle" font-size="10.5">Architecture Roadmap</text><line x1="205" y1="173" x2="233" y2="173" stroke="#555" marker-end="url(#arr-f4-17)"/><rect x="10" y="208" width="195" height="46" rx="6" fill="#e0ecff" stroke="#7aa2e3"/><text x="107.5" y="222" text-anchor="middle" font-size="10.5">Architecture Definition Document;</text><text x="107.5" y="235" text-anchor="middle" font-size="10.5">Architecture Requirements</text><text x="107.5" y="248" text-anchor="middle" font-size="10.5">Specification</text><line x1="205" y1="231" x2="233" y2="231" stroke="#555" marker-end="url(#arr-f4-17)"/><rect x="555" y="34" width="195" height="46" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/><text x="652.5" y="54.5" text-anchor="middle" font-size="10.5">Architecture Contract</text><text x="652.5" y="67.5" text-anchor="middle" font-size="10.5">(signed)</text><rect x="705.6" y="26" width="40.4" height="15" rx="7" fill="#f3e3f7" stroke="#b58ac9"/><text x="725.8" y="37" text-anchor="middle" font-size="9.5" fill="#5b2d6e">signed</text><line x1="525" y1="57" x2="553" y2="57" stroke="#555" marker-end="url(#arr-f4-17)"/><rect x="555" y="92" width="195" height="46" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/><text x="652.5" y="119" text-anchor="middle" font-size="10.5">Compliance Assessments</text><rect x="711" y="84" width="35" height="15" rx="7" fill="#f3e3f7" stroke="#b58ac9"/><text x="728.5" y="95" text-anchor="middle" font-size="9.5" fill="#5b2d6e">first</text><line x1="525" y1="115" x2="553" y2="115" stroke="#555" marker-end="url(#arr-f4-17)"/><rect x="555" y="150" width="195" height="46" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/><text x="652.5" y="177" text-anchor="middle" font-size="10.5">Change Requests</text><rect x="711" y="142" width="35" height="15" rx="7" fill="#f3e3f7" stroke="#b58ac9"/><text x="728.5" y="153" text-anchor="middle" font-size="9.5" fill="#5b2d6e">first</text><line x1="525" y1="173" x2="553" y2="173" stroke="#555" marker-end="url(#arr-f4-17)"/><rect x="555" y="208" width="195" height="46" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/><text x="652.5" y="228.5" text-anchor="middle" font-size="10.5">Architecture-compliant solutions</text><text x="652.5" y="241.5" text-anchor="middle" font-size="10.5">deployed; populated Repository</text><line x1="525" y1="231" x2="553" y2="231" stroke="#555" marker-end="url(#arr-f4-17)"/><text x="380" y="272" text-anchor="middle" font-size="11" fill="#666">Not an input: the Communications Plan, listed for every phase from B to F but not for G (ADM §11.2)</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">Inputs, steps and outputs of Phase G. Original drawing; inputs and outputs per ADM §11.2 and ADM §11.4, steps per ADM §11.3.</figcaption>
</figure>

> **Trap.** The Architecture Contract is the Phase G signature item. It is an *input* as a
> standard and an *output* when signed, and it is signed in step 3, "Guide development of
> solutions deployment", not in a separate "sign the contract" step. Phase H then receives the
> signed contract and may update it.

> **Trap.** "Compliance reviews" are a Phase G *step* and "Compliance Assessments" a Phase G
> *output*. The compliance review *process*, checklists and the Architecture Board belong to the
> EA Capability and Governance document, not to the ADM chapter.

<!-- figures:start -->
## Figures from the standard

The diagrams the cited sections carry, from your local copy of the publication. The exam reproduces these; know what each box is.

<div class="grid gap-4 md:grid-cols-2">
<figure class="max-w-lg"><img src="/figure/ADM:fig-11-1" alt="Figure 11-1: Phase G: Implementation" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 11-1: Phase G: Implementation (ADM)</figcaption></figure>
</div>
<!-- figures:end -->

## Check yourself

1. Through which deliverable does Phase G connect the architecture to the implementation organization?
2. Which every-phase input is missing from Phase G's list?
3. When does Phase G close?
4. Who identifies the SBBs that fill the gaps found in step 1?
