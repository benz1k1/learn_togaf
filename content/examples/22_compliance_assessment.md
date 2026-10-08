---
title: Compliance Assessment — Project P5, checkpoint 1 (design)
deliverable: Compliance Assessment
phase: G
kind: ASSESSMENT
summary: The design-stage architecture compliance review of the fraud scoring project — progress, the design as presented, and the completed checklists with a conditional pass and three conditions.
refs: ["CONTENT §4.2.13", "GOV §6", "ADM §11.3"]
source: authored
status: draft
---

> **What to notice.** Compliance reviews are periodic, happen *during implementation* (Phase G), and check that design and build stay in line with the architecture and the Vision, feeding learnings back. The contents list is three things: project progress and status, the project's architecture/design, and the completed checklists — the standard names eight checklist areas. The result is a Phase G output and a Phase H input, so it is written to be read later, not just filed.

| | |
|---|---|
| Reference | CA-P5-01, 24 June 2027 |
| Project | P5 Fraud Scoring (contract AC-2027-05) |
| Checkpoint | 1 — design sign-off |
| Reviewer | Owen Price (independent of the project) |
| Result | **Conditional pass** — three conditions to close before checkpoint 2 |

## 1. Overview of project progress and status

| | |
|---|---|
| Stage | Design complete; product selected 14 April 2027 (in-country hosted, bank-run containers) |
| Schedule | On plan for shadow scoring in August; checkpoint 1 held on the contracted date |
| Budget | £1.9m capital, £120k spent; vendor licence signed |
| Open risks | R-1 analyst acceptance (console demo went well; unchanged); 150 ms budget confirmed with the Card Switch vendor on 3 May |
| Change Requests | None raised. One deviation found in this review (see condition C-2) should have been a Change Request |

## 2. Overview of project architecture / design

The Fraud Engine runs on Platform Services in both data centres; the Card Switch calls it synchronously on IF-02 with a 150 ms budget and *authorise-and-flag* on timeout; card events arrive on Kafka to compute features; analysts use the vendor console for review and blocking; rules and thresholds are configuration in the console, owned by Cards Operations. Fraud Score data is stewarded by the Cards Ops Lead (PR-01). The design traces every Must requirement in the contract (RQ-02, RQ-04, RQ-09, RQ-18) to a component and a test.

**Deviation found.** The design stores a 90-day copy of transaction data inside the engine for model retraining. This is a *derived* store, so CN-03 (no new customer data store) is arguably not breached, but transaction records include the customer id, and the Definition Document (chapter 5b) allows the engine "derived data only". Not raised as a Change Request.

## 3. Completed architecture checklists

| Checklist | Result | Notes |
|---|---|---|
| Hardware and operating system | Green | RHEL 9.3 containers; sized at 300 tx/s with 40% headroom; both data centres |
| Software services and middleware | Green | Kafka 3.7 feed; gateway not in the scoring path (correct — latency) |
| Applications | Amber | Retraining store — condition C-2 |
| Information management | Amber | Steward named; retention of the retraining store undefined — condition C-2; score history 13 months, agreed |
| Security | Amber | Threat model complete; secrets in the secrets manager; console authentication via bank single sign-on; **vendor support access path not yet documented** — condition C-1 |
| System management | Green | Monitoring of p99 latency, availability and timeout rate to the platform team; alert thresholds set |
| System engineering | Green | Failover tested in design review; pre-prod plan agreed with P3 |
| Methods and tools | Amber | IF-02 not yet registered in the Interface catalog (RQ-07) — condition C-3 |

## Conditions

| Id | Condition | Owner | Due |
|---|---|---|---|
| C-1 | Document and threat-model the vendor support access path; no standing vendor credentials | Solution architect | Before build starts, 15 July 2027 |
| C-2 | Either pseudonymise the customer id in the retraining store and set a 90-day purge, or raise a Change Request for a new data store | Solution architect with the data steward | Design change by 15 July, or Change Request within five days |
| C-3 | Register IF-02 in the Interface catalog with the ISO 8583 field mapping | Project EA member | 1 July 2027 |

## Learnings fed back (to Phase H)

- The Definition Document's phrase "derived data only" was not precise enough to be checked; propose a definition in the Architecture Metamodel.
- Vendor products bring support-access paths the threat-model template does not ask about; add a question.

**Decision recorded in the Governance Log:** conditional pass, AB-2027-08 noted.
