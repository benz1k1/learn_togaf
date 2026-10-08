---
title: "SABSA risk assessment — mobile payments and onboarding, two-sided"
deliverable: SABSA risk assessment (two-sided)
phase: A
kind: DELIVERABLE
track: SABSA
summary: "Threats and opportunities for mobile payments and digital onboarding scored as impact × likelihood over the business attributes, with controls typed enhance, protect, detect, recover and correct, feeding the TOGAF risk technique."
refs: ["SABSA §4", "TECH §8", "GUIDE:integrating-risk-and-security §3", "GUIDE:integrating-risk-and-security §5"]
artefacts: []
source: authored
status: draft
---

> **What to notice.** SABSA scores risk over *business attributes*, not over systems: the question is never "how risky is the Mobile App" but "what could happen to *Timely* or *Confidential*, and how badly". Risk is two-sided — an opportunity is a positive outcome the architecture can make more likely, and it gets a score and a control just as a threat does. Controls are then typed by what they do to the outcome curve: **enhance** (make the good outcome likelier), **protect** (make the bad one less likely), **detect** (know it happened), **recover** (restore the attribute), **correct** (stop the recurrence). The trap is a register that is all protect-type controls against threats: it has ignored the reason the programme exists.

| | |
|---|---|
| Reference | SEC-RA-2026-01, version 1.0, 10 April 2026; reviewed at each phase gate |
| Method | Impact 1–5 over the attribute's target, likelihood 1–5 over twelve months; score = impact × likelihood; appetite from document 62 |
| Owner | Owen Price with the Cards Ops Lead and the Compliance Officer; accepted by the Head of Risk |

## Mobile payments (WP-1, WP-3)

| Id | Type | Event | Attribute at risk / gained | I | L | Score | Controls (type) | Residual |
|---|---|---|---|---|---|---|---|---|
| T-01 | Threat | Account takeover through a stolen credential or SIM swap, transfer from the app | Authenticated, Reputable | 5 | 4 | 20 | Strong customer authentication with device binding (**protect**); step-up on new payee or unusual amount (**protect**); fraud scoring of transfers (**detect**); transfer recall and customer refund process (**recover**); rule update after each confirmed case (**correct**) | 8 |
| T-02 | Threat | Payments API unavailable in one data centre | Available, Timely | 4 | 3 | 12 | Active in both data centres (**protect**); synthetic transaction monitoring (**detect**); two-hour failover, tested twice a year (**recover**) | 4 |
| T-03 | Threat | Duplicate transfer after a timeout between the API layer and Core Banking | Accurate | 4 | 3 | 12 | Idempotent transfers on IF-01 (**protect**); daily reconciliation (**detect**); reversal procedure (**correct**) | 4 |
| T-04 | Threat | Customer data read from a channel cache | Confidential | 4 | 2 | 8 | Cache non-authoritative, 15-minute expiry, encrypted (**protect**); access logging (**detect**) | 4 |
| O-01 | Opportunity | 60 % of transfers move to the app, releasing counter and telephone capacity | Usable, Cost-effective | 5 | 3 | 15 | Ten-second end-to-end target and in-app card controls (**enhance**); adoption reporting to the Board (**detect**) | 20 (target) |
| O-02 | Opportunity | Fewer false declines than the batch causes, so genuine sales complete | Usable, Reputable | 3 | 3 | 9 | Score thresholds tuned by Cards Ops without a release (**enhance**); false-decline rate on the console (**detect**) | 12 (target) |

## Digital onboarding (WP-2)

| Id | Type | Event | Attribute at risk / gained | I | L | Score | Controls (type) | Residual |
|---|---|---|---|---|---|---|---|---|
| T-05 | Threat | Synthetic identity passes automated verification, opens a mule account | Legal, Reputable, Fraud-resistant | 5 | 3 | 15 | Document and liveness checks in the bought service (**protect**); same rule set at counter and app (**protect**); new-account velocity monitoring (**detect**); account freeze and report (**correct**) | 6 |
| T-06 | Threat | Identity evidence retained past 30 days or copied to the API layer | Legal, Confidential | 4 | 3 | 12 | Evidence held only in the verification service (**protect**); purge job with evidence count reported monthly (**detect**); purge on finding (**correct**) | 4 |
| T-07 | Threat | Vendor outage stalls onboarding in every channel at once | Available | 3 | 3 | 9 | Counter journey saves state and completes verification later (**recover**); vendor availability in the contract (**protect**) | 4 |
| T-08 | Threat | Vendor support staff access customer evidence | Confidential | 4 | 2 | 8 | No standing vendor credentials, access path documented and threat-modelled (**protect**); access log review (**detect**) | 4 |
| O-03 | Opportunity | Onboarding in ten minutes halves counter time and lifts new-to-bank share | Usable, Cost-effective | 5 | 4 | 20 | Save-and-resume across channels (**enhance**); minutes-per-onboarding measured from activation timestamps (**detect**) | 25 (target) |

Residual scores for threats are after controls; for opportunities the "residual" is the target score the controls are meant to reach. T-01 and T-05 stay above the appetite line (residual > 6) until the analyst-in-the-loop period ends, which is why the appetite statement allows them for six months and no longer.

## How this feeds the TOGAF risk technique

TOGAF's risk management technique (TECH §8) classifies each risk, records initial and residual levels, and carries the mitigation into the Roadmap and the Implementation Factor catalog. The rows above are that technique with SABSA's two additions: the attribute column, which is what lets a mitigation be traced to a business requirement, and the opportunity rows, which the technique's "risk" vocabulary does not naturally hold. G152 §3 describes the same enterprise-risk vocabulary of asset, threat, vulnerability and control that the columns here use. In practice the Architecture Roadmap's Implementation Factor catalog (document 18) lists R-1 analyst acceptance and the scoring timeout policy; both are rows here (T-01's recover control and T-02) seen from the delivery side.

## In the other frameworks

TOGAF's *Risk Management* technique and the Business Risk Model/Risk Register of G152 §5.3 hold the same rows without the attribute or the opportunity; ArchiMate draws each row with the W172 pattern — an *Assessment* for the threat or opportunity, associated with the *Driver* (attribute) it affects, and the control as a *Requirement* realised by a core element.

*Source note: SABSA framework as published by the SABSA Institute (open-use with attribution); section numbers refer to the SABSA White Paper and are to be verified against the registered PDF.*
