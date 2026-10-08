---
title: Architecture Maturity Assessment — ACMM scorecard
deliverable: Architecture maturity assessment (ACMM scorecard, part of the Organizational Model and the Capability Assessment)
phase: PRELIM
kind: ASSESSMENT
summary: Northgate scored on the nine ACMM elements at six levels, both ways the guide describes — a weighted mean and a percentage per level — with the evidence behind each score.
refs: ["GUIDE:architecture-maturity-models §2.2", "GUIDE:architecture-maturity-models §2.3", "GUIDE:architecture-maturity-models §2.1", "CONTENT §4.2.16"]
source: authored
status: draft
---

> **What to notice.** The Series Guide describes the US Department of Commerce ACMM: **six levels (0 None, 1 Initial, 2 Under Development, 3 Defined, 4 Managed, 5 Measured)** across **nine elements**, and *two* ways of reporting — a weighted mean level and the percentage achieved at each level. Exam questions ask for the level count, the element count, and which of the two methods a scenario is using. The scorecard feeds the "maturity assessment, gaps and resolution approach" heading of the Organizational Model and the "architecture maturity assessment" part of the Phase A Capability Assessment.

| | |
|---|---|
| Assessed | February 2026, by the Chief Architect with the CIO's office; re-scored at Phase H |
| Method | US DoC Architecture Capability Maturity Model, as described in the TOGAF Series Guide |
| Scope | The Enterprise Architecture capability of Northgate Bank as a whole (not the Digital Channels programme) |

## 1. Scorecard by element

Scores are the highest level whose characteristics for that element are *fully* met.

| # | Element | Level | Evidence for the score | What the next level would need |
|---|---|---|---|---|
| 1 | Architecture process | 2 | A basic process is written down and roles are assigned (Level 2). It is not "largely followed": two of last year's five projects skipped it | Follow the process on every project; publish it to IT staff and business management |
| 2 | Architecture development | 2 | Principles, business linkage and a Baseline Architecture exist; a Target Architecture exists for Core Banking only. Standards exist but are not linked to a target | Gap analysis and a migration plan; a full standards profile |
| 3 | Business linkage | 2 | Explicit link to the Retail Strategy through the driver/goal table | Integration with capital planning and investment control |
| 4 | Senior management involvement | 2 | The CIO and Head of Retail are aware and have signed the Request for Architecture Work | Active support for standards from the whole senior team |
| 5 | Operating unit participation | 1 | Branches and Cards Operations have limited acceptance; they have never been asked to take part | Responsibilities assigned in the operating units and work under way |
| 6 | Architecture communication | 1 | The latest documentation is online, but only the EA team opens it; no communication about the process | Pages updated periodically and used to document deliverables |
| 7 | IT security | 2 | Security architecture has clear roles (Risk owns it); no standards profile | A fully developed security standards profile integrated with the EA |
| 8 | Architecture Governance | 1 | No explicit governance of architectural standards; the Board approves documents but nothing checks compliance | Governance of at least a few standards and some adherence |
| 9 | IT investment and acquisition strategy | 1 | Procurement does not involve EA; little adherence to existing standards | Some formal link between acquisition and the standards profile |

## 2. Method one — weighted mean maturity level

The bank weights the nine elements equally, so the weighted mean is the arithmetic mean:

| Levels scored | 2, 2, 2, 2, 1, 1, 2, 1, 1 |
|---|---|
| **Weighted mean** | **(2+2+2+2+1+1+2+1+1) / 9 = 1.56 → reported as 1.6** |

Reported to the CIO as "between Initial and Under Development".

## 3. Method two — percentage achieved at each level

The second method asks, for each level, what share of the nine elements has reached it.

| Level | Elements at or above this level | Percentage |
|---|---|---|
| 0 None | 9 of 9 | 100% |
| 1 Initial | 9 of 9 | 100% |
| 2 Under Development | 5 of 9 (elements 1, 2, 3, 4, 7) | 56% |
| 3 Defined | 0 of 9 | 0% |
| 4 Managed | 0 of 9 | 0% |
| 5 Measured | 0 of 9 | 0% |

The two methods tell the same story differently: the mean says "1.6"; the percentages say "Level 2 is half done and Level 3 has not started anywhere". The second view is the one the Organizational Model uses to choose where to act, because it shows that governance, participation, communication and acquisition (the four elements still at Level 1) are what hold the capability back.

## 4. Target and resolution

| Element | Now | Target after the Digital Channels cycle | How |
|---|---|---|---|
| 5 Operating unit participation | 1 | 2 | Cards Operations and the Branch Council take named roles in the Communications Plan and the Architecture Contracts |
| 6 Architecture communication | 1 | 2 | Repository published read-only; every deliverable posted at its phase gate |
| 8 Architecture Governance | 1 | 2 | Implementation Governance Model; two compliance checkpoints per project |
| 9 IT investment and acquisition | 1 | 2 | Architecture Requirements Specification is a mandatory input to the Fraud Engine and identity-verification procurements |
| 1–4, 7 | 2 | 3 where the cycle produces the evidence (gap analysis and migration plan will exist after Phases E–F) | — |

**Target weighted mean: 2.5.** Re-score at the Phase H review, September 2027.

## 5. Why ACMM and not CMMI here

The guide also describes CMMI and its SCAMPI appraisal method. The bank chose the ACMM because it is specific to Enterprise Architecture, can be self-assessed in an afternoon, and its nine elements map directly onto the Organizational Model's headings. CMMI remains the reference if a formal external appraisal is ever needed.
