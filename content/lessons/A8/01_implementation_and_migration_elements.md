---
title: "Work package, deliverable, implementation event, plateau and gap"
unit: A8
objectives: ["A8.1"]
refs: ["ARCHIMATE §12", "ARCHIMATE §12.1", "ARCHIMATE §12.2.1", "ARCHIMATE §12.2.2", "ARCHIMATE §12.2.3", "ARCHIMATE §12.2.4", "ARCHIMATE §12.2.5", "ARCHIMATE §12.2.6", "ARCHIMATE §12.3", "ARCHIMATE §12.5"]
reading_minutes: 10
source: authored
status: draft
---
## What the layer is for

The implementation and migration elements exist so that a model can describe *how the
architecture gets built*, not only what it is: programmes and projects for portfolio and project
management, and the staged transition from today's architecture to tomorrow's. Five elements do
this work, and they use the ordinary ArchiMate relationships rather than any of their own
(ARCHIMATE §12).

<figure class="max-w-lg"><img src="/figure/ARCHIMATE:fig-106" alt="Implementation and migration metamodel" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 106. Implementation and Migration Metamodel (ARCHIMATE)</figcaption></figure>

| Element | Kind | Notation cue | One-line definition |
|---|---|---|---|
| **Work Package** | behaviour | rounded rectangle, like a process, pale pink | a bounded series of actions producing defined results within time and resource limits |
| **Deliverable** | passive structure | wavy-bottomed rectangle (a document) | a precisely defined result of a work package |
| **Implementation Event** | event | notched rectangle, like other events | a state change related to implementation or migration |
| **Plateau** | composite | stacked-layers icon, pale green | a relatively stable state of the architecture over a limited period |
| **Gap** | — | rectangle with a "not equal" style icon | a statement of difference between two plateaus |

The metamodel figure carries one deprecation to remember: the realization from Work Package to
Deliverable is marked for possible removal, and the recommended relationship is **access** instead
— the work package *produces* (writes) the deliverable (ARCHIMATE §12.1).

## Work package

A work package is the behavioural centre of the layer. It has a start and an end — modelled as
attributes if needed — and produces well-defined results, typically goals, outcomes or
deliverables. The element scales: a task inside a project, a whole project, a programme, or a
portfolio can all be work packages, composed of one another, and in agile delivery a sprint or an
increment fits the same mould (ARCHIMATE §12.2.1).

The specification compares it to a business process, since both are causally related sets of
tasks aimed at a result; the difference is that a work package is a *one-off* — it runs once,
whereas a process is a repeatable pattern (ARCHIMATE §12.2.1).

## Deliverable

A deliverable is what a work package hands over: a report, a piece of software, a service, a
physical product, or an intangible such as organisational change. Crucially for the TOGAF
mapping, a deliverable may be *the implementation of part of an architecture*, which is why any
core element may be **realized** by a deliverable. Deliverables are typically specified in a
contract, reviewed and signed off — the TOGAF sense of the word exactly (ARCHIMATE §12.2.2).

## Implementation event

An implementation event is instantaneous — it has no duration — and marks a state change in the
delivery: a programme approved, a phase completed, a release made. It may carry a time attribute,
which is how schedules and milestones enter the model. Events **trigger** work packages and are
**triggered** by them (a work package raising its own "completed" event), and they may trigger or
be triggered by plateaus. An event may also **access** a deliverable to mark a lifecycle change —
"release to production" accessing the final build and the production environment — and may be
composed of other events. Name it as a verb in the perfect tense: "Initiation phase completed"
(ARCHIMATE §12.2.3).

**Trap:** a work package has a duration; an implementation event does not. An option that gives
an event a start and an end, or a work package a single moment, has swapped them
(ARCHIMATE §12.2.3).

## Plateau

A plateau is a snapshot of the architecture that holds still for a while. It is the ArchiMate
answer to TOGAF's Baseline, Target and Transition Architectures: Phases B, C and D each describe a
baseline and a target, and Phase E defines the transition states between them so that work
packages can be grouped into managed programmes with visible business value at each step. Each of
those states is a plateau (ARCHIMATE §12.2.4).

A plateau may **aggregate or compose** any core concept to say what belongs to that state, and
may **realize** part of the architecture — a capability realized by a plateau is a capability
increment valid only for that period. Motivation elements can be aggregated in a plateau too, so
that a requirement can be tied to the target state alone. Plateaus trigger each other in sequence
(ARCHIMATE §12.5).

## Gap

A gap is the difference between two plateaus — baseline and target, or two consecutive
transitions. It is **associated** with both plateaus and with the core concepts that exist in only
one of them. In TOGAF terms a gap is the output of gap analysis in Phases B, C and D and the input
to migration planning in E and F (ARCHIMATE §12.2.5).

**Trap:** a gap connects two *plateaus*, and it does so by association, not by realization or
triggering. "Gap realizes target plateau" is wrong on both the relationship and the meaning
(ARCHIMATE §12.2.5).

## Relationships to the rest of the language

The layer's contact points with the core and motivation elements are few and worth memorising
(ARCHIMATE §12.5):

| From | To | Relationship | Meaning |
|---|---|---|---|
| business internal active structure (actor, role) | work package | assignment | who is responsible, e.g. a project manager role |
| plateau | any core concept | aggregation / composition | what the state contains |
| plateau | core element or capability | realization | e.g. a capability increment |
| deliverable | any core element | realization | the deliverable implements that part |
| gap | core concepts unique to one plateau | association | what differs |
| composite element (grouping, location) | work package or deliverable | aggregation | organising the work |
| deliverable | requirement (and, indirectly, goal or outcome) | realization | why the work is done |
| plateau | goal, outcome, requirement | aggregation / composition | which motivation applies to which state |

Strictly, a deliverable realizes a goal only *through* the core element it delivers, but the
specification allows the shortcut so the traceability from work to intent can be drawn explicitly
(ARCHIMATE §12.5).

## The reference example, in prose

A programme work package composes three project work packages. A "Programme approved" event
triggers the first, which triggers the second, which triggers the third, which triggers a
"Programme completed" event. The approval event also provides a "Programme brief" deliverable that
the first project accesses as input. The first project realizes a business plan, an architecture
and a roadmap; those deliverables together realize a plateau, "Strategic plan complete", which
follows the "Baseline" plateau across a named gap. Each later project realizes deliverables that
realize the next plateau (ARCHIMATE §12.2.6).

## Check yourself

- Which relationship does the metamodel now recommend from a work package to its deliverable?
- Which element has no duration, and how should it be named?
- Which two elements does a gap connect, and by which relationship?
