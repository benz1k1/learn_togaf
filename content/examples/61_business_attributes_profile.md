---
title: "Business Attributes Profile — Digital Channels"
deliverable: Business Attributes Profile
phase: A
kind: PROFILE
track: SABSA
summary: "Twelve business attributes for mobile payments, onboarding and fraud scoring, each traced to a driver and given a metric type, a measurement approach and a performance target — Phase A's requirements written by a security architect."
refs: ["SABSA §3", "GUIDE:integrating-risk-and-security §5", "GUIDE:integrating-risk-and-security §3", "ADM §3"]
artefacts: []
source: authored
status: draft
---

> **What to notice.** The Business Attributes Profile is the Conceptual × Motivation cell and the hinge of the whole Matrix: every driver above it maps down to an attribute, every control below it must trace up to one. An attribute is an adjective the business would use about itself ("available", "accurate"), and it only becomes a requirement when it carries a **metric type**, a **measurement approach** and a **performance target**. The trap is a profile that lists the whole taxonomy: twelve attributes the bank will measure are worth more than sixty it will not. Targets here are the same numbers as the Architecture Requirements Specification, not a second set.

| | |
|---|---|
| Reference | SEC-BAP-2026-01, version 1.0, 27 March 2026 (signed with the Architecture Vision) |
| Owner | Owen Price for the Head of Risk; targets agreed with the Head of Retail and the Cards Ops Lead |
| Scope | Mobile payments (WP-1, WP-3), digital onboarding (WP-2), real-time fraud scoring (WP-4) |

## The profile

| # | Attribute | Family | Business driver traced | Metric type | Measurement approach | Performance target |
|---|---|---|---|---|---|---|
| BA-01 | Available | Operational | Customers expect digital banking; card network never sleeps | Hard | Monthly availability from platform monitoring, per service | Payments API 99.9 %; fraud screening 99.99 %; identity verification 99.5 % 07:00–23:00 |
| BA-02 | Timely | User | Customers expect digital banking | Hard | p95/p99 latency from gateway and engine logs | Transfer ≤ 10 s p95; score ≤ 150 ms p99; identity decision ≤ 60 s for 95 % |
| BA-03 | Usable | User | Cost pressure; ten-minute onboarding goal | Soft | Median minutes per onboarding from Core Banking activation timestamps; app-store rating | ≤ 10 minutes; rating ≥ 4.3 |
| BA-04 | Confidential | Risk management | Safe by default; data protection law | Hard | Confirmed disclosures of customer data per year; encryption coverage audit | Zero reportable disclosures; 100 % of customer data encrypted in transit and at rest |
| BA-05 | Authenticated | Risk management | Rising card fraud; account takeover | Hard | Share of payment sessions with strong customer authentication; takeover incidents per 100 k customers | 100 % of payments strongly authenticated; ≤ 2 takeovers per 100 k per year |
| BA-06 | Accurate | Operational | One bank; new capital rules | Hard | Reconciliation breaks between channels and Core Banking per month | Zero unreconciled transfers; one system of record (CN-01) |
| BA-07 | Fraud-resistant | Risk management | Rising card fraud, 41 % up | Hard | Fraud loss per 1,000 cards (index), seconds from score to block | Index ≤ 70 within 12 months of WP-4; block ≤ 5 s |
| BA-08 | Auditable | Management | Compliance Officer's audit finding on channel rules | Hard | Share of onboarding and payment events with a complete, tamper-evident log entry | 100 %; log retained 13 months |
| BA-09 | Recoverable | Operational | Regulator's DR rule | Hard | Failover time in the twice-yearly DR test | Payments and authorisation restored within 2 hours (RQ-08) |
| BA-10 | Legal / Compliant | Legal and regulatory | KYC, data protection, data residency | Hard | Compliance review findings; evidence retention checks | Same KYC rule set in every channel (RQ-03); evidence purged ≤ 30 days (RQ-06); data in-country (CN-05) |
| BA-11 | Reputable | Business strategy | Head of Retail: "the name is lost first" | Soft | Complaints per 1,000 customers about fraud handling; press incidents | Complaints down 20 % by end 2027; zero press-reported breaches |
| BA-12 | Cost-effective | Business strategy | Run within our means | Hard | Run cost of security services against the +£640 k/yr envelope | Security share ≤ £150 k/yr of that envelope |

Family names follow the SABSA taxonomy's grouping (User, Management, Operational, Risk-management, Legal/Regulatory, Business Strategy); "Fraud-resistant" and "Authenticated" are the bank's own refinements of the taxonomy's *Protected* and *Access-controlled*, which SABSA permits because the profile is meant to be tailored.

## Why this is Phase A's requirements in security terms

The Architecture Vision's mapped requirements say *what the programme must do* (RQ-01 to RQ-04, CN-01 to CN-03). Read again with a risk hat on, each of them is an attribute with a target: RQ-01 is *Timely*, RQ-02 and RQ-04 are *Fraud-resistant*, RQ-03 is *Legal*, CN-01 is *Accurate*, CN-03 is *Confidential* and *Accurate* together. W117's argument is exactly this — the profile is not an extra security document bolted onto Phase A but the same requirements written so that a control can later prove it serves one of them. That is why the profile is signed with the Vision on the same day and why the Requirements Management phase (document 69) treats an attribute and its target as a requirement under change control for the rest of the cycle. When the Requirements Specification adds RQ-10 to RQ-24 in Phases C and D, each new requirement is assigned to an attribute here or the profile grows; a requirement with no attribute is a requirement nobody will measure.

## Conflicts the profile makes visible

*Usable* against *Authenticated*: a ten-minute onboarding and strong authentication pull apart, and the profile records the resolution — step-up authentication is applied by risk, not to every step. *Timely* against *Fraud-resistant*: a 150 ms scoring budget is what keeps the score in front of the authorisation; on timeout the Card Switch authorises and flags, a decision recorded in the risk appetite (document 62), not left to the engineers.

## In the other frameworks

TOGAF's *Architecture Requirements Specification* (document 14) is this table with the attribute column removed; the ArchiMate *Requirements Realization view* and *Goal Realization view* draw the same chain, Driver → Goal → Requirement → realising element, with each attribute as a Requirement whose target is its property.

*Source note: SABSA framework as published by the SABSA Institute (open-use with attribution); section numbers refer to the SABSA White Paper and are to be verified against the registered PDF.*
