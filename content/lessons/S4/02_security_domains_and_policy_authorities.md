---
title: "The domain model: security domains, sub-domains, multi-tiered domains and policy authorities"
unit: S4
objectives: ["S4.2"]
refs: ["SABSA §6.3", "SABSA §6.3.1", "SABSA §6.3.2", "SABSA §2.2", "GUIDE:integrating-risk-and-security §5.3.2", "GUIDE:integrating-risk-and-security §5.3.1"]
reading_minutes: 10
source: authored
status: draft
---
## What a security domain is

A **security domain** is a set of elements — people, systems, information, processes, places —
that is subject to a **common security policy** defined and enforced by a **single policy
authority**. The definition has three parts and the exam tests all three: a *set of elements*, a
*common policy*, and *one authority*. Two systems under the same policy but different authorities
are two domains; two under one authority but different policies are two domains; a domain is the
scope of one policy from one authority (SABSA §6.3).

The **policy authority** is the person or body accountable for the domain's policy: it decides
what the policy says, approves exceptions, and is answerable for the domain's risk. Naming the
authority is what makes a domain real. A boundary drawn on a network diagram with nobody
accountable for what crosses it is a segment, not a domain (SABSA §6.3).

Domains may be **logical** (a set of elements grouped by policy regardless of where they sit — all
payment-card data, wherever stored) or **physical** (a set grouped by place — a data centre, a
building, a network segment). Most enterprises need both, overlaid. The TOGAF guide's Phase B
security domain model is this same idea with the ADM's name
(GUIDE:integrating-risk-and-security §5.3.2).

> **Trap.** A SABSA security domain is not a TOGAF architecture domain (Business, Data,
> Application, Technology) and not an ArchiMate layer. It is a policy scope under one authority.
> Cross-framework confusable questions ask exactly this.

## Sub-domains and multi-tiered domains

A **sub-domain** is a domain wholly contained within another (its **super-domain**). The
sub-domain has its own policy authority and its own policy, but that policy must **comply with
the super-domain's policy**: it may be more specific or more restrictive, never contradictory or
more permissive. The super-domain's authority is accountable for the whole; the sub-domain's
authority is accountable for the part. Nesting can continue, producing a **multi-tiered**
domain structure — a hierarchy of policy scopes with a hierarchy of authorities to match
(SABSA §6.3.1).

| Concept | Definition | Example |
|---|---|---|
| Security domain | Elements under one policy from one authority | The bank, under the board's information-security policy |
| Super-domain | A domain that contains other domains | The bank, relative to its business units |
| Sub-domain | A domain inside a super-domain, with a compliant, possibly stricter policy | The card-payments unit, under a PCI-aligned policy that adds to the bank's |
| Multi-tiered domains | Several levels of super- and sub-domains | Bank → business unit → department → project team |
| Peer domains | Domains at the same level with no containment | Two business units side by side |
| Independent domains | Domains with unrelated policy authorities | The bank and a supplier |
| Isolated domain | A domain with no association to any other | An air-gapped test lab |

(SABSA §6.3.1)

> **Trap.** A sub-domain's policy must *comply with* its super-domain's policy. It may add
> restrictions; it may not relax them. A distractor that says a sub-domain "overrides" or "is
> independent of" the super-domain policy is wrong. Independence is the relationship between
> domains with *different* authorities, not between a domain and its parent.

## A worked domain diagram, in prose

Picture the bank as one large rectangle labelled *Bank — policy authority: the Board, via the
CISO*. Inside it, three rectangles side by side: *Retail Banking*, *Card Payments* and *Corporate
Services*, each with its divisional head as policy authority; these are peer sub-domains of the
bank. Inside *Card Payments*, a smaller rectangle *Cardholder Data Environment* whose authority is
the payments security manager and whose policy adds the card-scheme requirements to the bank's —
a third tier. Outside the bank's rectangle, touching its edge, a separate rectangle *Outsourced
Call Centre* with its own board as authority: an independent domain, associated with Retail
Banking by a contract. Across the whole picture, a dotted rectangle *Regulated Data* that cuts
through Retail Banking and Card Payments alike: a logical domain, overlaid on the physical
structure, whose authority is the compliance officer (SABSA §6.3.2).

Reading the diagram answers the design questions: a data flow from the call centre into Retail
Banking crosses an independent-domain boundary and needs an inter-domain agreement; a flow from
Retail Banking into the Cardholder Data Environment moves into a stricter sub-domain and must
meet the stricter policy on entry; a report that draws on Regulated Data in two sub-domains must
satisfy the logical domain's policy as well as each physical domain's (SABSA §6.3.2).

## Policy authorities and the policy architecture

The **policy architecture** is the structure of authorities and policies laid over the domain
model: which authority owns which domain, which policy each publishes, and how each lower policy
demonstrates compliance with the one above. It is Conceptual in its framework (which authorities
exist) and Logical in its content (what each policy says). The TOGAF guide's Phase B security
policy architecture is this structure, and it names the same rule: lower-level policies inherit
from and comply with higher-level ones (GUIDE:integrating-risk-and-security §5.3.1).

## Why domains matter

Domains scope everything else. A policy is written *for* a domain; a service is deployed *in* a
domain; a trust relationship exists *between* domains; an information asset's classification
applies *within* a domain; an entity's privileges are granted *by* a domain's authority. Without
a domain model, none of these has a boundary, and the architecture cannot say where one rule
stops and another starts (SABSA §6.3).

## In TOGAF terms

The domain model is a Phase B artefact in the TOGAF guide — drawn against the organisation, roles
and processes of the Business Architecture — and it scopes the Phase C and D security services
and mechanisms. In the ADM's own vocabulary the nearest idea is the *scope of the enterprise* and
the *architecture partitioning* of the Preliminary Phase: which parts of the organisation are
governed by which architecture. SABSA's domain is narrower and sharper: the scope of one security
policy from one accountable authority (GUIDE:integrating-risk-and-security §5.3.2).

*Source note: written from the SABSA framework as published by the SABSA Institute; section numbers refer to the SABSA White Paper and are to be verified against the registered PDF.*
