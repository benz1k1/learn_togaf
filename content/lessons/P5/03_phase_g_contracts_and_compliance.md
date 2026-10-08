---
title: Phase G in practice, the contract, the compliance review and the dispensation
unit: P5
objectives: ["P5.2"]
refs: ["ADM §11", "ADM §11.1", "ADM §11.3", "ADM §11.3.1", "ADM §11.3.3", "ADM §11.3.4", "ADM §11.3.6", "ADM §11.4", "ADM §11.5", "GOV §3.2.1", "GOV §5.1", "GOV §5.2.2", "GOV §5.3", "GOV §6.2", "GOV §6.3.1", "GOV §6.3.2", "GOV §6.3.3", "GOV §6.4.3", "CONTENT §4.2.11", "CONTENT §4.2.13", "TECH §8.7"]
reading_minutes: 11
source: authored
status: draft
---
## What a Phase G scenario looks like

Implementation has started, or is about to. The scenario gives you an implementation partner
(an in-house development function or an outsourced integrator), a project that has quietly
chosen a different product from the one in the Target Architecture, a project manager who
says the review will "slow us down", and an Architecture Board that meets monthly. It asks
how the architecture function should govern the work. Phase G's two objectives are the
whole answer in miniature: ensure the implementation projects conform to the Target
Architecture, and perform the governance functions for the solution and for any
implementation-driven Change Requests (ADM §11.1).

The five-point answer establishes the Architecture Contract with the implementers, holds
compliance reviews at the right milestones using tailored checklists, handles the deviation
through the compliance and dispensation process or a Change Request, and closes with a
post-implementation review. The three-point answer reviews but has no contract, or grants an
open-ended waiver. The one-point answer redesigns the architecture to match what the project
built. The zero-point answer lets the project proceed because it is late.

## The contract comes first

Phase G establishes the connection between architecture and the implementation organisation
*through the Architecture Contract* (ADM §11.5). Architecture Contracts are joint agreements
between development partners and sponsors on the deliverables, quality and fitness for
purpose of an architecture, and they are enforced through governance (GOV §5.1). They occur
at several points: the Statement of Architecture Work in Phase A is effectively a contract
with the sponsor; contracts with systems integrators govern contracted-out domains; a
contract is drawn up at the *start* of Phase G between the architecture function and the
implementer; and when the Definition Document is finalised at the end of Phase F, one may be
drawn up with the business users who will build and deploy in the architected environment
(GOV §5.1).

| Contract | Parties | Typical content |
|---|---|---|
| Statement of Architecture Work | architecting organisation and sponsor | as defined in Architecture Content (GOV §5.1) |
| Design and development contract | architecture function and partners (integrators, providers) | introduction, nature of agreement, scope, principles and requirements, conformance requirements, process and roles, target measures, phased deliverables, joint workplan, time windows, delivery and business metrics (GOV §5.2.2) |
| Business stakeholders' contract | architecting function and business users | scope, strategic requirements, deliverables, conformance requirements, adopters, time window, business metrics, SLA; also used to manage change in Phase H (GOV §5.2.2) |

For the contract to work in Phase G the governance framework may need simple processes,
people-centred authority, strong communication, timely responses with escalation, supporting
structures and status tracking of implementation (GOV §5.3). In step 11.3.3 the architect
documents each project's scope, strategic requirements, Change Requests, conformance rules
and roadmap timeline in an impact analysis, then documents the contract and obtains
signatures from all developing organisations and the sponsor (ADM §11.3.3).

**Trap.** The signed Architecture Contract is an *output* of Phase G and an *input* to Phase
H; an answer that signs it at the end of Phase G, after the reviews, has the order backwards
(ADM §11.4, ADM §11.5).

## The compliance review

An Architecture Compliance review scrutinises a specific project against established
architectural criteria, spirit and business objectives; its first purpose is to catch errors
early and so reduce the cost and risk of later change, and it also surfaces standards that
need changing, application-specific services that could become shared infrastructure and
criteria for procurement (GOV §6.3.1). Reviews are held at project milestones, project
initiation, initial design, major design changes and ad hoc, and the sweet spot is when
requirements and the Enterprise Architecture are reasonably firm and the project
architecture is taking shape, *well before completion* (GOV §6.3.2).

Who runs it depends on the situation: a small project may self-assess with the checklists; a
project that has had no practising architect gets a review organised and led by the EA
function with business domain experts; the typical TOGAF scenario has the lead Enterprise
Architect co-ordinate a team of business and technical experts, or a representative of the
Architecture Board leads (GOV §6.3.3). The twelve-step process runs from "request review" by
anyone with an interest, through the Architecture Review Co-ordinator identifying principals
and scope, the Lead Enterprise Architect tailoring checklists, interviewing, analysing and
reporting, to the Architecture Board and the customer accepting and signing off
(GOV §6.4.3). The Compliance Assessment deliverable holds project progress, an overview of
the project architecture and the completed checklists (CONTENT §4.2.13).

<figure class="my-4">
<svg viewBox="0 0 760 330" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="11" role="img" aria-label="Phase G governance path: contract, then compliance review, then one of four outcomes: accept, adjust and realign, time-bound dispensation, or Change Request">
<defs><marker id="arr-p5g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
<rect x="10" y="20" width="170" height="56" rx="8" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="95" y="42" text-anchor="middle" font-weight="bold">Architecture Contract</text>
<text x="95" y="58" text-anchor="middle">signed at the start of Phase G</text>
<text x="95" y="70" text-anchor="middle">(ADM §11.3.3, GOV §5.1)</text>
<rect x="215" y="20" width="190" height="56" rx="8" fill="#e3f5e1" stroke="#7fbf7a"/>
<text x="310" y="42" text-anchor="middle" font-weight="bold">Compliance review</text>
<text x="310" y="58" text-anchor="middle">initiation, initial design, major change, ad hoc</text>
<text x="310" y="70" text-anchor="middle">tailored checklists, report, sign-off (GOV §6.4.3)</text>
<line x1="180" y1="48" x2="215" y2="48" stroke="#555" marker-end="url(#arr-p5g)"/>
<rect x="440" y="20" width="310" height="56" rx="8" fill="#fff" stroke="#666"/>
<text x="595" y="42" text-anchor="middle" font-weight="bold">Is the project "in accordance with" the architecture?</text>
<text x="595" y="58" text-anchor="middle">strategy and direction, standards, functionality, principles</text>
<text x="595" y="70" text-anchor="middle">levels of conformance (GOV §6.2)</text>
<line x1="405" y1="48" x2="440" y2="48" stroke="#555" marker-end="url(#arr-p5g)"/>
<g fill="#fff" stroke="#666">
<rect x="20" y="150" width="160" height="60" rx="6"/>
<rect x="205" y="150" width="160" height="60" rx="6"/>
<rect x="390" y="150" width="165" height="60" rx="6"/>
<rect x="580" y="150" width="170" height="60" rx="6"/>
</g>
<text x="100" y="172" text-anchor="middle" font-weight="bold" fill="#3a7d3a">accept</text>
<text x="100" y="188" text-anchor="middle">assessment accepted;</text>
<text x="100" y="202" text-anchor="middle">continue, publish (GOV §3.2.1)</text>
<text x="285" y="172" text-anchor="middle" font-weight="bold">adjust and realign</text>
<text x="285" y="188" text-anchor="middle">subject area changed to</text>
<text x="285" y="202" text-anchor="middle">meet compliance (GOV §3.2.1)</text>
<text x="472" y="172" text-anchor="middle" font-weight="bold" fill="#e0b060">dispensation</text>
<text x="472" y="188" text-anchor="middle">time-bound, with service and</text>
<text x="472" y="202" text-anchor="middle">operational criteria enforced</text>
<text x="665" y="172" text-anchor="middle" font-weight="bold" fill="#c0392b">Change Request</text>
<text x="665" y="188" text-anchor="middle">deviation or scope extension</text>
<text x="665" y="202" text-anchor="middle">starts further architecture work</text>
<line x1="500" y1="76" x2="100" y2="150" stroke="#555" marker-end="url(#arr-p5g)"/>
<line x1="560" y1="76" x2="285" y2="150" stroke="#555" marker-end="url(#arr-p5g)"/>
<line x1="600" y1="76" x2="472" y2="150" stroke="#555" marker-end="url(#arr-p5g)"/>
<line x1="660" y1="76" x2="665" y2="150" stroke="#555" marker-end="url(#arr-p5g)"/>
<text x="120" y="120" text-anchor="middle" fill="#3a7d3a">compliant</text>
<text x="640" y="120" text-anchor="middle" fill="#c0392b">non-compliant, or the architecture itself is wrong</text>
<rect x="20" y="250" width="730" height="34" rx="6" fill="#fff1d6" stroke="#e0b060"/>
<text x="385" y="271" text-anchor="middle">a dispensation is never indefinite: its expiry is a trigger for the next compliance activity (GOV §3.2.1); a Change Request may kick-start a further cycle of architecture work (CONTENT §4.2.11)</text>
<text x="385" y="312" text-anchor="middle" fill="#666">closure: post-implementation review, publish reviews, close projects; Phase G closes when the solutions are fully deployed once (ADM §11.3.6)</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">The Phase G governance path and its four outcomes. Original drawing; the outcomes follow GOV §3.2.1 and §6.2, the closure rule ADM §11.3.6.</figcaption>
</figure>

## Deviations: adjust, dispense, or change the architecture

When a Compliance Assessment is rejected the subject area can be adjusted to comply or can
request a dispensation. Dispensations are granted for a given time period and a set of
service and operational criteria that must be enforced while they last; they are never
granted indefinitely, and their time-bound nature makes them a major trigger in the
compliance cycle (GOV §3.2.1). Non-compliance is also a signal: it highlights areas for
realignment and areas the architecture itself may need to integrate, and dispensations are
the mechanism that registers and monitors those changes (GOV §6.3.1).

Sometimes the project is right and the architecture is wrong. When the original Definition
and requirements are not sufficient, or external factors open new opportunities, the project
submits a Change Request with a description, rationale, an impact assessment (requirements
referenced, phases to be revisited, phase to lead prioritisation) and a repository reference;
it may kick-start a further cycle of architecture work (CONTENT §4.2.11). Change Requests are
a listed Phase G output, next to the signed contract, the Compliance Assessments and the
architecture-compliant solutions with their populated repository and dispensations
(ADM §11.4).

Risk is governed here too. Residual risks must be approved by the IT governance framework, and
the risk identification and mitigation worksheets are governance artefacts kept up to date
in Phase G, where monitoring may reveal critical risks that need another full or partial ADM
cycle (TECH §8.7).

## How the 5, 3 and 1 differ

| Answer | Why it scores that |
|---|---|
| 5 | Confirms scope and priorities with development management, signs the Architecture Contract with the integrator and sponsor, schedules reviews at initiation and initial design led by the lead Enterprise Architect with tailored checklists, treats the product deviation as a rejected assessment: adjust, or a time-bound dispensation with criteria, or a Change Request if the architecture should change; records everything in the repository; closes with a post-implementation review |
| 3 | Runs the reviews and grants a waiver, but the waiver has no expiry and no criteria, so it is not a dispensation as the standard defines one (GOV §3.2.1); or there is no signed contract, so the conformance requirements have no agreed basis (GOV §5.2.2) |
| 1 | Updates the Target Architecture to match the product the project chose, without a Change Request or impact assessment; the architecture is changed by a project decision rather than by governance (CONTENT §4.2.11) |
| 0 | Waives the review because the project is late; the review's first purpose is to catch errors early precisely to shorten project time (GOV §6.3.1) |

**Trap.** "Compliant" and "conformant" are distinct levels; "in accordance with" means
supporting the strategy, adhering to standards, providing the stated functionality and
adhering to the principles (GOV §6.2). An answer that calls a partial match "fully
compliant" is using the wrong level.

## Where to look in the book

ADM chapter 11: §11.3 for the six steps, §11.3.3 for the contract signature, §11.4 for the
outputs, §11.5 for the approach. EA Capability and Governance: §5.1 for when contracts arise,
§5.2 for their contents, §5.3 for the Phase G governance aspects, §6.2 for conformance
levels, §6.3 for review purpose, timing and personnel, §6.4.3 for the twelve steps, §3.2.1
for compliance and dispensation. Architecture Content §4.2.11 (Change Request) and §4.2.13
(Compliance Assessment). ADM Techniques §8.7 for risk monitoring in Phase G.

## Check yourself

- Who signs the Phase G Architecture Contract, and when?
- Name the four review checkpoints and the moment the standard calls the right time to review.
- What two properties make a waiver a dispensation?
