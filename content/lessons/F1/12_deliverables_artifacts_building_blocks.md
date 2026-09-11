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

<figure class="my-4">
<svg viewBox="0 0 760 255" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="The Architecture Definition Document as a deliverable containing artifacts which describe the process and actor building blocks">
  <defs><marker id="arr-f1-12a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
  <rect x="10" y="10" width="440" height="215" rx="8" fill="#f3e3f7" stroke="#b58ac9"/>
  <text x="230.0" y="28" text-anchor="middle" font-size="12" font-weight="bold">Deliverable: the Architecture Definition Document (signed off)</text>
  <rect x="30" y="50" width="190" height="64" rx="6" fill="#fff" stroke="#666"/>
  <text x="125" y="71.85" text-anchor="middle" font-size="11" font-weight="bold">Artifact: process flow</text>
  <text x="125" y="85.85" text-anchor="middle" font-size="11" fill="#345">diagram</text>
  <text x="125" y="99.85" text-anchor="middle" font-size="11" fill="#345">(a diagram)</text>
  <rect x="30" y="130" width="190" height="64" rx="6" fill="#fff" stroke="#666"/>
  <text x="125" y="158.85" text-anchor="middle" font-size="11" font-weight="bold">Artifact: actor catalog</text>
  <text x="125" y="172.85" text-anchor="middle" font-size="11" fill="#345">(a catalog)</text>
  <text x="335" y="122" text-anchor="middle" font-size="11" fill="#345">several complementary</text>
  <text x="335" y="137" text-anchor="middle" font-size="11" fill="#345">artifacts, each one aspect</text>
  <text x="230" y="210" text-anchor="middle" font-size="11" fill="#345">catalog (list) | matrix (grid) | diagram (picture)</text>
  <rect x="480" y="10" width="270" height="215" rx="8" fill="#e3f5e1" stroke="#7fbf7a"/>
  <text x="615.0" y="28" text-anchor="middle" font-size="12" font-weight="bold">Building blocks: what the artifacts describe</text>
  <rect x="495" y="60" width="240" height="44" rx="6" fill="#fff" stroke="#666"/>
  <text x="615" y="78.85" text-anchor="middle" font-size="11" font-weight="bold">target call-handling process</text>
  <text x="615" y="92.85" text-anchor="middle" font-size="11" fill="#345">a business process building block</text>
  <rect x="495" y="130" width="240" height="44" rx="6" fill="#fff" stroke="#666"/>
  <text x="615" y="148.85" text-anchor="middle" font-size="11" font-weight="bold">Customer Services Representative</text>
  <text x="615" y="162.85" text-anchor="middle" font-size="11" fill="#345">an actor: a further building block</text>
  <line x1="220" y1="82" x2="493" y2="82" stroke="#555" marker-end="url(#arr-f1-12a)"/>
  <path d="M220 95 L460 95 L460 145 L493 145" fill="none" stroke="#555" marker-end="url(#arr-f1-12a)"/>
  <line x1="220" y1="162" x2="493" y2="162" stroke="#555" marker-end="url(#arr-f1-12a)"/>
  <text x="350" y="74" text-anchor="middle" font-size="10" fill="#666">describes</text>
  <text x="350" y="178" text-anchor="middle" font-size="10" fill="#666">describes</text>
  <text x="380" y="245" text-anchor="middle" font-size="11" fill="#666">deliverable contains artifact; artifact describes building block; never the other way round</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">The standard's worked example drawn as containment and description. Original drawing; the example follows INTRO §3.6.</figcaption>
</figure>

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

<figure class="my-4">
<svg viewBox="0 0 760 260" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="Side-by-side cards comparing Architecture Building Blocks and Solution Building Blocks, with the network example">
  <defs><marker id="arr-f1-12b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
  <rect x="10" y="10" width="335" height="195" rx="8" fill="#e0ecff" stroke="#7aa2e3"/>
  <text x="177.5" y="28" text-anchor="middle" font-size="12" font-weight="bold">Architecture Building Block (ABB)</text>
  <text x="177" y="50" text-anchor="middle" font-size="11" fill="#345">lives on the Architecture Continuum</text>
  <text x="177" y="67" text-anchor="middle" font-size="11" fill="#345">defined or selected through the ADM</text>
  <text x="177" y="84" text-anchor="middle" font-size="11" fill="#345">logical, supplier-independent</text>
  <text x="177" y="101" text-anchor="middle" font-size="11" fill="#345">captures Business, Data, Application</text>
  <text x="177" y="118" text-anchor="middle" font-size="11" fill="#345">and Technology requirements</text>
  <text x="177" y="135" text-anchor="middle" font-size="11" fill="#345">directs and guides SBB development</text>
  <rect x="415" y="10" width="335" height="195" rx="8" fill="#e3f5e1" stroke="#7fbf7a"/>
  <text x="582.5" y="28" text-anchor="middle" font-size="12" font-weight="bold">Solution Building Block (SBB)</text>
  <text x="582" y="50" text-anchor="middle" font-size="11" fill="#345">lives on the Solutions Continuum</text>
  <text x="582" y="67" text-anchor="middle" font-size="11" fill="#345">procured or developed</text>
  <text x="582" y="84" text-anchor="middle" font-size="11" fill="#345">product- or vendor-aware</text>
  <text x="582" y="101" text-anchor="middle" font-size="11" fill="#345">defines which products and components</text>
  <text x="582" y="118" text-anchor="middle" font-size="11" fill="#345">implement the functionality</text>
  <text x="582" y="135" text-anchor="middle" font-size="11" fill="#345">fulfils the business requirements</text>
  <line x1="347" y1="108" x2="413" y2="108" stroke="#555" marker-end="url(#arr-f1-12b)"/>
  <text x="380" y="98" text-anchor="middle" font-size="10" fill="#666">specifies</text>
  <text x="380" y="168" text-anchor="middle" font-size="10" fill="#666">realises</text>
  <line x1="413" y1="155" x2="347" y2="155" stroke="#555" marker-end="url(#arr-f1-12b)"/>
  <rect x="10" y="220" width="740" height="30" rx="6" fill="#f4f4f4" stroke="#bbb"/>
  <text x="380" y="238.85" text-anchor="middle" font-size="11" fill="#345">example: a network (ABB) may be realised by many microsatellites or by a few large ones (two different SBBs)</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">ABB and SBB side by side. Original drawing; the attributes follow CONTENT §5.2.3 and CONTENT §5.2.4.</figcaption>
</figure>

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

<!-- figures:start -->
## Figures from the standard

The diagrams the cited sections carry, from your local copy of the publication. The exam reproduces these; know what each box is.

<div class="grid gap-4 md:grid-cols-2">
<figure class="max-w-lg"><img src="/figure/CONTENT:fig-3-3" alt="Figure 3-3: Interactions between Metamodel, Building Blocks, Diagrams, and Stakeholders" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 3-3: Interactions between Metamodel, Building Blocks, Diagrams, and Stakeholders (CONTENT)</figcaption></figure>
<figure class="max-w-lg"><img src="/figure/CONTENT:fig-3-4" alt="Figure 3-4: Artifacts Associated with the Enterprise Metamodel" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 3-4: Artifacts Associated with the Enterprise Metamodel (CONTENT)</figcaption></figure>
<figure class="max-w-lg"><img src="/figure/CONTENT:fig-5-1" alt="Figure 5-1: Key ADM Phases/Steps at which Building Blocks are Evolved/Specified" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 5-1: Key ADM Phases/Steps at which Building Blocks are Evolved/Specified (CONTENT)</figcaption></figure>
<figure class="max-w-lg"><img src="/figure/INTRO:fig-3-2" alt="Figure 3-2: Relationships between Deliverables, Artifacts, and Building Blocks" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 3-2: Relationships between Deliverables, Artifacts, and Building Blocks (INTRO)</figcaption></figure>
<figure class="max-w-lg"><img src="/figure/INTRO:fig-3-3" alt="Figure 3-3: Example — Architecture Definition Document" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 3-3: Example — Architecture Definition Document (INTRO)</figcaption></figure>
</div>
<!-- figures:end -->

## Check yourself

- A CRUD table of applications against data entities: catalog, matrix or diagram?
- Which of the three categories is "contractually specified"?
- Which building block type is vendor-aware, and which continuum does it belong to?
- In which phases does most building block definition take place?
