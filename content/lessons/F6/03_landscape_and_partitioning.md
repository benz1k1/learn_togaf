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

<figure class="my-4">
<svg viewBox="0 0 760 234" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="The three Architecture Landscape levels as a pyramid, beside three axes that run from broad, summary and long-lived at the top to narrow, detailed and short-lived at the base">
<defs><marker id="arr-f6-11a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
<path d="M240 22 L360 22 L420 78 L180 78 Z" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="300" y="47" text-anchor="middle" font-size="13" fill="#222" font-weight="bold">Strategic</text>
<text x="300" y="65" text-anchor="middle" font-size="10" fill="#444">direction at executive level</text>
<path d="M180 82 L420 82 L480 138 L120 138 Z" fill="#e3f5e1" stroke="#7fbf7a"/>
<text x="300" y="107" text-anchor="middle" font-size="13" fill="#222" font-weight="bold">Segment</text>
<text x="300" y="125" text-anchor="middle" font-size="10" fill="#444">roadmaps at program or portfolio level</text>
<path d="M120 142 L480 142 L540 198 L60 198 Z" fill="#fff1d6" stroke="#e0b060"/>
<text x="300" y="167" text-anchor="middle" font-size="13" fill="#222" font-weight="bold">Capability</text>
<text x="300" y="185" text-anchor="middle" font-size="10" fill="#444">roadmaps for capability increments</text>
<text x="590" y="16" text-anchor="middle" font-size="11" fill="#222" font-weight="bold">Breadth</text>
<text x="590" y="40" text-anchor="middle" font-size="9" fill="#555">broad</text>
<line x1="590" y1="48" x2="590" y2="176" stroke="#555" marker-end="url(#arr-f6-11a)"/>
<text x="590" y="194" text-anchor="middle" font-size="9" fill="#555">narrow</text>
<text x="656" y="16" text-anchor="middle" font-size="11" fill="#222" font-weight="bold">Depth</text>
<text x="656" y="40" text-anchor="middle" font-size="9" fill="#555">summary</text>
<line x1="656" y1="48" x2="656" y2="176" stroke="#555" marker-end="url(#arr-f6-11a)"/>
<text x="656" y="194" text-anchor="middle" font-size="9" fill="#555">detailed</text>
<text x="722" y="16" text-anchor="middle" font-size="11" fill="#222" font-weight="bold">Time</text>
<text x="722" y="40" text-anchor="middle" font-size="9" fill="#555">valid longer</text>
<line x1="722" y1="48" x2="722" y2="176" stroke="#555" marker-end="url(#arr-f6-11a)"/>
<text x="722" y="194" text-anchor="middle" font-size="9" fill="#555">valid briefly</text>
<text x="380" y="222" text-anchor="middle" font-size="10" fill="#666">Breadth is the primary organising characteristic; Recency organises historic architectures</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">The pyramid with the organising axes beside it. Original drawing; levels per APPLY §3.2, characteristics per APPLY §3.4.</figcaption>
</figure>

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

<figure class="my-4">
<svg viewBox="0 0 760 232" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="The enterprise scope partitioned into three partitions, each with exactly one owning team, held together by integration standards and governance">
<defs><marker id="arr-f6-11b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
<rect x="15" y="12" width="730" height="150" rx="10" fill="#fafafa" stroke="#999" stroke-dasharray="6 4"/>
<text x="30" y="32" text-anchor="start" font-size="12" fill="#222" font-weight="bold">Enterprise scope — partitioned in the Preliminary Phase</text>
<rect x="35" y="46" width="220" height="66" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="145.0" y="69.5" text-anchor="middle" font-size="10" font-weight="bold">Partition 1</text>
<text x="145.0" y="82.5" text-anchor="middle" font-size="10">subject matter × time × depth</text>
<text x="145.0" y="95.5" text-anchor="middle" font-size="10">owner: standing team</text>
<rect x="75" y="120" width="140" height="24" rx="6" fill="#fff" stroke="#666"/>
<text x="145.0" y="135.5" text-anchor="middle" font-size="10">exactly one owning team</text>
<rect x="271" y="46" width="220" height="66" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/>
<text x="381.0" y="69.5" text-anchor="middle" font-size="10" font-weight="bold">Partition 2</text>
<text x="381.0" y="82.5" text-anchor="middle" font-size="10">subject matter × time × depth</text>
<text x="381.0" y="95.5" text-anchor="middle" font-size="10">owner: standing team</text>
<rect x="311" y="120" width="140" height="24" rx="6" fill="#fff" stroke="#666"/>
<text x="381.0" y="135.5" text-anchor="middle" font-size="10">exactly one owning team</text>
<rect x="507" y="46" width="220" height="66" rx="6" fill="#fff1d6" stroke="#e0b060"/>
<text x="617.0" y="69.5" text-anchor="middle" font-size="10" font-weight="bold">Partition 3</text>
<text x="617.0" y="82.5" text-anchor="middle" font-size="10">a change initiative's temporary team,</text>
<text x="617.0" y="95.5" text-anchor="middle" font-size="10">under a standing team's governance</text>
<rect x="547" y="120" width="140" height="24" rx="6" fill="#fff" stroke="#666"/>
<text x="617.0" y="135.5" text-anchor="middle" font-size="10">exactly one owning team</text>
<line x1="380" y1="162" x2="380" y2="184" stroke="#555" marker-end="url(#arr-f6-11b)"/>
<rect x="15" y="186" width="730" height="34" rx="6" fill="#f1f1f1" stroke="#999"/>
<text x="380.0" y="200.0" text-anchor="middle" font-size="10">Integration: content standards and compliance conditions in governance keep the partitions a big picture</text>
<text x="380.0" y="213.0" text-anchor="middle" font-size="10">(federated architectures in large enterprises)</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">Partitions with one owning team each, and the integration that reassembles them. Original drawing; Preliminary Phase activities per APPLY §4.2.1, integration per APPLY §4.3.</figcaption>
</figure>

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

<!-- figures:start -->
## Figures from the standard

The diagrams the cited sections carry, from your local copy of the publication. The exam reproduces these; know what each box is.

<div class="grid gap-4 md:grid-cols-2">
<figure class="max-w-lg"><img src="/figure/APPLY:fig-3-1" alt="Figure 3-1: Summary Classification Model for Architecture Landscapes" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 3-1: Summary Classification Model for Architecture Landscapes (APPLY)</figcaption></figure>
<figure class="max-w-lg"><img src="/figure/APPLY:fig-3-2" alt="Figure 3-2: Summary of Architecture Continuum" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 3-2: Summary of Architecture Continuum (APPLY)</figcaption></figure>
<figure class="max-w-lg"><img src="/figure/APPLY:fig-4-1" alt="Figure 4-1: Allocation of Teams to Architecture Scope" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 4-1: Allocation of Teams to Architecture Scope (APPLY)</figcaption></figure>
<figure class="max-w-lg"><img src="/figure/APPLY:fig-4-2" alt="Figure 4-2: Architecture Content Aggregation" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 4-2: Architecture Content Aggregation (APPLY)</figcaption></figure>
</div>
<!-- figures:end -->

## Check yourself

- Which level provides roadmaps at program or portfolio level?
- Which characteristic is the primary one for organising the landscape?
- Why must each architecture end up with exactly one owning team?
