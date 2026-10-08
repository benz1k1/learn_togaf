---
title: "What SABSA is: a business-driven security architecture framework"
unit: S1
objectives: ["S1.1"]
refs: ["SABSA §1", "SABSA §1.1", "SABSA §1.2", "SABSA §2", "GUIDE:integrating-risk-and-security §2.8", "GUIDE:integrating-risk-and-security §3"]
reading_minutes: 8
source: authored
status: draft
---
## The name and the claim

SABSA stands for **Sherwood Applied Business Security Architecture**. It is a framework and a
method for developing risk-driven enterprise information-security and information-assurance
architectures, and for delivering the security infrastructure that supports critical business
initiatives. The name carries the claim: security architecture is *applied to the business*, not
to the technology. Every security service, mechanism and product must be justified by something
the business wants to achieve, and that justification must be visible and testable (SABSA §1).

The framework is published by the SABSA Institute and is **open-use with attribution**: anyone
may use the framework and its models, provided the source is acknowledged. The training
material, the certification examinations and the SABSA trade marks are not open, which is why
this app rehearses the syllabus rather than reproducing a course. The framework itself was first
presented publicly in 1996 and has been developed continuously since (SABSA §1.1).

## "Business-driven" — what it means in practice

A security architecture is business-driven when the chain of reasoning runs *downward* from the
business, not upward from a product catalogue. SABSA phrases the starting question not as "what
threats do we face?" but as "what does the business need to be true about its information and
processes in order to succeed?" Those needs are captured as **business attributes** (for example
*available*, *confidential*, *reputable*, *compliant*), and everything below them exists to make
an attribute true to a measurable level (SABSA §1.2). The TOGAF Series Guide on integrating risk
and security borrows this idea outright: it treats security as a set of business-level
requirements and reframes the question from "is it secure?" to "does it meet the attributes the
business asked for?" (GUIDE:integrating-risk-and-security §2.8).

> **Trap.** "Business-driven" does not mean "the business writes the security policy". It means
> the *justification* for every control traces to a business requirement. The business owns the
> requirements; the architect owns the traceability.

## The attributes of the framework

The SABSA Institute describes the framework with a short list of characteristics. The SCF paper
asks these as recognition questions, so learn them as a set (SABSA §1.2):

| Characteristic | What it means |
|---|---|
| **Business-driven** | Requirements come from business drivers, expressed as business attributes |
| **Risk-focused** | Risk (both threat and opportunity) is the lens through which requirements are prioritised |
| **Comprehensive** | Covers strategy, design, implementation and operations, across all six columns of the Matrix |
| **Modular** | Each layer, column and domain can be developed and changed independently |
| **Open-use** | Free to use with attribution; not tied to a vendor or a product set |
| **Auditable** | Every decision is recorded with its justification, so an auditor can follow it |
| **Transparent** | The reasoning from driver to control is visible to business stakeholders |
| **Scalable** | Applies to a single system, a business unit, an enterprise or a supply chain |
| **Two-way traceable** | Every control traces up to an attribute; every attribute traces down to controls |

The last row is the one that makes the others possible. **Two-way traceability** means that a
control with no attribute above it is unjustified and should be questioned, and an attribute with
no control below it is a gap that must be closed. This completeness check is what distinguishes
an architecture from a list of good ideas (SABSA §2).

## Layered abstraction and the six views

SABSA organises the architecture into six layers, each a complete architecture at its own level
of abstraction and each written for a different audience: the business, the architect, the
designer, the builder, the tradesman and the facilities (service) manager. The layers are read
top-down when designing and bottom-up when checking completeness. The next lesson gives the
Matrix that results when those six layers are crossed with six questions (SABSA §2).

The TOGAF guide's phase-by-phase treatment is the learner's existing entry point to these ideas:
its Preliminary and Phase A material corresponds to SABSA's top two layers, and its Phase B
material (security policy architecture, domain model, trust framework, risk assessment) is a
Logical-layer design in SABSA's terms. Read
[the guide lesson](/lesson/G_RISK_SECURITY/01_integrating_risk_and_security_phase_by_phase)
alongside this unit, and the TOGAF risk technique in
[F5 lesson 6](/lesson/F5/06_readiness_and_risk) when the risk model comes up in S3
(GUIDE:integrating-risk-and-security §3).

## What SABSA is not

SABSA is not a controls checklist, not a product standard and not a certification of a system.
ISO/IEC 27001 supplies a management system and a control catalogue; NIST and national frameworks
supply control baselines; SABSA supplies the *architecture* that says which of those controls are
needed, why, and how the business will know they are working. The TOGAF guide places SABSA among
those other standards for exactly that reason: it is the one that explains the *why*
(GUIDE:integrating-risk-and-security §2.8).

## In TOGAF terms

SABSA's top two layers, Contextual and Conceptual, are the Preliminary Phase and Phase A of the
ADM: establishing the security architecture capability, the principles, the risk appetite and the
business attributes that become Phase A requirements. The Logical layer is Phases B–C, the
Physical layer C–D, the Component layer D, and the Service Management layer is the Phase G–H
governance loop. The app's crosswalk on each `/adm/{phase}` page shows that mapping, and
this unit's Matrix lesson gives the cell-level detail (GUIDE:integrating-risk-and-security §3).

*Source note: written from the SABSA framework as published by the SABSA Institute; section numbers refer to the SABSA White Paper and are to be verified against the registered PDF.*
