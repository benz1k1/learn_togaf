---
title: "Aspects, layers and the full framework"
unit: A1
objectives: ["A1.2"]
refs: ["ARCHIMATE §3", "ARCHIMATE §3.3", "ARCHIMATE §3.4", "ARCHIMATE §3.5", "ARCHIMATE §3.7", "ARCHIMATE §3.8", "ARCHIMATE §3.9", "ARCHIMATE §4.1"]
reading_minutes: 9
source: authored
status: draft
---
## The three aspects

Every core element sits in one of three *aspects*, and the specification's own explanation is a
sentence: a **subject** does a **verb** to an **object**. The subject is the **active structure**
aspect — actors, application components, devices, the things that display behaviour. The verb is
the **behaviour** aspect — processes, functions, events, services. The object is the **passive
structure** aspect — the things behaviour is performed on, usually information or data objects but
possibly physical objects. Because diagrams are spatial, the left-to-right order carries no meaning
in a model (ARCHIMATE §3.4).

| Aspect | Role in the sentence | Typical elements | Corner shape |
|---|---|---|---|
| Active structure | subject | Business Actor, Business Role, Application Component, Node, Device, all interfaces | square |
| Behaviour | verb | Process, Function, Interaction, Event, Service (in every layer) | round |
| Passive structure | object | Business Object, Contract, Representation, Data Object, Artifact, Material | square |

**Trap:** Part 1 asks "which aspect is X?" Interfaces are *active* structure even though they are
"external"; services are *behaviour* even though they are what the outside sees; a Business Role is
active structure, not behaviour, because it is something that can perform behaviour (ARCHIMATE §3.4,
§4.1).

## The three core layers

The core language is layered three ways. The **Business Layer** shows business services offered to
customers and the processes and actors that realize them. The **Application Layer** shows
application services supporting the business and the applications that realize them. The
**Technology Layer** covers both information technology — processing, storage, communication — and
operational technology such as facilities, equipment, materials and distribution networks. The same
generic element types recur in each layer at a different granularity, which is why the generic
metamodel is defined once and then specialized per layer (ARCHIMATE §3.3).

Two relationships tie the layers together. The most important is **serving**, in line with
service orientation: a layer is served by the services of the layer below (and a service may also
serve elements in its own layer). The second is **realization**: a lower-layer element may realize
a comparable higher-layer one — a data object realizes a business object, an artifact realizes a
data object or an application component (ARCHIMATE §3.3).

**Trap:** "serving" was called "used by" in earlier versions; an option using the old name for the
current relationship is describing the same thing (ARCHIMATE §3.3).

## The Core Framework: a grid of nine cells

Three aspects across, three layers down: the **ArchiMate Core Framework** is a nine-cell grid used
to classify core elements. The classification is a global one, not a cage — a Business Role sits
between "purely behavioural" and "purely structural" elements, and whether a piece of software is
Application or Technology can depend on context. A composite element may span more than one aspect,
and the framework imposes no layout on diagrams; it merely categorizes the language (ARCHIMATE
§3.4).

<figure class="max-w-lg"><img src="/figure/ARCHIMATE:fig-2" alt="ArchiMate Core Framework" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 2. ArchiMate Core Framework (ARCHIMATE)</figcaption></figure>

## The Full Framework

The **Full Framework** extends the core in both directions. It adds a **Motivation** aspect as a
new column, and adds layers: **Strategy** above the Business Layer, **Physical** elements folded
into the Technology Layer (these count as core elements), and **Implementation & Migration** at the
bottom. There is deliberately *no information layer* — information is modelled with passive
structure elements in whichever layer it belongs to (ARCHIMATE §3.5).

<figure class="max-w-lg"><img src="/figure/ARCHIMATE:fig-3" alt="ArchiMate Full Framework" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 3. ArchiMate Full Framework (ARCHIMATE)</figcaption></figure>

| Part of the Full Framework | Elements | Chapter |
|---|---|---|
| Motivation aspect | Stakeholder, Driver, Assessment, Goal, Outcome, Principle, Requirement, Constraint, Meaning, Value | 6 |
| Strategy layer | Resource, Capability, Value Stream, Course of Action | 7 |
| Business / Application / Technology | the core, specialized from chapter 4 | 8, 9, 10 |
| Physical (within Technology) | Equipment, Facility, Distribution Network, Material | 11 |
| Implementation & Migration | Work Package, Deliverable, Implementation Event, Plateau, Gap | 12 |

**Trap:** an option claiming ArchiMate has a dedicated "Information" or "Data" layer is wrong
(ARCHIMATE §3.5). Physical elements are *inside* the Technology Layer, not a fourth core layer
(ARCHIMATE §3.5).

## The whole notation on one page

Every element and relationship type of the language, drawn in the standard notation:

<img src="/static/archimate/notation_sampler.svg" alt="ArchiMate 3.2 notation sampler" class="rounded border border-base-300">

## Reading the notation: corners, colours, letters

The default notation is a box with an icon in the top-right corner, and in many cases the icon
alone is an accepted alternative. The standard prefers its own iconography so that anyone who
knows the language can read any diagram (ARCHIMATE §3.7). Corner shapes are meaningful: **square
corners** mark structure elements, **round corners** mark behaviour, **diagonal corners** mark
motivation elements (ARCHIMATE §3.9).

Colour has *no* formal semantics; it is left to the modeller. The convention used in the
specification's examples is yellow for Business, blue for Application, green for Technology, and
in metamodel figures shades of grey distinguish aspects (white for abstract concepts, light grey
passive, medium grey behaviour, dark grey active). A letter in the top-left corner — M, S, B, A, T,
P or I — is an optional cue for Motivation, Strategy, Business, Application, Technology, Physical
or Implementation & Migration (ARCHIMATE §3.9).

**Trap:** "yellow means Business Layer" is a *convention*, not a rule of the language. If a
question asks what colour formally means, the answer is nothing (ARCHIMATE §3.9).

Nesting one element inside another is an alternative graphical notation for certain relationships
(composition, aggregation, assignment, realization), explained per relationship in chapter 5
(ARCHIMATE §3.8).
