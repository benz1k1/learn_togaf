---
title: Phase A, Architecture Vision, in depth
unit: F4
objectives: ["4.2", "4.3"]
refs: ["ADM §3", "ADM §3.1", "ADM §3.2", "ADM §3.2.1", "ADM §3.2.2", "ADM §3.2.3", "ADM §3.3", "ADM §3.3.1", "ADM §3.3.2", "ADM §3.3.3", "ADM §3.3.4", "ADM §3.3.5", "ADM §3.3.6", "ADM §3.3.7", "ADM §3.3.8", "ADM §3.3.9", "ADM §3.3.10", "ADM §3.3.11", "ADM §3.4", "ADM §3.5", "ADM §3.5.1", "ADM §3.5.2"]
reading_minutes: 12
source: authored
status: draft
---
## What the phase is for

Phase A is the first phase of a cycle. It scopes the effort, identifies the stakeholders,
creates the Architecture Vision and gets the approvals to proceed (ADM §3). Its two objectives
(ADM §3.1):

| Objective | In plain words |
|---|---|
| Develop a high-level **aspirational vision** of the capabilities and business value the proposed Enterprise Architecture will deliver | sell the outcome before doing the detailed work |
| Obtain approval for a **Statement of Architecture Work** that defines a program of works to develop and deploy that architecture | get the sponsor to sign |

## Approach

Phase A starts with the receipt of a **Request for Architecture Work** from the sponsoring
organization (ADM §3.5.1). It defines what is inside and outside scope and the constraints;
scoping here is restricted to this cycle's objectives, inside the overall scope the Preliminary
Phase set. If the framework in place cannot achieve the desired vision, the Preliminary Phase is
revisited and extended. Business principles, goals, drivers and Architecture Principles are
normally already defined; Phase A checks they are current and clarifies ambiguity, defining them
for the first time only if they do not exist (ADM §3.5.1).

Creating the vision (ADM §3.5.2): the Architecture Vision is the sponsor's tool to sell the
benefits of the proposed capability to stakeholders and decision makers. Clarifying and agreeing
the *purpose* of the effort is the whole point. The phase looks for existing Business
Architecture material — **business capabilities, value streams and organization maps** — and may
also explore additional domains (information, security, digital, and so on). A business
assessment, typically with business scenarios, weighs courses of action and picks the best one.
The vision is a first-cut, high-level description of the Baseline and Target Architectures across
Business, Data, Application and Technology; consensus is represented by the sponsor **signing the
Statement of Architecture Work**.

## Inputs

| Group | Inputs |
|---|---|
| External reference materials (ADM §3.2.1) | architecture reference materials |
| Non-architectural (ADM §3.2.2) | **Request for Architecture Work**; business principles, business goals and business drivers |
| Architectural (ADM §3.2.3) | Organizational Model for Enterprise Architecture; Tailored Architecture Framework (including Architecture Principles and business principles when pre-existing); populated Architecture Repository |

Every architectural input is a Preliminary Phase output.

## Steps

Eleven steps; the order and timing may be adapted under the governance in force (ADM §3.3).

| # | Step | Key point |
|---|---|---|
| 1 | Establish the architecture project | each ADM cycle is normally run as a project using the enterprise's project management framework (ADM §3.3.1) |
| 2 | Identify stakeholders, concerns and business requirements | produces the **stakeholder map**, which feeds the Architecture Vision, the Communications Plan and the Statement of Architecture Work; out-of-scope requirements go to the Requirements Repository (ADM §3.3.2) |
| 3 | Confirm and elaborate business goals, business drivers and constraints | check existing definitions are current; define enterprise-wide and project-specific constraints (ADM §3.3.3) |
| 4 | Evaluate capabilities | both the enterprise's capability to *do* architecture and its baseline/target business capability; results go into the **Capability Assessment**; detailed business capability gap work belongs in Phase B (ADM §3.3.4) |
| 5 | Assess readiness for business transformation | a **Business Transformation Readiness Assessment**; its results are added to the Capability Assessment and shape scope, activities and risk (ADM §3.3.5) |
| 6 | Define scope | breadth, level of detail, partitioning, domains, time period, assets to re-use; baseline need not be at the same detail as target (ADM §3.3.6) |
| 7 | Confirm and elaborate Architecture Principles, including business principles | principles normally come from the Preliminary Phase (ADM §3.3.7) |
| 8 | Develop Architecture Vision | high-level view of Baseline and Target; a **solution concept diagram** is common practice; business scenarios discover requirements (ADM §3.3.8) |
| 9 | Define the Target Architecture value propositions and KPIs | business case, value proposition per stakeholder group, procurement requirements, performance metrics, business risk; goes into the Statement of Architecture Work (ADM §3.3.9) |
| 10 | Identify the business transformation risks and mitigation activities | **initial** and **residual** levels of risk; mitigation goes in the Statement of Architecture Work (ADM §3.3.10) |
| 11 | Develop Statement of Architecture Work; secure approval | resources, roadmap and schedule, performance metrics, the **Communications Plan**, sponsor sign-off (ADM §3.3.11) |

## Outputs

(ADM §3.4)

| Output | Contents worth knowing |
|---|---|
| **Approved Statement of Architecture Work** | project description and scope, overview of the vision, plan and schedule |
| Refined statements of business principles, goals and drivers | |
| Architecture Principles | |
| **Capability Assessment** | includes the readiness results |
| Tailored Architecture Framework, for the engagement | |
| **Architecture Vision** | problem description, objective of the Statement of Architecture Work, summary views, optional business scenario, refined key high-level stakeholder requirements |
| Draft Architecture Definition Document | may already include Baseline and/or Target of any domain |
| **Communications Plan** | |
| Additional content populating the Architecture Repository | |

<figure class="my-4">
<svg viewBox="0 0 760 294" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="Phase A: its inputs, eleven steps and outputs, with the deliverables it produces first">
  <defs><marker id="arr-f4-11" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
  <text x="107.5" y="18" text-anchor="middle" font-size="12" font-weight="bold" fill="#345">Inputs</text><text x="652.5" y="18" text-anchor="middle" font-size="12" font-weight="bold" fill="#345">Outputs</text><text x="380" y="18" text-anchor="middle" font-size="12" font-weight="bold" fill="#345">Steps</text><rect x="235" y="34" width="290" height="226" rx="8" fill="#fff1d6" stroke="#e0b060"/><text x="380" y="52" text-anchor="middle" font-size="12" font-weight="bold">Phase A: Architecture Vision</text><text x="245" y="72" font-size="11">1 Establish the architecture project</text><text x="245" y="87" font-size="11">2 Identify stakeholders, concerns, requirements</text><text x="245" y="102" font-size="11">3 Confirm goals, drivers and constraints</text><text x="245" y="117" font-size="11">4 Evaluate capabilities</text><text x="245" y="132" font-size="11">5 Assess readiness for transformation</text><text x="245" y="147" font-size="11">6 Define scope</text><text x="245" y="162" font-size="11">7 Confirm and elaborate Architecture Principles</text><text x="245" y="177" font-size="11">8 Develop Architecture Vision</text><text x="245" y="192" font-size="11">9 Define value propositions and KPIs</text><text x="245" y="207" font-size="11">10 Identify transformation risks</text><text x="245" y="222" font-size="11">11 Develop Statement of Architecture Work;</text><text x="245" y="237" font-size="11">     secure approval</text><rect x="10" y="37" width="195" height="46" rx="6" fill="#e0ecff" stroke="#7aa2e3"/><text x="107.5" y="57.5" text-anchor="middle" font-size="10.5">Request for Architecture Work</text><text x="107.5" y="70.5" text-anchor="middle" font-size="10.5">(the trigger)</text><line x1="205" y1="60" x2="233" y2="60" stroke="#555" marker-end="url(#arr-f4-11)"/><rect x="10" y="95" width="195" height="46" rx="6" fill="#e0ecff" stroke="#7aa2e3"/><text x="107.5" y="115.5" text-anchor="middle" font-size="10.5">Business principles,</text><text x="107.5" y="128.5" text-anchor="middle" font-size="10.5">goals and drivers</text><line x1="205" y1="118" x2="233" y2="118" stroke="#555" marker-end="url(#arr-f4-11)"/><rect x="10" y="153" width="195" height="46" rx="6" fill="#e0ecff" stroke="#7aa2e3"/><text x="107.5" y="173.5" text-anchor="middle" font-size="10.5">Organizational Model for EA;</text><text x="107.5" y="186.5" text-anchor="middle" font-size="10.5">Tailored Architecture Framework</text><line x1="205" y1="176" x2="233" y2="176" stroke="#555" marker-end="url(#arr-f4-11)"/><rect x="10" y="211" width="195" height="46" rx="6" fill="#e0ecff" stroke="#7aa2e3"/><text x="107.5" y="238" text-anchor="middle" font-size="10.5">Populated Architecture Repository</text><line x1="205" y1="234" x2="233" y2="234" stroke="#555" marker-end="url(#arr-f4-11)"/><rect x="555" y="37" width="195" height="46" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/><text x="652.5" y="57.5" text-anchor="middle" font-size="10.5">Approved Statement of</text><text x="652.5" y="70.5" text-anchor="middle" font-size="10.5">Architecture Work</text><rect x="711" y="29" width="35" height="15" rx="7" fill="#f3e3f7" stroke="#b58ac9"/><text x="728.5" y="40" text-anchor="middle" font-size="9.5" fill="#5b2d6e">first</text><line x1="525" y1="60" x2="553" y2="60" stroke="#555" marker-end="url(#arr-f4-11)"/><rect x="555" y="95" width="195" height="46" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/><text x="652.5" y="122" text-anchor="middle" font-size="10.5">Architecture Vision</text><rect x="711" y="87" width="35" height="15" rx="7" fill="#f3e3f7" stroke="#b58ac9"/><text x="728.5" y="98" text-anchor="middle" font-size="9.5" fill="#5b2d6e">first</text><line x1="525" y1="118" x2="553" y2="118" stroke="#555" marker-end="url(#arr-f4-11)"/><rect x="555" y="153" width="195" height="46" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/><text x="652.5" y="173.5" text-anchor="middle" font-size="10.5">Capability Assessment</text><text x="652.5" y="186.5" text-anchor="middle" font-size="10.5">(with the readiness results)</text><rect x="711" y="145" width="35" height="15" rx="7" fill="#f3e3f7" stroke="#b58ac9"/><text x="728.5" y="156" text-anchor="middle" font-size="9.5" fill="#5b2d6e">first</text><line x1="525" y1="176" x2="553" y2="176" stroke="#555" marker-end="url(#arr-f4-11)"/><rect x="555" y="211" width="195" height="46" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/><text x="652.5" y="238" text-anchor="middle" font-size="10.5">Communications Plan</text><rect x="711" y="203" width="35" height="15" rx="7" fill="#f3e3f7" stroke="#b58ac9"/><text x="728.5" y="214" text-anchor="middle" font-size="9.5" fill="#5b2d6e">first</text><line x1="525" y1="234" x2="553" y2="234" stroke="#555" marker-end="url(#arr-f4-11)"/><text x="380" y="278" text-anchor="middle" font-size="11" fill="#666">Not an output: the Architecture Requirements Specification, which first appears in Phase B (ADM §4.4)</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">Inputs, steps and outputs of Phase A. Original drawing; inputs and outputs per ADM §3.2 and ADM §3.4, steps per ADM §3.3.</figcaption>
</figure>

> **Trap.** Inputs versus outputs of Phase A is the single most tested pair in this unit. The
> **Request** for Architecture Work goes *in*; the **Statement** of Architecture Work comes *out*
> (approved). The Architecture Vision, Communications Plan and Capability Assessment are all
> *first produced* here. The Architecture Requirements Specification is *not* a Phase A output — it
> first appears in Phase B.

> **Trap.** The readiness assessment is *done* in Phase A (step 5) and *reviewed* in Phase E
> (step 7). The Capability Assessment carries it forward.

## Check yourself

1. What document triggers Phase A, and what document ends it?
2. Which step produces the stakeholder map, and which three outputs does the map feed?
3. Which two levels of risk does step 10 distinguish?
4. Name three outputs that Phase A produces for the first time in the cycle.
