---
title: "The Conceptual layer: the architect's view, strategy, appetite and policy"
unit: S2
objectives: ["S2.2"]
refs: ["SABSA §3", "SABSA §3.2", "SABSA §2.2", "SABSA §4", "GUIDE:integrating-risk-and-security §5.1", "GUIDE:integrating-risk-and-security §5.2", "GUIDE:integrating-risk-and-security §5.10"]
reading_minutes: 10
source: authored
status: draft
---
## The architect's view

The Conceptual layer is the second row of the Matrix and is the **architect's view**. It
translates the business context into a security *strategy*: what the business needs its assets to
be, what the architecture must therefore achieve, how it will be assured, who will be
accountable, how the enterprise will be divided into domains, and how risk will be managed over
time. It is still free of design detail — no services, no mechanisms, no products — but it is
the first layer written by the architect rather than recorded from the business (SABSA §3.2).

The TOGAF guide places this work at the end of the Preliminary Phase and in Phase A: security
principles, the risk appetite, the business impact analysis and the security resource plan, with
the Business Attribute Profile handled by Requirements Management because it is the requirement
set every later phase consumes (GUIDE:integrating-risk-and-security §5.1).

## The six cells

| Column | Conceptual cell | What goes in it |
|---|---|---|
| **Assets (What)** | Business knowledge and risk strategy | The **Business Attributes Profile**: the taxonomy of attributes the business needs its assets to have, each with a metric and a performance target |
| **Motivation (Why)** | Risk management objectives | **Control objectives** (to reduce threats) and **enablement objectives** (to realise opportunities); the risk appetite that sets how much of each is enough |
| **Process (How)** | Strategies for process assurance | The process-mapping framework and the architectural strategies (for example layered defence, separation of duties, secure-by-design) that will assure the business processes |
| **People (Who)** | Roles and responsibilities | Owners, custodians and users of information; service providers and customers; the accountabilities each role carries |
| **Location (Where)** | Domain framework | The concept of security domains, the policy authorities, and the framework of super-domains and sub-domains that the Logical layer will map |
| **Time (When)** | Time management framework | The through-life risk management framework: how risk is assessed and re-assessed across the lifetime of assets and services |

(SABSA §3.2)

## Strategy, appetite and policy

Three ideas that the exam treats as Conceptual-layer content are easy to confuse with their
neighbours above and below.

**Risk appetite** is the amount and kind of risk the business is willing to bear in pursuit of its
objectives. It is set by the business but *recorded and applied* at the Conceptual layer, because
it is what converts a business risk (Contextual) into an objective with a threshold. SABSA treats
the appetite and the attribute performance targets as the same decision seen twice: the target
says how good an attribute must be, the appetite says how much shortfall is tolerable
(SABSA §4).

**Policy** sits at the boundary between Conceptual and Logical. The *policy architecture* — which
policy authorities exist and what each is responsible for — is Conceptual, because it belongs to
the domain framework. The *policies themselves*, written per domain, are Logical (the Logical ×
Motivation cell). The TOGAF guide draws the same line: risk appetite and security principles are
Preliminary and Phase A, while the security policy architecture is Phase B
(GUIDE:integrating-risk-and-security §5.2).

**Strategy** is the word SABSA uses for the whole layer. A strategy is a stated way of achieving
the objectives that can be tested for coverage: every attribute in the profile should be covered
by an objective, every objective by a process-assurance strategy, and every strategy should have a
role accountable for it (SABSA §3.2).

> **Trap.** The Business Attributes Profile is in the **Assets** column, not Motivation. The
> Motivation cell of this layer holds the *objectives* derived from the profile. A distractor
> that reads "Conceptual × Motivation: Business Attributes Profile" is wrong.

> **Trap.** "Domain framework" (Conceptual × Location) is the *concept* and structure of
> domains. "Domain maps" (Logical × Location) are the *drawn* domains with their inter-domain
> associations. The paper asks which layer the domain *model* belongs to and accepts either
> phrase only when it matches the layer.

## Control and enablement objectives

The Motivation cell is where SABSA's two-sided view of risk first becomes explicit. A **control
objective** states what must be achieved to keep a threat within appetite ("unauthorised
disclosure of customer data is prevented"). An **enablement objective** states what must be
achieved to realise an opportunity ("customers can open an account online within ten minutes").
Both are derived from attributes; both are later met by security services. An architecture that
writes only control objectives has read only half the Contextual risk cell (SABSA §4).

## In TOGAF terms

The Conceptual layer is the second half of Phase A and the requirements it hands to Requirements
Management. Security principles are TOGAF Architecture Principles with a security scope; the
risk appetite is a Phase A input to the risk technique; the Business Attribute Profile is the
requirement set that the TOGAF guide places in Requirements Management so that Phases B to H all
trace to it; the domain framework is the scoping decision that Phase B's security domain model
will draw. The content of this layer becomes the target that the Logical-layer design in Phases
B and C must meet (GUIDE:integrating-risk-and-security §5.10).

*Source note: written from the SABSA framework as published by the SABSA Institute; section numbers refer to the SABSA White Paper and are to be verified against the registered PDF.*
