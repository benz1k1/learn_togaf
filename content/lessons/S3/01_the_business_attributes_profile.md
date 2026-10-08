---
title: "The Business Attributes Profile: the taxonomy and its families"
unit: S3
objectives: ["S3.1"]
refs: ["SABSA §3.3", "SABSA §3.4", "SABSA §2.2", "GUIDE:integrating-risk-and-security §5.10", "GUIDE:integrating-risk-and-security §3"]
reading_minutes: 10
source: authored
status: draft
---
## SABSA's signature idea

A **business attribute** is a quality the business needs its information, systems or services to
possess, stated as a single adjective or short phrase the business would use itself: *available*,
*confidential*, *accurate*, *reputable*, *compliant*. The **Business Attributes Profile** is the
set of attributes chosen for a particular enterprise, system or project, each one carrying a
metric, a measurement approach and a performance target. It sits at the Conceptual × Assets cell
of the Matrix and is the hinge of the whole framework: every driver above it maps down to an
attribute, every control below it traces up to one (SABSA §3.3).

The profile is an *abstraction layer*. Business people do not need to understand encryption to
say they need confidentiality; engineers do not need to understand the market to know that
confidentiality of card data at a stated level is required. The attribute is the word both sides
agree on. The TOGAF guide adopts the profile for precisely this reason and places it in
Requirements Management as the requirement set that every phase consumes
(GUIDE:integrating-risk-and-security §5.10).

## The taxonomy

SABSA publishes a **taxonomy** of attributes — a standard vocabulary, organised into families —
from which a profile is drawn. The taxonomy is a menu, not a checklist: a real profile selects the
attributes the business needs and adds any that are missing. The families and representative
members are (SABSA §3.4):

| Family | What it covers | Example attributes |
|---|---|---|
| **User** | The experience of people using the systems | Accessible, accurate, anonymous, consistent, current, duty-segregated, educated and aware, informed, motivated, protected, reliable, responsive, supported, timely, transparent, usable |
| **Management** | Running and administering the systems | Automated, change-managed, controlled, cost-effective, efficient, maintainable, measured, supportable |
| **Operational** | Day-to-day service delivery | Available, detectable, error-free, interoperable, productive, recoverable |
| **Risk management** | The classic security qualities | Access-controlled, accountable, assurable, auditable, authenticated, authorised, confidential, crime-free, flexibly secure, identified, in our sole possession, integrity-assured, non-repudiable, owned, private, trustworthy |
| **Legal and regulatory** | Obligations imposed from outside | Admissible, compliant, enforceable, insurable, legal, liability-managed, regulated, resolvable, time-bound |
| **Technical strategy** | The long-term shape of the technology | Architecturally open, COTS/GOTS, extendible, flexible and adaptable, future-proof, legacy-sensitive, migratable, multi-sourced, scalable, simple, standards-compliant, traceable, upgradeable |
| **Business strategy** | The long-term shape of the business | Brand-enhancing, business-enabled, competent, confident, credible, culture-sensitive, enabling time-to-market, governable, providing good stewardship and custody, providing investment re-use, providing return on investment, reputable |

> **Trap.** *Confidential*, *integrity-assured* and *available* are three attributes in the
> taxonomy, not the whole of it — and the first two are in the **risk management** family while
> *available* is **operational**. The paper asks family membership: *reputable* is business
> strategy; *compliant* is legal and regulatory; *usable* is user; *recoverable* is operational;
> *scalable* is technical strategy; *auditable* is risk management.

## From taxonomy to profile

Building a profile is a business workshop, not a desk exercise. The architect brings the
taxonomy; the business owners pick the attributes that express their drivers, discard the rest,
and weight the survivors by how much each matters. A profile for a customer payment service might
select fifteen attributes; a profile for an internal reporting tool might select eight. The
taxonomy stays the same across the enterprise so that profiles can be compared and re-used; the
selection changes with the business context (SABSA §3.3).

Each selected attribute is then made **measurable**: the business states how it will know the
attribute is true, and to what standard. Those three columns — metric type, measurement approach,
performance target — are the subject of the next lesson. An attribute without them is a slogan;
with them it is a requirement that can be designed to, tested and reported on (SABSA §3.3).

## Why families matter

The families are more than a filing system. They prompt the architect to look beyond the
security-team reflexes of the risk-management family and ask the business about usability,
cost, legal exposure and strategy. A profile with attributes from only one family is a warning
sign that the Contextual layer was read narrowly. The families also give a first cut at
*ownership*: user attributes are owned by the people who run the business processes, legal
attributes by the compliance function, technical-strategy attributes by the CTO, and so on —
which feeds the Conceptual × People cell (SABSA §3.4).

## The profile and the rest of the Matrix

Because the profile is in the Assets column, it describes what the business's assets must *be*.
The Motivation cell beside it turns each attribute into control and enablement objectives; the
Process cell says how those objectives will be assured; the People cell assigns owners; the
Location cell decides which domains the attribute applies in; the Time cell says when it is
re-assessed. Below, the Logical layer's information-asset inventory classifies each asset by the
attributes it needs, and the security services are chosen to deliver them (SABSA §2.2).

## In TOGAF terms

The Business Attribute Profile is what Phase A requirements look like when a security architect
writes them, and the TOGAF guide places it in Requirements Management so that Phases B to H all
trace to it. In TOGAF's own metamodel the closest concepts are Requirements and Measures; in
ArchiMate they would be drawn as Requirement or Goal elements with Outcome measures. Read
[the guide lesson](/lesson/G_RISK_SECURITY/01_integrating_risk_and_security_phase_by_phase) for
where the profile appears phase by phase (GUIDE:integrating-risk-and-security §3).

*Source note: written from the SABSA framework as published by the SABSA Institute; section numbers refer to the SABSA White Paper and are to be verified against the registered PDF.*
