---
title: "Business behaviour: process, function, interaction, event, service"
unit: A4
objectives: ["A4.2"]
refs: ["ARCHIMATE §8.3", "ARCHIMATE §8.3.1", "ARCHIMATE §8.3.2", "ARCHIMATE §8.3.3", "ARCHIMATE §8.3.4", "ARCHIMATE §8.3.5", "ARCHIMATE §8.6"]
reading_minutes: 10
source: authored
status: draft
---
## External and internal behaviour

The behaviour aspect of the Business Layer is built on one design decision borrowed from
service orientation: separate what an organisation shows to the outside (its *external*
behaviour) from how it does it (its *internal* behaviour). External behaviour is the business
service; internal behaviour is the process, function or interaction that realizes it
(ARCHIMATE §8.3). A service may be offered to outside customers, or it may be an internal
service that supports other processes inside the organisation (ARCHIMATE §8.3).

<figure class="max-w-lg"><img src="/figure/ARCHIMATE:fig-58" alt="Business internal behavior elements" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 58. Business Internal Behavior Elements (ARCHIMATE)</figcaption></figure>

| Element | Aspect | Notation | Definition in plain words | Typical confusion |
|---|---|---|---|---|
| Business Process | Behaviour (internal) | Yellow rounded box, arrow icon | A sequence of behaviours that reaches a defined result, such as a product or service | Confusing it with a function: a process is ordered by flow, a function by skills and resources |
| Business Function | Behaviour (internal) | Yellow rounded box, chevron icon | A grouping of behaviour by criteria such as required resources or competencies, managed as a whole | Confusing it with a capability: a function is current, organisation-aligned behaviour; a capability is potential, organisation-independent |
| Business Interaction | Behaviour (internal) | Yellow rounded box, double-arrow icon | A unit of collective behaviour performed by two or more actors, roles or a collaboration | Treating it as atomic: ArchiMate interactions can be decomposed |
| Business Event | Behaviour | Yellow box with notched left edge | A business-related state change; instantaneous, no duration | Giving an event duration or assigning a role to it |
| Business Service | Behaviour (external) | Yellow rounded box, rounded-rectangle icon | Explicitly defined behaviour that a role, actor or collaboration exposes to its environment | Confusing service (behaviour) with interface (the access point, active structure) |

## Process versus function

Both process and function group finer-grained behaviour, but on different criteria. A process
is a workflow with one or more starting points that leads to a result — sometimes described as
"customer to customer", where the customer may be internal. A function collects behaviour that
shares the same skills, resources or application support, and it is the natural basis for
allocating resources and IT support (ARCHIMATE §8.3). Processes are usually derived from the
products and services an organisation offers; functions from how it is organised. The
relationship between the two is many-to-many: a complex process strings together several
functions, and one function contributes to many processes (ARCHIMATE §8.3.1, ARCHIMATE §8.3.2).

A process describes the internal behaviour a role performs to produce products and services;
to the consumer it is a black box, which is why it counts as internal. A large process can be an
aggregation of smaller ones, each with its own role. It may trigger or be triggered by any
business behaviour element, access business objects, realize one or more services, and be served
by business, application or technology services. A role is assigned to it to model manual
performance; an automated process is realized by an application process. Name it with a verb or
verb-noun phrase — "adjudicate claim", "employee on-boarding" (ARCHIMATE §8.3.1).

**Trap:** ArchiMate only records that a process *exists* and how it relates to other elements. It
does not describe the detailed flow of activities; that belongs to a process-design language such
as BPMN, into which a process can be expanded (ARCHIMATE §8.3.1).

A function delivers added value from the business's point of view and often lines up with an
organisational unit, though it is not governed by one. Functions can *realize capabilities*: the
function describes today's day-to-day activity in the organisation; the capability (a strategy
element) describes potential behaviour independent of how the organisation is structured. Functions
have the same triggering, access, realization and serving relationships as processes, and take
noun-ish names such as "claims administration" or "payment processing" (ARCHIMATE §8.3.2).

## Interaction

An interaction is like a process or function except that it is performed by (a collaboration of)
two or more active-structure elements, who share responsibility for it. From the perspective of
each participating role the interaction is external, but for the collaboration as a whole it is
internal (ARCHIMATE §8.3, ARCHIMATE §8.3.3). It may trigger or be triggered by any business
behaviour element, access business objects, realize services and use business or application
services. A collaboration, or two or more actors or roles, is assigned to it; name it with a
present-tense verb (ARCHIMATE §8.3.3).

**Trap:** the specification's own example makes "Adjudicate High-Risk Claim" an interaction
because company policy requires two people, to reduce fraud risk. When a scenario says two parties
must act jointly, the answer is interaction plus collaboration, not two processes (ARCHIMATE §8.3).

## Event

An event is a state change that matters to the business. It can trigger or interrupt processes,
functions and interactions, and those in turn can raise events that trigger others. Unlike the
other behaviour elements it has no duration. Events may come from outside (a customer acts) or
inside (another process finishes) (ARCHIMATE §8.3.4). An event may carry a time attribute to model
schedules — "every first Monday of the month" — and may access a business object or be composed
of other events. Name it with a perfect-tense verb: "claim received" (ARCHIMATE §8.3.4).

## Service

A business service is behaviour a role, actor or collaboration explicitly exposes, accessed
through one or more interfaces. It must be meaningful from the environment's point of view, and
its purpose is expressed as a value element associated with it. The environment includes users
inside the organisation as well as outside, so a service can be customer-facing ("travel
insurance") or internal support ("resource management") (ARCHIMATE §8.3.5). A service may serve
business, application and technology behaviour or active structure; it is realized by a process,
function or interaction; an interface is assigned to it; and it may access business objects.
Name it with an "-ing" verb or with the word "service" (ARCHIMATE §8.3.5).

**Trap:** which elements *realize* a business service? Process, function and interaction — the
three internal behaviour elements. Not the role (it is *assigned*), not the interface (also
assigned), not the event (it triggers). The direction of realization is internal → external
(ARCHIMATE §8.3.5).

## The example as a map of the relationships

The specification's claims example ties the family together: a function "Claims Administration"
composed of processes and one interaction, realizing a "Claims Processing" service; an event
"Claim Filed" triggering "Accept Claim", which triggers "Assign Claim"; a choice between a
standard-claim process and a high-risk interaction; two processes running in parallel; and a
final process triggered when both finish. Composition, realization, triggering and the
process/function/interaction distinction are all visible in one small view (ARCHIMATE §8.3).

Table 6 lists each element's one-line definition. Learn the five behaviour rows as pairs of
aspect and definition — the definitions of process and function are the most frequently swapped
options in Part 1 (ARCHIMATE §8.6).
