---
title: Architecture Building Blocks — the Digital Channels set
deliverable: Architecture Building Blocks
phase: D
kind: DELIVERABLE
summary: The re-usable, vendor-neutral building blocks Phases B–D defined, each with the capability it delivers, its interfaces and the requirements it satisfies, before any product is chosen.
refs: ["CONTENT §4.2.1", "CONTENT §5", "ADM §8.3"]
source: authored
status: draft
---

> **What to notice.** An Architecture Building Block (ABB) describes *what* capability is required and the interfaces it exposes, independent of any product; a Solution Building Block (SBB) is the product or component that *implements* it. ABBs are outputs of Phases B, C, D (and F, H); they live in the Architecture Repository and are what the roadmap and the Solution Building Blocks in Phase G point back at. A good ABB has a name, the capability, the interfaces, the requirements it meets and the other blocks it depends on.

| | |
|---|---|
| Location | Architecture Repository › Architecture Landscape › Digital Channels segment › Building blocks |
| Version | after Phase D, 31 July 2026 |

## ABB-01 Channel API Layer

| | |
|---|---|
| Capability | One entry point for every channel to every business service; routing, authentication, rate limiting, journey-state token |
| Interfaces exposed | Payments API, Onboarding API, Card Management API, Notification API — all OpenAPI 3, OAuth 2.1 |
| Interfaces used | IF-01 Core Banking REST; IF-03 Identity Verification; Card Switch card-status API |
| Requirements met | RQ-01, RQ-03, RQ-05, RQ-07; principles PR-02 (no write-back from caches), PR-05 |
| Depends on | ABB-06 Platform Services |
| Realised by | SBB-01 (API gateway product, Phase E/G) |
| Re-use | Lending, next cycle |

## ABB-02 Identity Verification Service

| | |
|---|---|
| Capability | Verify a person against a passport or driving licence with liveness check; return a decision and reasons; retain evidence ≤ 30 days |
| Interfaces exposed | Verify (asynchronous, callback), Evidence purge |
| Interfaces used | none inside the bank; document-authority services externally |
| Requirements met | RQ-03, RQ-06, SM-01; constraint CN-05 (in-country hosting) |
| Depends on | ABB-01 for every consumer |
| Realised by | SBB-02 (bought, vendor-hosted) |

## ABB-03 Fraud Screening Service

| | |
|---|---|
| Capability | Score a card transaction synchronously before authorisation; compute features in real time from card events; expose rule tuning to Cards Operations |
| Interfaces exposed | Score (synchronous, 150 ms budget), Rule administration, Score history |
| Interfaces used | Kafka card-event stream from ABB-05 |
| Requirements met | RQ-02, RQ-04, RQ-09, RQ-18, SM-03, SM-04 |
| Depends on | ABB-06; dual-homed card network link (RC-D2) |
| Realised by | SBB-03 (bought, bank-hosted containers) |

## ABB-04 Mobile Banking Application

| | |
|---|---|
| Capability | Customer self-service: onboarding, transfers, card management, notifications; native on both platforms |
| Interfaces used | ABB-01 only |
| Requirements met | RQ-01, RQ-05, SM-02 |
| Note | The one *built* block (PR-03 exception recorded in the Governance Log) |
| Realised by | SBB-04 Mobile App v4 |

## ABB-05 Card Authorisation (existing)

| | |
|---|---|
| Capability | Authorise card transactions against the card network; publish card events; block a card |
| Change | Calls ABB-03 before answering the network; timeout policy *authorise and flag* |
| Realised by | the existing Card Switch (SBB-05, vendor change request) |

## ABB-06 Platform Services

| | |
|---|---|
| Capability | Container runtime, secrets management, monitoring, deployment pipeline for ABB-01 and ABB-03 in both data centres |
| Requirements met | RQ-08, PR-04 |
| Realised by | SBB-06 (container platform on RHEL 9, secrets manager) |

## ABB-07 Core Banking Services (existing, unchanged)

Customer, Account and Transaction posting as the system of record (CN-01). Consumed through IF-01 only.

## Building-block dependency order

ABB-06 → ABB-01 → {ABB-04 payments, ABB-02, ABB-03}; ABB-05's change waits for ABB-03 and RC-D2. This order is what the Architecture Roadmap sequences into work packages.
