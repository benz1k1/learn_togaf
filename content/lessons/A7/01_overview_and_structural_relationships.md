---
title: "The relationship families and the four structural relationships"
unit: A7
objectives: ["A7.1"]
refs: ["ARCHIMATE §5", "ARCHIMATE §5.1", "ARCHIMATE §5.1.1", "ARCHIMATE §5.1.2", "ARCHIMATE §5.1.3", "ARCHIMATE §5.1.4", "ARCHIMATE §5.1.5", "ARCHIMATE §5.6"]
reading_minutes: 10
source: authored
status: draft
---
## Eleven relationships, one connector, four families

Elements on their own say nothing about an architecture; the relationships between them carry
the meaning. ArchiMate defines a small, fixed set of relationship types, and most of them are
*overloaded*: the same arrow means something slightly different depending on what it joins, so
"assignment" between an actor and a role is not quite the same statement as "assignment" between a
node and an artifact. The specification groups the set into four families (ARCHIMATE §5).

| Family | Members | What the family says |
|---|---|---|
| **Structural** | Composition, Aggregation, Assignment, Realization | how things are built or made up, statically |
| **Dependency** | Serving, Access, Influence, Association | how one thing supports or is used by another |
| **Dynamic** | Triggering, Flow | behaviour over time: what precedes what, what is passed |
| **Other** | Specialization | a kind-of relationship |
| *Connector* | Junction (and / or) | joins several relationships of one type |

<img src="/static/archimate/notation_sampler.svg" alt="ArchiMate notation sampler" class="rounded border border-base-300">

Every relationship has exactly one source ("from") and one target ("to"). A few restrictions
hold everywhere: two relationships can never be joined to each other directly; every
relationship attached to one junction must be of the same type; and a chain through junctions is
only allowed where the same direct relationship would be allowed. When an element is connected to
a *relationship* (rather than to another element), only aggregation, composition or association may
do it, and the first two only from a composite element such as a grouping (ARCHIMATE §5).

Three "always allowed" facts are worth memorising because they short-circuit many exam questions:
composition, aggregation and specialization are permitted between any two elements of the *same*
type; association is permitted between any two elements at all, and between any element and any
relationship; everything else is governed by the metamodel plus the derivation rules, with the
complete answer in Appendix B (ARCHIMATE §5).

<figure class="max-w-lg"><img src="/figure/ARCHIMATE:fig-21" alt="Overview of the relationship families" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 21. Overview of Relationships (ARCHIMATE)</figcaption></figure>

## Structural relationships: static coherence

The four structural relationships describe the "static" build of an architecture. The
*uniting* end (the whole, the performer, the realizer) is always an element; the *united* end can
sometimes be another relationship or a junction. All four may be drawn either as a line or by
**nesting** the united concept inside the uniting element — a convenient notation, but ambiguous
whenever more than one structural relationship would be legal between the two (ARCHIMATE §5.1).

| Relationship | Notation | Meaning | Direction to remember |
|---|---|---|---|
| **Composition** | line with a filled diamond at the whole | the whole *consists of* the part; delete the whole and the parts normally go with it | diamond on the whole |
| **Aggregation** | line with a hollow diamond at the whole | the whole *combines* parts that can exist on their own | diamond on the whole |
| **Assignment** | line with a filled dot at the source and an arrowhead at the target | allocation: who performs, who fulfils, where something is stored or executed | active structure → behaviour; actor → role; node → artifact |
| **Realization** | dotted line with a hollow triangular arrowhead | a concrete "how" element brings about a more abstract "what" element | from the concrete to the abstract |

### Composition and aggregation

Composition is the stronger whole-part relationship. It borrows the UML idea of an existence
dependency: a department that is *composed in* a division does not outlive the division. When a
model shows categories rather than instances — a server type composed of a device type and system
software — the dependency is read as applying to the real-world instances of those types. The
weaker sibling, aggregation, drops the existence dependency: a customer file aggregating policies
and claims can lose one without ceasing to be the file (ARCHIMATE §5.1.1, ARCHIMATE §5.1.2).

**Trap:** the filled diamond is composition, the hollow diamond is aggregation, and both diamonds
sit at the *whole*. A question that puts the diamond at the part, or asks which of the two allows
the part to be shared between wholes, is testing exactly this: only aggregation allows sharing
(ARCHIMATE §5.1.2).

### Assignment

Assignment allocates responsibility. In the core framework it always runs from active structure
to behaviour (a component assigned to a function), from behaviour to passive structure in the
technology layer's storage sense, or between active structure elements (an actor assigned to the
role it fulfils, a node assigned to the artifact it stores). Nesting follows the same direction: a
role drawn inside the actor that plays it. If two performers are each assigned to one behaviour, the
reading is that *either* could perform all of it; if both are needed together, use an and-junction,
a grouping, or model a collaboration (ARCHIMATE §5.1.3).

**Trap:** the old two-dot, non-directional assignment from ArchiMate 2.1 is still accepted but
deprecated; the current notation has one dot at the source and an arrowhead at the target
(ARCHIMATE §5.1.3).

### Realization

Realization runs from the tangible to the abstract: a business process realizes a business
service, a data object realizes a business object, an artifact realizes an application component,
a core element realizes a requirement. Two processes each realizing one service means either can
deliver the whole service. Where an element merely helps a motivation element along rather than
being critical to it, influence is the right choice, not realization (ARCHIMATE §5.1.4).

**Trap:** the arrowhead points at the *abstract* element. "Service realizes process" is reversed;
"process realizes service" is correct. The same trap appears across layers: the artifact realizes
the component, never the other way round (ARCHIMATE §5.1.4).

## The structural semantics rule

Structural relationships tolerate unmodelled detail on the *source* side. If some part of A
aggregates B, A aggregates B; if a role is assigned to a process, some part of that role may be
what actually performs it; if a process realizes a service, some sub-process may be what does the
realizing. This is what lets a summary model stay truthful when the detail is left out, and it is
the basis of the derivation rules in lesson 04 (ARCHIMATE §5.1.5).

## Worked reading

"Claims Department (actor) —assigned→ Claims Handler (role) —assigned→ Assess Claim (process)
—realizes→ Claim Assessment Service; Assess Claim —composed of→ Check Policy, Estimate Loss."
Read it as: the department fulfils the role; the role performs the process; the process, made of
two sub-processes, delivers the service. Every arrow here is structural, and lesson 04 will
collapse this chain into a single derived relationship (ARCHIMATE §5.6).

## Check yourself

- Which diamond means an existence dependency?
- Which end of a realization carries the arrowhead — the abstract or the concrete element?
- What does nesting a role inside an actor express, and why can nesting be ambiguous?
