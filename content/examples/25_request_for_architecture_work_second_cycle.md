---
title: Request for Architecture Work — Lending on the Digital Platform (second cycle)
deliverable: Request for Architecture Work (issued from Phase H)
phase: H
kind: DELIVERABLE
summary: The new request Phase H issued after classifying the lending changes as re-architecting — the same headings as the first request, showing what a second cycle starts from.
refs: ["CONTENT §4.2.17", "ADM §12.4", "ADM §12.3"]
source: authored
status: draft
---

> **What to notice.** Phase H does not re-architect. It classifies each change (simplification, incremental, re-architecting) and, when a change is re-architecting, issues a **new Request for Architecture Work** to start another cycle — which is why the request is listed as an output of Phase H as well as of the Preliminary Phase and Phase F. Compare this with the first request: same headings, but the current-state sections now describe the architecture the first cycle delivered, and the constraints include the Lending capability that was explicitly deferred.

| | |
|---|---|
| Reference | RAW-2027-02 |
| Date | 28 September 2027, after the Phase H review of the Digital Channels cycle |
| From | Priya Nandakumar, Head of Retail Banking, with Kwame Mensah, Head of Lending (co-sponsor) |
| To | Lena Okafor, Chief Architect |
| Phase H classification that led here | Change Request CR-2027-06 "small-business lending in the app" assessed as **re-architecting** (new capability, new data entities, new external parties) — Architecture Board minute AB-2027-12 |

## 1. Organization sponsors

Head of Retail (budget) and Head of Lending (business outcome); the CIO remains co-sponsor for the platform.

## 2. Organization's mission statement

Unchanged: everyday banking that is simple to open, safe to use and available wherever the customer is.

## 3. Business goals (and changes)

| Goal | Status after the first cycle | Change requested |
|---|---|---|
| Grow lending | Deferred in cycle one | Approve 80% of small-business loans within one day, in the app or at the counter |
| Stay compliant | Constraint only in cycle one | Regulatory reports from one data source before the 2028 regime — now in scope, as the Data Warehouse must be replaced |
| Grow mobile adoption | 41% mobile transfers at September 2027, on track for 60% | Maintain |
| Reduce fraud losses | Scoring goes live November 2027 | Extend scoring to loan applications |

## 4. Strategic plans of the business

Retail Strategy 2026–2028, year three: "credit where the customer is". The Lending plan targets £120m of small-business lending in 2028, of which half originated digitally.

## 5. Time limits

Lending in the app by Q3 2028; Data Warehouse replaced before the 2028 reporting regime's first return (Q1 2029); Architecture Vision for this cycle by 31 January 2028.

## 6. Changes in the business environment

Two competitors offer same-day small-business credit in-app; the regulator has published the 2028 reporting data model; the card network's 2028 message migration is confirmed for Q2 2028.

## 7. Organizational constraints

- The Digital Platform team (4) is fully occupied running Transition 2 until Q1 2028.
- Lending has no digital team; Loan Officers do credit assessment by hand.
- The analyst-in-the-loop period for fraud scoring runs to June 2028; nothing may change the scoring path before then.

## 8. Budget information, financial constraints

Architecture work: £300k (a smaller cycle — the capability and platform now exist). Programme envelope indicative £4.8m, plus the Data Warehouse replacement budget held by Finance.

## 9. External constraints, business constraints

Credit decisions must be explainable to the customer and the regulator; credit bureau data may be used only with consent captured in the journey; in-country data rule unchanged.

## 10. Current business system description

Accounts open in ten minutes in the app or at the counter (Transition 2, from November 2027); transfers and card controls in the app; fraud scored before authorisation with analysts reviewing. Loans: paper application, Loan Officer assessment, four-day median decision.

## 11. Current architecture / IT system description

Channel API Layer (SBB-01) on Platform Services (SBB-06) in both data centres; Mobile App v4; Identity Verification service; Fraud Engine with Kafka feed; Core Banking v12 as system of record; Card Switch dual-homed; Data Warehouse (Oracle 11g) still producing regulatory reports, fraud batch retired. The Architecture Repository holds the full first-cycle landscape, dated and verified.

## 12. Description of developing organization

Enterprise Architecture: five (a data architect was hired after cycle one); ACMM re-scored at **2.4** in September 2027 (target was 2.5; governance and communication reached Level 2; acquisition strategy remains at 1). Architecture Board unchanged; Programme Board to be re-formed for Lending.

## 13. Description of resources available to developing organization

Five EA staff at 60%; the first cycle's deliverables as templates in the Reference Library; SBB-01, SBB-02 and SBB-06 marked re-usable; the Lending capability's baseline processes are *not* in the Landscape and will need Phase B discovery.

**Sponsors' signatures:** P. Nandakumar, K. Mensah, 28 September 2027 · **Accepted:** Architecture Board AB-2027-12
