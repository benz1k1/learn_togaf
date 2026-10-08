---
title: "W172: asset, threat, vulnerability, risk and control as ArchiMate elements"
unit: X3
objectives: ["X3.1"]
refs: ["WP:w172 §3", "WP:w172 §4", "ARCHIMATE §6.2", "ARCHIMATE §6.3", "ARCHIMATE §6.6", "ARCHIMATE §14.2", "ARCHIMATE §4.1", "SABSA §7", "GUIDE:integrating-risk-and-security §5.12"]
reading_minutes: 10
source: authored
status: draft
---
## Why risk needs the motivation aspect

ArchiMate's core elements describe what the enterprise *is* and *does*; the **motivation** elements describe *why*. Risk is a why-question — it is uncertainty about whether goals will be met — so the Open Group white paper W172, *Modeling Enterprise Risk Management and Security with the ArchiMate Language*, models risk concepts mostly as motivation elements, and connects them to the core elements they concern. The TOGAF risk and security guide recommends the same approach for drawing the security content it plants in each phase (WP:w172 §3; ARCHIMATE §6; GUIDE:integrating-risk-and-security §5.12).

W172 does not invent new element types. It uses ArchiMate's **specialization** mechanism: a Risk is an Assessment with a stereotype, a Threat Agent is a Business Actor with a stereotype, and so on. That keeps every risk model exchangeable with any conforming tool while giving the diagram a risk vocabulary (ARCHIMATE §14.2; WP:w172 §3).

## The mapping

| Risk concept (SABSA / ISO vocabulary) | ArchiMate element | Specialization of | Why that element |
|---|---|---|---|
| **Asset** — the thing of value that could be affected | Any core structure element (Business Object, Application Component, Node…) or Resource | — (no stereotype needed) | The asset already exists in the architecture; risk is *about* it |
| **Threat agent** — who or what acts | Business Actor or Business Role | Active structure | An agent is an actor, hostile or not |
| **Threat event** — the act | Business Event (or Application / Technology Event) | Event | An event that may happen and trigger loss |
| **Loss event** — the harm occurring | Event | Event | Triggered by the threat event; the point where value is lost |
| **Vulnerability** — the weakness the threat exploits | Assessment | Assessment | An analysed property of the asset |
| **Risk** — likelihood and impact combined | Assessment | Assessment | The outcome of analysing vulnerability and loss |
| **Risk driver** / concern | Driver | — | What the stakeholder cares about (continuity, reputation, compliance) |
| **Control objective** | Goal | Goal | What the control must achieve |
| **Control measure / security requirement** | Requirement | Requirement | The statement the architecture must satisfy |
| **Security principle** | Principle | — | The governing statement |
| **Control** (implemented) | Core element: Business Process, Application Function, Node, Technology Service… | — | A control *is* a piece of the architecture that realizes the requirement |
| **Risk appetite** | Goal or Constraint on the Driver | — | The target the business accepts |

(WP:w172 §3; ARCHIMATE §6.2, §6.3.)

**Trap:** *risk* and *vulnerability* are both Assessments, but they are not interchangeable. A vulnerability is an assessment *of the asset* ("the API accepts unsigned tokens"); a risk is an assessment *of the consequence* ("account takeover, likely, critical"). Draw them as two elements with an Influence from vulnerability to risk, not as one box (WP:w172 §3; ARCHIMATE §6.2).

## The relationships that hold the pattern together

| From | Relationship | To | Reading |
|---|---|---|---|
| Threat Agent (Actor/Role) | Assignment | Threat Event | The agent performs the act |
| Threat Event | Triggering | Loss Event | If the act succeeds, harm follows |
| Loss Event | Association | Asset | The harm is to this asset |
| Vulnerability (Assessment) | Association | Asset | The weakness belongs to the asset |
| Vulnerability, Loss Event | Influence (+) | Risk (Assessment) | They raise the risk |
| Risk | Influence (−) | Driver / Goal | The risk threatens what the stakeholder wants |
| Control Objective (Goal) | Realization ← | Control Measure (Requirement) | The requirement realizes the objective |
| Control Measure (Requirement) | Realization ← | Control (core element) | The architecture element realizes the requirement |
| Control Measure | Influence (−) | Vulnerability or Risk | The control reduces it |

(WP:w172 §4; ARCHIMATE §5.2, §6.6.)

Read the bottom three rows and the SABSA traceability chain appears in ArchiMate form: attribute (Driver/Goal) → control objective (Goal) → control measure (Requirement) → control (core element). Top-down justification is following Realization arrows upward; bottom-up completeness is checking that every Requirement has a realizing core element (SABSA §7; WP:w172 §4).

## The two-sided extension

SABSA insists risk has an upside. W172's pattern handles it with the sign on Influence: an **opportunity** is an Assessment that influences a Goal *positively*, and an **enhance** control is a Requirement realized by a core element that raises the likelihood of the opportunity. The same elements draw both sides; only the signs and the stereotypes differ, which is a strong argument for modelling risk this way rather than with a separate risk tool (SABSA §7; ARCHIMATE §6.3).

**Trap:** do not model a control as a Requirement *only*. A Requirement is a statement; the control the auditor will test is the process, function or node that realizes it. A risk view with Requirements and no realizing core elements is a wish list — the SABSA bottom-up check would fail it (WP:w172 §4; ARCHIMATE §6.6).

## A Northgate Bank fragment, in words

Asset: *Identity Evidence* (Data Object) held by the Identity Verification Service. Vulnerability (Assessment): "evidence retained beyond 30 days in branch exports". Threat agent: *Insider* (Business Role) assigned to threat event *Bulk export of evidence* (Business Event), triggering loss event *Disclosure of customer identity data*, associated with the asset. Risk (Assessment): "disclosure — occasional, critical", influencing (−) the Driver *Regulatory compliance* and the Goal *Confidential at zero confirmed disclosures*. Control objective (Goal): "no evidence exists outside the verified store after 30 days". Control measure (Requirement): "retention purge with proof". Controls: *Retention purge* (Application Function of the Identity Verification Service) and *Branch file destruction* (Business Process, Compliance signs off) — both Realization to the Requirement, and the Requirement Influence (−) the vulnerability. Every SABSA word in unit S3 has a box; every box has a reason (WP:w172 §4; SABSA §7).

## Drawing it

In Archi, create the specializations once (*Specializations Manager*: Assessment → Risk, Assessment → Vulnerability, Business Event → Threat Event, Business Role → Threat Agent, Goal → Control Objective, Requirement → Control Measure) and use a **Motivation** view with the affected core elements dragged in; ArchiMate's Motivation viewpoint permits core elements that motivation elements relate to, so the asset and the control sit on the same diagram as the risk (ARCHIMATE §C.2, §14.2).

## Check yourself

- Which ArchiMate element models vulnerability, and which models risk? Why two?
- What realizes a control measure, and why must the realizing element be shown?
- How does the pattern express an opportunity and an enhance control?
