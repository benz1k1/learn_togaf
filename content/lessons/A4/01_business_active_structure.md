---
title: "Business active structure: actor, role, collaboration, interface"
unit: A4
objectives: ["A4.1"]
refs: ["ARCHIMATE §8", "ARCHIMATE §8.1", "ARCHIMATE §8.2", "ARCHIMATE §8.2.1", "ARCHIMATE §8.2.2", "ARCHIMATE §8.2.3", "ARCHIMATE §8.2.4", "ARCHIMATE §8.6"]
reading_minutes: 9
source: authored
status: draft
---
## Where the Business Layer sits

The Business Layer is the part of the core language that describes how an enterprise actually
operates day to day, without saying anything about the technology it runs on. That is the
contrast the specification draws with the strategy elements of Chapter 7, which describe
direction and choices rather than operations (ARCHIMATE §8). Every Business Layer element is
yellow in the default notation and sits in one of the three aspects: active structure (who
acts), behaviour (what happens) or passive structure (what is acted upon) (ARCHIMATE §8.1).

The metamodel in Figure 52 is the picture the Part 1 exam reproduces in fragments. Three of its
boxes are abstract — "business internal active structure element", "business internal behavior
element" and "business passive structure element" — and are never drawn in a model; only their
concrete specializations are (ARCHIMATE §8.1). The figure also does not show every permitted
relationship: any element may be composed of, aggregate, or specialize an element of its own type,
and further relationships can be derived by the chain rules of §5.7 (ARCHIMATE §8.1).

<figure class="max-w-lg"><img src="/figure/ARCHIMATE:fig-52" alt="Business Layer metamodel" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 52. Business Layer Metamodel (ARCHIMATE)</figcaption></figure>

## The active-structure family

The active-structure aspect of the Business Layer is the static organisation: the entities that
make up an enterprise and how they relate. These are the *subjects* — the things that perform
processes and functions. An actor can be one person, but it can equally be a group with a lasting
place in the organisation, such as a department or a business unit (ARCHIMATE §8.2). Three of the
four elements are *internal* active structure (actor, role, collaboration); the interface is the
*external* active structure — the point where the outside world touches the organisation
(ARCHIMATE §8.2).

<figure class="max-w-lg"><img src="/figure/ARCHIMATE:fig-53" alt="Business internal active structure elements" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 53. Business Internal Active Structure Elements (ARCHIMATE)</figcaption></figure>

| Element | Aspect | Notation | Definition in plain words | Typical confusion |
|---|---|---|---|---|
| Business Actor | Active structure (internal) | Yellow box, stick-figure icon | An organisational entity able to perform behaviour: a person, team, department, or an outside party such as a customer or partner | Mistaking an actor for a role: "ABC Corporation" is an actor, "Supplier" is the responsibility it takes on |
| Business Role | Active structure (internal) | Yellow box, cylinder-on-its-side icon | A responsibility for performing behaviour, or the part played in an action, to which an actor is assigned | Assigning an actor directly to a process; the normal chain is actor → role → process |
| Business Collaboration | Active structure (internal) | Yellow box, two overlapping circles | A temporary grouping of two or more roles, actors or collaborations that together perform collective behaviour | Confusing it with a department, which is a permanent actor; a collaboration need not exist formally |
| Business Interface | Active structure (external) | Yellow box, lollipop icon | A channel or access point through which a business service is offered to the environment | Confusing interface with service: the service is behaviour, the interface is where it is reached |

### Business actor

An actor is any business entity capable of behaviour, and "business" here means it belongs to
this layer rather than being a technical thing. Actors are not limited to the enterprise's own
staff; customers and partners are actors too. The element maps onto both "actor" and
"organization unit" in TOGAF, which is why a single ArchiMate element can be drawn at several
levels of detail (ARCHIMATE §8.2.1). An actor can be specific ("Jane Doe", "ABC Corporation") or
generic ("customer", "supplier"); it is assigned to one or more roles and may be aggregated in a
location. Name it with a noun (ARCHIMATE §8.2.1).

### Business role

A role is the responsibility for doing something, separated from whoever currently does it. Roles
are assigned to processes and functions; actors are assigned to roles. An actor assigned to a role
must make sure the behaviour happens — either by performing it or by delegating and overseeing it
(ARCHIMATE §8.2.2). Roles are also used structurally, to describe a division of labour. A business
interface or an application interface may serve a role, and an interface may be part of a role
(ARCHIMATE §8.2.2).

**Trap:** the exam likes "Supplier". Modelled as an actor it is an organisational entity; modelled
as a role it is a responsibility. Either is legitimate, but the specific actor "ABC Corporation"
or the generic actor "Business Partner" is what gets *assigned* to the role "Supplier", never the
other way round (ARCHIMATE §8.2.2).

### Business collaboration

A collaboration is an aggregate of two or more internal active structure elements that work
together. A process or function is normally the internal behaviour of one active element; when
several must act jointly, and the joint result is more than the sum of their parts, the
collaboration is the element that carries that collective effort, and business interactions
describe what it does (ARCHIMATE §8.2.3). Unlike a department it may be temporary and need not
have an official place in the organisation chart; it is a good fit for B2B provider networks and
social networks. It aggregates roles, actors or other collaborations, is assigned to interactions,
and may be served by or composed of interfaces. Leaving it unnamed is common (ARCHIMATE §8.2.3).

### Business interface

The interface is where business services are made available: the telephone line, the website,
the branch counter. One service may be exposed through several interfaces, and the interface is
what exposes the service to other roles or actors (ARCHIMATE §8.2.4). Structurally it may be a
part of a role or actor by composition, it may serve a role, and it is *assigned to* the services
it exposes. Interfaces are common in application modelling but comparatively rare in business
modelling practice, which is exactly why the specification introduces the element explicitly
(ARCHIMATE §8.2, ARCHIMATE §8.2.4).

**Trap:** an interface is assigned to a *service*, never to a process. If a question offers "the
business interface realizes the business service", it is wrong on two counts: the relationship is
assignment, and it is a process, function or interaction that realizes the service (ARCHIMATE §8.2.4).

## Reading the example

The specification's own example has a contact centre modelled as an actor composed of three
employee actors, three interfaces (phone, e-mail, web chat), one role per employee, two of those
roles specializing a generic "Specialist" role, and a collaboration of "Specialist" and
"Customer Service Representative" for high-risk claims. Every structural device of this lesson
appears in one small diagram: composition of actors, assignment of actors to roles,
specialization of roles, and aggregation of roles into a collaboration (ARCHIMATE §8.2).

## Summary table check

Table 6 of the specification restates each element in one line; the four active-structure rows
are the definitions above, and the exam draws its single-answer definition questions almost
verbatim from them (ARCHIMATE §8.6). Learn the aspect of each element before the definition:
"which aspect is a Business Role?" is the commonest question shape in this unit.
