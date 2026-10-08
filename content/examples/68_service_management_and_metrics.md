---
title: "Security service management and metrics — Digital Channels in operation"
deliverable: Security service management and metrics
phase: G
kind: DELIVERABLE
track: SABSA
summary: "The Service Management row for the live programme: how the security services are operated, how incidents and changes are handled, how assurance and audit produce evidence, and the attribute metrics — with the targets of the Business Attributes Profile — that feed Manage & Measure back into strategy."
refs: ["SABSA §7", "GUIDE:integrating-risk-and-security §5", "GUIDE:integrating-risk-and-security §3", "ADM §11", "GOV §6"]
artefacts: []
source: authored
status: draft
---

> **What to notice.** The sixth row of the Matrix is not a seventh layer beneath Component; it runs *across* all six, because every service, mechanism and product has to be operated, changed, measured and assured. Its Motivation cell is the metric set — the same attributes and targets as document 61, now measured rather than promised — and that is what closes the SABSA Lifecycle: Manage & Measure hands numbers back to Strategy & Planning. The trap is measuring what the tools emit instead of what the attributes ask: a dashboard of blocked IPs says nothing about *Fraud-resistant*, whose metric is loss per 1,000 cards and seconds to block.

| | |
|---|---|
| Reference | SEC-OPS-2027-01, version 1.0, 1 July 2027 (Phase G, from Transition 1); revised at Transition 2 |
| Owner | Platform team lead for operations; Cards Ops Lead for fraud operation; Owen Price for assurance; Head of Risk as policy authority |

## Service Management × Process — operations, incident and change

| Process | How it runs for the security services | Evidence it leaves |
|---|---|---|
| Operate | The platform team runs SS-02, SS-07, SS-08, SS-11 and SS-12 as platform services with an on-call rota; Cards Operations runs SS-09 from the console; the vendor runs SS-10 under contract with the bank holding the logs | Monthly service report per service level of the Requirements Specification §3 |
| Incident | Security incidents follow the bank's incident process with two additions: a SIEM alert opens an incident automatically within 15 minutes, and any incident touching a customer's data or money is classified by the *attribute* harmed (Confidential, Accurate, Fraud-resistant) so the Head of Risk sees appetite breaches, not ticket counts | Incident record with attribute, impact and the risk-register row (T-01 to T-08) it realised |
| Change | Changes go through the existing change-advisory board with the Implementation Governance Model's checkpoints as gates; a change to a fraud rule or threshold is configuration owned by Cards Operations and is logged, not board-approved; a change to an *attribute target* or an appetite line is a Change Request into Requirements Management, never an operational change | Change record; Change Request (as CR-2027-03 for the retraining store) |
| Vulnerability and patch | Platform components patched monthly, critical within 72 hours; vendor products under contract terms; the card link under network rules | Patch report against the Technology Standards catalog |

## Service Management × People — assurance and audit

Three lines: the platform and Cards Operations teams operate and self-check; Risk, through Owen Price's assurance role, verifies that the implemented control matches the designed one; Internal Audit and the regulator examine the evidence. The Compliance Assessment of P5 (CA-P5-01, 24 June 2027) is the assurance framework in action: its security checklist found the vendor support access path undocumented (C-1) and the retraining store unclassified (C-2) — both are SS-02 and SS-04 mechanisms checked against their design, and both conditions carry a due date the Governance Log tracks. TOGAF's compliance review is thus the *event* that produces SABSA's assurance evidence; the Service Management row is what keeps producing it between reviews.

## Service Management × Motivation — the metric set

| Attribute | Metric (document 61) | Target | Transition 1 reading, June 2027 | Source |
|---|---|---|---|---|
| BA-01 Available | Monthly availability | Payments 99.9 % | 99.94 % | Platform monitoring |
| BA-02 Timely | Transfer p95 | ≤ 10 s | 6.8 s | Gateway logs |
| BA-05 Authenticated | Takeovers per 100 k customers per year | ≤ 2 | 1.4 (annualised, two months) | Incident records |
| BA-06 Accurate | Unreconciled transfers per month | 0 | 0 | Daily reconciliation |
| BA-07 Fraud-resistant | Loss index; seconds to block | ≤ 70; ≤ 5 s | 100 (batch still live); n/a until WP-4 | Loss ledger |
| BA-08 Auditable | Events with complete log entry | 100 % | 99.7 % — gap found in card-control events, fixed 18 June | Log pipeline check |
| BA-09 Recoverable | DR test failover time | ≤ 2 h | 1 h 20 min (test of 3 May) | DR test record |
| BA-04 Confidential | Reportable disclosures | 0 | 0 | Incident records |
| BA-12 Cost-effective | Security run cost | ≤ £150 k/yr | £132 k/yr run rate | Finance |

*Legal*, *Usable* and *Reputable* start reporting at Transition 2, when onboarding and scoring go live; their baselines are recorded now so the change can be shown.

## Service Management × Time — the review cycle

Metrics are reported monthly to the platform service review and quarterly to the Architecture Board with the four success measures SM-01 to SM-04; the risk register and appetite are reviewed at each phase gate and at the six-month point after Transition 2, when the analyst-in-the-loop acceptance expires and the automatic-blocking decision (G-12) is taken on evidence. That review is the Phase H input: if *Fraud-resistant* has reached its target with analysts in the loop, the target for the next cycle tightens; if not, the appetite line is revisited rather than quietly missed.

## In the other frameworks

TOGAF Phases G and H hold this as the *Compliance Assessment* (document 22), the *Architecture Contract*'s service levels and the Phase H change management with its security audit of G152 §5.8–5.9; ArchiMate draws it in an *Implementation and Migration view* with the Contract element and, for the metrics, a *Motivation view* whose Assessments are the monthly readings against each Requirement.

*Source note: SABSA framework as published by the SABSA Institute (open-use with attribution); section numbers refer to the SABSA White Paper and are to be verified against the registered PDF.*
