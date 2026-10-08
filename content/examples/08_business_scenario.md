---
title: Business Scenario — Opening an account and paying from the phone
deliverable: Business Scenario (technique used in Phase A)
phase: A
kind: SCENARIO
summary: The scenario document that drove Phase A, laid out in the Series Guide's contents list, with SMART objectives and the actors, processes and pain points the workshops found.
refs: ["GUIDE:business-scenarios §4", "GUIDE:business-scenarios §9.2", "GUIDE:business-scenarios §6", "ADM §3.3"]
source: authored
status: draft
---

> **What to notice.** A Business Scenario is a *technique*, not a deliverable in the Content Framework table, but it is the technique Phase A uses to discover and agree business requirements and it is what the Architecture Vision's "problem description" summarises. The guide's contents list (executive summary, roadmap, scenario, business environment, technical environment, analysis, priorities, next steps, appendices) is followed here, and the objectives are made SMART the way the guide's §9.2 example does.

| | |
|---|---|
| Version | 1.0, 17 March 2026 — after two gathering workshops and one review workshop |
| Owner | Rahul Desai, business architect |
| Workshop attendees | Head of Retail, Cards Ops Lead, two branch managers, Digital Channels product owner, Compliance Officer, Core Banking lead |

## 1. Executive summary

**1.1 "So what?"** Northgate loses two thirds of young new-to-bank customers to banks that open accounts in minutes, and loses £4.1m a year to card fraud its overnight scoring finds too late. Both problems have the same shape: the customer acts now and the bank responds tomorrow.

**1.2 Who will use this scenario, and how?** The Architecture Board, to agree the problem before the architecture is drawn; the Phase B–D architects, to derive requirements; delivery teams, as the story their acceptance tests replay.

## 2. Document roadmap

Sections 3–5 describe the situation as found; section 6 analyses it; section 7 ranks where to standardise; appendices hold workshop notes and measures.

## 3. Business scenario

**3.1 Background.** The 2026–2028 Retail Strategy commits to a mobile channel that can open, pay and manage a card without a branch. The Request for Architecture Work RAW-2026-01 asked for the architecture to plan it.

**3.2 Purpose.** Establish the business requirements for the Digital Channels programme, agree them with the stakeholders who own the affected processes, and give Phase A a problem statement everyone has signed.

**3.3 Definition of terms.** *Onboarding*: everything from "I want an account" to a usable account and card. *Authorisation*: the Card Switch's yes/no to the card network. *Scoring*: assigning a fraud probability to a transaction.

**3.4 Development.** Premise formulation by the sponsor and Chief Architect (2 March); two gathering workshops (5 and 9 March); analysis by EA (10–13 March); documented (this version); reviewed with all attendees (17 March).

## 4. Business environment

**4.1 Constituencies.** Retail Banking (sponsor); Cards Operations; Branch Network; Risk and Compliance; Retail IT; the card network and the regulator as external parties.

**4.2 Business drivers.** Customers expect digital banking; rising card fraud; cost pressure. (Full table in *Business Principles, Goals and Drivers*.)

**4.3 Business process (value stream).** *Onboarding:* attract → verify identity → open account → issue card → activate. *Payment:* initiate → check funds → screen for fraud → authorise → post → notify.

**4.4 Human actors and roles.** Customer (any channel); Branch Teller (opens accounts, today); Fraud Analyst in Cards Operations (reviews flagged transactions, blocks cards); Compliance Officer (approves KYC procedure); Digital product owner (owns the app journey).

**4.5 Relationship to processes.** Tellers perform all of onboarding today; analysts act on scoring the next morning; the customer only *initiates* today and waits for the bank.

## 5. Technical environment

**5.1 Technical process.** Onboarding: paper form → teller keys into Core Banking → overnight batch activates. Payment: channel → Core Banking or Card Switch point-to-point → overnight batch to the Data Warehouse → fraud report.

**5.2 Computer actors and roles.** Core Banking (system of record: customer, account, posting); Card Switch (authorisation); Mobile App (balance display only); Data Warehouse (batch fraud scoring, reporting); SMS gateway (notifications).

**5.3 Relationship to processes.** Every channel integrates directly with Core Banking; there is no shared service layer, so a rule changed for the counter is not changed for the app.

## 6. Business scenario analysis

**6.1 Problem summary.** The bank responds to customer actions a day late because verification, scoring and activation are batch processes behind channel-specific integrations.

**6.2 Issues / pain points.**

| Pain point | Who feels it | Measure today |
|---|---|---|
| Account opening takes 45 minutes at a counter and activates next day | Customer, Teller | 45 min; 31% of counter time |
| Fraud is found overnight | Fraud Analyst, Customer | Median 14 hours from transaction to block |
| The app cannot pay | Customer, product owner | 22% of transfers mobile |
| Rules differ by channel | Compliance Officer | 3 KYC exceptions found in audit |

**6.3 Desired outcomes (SMART objectives).** Written first as goals, then sharpened the way the guide's §9.2 example does — adding a measure, a realistic scope and a date:

| Goal as first stated | SMART objective |
|---|---|
| "Open accounts quickly in the app" | By the end of Q4 2027, a customer with a passport or driving licence can open a current account in the Mobile App or at a counter in under 10 minutes, with the account usable immediately; measured as median minutes per onboarding |
| "Stop fraud faster" | By the end of Q2 2027, every card transaction is fraud-scored before authorisation and a suspected card is blocked within 5 seconds of scoring; measured as seconds from score to block |
| "Let people pay from the phone" | By Q2 2027, a customer can send a transfer from the Mobile App within 10 seconds end to end; by end 2027, 60% of transfers are made in the app |

**6.4 Information flow.** Identity evidence → verification result → customer record (Core Banking) → account → card. Transaction → score → authorisation decision → posting → notification.

**6.5 Requirements (first cut, into the Requirements catalog).** RQ-01 transfer from the app in 10 s; RQ-02 every card transaction scored before authorisation; RQ-03 onboarding usable at counter or app with the same rules; RQ-04 block within 5 s of a fraud score.

**6.6 Principles and constraints.** PR-02 one customer record; PR-05 channel independence; CN-01 Core Banking stays system of record; CN-02 go-live before the Q3 2027 card re-issue; CN-03 no new customer data store.

**6.7 Resulting architecture models.** Value Chain diagram; Solution Concept diagram; Business Capability Map with heat overlay (all on the Artefacts page).

## 7. Prioritized areas for standardization

**7.1 Priorities by process area.** 1. A single service layer every channel uses (fixes rules-by-channel and enables everything else). 2. Real-time fraud scoring. 3. Digital identity verification. 4. Reporting from one data source (deferred).

**7.2 Suggested starting points.** The service layer and mobile payments first — smallest change to Core Banking, largest share of the 60% goal, and must precede the card re-issue.

## 8. Summary and next steps

The stakeholders agreed the problem statement and the three SMART objectives on 17 March. Next: Statement of Architecture Work and Architecture Vision to the Architecture Board on 31 March.

## Appendices (in the repository)

A. Measures and baselines by pain point. B. Referenced documents (Retail Strategy, RAW-2026-01, audit report 2025). C. Workshop notes and the money-voting result. D. Acknowledgements.
