---
title: "SABSA Conceptual layer — risk appetite and security strategy"
deliverable: SABSA Conceptual layer (risk appetite and security strategy)
phase: A
kind: DELIVERABLE
track: SABSA
summary: "The architect's view: the risk appetite statement the Head of Risk signs, the security strategy that answers it, and the Assets, People, Location and Time cells that make the Business Attributes Profile a coherent conceptual architecture."
refs: ["SABSA §3", "GUIDE:integrating-risk-and-security §5", "GUIDE:integrating-risk-and-security §3", "ADM §3"]
artefacts: []
source: authored
status: draft
---

> **What to notice.** The Conceptual layer is where the business's adjectives become an architect's decisions. Its Motivation cell — the risk appetite statement together with the Business Attributes Profile (document 61) — says *how much* of each attribute the bank is willing to lose; its Process cell, the security strategy, says *by what approach* the bank will hold the line. The trap is a risk appetite that is a paragraph of good intentions: "the bank has a low appetite for fraud" cannot be tested against a design. Every appetite line here is a number that the attribute metrics can breach, which is what makes appetite and performance target the same thing seen twice.

| | |
|---|---|
| Reference | SEC-CON-2026-01, version 1.0, 27 March 2026 |
| Signed | Head of Risk (policy authority); noted by the Architecture Board with the Vision, AB-2026-07 |

## Conceptual × Motivation — the risk appetite statement

| Area | Appetite | Attribute breached when exceeded |
|---|---|---|
| Fraud loss | Accept up to index 70 per 1,000 cards after WP-4; no appetite for a scam that a score above threshold could have blocked but did not within 5 s | BA-07 |
| False declines | Accept up to 0.5 % of genuine card transactions declined by scoring — the opportunity side, below the 1.2 % the batch causes today | BA-03, BA-11 |
| Scoring outage | Accept authorise-and-flag for up to 15 minutes per month; beyond that, the Card Switch falls back to the network's stand-in limits | BA-01, BA-07 |
| Customer data disclosure | Zero appetite for a reportable disclosure; zero appetite for customer data leaving the country | BA-04, BA-10 |
| Onboarding error | Accept up to 1 in 2,000 accounts opened on evidence later found false, provided the same rule set ran in every channel | BA-10, BA-06 |
| Service loss | Accept payments unavailability within the 99.9 % level; no appetite for authorisation failover longer than two hours | BA-01, BA-09 |
| Vendor dependence | Accept bought identity verification and fraud engines only if hosted in-country and integrated through the API layer | BA-10, BA-12 |

The Head of Risk owns the statement; a change to any line is a Change Request into Requirements Management, because the targets in document 61 are its mirror.

## Conceptual × Process — the security strategy

Five strategic choices, each answering one appetite line and one business principle:

1. **Score before you authorise, then keep a person in the loop.** Fraud scoring sits in front of authorisation (Safe by default), but analysts confirm blocks for the first six months so the readiness risk R-1 is managed rather than ignored.
2. **One rule set, many channels.** KYC and fraud rules live once, behind the API layer, and are configuration owned by Compliance and Cards Operations, so the audit finding on channel drift cannot recur.
3. **Risk-based authentication, not maximum authentication.** Strong authentication on every payment, step-up only when the score or the amount warrants it, so *Usable* and *Authenticated* both hold.
4. **Nothing new holds the customer.** No new customer data store (CN-03); evidence is held by the verification service and purged within 30 days; caches are non-authoritative and short-lived.
5. **Buy the specialist, own the evidence.** Identity verification and fraud scoring are bought, but logs, keys and the audit trail stay with the bank so assurance never depends on a vendor's word.

## Conceptual × Assets — what is being protected, in the architect's terms

The business assets of the Contextual layer become four asset classes: **Customer identity** (evidence, credentials, device binding), **Money movement** (transfer and authorisation instructions), **Customer record** (Core Banking's master data, cached but never copied) and **Fraud knowledge** (scores, rules, the model). Each carries the attributes it needs most: identity is *Authenticated* and *Confidential*, money movement is *Accurate* and *Timely*, the record is *Accurate* and *Confidential*, fraud knowledge is *Auditable* and *Fraud-resistant*.

## Conceptual × People — roles and the trust the strategy assumes

Customers, tellers, analysts, platform operators, vendors and the card network are the actors; the policy authorities are the Head of Risk (appetite and policy), the Compliance Officer (onboarding rules) and Cards Operations (fraud rules). The strategy assumes the bank trusts its own tellers and analysts once authenticated, trusts vendors only for the service they are contracted for, and trusts the card network for what the network standard defines — assumptions the domain model (document 64) turns into trust relationships.

## Conceptual × Location — the security domain concept

Four zones follow from the strategy: the **customer channel** on untrusted networks, the **bank's core** in two in-country data centres, **bought services** reachable only over private links, and the **card network**. Everything crossing a zone boundary crosses the API layer or the Card Switch — the two places where policy is enforced.

## Conceptual × Time — the lifetimes the strategy sets

Identity evidence ≤ 30 days; audit log 13 months; cache ≤ 15 minutes; analyst-in-the-loop for six months after Transition 2; DR test twice a year; keys rotated annually; the appetite statement reviewed at each phase gate and at the Phase H review.

## In the other frameworks

TOGAF places the risk appetite and security principles in the Preliminary Phase and Phase A (G152 §5.1–5.2) and the strategy in the *Architecture Vision*; ArchiMate draws this layer as a *Strategy view* (Course of Action for each strategic choice, realising Goals) over a *Motivation view* whose Assessments are the appetite lines.

*Source note: SABSA framework as published by the SABSA Institute (open-use with attribution); section numbers refer to the SABSA White Paper and are to be verified against the registered PDF.*
