---
title: Architecture Definition Document v0.3 — Technology Architecture chapter, consolidated gaps and impact
deliverable: Architecture Definition Document (draft)
phase: D
kind: DELIVERABLE
summary: The Phase D chapter plus the two cross-domain chapters Phase D can now fill — consolidated gap analysis and impact assessment — leaving only the Transition Architecture chapter for Phase E.
refs: ["CONTENT §4.2.3", "ADM §8.4", "ADM §8.3"]
source: authored
status: draft
---

> **What to notice.** Phase D is the only development phase whose external inputs include *product information on candidate products*, because platform choices are made here. Its steps are the same nine as B and C. After Phase D the Definition Document has every domain chapter, so the consolidated gap analysis (chapter 8) and impact assessment (chapter 9) are written now; the Transition Architecture chapter (10) waits for Phase E. This version also carries the technology constraints the Requirements Specification v0.3 gained.

| | |
|---|---|
| Reference | ADD-2026-01, version 0.3 (Phase D), 31 July 2026 |
| Chapter owner | Owen Price, technology architect; security section reviewed externally (Risk budget) |

## Chapter 5d — Technology Architecture models

### Baseline Technology Architecture

- **Technology Portfolio catalog**: PostgreSQL 16.2 (Core Banking, Card Switch); OpenJDK 21 (both); Apache Kafka 3.7 (Card Switch events); Oracle 11g (Data Warehouse — non-standard, retire); RHEL 9.3 on all servers; Dell PowerEdge R760 in the primary data centre.
- **Technology Standards catalog**: the above as *adopted*; Oracle 11g *retire*; no API gateway, container platform or secrets-management standard exists.
- **Environments and Locations diagram**: Primary data centre (Head Office) and DR data centre (Operations Centre), both in-country; environments *dev, test, prod* for Core Banking; the Mobile App is built and tested on developer machines only.
- **Networked Computing/Hardware diagram**: channels reach Core Banking over the internal network through a single load balancer; card network link terminates at the Card Switch in the primary data centre only — DR failover of authorisation is manual (a finding against RQ-08).

### Target Technology Architecture

- **Platform Decomposition diagram**: presentation (app stores, counter workstation); API layer (API gateway product, two nodes per data centre); services (Identity Verification — vendor-hosted in-country; Fraud Engine — bank-hosted containers); systems of record (Core Banking, Card Switch, unchanged); integration (Kafka for card events feeding the engine's feature store); management (monitoring, secrets management — new standards).
- **Technology Standards catalog, additions**: API gateway product (*adopted*, selected under PR-03); container platform on RHEL 9 (*adopted*); secrets manager (*adopted*, PR-04); OAuth 2.1 (*adopted*); Oracle 11g stays *retire*.
- **Environments and Locations, target**: dev, test, pre-prod, prod for the API layer and engines; the card network link is dual-homed to both data centres so authorisation and scoring fail over within the 2-hour level (RQ-08); vendor verification service reached over a private link from both centres.
- **Networked Computing/Hardware, target**: latency budget for IF-02 scoring — 150 ms total, of which 40 ms network, 90 ms engine, 20 ms Switch mapping (RQ-18); Fraud Engine sized at 300 transactions per second with headroom for the re-issue peak.
- **Technology principles review (step 1)**: PR-04 security by design applied — threat models done for the API layer and the scoring call; no shared credentials (secrets manager); PR-03 buy applied to the gateway.
- **Product information considered**: three API gateway products and two container platforms assessed against the standards; the selection is recorded as a *logical* building block here and a *solution* choice in Phase E.

### Technology gap analysis

| Gap | Type | Roadmap component |
|---|---|---|
| No API gateway, container platform or secrets management | New | RC-D1 Platform build (part of WP-1) |
| Card network link single-homed; manual DR failover | Changed | RC-D2 Dual-home the network link before WP-4 (must precede scoring) |
| No pre-prod environment | New | RC-D3 Pre-prod for the API layer and app |
| Oracle 11g warehouse | Retire (next cycle) | none in this cycle — constraint only |

## Chapter 8 — Gap analysis (consolidated across domains)

| Domain | Gap | Potential solution | Dependencies |
|---|---|---|---|
| Business | Identity verification is a person with paper | Identity Verification service; teller retraining | Compliance procedure (RC-B2) |
| Business | Fraud blocking is a morning task | Real-time screening; analyst-in-the-loop for six months | Cards Operations readiness (R-1) |
| Data | No controlled evidence store; journey state not shareable | Evidence in the verification service (30-day); journey token in the API layer | API layer first |
| Application | No service layer; app cannot act | API layer; Mobile App v4 | Platform team; Core Banking v12 done |
| Application | No scoring or verification applications | Buy both | Procurement; ARS as input |
| Technology | No gateway/container/secrets platform; single-homed card link; no pre-prod | Platform build; dual-homing; pre-prod | Data-centre change window |

Every row is carried into Phase E's Consolidated Gaps, Solutions and Dependencies matrix in the Architecture Roadmap.

## Chapter 9 — Impact assessment

| Area | Impact of the Target Architecture |
|---|---|
| Existing projects | Core Banking v12 upgrade: no change to scope, but its REST API becomes a dependency (AS-02 confirmed). Branch closure programme: teller retraining sequenced with it. |
| Organisation | Digital Platform team (new, 4); Rule Tuner role in Cards Operations; Data Warehouse team loses the fraud batch; Compliance gains evidence-retention monitoring. |
| Other architectures | Lending (next cycle) inherits the API layer and verification service; the Data Warehouse replacement must not assume the fraud feed. |
| Operations | Two new 24×7 services (API layer, Fraud Engine); vendor-run verification; DR test scope grows. |
| Cost | Run cost +£640k a year from Transition 2 (engines, gateway licences, platform team); offset estimates in the Phase F business case. |
| Risk | Scoring timeout policy (authorise and flag) means a Fraud Engine outage degrades to today's behaviour, not to declined cards. |

## Chapter 10 — Transition Architecture: placeholder for Phase E
