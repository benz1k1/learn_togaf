---
title: Architecture Vision — Digital Channels
deliverable: Architecture Vision
phase: A
kind: DELIVERABLE
summary: The four-page agreed outcome the sponsor signs before detailed architecture starts; problem, objective of the Statement of Architecture Work, summary views, mapped requirements.
refs: ["CONTENT §4.2.8", "ADM §3.4", "ADM §3.3"]
source: authored
status: draft
---

> **What to notice.** The Vision is a *summary agreed early* so that stakeholders commit to an outcome before the architects spend months on detail. Its contents list is short: problem description (stakeholders, concerns, scenarios), the objective of the Statement of Architecture Work, summary views (typically a Value Chain and a Solution Concept diagram), mapped requirements, and a reference to the draft Architecture Definition Document. It is an output of Phase A (and updated in E); it is *not* the Architecture Definition Document, which carries the models.

| | |
|---|---|
| Reference | AV-2026-01, version 1.0 |
| Date | 31 March 2026 |
| Approved | Sponsor and Architecture Board, minute AB-2026-07 |

## 1. Problem description

### 1.1 Stakeholders and their concerns

| Stakeholder | Class | Key concern | Views that answer it |
|---|---|---|---|
| Head of Retail (sponsor) | Key player | Mobile adoption, cost to serve | Value Chain, Business Footprint |
| CIO | Key player | Fit with the Core Banking roadmap | Solution Concept, Application Communication |
| Compliance Officer | Keep satisfied | KYC and fraud controls | Data security views, Requirements catalog |
| Branch Manager (Branch Council) | Keep informed | Branch workload after the change | Process Flow, Organization Decomposition |
| Cards Ops Lead | Keep informed | Card authorisation latency | Interface catalog, Networked Computing diagram |

(The Stakeholder Map matrix on the Artefacts page is the source of this table.)

### 1.2 Business scenarios to be addressed

*Opening an account and paying from the phone* (Business Scenario BS-2026-01): onboarding, payment and fraud handling as experienced by the customer, the teller and the fraud analyst.

### 1.3 Issues to be addressed

- The bank responds a day late: verification, scoring and activation are overnight batches.
- Every channel integrates directly with Core Banking, so rules differ by channel.
- The app can show but not do.

## 2. Objective of the Statement of Architecture Work

Produce, by September 2026, the Target Architecture, two Transition Architectures and a funded Implementation and Migration Plan for mobile payments, digital onboarding and real-time fraud scoring, within £420k of architecture effort, such that mobile payments are live before the Q3 2027 card re-issue.

## 3. Summary views

**Value Chain diagram** (Artefacts page): primary activities *attract → onboarding → payments → lending → service and retain*, supported by risk and compliance and by technology; the programme changes onboarding and payments and adds real-time risk.

**Solution Concept diagram** (Artefacts page), in words: the customer uses the **Mobile App (new)** or the counter; both call an **API layer (new)**; behind it **Core Banking (existing)** remains the system of record and the **Card Switch (existing)** authorises cards against the card network, now calling a **Fraud Engine (new)** before it answers. **Identity verification** is marked "buy or build — investigate in Phase C".

**Objectives on the sketch:** open an account in under 10 minutes; pay from the phone without a branch visit; card blocked within 5 seconds of fraud. **Constraints on the sketch:** keep Core Banking as the system of record; go live before the Q3 card re-issue; no new customer data stores.

**Business Capability Map** with heat overlay: Customer Onboarding (identity verification, account opening, KYC review) and Payments (card payments, transfers) are the capabilities the engagement changes; Lending and the supporting capabilities are untouched.

## 4. Mapped requirements

| Id | Requirement | From | Objective it serves |
|---|---|---|---|
| RQ-01 | A customer can send a transfer from the Mobile App within 10 seconds end to end | Business Scenario | 60% mobile transfers |
| RQ-02 | Every card transaction is fraud-scored before authorisation is returned | Business Scenario | 30% fewer fraud losses |
| RQ-03 | Onboarding uses the same rules at the counter and in the app | Compliance Officer | Halve onboarding time; audit finding |
| RQ-04 | A suspected card is blocked within 5 seconds of scoring | Cards Ops Lead | 30% fewer fraud losses |
| CN-01 | Core Banking stays the system of record for Customer and Account | Principle PR-02 | — |
| CN-02 | Mobile payments live before the Q3 2027 card re-issue | Request for Architecture Work | — |
| CN-03 | No new customer data store | Request for Architecture Work | — |

Readiness: the Business Transformation Readiness Assessment (in the Capability Assessment) rates *Cards Operations' willingness to hand first-line blocking to an engine* as the highest risk; the vision therefore keeps analysts in the loop for the first six months.

## 5. Reference to the draft Architecture Definition Document

ADD-2026-01 v0.1 exists as an outline with this vision as chapter 1; Phases B–D fill the domain chapters.

**Signed:** P. Nandakumar, sponsor · L. Okafor, Chief Architect · 31 March 2026
