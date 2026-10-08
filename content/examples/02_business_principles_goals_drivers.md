---
title: Business Principles, Goals and Drivers — Northgate Bank
deliverable: Business Principles, Business Goals, and Business Drivers
phase: PRELIM
kind: DELIVERABLE
summary: The business context the architects receive rather than write; confirmed and elaborated in Phase A, and the root of every objective the programme measures.
refs: ["CONTENT §4.2.9", "ADM §2.2", "ADM §3.3"]
source: authored
status: draft
---

> **What to notice.** This is a *non-architectural input*: it comes from business planning, not from the ADM. The Preliminary Phase and Phase A consume it; Phase A step 3 "confirms and elaborates" the goals and drivers, and Phase B turns them into the Driver/Goal/Objective catalog. The standard deliberately leaves its structure open ("likely to vary considerably from one organization to the next"), so a bank's version is short and looks like a strategy extract.

**Source:** Retail Strategy 2026–2028 ("Digital First"), approved by the Executive Committee 4 December 2025. Extract prepared for the architecture team by the Strategy Office.

## Business drivers

| Driver | Evidence | Owner |
|---|---|---|
| Customers expect digital banking | 68% of new-to-bank customers under 30 chose a competitor that opens accounts in the app | Head of Retail |
| Rising card fraud | Losses up 41% year on year; 70% are real-time scams the overnight batch cannot stop | Head of Cards Operations |
| Cost pressure | Cost-to-income ratio 62% against a peer median of 55%; branch counters spend 31% of time on onboarding | CFO |
| New capital rules | 2028 reporting regime requires reconciled data from one source | Head of Finance |
| Small-business demand | Loan applications up 18%, decision time median four days | Head of Lending |

## Business goals

| Goal | Objective (SMART) | Measure |
|---|---|---|
| Grow mobile adoption | 60% of transfers made in the Mobile App by 31 December 2027 | Mobile share of transfers, monthly |
| Reduce fraud losses | Cut card fraud losses by 30% within twelve months of fraud scoring going live | Fraud loss per 1,000 cards |
| Lower cost to serve | Halve branch time spent on account opening by the end of 2027 | Minutes per onboarding |
| Stay compliant | Regulatory reports produced from one data source before the 2028 regime | Reports needing manual rework |
| Grow lending | Approve 80% of small-business loans within one day | Median decision time |

The first three goals are in scope for the Digital Channels cycle. "Stay compliant" is a constraint on this cycle (nothing may add a customer data store) and a candidate for the next. "Grow lending" is explicitly out of scope; it is recorded so the Architecture Vision can say so.

## Business principles

These are the *bank's* principles, from which the Preliminary Phase derives the architecture principles.

| Principle | Statement | What it means for the programme |
|---|---|---|
| Customer first | Every change is judged by the customer's time and effort | Onboarding is designed backwards from a ten-minute target |
| Safe by default | The bank never trades security for speed | Fraud scoring runs before, not after, a card is authorised |
| One bank | Branch, mobile and card are one service with one record of the customer | Rules out a separate customer store for the app |
| Spend once | Prefer proven products and re-use over bespoke build | The mobile app is built; identity verification and fraud scoring are bought |
| Run within our means | Change must fit the run-cost envelope agreed with the CFO | Subscriptions need CFO approval; see the Request for Architecture Work |

## Ways of working the architects must respect

- Change is approved through the quarterly Retail Investment Committee; the Architecture Board recommends, it does not fund.
- Branch staff are consulted through the Branch Council before any counter process changes.
- Cards Operations owns the fraud rules; the architecture may change how rules run, not what they say.
