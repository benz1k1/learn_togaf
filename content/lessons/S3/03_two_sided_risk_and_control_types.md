---
title: "Two-sided risk: threat, opportunity and the five control types"
unit: S3
objectives: ["S3.3"]
refs: ["SABSA §4", "SABSA §4.1", "SABSA §4.2", "SABSA §2.2", "GUIDE:integrating-risk-and-security §3.1", "GUIDE:integrating-risk-and-security §3.1.1", "GUIDE:integrating-risk-and-security §5.6"]
reading_minutes: 10
source: authored
status: draft
---
## Risk has two sides

Most security frameworks define risk as the chance of loss. SABSA defines it as the
**uncertainty of outcome**, which can fall either way: a **threat** is the possibility that an
outcome is worse than expected, an **opportunity** the possibility that it is better. The
business takes risks in order to gain, and a security architecture that only reduces the
downside will also reduce the upside — every lock is also a delay. So SABSA's Motivation column
carries both sides from the Contextual layer's "business risk: opportunities and threats" down to
the operational layer's risk management (SABSA §4).

The TOGAF guide takes the same position in its definition of risk: it describes risk in terms of
the effect of uncertainty on objectives, which may be positive or negative, and it cites the SABSA
view that the security architect's job includes enabling the business, not only protecting it
(GUIDE:integrating-risk-and-security §3.1.1).

## Objectives on both sides

At the Conceptual layer the two sides become two kinds of objective. A **control objective**
says what must be achieved to keep a threat within appetite. An **enablement objective** says
what must be achieved to realise an opportunity. Both are derived from business attributes:
*confidential* yields a control objective; *enabling time-to-market* yields an enablement
objective; *available* yields both, because an outage is a threat and round-the-clock service is
an opportunity (SABSA §4.1).

> **Trap.** Opportunity is not "the absence of threat", and enablement is not "a weaker
> control". They are the positive side of the same uncertainty. A question that asks what SABSA
> adds to the conventional risk model wants *opportunity* and *enablement*; a distractor that
> says "SABSA treats risk only as loss" is wrong.

## The five control types

Security services, mechanisms and components exist to move the outcome in the business's
favour. SABSA classifies what they do into five **control types**, one on the opportunity side
and four on the threat side, ordered by when they act relative to the event (SABSA §4.2):

| Control type | Side | When it acts | What it does | Example services |
|---|---|---|---|---|
| **Enhance** | Opportunity | Before and during | Increases the likelihood or the value of a good outcome | Single sign-on that speeds onboarding; digital signature that lets contracts close online; scalable identity service that opens a new channel |
| **Protect** | Threat | Before the event | Reduces the likelihood of a bad outcome, by deterring or preventing it | Access control, encryption, segregation of duties, awareness training, network segmentation |
| **Detect** | Threat | During the event | Discovers that a bad outcome is occurring or has occurred, and notifies | Monitoring, logging, intrusion detection, reconciliation, audit |
| **Recover** | Threat | After the event | Restores the service or asset to its required state | Backup and restore, failover, business continuity, incident response |
| **Correct** | Threat | After the event | Removes the cause so that the event does not recur; adjusts the architecture | Root-cause analysis, patching, policy change, control redesign, lessons learned |

The four threat-side types together form a **layered** strategy: prevent what you can, detect
what you cannot prevent, recover from what you detect, correct so it does not happen again. No
single type is sufficient; a design that has only protective controls has no way of knowing it
has failed. The Blue Book's older multi-tiered control strategy (deter, prevent, contain, detect
and notify, evidence and track, recover and restore, assure) is a finer-grained version of the
same threat-side sequence (SABSA §4.2).

> **Trap.** *Recover* restores the state; *correct* removes the cause. Backup and failover are
> recovery; patching the vulnerability that was exploited and changing the policy that allowed
> it are correction. The paper describes an action and asks its type — look for "restore" versus
> "prevent recurrence".

> **Trap.** *Enhance* is the only opportunity-side type. Any control described as increasing
> value, speed, reach or revenue is *enhance*, however protective it also happens to be.

## Risk appetite and targets, seen twice

The business's **risk appetite** — how much uncertainty it will bear for the gain it seeks — is
recorded at the Conceptual layer and expressed operationally as the attribute performance targets.
A target of 99.95 % availability *is* an appetite statement: the business accepts up to 0.05 %
outage. A control objective's threshold, a target and an appetite are therefore the same decision
in three vocabularies, and changing one must change the others. When the Manage and Measure phase
reports a measured value, it is comparing the outcome against this appetite (SABSA §4.1).

## Treating risk

Given a risk that exceeds appetite, the treatment options are the conventional four — **avoid**
the activity, **transfer** or share the risk (insurance, contract), **mitigate** it with controls
of the types above, or **accept** it with a recorded decision — with SABSA adding the symmetrical
option on the opportunity side: **exploit** it with enhancing controls. The choice is recorded
against the attribute so that the residual risk can be shown to be within appetite, and the TOGAF
guide's Phase E risk mitigation plan is the same record with the ADM's name
(GUIDE:integrating-risk-and-security §5.6).

## In TOGAF terms

The SABSA risk model is the content behind TOGAF's risk technique: TOGAF's initial and residual
risk, its classification and mitigation in Phase A and its monitoring in Phase G (see
[F5 lesson 6](/lesson/F5/06_readiness_and_risk)) are the threat side of this lesson with the
ADM's vocabulary. TOGAF does not name enablement objectives or the enhance control type; when a
scenario asks how the security architect contributes to *opportunity*, the answer is SABSA's, and
the guide's enterprise risk management section is where the two frameworks are reconciled
(GUIDE:integrating-risk-and-security §3.1).

*Source note: written from the SABSA framework as published by the SABSA Institute; section numbers refer to the SABSA White Paper and are to be verified against the registered PDF.*
