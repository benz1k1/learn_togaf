---
title: "The Contextual layer: the business view and its six cells"
unit: S2
objectives: ["S2.1"]
refs: ["SABSA §3", "SABSA §3.1", "SABSA §2.2", "GUIDE:integrating-risk-and-security §5.1", "GUIDE:integrating-risk-and-security §5.2"]
reading_minutes: 9
source: authored
status: draft
---
## The business view

The Contextual layer is the top row of the Matrix and is called the **business view**. It
describes the enterprise as the business sees itself, in the business's own language, with no
security vocabulary at all. Its purpose is to establish the *context* in which every later
decision will be justified: what the business does, why it does it, who is involved, where and
when it operates, and what could go right or wrong. A security architect who skips this layer
has nothing to trace to (SABSA §3).

The layer is populated by listening, not by designing. The sources are strategy documents,
business plans, process descriptions, organisation charts, contracts, regulatory obligations and
interviews with the people who own the business outcomes. The TOGAF guide places the same
activity in the Preliminary Phase and Phase A, where business drivers and objectives, the risk
appetite and the key risk areas are captured before any architecture is drawn
(GUIDE:integrating-risk-and-security §5.1).

## The six cells

| Column | Contextual cell | What goes in it |
|---|---|---|
| **Assets (What)** | The business | The business decisions, goals, objectives and assets the enterprise exists to pursue and protect: revenue streams, brand, customer relationships, intellectual property, regulatory licence to operate |
| **Motivation (Why)** | Business risk | The opportunities the business wants to seize and the threats it wants to avoid — the two sides of risk, stated in business terms and prioritised by the business |
| **Process (How)** | Business processes | The value chain: how the business does what it does, the transactions it performs, the information flows those transactions need |
| **People (Who)** | Business governance | The organisation and its relationships: structures, roles, accountabilities, customers, suppliers, partners, regulators |
| **Location (Where)** | Business geography | Where the business operates: countries, sites, jurisdictions, markets, the physical and legal places that shape what is possible and what is required |
| **Time (When)** | Business time dependencies | The business's temporal constraints: trading hours, settlement windows, reporting deadlines, seasonal peaks, contract terms, the lifetimes of assets |

(SABSA §3.1)

## Reading the cells as business drivers

Each cell yields **business drivers**: statements of what the business needs, still free of any
security wording. From the Assets cell come drivers such as "protect the brand" or "retain the
banking licence". From Motivation come "enter the new market before the competitor" and "avoid
regulatory fines". From Process come "settle every trade the same day". From People come
"customers must be able to trust us with their data". From Location come "operate under EU and
Indian law at the same time". From Time come "the payments window closes at 16:00" (SABSA §3.1).

The drivers are the raw material of the next layer. Every business attribute in the Conceptual
layer's profile must be traceable to at least one driver here, and every driver here should map
to at least one attribute — the first link in the two-way traceability chain. Lesson 3 of this
unit walks a driver down that chain (SABSA §2.2).

> **Trap.** The Contextual × Motivation cell is **business risk**, both opportunity and threat.
> The paper likes distractors that put "risk management objectives" (Conceptual), "risk
> management policies" (Logical) or "operational risk management" (Service Management) in the
> Contextual row. Business risk is what the *business* perceives, before the architect has
> turned it into objectives.

> **Trap.** The Contextual × People cell is **business governance** (organisation and
> relationships), not "roles and responsibilities" — that phrase is the Conceptual cell, where
> the architect assigns owners, custodians and users.

## Why the layer matters to the architect

Three consequences follow from a well-populated Contextual layer. First, scope: the geography and
governance cells set the boundaries of the architecture, so that a security domain drawn later
matches a real jurisdiction or organisational unit. Second, priority: the business-risk cell says
which attributes will matter most, so that the profile is weighted by the business and not by the
architect's instincts. Third, language: because every driver is written as the business speaks,
the architect can later show a control's justification to a business owner and be understood
(SABSA §3).

The TOGAF guide's Phase A activity is the mirror of this: the security architect's contribution to
the Architecture Vision is the business drivers, the risk appetite statement and the key risk
areas, expressed so that the sponsor recognises them as their own concerns
(GUIDE:integrating-risk-and-security §5.2).

## In TOGAF terms

The Contextual layer is the Preliminary Phase and the opening of Phase A: the business drivers and
objectives, the organisation model, the scope of the enterprise and the stakeholder concerns that
the Architecture Vision records. In TOGAF the drivers, goals and objectives are Motivation
elements in the content metamodel; in SABSA they are the Contextual row. The Business Attributes
Profile that follows in the Conceptual layer is what those drivers become when the security
architect writes Phase A requirements, which is where the next lesson goes
(GUIDE:integrating-risk-and-security §5.1).

*Source note: written from the SABSA framework as published by the SABSA Institute; section numbers refer to the SABSA White Paper and are to be verified against the registered PDF.*
