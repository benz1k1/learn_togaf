---
title: Architecture Requirements Specification v0.1
deliverable: Architecture Requirements Specification (draft)
phase: B
kind: DELIVERABLE
summary: The quantitative companion to the Definition Document — measurable criteria an implementation must meet — first produced in Phase B and grown through C, D and E until Phase F finalises it.
refs: ["CONTENT §4.2.6", "ADM §4.4", "ADM §13.4"]
source: authored
status: draft
---

> **What to notice.** Where the Definition Document says *what the architecture is*, this says *what an implementation must measurably do to comply*. It is first *produced* in Phase B (it is not among B's inputs), grows in C and D, and its contents form a major part of an implementation contract. The Requirements Management process updates it throughout. Every entry has an id so the Requirements catalog, the Architecture Contract and the Compliance Assessment can point at it.

| | |
|---|---|
| Reference | ARS-2026-01, version 0.1 (Phase B), 30 April 2026; v0.3 after Phase D; v1.0 finalised Phase F |
| Owner | Chief Architect; requirements in Jira project ARCH |

## 1. Success measures

| Id | Measure | Baseline | Target | Verified by |
|---|---|---|---|---|
| SM-01 | Median minutes per onboarding, counter or app | 45 | ≤ 10 | Core Banking activation timestamps |
| SM-02 | Share of transfers made in the Mobile App | 22% | 60% by 31 Dec 2027 | Monthly channel report |
| SM-03 | Card fraud loss per 1,000 cards | index 100 | ≤ 70 within 12 months of WP-4 go-live | Cards Operations loss ledger |
| SM-04 | Seconds from fraud score to card block | ~50,000 (14 h) | ≤ 5 | Fraud Engine and Card Switch logs |

## 2. Architecture requirements

| Id | Requirement | Domain | Source | Priority |
|---|---|---|---|---|
| RQ-01 | A transfer initiated in the Mobile App completes end to end within 10 seconds at the 95th percentile | Application | Business Scenario | Must |
| RQ-02 | Every card transaction receives a fraud score before the Card Switch returns an authorisation | Application | Business Scenario | Must |
| RQ-03 | Onboarding at the counter and in the app executes the same KYC rule set from the same service | Business | Compliance Officer | Must |
| RQ-04 | A card is blocked within 5 seconds of a score above the block threshold | Application | Cards Ops Lead | Must |
| RQ-05 | A customer may start onboarding in one channel and finish in another without re-entering evidence | Business | PR-05 | Should |
| RQ-06 | Identity evidence is retained no longer than 30 days after a decision | Data | Compliance Officer | Must |
| RQ-07 | Every new interface is described in OpenAPI 3 and registered in the Interface catalog before build | Application | Standards | Must |
| RQ-08 | Payments fail over to the DR data centre within 2 hours | Technology | Regulator | Must |
| RQ-09 | Fraud rules are editable by Cards Operations without a code release | Application | Cards Ops Lead | Must |

Requirements added in Phase C (RQ-10 to RQ-17: data entity ownership, API authentication, caching limits) and Phase D (RQ-18 to RQ-24: environments, network latency budget of 150 ms for scoring, key management) are in v0.3.

## 3. Business service contracts

| Service | Consumer | Provider | Service level |
|---|---|---|---|
| Verify identity | Counter, Mobile App | Identity Verification (WP-2) | Decision in ≤ 60 s for 95% of cases; availability 99.5% 07:00–23:00 |
| Transfer funds | Mobile App, counter, online site | Payments API (WP-1 over Core Banking) | 10 s end to end at p95; 99.9% availability |
| Screen transaction | Card Switch | Fraud Screening (WP-4) | Score in ≤ 150 ms at p99; 99.99% availability; on timeout the Switch authorises and flags |

## 4. Application service contracts

| Interface | From | To | Contract |
|---|---|---|---|
| IF-01 Account and transfer API | API layer | Core Banking | Vendor's REST API v12; idempotent transfers; rate 200 req/s |
| IF-02 Scoring call | Card Switch | Fraud Engine | Synchronous; 150 ms budget; ISO 8583 fields mapped per the interface catalog |
| IF-03 Identity decision | API layer | Identity Verification | Asynchronous with callback; evidence never stored by the API layer |

## 5. Implementation guidelines

- Channels contain presentation and channel-specific validation only; business rules live behind the API layer.
- Any cache of customer data is non-authoritative, expires within 15 minutes and is never written back.
- Fraud thresholds are configuration owned by Cards Operations.

## 6. Implementation specifications

- Mobile App: native iOS and Android; no embedded web views for payments.
- API layer: the selected API management product, configured not coded; one gateway per environment.
- Fraud Engine and identity verification: bought products, deployed in-country; integration through the API layer only.

## 7. Implementation standards

OpenAPI 3 for interfaces; OAuth 2.1 for channel authentication; ISO 8583 (network's fixed version) for card messages; the Technology Standards catalog for platforms.

## 8. Interoperability requirements

The Card Switch and Fraud Engine interoperate at the message level (ISO 8583 field mapping) with no shared database. The counter and app interoperate through the onboarding API's saved-state token, so a journey can move channel.

## 9. IT Service Management requirements

Monitoring of the three service levels above with alerts to the Digital Platform team; monthly service review with Cards Operations; change through the existing change-advisory board with the Implementation Governance Model's checkpoints as gates.

## 10. Constraints

CN-01 Core Banking stays the system of record for Customer and Account. CN-02 Mobile payments live before the Q3 2027 card re-issue. CN-03 No new customer data store. CN-04 No Core Banking change before July 2026. CN-05 Customer data stays in-country.

## 11. Assumptions

AS-01 The card network keeps its ISO 8583 message version through 2027 (to confirm in Phase D). AS-02 The Core Banking v12 REST API supports idempotent transfers (confirmed 12 May 2026). AS-03 Identity-verification products can meet the 60-second decision level for passports and driving licences.
