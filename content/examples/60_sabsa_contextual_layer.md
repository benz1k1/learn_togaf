---
title: "SABSA Contextual layer — Northgate Bank, the business view"
deliverable: SABSA Contextual layer (the business view)
phase: PRELIM
kind: DELIVERABLE
track: SABSA
summary: "The six Contextual cells filled for Northgate Bank: what the bank is, why it must change, how it works, who decides, where it operates and when it must be done — in the business's own words, before any security word is used."
refs: ["SABSA §2", "GUIDE:integrating-risk-and-security §5", "GUIDE:integrating-risk-and-security §3", "ADM §2"]
artefacts: []
source: authored
status: draft
---

> **What to notice.** The Contextual layer is the *business's* view of itself, not the architect's. Every cell is written in the language of the Retail Strategy and the Request for Architecture Work, and none of them says "encrypt", "firewall" or "control". The trap it guards against is starting SABSA one row too low: a security architect who begins at the Conceptual layer invents attributes nobody asked for and can never trace them upward. Fill this row first, from documents the business already signed, and the Business Attributes Profile of Phase A (document 61) has something real to hang from.

| | |
|---|---|
| Reference | SEC-CTX-2026-01, version 1.0, 12 February 2026 |
| Prepared by | Owen Price (technology architect, security architecture with Risk) with the Strategy Office |
| Sources | Retail Strategy 2026–2028 "Digital First"; Request for Architecture Work RAW-2026-01; Business Principles, Goals and Drivers extract |

## Contextual × Assets — what the business is

Northgate Bank is a mid-sized retail bank: current and savings accounts, debit and credit cards, small-business lending, served through 140 branches, a Mobile App that can "show but not do", an online banking site and a telephone centre. The assets the Digital Channels programme touches, in business terms, are **the customer relationship** (1.9 million customers, of whom 22 % use the app for transfers), **the customer's money and the bank's licence to move it**, **the record of the customer** held once in Core Banking, and **the bank's name** — the thing the Head of Retail says is lost first when a scam succeeds. Regulatory reporting data is an asset the programme must not disturb (constraint, next cycle).

## Contextual × Motivation — business drivers and risk drivers

| Business driver (from the strategy) | Risk driver (the two-sided reading) |
|---|---|
| Customers expect digital banking — 68 % of new-to-bank under-30s chose a competitor that opens accounts in the app | *Opportunity*: growth and cost to serve. *Threat*: a faster onboarding that verifies identity worse than a teller does |
| Rising card fraud — losses up 41 % year on year, 70 % real-time scams the overnight batch cannot stop | *Threat*: financial loss and reputation. *Opportunity*: a scoring engine that also cuts false declines, which cost sales today |
| Cost pressure — cost-to-income 62 % against a peer median of 55 % | *Opportunity*: halve counter time on onboarding. *Threat*: cutting the human check that catches impersonation |
| New capital rules — one reconciled data source by 2028 | *Threat*: any new customer data store breaks reconciliation (CN-03) |
| Safe by default (business principle) — the bank never trades security for speed | The principle that decides every trade-off below this row |

The business's own goals become the targets of the attributes in document 61: 60 % of transfers in the Mobile App by 31 December 2027; fraud losses cut 30 % within twelve months of scoring; ten-minute onboarding.

## Contextual × Process — how the business works

The value chain is *attract → onboarding → payments → lending → service and retain*, supported by risk and compliance. Three processes change: **opening an account** (today 45 minutes at a counter, verified by a person, activated overnight), **paying** (today a transfer in the app is really an instruction the branch executes), and **stopping fraud** (today a batch in the Data Warehouse and an analyst the next morning, about fourteen hours after the transaction). Business Scenario BS-2026-01, *Opening an account and paying from the phone*, is the process description this layer points to rather than repeats.

## Contextual × People — stakeholders and policy authorities

| Who | Role in the business | Security-relevant authority |
|---|---|---|
| Head of Retail (P. Nandakumar) | Sponsor; owns the customer relationship | Accepts residual risk on customer-facing journeys |
| Head of Risk | Second line; sits on the Architecture Board | **Policy authority** for the bank's risk appetite and security policy |
| Compliance Officer | KYC, anti-money-laundering, data protection | Policy authority for onboarding rules; owns the regulator relationship |
| Head of Cards Operations and the Cards Ops Lead | Own the fraud rules and the analysts | Policy authority for what a fraud rule says; the architecture may change how rules run, not what they say |
| CIO | Runs technology; chairs the Architecture Board | Accountable for technology control operation |
| Branch Council and tellers | Perform onboarding today | Consulted before any counter process changes |
| Customers, the card network, the regulator | External parties the bank must satisfy | Set the rules the bank cannot negotiate (ISO 8583, DR within two hours, data in-country) |

Owen Price is named in the Organizational Model for EA as the architect who carries security architecture with Risk; the Head of Risk, not the architect, is the authority whose policy the later layers implement.

## Contextual × Location — where the business operates

One country, one regulator. Head Office (primary data centre) and the Operations Centre (DR data centre), both in-country, which is where CN-05 "customer data stays in-country" comes from. 140 branches on the bank's network; customers on the public internet and mobile networks; the card network reached over a single-homed link today; identity verification and fraud scoring will be bought and may be vendor-hosted, so "in-country" must be written into the purchase.

## Contextual × Time — when it matters

Mobile payments must be live before the **Q3 2027 card re-issue** (CN-02), which fixes Transition 1 at Q2 2027 and Transition 2 at Q4 2027. Payments are expected 07:00–23:00 at full service and the card network never sleeps, so authorisation has no maintenance window. The regulator's DR rule is two hours. Identity evidence may be kept 30 days after a decision and no longer. The 2028 reporting regime is the outer boundary the programme must not cross.

## In the other frameworks

This row is the SABSA reading of TOGAF's *Business Principles, Goals and Drivers* and the Preliminary-Phase context in the *Request for Architecture Work*; the ArchiMate *Motivation view* (Stakeholder, Driver, Assessment, Goal) draws the same content, and the *Organization view* draws the People cell. Where TOGAF confirms the drivers in Phase A, SABSA has already asked what each driver puts at risk.

*Source note: SABSA framework as published by the SABSA Institute (open-use with attribution); section numbers refer to the SABSA White Paper and are to be verified against the registered PDF.*
