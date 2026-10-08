---
title: Architecture Roadmap — work packages, transitions and implementation factors
deliverable: Architecture Roadmap
phase: E
kind: DELIVERABLE
summary: The work package portfolio laid on a timeline with two Transition Architectures, the Implementation Factor catalog and the Consolidated Gaps, Solutions and Dependencies matrix — Phase E's first complete version.
refs: ["CONTENT §4.2.7", "ADM §9.4", "ADM §9.3"]
source: authored
status: draft
---

> **What to notice.** Phase E produces the *initial complete* roadmap; Phase F finalises it. It is built from the roadmap components Phases B, C and D handed over. Its contents list has five parts — work package portfolio, Implementation Factor catalog, Consolidated Gaps/Solutions/Dependencies matrix, Transition Architectures, implementation recommendations — and two of those (the factor catalog at step 1 and the consolidated matrix at step 3) are Phase E *techniques*, which is why they appear here and not earlier. Phase E also *reviews* the readiness assessment conducted in Phase A (step 7).

| | |
|---|---|
| Reference | AR-2026-01, version 1.0 (Phase E), 29 August 2026; v1.1 finalised in Phase F |
| Approved | Architecture Board minute AB-2026-14 |

## 1. Work package portfolio

| WP | Name | Objectives and deliverables | Functional requirements | Dependencies | Opportunity | ADD / ARS reference | Business value |
|---|---|---|---|---|---|---|---|
| WP-1 | Platform and API layer | Platform services and the channel API layer live in both data centres; Payments and Card Management APIs first | RQ-01, RQ-07, RQ-08 | Platform team formed (RC-B1); Core Banking v12 complete | Enables every other package; re-used by Lending | ABB-01, ABB-06; ARS §3–4 | Indirect: prerequisite |
| WP-2 | Digital onboarding | Identity Verification service bought and integrated; Onboarding API; app and counter journeys | RQ-03, RQ-05, RQ-06 | WP-1; Compliance procedure (RC-B2) | Ten-minute onboarding | ABB-02, ABB-04 | SM-01: halve counter time; new-to-bank growth |
| WP-3 | Mobile payments launch | Mobile App v4 with transfers and card controls; SMS gateway retired | RQ-01 | WP-1 | Mobile share of transfers | ABB-04; Project Context diagram on the Artefacts page | SM-02: 60% mobile transfers |
| WP-4 | Real-time fraud scoring | Fraud Engine bought and hosted; Card Switch calls it; analyst-in-the-loop for six months | RQ-02, RQ-04, RQ-09, RQ-18 | WP-1 (platform); dual-homed card link (RC-D2); Cards Ops readiness | Fraud losses | ABB-03, ABB-05 | SM-03, SM-04: 30% lower losses |
| WP-5 | Card network dual-homing and pre-prod | Network change; pre-prod environment | RQ-08 | Data-centre change window | Resilience | RC-D2, RC-D3 | Regulatory; enables WP-4 |

## 2. Implementation Factor catalog

| Factor | Type | Description | Impact |
|---|---|---|---|
| Card re-issue Q3 2027 | Dependency | Cards must ship with in-app controls | Fixes Transition 1 at Q2 2027 |
| Retail IT capacity | Risk | Committed to v12 until June 2026 | WP-1 starts with the platform team, not Retail IT |
| Analyst acceptance | Risk (R-1) | Resistance to engine-led blocking | Six-month analyst-in-the-loop in WP-4 |
| Vendor procurement lead time | Assumption | Verification and fraud products selectable within four months | WP-2 and WP-4 procurement starts in Phase F, before funding of build |
| ISO 8583 version | Assumption (AS-01) | Network version fixed through 2027 | Confirmed by the network 20 August 2026 |
| Branch closure programme | Dependency | Teller retraining must follow closure announcements | WP-2 counter rollout after Q1 2027 |
| Data-centre change window | Issue | One window per quarter | WP-5 booked for Q4 2026 |
| Run cost +£640k/yr | Input | From the impact assessment | Business case in Phase F |
| Regulator's DR rule | Input | Two-hour failover | WP-5 precedes WP-4 |
| Action: form platform team | Action | Four hires or moves by October 2026 | Owner: CIO |

## 3. Consolidated Gaps, Solutions and Dependencies matrix

| Domain | Gap | Potential solution | Dependencies |
|---|---|---|---|
| Business | Identity verification by a person | Verification service, teller retraining (WP-2) | Compliance procedure; branch closures |
| Business | Fraud blocking next morning | Real-time screening with analyst-in-the-loop (WP-4) | Cards Ops readiness; WP-5 |
| Data | Uncontrolled evidence; no cross-channel journey state | Evidence store in the service; journey token in the API layer (WP-2, WP-1) | WP-1 first |
| Application | No service layer; app cannot act | API layer; Mobile App v4 (WP-1, WP-3) | Platform team; v12 done |
| Application | No scoring or verification applications | Buy (WP-4, WP-2) | Procurement; ARS |
| Technology | No platform; single-homed card link; no pre-prod | Platform build; dual-homing; pre-prod (WP-1, WP-5) | Change window |

## 4. Transition Architectures

| State | Date | Contains | Business value released |
|---|---|---|---|
| **Transition 1** | Q2 2027 (before the card re-issue) | WP-1 Payments and Card Management APIs; WP-3 Mobile App v4 with transfers and card controls; SMS gateway retired; WP-5 dual-homing and pre-prod | Mobile transfers; in-app card controls for the re-issue |
| **Transition 2** | Q4 2027 | WP-2 onboarding in app and at the counter; WP-4 scoring before authorisation, analysts in the loop | Ten-minute onboarding; fraud losses start falling |
| **Target** | mid-2028 | Automatic blocking above threshold; online banking site retired; Lending starts on the API layer (next cycle) | Full objectives; re-use |

The Transition Architecture chapter of the Definition Document (chapter 10) is now written from this table, with the business, data, application and technology state for each transition.

## 5. Implementation recommendations

- **Criteria and measures of effectiveness**: the four success measures SM-01 to SM-04 of the Requirements Specification, reported quarterly to the Board from Transition 1.
- **Risks and issues**: R-1 (analyst acceptance) and R-3 (IT capacity) from the readiness review; the scoring timeout policy is the mitigation for engine outage.
- **Solution Building Blocks**: SBB-01 API gateway product and SBB-06 platform selected in this phase; SBB-02 verification and SBB-03 fraud products to be selected by procurement against the Requirements Specification; SBB-04 Mobile App v4 built in-house; SBB-05 Card Switch change ordered from the vendor.
- **Sequence**: WP-1 → WP-3 and WP-5 in parallel → WP-2 and WP-4 in parallel. Value first (payments), then risk (scoring), because the re-issue date cannot move.
