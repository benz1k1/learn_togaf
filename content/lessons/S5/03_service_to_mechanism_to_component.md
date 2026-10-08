---
title: "From service to mechanism to component: the three-step drop"
unit: S5
objectives: ["S5.3"]
refs: ["SABSA §3.3", "SABSA §3.4", "SABSA §3.5", "SABSA §6", "GUIDE:integrating-risk-and-security §5.4.1", "GUIDE:integrating-risk-and-security §1.3"]
reading_minutes: 9
source: authored
status: draft
---
## Three layers, one thread

SABSA's design layers are not three separate documents; they are one thread pulled through three levels of abstraction. A **security service** (Logical) is delivered by one or more **security mechanisms** (Physical), each of which is realised by one or more **components** — products, tools, standards (Component). The thread is what makes the architecture traceable: pick any component and you should be able to walk up to a service, and from the service up to the business attribute that justifies it (SABSA §3.3, §6).

TOGAF learners already know this shape. An Architecture Building Block is refined into a specification and implemented by a Solution Building Block; SABSA's service → mechanism → component is the same drop with security vocabulary. The TOGAF risk and security guide even insists that security services are *ABBs*, listed in a Security Services Catalog, and not items on a controls checklist (GUIDE:integrating-risk-and-security §5.4.1, §1.3).

## The three definitions

| Term | Layer | Definition | Test question |
|---|---|---|---|
| Security service | Logical | A capability the architecture provides, described by *what* it does for the business, independent of how | Could two different technologies deliver it? Then it is a service. |
| Security mechanism | Physical | The means by which a service is delivered: a technique, a data structure, a procedure, a timing rule | Is it technology-specific but still vendor-neutral? Then it is a mechanism. |
| Component | Component | The product, tool, protocol or standard that realises a mechanism | Could you buy it, download it or cite it by number? Then it is a component. |

(SABSA §3.3–3.5.)

**Trap:** the relationship is many-to-many at each step. "Confidentiality in transit" (service) may be delivered by transport encryption *and* by a private network (two mechanisms); transport encryption (mechanism) may be realised by a gateway product *and* a library *and* a cryptographic standard (three components). Questions that say "each service maps to exactly one mechanism" are describing something SABSA does not claim (SABSA §3.3).

## A worked trace

Take one attribute from a Business Attributes Profile and follow it all the way down.

| Level | Content | Matrix cell |
|---|---|---|
| Business attribute (Conceptual) | *Confidential* — customer identity evidence is seen only by authorised staff; target: zero confirmed disclosures per year | Conceptual × Motivation |
| Security service (Logical) | Access control to identity evidence; confidentiality in storage; audit of access | Logical × Process |
| Security mechanism (Physical) | Role-based access control at the application; encryption at rest with segregated key management; access logging with tamper-evident storage | Physical × Process |
| Component | Identity-provider product with its role catalogue; storage-encryption feature at a named key length under a named standard; log-management tool with write-once retention | Component × Process, × Motivation |
| Service management | Role recertification each quarter; key rotation each year; log review each week | Service Management × Time |

(SABSA §3.3–3.6.)

Read the table upward and each row *justifies* the one below it: the log tool exists because logging is a mechanism, which exists because audit is a service, which exists because the attribute *Confidential* carries a measurable target. Read it downward and each row *completes* the one above: if the attribute were listed without a service, or the service without a mechanism, the profile would be a wish, not an architecture. Unit S7 names these two readings top-down justification and bottom-up completeness (SABSA §6).

## Why the drop matters in practice

**Substitution without redesign.** When a product reaches end of life, the change is contained at the Component layer: the mechanism it realised is unchanged, so the service and the attribute remain satisfied once an equivalent component is proven (SABSA §3.5).

**Reuse with verification.** The TOGAF guide's Phase E advice — reuse an existing security service only after its efficacy is verified — is the drop applied in reverse: does the existing component still realise the mechanism the new service needs, at the performance the attribute demands? (GUIDE:integrating-risk-and-security §5.6.)

**Costed justification.** Because every component traces to an attribute with a performance target, spend can be argued in business terms: "this HSM is what *Confidential* at zero disclosures costs". That is what SABSA means by business-driven (SABSA §1, §6).

**Trap:** do not put the *mechanism* in the Logical layer because it "seems logical". Encryption is a mechanism; *confidentiality* is the service. The Logical layer describes services in terms a business analyst could read; anything that names a technique has already dropped to Physical (SABSA §3.3, §3.4).

## Relating the drop to the ADM

| ADM phase | What the drop looks like there |
|---|---|
| C | Security services in the Security Services Catalog; application-level mechanisms chosen (GUIDE:integrating-risk-and-security §5.4.1) |
| D | Platform and network mechanisms; technology components identified (§5.5) |
| E | Security ABBs become SBBs; reuse verified; Risk Mitigation Plan (§5.6) |
| G | Compliance review checks the implemented component against the designed mechanism (§5.8) |

The crosswalk panels on `/adm/C`, `/adm/D` and `/adm/E` show the same placement.

## Check yourself

- Give a service, a mechanism that delivers it and a component that realises the mechanism.
- Why does SABSA insist the relationship is many-to-many?
- Which TOGAF concept does each of the three levels correspond to?

*Source note: written from the SABSA framework as published by the SABSA Institute; section numbers refer to the SABSA White Paper and are to be verified against the registered PDF.*
