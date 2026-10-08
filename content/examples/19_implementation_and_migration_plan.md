---
title: Implementation and Migration Plan v1.0
deliverable: Implementation and Migration Plan
phase: F
kind: DELIVERABLE
summary: The schedule of projects that realise the target, grouped into a programme with milestones, resources and costs, and the strategy behind the sequence; drafted in Phase E and approved in Phase F.
refs: ["CONTENT §4.2.14", "ADM §10.4", "ADM §10.3"]
source: authored
status: draft
---

> **What to notice.** Phase E produces the *draft*; Phase F produces the *approved* plan, after confirming it with the bank's other management frameworks (business planning, portfolio/project management, operations) at step 1. The contents list is strategy, then project and portfolio breakdown, then optional project charters. Northgate writes it in PRINCE2 project-brief form (a tailoring decision) so the PMO can adopt it as the programme's plan of record without translation.

| | |
|---|---|
| Reference | IMP-2026-01, version 1.0 (approved), 26 September 2026 |
| Approved | Architecture Board minute AB-2026-16; Retail Investment Committee 30 September 2026 (WP-1, WP-3, WP-5 funded; WP-2, WP-4 funded subject to procurement outcome) |

## 1. Implementation and Migration Strategy

**Strategic implementation direction.** *Greenfield around an unchanged core*: build the platform and service layer beside Core Banking and the Card Switch, buy the two engines, and move channels onto the layer one journey at a time. No big-bang; nothing is switched off until its replacement has run for one full quarter.

**Implementation sequencing approach.** Value first, risk second, in two releases fixed by the card re-issue: Transition 1 (Q2 2027) delivers payments and the platform; Transition 2 (Q4 2027) delivers onboarding and scoring. Work packages that need the same scarce resource (the data-centre change window; the Card Switch vendor) are serialised; everything else runs in parallel.

**Confirmation with other frameworks (Phase F step 1).**

| Framework | Confirmed |
|---|---|
| Business planning | The two transitions match the Retail Strategy's 2027 milestones; the roadmap feeds the September investment plan |
| Portfolio and project management | Five projects entered in the PMO portfolio; project boards include an EA member; the Implementation Governance Model's checkpoints are PRINCE2 stage boundaries |
| Operations | Transitions map to two ITIL releases; the change-advisory board is the release gate; the DR test in Q1 2027 includes the API layer |

## 2. Project and portfolio breakdown

**Programme: Digital Channels** (PMO programme DC-2027), five projects.

| Project | Work packages | Capabilities delivered | Start | Finish | Milestones |
|---|---|---|---|---|---|
| P1 Platform | WP-1 | Platform services; Payments and Card Management APIs; Onboarding API (stub) | Oct 2026 | Mar 2027 | Platform team formed Oct 2026; gateway live in pre-prod Jan 2027; Payments API live Mar 2027 |
| P2 Mobile payments | WP-3 | Transfers and card controls in the app; SMS gateway retired | Nov 2026 | Jun 2027 | Beta Apr 2027; store release May 2027; **Transition 1 complete 30 June 2027**, before the re-issue |
| P3 Resilience | WP-5 | Dual-homed card link; pre-prod | Nov 2026 (change window Q4) | Feb 2027 | DR test Q1 2027 passes the two-hour level |
| P4 Digital onboarding | WP-2 | Verification service; app and counter journeys; branch file destruction | Jan 2027 (procurement) | Nov 2027 | Product selected Mar 2027; app journey Sep 2027; counter rollout Oct–Nov 2027 |
| P5 Fraud scoring | WP-4 | Fraud Engine; Card Switch call; rule tuning; analyst-in-the-loop | Jan 2027 (procurement) | Dec 2027 (+6 months in-the-loop) | Product selected Apr 2027; shadow scoring Aug 2027; scoring before authorisation Nov 2027; **Transition 2 complete 15 December 2027**; automatic blocking Jun 2028 |

**Work breakdown (summary).** Each project: initiate (charter, Architecture Contract signed) → design (architecture checkpoint 1) → build → test (including the compliance checklists) → pre-go-live (checkpoint 2) → release → one-quarter hypercare → close (lessons learned to Phase H).

**Impact on the existing portfolio.** Core Banking v12 upgrade: unchanged, must finish before P1's integration stage. Branch closure programme: P4's counter rollout follows each closure announcement by at least one quarter. Data Warehouse replacement (2028, next cycle): must not plan on the fraud feed, which stops at Transition 2.

## 3. Project charters (summary — full charters in the PMO)

| Project | Business value | Risks, issues, assumptions, dependencies | Resources and cost | Benefits mapped to requirements |
|---|---|---|---|---|
| P1 Platform | Prerequisite for all benefits; re-use by Lending | Platform team hiring (action, CIO); v12 completion | 4 platform engineers, gateway licence; **£1.1m** | RQ-01, RQ-07, RQ-08 |
| P2 Mobile payments | SM-02 mobile share 22% → 60% (£2.3m/yr lower cost to serve at target) | App store review timing; re-issue date immovable | 6 developers, 2 testers; **£1.4m** | RQ-01, SM-02 |
| P3 Resilience | Regulatory compliance; enables scoring | Single change window per quarter | Network team, Card Switch vendor; **£0.5m** | RQ-08 |
| P4 Digital onboarding | SM-01 counter time halved (£1.1m/yr); new-to-bank growth | Procurement lead time; Compliance procedure; branch sequencing | Vendor subscription (CFO approval), 4 developers; **£1.6m** + £180k/yr |
| P5 Fraud scoring | SM-03 losses −30% (£1.2m/yr) | R-1 analyst acceptance; 150 ms budget; vendor timeout behaviour | Vendor licence, 2 engineers, Cards Ops rule tuner; **£1.9m** + £460k/yr | RQ-02, RQ-04, RQ-09 |

**Programme total: £6.5m capital** (matches the Request for Architecture Work envelope) **plus £640k/yr run cost from Transition 2.** Estimated migration options considered and rejected: single release in Q4 2027 (misses the re-issue; £1.4m second mailing); replace the Card Switch instead of adding the engine (£4m more, 2029).
