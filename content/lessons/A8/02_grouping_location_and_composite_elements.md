---
title: "Composite elements: grouping, location, product and plateau"
unit: A8
objectives: ["A8.2"]
refs: ["ARCHIMATE §4.5", "ARCHIMATE §4.5.1", "ARCHIMATE §4.5.2", "ARCHIMATE §B.6", "ARCHIMATE §B.3.5", "ARCHIMATE §5.5.1", "ARCHIMATE §8.5.1", "ARCHIMATE §12.5"]
reading_minutes: 8
source: authored
status: draft
---
## What "composite" means

A composite element is one whose job is to *contain* other concepts, possibly from several
layers and aspects at once. The generic metamodel names two — **Grouping** and **Location** — and
two more live in their own chapters: **Product** in the business layer and **Plateau** in
implementation and migration. Composites can nest: a grouping may aggregate another grouping, a
location may contain a plateau (ARCHIMATE §4.5).

<figure class="max-w-lg"><img src="/figure/ARCHIMATE:fig-18" alt="Composite elements" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 18. Composite Elements (ARCHIMATE)</figcaption></figure>

| Element | Notation | Contains | Typical use |
|---|---|---|---|
| **Grouping** | dashed rectangle with a tab | any concepts — elements *and* relationships, of any type | domains, ABBs and SBBs, "these belong together" |
| **Location** | pin icon, orange | structure elements (where they are), behaviour (where it happens) | sites, regions, data centres; the Zachman "where" |
| **Product** | rectangle with the product icon | services, contracts, value, interfaces | what is offered to a customer |
| **Plateau** | stacked-layers icon | any core concept, motivation elements | a state of the architecture in time |

## Grouping

Grouping collects an arbitrary set of concepts that share some characteristic, joined to the
group by **aggregation** or **composition**. Members may be elements or relationships, of the same
or different types, and one concept may sit in several overlapping groups. Two uses are called out
because they map straight onto TOGAF: modelling Architecture and Solution Building Blocks, and
modelling *domains* — an information domain being a grouping of data entities by classification,
ownership or location (ARCHIMATE §4.5.1).

<figure class="max-w-lg"><img src="/figure/ARCHIMATE:fig-19" alt="Grouping notation" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 19. Grouping Notation (ARCHIMATE)</figcaption></figure>

A relationship drawn to or from the group is read *collectively*: "grouping realizes service"
means the members together, or some of them, realize it. The specification warns that this
collective meaning is not always reducible to relationships on individual members
(ARCHIMATE §4.5.1).

**Trap — grouping versus view:** a view is a separate visualisation selected by a viewpoint; a
grouping is an element *inside* the model (and inside views) that adds structure. Putting elements
in a grouping does not create a view of them, and a viewpoint is not a kind of grouping
(ARCHIMATE §4.5.1).

Grouping is the most permissive element in the language. Beyond aggregating or composing
anything, it may be the *source* of any relationship whose target could receive it, the *target*
of any relationship whose source could send it, and may relate to another grouping in any way at
all. Plateau and location share the first power over relationships and junctions, not the second
(ARCHIMATE §B.6).

The one derivation rule written specifically for grouping, PDR 12, lets a realization or an
assignment from the group be pushed down to a member — potentially, and only where the member's
own row of the relationship table permits that relationship (ARCHIMATE §B.3.5).

## Location

A location is a conceptual or physical place. It **aggregates** the structure elements that are
located there — actors, application components, devices — and may aggregate a behaviour element to
say where that behaviour is performed. It answers the "where" column of Zachman and appears in the
Organization, Technology, Physical and Application Cooperation viewpoints (ARCHIMATE §4.5.2).

**Trap:** the relationship from a location to what it holds is *aggregation*, not assignment.
"Data centre assigned to server" reverses the sense; "data centre aggregates server" is right. A
location may also compose, since composites may compose, but assignment is not on the list
(ARCHIMATE §4.5.2).

## Product and plateau as composites

Product is a business-layer composite: a coherent collection of services and a contract, sold as
a whole. It may aggregate services from any layer, a contract, interfaces and value — but only the
concepts its own metamodel fragment shows; unlike grouping it is not a universal container
(ARCHIMATE §8.5.1).

Plateau has the same restriction stated the other way round: it may aggregate or compose any *core*
concept and any motivation element, and may realize core elements and capabilities, but its
contents are limited to what its fragment permits rather than the "anything" of grouping
(ARCHIMATE §12.5).

## Junctions inside composites

A junction may itself be aggregated or composed in a plateau, grouping or location. That
containment is read on its own — it says only that the junction belongs to the container — and does
not join the junction's relationships to the container. The junction must still satisfy its usual
rule: relationships of one type, at least one in and one out (ARCHIMATE §5.5.1).

## Worked model

"Claims Domain (grouping) aggregates: Assess Claim (process), Settle Claim (process), Claim
(business object), and the access relationship between Assess Claim and Claim. Claims Domain
realizes Claims Handling Service. Head Office (location) aggregates Claims Department (actor) and
Assess Claim." The group holds a relationship as a member; the realization is collective; the
location says where the department sits and where the assessment happens. PDR 12 would let a
modeller *propose* that Assess Claim alone realizes the service — permitted, since a process may
realize a service — but it stays potential until the modeller confirms it (ARCHIMATE §B.3.5).

## Check yourself

- Which composite may contain relationships, and which two others may also do so?
- Which relationship connects a location to the actors it holds?
- Why is a grouping not a view?
