---
title: "Tracing a business driver to a business attribute"
unit: S2
objectives: ["S2.3"]
refs: ["SABSA §3", "SABSA §3.1", "SABSA §3.2", "SABSA §3.3", "SABSA §2.2", "GUIDE:integrating-risk-and-security §5.1", "GUIDE:integrating-risk-and-security §5.10"]
reading_minutes: 9
source: authored
status: draft
---
## The first link in the chain

SABSA's promise of two-way traceability begins with a single step: a **business driver** in the
Contextual layer is turned into one or more **business attributes** in the Conceptual layer. Get
this step right and every later decision — objective, policy, service, mechanism, product — has a
business justification it can point to. Get it wrong and the architecture is a well-organised
list of controls with no owner. This lesson walks the step with worked examples, because the SCF
paper tests it as a matching exercise: given a driver, which attribute; given an attribute, which
driver (SABSA §3.3).

## The procedure

| Step | Question the architect asks | Output |
|---|---|---|
| 1 | What does the business say it needs? (Contextual cells) | A business driver in the business's words |
| 2 | Which of the business's assets, processes, people, places or times does the driver concern? | The Contextual cell it belongs to |
| 3 | What must be *true* about those things for the driver to be satisfied? | Candidate attributes, chosen from the taxonomy |
| 4 | Which attributes does the business actually care about, and how much? | The selected attributes, weighted by the business risk cell |
| 5 | How will the business know the attribute is true? | A metric, a measurement approach and a performance target for each |

Steps 1 and 2 belong to the Contextual layer; steps 3 to 5 are the Conceptual layer's Assets cell
being filled. The output of step 5 is the row in the Business Attributes Profile that S3 examines
in detail (SABSA §3.2).

## Worked examples

**Driver: "Customers must be able to pay online at any hour."** This is a Process driver with a
Time dependency. The things that must be true: the payment service is **available** around the
clock; payments are **accurate**; the customer's card details are **confidential**; the payment is
**non-repudiable** so that disputes can be settled. Four attributes, from the operational, user and
risk-management families. Performance targets follow: availability 99.95 % measured monthly from
service logs; accuracy zero unreconciled payments per day; confidentiality no card data outside
the tokenised zone, verified by quarterly audit (SABSA §3.3).

**Driver: "Retain the banking licence."** An Assets driver from the Contextual layer's first cell.
Attributes: **compliant** with the regulator's rules, **auditable** so that compliance can be
demonstrated, **regulated** in the sense of operating within the licence conditions. The
performance target for *auditable* might be "every regulated transaction reconstructable from
records within 24 hours", measured by a sampled audit test twice a year (SABSA §3.3).

**Driver: "Enter the new market before the competitor."** A Motivation driver on the
*opportunity* side of the risk cell. The attributes are enablement attributes: **enabling
time-to-market**, **business-enabled**, **flexible** and **scalable**. This driver produces
enablement objectives at the Conceptual × Motivation cell, not control objectives, and the
services designed for it will be of the *enhance* type. An architect who only knows how to derive
protective attributes cannot trace this driver at all (SABSA §3.3).

> **Trap.** A driver is not an attribute. "Protect the brand" is a driver; "reputable" is the
> attribute; "no security incident reported in the press in any quarter" is the performance
> target. The paper gives one of the three and asks which layer or which cell it belongs to:
> driver → Contextual, attribute and target → Conceptual × Assets.

## Checking the trace both ways

Top-down, every driver must reach at least one attribute; a driver with no attribute is a
business need the architecture has ignored. Bottom-up, every attribute in the profile must be
traceable to at least one driver; an attribute with no driver is the architect's preference
dressed as a requirement and will not survive a budget review. The check is a matrix of drivers
against attributes with a mark in each justified cell; empty rows and empty columns are the
findings (SABSA §2.2).

The same check is what the TOGAF guide expects Requirements Management to hold: the Business
Attribute Profile is the requirement set, and every phase's security artefact is expected to cite
the attributes it serves. When the guide describes business drivers and objectives in the
Preliminary Phase and the attribute profile in Requirements Management, it is describing this
same trace with the ADM's names (GUIDE:integrating-risk-and-security §5.10).

## Common mistakes

Deriving attributes from threats instead of drivers produces a purely protective profile and
misses every enablement attribute. Choosing attributes the taxonomy offers rather than the ones the
business needs produces a profile of sixty attributes nobody can measure; a working profile is
typically a couple of dozen, chosen and weighted by the business. Writing the target before the
metric produces an unmeasurable requirement. Each of these is a failure of the trace, not of the
taxonomy (SABSA §3.3).

## In TOGAF terms

This lesson is Phase A with a security architect in the room. TOGAF's business drivers, goals and
objectives are recorded in the Architecture Vision; the security architect derives from them the
attribute profile that Requirements Management will carry through the cycle. Phase A's risk
technique (see [F5 lesson 6](/lesson/F5/06_readiness_and_risk)) supplies the initial risk view
that weights the attributes; the guide's Preliminary and Phase A sections describe the same
inputs (GUIDE:integrating-risk-and-security §5.1).

*Source note: written from the SABSA framework as published by the SABSA Institute; section numbers refer to the SABSA White Paper and are to be verified against the registered PDF.*
