---
title: Phase H, Architecture Change Management, in depth
unit: F4
objectives: ["4.3", "4.6"]
refs: ["ADM §12", "ADM §12.1", "ADM §12.2", "ADM §12.2.1", "ADM §12.2.2", "ADM §12.2.3", "ADM §12.3", "ADM §12.3.1", "ADM §12.3.2", "ADM §12.3.3", "ADM §12.3.4", "ADM §12.3.5", "ADM §12.3.6", "ADM §12.3.7", "ADM §12.4", "ADM §12.5", "ADM §12.5.1", "ADM §12.5.2", "ADM §12.5.3"]
reading_minutes: 11
source: authored
status: draft
---
## What the phase is for

Phase H establishes the procedures for managing change to the new architecture (ADM §12).
Three objectives (ADM §12.1):

| Objective | In plain words |
|---|---|
| Ensure that the **architecture development cycle** is maintained | keep the ADM turning |
| Ensure that the **Architecture Governance Framework** is executed | governance actually runs |
| Ensure that the **Enterprise Architecture Capability** meets current requirements | the capability itself stays fit |

## Approach

The goal of architecture change management is to ensure the architecture **achieves its original
target business value**, managing changes in a cohesive, architected way (ADM §12.5). The process
continually monitors governance requests, new technology and business change, and decides whether
to formally start a new architecture evolution cycle. It aims to keep the implemented
architecture *dynamic* — able to evolve quickly. Monitoring business growth and decline, and
capacity measurement, are key aspects. The governance body must set criteria to judge whether a
Change Request warrants just an architecture update or a new ADM cycle, and must guard against
"creeping elegance".

**Drivers for change** (ADM §12.5.1): three ways to change the infrastructure must be integrated
— strategic top-down change, bottom-up operational change, and experience with previously
delivered increments. Technology-related drivers (new technology reports, asset management cost
reductions, technology withdrawal, standards initiatives) are usually handled through change
management and governance. Business drivers (business-as-usual developments, exceptions,
innovations, business technology innovations, strategic change) often result in a complete
re-development or an iteration of part of the cycle. The **Architecture Board** assesses and
approves Requests for Change.

**The three categories** (ADM §12.5.2):

| Category | Handling | Investment driver |
|---|---|---|
| **Simplification** change | change management techniques | reduce investment |
| **Incremental** change | change management, or partial re-architecting depending on the change | derive more value from existing investment |
| **Re-architecting** change | put the whole architecture through the development cycle again | increase investment to create new value |

Four activities decide which category applies: register all events that may affect the
architecture; allocate and manage resources for architecture tasks; the responsible process or
role assesses what should be done; evaluate impacts.

**Maintenance versus redesign** (ADM §12.5.3): if a change affects **two or more stakeholders**
it is likely to need architecture redesign and re-entry to the ADM; one stakeholder, or a change
allowable under a dispensation, is more likely a change-management candidate. Examples: a change
significant to business strategy is re-architecting; a new technology or standard refreshing only
the Technology Architecture is incremental; ten systems consolidated into one at the
infrastructure level is a simplification. A refreshment cycle requires a **new Request for
Architecture Work**.

## Inputs

| Group | Inputs |
|---|---|
| External (ADM §12.2.1) | architecture reference materials |
| Non-architectural (ADM §12.2.2) | Request for Architecture Work |
| Architectural (ADM §12.2.3) | Organizational Model; Tailored Framework; Statement of Architecture Work; Architecture Vision; Architecture Repository; Architecture Definition Document; Architecture Requirements Specification; Architecture Roadmap; **Change Request — technology changes**; **Change Request — business changes**; **Change Request — from lessons learned**; Implementation Governance Model; **Architecture Contract (signed)**; **Compliance Assessments**; Implementation and Migration Plan |

Three kinds of Change Request, plus the two Phase G outputs (signed contract and Compliance
Assessments), are the distinctive inputs.

## Steps

Seven steps (ADM §12.3).

| # | Step | Key point |
|---|---|---|
| 1 | Establish value realization process | influence business projects to exploit the architecture for value (ADM §12.3.1) |
| 2 | Deploy monitoring tools | monitor technology and business changes that could affect the Baseline, track business value, capability maturity, asset management, QoS and business continuity (ADM §12.3.2) |
| 3 | Manage risks | manage EA risks and recommend on IT strategy (ADM §12.3.3) |
| 4 | Provide analysis for architecture change management | performance analysis and reviews, assess Change Requests against expected value and SLAs, gap analysis of the architecture's performance (ADM §12.3.4) |
| 5 | Develop change requirements to meet performance targets | recommendations and a position to act (ADM §12.3.5) |
| 6 | Manage governance process | arrange and hold the **Architecture Board** meeting to decide on changes and dispensations (ADM §12.3.6) |
| 7 | Activate the process to implement change | produce a **new Request for Architecture Work** and request for investment; record changes in the Architecture Repository (ADM §12.3.7) |

## Outputs

(ADM §12.4)

| Output | Change class |
|---|---|
| Architecture updates | maintenance |
| Changes to architecture framework and principles | maintenance |
| **New Request for Architecture Work**, to move to another cycle | major |
| Statement of Architecture Work, updated if necessary | |
| Architecture Contract, updated if necessary | |
| Compliance Assessments, updated if necessary | |

> **Trap.** The three change categories are the most examined Phase H fact. Only
> *re-architecting* change puts the whole architecture through the cycle again; *simplification*
> is handled by change management; *incremental* may be either. Distractors invent a fourth
> category ("corrective", "emergency") or swap the handling.

> **Trap.** Phase H's first objective is that the "architecture development cycle" is
> maintained — not "the architecture" or "the lifecycle". And Phase H does not re-architect
> anything itself: for a major change it issues a new Request for Architecture Work, and the
> cycle starts again at Phase A.

## Check yourself

1. Name the three change categories and say which one requires a new ADM cycle.
2. What stakeholder-count rule of thumb separates redesign from change management?
3. Which body decides how changes and dispensations are handled, and in which step?
4. Which three kinds of Change Request enter Phase H?
