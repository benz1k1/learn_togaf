---
title: The Architecture Landscape levels, and Architecture Partitioning
unit: F6
objectives: ["6.2"]
refs: ["APPLY §3.1", "APPLY §3.2", "APPLY §3.3", "APPLY §3.4", "APPLY §4.1", "APPLY §4.2", "APPLY §4.2.1", "APPLY §4.3"]
reading_minutes: 9
source: authored
status: draft
---
## Levels of the Architecture Landscape

Many architectures coexist in an enterprise's landscape at any time — specific and general,
detailed and big-picture. The standard organises them with two concepts, **levels** and the
**Enterprise Continuum**, which tie to how content is held in the Architecture Repository and to
partitions (APPLY §3.1).

| Level | What it provides |
|---|---|
| **Strategic Architecture** | An organising framework for operational and change activity, and direction-setting at **executive** level |
| **Segment Architecture** | The same framework plus effective roadmaps at **program or portfolio** level |
| **Capability Architecture** | An organising framework for change activity and roadmaps that realise **capability increments** |

(APPLY §3.2)

The Architecture Continuum divides each level by **abstraction** — from foundation elements to
organisation-specific architecture — giving a consistent way to define generic rules,
representations, traceability and derivation, and it helps discover commonality and remove
redundancy. Levels plus the Continuum classify the landscape into related architectures with
manageable complexity, defined groupings, hierarchies and navigation, and processes, roles and
responsibilities per grouping. There is **no definitive organising model** — each enterprise
adopts one that reflects its operating model (APPLY §3.2).

> **Trap.** The levels are not the domains: Business, Data, Application and Technology
> architectures can exist at every level. And "Solution Architecture" is not a landscape level
> (APPLY §3.2).

Different architectures serve different stakeholder needs and sit in a governance hierarchy:
broad, summary architectures set direction for narrow, detailed ones. Two strategies let the ADM
support such hierarchies — develop the levels through **iterations within a single ADM cycle**,
or through a **hierarchy of ADM processes executed concurrently** — and in practice an architect
blends both to fit the Request for Architecture Work (APPLY §3.3).

### Organising the landscape

| Characteristic | Role |
|---|---|
| **Breadth** | Subject matter — generally the *primary* organising characteristic; architectures decompose into a hierarchy of subject areas or segments |
| **Depth** | Broader subject areas need less detail to stay manageable; narrower ones permit and require more |
| **Time** | For a given breadth and depth there is a baseline and a set of targets stretching into the future; broader, less detailed architectures stay valid longer |
| **Recency** | An architecture gains accuracy until approved, then loses accuracy unless maintained; recency may organise historic architectures |

Using these, architectures group into the Strategic, Segment and Capability levels (APPLY §3.4).

## Architecture Partitioning

Partitions simplify developing and managing the Enterprise Architecture. They lie at the
foundation of Architecture Governance and are **distinct from levels and from the Architecture
Continuum**. Architectures are partitioned because organisational-unit architectures conflict,
because different teams must work on different elements at the same time and own them, and because
re-use needs modular segments that can be incorporated into broader architectures. There is no
definitive partitioning model; each enterprise reflects its own operating model (APPLY §4.1).

### Classification criteria

Partitioning organises the Enterprise Continuum into related solutions and architectures with
manageable complexity, defined groupings, hierarchies and navigation, and attached roles
(APPLY §4.2).

| Criterion | Used to partition… | How |
|---|---|---|
| Subject matter (breadth) | Solutions | Applications, departments, products, services, sites — the fundamental structuring technique |
| Time | Solutions | Lifecycle on a timeline: development, introduction, operation, retirement against other activity |
| Maturity / volatility | Solutions | Volatile, immature solutions need faster lifecycles and may suit agile techniques; shapes investment priority |
| Depth | Architectures | Level of detail correlates with audience — executives want less detail, implementers more |

Two characteristics are generally **not** used: abstraction (landscape architectures are generally
not abstract) and far-future or historic time, because volatility limits how far ahead an
architecture can be defined and erodes the accuracy of old ones (APPLY §4.2).

### Partitioning in the Preliminary Phase

Establishing the Architecture Capability means establishing partitions with defined boundaries,
governance and ownership. Each team owns one or more partitions and runs the ADM on them; when
several teams work on one architecture responsibilities blur, so partition until **each
architecture has one owning team**. Temporary teams set up for a change initiative should sit
under the governance of a standing team. The Preliminary Phase steps are: determine the
organisation structure for architecture (standing teams, governance bodies, membership, reporting
lines); determine each team's responsibilities, partitioning the whole enterprise scope and
defining each architecture's subject matter, level of detail, time periods and stakeholders; and
determine the relationships between architectures — overlaps, drill-downs and compliance
requirements. The Enterprise layer is defined by the corporate and segment EA capabilities, the
Segment layer with the portfolio team, and the Capability layer by the portfolio and project teams
(APPLY §4.2.1).

### Integration

Partitioning risks a fragmented set of architectures that cannot be integrated into a big picture.
Large complex enterprises — governments and conglomerates — typically use **federated
architectures**: independently developed and managed, then integrated within a framework that sets
principles for interoperability, migration and conformance. Mitigation is to define content
integration standards and make integration a condition of compliance in governance, using a
content framework to specify standard building blocks and artifacts (a shared process catalog, for
example). Integration is addressed across domains (a cross-domain view of a segment at a point in
time), across organisational scope (a cross-segment view), and through the Architecture Vision
summarising the Architecture Definitions, which summarise the Transition Architectures
(APPLY §4.3).

## Check yourself

- Which level provides roadmaps at program or portfolio level?
- Which characteristic is the primary one for organising the landscape?
- Why must each architecture end up with exactly one owning team?
