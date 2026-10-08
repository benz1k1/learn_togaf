---
title: "Security services catalogue — Digital Channels"
deliverable: Security services catalogue
phase: C
kind: DELIVERABLE
track: SABSA
summary: "The Logical-layer security services — authentication, authorisation, confidentiality, integrity, non-repudiation, audit, availability, fraud detection and evidence handling — each traced up to the attributes it serves and across to the processes and applications that consume it."
refs: ["SABSA §5", "GUIDE:integrating-risk-and-security §5", "GUIDE:integrating-risk-and-security §3", "ADM §6"]
artefacts: []
source: authored
status: draft
---

> **What to notice.** A security service is a *logical* thing: "authenticate a customer" says what is provided, to whom and at what level, and says nothing about passwords, tokens or products. That silence is deliberate — the same service is realised by different mechanisms in the app and at the counter (document 66), and if the catalogue named the mechanism the trace from attribute to control would break at the first product change. The trap is a catalogue copied from a standard's control list: every service here exists because a row in the Business Attributes Profile or the risk assessment needs it, and the two trace columns prove that.

| | |
|---|---|
| Reference | SEC-SVC-2026-01, version 1.0, 12 June 2026 (Phase C); mechanisms in SEC-MECH-2026-01 |
| Owner | Owen Price; consumers confirmed with the application architects for WP-1 to WP-4 |

## The catalogue

| Id | Service | What it provides | Level | Attributes served | Consumed by (process / application) | Risk rows |
|---|---|---|---|---|---|---|
| SS-01 | Customer authentication | Establishes that the person in a channel is the account holder; risk-based step-up for high-value or unusual actions | Strong for every payment; step-up on new payee, amount above £1,000 or device change | BA-05 Authenticated, BA-03 Usable | Pay (Mobile App, online site); Open account (Mobile App, counter); Channel API layer as enforcement point | T-01 |
| SS-02 | Staff and service authentication | Identifies tellers, analysts, operators and calling services | Single sign-on for people; mutual authentication for services | BA-05, BA-08 Auditable | Counter onboarding; analyst console; IF-01, IF-02, IF-03 | T-08 |
| SS-03 | Authorisation | Decides what an authenticated party may do; enforces rule ownership (Cards Ops on fraud rules, Compliance on KYC rules) | Role-based for staff; scope-based for channels and services | BA-08, BA-10 Legal | Every API operation; console block versus rule edit; rule administration | T-01, T-08 |
| SS-04 | Confidentiality | Keeps customer identity, evidence and account data readable only by authorised parties, in transit, at rest and in caches | All customer data; in-country only | BA-04 Confidential, BA-10 | All channels; API layer cache; Identity Verification; Fraud Engine feature store | T-04, T-06, T-08 |
| SS-05 | Integrity | Ensures a transfer or authorisation executes once, unchanged, against the record | Idempotent money movement; signed messages on the card link | BA-06 Accurate | Transfer funds (IF-01); card authorisation (ISO 8583) | T-03 |
| SS-06 | Non-repudiation | Binds a payment instruction to the customer who gave it so neither side can deny it later | Every transfer and card control change | BA-08, BA-11 Reputable | Pay; card controls; dispute handling in Cards Operations | T-01 |
| SS-07 | Audit and logging | Records every security-relevant event tamper-evidently, attributable to a party, retained 13 months | 100 % of onboarding, payment, scoring and console events | BA-08 Auditable | All applications; Compliance reviews; Phase G assurance | T-01, T-05, T-08 |
| SS-08 | Availability and continuity | Keeps payments, authorisation and scoring running through component and site loss | 99.9 % / 99.99 % / 99.5 %; two-hour failover | BA-01 Available, BA-09 Recoverable | Payments API; Card Switch; Fraud Engine; Identity Verification | T-02, T-07 |
| SS-09 | Fraud detection and response | Scores every card transaction and app transfer before it completes; blocks, flags or steps up; feeds confirmed cases back to rules | Score ≤ 150 ms p99; block ≤ 5 s; analyst in the loop six months | BA-07 Fraud-resistant, BA-02 Timely | Card authorisation (IF-02); Pay; analyst console; rule administration | T-01, T-05, O-02 |
| SS-10 | Identity proofing and evidence handling | Verifies a new customer's documents and liveness; holds evidence only in the verification service and purges it within 30 days | Decision ≤ 60 s for 95 %; same rule set per channel | BA-10 Legal, BA-03 Usable, BA-04 | Open account (Mobile App, counter); IF-03 | T-05, T-06, O-03 |
| SS-11 | Key and secret management | Generates, stores and rotates the keys and credentials every other service relies on | Bank-held keys; annual rotation; no standing vendor credentials | BA-04, BA-08 | Platform services; every service above | T-08 |
| SS-12 | Security monitoring | Correlates events from SS-07 and the platform to detect attack and misuse in near real time | Alert within 15 minutes of a defined pattern | BA-07, BA-01, BA-11 | Platform team; Cards Operations; incident process | T-01, T-02, T-05 |

## Reading the trace columns

Top-down: BA-05 *Authenticated* is served by SS-01, SS-02 and SS-11, so a change to the authentication target (say, step-up on every payment) is scoped in three rows, not discovered in a product's settings. Bottom-up: SS-12 security monitoring serves three attributes and four risk rows, which is the argument for funding it in Transition 1 even though no single requirement asked for it by name. Every service has at least one attribute and at least one consumer; a service with neither was removed during review (an early "data loss prevention" row had no consumer in this programme and was struck out rather than left as aspiration).

## Information assets and their classification

Phase C also fills Logical × Assets: the four asset classes of document 62 are classified so SS-04 knows what it protects. **Customer identity** and **evidence** are *Confidential — customer*, in-country, evidence ≤ 30 days; **money movement** is *Confidential — customer* with *Accurate* dominant; **customer record** is *Confidential — customer*, Core Banking only, caches ≤ 15 minutes; **fraud knowledge** is *Confidential — bank*, because the rules and thresholds are what an attacker most wants to read. Scores retained 13 months; the retraining store is pseudonymised (CR-2027-03).

## In the other frameworks

TOGAF Phase C holds this as the Security Services Catalog and the security classification of G152 §5.4, sitting beside the *Application Portfolio catalog* and the *Data Entity/Data Component catalog*; ArchiMate draws each service as an *Application Service* (or Business Service for SS-10's proofing) in an *Application Usage view*, served to the business processes that consume it, with the attribute as the Requirement it realises.

*Source note: SABSA framework as published by the SABSA Institute (open-use with attribution); section numbers refer to the SABSA White Paper and are to be verified against the registered PDF.*
