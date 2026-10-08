---
title: Architecture Definition Document v0.2 — Data and Application Architecture chapters
deliverable: Architecture Definition Document (draft)
phase: C
kind: DELIVERABLE
summary: The Phase C chapters — data entities and their owners, the application portfolio and interfaces, baseline and target, with the gaps and roadmap components each part of Phase C produced.
refs: ["CONTENT §4.2.3", "ADM §6.4", "ADM §7.4", "ADM §5"]
source: authored
status: draft
---

> **What to notice.** Phase C is *one* phase in two parts — Data and Application — described in two chapters of the ADM. Either order is allowed; Northgate did Data first because "no new customer data store" is the constraint most likely to be broken by an application choice. Each part reviews its own principles at step 1 and adds constraints on the Technology Architecture to the Requirements Specification. The identity-verification "buy or build" question left open in the Vision is answered here.

| | |
|---|---|
| Reference | ADD-2026-01, version 0.2 (Phase C), 30 June 2026 |
| Chapter owners | Data: Fatima Al-Sayed; Application: Mei Chen |

## Chapter 5b — Data Architecture models

### Baseline Data Architecture

- **Data Entity/Data Component catalog**: Customer, Account, Card, Transaction — all mastered in Core Banking; Card lifecycle events duplicated in the Card Switch; fraud features derived overnight in the Data Warehouse; identity evidence on paper in branch files (retention uncontrolled — audit finding).
- **Data Entity/Business Function matrix**: *Open account* creates Customer and Account; *Authorise card* reads Card and creates Transaction; *Score transaction* reads Transaction (a day late).
- **Conceptual Data diagram**: Customer 1–n Account 1–n Card; Card 1–n Transaction.

### Target Data Architecture

- **Ownership** (PR-01): Customer and Account — Retail Banking data steward; Card and Transaction — Cards Operations; Identity Evidence — Compliance; Fraud Score — Cards Operations.
- **Logical Data diagram**, additions: *Identity Evidence* (document images, liveness result, decision, expiry ≤ 30 days — RQ-06) held only in the Identity Verification service; *Fraud Score* (transaction ref, score, reasons, threshold version) held in the Fraud Engine; *Onboarding Journey* (saved state token, channel, step) held in the API layer with a 24-hour expiry so a journey can move between counter and app (RQ-05).
- **Data Dissemination diagram**: Core Banking remains the only master of Customer and Account (CN-01, CN-03). The Mobile App's cache and the API layer's journey state are non-authoritative and expire. The Fraud Engine keeps *derived* data only; the Data Warehouse stops receiving the fraud feed at Transition 2.
- **Data principles review (step 1)**: PR-01 and PR-02 unchanged; a third data principle was proposed ("minimise personal data") and folded into RQ-06 rather than added, to keep the set at five.

### Data gap analysis

| Gap | Type | Roadmap component |
|---|---|---|
| No controlled store for identity evidence | New | RC-C1 Identity Verification service holds evidence with 30-day retention |
| Fraud features computed overnight | Changed | RC-C2 Real-time feature computation inside the Fraud Engine |
| Journey state not shareable across channels | New | RC-C3 Journey-state token in the API layer |
| Paper evidence in branch files | Eliminated | RC-C4 Branch file destruction after WP-2 go-live, with Compliance sign-off |

Constraint added for Phase D: CN-05 customer data in-country applies to the engine and verification vendors' hosting.

## Chapter 5c — Application Architecture models

### Baseline Application Architecture

- **Application Portfolio catalog**: Core Banking (package, retain, v12 to 2029); Mobile App v3 (bespoke, balances only); Card Switch (package, retain); Data Warehouse (Oracle 11g, tolerate, replace 2028); legacy online banking site (retire 2028); SMS gateway.
- **Interface catalog**: eleven point-to-point interfaces, each channel to Core Banking directly; Card Switch to card network (ISO 8583); warehouse batch feeds.
- **Application/Organization matrix**: every unit uses Core Banking directly; Cards Operations uses the Card Switch console and warehouse reports.

### Target Application Architecture

- **Application Portfolio, target**: Mobile App v4 (invest: payments, onboarding); **API layer** (new, product); **Identity Verification service** (new, *bought* — see decision); **Fraud Engine** (new, bought, logical component "Fraud Scoring" to be selected in Phase E); Core Banking, Card Switch unchanged; SMS gateway *removed*, replaced by the API layer's notification service.
- **Application Communication diagram**: channels → API layer → Core Banking / Identity Verification; Card Switch → Fraud Engine (synchronous, IF-02) → Card Switch; API layer → notification. No channel talks to Core Banking directly after Transition 1.
- **Application Interaction matrix**: 6 interfaces replace 11.
- **Application Use-Case diagram**: Customer {open account, send transfer, manage card}; Teller {assist onboarding}; Fraud Analyst {review score, block card, tune rules}.
- **Application principles review (step 1)**: PR-03 (buy before build) and PR-05 (channel independence) applied; conflict on the app vendor's cache resolved in the Preliminary Phase decision.

### Decision recorded: identity verification — buy

Options assessed against PR-03, RQ-06, CN-05 and AS-03: (a) build on the Core Banking vendor's KYC module — fails the 60-second level and cannot serve the app; (b) build in-house — no skills, fails PR-03; (c) buy an in-country hosted verification product — meets all four. **Decision: buy** (Architecture Board AB-2026-11). Product selection is Phase E/procurement; the *logical* building block is fixed here.

### Application gap analysis

| Gap | Type | Roadmap component |
|---|---|---|
| No service layer; 11 point-to-point interfaces | New / Eliminated | RC-C5 API layer (WP-1) |
| App cannot pay or onboard | Changed | RC-C6 Mobile App v4 (WP-3, WP-2) |
| No identity verification application | New | RC-C7 Buy verification service (WP-2) |
| No real-time scoring application | New | RC-C8 Buy fraud engine (WP-4) |
| SMS gateway | Eliminated | RC-C9 Retire at Transition 1 |

Constraints added for Phase D: scoring round trip ≤ 150 ms (RQ-18); API gateway per environment; DR failover within 2 hours for the API layer as well as Core Banking.

## Impact on other chapters

Chapter 7 (repository mapping): the API-layer pattern from the Reference Library is adopted. Chapter 9 (impact): the Data Warehouse team loses the fraud batch at Transition 2; the online banking site's interfaces are retired.
