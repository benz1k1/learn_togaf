---
title: "Card fraud risk as an ArchiMate risk and security view — the W172 pattern"
deliverable: Risk and security view of the mobile-payments fraud risk
phase: A
kind: MODEL
track: ARCHIMATE
summary: "The Open Group's risk and security modelling pattern applied to Northgate's card-fraud risk: asset, threat, vulnerability and risk on the motivation and business layers, the control objective, control requirement and the course of action and capability that realize it."
refs: ["ARCHIMATE §6", "GUIDE:integrating-risk-and-security §3"]
figure: northgate_risk_security.svg
viewpoint: Motivation
artefacts: []
source: authored
status: draft
---

> **What to notice.** ArchiMate has no risk, threat or control element, and The Open Group's guidance is that it does not need them. The W172 pattern reuses the motivation elements (ARCHIMATE §6) with agreed meanings: a **threat** is a Driver, a **vulnerability** and a **risk** are Assessments, a **control objective** is a Goal, a **control requirement** is a Requirement, and the **control measure** is whatever core element realizes it. The Series Guide on integrating risk and security makes the same point for Phase A: risk is a motivation concern before it is a design concern (GUIDE:integrating-risk-and-security §3).

## How to read the view

Top left, the **Cards Operations Lead** is the Stakeholder who cares. The **Threat** — card-not-present fraud on mobile payments — is a Driver associated with the **Asset**, a Business Object: card transactions and the customer funds behind them. The **Vulnerability** is an Assessment of the baseline: fraud is scored overnight and blocked next morning, the fourteen-hour window recorded as SM-04. Threat and vulnerability both **influence** the **Risk** with a `+`: fraud loss index 100 and rising, the R-1 of the readiness assessment.

Then the response, reading downward. The **Control objective** is a Goal — losses down 30%, block within five seconds — and it influences the risk with a `−`: it exists to reduce it. **RQ-02**, the control requirement that every card transaction is scored before authorisation, **realizes** the objective. The **Course of Action** — real-time scoring with an analyst in the loop for six months — realizes the requirement, and the **Capability** "Real-time fraud scoring" realizes the course of action. The Fraud Engine and scoring API on the Phase C views are the same control one layer down.

## Elements

| Element | ArchiMate type | Aspect / layer | Why that type (W172 role) |
|---|---|---|---|
| Cards Operations Lead | Stakeholder | motivation | Who owns the risk |
| Card-not-present fraud | Driver | motivation | Threat: an external condition that motivates action |
| Fraud scored overnight | Assessment | motivation | Vulnerability: an observed weakness in the baseline |
| Fraud loss index 100 and rising | Assessment | motivation | Risk: the assessed consequence of threat meeting vulnerability |
| Card transactions and customer funds | Business Object | passive, Business | Asset: what is at risk |
| Losses down 30%, block within 5 s | Goal | motivation | Control objective |
| RQ-02 score before authorisation | Requirement | motivation | Control requirement — the same RQ-02 as on the Requirements view |
| Real-time scoring with analyst-in-the-loop | Course of Action | behaviour, Strategy | Control measure as a decided approach |
| Real-time fraud scoring | Capability | behaviour, Strategy | Control measure as an ability the bank must acquire |

## Relationships used

| Relationship | Notation | What it says here |
|---|---|---|
| Association (stakeholder — driver; driver — asset; vulnerability — asset) | plain line | Concern, exposure and where the weakness sits |
| Influence `+` (driver, vulnerability → risk) | dashed, open arrowhead | Both make the risk worse |
| Influence `−` (goal → risk) | dashed, open arrowhead | The objective is to reduce the risk |
| Realization (requirement → goal; course of action → requirement; capability → course of action) | dashed, hollow triangle | Each layer of the control makes the one above it real |

## What changed from the TOGAF drawing

There is no TOGAF drawing for this: the Phase A deliverables carry the risk as a row in the readiness assessment (R-1) and the security guide's Phase A concerns as prose. The view is the addition. What it buys is traceability in both directions — from a stakeholder's concern down to a capability the roadmap must deliver, and from RQ-02 on the Requirements view back up to the risk it exists to treat.

## Draw it yourself

1. Create a *Motivation* view; add the Stakeholder, a Driver for the threat and an Assessment for the vulnerability, and give each a `role` property (`threat`, `vulnerability`) so the W172 meaning is recorded.
2. Add the asset as a Business Object and associate the threat and vulnerability with it.
3. Add the risk as an Assessment; draw Influence from threat and vulnerability to it, strength `+`.
4. Add the control objective as a Goal with Influence `−` to the risk, then RQ-02 as a Requirement realizing the goal — drag the existing RQ-02 in rather than duplicating it.
5. Add the Course of Action and the Capability, draw the two realizations, and on the Application Usage view later draw the Fraud Engine realizing the capability — the control is then traceable to a component.
