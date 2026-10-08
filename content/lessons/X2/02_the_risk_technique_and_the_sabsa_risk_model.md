---
title: "G152 and the TOGAF risk technique against the SABSA risk model"
unit: X2
objectives: ["X2.2"]
refs: ["TECH §8", "GUIDE:integrating-risk-and-security §1.2", "GUIDE:integrating-risk-and-security §3.1.1", "GUIDE:integrating-risk-and-security §3.1.2", "GUIDE:integrating-risk-and-security §5.6.1", "GUIDE:integrating-risk-and-security §5.9", "SABSA §5", "SABSA §7", "WP:w117 §3"]
reading_minutes: 9
source: authored
status: draft
---
## Three treatments of one word

TOGAF has a risk *technique*; G152 (the *Integrating Risk and Security* guide) has a risk *process*; SABSA has a risk *model*. They are not rivals, but they are not the same size, and the exams of all three test whether you know which one is in play. The `G_RISK_SECURITY` lesson (`/lesson/G_RISK_SECURITY/01_integrating_risk_and_security_phase_by_phase`) covers the guide phase by phase; the technique has its own page at `/adm/technique/RISK`. This lesson lines the three up (TECH §8; GUIDE:integrating-risk-and-security §1.2; SABSA §7).

| | TOGAF risk technique | G152 guide | SABSA risk model |
|---|---|---|---|
| Scope | Risk to the *architecture project and transformation* | *Enterprise* and *operational* risk, security and privacy | Business risk, two-sided |
| Where | Phases A (identify, classify) and G (monitor) | Every phase, as a cross-cutting concern | Every Matrix layer, the Why column; Operational Risk Management in Service Management |
| Unit of analysis | Risk with initial and residual levels | Risk against risk appetite; risk owners | Business attribute with a performance target; threat *and* opportunity |
| Response | Mitigation to bring risk under residual target | Risk Mitigation Plan: control, transfer, avoid, delay, compensate | Control types: enhance, protect, detect, recover, correct |
| Direction | Loss only | Loss, with security as an enabler of benefit | Loss *and* gain |

(TECH §8; GUIDE:integrating-risk-and-security §1.2, §3.1, §5.6.1; SABSA §7.)

## The TOGAF technique, briefly

The ADM Techniques document treats risk as something the transformation carries: risks are identified in Phase A, classified by *effect* (catastrophic, critical, marginal, negligible) and *frequency* (frequent, likely, occasional, seldom, unlikely), combined into an *initial* level, mitigated to a *residual* level, and then monitored during Phase G. It is a project-risk discipline, and G152 says so explicitly: the technique's risk is *project* risk, and the guide widens the word to operational and enterprise risk (TECH §8; GUIDE:integrating-risk-and-security §1.2).

**Trap:** a TOGAF exam question about "initial and residual risk" is asking about the *technique*, not about SABSA. Do not answer with attributes or two-sided risk; answer with classification, mitigation and monitoring in A and G (TECH §8).

## G152's definition and where it comes from

The guide defines risk in the ISO 31000 sense — the effect of uncertainty on objectives — and builds enterprise risk management on it: risk appetite set in the Preliminary Phase, key risk areas and business impact analysis, a business risk model or risk register in Phase B, the Risk Mitigation Plan in Phase E, and continuous re-evaluation in Phase H. It names SABSA as one of its source standards and adopts SABSA's vocabulary of business attributes and control objectives; what it does *not* carry over is SABSA's explicit two-sidedness — the guide says security *enables* benefit, but it does not model opportunity as a risk with its own controls (GUIDE:integrating-risk-and-security §3.1.1, §3.1.2, §2.8, §5.9).

## The SABSA model

SABSA's model starts from the business attribute. Each attribute has a target; anything that could push performance *below* target is a **threat**, anything that could push it *above* is an **opportunity**; both are risk, because both are uncertainty on an objective. Controls are therefore not only protective:

| Control type | Acts on | Example against the attribute *Available* |
|---|---|---|
| Enhance | Opportunity — increase the upside | Elastic capacity that raises availability beyond target at peak |
| Protect | Threat — reduce likelihood | Redundant hosting |
| Detect | Threat — notice the event | Uptime monitoring with alerting |
| Recover | Threat — restore the target | Tested restore procedure |
| Correct | Threat — fix the cause | Root-cause change after an outage |

(SABSA §7.)

Risk appetite in SABSA is not a separate document; it is the attribute's performance target read from the other side. "Available at 99.9 %" *is* the appetite for downtime. That is why the crosswalk lists RISK_APPETITE beside the Business Attributes Profile in Phase A rather than as a Preliminary-Phase deliverable of its own (SABSA §5, §7; WP:w117 §3).

**Trap:** SABSA's five control types are not the guide's five mitigation strategies. *Control, transfer, avoid, delay, compensate* (G152) are decisions about *what to do with a risk*; *enhance, protect, detect, recover, correct* (SABSA) are *what a control does*. A "transfer" decision (insure) may be implemented by a "recover" control (the payout). Keep the lists apart (GUIDE:integrating-risk-and-security §5.6.1; SABSA §7).

## Reconciling the three

The practical reconciliation W117 and G152 reach is layered:

1. Use the **SABSA model** to *define* risk in business terms — attributes, targets, threats and opportunities — in Phase A and Requirements Management (WP:w117 §3).
2. Use **G152's ERM process** to *manage* it across the ADM — appetite, register, mitigation plan, owners, Phase H re-evaluation (GUIDE:integrating-risk-and-security §3.1.2).
3. Use the **TOGAF technique** to *track the transformation's own risks* — the ones the project creates by changing things — in A and G (TECH §8).

The three then trace: a project risk (technique) that materialises as an outage is an operational risk event (G152) that is a miss against *Available* (SABSA), and the same control appears in all three ledgers under three names.

## A worked line

Northgate Bank's target architecture buys a Fraud Engine. The technique's risk: "vendor integration slips, delaying Transition 1" — initial level critical/likely, mitigated by an early proof of concept to marginal/occasional, monitored in Phase G. G152's risk: "real-time scoring fails open, allowing fraudulent payments" — against appetite, owned by the Head of Payments, mitigated by *control* (fail closed) in the Risk Mitigation Plan. SABSA's attribute: *Accurate* (fraud decisions), target under 0.1 % false negatives, with a **detect** control (score monitoring) and a **correct** control (model retraining), and an **enhance** control — the same engine cutting false positives, which is the opportunity side the other two frameworks do not name (TECH §8; GUIDE:integrating-risk-and-security §5.6.1; SABSA §7).

## Check yourself

- Which framework's risk is project risk, and in which phases does it live?
- List the five G152 mitigation strategies and the five SABSA control types, and say how they differ in kind.
- Where is SABSA's risk appetite recorded?
