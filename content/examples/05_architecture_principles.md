---
title: Architecture Principles — Northgate Bank
deliverable: Architecture Principles
phase: PRELIM
kind: DELIVERABLE
summary: The five principles behind the Principles catalog drawing, in the name/statement/rationale/implications form, with how each was applied in this cycle.
refs: ["CONTENT §4.2.4", "TECH §2", "ADM §2.3"]
source: authored
status: draft
---

> **What to notice.** Each principle has the four parts the ADM Techniques document prescribes: name, statement, rationale, implications. Principles are *established* in the Preliminary Phase, *confirmed and elaborated* in Phase A, and domain principles (data, application, technology) are reviewed at step 1 of Phases B, C and D. Five is deliberate: the guidance warns that too many principles reduce flexibility. The catalog drawing on the Artefacts page shows the same five as an artefact; this is the deliverable that carries them.

| | |
|---|---|
| Version | 1.1, confirmed in Phase A on 24 March 2026 |
| Approved by | Architecture Board minute AB-2026-04; re-affirmed AB-2026-07 |

## PR-01 Data is an asset (data principle)

- **Statement.** Data is owned, valued and managed like any other asset of the bank.
- **Rationale.** Every decision the programme enables — an account opened, a payment released, a card blocked — depends on trusted customer and account data.
- **Implications.** Every data entity in the Data Entity catalog has a named steward. Data quality is measured, and the measure is reported to the steward monthly. Projects budget for data-quality work rather than assuming it.
- **Applied in this cycle.** The Data Entity/Data Component catalog names a steward for Customer, Account, Card and Transaction; the Fraud Engine's scoring data has a steward in Cards Operations.

## PR-02 One customer record (data principle)

- **Statement.** A customer is held once and referenced everywhere.
- **Rationale.** Duplicate records have caused failed KYC checks and mis-sent statements; the regulator noted both in 2025.
- **Implications.** Core Banking is the master for Customer and Account. Channels read, and write only through Core Banking's services. No new customer data store is created; caches are non-authoritative and expire.
- **Applied in this cycle.** Constraint CN-01 in the Requirements catalog. The identity-verification service holds evidence for 30 days and then deletes it; it never becomes a second customer store.

## PR-03 Buy before build (application principle)

- **Statement.** Prefer proven packages over bespoke development.
- **Rationale.** Lower delivery risk and cost; the bank differentiates on customer experience, not on plumbing.
- **Implications.** Build only where the bank differentiates. A build decision needs an Architecture Board waiver with a written reason.
- **Applied in this cycle.** The Mobile App is built (differentiating). The Fraud Engine and identity verification are bought; the API layer is a product with configuration, not code.

## PR-04 Security by design (technology principle)

- **Statement.** Controls are designed in, not bolted on.
- **Rationale.** Card and payment data carry a regulatory duty and a reputational cost the bank cannot insure away.
- **Implications.** Every change has a threat model before design sign-off. No shared credentials between components. Security requirements enter the Architecture Requirements Specification, not a separate annex.
- **Applied in this cycle.** Phase D security architecture reviewed externally; Compliance Assessments carry the security checklist.

## PR-05 Channel independence (application principle)

- **Statement.** Any service works from any channel: branch, mobile, card.
- **Rationale.** Customers switch channels mid-journey; a customer who starts opening an account in the app and finishes at the counter must not start again.
- **Implications.** Services expose one API used by every channel. Channel-specific logic stays in the channel. Business rules live once, behind the API.
- **Applied in this cycle.** The API layer is work package WP-1 and precedes every other work package on the roadmap.

## Conflicts and how they are resolved

PR-03 (buy) and PR-05 (one API for every channel) conflicted on the Mobile App vendor, whose package brought its own customer cache. Resolution recorded in the Governance Log: the cache is allowed as non-authoritative with a 15-minute expiry, which honours PR-02; the package is not adopted for onboarding because its flow could not be re-used at the counter, which is why the app is built.
