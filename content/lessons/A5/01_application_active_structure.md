---
title: "Application active structure: component, collaboration, interface"
unit: A5
objectives: ["A5.1"]
refs: ["ARCHIMATE §9", "ARCHIMATE §9.1", "ARCHIMATE §9.2", "ARCHIMATE §9.2.1", "ARCHIMATE §9.2.2", "ARCHIMATE §9.2.3", "ARCHIMATE §9.5", "ARCHIMATE §3.6"]
reading_minutes: 8
source: authored
status: draft
---
## The Application Layer

Application Layer elements model the Application Architecture: the structure, behaviour and
interaction of the enterprise's applications. The layer is drawn in blue and, wherever it made
sense, its metamodel copies the Business Layer's, so the three-aspect pattern you learned in A4
applies unchanged (ARCHIMATE §9, ARCHIMATE §9.1). The exam reproduces Figure 70 in fragments and
asks which relationship belongs on a missing arrow (ARCHIMATE §9.1).

<figure class="max-w-lg"><img src="/figure/ARCHIMATE:fig-70" alt="Application Layer metamodel" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 70. Application Layer Metamodel (ARCHIMATE)</figcaption></figure>

## The active-structure family

The main active-structure element is the application component, and it is used for *any*
structural entity at this level: a reusable software component, a whole application, a
sub-application or an information system. It resembles a UML component but models strictly the
structural side; behaviour is attached through an explicit relationship to a behaviour element
(ARCHIMATE §9.2). Application collaboration captures cooperating components, and application
interface is the logical channel through which a component's services are reached. The
interface may be application-to-application (exposing internal services) or
application-to-business, including a user interface (exposing external services) (ARCHIMATE §9.2).

<figure class="max-w-lg"><img src="/figure/ARCHIMATE:fig-71" alt="Application internal active structure elements" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 71. Application Internal Active Structure Elements (ARCHIMATE)</figcaption></figure>

| Element | Aspect | Notation | Definition in plain words | Typical confusion |
|---|---|---|---|---|
| Application Component | Active structure (internal) | Blue box, component icon (two small tabs) | A modular, replaceable encapsulation of application functionality, aligned to how it is implemented | Using it for behaviour: a component *performs* functions, it is not one |
| Application Collaboration | Active structure (internal) | Blue box, two overlapping circles | An aggregate of two or more components (or collaborations) that work together to perform collective behaviour | Thinking it must exist as a real thing; it is usually logical or temporary |
| Application Interface | Active structure (external) | Blue box, lollipop icon | A point of access where application services are made available to a user, another component or a node | Confusing interface (where) with service (what) |

### Application component

A component is a self-contained unit that is independently deployable, reusable and
replaceable. It performs one or more application functions, encapsulates its behaviour and data,
exposes services and makes them available through interfaces; cooperating components are
connected through collaborations (ARCHIMATE §9.2.1). It is *assigned to* the functions it
performs; it *has* interfaces (composition), and interfaces of other components may *serve* it.
Name it with a noun (ARCHIMATE §9.2.1).

The element covers entire applications — deployed, operational IT systems in TOGAF's sense —
as well as their parts, at every level of detail. A component may also *realize* another
component, which is how a more concrete component is shown implementing a more abstract one
(ARCHIMATE §9.2.1, ARCHIMATE §3.6).

**Trap:** "the application component realizes the application service" is wrong. The component
is assigned to a *function*, and the function realizes the service. The component is only
indirectly connected to the service (a derivable relationship), and the exam expects you to
name the direct one (ARCHIMATE §9.2.1).

### Application collaboration

A collaboration says which components or other collaborations cooperate to perform a task. Their
collective behaviour, including their communication pattern, is an application interaction.
Collaborations usually model a logical or temporary grouping that has no separate existence in
the enterprise (ARCHIMATE §9.2.2). Formally it is a specialization of application internal active
structure element that aggregates two or more components or collaborations; it may be assigned
to interactions or other internal behaviour; an interface may serve it and it may be composed of
interfaces. Name it with a noun (ARCHIMATE §9.2.2).

### Application interface

An interface says how a component's functionality can be reached by other elements, and it
exposes application services to the environment. One service may be reachable through several
interfaces and one interface may expose several services (ARCHIMATE §9.2.3). It amounts to a
contract the providing component must honour — parameters, protocols, pre- and post-conditions,
data formats. Structurally it may be part of a component through composition, it may serve other
components, and it is *assigned to* the services it exposes. Name it with a noun (ARCHIMATE §9.2.3).

**Trap:** the interface definition names three kinds of consumer — a user, another application
component, or a *node*. That last one is the technology-layer consumer, and distractors drop or
swap it. Also note the interface may serve a business role or business collaboration, which is one
of the cross-layer serving relationships of Chapter 11 (ARCHIMATE §9.2.3).

## The example

An "Online Travel Insurance Sales" collaboration aggregates the "Quotation" and "Purchase"
components and provides a "Web Services Interface" that serves a third component, "Travel
Website". Aggregation into a collaboration, composition of an interface, and an interface serving
a component are the three relationships to recognise (ARCHIMATE §9.2).

## Summary table

Table 7 restates the definitions; for the active-structure rows the marker words are
"encapsulation ... modular and replaceable" (component), "aggregate of two or more ... collective
application behavior" (collaboration) and "point of access ... user, another application
component, or a node" (interface) (ARCHIMATE §9.5).
