---
title: "Resource, Capability, Value Stream and Course of Action"
unit: A3
objectives: ["A3.1"]
refs: ["ARCHIMATE §7", "ARCHIMATE §7.1", "ARCHIMATE §7.2", "ARCHIMATE §7.2.1", "ARCHIMATE §7.3", "ARCHIMATE §7.3.1", "ARCHIMATE §7.3.2", "ARCHIMATE §7.3.3", "ARCHIMATE §7.4", "ARCHIMATE §7.5", "ARCHIMATE §3.5"]
reading_minutes: 10
source: authored
status: draft
---
## What the Strategy layer is for

The strategy elements model the strategic direction and choices of the enterprise, as far as they
affect its architecture: how it intends to create value, the capabilities it needs, the resources
behind those capabilities, and how it plans to configure them to reach its aims. Business Layer
elements, by contrast, describe the *operational* organization. The set is deliberately tiny and
more abstract than the business elements: the Strategy layer ignores the active/passive split and
the internal/external split, so it has **no service and no interface** elements (ARCHIMATE §7).

Four elements, one of them structure and three behaviour — with a twist for Course of Action
(ARCHIMATE §7.1):

<figure class="max-w-lg"><img src="/figure/ARCHIMATE:fig-46" alt="Strategy elements metamodel" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 46. Strategy Elements Metamodel (ARCHIMATE)</figcaption></figure>

| Element | Aspect | Icon (top-right) | Definition in short | Naming | Typical mistake |
|---|---|---|---|---|---|
| **Resource** | structure (neither active nor passive) | a bar divided into three segments | an asset owned or controlled by an individual or organization | noun | drawing it with round corners; it is structure, so square |
| **Capability** | behaviour | three small stepped squares | an ability that an active structure element possesses | compound noun or gerund: "Risk Management" | naming it as a process ("Process a claim") |
| **Value Stream** | behaviour | a chevron | a sequence of activities creating an overall result for a customer, stakeholder or end user | verb–noun, active: "Acquire Insurance Product" | confusing it with a business process |
| **Course of Action** | behaviour, but *not* a strategy behaviour element | an arrow into a target | an approach or plan for configuring capabilities and resources to achieve a goal | — | treating it as a goal; it is what the enterprise *decided to do* |

## Resource

Resources are a central idea of strategic management: alongside capabilities they are the
sources of competitive advantage, they are analysed as strengths and weaknesses, and because they
are limited they often decide which strategy, goal or project goes first. They can be *tangible*
(financial and physical assets), *intangible* (patents, brand, culture) or *human* (skills,
collaboration capacity, motivation). In the metamodel a resource is **realized by active and
passive structure elements**, which is why it is classified as structure that is neither active nor
passive (ARCHIMATE §7.2.1).

**Trap:** what aspect is Resource? *Structure* — but not active and not passive. An option that
puts Resource in the behaviour aspect, or that calls it passive structure, is wrong (ARCHIMATE
§7.2.1).

## Capability

Strategy and high-level goals are rarely directly implementable. Capabilities close the gap by
focusing on business outcomes: they give a high-level view of what the organization can do now and
wants to be able to do, and they are *realized* by people, processes, information and technology
that the architecture can then design. A capability may *serve* another capability to say it
contributes to it. Capabilities are **behaviour** because they describe abilities — what the
enterprise can do, now or in future — and the concept matches TOGAF's business capability
(ARCHIMATE §7.3.1).

Capabilities are typically aimed at a goal, and a Grouping can show that a set of core elements
together realizes a capability. For capability-based planning, a *capability increment* — one
version of a capability at a point in time — is modelled with **specialization**, and increments
are aggregated with their realizing elements into **plateaus** to show evolution (ARCHIMATE
§7.3.1).

**Trap:** how is a capability increment modelled? By *specializing* the capability, not by
composing or triggering it (ARCHIMATE §7.3.1).

## Value Stream

A value stream describes how the enterprise organizes activity to create value, and value is
always judged **from the recipient's perspective** — it depends on the customer's perception, not
on cost to produce. That perceived value is modelled with the *Value* element, associated with the
result produced and, optionally, with the stakeholder. Value streams exist at enterprise, business
unit or department level; they compose or aggregate *value stream stages*, which are also Value
Stream elements, and stages are related with **flow** to show value passing from one to the next.
Resources may be **assigned** to a value stream, and capabilities **serve** (enable) it (ARCHIMATE
§7.3.2).

The distinction the exam tests is value stream versus business process:

| | Value Stream | Business Process |
|---|---|---|
| Abstraction | strategic — business model and value proposition | operational — operating model |
| Describes | overall value-creating behaviour, judged by worth to the recipient | the time-ordered sequence for an individual case, with alternatives and decisions |
| Decision points | no | yes, with junctions |
| Realized by | business processes and other core behaviour | — |
| "Enterprise in …" | motion | motion |

Value streams and processes both show the enterprise *in motion*; capabilities and business
functions both show it *at rest*. Stages give a frame for organizing processes, and different parts
of the organization may realize the same stage with different processes (ARCHIMATE §7.3.2).

## Course of Action

A course of action is what the enterprise has **decided to do**: an approach or plan for
configuring some of its capabilities and resources to achieve a goal. It is categorized into
*strategies* (long-term, broad) and *tactics* (shorter-term, narrower) with no hard line between
them (ARCHIMATE §7.3.3). In the metamodel it is behaviour, but it is kept apart from the strategy
behaviour elements because it models a different kind of behaviour with a different set of
relationships (ARCHIMATE §7.1).

## The worked examples

The specification's first example: the goal "increase profit" decomposes into "decrease costs"
and "increase revenue"; the course of action "operational excellence" decomposes into "centralize
IT systems" and "standardize products"; these produce the outcomes "decreased costs" and "loss of
customers", which influence the goals positively and negatively — the reminder that outcomes are
not always what was intended. The courses of action are *realized by* the capabilities "IT
management and operations" and "product management"; resources are *assigned* to the former; and
a Location aggregates the resources at headquarters (ARCHIMATE §7.4).

The second example is a value stream for an insurer: each stage is *served by* capabilities, value
*flows* between stages carrying value items, and the final stage *realizes* a business outcome for
a stakeholder — the pattern the Value Stream viewpoint is built for (ARCHIMATE §7.4).

## Summary

| Element | Definition (restated) |
|---|---|
| Resource | an asset owned or controlled by a person or organization |
| Capability | an ability that an active structure element possesses |
| Value Stream | a sequence of activities creating an overall result for a customer, stakeholder or end user |
| Course of Action | an approach or plan for configuring capabilities and resources to achieve a goal |

(ARCHIMATE §7.5) All four live in the Strategy row of the Full Framework, above the Business
Layer (ARCHIMATE §3.5).
