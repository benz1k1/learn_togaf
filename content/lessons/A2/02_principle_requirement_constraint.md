---
title: "Principle, Requirement and Constraint"
unit: A2
objectives: ["A2.2"]
refs: ["ARCHIMATE §6.3", "ARCHIMATE §6.3.3", "ARCHIMATE §6.3.4", "ARCHIMATE §6.3.5", "ARCHIMATE §6.3.6", "ARCHIMATE §6.5", "ARCHIMATE §6.6", "ARCHIMATE §3.6", "ARCHIMATE §C.2.2", "ARCHIMATE §C.2.3", "ARCHIMATE §14.2.5"]
reading_minutes: 9
source: authored
status: draft
---
## Ends and means

Goals and outcomes are *ends*. Principles, requirements and constraints are *means*: desired
properties of the solutions that will realize the ends. A principle is a normative guideline that
applies to *all* possible solutions in a context — "data should be stored only once" — while a
requirement applies that guidance to *this* architecture — "use a single CRM system". Both are
statements about properties of systems; they differ in scope and abstraction (ARCHIMATE §6.3).

| Element | Icon | Definition in short | Scope | Typical mistake |
|---|---|---|---|---|
| **Principle** | an exclamation mark in a box | a statement of intent defining a general property that applies to any system in a context | general — every system in the context | writing a principle that names one specific system; that is a requirement |
| **Requirement** | a parallelogram | a statement of need defining a property that applies to a specific system described by the architecture | specific — one system in this architecture | treating a requirement as an end; it is a means to a goal |
| **Constraint** | a parallelogram with an extra bar on the left | a limitation on the architecture, its implementation process, or its realization | restricts *how*, not *what* | modelling "must use vendor X's platform" as a requirement; it prescribes no function, so it is a constraint |

## Principle

The word "system" is used broadly: any active structure, behaviour or passive structure element —
an actor, an application component, a process, a service, an object — is a system, and so is any
grouping of them. Principles resemble requirements in that both define intended properties, but a
principle is broader and more abstract: it applies to every system in a context, whereas a
requirement applies to one system as described. The specification's example is a principle that
information processes comply with law and policy, which is *realized by* the requirements the
specific laws impose on a specific system (ARCHIMATE §6.3.3).

**Trap:** a Principle is realized by Requirements, not the other way round. The more specific
element realizes the more general one, exactly as a data object realizes a business object
(ARCHIMATE §6.3.3, §3.6).

## Requirement

A goal is ultimately achieved by a plan or a concrete change, which may or may not need a new or
changed system. Requirements model the properties those systems must have to achieve the ends the
goals express — they are the means. During design, goals are decomposed until sub-goals are
detailed enough to be realized by properties a system can exhibit; at that point a goal is
*realized by* requirements. The example: "improve portfolio management" can be realized by
either "assign a personal assistant to each customer" (realized by a human actor) or "introduce
online portfolio management" (realized by software), and each requirement decomposes further
(ARCHIMATE §6.3.4).

Constraint is a **subtype** (specialization) of requirement in the metamodel, which is why it
inherits requirement's relationships and why "requirement/constraint" appears as one row in the
viewpoint tables (ARCHIMATE §4.4, §C.2.3).

## Constraint

A constraint restricts how the system operates or how it may be realized, without prescribing
functionality. Three kinds of restriction are named: on the *implementation* (a specific
technology must be used), on the *implementation process* (time or budget), and on the
*functioning* of the system (legal limits) (ARCHIMATE §6.3.5).

**Trap:** "the project must finish by Q3 within 2 M" — is that a Requirement or a Constraint?
Constraint: it limits the implementation process and prescribes no function (ARCHIMATE §6.3.5).
"Customers must be able to view their balance online" prescribes a function — Requirement
(ARCHIMATE §6.3.4).

## How they are realized

The chain, top to bottom, reads: a goal is realized by outcomes; outcomes are realized by
principles; principles are realized by requirements and constraints. The specification's worked
example is worth memorizing in outline: the goal to improve profitability of the service offering
is realized by the outcome of a 10 % profit increase; that outcome is positively *influenced* by
outcomes about revenue and acquisition cost, and negatively by an outcome about technology
spending; the outcomes are *realized by* two principles about serving customers wherever and
whenever; each principle is *realized by* two requirements about mobile platforms and browsers;
and one outcome is realized by a principle that is in turn realized by a *constraint* — build with
cross-platform frameworks (ARCHIMATE §6.3.6).

Below the motivation aspect, a **requirement** (and, indirectly, a principle, outcome or goal)
may be *realized* directly by a structure or behaviour element — an application component realizes
a requirement. The weaker *influence* relationship is also allowed from core elements to these
motivation elements (ARCHIMATE §6.6).

| From | To | Relationship |
|---|---|---|
| Outcome | Goal | realization |
| Principle | Outcome or Goal | realization |
| Requirement / Constraint | Principle | realization |
| Requirement / Constraint | Goal | realization (goal refinement into requirements) |
| Core element (actor, process, component…) | Requirement | realization (or influence) |
| Requirement | Requirement | aggregation (refinement into detail) |

(ARCHIMATE §6.3.6, §6.6, §C.2.2, §C.2.3)

**Trap:** which relationship refines a goal into *sub-goals*? **Aggregation**. Which refines a goal
into *requirements*? **Realization**. The Goal Realization viewpoint is built on exactly that
distinction (ARCHIMATE §C.2.2).

## Two viewpoints that carry these elements

The **Goal Realization viewpoint** (purpose: designing, deciding) shows goals refined into
sub-goals by aggregation and into requirements or constraints by realization, with the principles
that guide the refinement; its elements are goal, principle, requirement, constraint and outcome
(ARCHIMATE §C.2.2). The **Requirements Realization viewpoint** (designing, deciding, informing)
shows requirements realized by core elements and refined into more detailed requirements by
aggregation; it admits core elements plus the strategy elements (ARCHIMATE §C.2.3).

## Specializations you may meet

The informative examples specialize Principle as *Business Policy* (a directive not directly
enforceable) and Requirement as *Business Rule* (an enforceable directive) or *Control Measure*
(from the Risk and Security overlay). The exam may ask which parent a business rule specializes:
Requirement (ARCHIMATE §14.2.5).
