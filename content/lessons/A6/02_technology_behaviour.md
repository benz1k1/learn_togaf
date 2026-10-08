---
title: "Technology behaviour: function, process, interaction, event, service"
unit: A6
objectives: ["A6.2"]
refs: ["ARCHIMATE §10.3", "ARCHIMATE §10.3.1", "ARCHIMATE §10.3.2", "ARCHIMATE §10.3.3", "ARCHIMATE §10.3.4", "ARCHIMATE §10.3.5", "ARCHIMATE §10.9", "ARCHIMATE §C.1.4"]
reading_minutes: 8
source: authored
status: draft
---
## The same pattern, a third time

Technology behaviour follows the pattern of the two layers above: the *external* behaviour of a
node is a technology service; the *internal* behaviour that realizes it is a technology function,
process or interaction (ARCHIMATE §10.3). Because the pattern is identical, the exam tests this
layer mostly by substitution — the same stem it used for application behaviour with "technology"
in place of "application" — and by the elements' specific consumers and passive objects.

<figure class="max-w-lg"><img src="/figure/ARCHIMATE:fig-91" alt="Technology internal behavior elements" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 91. Technology Internal Behavior Elements (ARCHIMATE)</figcaption></figure>

| Element | Aspect | Notation | Definition in plain words | Typical confusion |
|---|---|---|---|---|
| Technology Function | Behaviour (internal) | Green rounded box, chevron icon | A collection of technology behaviour that a technology internal active element can perform | Exposing it directly; it is invisible to users and exposed only through a service |
| Technology Process | Behaviour (internal) | Green rounded box, arrow icon | A sequence of technology behaviours that reaches a specific result | Confusing with function; a process is ordered |
| Technology Interaction | Behaviour (internal) | Green rounded box, double-arrow icon | Collective behaviour performed by two or more technology internal active elements | Assigning a single node to it |
| Technology Event | Behaviour | Green notched box | A technology state change; instantaneous | Giving it duration |
| Technology Service | Behaviour (external) | Green rounded box, rounded-rectangle icon | Explicitly defined, exposed technology behaviour | Confusing with technology interface |

## Function

A technology function is the internal behaviour of a technology internal active structure
element. For whoever uses that element the function is invisible; if it is exposed, that is done
through one or more services. The function abstracts from its implementation (ARCHIMATE §10.3.1).
It may realize technology services; it may access technology passive structure elements; and an
internal active element is assigned to it — the node performs the function. Name it with an
"-ing" verb (ARCHIMATE §10.3.1).

## Process

A technology process is an ordered sequence of technology behaviours reaching a specific result,
likewise invisible to the user of the element performing it and exposed only through services.
It can take passive elements as input and use or transform them to produce other passive
elements as output (ARCHIMATE §10.3.2). It may realize services, other services may serve it, and
an internal active element is assigned to it. Name it with a verb or verb-noun phrase — "boot up
system", "replicate database" (ARCHIMATE §10.3.2).

**Trap — process vs function:** both are internal, both realize services, both are performed by
an assigned node. The difference is the same as in the other layers: a process is a *sequence*
achieving a result; a function is a *collection* of behaviour grouped together. Look for "sequence"
or "series" in the stem for process, "collection" for function (ARCHIMATE §10.3.1, ARCHIMATE §10.3.2).

## Interaction

A technology interaction is the collective behaviour of two or more technology internal active
elements, possibly through their participation in a technology collaboration. It may capture the
communication pattern between them or the joint behaviour needed to realize a service; the detail
belongs in a UML interaction diagram at design time (ARCHIMATE §10.3.3). A collaboration, or two or
more nodes, is assigned to it; it may realize services and be served by them; it may access
artifacts (ARCHIMATE §10.3.3).

## Event

A technology event is a technology state change. It may trigger or interrupt functions and other
behaviour; behaviour may raise events that trigger further behaviour; and the event has no
duration. It may come from outside the organisation or from another device inside it
(ARCHIMATE §10.3.4). A time attribute models schedules — a daily backup. It may trigger or be
raised by a function, process or interaction; may access an artifact or material; may be composed
of other events. Name it with a perfect-tense verb — "message received" (ARCHIMATE §10.3.4).

**Trap:** a technology event may access an artifact *or material*. Material is the physical
passive element, and the event is the only technology behaviour element whose section spells out
both. Do not rule out "material" as an accessed object just because it is not a file
(ARCHIMATE §10.3.4).

## Service

A technology service exposes a node's functionality to its environment, is accessed through one
or more technology interfaces, and may require, use and produce artifacts. It should be
meaningful and useful in its own right to its users — which the specification names as
application components and nodes — and its added value may be modelled as a value element
(ARCHIMATE §10.3.5). Typical technology services are messaging, storage, naming and directory
services; a messaging service may access a file containing a message (ARCHIMATE §10.3.5).

Its relationships: it may serve business elements, application components and technology
behaviour or active structure; it is realized by a function, process or interaction; it is exposed
by a node through the interfaces assigned to it; it may access artifacts; it may consist of
sub-services. Name it with an "-ing" verb or the word "service" (ARCHIMATE §10.3.5).

**Trap — service vs interface:** the service is the *behaviour* offered (storage, messaging); the
interface is the *access point* through which it is reached (a management port, an API endpoint).
The interface is *assigned to* the service; a function *realizes* the service. "Which element is
the point of access for a technology service?" is interface; "which element exposes technology
behaviour?" is service (ARCHIMATE §10.3.5).

**Trap — who does a technology service serve?** Application components and application behaviour
are the usual consumers, but the specification also allows a technology service to serve
*business* elements directly. An option that says "a technology service may only serve
application elements" is too narrow (ARCHIMATE §10.3.5).

## The example

An event "Database Update" triggers a process "Replicate Remote Data", served by a service
"Database Update Replication". That service is realized by a function "Database Replication",
composed of four sub-functions with flows from "Administrate Replication" to the other three.
Triggering, serving, realization, composition and flow between functions appear in one small view
(ARCHIMATE §10.3).

## Where the behaviour elements appear

The technology viewpoint is the composition-category viewpoint for this layer: it holds the
software and hardware elements supporting the Application Layer — devices, networks, system
software — together with technology process/function/interaction, service and event, artifact,
node, collaboration, interface, path, communication network and location. Its stakeholders are
infrastructure architects and operational managers; its concerns stability, security,
dependencies and cost; its purpose designing; its scope single layer, multiple aspects
(ARCHIMATE §C.1.4).

Table 8's one-line definitions for the behaviour elements repeat the application ones with
"technology" substituted, which is why the exam rarely asks the definition alone and instead
asks which layer's element a described piece of behaviour belongs to (ARCHIMATE §10.9).
