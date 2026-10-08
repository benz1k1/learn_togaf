---
title: Architecture Contract — Project P5 Fraud Scoring
deliverable: Architecture Contract
phase: G
kind: DELIVERABLE
summary: The signed Architecture Design and Development Contract between the P5 project and the architecture function, following the contents list for that contract type.
refs: ["CONTENT §4.2.2", "ADM §11.3", "GOV §5"]
source: authored
status: draft
---

> **What to notice.** The contract enters Phase G as a *standard* (template) and leaves it *signed* by the developing and sponsoring organisations (step 3). The standard gives two contents lists — an Architecture Design and Development Contract and a Business Users' Architecture Contract; this is the first kind. It binds the project to the Definition Document and Requirements Specification by id, which is what the Compliance Assessments later check.

| | |
|---|---|
| Reference | AC-2027-05, signed 20 January 2027 |
| Parties | Northgate Bank Enterprise Architecture (architecture organisation); Project P5 Fraud Scoring, Retail IT with the Fraud Engine vendor (developing organisation); Head of Retail (sponsor) |

## 1. Introduction and background

Project P5 delivers work package WP-4 of the Architecture Roadmap AR-2026-01: real-time fraud scoring before card authorisation, with Cards Operations analysts in the loop for six months. It realises Architecture Building Blocks ABB-03 Fraud Screening Service and the change to ABB-05 Card Authorisation, in Transition Architecture 2 (Q4 2027).

## 2. The nature of the agreement

A joint agreement on the deliverables, quality and fitness for purpose of the architecture P5 implements, governed under the Implementation Governance Model IGM-2026-01. It is not a commercial contract; the vendor's commercial terms sit with procurement and refer to this document for architecture conformance.

## 3. Scope of the architecture

In scope: the Fraud Engine and its hosting on Platform Services; the Card Switch's synchronous scoring call (IF-02) and timeout policy; the Kafka card-event feed; rule administration for Cards Operations; the analyst review console. Out of scope: any change to Core Banking; the Data Warehouse fraud batch (retired at Transition 2 by P5, but owned by Finance); automatic blocking (a Phase H change after the in-the-loop period).

## 4. Architecture and strategic principles and requirements

Principles binding on the project: PR-01 (a named steward for Fraud Score data), PR-03 (bought engine; no bespoke scoring code), PR-04 (threat model before checkpoint 1; secrets manager; no shared credentials). Requirements: RQ-02, RQ-04, RQ-09, RQ-18 and success measures SM-03, SM-04 from ARS-2026-01 v1.0; constraint CN-05 (in-country hosting).

## 5. Conformance requirements

- Design conforms to ADD-2026-01 v1.0 chapters 5c, 5d and 10 (Transition 2).
- Interface IF-02 is described in OpenAPI 3 / ISO 8583 mapping in the Interface catalog before build (RQ-07).
- Timeout behaviour: on no score within 150 ms the Card Switch authorises and flags; never declines on timeout.
- Fraud thresholds and rules are configuration owned by Cards Operations, changeable without a release.
- Any deviation is raised as a Change Request before it is built.

## 6. Architecture development and management process and roles

Per IGM-2026-01: EA member on the project board — Mei Chen; independent compliance reviewer — Owen Price; solution architect — the vendor's lead architect with Retail IT's Anil Shah; rule owner — Cards Ops Lead. Checkpoints at design sign-off and before the change-advisory board; Change Requests through the Chief Architect.

## 7. Target Architecture measures

| Measure | Target | Evidence |
|---|---|---|
| Score latency (RQ-18) | ≤ 150 ms at p99 in pre-prod at 300 tx/s | Load test report at checkpoint 2 |
| Block latency (RQ-04) | ≤ 5 s from score to block | End-to-end test |
| Availability | 99.99% for the scoring service | Platform monitoring, monthly |
| Rule change lead time (RQ-09) | Same day, no release | Demonstrated at checkpoint 1 |
| Agreement with analysts | ≥ 98% over six months shadow | Console report at in-the-loop exit |

## 8. Defined phases of deliverables

| Phase | Deliverables | Due |
|---|---|---|
| Initiate | Signed contract; project charter | Jan 2027 |
| Select | Product selected against ARS-2026-01; procurement complete | Apr 2027 |
| Design | Solution design; threat model; IF-02 in the Interface catalog; **checkpoint 1** | Jun 2027 |
| Build and shadow | Engine hosted; shadow scoring alongside the batch | Aug 2027 |
| Pre-go-live | Load and failover tests; **checkpoint 2**; Compliance Assessment | Oct 2027 |
| Release | Scoring before authorisation; analysts in the loop | Nov 2027 |
| Close | Hypercare; lessons learned; Transition 2 declared | Dec 2027 |

## 9. Prioritized joint workplan

1. Confirm the 150 ms budget with the Card Switch vendor (blocks everything). 2. Procurement. 3. Platform hosting on P1's environments. 4. Kafka feed. 5. Console for analysts. 6. Rule administration. 7. Switch change. 8. Shadow period. 9. Cut-over.

## 10. Time windows

Design checkpoint by 30 June 2027; go-live between 1 and 30 November 2027 (after the card re-issue settles, before the December peak); no changes 15 December – 5 January (Cards Operations freeze).

## 11. Architecture delivery and business metrics

Delivery: checkpoints passed first time; open conditions; Change Requests raised. Business: SM-03 fraud loss per 1,000 cards, baseline index 100, target ≤ 70 within twelve months of go-live; SM-04 seconds to block.

**Signed:** L. Okafor, Chief Architect · A. Shah, Retail IT and the vendor's lead architect · P. Nandakumar, sponsor · 20 January 2027
