---
title: Change Request — Retraining data store for the Fraud Engine
deliverable: Change Request
phase: G
kind: DELIVERABLE
summary: The change the compliance review forced project P5 to raise, with its impact assessment in the standard's form and the decision the Chief Architect took under the small-change route.
refs: ["CONTENT §4.2.11", "ADM §11.3", "ADM §12.2"]
source: authored
status: draft
---

> **What to notice.** Change Requests come from implementation projects that cannot follow the architecture or need more scope, or from outside events; they are outputs of Phases F, G and H and inputs to Phase H, where they are classified (simplification, incremental, re-architecting). The contents list — description, rationale, impact assessment with six sub-items, repository reference — is followed exactly; the impact-assessment sub-items are the same ones a Requirements Impact Assessment carries.

| | |
|---|---|
| Reference | CR-2027-03 |
| Raised by | Anil Shah, solution architect, Project P5 — 2 July 2027 |
| Trigger | Compliance Assessment CA-P5-01 condition C-2 |
| Route | Under £50k and ten days: Chief Architect with sponsor, per the Statement of Architecture Work §5 |

## 1. Description of the proposed change

Allow the Fraud Engine to hold a 90-day store of card transaction records for retraining its scoring models, with the customer id replaced by a one-way token and an automatic purge after 90 days. Amend the Data Architecture (Definition Document chapter 5b) to add a data entity *Retraining Sample* owned by Cards Operations, and add requirement RQ-25 (pseudonymised, 90-day retention) to the Requirements Specification.

## 2. Rationale for the proposed change

The selected product retrains monthly on recent transactions; without the store, models drift and the vendor estimates a 30% loss of detection accuracy within a year, which would put SM-03 (30% lower losses) at risk. Pseudonymisation and purge keep principle PR-02 (one customer record) and constraint CN-03 (no new customer data store) intact in substance: the store cannot identify a customer and is not a system of record for anything.

## 3. Impact assessment of the proposed change

| Item | Assessment |
|---|---|
| Reference to specific requirements | RQ-06-style retention applied to a new entity; CN-03; PR-01, PR-02; new RQ-25. SM-03 depends on this change |
| Stakeholder priority of the requirements to date | Compliance Officer: CN-03 *Must*, satisfied by pseudonymisation (confirmed 6 July). Cards Ops Lead: retraining is *Must* for SM-03. Data steward: agrees if purge is automatic and audited |
| Phases to be revisited | C (Data Architecture, one entity and the dissemination diagram); none of B, D, E, F — no roadmap, cost or schedule change |
| Phase to lead on requirements prioritisation | Phase C, through the Requirements Management process |
| Results of phase investigations and revised priorities | Data architect reviewed on 8 July: entity added; dissemination diagram updated to show the engine holding *derived and pseudonymised* data; RQ-25 added at *Must*; no other requirement re-prioritised |
| Recommendations on management of requirements | Define "derived data" in the Architecture Metamodel (learning from CA-P5-01); add a retention field to every data entity in the catalog |

Cost: £12k (pseudonymisation configuration, purge job, audit report). Schedule: none; fits before build on 15 July.

## 4. Repository reference number

Governance Log GL-2027-041; Requirements Repository ARCH-25; Definition Document ADD-2026-01 v1.1.

## Decision

**Approved** — Lena Okafor, Chief Architect, and Priya Nandakumar, sponsor, 9 July 2027. Classified for Phase H as an **incremental change** (adds to the architecture without changing its structure); no new cycle. Condition C-2 of CA-P5-01 closed on 15 July on evidence of the configured purge.
