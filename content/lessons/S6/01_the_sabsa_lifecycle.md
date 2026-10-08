---
title: "The SABSA Lifecycle: Strategy and Planning, Design, Implement, Manage and Measure"
unit: S6
objectives: ["S6.1"]
refs: ["SABSA §4", "SABSA §2", "SABSA §5", "GUIDE:integrating-risk-and-security §5.9"]
reading_minutes: 8
source: authored
status: draft
---
## Two views of the same framework

The SABSA Matrix is a *static* picture: six layers by six columns, every cell an architectural question to answer. The **SABSA Lifecycle** is the *dynamic* picture: the order in which the cells are filled, built, run and revisited. The two are deliberately aligned — each lifecycle phase maps onto a band of Matrix layers — so that a learner who knows the Matrix already knows most of the lifecycle (SABSA §4, §2).

The lifecycle has four phases, arranged as a loop:

| Phase | What happens | Matrix layers it fills |
|---|---|---|
| **Strategy and Planning** | Understand the business, its drivers and risks; state the security strategy as a Business Attributes Profile with performance targets and a risk appetite | Contextual, Conceptual |
| **Design** | Design the services, domains and trust (Logical), the mechanisms and platforms (Physical), the products and standards (Component), and how they will be run (Service Management) | Logical, Physical, Component, Service Management |
| **Implement** | Build, procure, configure, test and deploy what was designed; hand over to operations | (the built architecture) |
| **Manage and Measure** | Operate the controls, measure attribute performance against target, report, and feed the results back into Strategy and Planning | Service Management, with feedback to every layer |

(SABSA §4.)

**Trap:** Design covers *four* layers, not one. Learners who map "Design = Logical" and "Implement = Physical and Component" have confused *designing* a component (choosing the product and standard, a Design-phase activity) with *installing* it (Implement). Physical and Component are still design layers; Implement is what happens after all the design layers are complete (SABSA §4).

## Strategy and Planning

This phase answers the Contextual and Conceptual questions: what business are we in, what are its assets, what does it want to achieve and what could go wrong or right, and how much risk it will carry. Its signature output is the **Business Attributes Profile** — the business's own requirements for security, each attribute with a metric type, a measurement approach and a performance target — together with the risk appetite and the conceptual frameworks (domain framework, trust framework, risk-management objectives) that the Design phase will refine (SABSA §4, §5).

The phase is where SABSA earns the word *business-driven*: nothing is designed until the business has said, in its own vocabulary, what the architecture must protect and enable (SABSA §1, §5).

## Design

Design walks down the remaining layers. At the Logical layer it defines security services, information assets, domains and their policies, entities and trust relationships, and the calendar of lifetimes. At the Physical layer it turns those into mechanisms, data structures, platforms, procedures and schedules. At the Component layer it selects products, tools and standards. And it designs the Service Management layer alongside — how the controls will be operated, monitored and audited once live — rather than leaving operations to be invented after go-live (SABSA §4, §3.3–3.6).

**Trap:** the Service Management layer is *designed* in the Design phase but *executed* in Manage and Measure. A question asking "in which lifecycle phase is the operational security process designed" wants Design; "in which is it performed" wants Manage and Measure (SABSA §4).

## Implement

Implement builds the design: procurement, development, configuration, integration and testing, followed by transition into service. SABSA says little that is specific about project mechanics here — it expects the enterprise's own delivery method — but it does insist on two things: that what is implemented is *verified against the design* (the start of assurance, unit S7) and that the hand-over to the Service Management layer is planned, so that the measurement loop can begin on day one (SABSA §4, §6).

## Manage and Measure

The fourth phase is the one that distinguishes SABSA from a design-only method. The controls are operated; the attribute metrics defined in Strategy and Planning are *collected*; performance is compared against the targets; and the result is reported to the business. Where a target is missed, or the business or the threat has changed, the finding flows back into Strategy and Planning and the loop begins again (SABSA §4, §5).

This closing loop is the same idea as TOGAF's Phase H: enterprise risk management continuously re-evaluates the architecture against changed threat and opportunity, and governance decides whether the change is minor or warrants a new cycle (GUIDE:integrating-risk-and-security §5.9). Lesson 3 of this unit lines the two loops up side by side.

## The lifecycle as a loop, drawn

```
 Strategy & Planning ──► Design ──► Implement ──► Manage & Measure
         ▲                                              │
         └──────────── attribute metrics, incidents ────┘
```

The arrow that returns is not decorative. Without it the Business Attributes Profile is written once and never tested; with it every performance target is a promise the enterprise checks (SABSA §4).

## Check yourself

- Name the four lifecycle phases in order and the Matrix layers each fills.
- Which phase produces the Business Attributes Profile? Which consumes its metrics?
- Why does Design include the Service Management layer?

*Source note: written from the SABSA framework as published by the SABSA Institute; section numbers refer to the SABSA White Paper and are to be verified against the registered PDF.*
