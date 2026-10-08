---
title: "Purpose of the language and the generic metamodel"
unit: A1
objectives: ["A1.1"]
refs: ["ARCHIMATE §1.1", "ARCHIMATE §1.2", "ARCHIMATE §3.1", "ARCHIMATE §3.2", "ARCHIMATE §3.6", "ARCHIMATE §3.7", "ARCHIMATE §4", "ARCHIMATE §4.1", "ARCHIMATE §4.1.1", "ARCHIMATE §4.1.2", "ARCHIMATE §4.1.3", "ARCHIMATE §4.2", "ARCHIMATE §4.3", "ARCHIMATE §4.4", "ARCHIMATE §4.5", "ARCHIMATE §4.5.1", "ARCHIMATE §4.5.2"]
reading_minutes: 10
source: authored
status: draft
---
## What the language is for

ArchiMate is a *visual modelling language* for Enterprise Architecture: a fixed set of element and
relationship types, each with a default icon, used to describe, analyse and communicate an
architecture and how it changes over time. It is not a method — it does not tell you what to do in
which order — and it is not a framework in the TOGAF sense. It comes with an XML exchange format so
models can move between tools (ARCHIMATE §1.1).

The motivating picture in the specification is that architectures exist because *stakeholders have
concerns*. The architect's job is to capture the motivation and strategy those stakeholders express,
develop the architecture, and produce views that show how it balances their concerns. The language
therefore has to cover several inter-related domains at once, offer viewpoints aimed at particular
stakeholders, and stay customizable (ARCHIMATE §1.2).

Three design ideas from the overview recur in exam questions (ARCHIMATE §1.2):

| Idea | What it means in the language |
|---|---|
| **Service orientation** | The Business, Application and Technology layers are distinguished and linked through the services each offers to the layer above |
| **Realization across layers** | A concrete element in a lower layer *realizes* a more abstract element in a higher one |
| **Concepts separate from notation** | The metamodel is one thing; how it is drawn is another, so the same element can be shown differently to different stakeholders |

## Design goals: deliberately small

The most important design restriction is that the language was built to be *as small as possible*
while still covering most Enterprise Architecture modelling — the specification talks about the
proverbial 80 % of practical cases. It started from a few generic concepts and specialized them per
layer, rather than trying to satisfy every possible user (ARCHIMATE §3.1).

**Trap:** if an option says the language aims to cover *every* modelling need of every user, it is
wrong; the stated goal is the opposite (ARCHIMATE §3.1).

## The top of the hierarchy

Figure 1 of the specification gives the top-level structure: a *model* is a collection of
*concepts*, and every concept is either an *element* or a *relationship*. An element is one of four
kinds — behaviour element, structure element, motivation element or composite element. These
top-level concepts are abstract: they organize the metamodel and are never placed in a model
themselves, which is why they are drawn in white with italic labels (ARCHIMATE §3.2).

<figure class="max-w-lg"><img src="/figure/ARCHIMATE:fig-1" alt="Top-level hierarchy of ArchiMate concepts" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 1. Top-Level Hierarchy of ArchiMate Concepts (ARCHIMATE)</figcaption></figure>

## The generic metamodel: nouns and verbs

The generic metamodel (chapter 4) defines structure and behaviour elements in a layer-independent
way. Structure elements are the *nouns*; behaviour elements are the *verbs*. Structure splits into
**active structure** (things that can perform behaviour) and **passive structure** (things
behaviour is performed on). Active structure splits again into *internal* active structure and
*external* active structure, the latter being an **interface**. Behaviour splits into *internal*
behaviour, *external* behaviour — a **service** — and **events** (ARCHIMATE §4.1).

| Generic element | Kind | Definition in short | Notation |
|---|---|---|---|
| Internal active structure | active structure | an entity capable of performing behaviour | square-cornered box, icon top-right |
| Interface | active structure (external) | a point of access where services are exposed to the environment | square corners |
| Internal behaviour | behaviour | a unit of activity performable by one or more active structure elements | round corners |
| Service | behaviour (external) | explicitly defined, exposed behaviour | round corners |
| Event | behaviour | a state change; may carry a time attribute | round corners, notched left edge |
| Passive structure | passive structure | an element on which behaviour is performed | square corners |

The interface gives an outside view of the provider while hiding its internals (ARCHIMATE §4.1.1).
A service is the behaviour visible to whoever uses it, and services are reached *through*
interfaces; the value the service offers is the reason it exists (ARCHIMATE §4.1.2). Passive
structure is most often information or data, but may also be a physical thing (ARCHIMATE §4.1.3).

**Trap:** "external active structure" *is* the interface and "external behaviour" *is* the service.
Questions swap them: an interface is structure, a service is behaviour (ARCHIMATE §4.1).

## Specializations inside the generic metamodel

Internal behaviour is refined into **process** (a sequence of behaviours that achieves a result)
and **function** (behaviour grouped by criteria such as skills, resources or location and managed as
a whole). Processes and functions may compose or aggregate each other in either direction. Collective
behaviour is an **interaction**, performed by two or more active structure elements, and those
elements working together form a **collaboration** — an aggregate of two or more internal active
structure elements (ARCHIMATE §4.2).

<figure class="max-w-lg"><img src="/figure/ARCHIMATE:fig-12" alt="Specializations of core elements" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 12. Specializations of Core Elements (ARCHIMATE)</figcaption></figure>

Chapter 4 also introduces the generic **motivation element** — the context of, or reason behind,
an architecture — drawn with diagonal corners and detailed in chapter 6 (ARCHIMATE §4.4). And it
defines the two generic **composite elements**: **Grouping**, which aggregates or composes any set
of concepts sharing some characteristic (elements *and* relationships, overlapping groups allowed),
and **Location**, a conceptual or physical place that aggregates the structure elements located
there or the behaviour performed there. Product and Plateau are composite elements too, defined in
their own chapters (ARCHIMATE §4.5, §4.5.1, §4.5.2).

**Trap:** a Grouping is *not* a view. A view is a separate visualization for a stakeholder; a
grouping is an element inside a view that adds structure (ARCHIMATE §4.5.1).

## Abstraction: black box, type versus instance, conceptual–logical–physical

The language supports several abstractions: external (black-box) versus internal (white-box);
behaviour versus the active structure that performs it; and conceptual/logical/physical, which maps
to business object → data object → artifact linked by realization. It deliberately has **no
type/instance distinction** — a business process is a type of process, not one execution of it
(ARCHIMATE §3.6). Finally, the concepts are separate from the notation: the standard supplies one
common notation (a box with an icon top-right, or the icon alone) but a viewpoint may present the
same concepts differently (ARCHIMATE §3.7).
