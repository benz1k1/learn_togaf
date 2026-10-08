---
title: "Two-way traceability matrix — attributes and controls"
deliverable: Two-way traceability matrix (attribute to control)
phase: REQ
kind: DELIVERABLE
track: SABSA
summary: "The attribute-to-service matrix read both ways: top-down, every control is justified by an attribute; bottom-up, every attribute is covered by at least one control — and the completeness check that Requirements Management runs on it at every phase gate."
refs: ["SABSA §8", "GUIDE:integrating-risk-and-security §5", "GUIDE:integrating-risk-and-security §3", "ADM §13"]
artefacts: []
source: authored
status: draft
---

> **What to notice.** Traceability is the proof that the security architecture is business-driven rather than asserted. It has to hold in *both* directions: top-down answers "why does this control exist" (an unjustified control is cost and friction), bottom-up answers "what protects this attribute" (an uncovered attribute is a promise the bank cannot keep). The matrix is a Requirements Management artefact because attributes and targets change across the cycle — every new requirement in Phases C and D, every Change Request, every appetite revision re-runs the check. The trap is a matrix filled once in Phase A and framed; a control added in Phase G with no attribute (the retraining store's pseudonymisation is the live example) shows up here first.

| | |
|---|---|
| Reference | SEC-TRC-2026-01, version 1.3, 30 June 2027 (re-issued after CR-2027-03); v1.0 signed with the Vision |
| Owner | Owen Price; checked by the Requirements Management process at each phase gate and each Change Request |

## The matrix

Rows are the twelve attributes of document 61; columns the twelve security services of document 65. ● primary (the service exists mainly for this attribute); ○ contributing.

| | SS-01 Cust. authn | SS-02 Staff/svc authn | SS-03 Authz | SS-04 Confid. | SS-05 Integrity | SS-06 Non-rep. | SS-07 Audit | SS-08 Avail. | SS-09 Fraud | SS-10 Proofing | SS-11 Keys | SS-12 Monitoring |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BA-01 Available | | | | | | | | ● | | | | ○ |
| BA-02 Timely | ○ | | | | | | | ○ | ● | ○ | | |
| BA-03 Usable | ● | | | | | | | | ○ | ● | | |
| BA-04 Confidential | ○ | ○ | ○ | ● | | | | | | ○ | ● | |
| BA-05 Authenticated | ● | ● | | | | | | | | | ○ | ○ |
| BA-06 Accurate | | | | | ● | | | | | | | |
| BA-07 Fraud-resistant | ○ | | | | | | | | ● | ○ | | ● |
| BA-08 Auditable | | ○ | ○ | | | ● | ● | | | | ○ | |
| BA-09 Recoverable | | | | | | | | ● | | | | |
| BA-10 Legal | | | ● | ○ | | | ○ | | | ● | | |
| BA-11 Reputable | | | | | | ○ | | | ○ | | | ○ |
| BA-12 Cost-effective | | | | | | | | | | | | |

## Top-down: every control justified

Read a column. SS-11 key and secret management has ● *Confidential* and ○ *Authenticated*, *Auditable*: it is justified by three attributes, and if the bank ever asked "why do we pay for an HSM cluster" the answer is on this page, not in a vendor's brochure. Every column has at least one ● — the rule the review applies is that a service with only ○ marks is suspect and a service with none is deleted. The early "data loss prevention" service failed this test in Phase C and was removed. Each mechanism and component in document 66 inherits its column's justification, so a product change alters nothing here; only a *service* change does.

## Bottom-up: every attribute covered

Read a row. *Recoverable* is covered by SS-08 alone — one ● and nothing else. That is not a failure, but it is a **single-point row**, and the review flags it: the DR test twice a year is the only evidence the attribute holds, so the metric set (document 68) reports the test result to the Board rather than burying it. *Cost-effective* has **no mark at all**, and that is correct and deliberate: it is an attribute the *architecture as a whole* serves through the buy-not-build strategy and the run-cost envelope, not one any single security service protects. The completeness rule allows this only when the row's owner has signed an explicit statement of how the attribute is met — the Head of Retail's sign-off on the run-cost line in the Roadmap's factor catalog is that statement, and it is cited in the row's note.

## The completeness check

| Check | Rule | Result at v1.3 |
|---|---|---|
| Every service has a ● | A control with no primary attribute is unjustified | 12 of 12 pass |
| Every attribute has a ● or a signed statement | An uncovered attribute is an unkept promise | 11 of 12 have a ●; BA-12 by statement |
| Single-point rows flagged | One control only means one piece of evidence only | BA-06, BA-09 flagged; evidence sources named in document 68 |
| Every risk row maps to a marked cell | T-01 to T-08 and O-01 to O-03 each name attributes and controls that appear here | 11 of 11 pass |
| Every Requirements Specification entry maps to an attribute | RQ-01 to RQ-24, CN-01 to CN-05 | 29 of 29 after v0.3; RQ-18 key management assigned to BA-04 in Phase D |
| Every Change Request re-runs the check | A changed control or target may orphan a cell | CR-2027-03: pseudonymisation of the retraining store added under SS-04 ● *Confidential*; matrix re-issued as v1.3 |

The Phase G finding that started v1.3 is worth recording: the retraining store's pseudonymisation was a control the project added to satisfy a compliance condition, and for six weeks it existed in the design with no attribute above it. Requirements Management caught it because a Change Request requires this matrix to be re-issued, not because anyone read the design closely — the whole argument for traceability as a *managed* artefact rather than a diagram.

## In the other frameworks

TOGAF's Requirements Management phase keeps this in the *Architecture Requirements Repository* and the *Requirements Impact Assessment* (document 26) is the change-time re-run; the ArchiMate *Requirements Realization view* draws the same matrix as lines — each Requirement (attribute with target) realised by the Application or Technology Service that is its control — and a Requirement with no realisation line is the uncovered row made visible.

*Source note: SABSA framework as published by the SABSA Institute (open-use with attribution); section numbers refer to the SABSA White Paper and are to be verified against the registered PDF.*
