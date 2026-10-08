---
title: Phase H in practice, classifying the change before choosing the route
unit: P6
objectives: ["P6.1"]
refs: ["ADM §12", "ADM §12.1", "ADM §12.4", "ADM §12.5", "ADM §12.5.1", "ADM §12.5.2", "ADM §12.5.3", "GOV §4.2", "GOV §5.2.3", "CONTENT §4.2.11"]
reading_minutes: 9
source: authored
status: draft
---
## What a Phase H scenario looks like

The architecture has been deployed, the Architecture Contract fulfilled, and the scenario
now drops two or three change requests on the Architecture Board in the same week: a vendor
withdrawing a product, a business unit wanting a new field or channel, a merger or a new
regulation. It asks how each should be handled. The exam is not testing whether you can
design the change; it is testing whether you can *classify* it and choose the route the
standard prescribes for that class, because Phase H's job is to keep the development cycle
alive, execute the governance framework and keep the capability fit for current requirements
(ADM §12.1, ADM §12.5).

The five-point answer classifies each request as simplification, incremental or
re-architecting, applies the stakeholder-impact guideline, routes the first two through
change management under governance and starts a new cycle with a Request for Architecture
Work for the third, recording the decisions. The three-point answer picks the right route
for most requests but mis-classifies the large one. The one-point answer starts a new cycle
for everything. The zero-point answer refuses the requests or applies them without
governance.

## Drivers: where change comes from

The standard names three sources that have to be integrated: strategic top-down change to
create new capability, bottom-up change to correct or enhance capability under operations
management, and experience with previously delivered increments still being delivered by
projects (ADM §12.5.1). It then splits drivers into two families with different consequences.
Technology drivers (new technology reports, asset cost reduction, technology withdrawal,
standards initiatives) are normally manageable through change management and governance
processes. Business drivers (business-as-usual developments, exceptions, innovations,
business technology innovations, strategic change) often result in a complete
re-development of the architecture or at least an iteration of part of the cycle
(ADM §12.5.1). Spotting which family a planted fact belongs to is half the classification.

## The three classes and the investment lens

| Class | How it is handled | The investment view | Example in the standard |
|---|---|---|---|
| Simplification | Normally via change management techniques | Driven by a need to reduce investment | Ten systems reduced to one: the Baseline Technology Architecture description changes, the architecture above the physical layer does not (ADM §12.5.3) |
| Incremental | Change management, or partial re-architecting depending on the nature of the change | Driven by a need to derive additional value from existing investment | New technology or standards: refresh the Technology Architecture, not the whole Enterprise Architecture (ADM §12.5.3) |
| Re-architecting | Put the whole architecture through the development cycle again | Driven by a need to increase investment to create new value | Significant impact on business strategy: redo the whole Enterprise Architecture (ADM §12.5.3) |

The classification is reached through four activities: register every event that may impact
the architecture, allocate and manage resources for architecture tasks, have the responsible
process or role assess what should be done, and evaluate impacts (ADM §12.5.2).

<figure class="my-4">
<svg viewBox="0 0 760 330" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="11" role="img" aria-label="Phase H classification path: register the event, apply the stakeholder guideline, classify as simplification, incremental or re-architecting, and route to change management or a new Request for Architecture Work">
<defs><marker id="arr-p6h" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
<rect x="230" y="10" width="300" height="40" rx="8" fill="#f1f1f1" stroke="#999"/>
<text x="380" y="27" text-anchor="middle" font-weight="bold">Change Request or event registered (ADM §12.5.2)</text>
<text x="380" y="42" text-anchor="middle">technology driver or business driver? (ADM §12.5.1)</text>
<line x1="380" y1="50" x2="380" y2="78" stroke="#555" marker-end="url(#arr-p6h)"/>
<rect x="160" y="80" width="440" height="52" rx="8" fill="#fff" stroke="#666"/>
<text x="380" y="100" text-anchor="middle" font-weight="bold">Guideline (ADM §12.5.3)</text>
<text x="380" y="116" text-anchor="middle">two or more stakeholders impacted: likely redesign and re-entry to the ADM</text>
<text x="380" y="128" text-anchor="middle">one stakeholder, or allowable under a dispensation: candidate for change management</text>
<line x1="230" y1="132" x2="120" y2="180" stroke="#555" marker-end="url(#arr-p6h)"/>
<line x1="380" y1="132" x2="380" y2="180" stroke="#555" marker-end="url(#arr-p6h)"/>
<line x1="530" y1="132" x2="640" y2="180" stroke="#555" marker-end="url(#arr-p6h)"/>
<rect x="20" y="182" width="200" height="60" rx="8" fill="#e3f5e1" stroke="#7fbf7a"/>
<text x="120" y="202" text-anchor="middle" font-weight="bold">Simplification</text>
<text x="120" y="218" text-anchor="middle">reduce investment</text>
<text x="120" y="232" text-anchor="middle">change management techniques</text>
<rect x="280" y="182" width="200" height="60" rx="8" fill="#fff1d6" stroke="#e0b060"/>
<text x="380" y="202" text-anchor="middle" font-weight="bold">Incremental</text>
<text x="380" y="218" text-anchor="middle">more value from existing investment</text>
<text x="380" y="232" text-anchor="middle">change management or partial re-architecting</text>
<rect x="540" y="182" width="200" height="60" rx="8" fill="#fde8e6" stroke="#c0392b"/>
<text x="640" y="202" text-anchor="middle" font-weight="bold">Re-architecting</text>
<text x="640" y="218" text-anchor="middle">increase investment for new value</text>
<text x="640" y="232" text-anchor="middle">whole architecture through the cycle</text>
<line x1="120" y1="242" x2="120" y2="272" stroke="#555" marker-end="url(#arr-p6h)"/>
<line x1="380" y1="242" x2="380" y2="272" stroke="#555" marker-end="url(#arr-p6h)"/>
<line x1="640" y1="242" x2="640" y2="272" stroke="#555" marker-end="url(#arr-p6h)"/>
<rect x="20" y="274" width="460" height="44" rx="6" fill="#fff" stroke="#666"/>
<text x="250" y="292" text-anchor="middle" font-weight="bold">architecture update, framework or principles update</text>
<text x="250" y="308" text-anchor="middle">maintenance change outputs, under the Architecture Board (ADM §12.4)</text>
<rect x="540" y="274" width="200" height="44" rx="6" fill="#fff" stroke="#c0392b"/>
<text x="640" y="292" text-anchor="middle" font-weight="bold">new Request for Architecture Work</text>
<text x="640" y="308" text-anchor="middle">to move to another cycle (ADM §12.4)</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">The Phase H classification path from registered event to route. Original drawing; the classes and the guideline follow ADM §12.5.2 and §12.5.3, the outputs §12.4.</figcaption>
</figure>

## The guideline that decides the borderline cases

Most scenarios plant one request that sits on the boundary between incremental and
re-architecting. The standard's guideline is short and quotable: if the change impacts two
stakeholders or more it is likely to require an architecture redesign and re-entry to the
ADM; if it impacts only one stakeholder it is more likely a candidate for change management;
if it can be allowed under a dispensation it is more likely a candidate for change management
(ADM §12.5.3). A refreshment cycle, partial or complete re-architecting, is required when
the Foundation Architecture must be realigned with business strategy, when substantial
change is required to components and guidelines used in deployment, or when significant
standards in the product architecture change with significant end-user impact, regulatory
change being the example given; and in that case a new Request for Architecture Work *must*
be issued (ADM §12.5.3).

**Trap.** "Regulatory change" is not automatically re-architecting. The test is whether the
standards change has significant end-user impact or realigns the foundation with strategy;
a regulation that changes one calculation in one system for one stakeholder is closer to
change management (ADM §12.5.3).

**Trap.** A new Request for Architecture Work is the output for *major* changes; maintenance
changes produce architecture updates and changes to framework and principles, plus updated
Statement of Architecture Work, Architecture Contract and Compliance Assessments if needed
(ADM §12.4).

## Governance around the decision

The governance body must establish criteria to judge whether a Change Request warrants an
architecture update or a new cycle, and must guard against "creeping elegance" by looking for
changes that relate directly to business value; an Architecture Compliance report states
whether the change is compliant, an exemption may be granted with valid rationale, and a high
impact change needs a strategy to manage its impact (ADM §12.5). The Architecture Board
assesses and approves Requests for Change and must decide whether to approve one or whether a
project already in a Transition Architecture will resolve it (ADM §12.5.1); the board is
responsible for granting dispensations in keeping with the technology strategy and for
identifying divergence and planning realignment (GOV §4.2). The business stakeholders'
Architecture Contract is the instrument used to manage change in Phase H (GOV §5.2.3), and a
Change Request that changes the architecture carries an impact assessment naming the phases
to revisit (CONTENT §4.2.11).

## How the 5, 3 and 1 differ

| Answer | Why it scores that |
|---|---|
| 5 | Registers all three requests, classifies the retirement as simplification and the new field as incremental (one stakeholder each, allowable under existing governance), classifies the acquisition or strategy shift as re-architecting because it impacts many stakeholders and realigns the foundation with strategy, issues a Request for Architecture Work for it, and records the decisions and compliance position through the board |
| 3 | Handles the small changes correctly but treats the strategic change as incremental "because the contract is still current"; the contract does not cover a change that realigns the foundation with strategy (ADM §12.5.3) |
| 1 | Starts a new ADM cycle for everything; the standard reserves the full cycle for re-architecting change and handles the rest by change management (ADM §12.5.2) |
| 0 | Declines the requests until a scheduled review, or applies them directly without classification; Phase H exists to receive and assess change, under governance (ADM §12.1, ADM §12.5) |

## Where to look in the book

ADM chapter 12: §12.5.1 for drivers, §12.5.2 for the three classes and the four activities,
§12.5.3 for the stakeholder guideline and the refreshment triggers, §12.4 for which output
matches which class. EA Capability and Governance §4.2 for the Architecture Board's
responsibilities and §5.2.3 for the contract used in Phase H. Architecture Content §4.2.11
for the Change Request contents.

## Check yourself

- Which class is "driven by a requirement to derive additional value from existing investment"?
- State the three-part stakeholder guideline from memory.
- What must be issued when a refreshment cycle is needed?
