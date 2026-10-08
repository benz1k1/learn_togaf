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

<figure class="my-4">
<svg viewBox="0 0 760 264" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="A change request classified as simplification, incremental or re-architecting, and where each classification goes">
  <defs><marker id="arr-f4-18b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
  <rect x="10" y="14" width="200" height="46" rx="6" fill="#f4f4f4" stroke="#999"/><text x="110" y="34.5" text-anchor="middle" font-size="10.5">Change Request</text><text x="110" y="47.5" text-anchor="middle" font-size="10.5">(technology, business, lessons learned)</text><text x="110" y="80" text-anchor="middle" font-size="10.5" fill="#666">four activities: register events,</text><text x="110" y="92" text-anchor="middle" font-size="10.5" fill="#666">allocate resources, assess, evaluate impact</text><line x1="210" y1="37" x2="258" y2="37" stroke="#555" marker-end="url(#arr-f4-18b)"/><rect x="260" y="14" width="210" height="46" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/><text x="365" y="34.5" text-anchor="middle" font-size="10.5">Simplification change</text><text x="365" y="47.5" text-anchor="middle" font-size="10.5">reduce investment</text><line x1="470" y1="37" x2="518" y2="37" stroke="#555" marker-end="url(#arr-f4-18b)"/><rect x="520" y="14" width="230" height="46" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/><text x="635" y="41" text-anchor="middle" font-size="10.5">handled by change management</text><line x1="210" y1="37" x2="258" y2="109" stroke="#555" marker-end="url(#arr-f4-18b)"/><rect x="260" y="86" width="210" height="46" rx="6" fill="#fff1d6" stroke="#e0b060"/><text x="365" y="106.5" text-anchor="middle" font-size="10.5">Incremental change</text><text x="365" y="119.5" text-anchor="middle" font-size="10.5">derive more value from existing investment</text><line x1="470" y1="109" x2="518" y2="109" stroke="#555" marker-end="url(#arr-f4-18b)"/><rect x="520" y="86" width="230" height="46" rx="6" fill="#fff1d6" stroke="#e0b060"/><text x="635" y="106.5" text-anchor="middle" font-size="10.5">change management, or partial</text><text x="635" y="119.5" text-anchor="middle" font-size="10.5">re-architecting, depending on the change</text><line x1="210" y1="37" x2="258" y2="181" stroke="#555" marker-end="url(#arr-f4-18b)"/><rect x="260" y="158" width="210" height="46" rx="6" fill="#f3e3f7" stroke="#b58ac9"/><text x="365" y="178.5" text-anchor="middle" font-size="10.5">Re-architecting change</text><text x="365" y="191.5" text-anchor="middle" font-size="10.5">increase investment to create new value</text><line x1="470" y1="181" x2="518" y2="181" stroke="#555" marker-end="url(#arr-f4-18b)"/><rect x="520" y="158" width="230" height="46" rx="6" fill="#f3e3f7" stroke="#b58ac9"/><text x="635" y="178.5" text-anchor="middle" font-size="10.5">the whole architecture goes through</text><text x="635" y="191.5" text-anchor="middle" font-size="10.5">the development cycle again</text><path d="M635 204 L635 232 L110 232 L110 190" fill="none" stroke="#c0392b" stroke-dasharray="5 4" marker-end="url(#arr-f4-18b)"/><rect x="10" y="140" width="200" height="46" rx="6" fill="#f3e3f7" stroke="#c0392b"/><text x="110" y="160.5" text-anchor="middle" font-size="10.5">New Request for Architecture Work</text><text x="110" y="173.5" text-anchor="middle" font-size="10.5">→ a new cycle, starting at Phase A</text><text x="380" y="252" text-anchor="middle" font-size="10.5" fill="#666">Rule of thumb: a change that affects two or more stakeholders is likely to need redesign and re-entry to the ADM (ADM §12.5.3)</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">The three change categories and their handling. Original drawing; categories per ADM §12.5.2, the stakeholder rule per ADM §12.5.3.</figcaption>
</figure>

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

<figure class="my-4">
<svg viewBox="0 0 760 288" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="Phase H: its inputs, seven steps and outputs, with the new Request for Architecture Work marked as the deliverable that starts the next cycle">
  <defs><marker id="arr-f4-18" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
  <text x="107.5" y="18" text-anchor="middle" font-size="12" font-weight="bold" fill="#345">Inputs</text><text x="652.5" y="18" text-anchor="middle" font-size="12" font-weight="bold" fill="#345">Outputs</text><text x="380" y="18" text-anchor="middle" font-size="12" font-weight="bold" fill="#345">Steps</text><rect x="235" y="34" width="290" height="220" rx="8" fill="#fff1d6" stroke="#e0b060"/><text x="380" y="52" text-anchor="middle" font-size="12" font-weight="bold">Phase H: Architecture Change Management</text><text x="245" y="106.5" font-size="11">1 Establish value realization process</text><text x="245" y="121.5" font-size="11">2 Deploy monitoring tools</text><text x="245" y="136.5" font-size="11">3 Manage risks</text><text x="245" y="151.5" font-size="11">4 Provide analysis for change management</text><text x="245" y="166.5" font-size="11">5 Develop change requirements</text><text x="245" y="181.5" font-size="11">6 Manage governance process (Architecture Board)</text><text x="245" y="196.5" font-size="11">7 Activate the process to implement change</text><rect x="10" y="34" width="195" height="46" rx="6" fill="#e0ecff" stroke="#7aa2e3"/><text x="107.5" y="54.5" text-anchor="middle" font-size="10.5">Change Requests: technology,</text><text x="107.5" y="67.5" text-anchor="middle" font-size="10.5">business, and from lessons learned</text><line x1="205" y1="57" x2="233" y2="57" stroke="#555" marker-end="url(#arr-f4-18)"/><rect x="10" y="92" width="195" height="46" rx="6" fill="#e0ecff" stroke="#7aa2e3"/><text x="107.5" y="119" text-anchor="middle" font-size="10.5">Architecture Contract (signed)</text><line x1="205" y1="115" x2="233" y2="115" stroke="#555" marker-end="url(#arr-f4-18)"/><rect x="10" y="150" width="195" height="46" rx="6" fill="#e0ecff" stroke="#7aa2e3"/><text x="107.5" y="177" text-anchor="middle" font-size="10.5">Compliance Assessments</text><line x1="205" y1="173" x2="233" y2="173" stroke="#555" marker-end="url(#arr-f4-18)"/><rect x="10" y="208" width="195" height="46" rx="6" fill="#e0ecff" stroke="#7aa2e3"/><text x="107.5" y="228.5" text-anchor="middle" font-size="10.5">Implementation and Migration Plan;</text><text x="107.5" y="241.5" text-anchor="middle" font-size="10.5">Implementation Governance Model</text><line x1="205" y1="231" x2="233" y2="231" stroke="#555" marker-end="url(#arr-f4-18)"/><rect x="555" y="34" width="195" height="46" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/><text x="652.5" y="54.5" text-anchor="middle" font-size="10.5">Architecture updates</text><text x="652.5" y="67.5" text-anchor="middle" font-size="10.5">(maintenance change)</text><line x1="525" y1="57" x2="553" y2="57" stroke="#555" marker-end="url(#arr-f4-18)"/><rect x="555" y="92" width="195" height="46" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/><text x="652.5" y="106" text-anchor="middle" font-size="10.5">Changes to the architecture</text><text x="652.5" y="119" text-anchor="middle" font-size="10.5">framework and principles</text><text x="652.5" y="132" text-anchor="middle" font-size="10.5">(maintenance change)</text><line x1="525" y1="115" x2="553" y2="115" stroke="#555" marker-end="url(#arr-f4-18)"/><rect x="555" y="150" width="195" height="46" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/><text x="652.5" y="164" text-anchor="middle" font-size="10.5">New Request for Architecture Work,</text><text x="652.5" y="177" text-anchor="middle" font-size="10.5">to move to another cycle</text><text x="652.5" y="190" text-anchor="middle" font-size="10.5">(major change)</text><rect x="684" y="142" width="62" height="15" rx="7" fill="#f3e3f7" stroke="#b58ac9"/><text x="715" y="153" text-anchor="middle" font-size="9.5" fill="#5b2d6e">next cycle</text><line x1="525" y1="173" x2="553" y2="173" stroke="#555" marker-end="url(#arr-f4-18)"/><rect x="555" y="208" width="195" height="46" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/><text x="652.5" y="222" text-anchor="middle" font-size="10.5">Statement of Architecture Work,</text><text x="652.5" y="235" text-anchor="middle" font-size="10.5">Contract, Compliance Assessments:</text><text x="652.5" y="248" text-anchor="middle" font-size="10.5">updated if necessary</text><line x1="525" y1="231" x2="553" y2="231" stroke="#555" marker-end="url(#arr-f4-18)"/><text x="380" y="272" text-anchor="middle" font-size="11" fill="#666">Phase H does not re-architect anything itself: a major change raises a new Request and the cycle restarts at Phase A (ADM §12.4)</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">Inputs, steps and outputs of Phase H. Original drawing; inputs and outputs per ADM §12.2 and ADM §12.4, steps per ADM §12.3.</figcaption>
</figure>

> **Trap.** The three change categories are the most examined Phase H fact. Only
> *re-architecting* change puts the whole architecture through the cycle again; *simplification*
> is handled by change management; *incremental* may be either. Distractors invent a fourth
> category ("corrective", "emergency") or swap the handling.

> **Trap.** Phase H's first objective is that the "architecture development cycle" is
> maintained — not "the architecture" or "the lifecycle". And Phase H does not re-architect
> anything itself: for a major change it issues a new Request for Architecture Work, and the
> cycle starts again at Phase A.

<!-- figures:start -->
## Figures from the standard

The diagrams the cited sections carry, from your local copy of the publication. The exam reproduces these; know what each box is.

<div class="grid gap-4 md:grid-cols-2">
<figure class="max-w-lg"><img src="/figure/ADM:fig-12-1" alt="Figure 12-1: Phase H: Architecture Change Management" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 12-1: Phase H: Architecture Change Management (ADM)</figcaption></figure>
</div>
<!-- figures:end -->

## Check yourself

1. Name the three change categories and say which one requires a new ADM cycle.
2. What stakeholder-count rule of thumb separates redesign from change management?
3. Which body decides how changes and dispensations are handled, and in which step?
4. Which three kinds of Change Request enter Phase H?
