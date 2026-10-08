---
title: "Mapping the ADM to ArchiMate: phases to viewpoints, metamodel to elements"
unit: A9
objectives: ["A9.3"]
refs: ["ARCHIMATE §D.1", "ARCHIMATE §12.2.4", "ARCHIMATE §12.2.2", "ARCHIMATE §4.5.1", "ARCHIMATE §C.1", "ARCHIMATE §C.2", "ARCHIMATE §C.3", "ARCHIMATE §C.4", "ARCHIMATE §13.4"]
reading_minutes: 11
source: authored
status: draft
---
## How the two standards fit

Appendix D.1 states the relationship in one sentence: ArchiMate complements TOGAF by supplying a
vendor-neutral set of concepts with a graphical notation, so that a consistent, integrated model
can be kept "below the waterline" and surfaced as TOGAF views. TOGAF gives the process and the
framework; ArchiMate gives the language. The two overlap only where they should — in the ISO 42010
notion of viewpoints and in the idea of a common repository of models — which is why they are used
together so easily (ARCHIMATE §D.1).

<figure class="max-w-lg"><img src="/figure/ARCHIMATE:fig-116" alt="Correspondence between the ArchiMate language and the TOGAF ADM" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 116. Correspondence Between the ArchiMate Language and the TOGAF ADM (ARCHIMATE)</figcaption></figure>

The structural correspondence is simple. The **core** of ArchiMate — business, application and
technology layers — lines up with Phases B, C and D. The **strategy, motivation and
implementation-and-migration** elements map approximately onto the rest of the cycle: motivation
and strategy onto Preliminary, A and Requirements Management; implementation and migration onto E,
F and G. "Approximately" is the specification's own word — motivation and strategy elements are
also used inside B, C and D (ARCHIMATE §D.1).

**Trap:** ArchiMate is a modelling language, not a framework, and the specification says so
twice. Its viewpoint definitions are therefore *more detailed* than TOGAF's — they name
stakeholders, concerns, purpose and elements — where TOGAF describes views more generally. There is
no one-to-one mapping between TOGAF and ArchiMate viewpoints; some TOGAF viewpoints have no
ArchiMate counterpart, though the viewpoint mechanism can be used to define them from ArchiMate
concepts (ARCHIMATE §D.1).

## Phase by phase: which viewpoints draw which phase

The table below is the one the ADM explorer in this app renders; it is a reading of D.1 through
the example viewpoints of Appendix C (ARCHIMATE §D.1).

| ADM phase | ArchiMate viewpoints | Elements that carry it |
|---|---|---|
| **Preliminary** | Motivation, Organization | Stakeholder, Driver, Principle, Business Actor, Business Role, Grouping |
| **A — Architecture Vision** | Motivation, Stakeholder, Goal Realization, Strategy, Outcome Realization | Stakeholder, Driver, Assessment, Goal, Outcome, Principle, Requirement, Capability, Course of Action |
| **B — Business Architecture** | Organization, Business Process Cooperation, Product, Capability Map, Value Stream | Business Actor, Role, Process, Function, Service, Object, Product, Capability, Value Stream |
| **C — Information Systems Architectures** | Information Structure (data), Application Cooperation and Application Usage (application) | Business Object, Data Object, Application Component, Interface, Service, Function |
| **D — Technology Architecture** | Technology, Technology Usage, Physical, Layered | Node, Device, System Software, Technology Service, Communication Network, Artifact, Facility, Equipment |
| **E — Opportunities and Solutions** | Migration, Implementation and Migration | Plateau, Gap, Work Package, Deliverable |
| **F — Migration Planning** | Implementation and Migration, Project | Work Package, Deliverable, Implementation Event, Plateau, Business Role |
| **G — Implementation Governance** | Implementation and Migration, Project | Work Package, Deliverable, Business Role, Contract |
| **H — Change Management** | Motivation, Migration | Driver, Assessment, Requirement, Plateau, Gap |
| **Requirements Management** | Requirements Realization, Motivation | Requirement, Constraint, Goal, Principle |

A few readings behind the rows. The Preliminary Phase's tailored framework and EA organisation
model are an Organization view, and its architecture principles are Principle elements. Phase A is
the motivation and strategy aspects: who cares, why, and what the vision must achieve. Phase C
splits neatly — Data Architecture is the Information Structure viewpoint, Application Architecture
the Application Cooperation and Usage viewpoints. Phase D's Layered view is where the three core
layers are tied together (ARCHIMATE §C.1, ARCHIMATE §C.2, ARCHIMATE §C.3).

Phases E through H rest on the implementation and migration layer. The specification itself
anchors the mapping: Baseline, Target and Transition Architectures are **plateaus**; gap analysis
output is **gap** elements; the Implementation and Migration Plan is **work packages** in
sequence, realizing **deliverables**, with **implementation events** as milestones. An
Architecture Contract in Phase G is a Contract element; a change request in Phase H is a new
Driver or Assessment whose impact is a Gap against the current plateau (ARCHIMATE §12.2.4,
ARCHIMATE §C.4).

**Trap — E versus F:** Phase E asks *what the transition states are* (Migration viewpoint,
plateaus and gaps) and *which work packages fill the gaps* (Implementation and Migration). Phase F
asks *in what order and under whose responsibility* (Project viewpoint: work packages, events,
roles). A question that names transition architectures wants E and Migration; one that names a
project schedule with milestones wants F and Project (ARCHIMATE §C.4).

## Content metamodel entities to language elements

The second half of the objective is the entity mapping: what a TOGAF content-metamodel entity
becomes when it is modelled in ArchiMate. Most are direct (ARCHIMATE §D.1):

| TOGAF entity | ArchiMate element | Note |
|---|---|---|
| Actor | Business Actor | |
| Role | Business Role | actor *assigned to* role |
| Organization Unit | Business Actor (composed) | departments compose in divisions |
| Business Function | Business Function | |
| Process | Business Process | |
| Business Service | Business Service | |
| Event | Business Event | |
| Product | Product | the composite, with its Contract |
| Contract | Contract | the Architecture Contract of Phase G too |
| Data Entity | Business Object (conceptual), Data Object (logical) | data object *realizes* business object |
| Logical / Physical Application Component | Application Component | physical realized by an Artifact |
| Information System Service | Application Service | |
| Logical / Physical Technology Component | Node, Device, System Software | |
| Platform Service | Technology Service | |
| Location | Location | |
| Driver, Goal, Objective | Driver, Goal, Outcome | an objective is a measurable outcome |
| Principle | Principle | |
| Requirement, Constraint, Assumption | Requirement, Constraint | assumptions have no element; use association or a note |
| Measure | attribute, or Outcome | |
| Capability | Capability | |
| Value Stream | Value Stream | |
| Course of Action | Course of Action | |
| Work Package | Work Package | |
| Deliverable | Deliverable | signed off, as TOGAF prescribes |
| Gap | Gap | |
| Architecture / Solution Building Block | Grouping | of the elements that make up the block |
| Transition Architecture | Plateau | |

Three of these need care. **Building blocks** have no element of their own; the specification's
recommended modelling is a grouping around the elements the block comprises. **Transition
Architecture** is a plateau, not a deliverable. And a TOGAF **deliverable** — a signed-off,
contractually specified output — is exactly the ArchiMate Deliverable, which may realize any core
element to say it implements that part of the architecture (ARCHIMATE §4.5.1, ARCHIMATE §12.2.2).

**Trap — Objective:** TOGAF's Objective (a time-bounded, measurable milestone toward a goal) is
closest to ArchiMate's **Outcome**, not Goal. Goal is the qualitative end state; Outcome is the
measurable result (ARCHIMATE §C.2).

## Where TOGAF artifacts land

A catalogue is a list of elements of one type; a matrix is a relationship table between two
types; a diagram is a view. All three are *representations* in the sense of the viewpoint
mechanism's second step, so a TOGAF artifact is a viewpoint whose representation is a catalogue,
a matrix or a diagram — for example the Actor/Role matrix is the assignment relationships of an
Organization view shown as a grid, and the Application/Technology matrix is the serving
relationships of a Technology Usage view (ARCHIMATE §13.4).

## Check yourself

- Which ArchiMate element is a Transition Architecture, and which is a TOGAF building block?
- Which viewpoints draw Phase C, and which of them is the data half?
- Why does the specification say the two standards are "complementary" rather than "overlapping"?
