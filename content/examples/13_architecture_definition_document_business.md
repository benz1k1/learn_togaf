---
title: Architecture Definition Document v0.1 — Business Architecture chapter
deliverable: Architecture Definition Document (draft)
phase: B
kind: DELIVERABLE
summary: The document's frame plus the Business Architecture chapter as it stands after Phase B — baseline, target, gap analysis and the roadmap components that feed Phase E.
refs: ["CONTENT §4.2.3", "ADM §4.4", "ADM §4.3"]
source: authored
status: draft
---

> **What to notice.** The Architecture Definition Document is the *container* for the core artefacts across all four domains and all states (baseline, transition, target). It is *qualitative* — the intent of the architects — and its companion, the Architecture Requirements Specification, is *quantitative*. Phase A may start it; Phase B "creates or updates" it (step 9); Phase F finalises it. The contents list is followed as chapter headings; Phase B fills the business ones and leaves the rest as placeholders.

| | |
|---|---|
| Reference | ADD-2026-01, version 0.1 (Phase B), 30 April 2026 |
| Owner | Chief Architect; chapter 5 by Rahul Desai, business architect |
| State | Draft, combined B–D gate |

## 1. Scope

The Retail Banking segment as touched by onboarding, payments and card fraud; all four domains; baseline March 2026, target end 2028, transitions Q2 and Q4 2027. Out of scope: Lending, Data Warehouse replacement. (From the Statement of Architecture Work SAW-2026-01.)

## 2. Goals, objectives and constraints

The three SMART objectives of the Business Scenario; constraints CN-01 to CN-03. Full list in the Requirements catalog and the Architecture Requirements Specification.

## 3. Architecture Principles

PR-01 to PR-05, confirmed in Phase A. Business principles reviewed at Phase B step 1: no change; PR-05 (channel independence) is the principle Phase B applies most.

## 4. Baseline Architecture (summary)

Onboarding at the counter, next-day activation; channel-specific integrations; batch fraud scoring. Baseline models are in the Landscape, dated March 2026 and now *verified* by the Phase B workshops.

## 5. Architecture models — Business Architecture

### 5.1 Baseline Business Architecture

- **Organisation** (Organization/Actor catalog): Retail Banking at Head Office runs the Branch Network, Digital Channels and Cards Operations (Operations Centre). Actors: Customer (external), Branch Teller, Loan Officer, Fraud Analyst, Digital product owner.
- **Functions and services** (Business Service/Function catalog): Customer Onboarding {verify identity, open account, issue card}; Payments {transfer funds, authorise card, post transaction, notify}; Risk {score transaction, block card}. Today *verify identity* and *score transaction* are performed by people, next day.
- **Processes** (Process Flow diagram, baseline): *Open account* — 11 steps, 4 hand-offs, 45 minutes plus overnight. *Make a payment* — 6 steps in the channel, then batch.
- **Actor/Role matrix**: Teller performs Onboarder, Cashier and, informally, Identity Checker; Fraud Analyst performs Scorer and Blocker.

### 5.2 Target Business Architecture

- **Value streams** (Value Stream map): *Onboard a customer* — attract → verify → open → issue → activate, target ten minutes with *verify* and *activate* automated. *Make a payment* — initiate → check → screen → authorise → post → notify, target ten seconds end to end.
- **Capabilities** (Business Capability Map, heat overlay): Customer Onboarding and Payments change; Identity Verification and real-time Fraud Screening are *new* sub-capabilities.
- **Functions and services, target**: *Verify identity* becomes an automated service used by both the counter and the app (PR-05). *Score transaction* becomes a synchronous service called before authorisation. *Block card* stays with the Fraud Analyst for six months, then becomes automatic for scores above a threshold the analysts set.
- **Organisation, target**: a Digital Platform team (new, 4 people) owns the API layer; Cards Operations gains a Rule Tuner role; the Teller role loses Identity Checker and gains Assisted Onboarder.
- **Business Footprint diagram**: goal *grow mobile adoption* → Retail Banking → Payments → *transfer funds* service → (Phase C) Mobile App and API layer.

### 5.3 Business Architecture gap analysis

| Baseline element | Target element | Gap | Type |
|---|---|---|---|
| Identity Checker (teller, paper) | Identity Verification service | New capability; no team or product | New |
| Score transaction (overnight, warehouse) | Fraud Screening service (real time) | Timing and location of the function change | Changed |
| Block card (analyst, morning) | Block card (analyst, then automatic) | Role change with a six-month transition | Changed |
| Channel-specific rules | Rules once, behind a service | Function duplicated across channels today | Eliminated |
| Legacy online banking site | — | Retired in 2028 | Eliminated |
| Lending processes | Lending processes | Untouched | Retained |

### 5.4 Candidate roadmap components from Phase B

- **RC-B1** Establish the Digital Platform team before any API work (precondition for WP-1).
- **RC-B2** Define the identity-verification procedure with Compliance before selecting a product (feeds WP-2).
- **RC-B3** Six-month analyst-in-the-loop period for card blocking (a constraint on WP-4's sequence).
- **RC-B4** Teller retraining aligned to the Branch Council's closure programme.

## 6. Rationale and justification for the architectural approach

One shared service layer is chosen over improving each channel separately because the audit finding (rules differ by channel) and the 60% mobile goal both require the counter and the app to run the same function; and because the same layer is what Lending will need next cycle (re-use assessment in chapter 7).

## 7. Mapping to the Architecture Repository

Landscape: Retail segment, states baseline (verified) and target (draft). Reference models: the Core Banking vendor's retail process model, used for the baseline function catalog. Standards: none at business level yet. Re-use: identity verification and the API layer assessed as re-usable by Lending.

## 8. Gap analysis (consolidated) — placeholder until Phase D

## 9. Impact assessment — placeholder until Phase D

## 10. Transition Architecture — placeholder until Phase E

## Chapters for Phase C and D — placeholders: Data Architecture models, Application Architecture models, Technology Architecture models
