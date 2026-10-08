---
title: Requirements Impact Assessment — card network message migration brought forward
deliverable: Requirements Impact Assessment
phase: REQ
kind: ASSESSMENT
summary: What the Requirements Management process produced when an assumption failed mid-cycle — which requirements change, which phases must be revisited, and who leads the re-prioritisation.
refs: ["CONTENT §4.2.18", "ADM §13.4", "ADM §13.3"]
source: authored
status: draft
---

> **What to notice.** Requirements Management is the process at the centre of the cycle. It does not itself decide, dispose of or prioritise requirements — the *phase* does that — but it identifies changed requirements, assesses their impact, and records which phases must be revisited. Its two outputs are the Requirements Impact Assessment and the updated Requirements Specification; the Impact Assessment is both an input and an output of the process. The contents list is the same six items as a Change Request's impact section, plus the repository reference.

| | |
|---|---|
| Reference | RIA-2026-02 |
| Date | 18 August 2026, during Phase E |
| Trigger | The card network wrote on 14 August that its ISO 8583 message migration moves from 2028 to **Q2 2027** — assumption AS-01 ("version fixed through 2027") no longer holds |
| Raised by | Owen Price (technology architect) into the Requirements Management process |

## 1. Reference to specific requirements

| Id | Requirement or assumption | Effect |
|---|---|---|
| AS-01 | Card network keeps its ISO 8583 version through 2027 | **Invalid** |
| RQ-02 | Every card transaction fraud-scored before authorisation | Unchanged in substance; IF-02 field mapping must be done for the *new* message version |
| RQ-18 | Scoring round trip ≤ 150 ms | Unchanged; the Card Switch vendor's migration build may change its latency profile — to re-confirm |
| CN-02 | Mobile payments live before the Q3 2027 card re-issue | Unchanged, but the network migration now lands in the same quarter as Transition 1 |
| New: RQ-26 | The Card Switch supports both message versions during the network's migration window | Proposed, *Must* |
| New: CN-06 | No scoring cut-over inside the network migration window (Q2 2027) | Proposed |

## 2. Stakeholder priority of the requirements to date

Cards Ops Lead: RQ-02 and RQ-04 *Must*, unchanged; strongly prefers scoring after the migration settles. CIO: CN-02 *Must*; the Card Switch vendor's migration work must not displace Transition 1. Compliance Officer: no view on sequence; the network mandate is non-negotiable. Sponsor: SM-03 (fraud losses) may slip a quarter if that protects Transition 1.

## 3. Phases to be revisited

| Phase | Why | Extent |
|---|---|---|
| D Technology Architecture | The Card Switch's interface to the network changes; the Technology Standards catalog entry for ISO 8583 needs the new version and a migration state | One catalog entry, one diagram (Networked Computing) |
| E Opportunities and Solutions (current) | Implementation Factor catalog and the work package sequence: the vendor's migration build competes with WP-4 and WP-5 | Factor catalog; WP-4 and WP-5 dependencies |
| C Application Architecture | IF-02 mapping to the new message version | Interface catalog entry only |
| A, B, F | No revisit: the Vision, business architecture and (not yet started) migration plan are unaffected beyond dates | — |

## 4. Phase to lead on requirements prioritisation

**Phase E**, currently in progress: it owns the sequence and the factor catalog, and Phase F will inherit whatever it decides. Phase D is revisited only to update the catalog and diagram; it does not re-open the technology decisions.

## 5. Results of phase investigations and revised priorities

Phase E investigation (16–18 August, with the Card Switch vendor): the vendor can deliver the network migration and the scoring call as one build if the scoring change is designed by June 2027, which matches P5's contract dates. Revised priorities: RQ-26 accepted at *Must*; CN-06 accepted; WP-5 (dual-homing) moved ahead of the network migration so both data centres are ready for the new version; WP-4 go-live confirmed for November 2027, *after* the migration and the re-issue. SM-03's twelve-month clock therefore starts in November 2027, as already planned — no slip.

## 6. Recommendations on management of requirements

- Record network and vendor mandates as *dated* assumptions with an owner who re-confirms them each phase; AS-01 had no re-confirmation step.
- Add a "vendor roadmap" factor type to the Implementation Factor catalog.
- Re-run this assessment when the network publishes the migration technical specification (expected October 2026).

## 7. Repository reference number

Requirements Repository ARCH-26 (RQ-26), ARCH-C06 (CN-06), ARCH-A01 (AS-01 closed); Governance Log GL-2026-027; Requirements Specification updated to v0.4; Roadmap AR-2026-01 v1.0 factor catalog updated.

**Outcome recorded by the Requirements Management process:** Architecture Requirements Specification updated; Phases D and E revisited as above; no change to the Statement of Architecture Work's plan.
