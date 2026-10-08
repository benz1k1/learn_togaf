---
title: "Control gap analysis — the two transition architectures"
deliverable: Control gap analysis
phase: E
kind: DELIVERABLE
track: SABSA
summary: "For Transition 1 (Q2 2027) and Transition 2 (Q4 2027), which security services and mechanisms must already exist at each plateau, which are missing today, and the work packages that close each gap — the SABSA Lifecycle's Design-to-Implement step laid on the Roadmap."
refs: ["SABSA §6", "GUIDE:integrating-risk-and-security §5", "GUIDE:integrating-risk-and-security §3", "ADM §9"]
artefacts: []
source: authored
status: draft
---

> **What to notice.** A control gap is timed. The question is not "does the bank have security monitoring" but "does it have it *by the plateau at which the risk it covers goes live*" — a fraud engine in Transition 2 with a SIEM planned for Target is a gap, whatever the target state says. This is the Conceptual × Time and Logical × Time cells: the security strategy's lifetimes and the services' readiness laid against the roadmap's dates. The trap is a gap list without an owner package: a gap that no work package closes is either accepted risk, which the Head of Risk must sign, or a missing work package, which the Roadmap must add. There is no third state.

| | |
|---|---|
| Reference | SEC-GAP-2026-01, version 1.0, 26 August 2026 (Phase E, with the Architecture Roadmap AR-2026-01) |
| Baseline | Controls in place on 1 August 2026, from the Baseline Technology Architecture and the Compliance Officer's audit |
| Owner | Owen Price; accepted risks signed by the Head of Risk |

## What each plateau brings into service, and the controls it therefore needs

| Plateau | Goes live | Attributes exposed | Services that must be operating |
|---|---|---|---|
| **Transition 1** (Q2 2027) | Payments and Card Management APIs (WP-1); Mobile App v4 with transfers and card controls (WP-3); dual-homing and pre-prod (WP-5); SMS gateway retired | Authenticated, Timely, Accurate, Confidential, Auditable, Recoverable, Available | SS-01, SS-02, SS-03, SS-04, SS-05, SS-06, SS-07, SS-08, SS-11, SS-12 (takeover patterns) |
| **Transition 2** (Q4 2027) | Onboarding in app and at the counter (WP-2); scoring before authorisation with analysts in the loop (WP-4) | adds Legal, Fraud-resistant, Usable | adds SS-09, SS-10; SS-12 velocity and vendor-access rules; SS-03 rule-ownership roles |
| **Target** (mid-2028) | Automatic blocking; online site retired; Lending on the API layer | Reputable, Cost-effective at full target | SS-09 without the analyst gate; SS-01 extended to Lending |

## Gap register

| Gap | Service / mechanism | Baseline (Aug 2026) | Needed by | Closure | Work package | Status |
|---|---|---|---|---|---|---|
| G-01 | SS-01 strong customer authentication with device binding | App authenticates with password only; no attestation | Transition 1 | Gateway authorisation server, OAuth 2.1, device attestation in App v4 | WP-1, WP-3 | Planned |
| G-02 | SS-02 mutual service authentication | Direct channel-to-Core-Banking calls with shared passwords | Transition 1 | Internal CA, mTLS on IF-01; remove direct integrations (D1 → D3 denied) | WP-1 | Planned |
| G-03 | SS-07 tamper-evident central logging | Per-application logs, no retention standard | Transition 1 | Logging pipeline, write-once store, 13-month retention, log schema | WP-1 | Planned |
| G-04 | SS-12 security monitoring | None — incidents found by customers or the batch | Transition 1 (takeover rules); Transition 2 (velocity, vendor access) | SIEM on the platform; rule sets per plateau | WP-1, then WP-4 | **Not in Roadmap v1.0** — added as WP-1 scope on 26 August, +£85 k, CFO to confirm |
| G-05 | SS-08 two-hour failover of authorisation | Single-homed card link; manual DR failover | Transition 1 | Dual-homing and pre-prod; DR test before go-live | WP-5 | Planned |
| G-06 | SS-06 non-repudiation of app instructions | None — transfers are branch-executed | Transition 1 | Signed instructions, device key, hash-chained log | WP-3 | Planned |
| G-07 | SS-11 secrets management | HSM exists for cards; application credentials in configuration files | Transition 1 | Secrets manager in platform services; migration of every credential | WP-1 | Planned |
| G-08 | SS-09 real-time scoring, block ≤ 5 s | Overnight batch, next-morning analyst | Transition 2 | Fraud Engine, IF-02, Kafka feed, console | WP-4 | Planned; product by procurement |
| G-09 | SS-10 identity proofing, evidence ≤ 30 days | Teller inspection; evidence photocopied and kept indefinitely | Transition 2 | Verification service, IF-03, purge job; counter retraining; historical evidence disposal | WP-2 | Planned; **disposal of legacy evidence has no package** — accepted as a Compliance Officer action, due Q1 2027 |
| G-10 | SS-03 rule-ownership roles | One "administrator" role in the batch tooling | Transition 2 | Separate block and edit-rule roles in the console; console roles verified at contract | WP-4 | Planned; contract condition |
| G-11 | SS-04 in-country hosting of vendors | No vendor yet | Transition 2 | CN-05 clause in both RFPs | WP-2, WP-4 | Planned |
| G-12 | SS-09 automatic blocking without analyst | Analyst gate by design | Target | Phase H change after six months' evidence from Manage & Measure | Next cycle | Deferred by design |

## Accepted risks at each plateau

At Transition 1, scoring is still the batch, so *Fraud-resistant* remains at baseline for one more quarter; the Head of Risk accepts this because the plateau date is fixed by the card re-issue and WP-4 cannot precede WP-5. At Transition 2, T-01 and T-05 sit above appetite for the six-month analyst period, as document 63 records. Both acceptances are entered in the Roadmap's Implementation Factor catalog as risks with an expiry, so Phase G checks that they lapse rather than linger.

## What this changed in the Roadmap

G-04 and G-09 are the findings: the Roadmap's work package portfolio had no security monitoring and no disposal of legacy evidence, because neither is a requirement in the Vision — both fall out of attributes (*Auditable*, *Legal*) rather than from a stakeholder's stated need. G-04 grew WP-1; G-09 became an action in the factor catalog. That is the Design-to-Implement step of the SABSA Lifecycle doing its job: the security architecture is not a separate roadmap but a check that the one roadmap carries every control the plateaus need.

## In the other frameworks

TOGAF's Phase E holds this inside the *Architecture Roadmap*'s Consolidated Gaps, Solutions and Dependencies matrix and the risk mitigation plan of G152 §5.6; ArchiMate draws it as a *Migration view* — each transition a Plateau, each gap a Gap element between two Plateaus, closed by the Work Package that realises the control's Deliverable.

*Source note: SABSA framework as published by the SABSA Institute (open-use with attribution); section numbers refer to the SABSA White Paper and are to be verified against the registered PDF.*
