---
title: "Metric types, measurement approaches and performance targets"
unit: S3
objectives: ["S3.2"]
refs: ["SABSA §3.3", "SABSA §3.5", "SABSA §5.1", "GUIDE:integrating-risk-and-security §5.10", "GUIDE:integrating-risk-and-security §5.8"]
reading_minutes: 9
source: authored
status: draft
---
## Making an attribute measurable

An attribute earns its place in the profile only when the business can say how it will be
measured and what result counts as success. SABSA records three things against each attribute:
a **metric type**, a **measurement approach** and a **performance target**. Together they turn an
adjective into a requirement that can be designed to, tested against and reported on, and they
are what the Service Management layer measures in the Manage and Measure phase of the Lifecycle
(SABSA §3.5).

## Metric type: hard or soft

The **metric type** says what kind of measure the attribute admits. A **hard** metric is
quantitative and objective: it is counted or timed from records and two observers would agree on
the number. A **soft** metric is qualitative and subjective: it is assessed by judgement, survey,
opinion or expert review, and reasonable observers may differ. Neither is better; the point is to
declare which kind is being used so that nobody mistakes a survey score for an audit count
(SABSA §3.5).

| Attribute | Metric type | Why |
|---|---|---|
| Available | Hard | Uptime and outage minutes are read from service logs |
| Accurate | Hard | Reconciliation errors are counted |
| Confidential | Hard or soft | Breach count is hard; assessed exposure of a design is soft |
| Usable | Soft | Assessed by user survey or task-completion study |
| Reputable | Soft | Judged from press, customer sentiment, analyst reports |
| Compliant | Hard | Audit findings are counted against a defined rule set |
| Auditable | Hard | Reconstruction of a sampled transaction succeeds or fails |
| Educated and aware | Soft, with a hard proxy | Awareness is judged; training completion is counted |

## Measurement approach

The **measurement approach** says *how* the metric is obtained: the source of the data, the
method, the frequency and who performs it. It is the difference between "we will measure
availability" and "availability is the percentage of one-minute intervals in each calendar month
in which the service responded to the synthetic probe, reported by the operations team on the
first working day of the following month". A good approach is repeatable by someone other than
its author and is cheap enough to run at the stated frequency (SABSA §3.5).

Typical approaches include reading system logs and monitoring data; reconciling records;
sampling and testing transactions; independent audit or penetration test; user or customer
survey; expert assessment against a maturity scale; and counting incidents or findings over a
period. Each approach carries a frequency (continuous, daily, monthly, annually) and an owner.

## Performance target

The **performance target** is the level at which the business declares the attribute
satisfied. It is stated in the units of the metric: "99.95 % of one-minute intervals", "zero
unreconciled payments per day", "no critical audit findings", "customer satisfaction 4.2 of 5 or
above". The target is agreed with the business, not set by the architect, because it is a
statement of risk appetite in disguise: the gap between the target and perfection is the
shortfall the business is prepared to tolerate (SABSA §3.3).

> **Trap.** Metric type answers "what kind of measure" (hard or soft); measurement approach
> answers "how and how often is it measured"; performance target answers "what level is good
> enough". The paper presents one of the three in a scenario and asks which it is. A percentage
> or a count with a threshold is a **target**; "monthly from the audit log" is an **approach**;
> "quantitative" or "qualitative" is a **type**.

## Targets, appetite and traceability

Because the target expresses appetite, it is the point at which the business risk of the
Contextual layer meets the design of the Logical layer. A control objective is derived from an
attribute *and* its target: "confidentiality of card data" alone gives no design guidance;
"confidentiality of card data with zero exposures outside the tokenised zone, verified
quarterly" tells the designer what services and mechanisms are needed and tells the auditor what
to check. Targets are therefore revisited whenever the appetite changes, and the measured results
in the Manage and Measure phase are the evidence that feeds the next Strategy and Planning cycle
(SABSA §5.1).

## Worked profile row

| Attribute | Family | Metric type | Measurement approach | Performance target |
|---|---|---|---|---|
| Available | Operational | Hard | Synthetic probe every minute; monthly report by operations | 99.95 % of intervals per month |
| Non-repudiable | Risk management | Hard | Sampled transaction test by internal audit, quarterly | 100 % of sampled transactions carry a verifiable signature |
| Usable | User | Soft | Customer survey after each release | Mean score 4.2 of 5 or above |
| Reputable | Business strategy | Soft | Media and sentiment review by communications, monthly | No adverse security story in mainstream press in the quarter |
| Compliant | Legal and regulatory | Hard | External audit against the regulator's rule set, annually | Zero critical findings |

(SABSA §3.5)

## In TOGAF terms

Performance targets are the measures that TOGAF's Requirements Management carries for each
requirement and that Phase G's implementation governance checks against the Architecture
Contract; the TOGAF guide describes the security audit in Phase G as the point at which the
attributes are verified. In TOGAF's metamodel a target is a Measure attached to a Requirement or
Objective; in SABSA it is a column in the profile. Both agree that a requirement without a
measure cannot be governed (GUIDE:integrating-risk-and-security §5.8).

*Source note: written from the SABSA framework as published by the SABSA Institute; section numbers refer to the SABSA White Paper and are to be verified against the registered PDF.*
