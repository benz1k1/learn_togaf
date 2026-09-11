---
title: Deliverables, artifacts and building blocks
unit: F1
objectives: ["1.4"]
refs: ["INTRO §3.6", "INTRO §4.23", "INTRO §4.26", "INTRO §4.40", "CONTENT §3.6.1", "CONTENT §4.1", "CONTENT §5.2.2", "CONTENT §5.2.3", "CONTENT §5.2.4", "CONTENT §5.3.1", "CONTENT §5.3.2"]
reading_minutes: 9
source: authored
status: draft
---
## Three categories of work product

Running the ADM produces a stream of outputs: process flows, requirements, project plans,
compliance assessments and more. The Architecture Content Framework gives those outputs a
consistent structure by sorting every architectural work product into one of three categories,
according to how it is used (INTRO §3.6).

| Category | One-line meaning | Examples |
|---|---|---|
| **Deliverable** | a work product that is contractually specified, then formally reviewed, agreed and signed off by stakeholders | Architecture Definition Document, Statement of Architecture Work |
| **Artifact** | a work product describing *one aspect* of the architecture | requirements catalog, application interaction matrix, value chain diagram |
| **Building block** | a potentially reusable component that can be combined with others to deliver architectures and solutions | a "customer services" capability, a network, a business service called "Purchase Order" |

Deliverables are the output of *projects*; when they take the form of documents they are usually
archived at project end or moved into the Architecture Repository as a reference model, a standard,
or a snapshot of the Architecture Landscape at a point in time (INTRO §3.6, INTRO §4.40).

Artifacts fall into three kinds: **catalogs** (lists of things), **matrices** (relationships
between things) and **diagrams** (pictures of things). A deliverable may contain one or more
artifacts, artifacts make up the content of the Architecture Repository, and whether a given
artifact also counts as a deliverable depends entirely on what the contract specifies
(INTRO §3.6, INTRO §4.23).

Building blocks can be described at whatever level of detail suits the stage of development: a
name or an outline early on, later decomposed into supporting blocks with a full specification.
They come in two flavours, tied to architectures and to solutions respectively (INTRO §3.6,
INTRO §4.26).

## How the three relate

The standard's worked example is the Architecture Definition Document: a *deliverable* that
documents an architecture description. Inside it sit several complementary *artifacts*, which are
views of the *building blocks* the architecture is about. A process flow diagram (artifact) can
describe the target call-handling process (a building block) and, at the same time, the actors
involved in it such as a Customer Services Representative (further building blocks) (INTRO §3.6).

> **Trap.** The direction of containment. Deliverables contain artifacts; artifacts describe
> building blocks. A building block is never "a kind of artifact", and an artifact is not
> automatically a deliverable.

The exam also likes to ask *where* the detail lives: the Architecture Content document holds the
detailed descriptions of deliverables, artifacts and building blocks, and the phase descriptions
carry summary lists of the deliverables and artifacts each phase may create (INTRO §3.6).

## Catalogs, matrices and diagrams versus the metamodel

Most stakeholders do not care about the metamodel; they want answers such as "which processes does
this project affect?". Building blocks, catalogs, matrices and diagrams exist to serve them
(CONTENT §3.6.1):

- A **building block** is an entity of a particular metamodel type (a business service, an actor)
  carrying metadata according to the metamodel, so it can be queried, for example all business
  services owned by one organisation.
- A **catalog** is a list of building blocks of one type or of related types, kept for governance or
  reference; an organisation chart of locations and actors is the example given.
- A **matrix** is a grid showing relationships between two or more model entities, used where the
  relationship is naturally list-like rather than graphical; the CRUD matrix of which applications
  create, read, update and delete a data type is the example.
- A **diagram** renders content graphically so stakeholders can retrieve what they need, and can
  also be used to populate content or check completeness. One diagram type may be drawn several
  times with different styles or coverage for different stakeholders.

On-demand queries of the repository can generate ad hoc catalogs, matrices and diagrams; because
such queries must stay flexible, they are not fixed by the metamodel (CONTENT §3.6.1).

## What makes a building block

A building block is a package of functionality defined to meet a business need across the
organisation; it normally has a type matching the metamodel (actor, business service, application,
data entity); it has a defined boundary and is recognisable as "a thing" by domain experts; and it
may interoperate with other blocks (CONTENT §5.2.2). A *good* block considers implementation and
usage and evolves to exploit technology and standards, can be assembled from other blocks, can be a
sub-assembly of others, and is ideally reusable, replaceable and well specified (CONTENT §5.2.2).

The boundary and specification should be loosely coupled to the implementation, so a block can be
realised several ways without changing its boundary; and because systems are assembled from many
blocks, published and reasonably stable interfaces matter (CONTENT §5.2.2). Less detail can be
worth more: a single clear picture of enterprise capabilities beats a dense hundred-page
specification when the audience is executives (CONTENT §5.2.2).

## ABBs and SBBs

| | Architecture Building Block (ABB) | Solution Building Block (SBB) |
|---|---|---|
| Relates to | the Architecture Continuum | the Solutions Continuum |
| Origin | defined or selected through the ADM | procured or developed |
| Role | captures Business, Data, Application and Technology requirements; directs and guides SBB development | defines which products and components implement the functionality; defines the implementation; fulfils business requirements |
| Awareness | logical, supplier-independent | product- or vendor-aware |
| Specification includes | fundamental functionality and attributes (incl. security and manageability), chosen interfaces, interoperability with other blocks, dependent blocks, mapping to business entities and policies | specific functionality, implemented interfaces, required SBBs, mapping to IT topology and operational policies, shared attributes (security, manageability, scalability), performance and configurability, design drivers and constraints, relationship to ABBs |

(CONTENT §5.2.3, CONTENT §5.2.4.) The standard's illustration: a network is an ABB that may be
realised by very different SBBs, such as a satellite network built from many microsatellites or
from a few large ones (INTRO §3.6).

## Building blocks in the ADM

An architecture *is* a set of building blocks shown in a model, plus a specification of how they
connect to meet the business requirements. Three principles apply: include only the blocks relevant
to the business problem; expect complex many-to-many relationships between blocks; and make blocks
conform to the standards for their type and to enterprise principles and standards
(CONTENT §5.3.1). When identifying blocks, consider three classes: reusable ones such as legacy
items, ones to be developed such as new applications, and ones to be purchased (COTS)
(CONTENT §5.3.1).

Block definition happens gradually, mainly in Phases A to D, as an evolutionary and iterative
process: the ABBs needed to meet the business goals are identified first, then refined into a set
of SBBs that can be bought off the shelf or custom built (CONTENT §5.3.2).

## Deliverables across the cycle

Deliverables are the contractual or formal work products of an architecture project, so any
overarching project method such as CMMI, PRINCE2, PMBOK or MSP is likely to constrain or alter
them; the standard's list is a typical baseline to tailor from (CONTENT §4.1). The Content
Framework identifies deliverables that are produced by ADM phases and consumed as inputs by others;
a few are produced outside the ADM and only consumed by it (CONTENT §4.1).

## Check yourself

- A CRUD table of applications against data entities: catalog, matrix or diagram?
- Which of the three categories is "contractually specified"?
- Which building block type is vendor-aware, and which continuum does it belong to?
- In which phases does most building block definition take place?
