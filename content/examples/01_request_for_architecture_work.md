---
title: Request for Architecture Work — Digital Channels
deliverable: Request for Architecture Work
phase: PRELIM
kind: DELIVERABLE
summary: The one-page trigger the Head of Retail sends to the architecture team; every later document traces back to it.
refs: ["CONTENT §4.2.17", "ADM §2.4", "ADM §3.2"]
source: authored
status: draft
---

> **What to notice.** Everything here is high level and comes *from the sponsor*, not from the architects. It is an output of the Preliminary Phase (or of Phase F or H in later cycles) and the input that starts Phase A. It contains no architecture: no models, no options, no target. If a candidate answer puts a Solution Concept diagram in a Request for Architecture Work, it is describing the Architecture Vision instead.

| | |
|---|---|
| Reference | RAW-2026-01 |
| Date | 12 January 2026 |
| From | Priya Nandakumar, Head of Retail Banking (sponsor) |
| To | Lena Okafor, Chief Architect, Enterprise Architecture |
| Status | Accepted by the Architecture Board, 26 January 2026 |

## 1. Organization sponsors

- **Executive sponsor:** Priya Nandakumar, Head of Retail Banking. Owns the budget and the business outcome.
- **Co-sponsor:** Tomasz Weber, Chief Information Officer. Owns the Core Banking roadmap the work must fit.
- **Sponsoring unit:** Retail Banking, which runs the branch network, the mobile channel and Cards Operations.

## 2. Organization's mission statement

Northgate Bank is a regional retail bank serving 1.2 million personal and small-business customers through 140 branches, a mobile app and a card portfolio. Its stated mission is *"everyday banking that is simple to open, safe to use and available wherever the customer is"*.

## 3. Business goals (and changes)

| Goal | Change from today |
|---|---|
| Grow mobile adoption | Transfers made in the Mobile App to rise from 22% to 60% by the end of 2027 |
| Reduce fraud losses | Card fraud losses to fall by 30% within twelve months of go-live |
| Lower cost to serve | Branch time spent on account opening to halve; today a new account takes 45 minutes at a counter |
| Stay compliant | Regulatory reports to be produced from one data source (deferred to a later cycle; recorded here so it is not lost) |

## 4. Strategic plans of the business

The 2026–2028 Retail Strategy ("Digital First") commits the bank to a mobile channel that can open an account, make a payment and manage a card without a branch visit, and to reducing the branch estate by 20 branches over the same period. This request asks for the architecture work that lets that strategy be planned and costed.

## 5. Time limits

- Architecture Vision and an agreed Statement of Architecture Work by **31 March 2026**.
- Mobile payments live before the **Q3 2027 card re-issue**, so that the new cards are issued with in-app controls. Slipping past the re-issue costs a second mailing (£1.4m).
- The Data Warehouse is out of support in 2028; nothing in this cycle may extend its life.

## 6. Changes in the business environment

- Two national competitors opened accounts in under ten minutes in 2025 and took a visible share of new-to-bank customers under 30.
- Card fraud losses rose 41% year on year, driven by real-time scams the current overnight batch scoring cannot stop.
- New capital-reporting rules take effect in 2028.

## 7. Organizational constraints

- Retail IT is committed to the Core Banking v12 upgrade until June 2026; no Core Banking change requests will be accepted before then.
- Cards Operations runs 24×7 and cannot accept a change freeze longer than 48 hours.
- The bank has no digital identity-verification capability or team today.

## 8. Budget information, financial constraints

- Architecture work in this cycle (Phases A–F): up to **£420k**, from the Retail change budget.
- Indicative programme envelope, subject to the Phase E/F business case: **£6.5m** over two years.
- Capital, not operating, budget; anything consumed as a subscription must be approved separately by the CFO.

## 9. External constraints, business constraints

- Regulator's operational-resilience rules: payments must fail over to the DR data centre within two hours.
- Card network mandate: the ISO 8583 message version stays fixed until the network's 2028 migration.
- Customer data may not leave the country of operation.

## 10. Current business system description

Account opening happens at the branch counter with paper identity checks and a next-day Core Banking activation. Payments are made at the counter, by the legacy online banking site or by card. Card fraud is detected by an overnight batch in the Data Warehouse and blocked by Cards Operations the following morning.

## 11. Current architecture / IT system description

Core Banking (package, v12 upgrade in progress) is the system of record for Customer and Account. The Card Switch (package) authorises card transactions against the card network. The Mobile App today shows balances only, reading Core Banking through point-to-point interfaces. The Data Warehouse (Oracle 11g) produces reports and the fraud batch. There is no API layer; each channel integrates directly.

## 12. Description of developing organization

Enterprise Architecture is a team of four (Chief Architect, business architect, application architect, technology architect) reporting to the CIO, with an Architecture Board that meets fortnightly. Solution delivery is by Retail IT (in-house) with the Card Switch vendor for card changes.

## 13. Description of resources available to developing organization

- The four EA staff at 60% for this cycle; a data architect can be borrowed from Finance for Phase C.
- Access to the Core Banking vendor's reference architecture and to the card network's integration guide.
- The existing Architecture Repository (Confluence space plus a modelling tool with 40 current diagrams).

**Sponsor's signature:** P. Nandakumar, 12 January 2026    **Accepted:** Architecture Board minute AB-2026-02
