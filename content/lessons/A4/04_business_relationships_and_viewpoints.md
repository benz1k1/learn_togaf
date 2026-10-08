---
title: "Business layer relationships, the Organization and Business Process Cooperation viewpoints"
unit: A4
objectives: ["A4.4", "A4.1", "A4.2", "A4.3"]
refs: ["ARCHIMATE §8.1", "ARCHIMATE §8.2", "ARCHIMATE §8.3", "ARCHIMATE §8.4", "ARCHIMATE §5.7", "ARCHIMATE §C.1", "ARCHIMATE §C.1.1", "ARCHIMATE §C.1.10", "ARCHIMATE §C.1.12", "ARCHIMATE §C.1.7"]
reading_minutes: 10
source: authored
status: draft
---
## The relationship pattern of one layer

Every core layer repeats the same three-aspect pattern, and the Business Layer is the one to
learn it on. Read Figure 52 left to right: active structure is *assigned to* behaviour,
behaviour *accesses* passive structure, internal behaviour *realizes* external behaviour (the
service), and the interface is *assigned to* the service it exposes. Composition, aggregation and
specialization between elements of the same type are always allowed even though the figure omits
them (ARCHIMATE §8.1).

<figure class="max-w-lg"><img src="/figure/ARCHIMATE:fig-52" alt="Business Layer metamodel" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 52. Business Layer Metamodel (ARCHIMATE)</figcaption></figure>

| From | Relationship | To | Where it is stated |
|---|---|---|---|
| Business actor | assignment | Business role | ARCHIMATE §8.2 |
| Business role | assignment | Business process / function | ARCHIMATE §8.2 |
| Business collaboration | aggregation | Business role / actor / collaboration | ARCHIMATE §8.2 |
| Business collaboration | assignment | Business interaction | ARCHIMATE §8.2 |
| Business interface | composition (part of) | Business role / actor | ARCHIMATE §8.2 |
| Business interface | assignment | Business service | ARCHIMATE §8.2 |
| Business interface | serving | Business role | ARCHIMATE §8.2 |
| Business process / function / interaction | realization | Business service | ARCHIMATE §8.3 |
| Business event | triggering | Business process / function / interaction (and back) | ARCHIMATE §8.3 |
| Any business behaviour | access | Business object | ARCHIMATE §8.4 |
| Representation | realization | Business object | ARCHIMATE §8.4 |
| Product | aggregation | Services, objects, contract | ARCHIMATE §8.4 |

Two rules of thumb settle most Part 1 relationship questions. First, *assignment* is the
structure-to-behaviour link: who does what, and which interface exposes which service. Second,
*realization* runs from the concrete to the abstract in the same direction every time —
internal behaviour to service, representation to object, and, across layers, function to
capability (ARCHIMATE §8.2, ARCHIMATE §8.3).

**Trap:** an actor is assigned to a role, and a role to a process. Directly assigning an actor to a
process is also permitted in the language, but if a question offers both "actor assigned to role"
and "actor realizes role", only the first exists; realization never links two active-structure
elements (ARCHIMATE §8.2).

## Derived relationships

The metamodel figures say they omit derivable relationships. The derivation rules in §5.7 let a
modeller draw one relationship where a chain of two or more exists: if an actor is assigned to a
role that is assigned to a process, the actor may be shown assigned to the process; if a process
realizes a service that serves another process, the first process may be shown serving the
second. Part 1 asks whether such a derived relationship is permitted, so the answer is "yes, by
derivation" rather than "no, it is not in the figure" (ARCHIMATE §8.1, ARCHIMATE §5.7).

## Viewpoints in one sentence

A viewpoint in ArchiMate selects a subset of elements and relationships for a stakeholder and
the concern they bring. The basic viewpoints of Appendix C are examples, not a normative list,
and each is classified by category — composition, support, cooperation, realization — and by scope
across layers and aspects (ARCHIMATE §C.1). Grouping, junction and or-junction may be used in
every viewpoint even when not listed (ARCHIMATE §C.1).

## Organization viewpoint

The organization viewpoint is the composition-category viewpoint for the enterprise's structure.
It shows the internal organisation of a company, department or network of companies, and it can
be drawn as nested blocks or as a conventional organisation chart. It is used to identify
competencies, authority and responsibilities (ARCHIMATE §C.1.1).

| Organization viewpoint | |
|---|---|
| Stakeholders | Enterprise, process and domain architects; managers; employees; shareholders |
| Concerns | Competencies, authority, responsibilities |
| Purpose | Designing, deciding, informing |
| Scope | Single layer, single aspect |
| Elements | Business actor, business role, business collaboration, location, business interface |

**Trap:** the organization viewpoint contains *no behaviour*. If an option lists "business
process" among its elements, that option is wrong. Its scope is the only single-layer,
single-aspect entry in the basic table — the active-structure aspect of the Business Layer
(ARCHIMATE §C.1, ARCHIMATE §C.1.1).

## Business process cooperation viewpoint

The business process cooperation viewpoint is the cooperation-category view of how processes
relate to each other and to their environment. It serves both high-level process design and an
operational manager's need to see dependencies. Four aspects are named as sub-viewpoints:
causal relationships between the main processes, mapping of processes onto functions,
realization of services by processes, and use of shared data (ARCHIMATE §C.1.10).

| Business process cooperation viewpoint | |
|---|---|
| Stakeholders | Process and domain architects; operational managers |
| Concerns | Dependencies between processes, consistency and completeness, responsibilities |
| Purpose | Designing, deciding |
| Scope | Multiple layers, multiple aspects |
| Elements | Business actor, role, collaboration, location, interface; business process/function/interaction, event, service, object, representation; application component/collaboration, interface, process/function/interaction, event, service; data object |

**Trap:** although its name says "business process", this viewpoint spans multiple layers: it may
include application components and services, because the dependencies of a process on the
applications that support it are one of the things the operational manager wants to see. Do not
pick "single layer" for its scope (ARCHIMATE §C.1.10).

## Two neighbouring viewpoints the exam contrasts

The *service realization* viewpoint looks the other way: it starts from one or more business
services and shows the processes (and possibly application components) that realize them, giving
an outside-in view of processes. Its stakeholders add product and operational managers, and its
concern is the added value of processes (ARCHIMATE §C.1.12). The *product* viewpoint shows the
composition of a product from services and its contract, the interfaces through which it is
offered, and the value it delivers; it belongs to the support category and is used in product
development (ARCHIMATE §C.1.7).

**Trap:** "which viewpoint shows the relationships between business processes and the services
they realize?" — business process cooperation lists that as a sub-viewpoint, but if the stem
starts from the *service* and asks how it is realized, service realization is the intended answer
(ARCHIMATE §C.1.10, ARCHIMATE §C.1.12).
