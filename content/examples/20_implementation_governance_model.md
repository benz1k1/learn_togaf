---
title: Implementation Governance Model — Digital Channels programme
deliverable: Implementation Governance Model
phase: F
kind: DELIVERABLE
summary: How the five delivery projects will be governed through Phase G — processes, organisation, roles and the two checkpoints with their pass and fail criteria.
refs: ["CONTENT §4.2.15", "ADM §10.4", "GOV §3"]
source: authored
status: draft
---

> **What to notice.** Produced in Phase F, consumed in G and H. Its job is to make sure a project *transitioning into implementation also transitions into architecture governance* — the bank already has an Architecture Board, but this model defines the project-specific processes, roles, checkpoints and success/failure criteria. The four contents headings are exactly the four sections below. It is a Phase G input, alongside the Architecture Contract standard and the Architecture Governance Framework; the Communications Plan is *not*.

| | |
|---|---|
| Reference | IGM-2026-01, version 1.0, 26 September 2026 |
| Applies to | PMO programme DC-2027, projects P1–P5 |

## 1. Governance processes

| Process | Trigger | Steps | Output into the Governance Log |
|---|---|---|---|
| Contract signing | Project initiation | EA drafts the Architecture Contract from the template; project manager and Chief Architect sign; sponsor countersigns | Signed Architecture Contract |
| Architecture checkpoint 1 — design | Design sign-off | Solution architect presents against the Definition Document and Requirements Specification; EA completes the checklists; pass / conditional pass / fail | Compliance Assessment |
| Architecture checkpoint 2 — pre-go-live | Before the change-advisory board | Evidence of the service levels in pre-prod; security checklist re-run; open conditions closed | Compliance Assessment |
| Change Request | A project cannot comply, or scope grows | Project raises; Chief Architect assesses impact in five days; decision route by size (see the Statement of Architecture Work) | Change Request with decision |
| Waiver | A principle or standard cannot be met in time | Board grants, time-boxed, with a remediation date | Waiver register entry; re-reviewed at Phase H |
| Lessons learned | Project close | Retrospective with EA present; findings to Phase H | Lessons record |

## 2. Governance organisation structure

```
Retail Investment Committee (funding)
        │
Architecture Board (CIO chair) ── Programme Board (Head of Retail, SRO)
        │                                  │
Chief Architect ── EA compliance reviewers   Project Boards P1–P5 (each with an EA member)
                                            │
                                        Solution architects (Retail IT / vendors)
```

The Architecture Board governs conformance; the Programme Board governs delivery. Where they disagree, the Statement of Architecture Work's change-of-scope procedure decides, because scope is the sponsor's.

## 3. Governance roles and responsibilities

| Role | Held by | Responsibilities |
|---|---|---|
| Chief Architect | Lena Okafor | Signs contracts; decides small Change Requests; chairs checkpoints |
| EA compliance reviewer | The domain architect not assigned to the project | Completes checklists; independent of the project's own EA member |
| Project EA member | One architect per project | Advises the project; may not review it |
| Solution architect | Retail IT or vendor | Designs within the contract; raises Change Requests |
| Project manager | PMO | Schedules checkpoints as stage boundaries; owns conditions |
| Sponsor / SRO | Head of Retail | Countersigns contracts; accepts residual risk on waivers |
| Cards Operations rule owner | Cards Ops Lead | Signs off P5's rule-tuning design and the analyst-in-the-loop exit |

## 4. Governance checkpoints and success/failure criteria

| Checkpoint | Success | Conditional pass | Failure |
|---|---|---|---|
| Contract signed | Signed before any build spend | — | Build spend before signature is reported to the Programme Board |
| Checkpoint 1 — design | All Must requirements in the contract traced to design; checklists complete with no red items; no unapproved deviation from the Definition Document | Amber items with an owner and a date before checkpoint 2 | Any red item; any Must requirement untraced; a deviation with no Change Request |
| Checkpoint 2 — pre-go-live | Service levels demonstrated in pre-prod (RQ-01 10 s p95; RQ-18 150 ms p99; RQ-08 failover); security checklist green; conditions closed | — | Any service level unmet; any condition open; change-advisory board is asked to defer |
| Transition complete | All packages in the transition passed checkpoint 2 and ran one quarter of hypercare; success measures reported | — | Board decides whether the transition is declared or re-planned |
| Analyst-in-the-loop exit (P5 only) | Six months of shadow decisions agree with analysts at ≥ 98%; Cards Ops Lead signs | — | Period extended; Change Request if the threshold design must change |

Metrics reported to the Architecture Board quarterly: checkpoints passed first time; open conditions older than 30 days; waivers outstanding; Change Requests by class.
