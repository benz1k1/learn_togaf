---
title: Statement of Architecture Work — Digital Channels cycle
deliverable: Statement of Architecture Work
phase: A
kind: DELIVERABLE
summary: The contract between the sponsor and the architecture team for this cycle — scope, approach, roles, plan, acceptance and change procedure — approved at the end of Phase A.
refs: ["CONTENT §4.2.20", "ADM §3.4", "ADM §3.3"]
source: authored
status: draft
---

> **What to notice.** The Statement of Architecture Work is an *output* of Phase A, signed by the sponsor; the Request for Architecture Work is the *input*. It is the document the architecture project is measured against, and it can be the basis of a contract between the supplier and consumer of architecture services — which is why it has acceptance criteria and a change-of-scope procedure. It is *updated*, not rewritten, at the end of each later phase (the table lists it as an output of A through H).

| | |
|---|---|
| Reference | SAW-2026-01, version 1.0 |
| Date | 31 March 2026 |
| Approved by | Priya Nandakumar (sponsor); Architecture Board minute AB-2026-07 |

## 1. Title

Digital Channels: architecture for mobile payments, digital onboarding and real-time fraud scoring.

## 2. Architecture project request and background

Request for Architecture Work RAW-2026-01 (12 January 2026) asked for the architecture that lets the "Digital First" strategy be planned and costed: mobile payments before the Q3 2027 card re-issue, account opening in under ten minutes, and a 30% reduction in card fraud losses. The Preliminary Phase established the architecture capability, principles and repository (Board minute AB-2026-04). Phase A ran the Business Scenario workshops in March and agreed three SMART objectives with the stakeholders.

## 3. Architecture project description and scope

**In scope.**

- Business, Data, Application and Technology Architectures for the Retail Banking segment as touched by onboarding, payments and card fraud.
- Baseline and Target Architectures; two Transition Architectures split by the Q3 2027 card re-issue.
- The Architecture Roadmap and the Implementation and Migration Plan for the programme envelope of £6.5m.
- Architecture governance of the resulting delivery projects through Phase G.

**Out of scope.** Lending (recorded as a candidate for the next cycle); replacement of the Data Warehouse (constraint only: nothing may extend its life past 2028); any change to Core Banking before its v12 upgrade completes in June 2026.

**Architecture domains and depth.** All four domains. Business and Application to the level of services and interfaces; Data to the logical level for Customer, Account, Card and Transaction; Technology to the platform and environment level.

**Time horizon.** Baseline as at March 2026; target at the end of 2028; transitions at Q2 2027 and Q4 2027.

## 4. Overview of the Architecture Vision

Customers act in the app or at the counter and the bank responds in seconds: one service layer used by every channel, real-time fraud scoring before authorisation, identity verified digitally, Core Banking unchanged as the system of record. Full statement in the Architecture Vision AV-2026-01.

## 5. Specific change of scope procedures

1. Any party may raise a scope change through a Change Request in the repository template.
2. Impact is assessed by the Chief Architect within five working days: effect on the plan in section 8, on the budget, on the objectives.
3. Changes under £50k or ten days' effort are approved by the sponsor and the Chief Architect jointly; larger ones go to the Architecture Board and, if the £420k budget is exceeded, to the Retail Investment Committee.
4. An approved change produces a new version of this Statement; the previous version is retained in the Governance Log.

## 6. Roles, responsibilities and deliverables

| Role | Who | Responsible for |
|---|---|---|
| Sponsor | Head of Retail | Accepts each deliverable; owns the business objectives |
| Chief Architect | Lena Okafor | The cycle; Architecture Definition Document; this Statement |
| Business, application, technology architects; loaned data architect | Desai, Chen, Price, Al-Sayed | Their domain chapters, catalogs and diagrams |
| Architecture Board | CIO (chair) and members per the Organizational Model | Phase-gate approvals, waivers |
| Stakeholder representatives | Cards Ops Lead, Branch Council chair, Compliance Officer | Review at each gate for their concerns |

Deliverables by phase: A — Architecture Vision, Communications Plan, Capability Assessment, this Statement. B–D — Architecture Definition Document (draft), Architecture Requirements Specification (draft), roadmap components. E — Architecture Roadmap, Transition Architectures, Implementation and Migration Plan (draft). F — finalised Definition Document, Requirements Specification and Roadmap; approved Implementation and Migration Plan; Implementation Governance Model. G — Architecture Contracts, Compliance Assessments. H — change classification, lessons learned, re-scored maturity.

## 7. Acceptance criteria and procedures

A phase is complete when its deliverables are in the repository at state *approved* with an Architecture Board minute, the sponsor has signed the acceptance sheet, and — for Phases B to F — every open requirement in the Requirements catalog is either addressed in the Definition Document or listed in the Requirements Impact Assessment with a decision. The cycle is accepted when the Phase F gate passes and the Retail Investment Committee funds the first two work packages.

## 8. Architecture project plan and schedule

| Phase | Window | Gate |
|---|---|---|
| A Architecture Vision | March 2026 | 31 March (this approval) |
| B Business Architecture | April 2026 | combined gate |
| C Information Systems Architectures | May–June 2026 | combined gate |
| D Technology Architecture | July 2026 | 31 July |
| E Opportunities and Solutions | August 2026 | 29 August |
| F Migration Planning | September 2026 | 26 September, to the Investment Committee 30 September |
| G Implementation Governance | October 2026 – Q4 2027 | per project checkpoints |
| H Architecture Change Management | continuous; formal review September 2027 | — |

Effort: 4 architects at 60% plus the data architect for Phase C, within the £420k in the Organizational Model.

## 9. Approvals

| | Name | Role | Date |
|---|---|---|---|
| Sponsor | Priya Nandakumar | Head of Retail Banking | 31 March 2026 |
| Architecture | Lena Okafor | Chief Architect | 31 March 2026 |
| Board | Tomasz Weber | CIO, Architecture Board chair | 31 March 2026 |
