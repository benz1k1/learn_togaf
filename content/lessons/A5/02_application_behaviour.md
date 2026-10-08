---
title: "Application behaviour: function, interaction, process, event, service"
unit: A5
objectives: ["A5.2"]
refs: ["ARCHIMATE §9.3", "ARCHIMATE §9.3.1", "ARCHIMATE §9.3.2", "ARCHIMATE §9.3.3", "ARCHIMATE §9.3.4", "ARCHIMATE §9.3.5", "ARCHIMATE §9.5"]
reading_minutes: 9
source: authored
status: draft
---
## External and internal behaviour, again

Application behaviour is described the same way as business behaviour: the *external* behaviour
of a component is an application service, and its *internal* behaviour is the function (or
process or interaction) that realizes the service. A service is an externally visible unit of
behaviour, provided by one or more components, exposed through well-defined interfaces and
meaningful to its environment (ARCHIMATE §9.3). What an interactive program offers through its
user interface is *also* modelled as an application service, exposed by an application-to-business
interface; internal services are exposed by application-to-application interfaces (ARCHIMATE §9.3).

<figure class="max-w-lg"><img src="/figure/ARCHIMATE:fig-75" alt="Application internal behavior elements" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 75. Application Internal Behavior Elements (ARCHIMATE)</figcaption></figure>

| Element | Aspect | Notation | Definition in plain words | Typical confusion |
|---|---|---|---|---|
| Application Function | Behaviour (internal) | Blue rounded box, chevron icon | Automated behaviour that a component can perform | Modelling it in too much detail; the spec warns that leads into design |
| Application Interaction | Behaviour (internal) | Blue rounded box, double-arrow icon | Collective behaviour performed by (a collaboration of) two or more components | Assigning a single component to it; it needs a collaboration or two or more components |
| Application Process | Behaviour (internal) | Blue rounded box, arrow icon | A sequence of application behaviours that reaches a specific result | Confusing it with a function: a process is ordered, a function is a grouping |
| Application Event | Behaviour | Blue notched box | An application state change; instantaneous | Giving it duration; using it where a triggering relationship alone would do |
| Application Service | Behaviour (external) | Blue rounded box, rounded-rectangle icon | Explicitly defined, exposed application behaviour | Confusing service with interface, and "realized by" with "exposed through" |

## Function

A function is the internal behaviour a component needs in order to realize one or more services;
if that behaviour is exposed, it is exposed through services. A function abstracts from how it is
implemented and states only the necessary behaviour (ARCHIMATE §9.3.1). It may realize services;
services of other functions and technology services may serve it; it may access data objects; and
a component is assigned to it, meaning the component performs it. Name it with an "-ing" verb,
such as "accounting" (ARCHIMATE §9.3.1).

**Trap:** the specification says in most cases the internal behaviour of a component is *not*
modelled in much detail in an architecture description, because doing so drags the architect
into design issues. An option that recommends decomposing every function to the operation level
is contradicting the specification (ARCHIMATE §9.3).

## Process

An application process is the ordered counterpart of a business process: a sequence of
application behaviours reaching a specific result, performed by a component to realize a set of
services. To a consumer, human or automated, it is a black box (ARCHIMATE §9.3.3). It may realize
services; other services may serve it; it may access data objects; a component is assigned to it.
Name it with a verb or verb-noun phrase — "general ledger update job" (ARCHIMATE §9.3.3).

## Interaction

An interaction is the collective behaviour of the components in a collaboration, which may include
their communication pattern or the joint behaviour needed to realize a service. Its detail can be
worked out later in a UML interaction diagram (ARCHIMATE §9.3.2). A collaboration of two or more
components is assigned to it; it may realize services; business, application and technology
services may serve it; it may access data objects. Name it as a series of behaviours — "update
customer records" (ARCHIMATE §9.3.2).

**Trap:** from each participating component's point of view an interaction is external
behaviour; from the collaboration's point of view it is internal. Questions that say "internal
to the collaboration as a whole" are describing an interaction, not a function (ARCHIMATE §9.3).

## Event

An application event is an application state change. Functions and other behaviour may be
triggered or interrupted by an event, and may raise events that trigger further behaviour; the
event itself has no duration. Events may come from outside the organisation (an external
application) or from another application inside it (ARCHIMATE §9.3.4). A time attribute can
model a schedule — an event that starts a daily batch process. An event may trigger or be raised
by a function, process or interaction, may access a data object, and may be composed of other
events. Name it with a perfect-tense verb (ARCHIMATE §9.3.4).

## Service

An application service exposes the functionality of components to their environment. It is
accessed through one or more interfaces, realized by one or more functions that the component
performs, and may require, use and produce data objects (ARCHIMATE §9.3.5). It must be meaningful
to the environment — useful in its own right — and its purpose is expressed as a *value* element
associated with it; if that environment includes business processes, the service should have
business relevance (ARCHIMATE §9.3.5).

Its relationships: it may serve business, application and technology behaviour or active
structure; a function or process may realize it; an interface is assigned to it; it may access data
objects. Name it with an "-ing" verb or the word "service" — "transaction processing"
(ARCHIMATE §9.3.5).

**Trap:** three verbs, three relationships. A service is *realized by* a function or process,
*exposed through* an interface (assignment), and *serves* whoever uses it. Distractors permute
these: "the interface realizes the service" and "the function serves the service" are both wrong
(ARCHIMATE §9.3.5).

## The example

"Purchase Travel Insurance" is a function composed of two functions, each realizing a service
("Get Quotation", "Purchase Quoted Insurance"); these functions belong to the "Quotation" and
"Purchase" components. An event "Request for a Quotation" triggers a process "Obtain Travel
Insurance", which the two services serve. Composition of functions, realization of services,
triggering by an event and serving of a process are all present (ARCHIMATE §9.3).

Table 7 supplies the one-line definitions; "automated behavior" (function), "collective
application behavior" (interaction), "sequence of application behaviors" (process),
"application state change" (event) and "explicitly defined exposed application behavior"
(service) are the phrases the exam varies (ARCHIMATE §9.5).
