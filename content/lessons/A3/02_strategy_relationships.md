---
title: "Strategy relationships: among the four, to motivation, to the core"
unit: A3
objectives: ["A3.2"]
refs: ["ARCHIMATE §7.1", "ARCHIMATE §7.2.1", "ARCHIMATE §7.3.1", "ARCHIMATE §7.3.2", "ARCHIMATE §7.4", "ARCHIMATE §7.6", "ARCHIMATE §5.7", "ARCHIMATE §B.5", "ARCHIMATE §6.6", "ARCHIMATE §12.2.4"]
reading_minutes: 9
source: authored
status: draft
---
## Three sets of relationships

Strategy elements sit between motivation (why) and the core (how), so their relationships fall into
three groups: among themselves, upward to motivation elements, and downward to core elements. The
metamodel figures show the direct relationships; every element may additionally compose, aggregate
or specialize elements of its own type, and derived relationships are permitted according to
Appendix B (ARCHIMATE §7.1, §5.7).

## Among the strategy elements

| From | To | Relationship | Reading |
|---|---|---|---|
| Resource | Capability | **assignment** | the resource is allocated to the capability |
| Resource | Value Stream | **assignment** | the resource is allocated to the value stream |
| Capability | Value Stream (or a stage) | **serving** | the capability enables the value stream |
| Capability | Capability | **serving** | one capability contributes to another |
| Capability, Resource | Course of Action | **realization** | the capability or resource brings the plan about |
| Value Stream stage | Value Stream stage | **flow** | value passes from one stage to the next |
| Value Stream | Value Stream stages | **composition / aggregation** | stages are value streams too |
| Capability | Capability increment | **specialization** | the increment is a version of the capability |

Resources are assigned to capabilities and to value streams; capabilities serve value streams and
other capabilities; stages are linked by flow and are themselves value stream elements
(ARCHIMATE §7.3.1, §7.3.2). In the specification's example, the courses of action are *realized by*
capabilities, and resources are *assigned to* a capability (ARCHIMATE §7.4).

**Trap:** "Which relationship is permitted from a Capability to a Value Stream?" — **serving**.
"From a Resource to a Capability?" — **assignment**. Swapping the two (a resource *serving* a
capability, a capability *assigned to* a value stream) is the standard distractor. Both are
plausible words; only one is the metamodel's (ARCHIMATE §7.3.2).

**Trap:** a Value Stream is decomposed into stages with **composition or aggregation**, and the
stages are connected with **flow** — not triggering. Triggering models temporal or causal
precedence between processes; value streams are not time-ordered task lists (ARCHIMATE §7.3.2).

## Upward: to motivation elements

Capabilities, value streams, courses of action and resources may **realize** or **influence**
requirements, and through the derivation rules therefore also principles and goals. A course of
action may in addition realize or influence an **outcome**, and indirectly a goal. Capabilities are
typically aimed at achieving a goal, and the specification describes outcomes as the results
produced by capabilities; the worked value-stream example shows a value stream realizing a business
outcome for a stakeholder (ARCHIMATE §7.6, §7.3.1, §7.4).

<figure class="max-w-lg"><img src="/figure/ARCHIMATE:fig-51" alt="Relationships between strategy elements and motivation and core elements" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 51. Relationships Between Strategy Elements and Motivation and Core Elements (ARCHIMATE)</figcaption></figure>

| From | To | Relationship |
|---|---|---|
| Capability / Value Stream / Resource / Course of Action | Requirement (and derived: Principle, Goal) | realization or influence |
| Course of Action | Outcome (and derived: Goal) | realization or influence |
| Value (motivation) | Value Stream or its result | association |
| Stakeholder | Value | association |

(ARCHIMATE §7.6, §7.3.2)

Which of realization and influence to choose follows the general rule: realization when the source
is critical to achieving the target, influence when it merely contributes or counteracts, with a
sign or strength attribute if wanted (ARCHIMATE §6.6).

**Trap:** an option that has a Goal *realizing* a Course of Action has the direction backwards.
Motivation elements are the targets; strategy elements realize or influence them (ARCHIMATE §7.6).

## Downward: from core elements

The core realizes the strategy. **Internal and external behaviour elements** — processes,
functions, interactions, services, in any layer — may **realize** a capability or a value stream.
**Active or passive structure elements** — actors, roles, application components, nodes, business
objects, data objects, artifacts — may **realize** a resource. That last rule is why Resource is
classified as structure that is neither active nor passive (ARCHIMATE §7.6, §7.2.1).

| Core element | Strategy element it may realize |
|---|---|
| Business Process, Business Function, Application Service, Technology Function … | Capability, Value Stream |
| Business Actor, Application Component, Node, Business Object, Data Object, Artifact … | Resource |

Value streams are *typically* realized by business processes, the stages providing a frame within
which different parts of the organization may run different processes (ARCHIMATE §7.3.2). A set of
core elements that together realize a capability can be shown with a Grouping (ARCHIMATE §7.3.1).

**Trap:** can an Application Component realize a Capability? Not directly — a component is
*active structure*, and capabilities are realized by *behaviour*. Assign the component to an
application function and let the function realize the capability, or draw the derived relationship
if the chain is valid (ARCHIMATE §7.6, §5.7). Can an Application Component realize a Resource?
Yes — structure realizes resources (ARCHIMATE §7.6).

## Capability evolution over time

For capability-based planning, a capability increment is modelled as a **specialization** of the
capability, and increments together with the core elements that realize them are aggregated into
a **Plateau** — the Implementation & Migration element for a relatively stable state of the
architecture — to show how the capability evolves (ARCHIMATE §7.3.1, §12.2.4).

## Reading the relationship tables

The metamodel figures deliberately leave out derived relationships to stay legible. Appendix B's
tables list, for every ordered pair of element types, every permitted relationship — direct and
derived — using one letter per relationship type. In the Part 2 open-book exam that table is the
authority; in Part 1 you are expected to know the direct ones above (ARCHIMATE §B.5, §5.7).
