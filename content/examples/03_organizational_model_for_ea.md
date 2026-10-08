---
title: Organizational Model for Enterprise Architecture
deliverable: Organizational Model for Enterprise Architecture
phase: PRELIM
kind: DELIVERABLE
summary: Who does architecture at Northgate, where the boundaries with delivery and operations lie, what it costs, and the maturity gaps the Preliminary Phase found.
refs: ["CONTENT §4.2.16", "ADM §2.3", "ADM §2.4"]
source: authored
status: draft
---

> **What to notice.** Six headings, straight from the contents list: scope of organizations impacted, maturity assessment, roles and responsibilities, constraints, budget, governance and support strategy. The maturity figures come from the separate ACMM scorecard; this document records the *gaps and the resolution approach*, not the scoring detail. It is an output of the Preliminary Phase and an input to every phase after it.

| | |
|---|---|
| Version | 1.0, 20 February 2026 |
| Owner | Lena Okafor, Chief Architect |
| Approved by | Architecture Board, minute AB-2026-04 |

## 1. Scope of organizations impacted

| Organization | Relationship to architecture work |
|---|---|
| Retail Banking (branches, Digital Channels, Cards Operations) | Sponsoring business; supplies stakeholders and accepts the Architecture Vision |
| Retail IT | Delivers solutions; subject to architecture compliance reviews |
| Risk and Compliance | Reviews security and KYC aspects; veto on customer-data decisions |
| Finance | Owns the Data Warehouse; consulted, not changed, in this cycle |
| Lending | Out of scope for this cycle; informed |
| External: Core Banking vendor, Card Switch vendor, card network | Bound by contract, not by the bank's governance; their standards enter as constraints |

## 2. Maturity assessment, gaps and resolution approach

The ACMM scorecard (see the separate assessment) rates the architecture capability at a weighted **1.6 — between Initial and Under Development**. The three lowest elements and what the Preliminary Phase does about them:

| Element | Score | Gap | Resolution in this cycle |
|---|---|---|---|
| Architecture Governance | 1 | Standards exist but nothing checks compliance | Implementation Governance Model in Phase F; compliance reviews at two checkpoints in Phase G |
| Operating unit participation | 1 | Cards Operations and branches have never been asked | Stakeholder map and Communications Plan in Phase A; Branch Council in the review loop |
| Architecture communication | 1 | 40 diagrams in a modelling tool nobody outside EA opens | Publish the Architecture Repository as read-only pages; one-page Architecture Vision |

Target after this cycle: **2.5**, re-scored at the Phase H review.

## 3. Roles and responsibilities for the architecture team

| Role | Person | Responsibilities in the ADM |
|---|---|---|
| Chief Architect | Lena Okafor | Owns the cycle, the Statement of Architecture Work and the Architecture Definition Document; chairs Architecture Board working sessions |
| Business architect | Rahul Desai | Phase B; business scenario workshops; capability map |
| Application architect | Mei Chen | Phase C (application), API layer design, building-block selection |
| Technology architect | Owen Price | Phase D, environments, security architecture with Risk |
| Data architect (loaned from Finance, Phase C only) | Fatima Al-Sayed | Data architecture; guardian of "no new customer data store" |
| Architecture Board | CIO (chair), Head of Retail, CFO delegate, Chief Architect, Head of Risk | Approves deliverables at each phase gate; grants waivers |

Boundaries: solution architects in Retail IT design *within* the Architecture Definition Document and Architecture Requirements Specification; they raise a Change Request when they cannot. Vendors' architects attend working sessions by invitation and have no vote.

## 4. Constraints on architecture work

- Retail IT will accept no Core Banking change until the v12 upgrade completes in June 2026 (from the Request for Architecture Work).
- Architecture staff are available at 60%; the cycle plan in the Statement of Architecture Work assumes that.
- Customer data stays in-country; every cloud option is evaluated against that first.
- The architecture team may recommend but not select vendors; procurement runs a separate process from the Architecture Requirements Specification.

## 5. Budget requirements

| Item | Amount | Source |
|---|---|---|
| Architecture staff time, Phases A–F (4 × 60% × 9 months) | £310k | Retail change budget |
| Data architect loan, Phase C (3 months) | £35k | Retail change budget |
| Modelling tool licences and repository publishing | £15k | EA run budget |
| External review of the security architecture (Phase D) | £40k | Risk budget |
| Contingency | £20k | Retail change budget |
| **Total** | **£420k** | matches the Request for Architecture Work |

## 6. Governance and support strategy

- **Phase gates.** Each phase ends with an Architecture Board decision recorded in the repository; the Statement of Architecture Work lists them.
- **Compliance.** Retail IT projects submit to an architecture compliance review at design sign-off and before go-live (Phase G). Reviews are recorded as Compliance Assessments.
- **Waivers.** The Architecture Board may grant a time-boxed waiver against a principle or standard; every waiver is logged and re-reviewed at Phase H.
- **Support.** EA runs a fortnightly open surgery for delivery teams and publishes the repository read-only to the whole bank.
- **Escalation.** Disagreements between a solution architect and EA go to the Chief Architect, then to the Architecture Board; the Board's decision is final unless the sponsor changes scope through the Statement of Architecture Work's change procedure.
