---
title: Scoping the work — the Architecture Landscape, partitioning and superior architecture
unit: P1
objectives: ["P1.2"]
refs: ["APPLY §3.2", "APPLY §3.3", "APPLY §3.4", "APPLY §4.1", "APPLY §4.2", "APPLY §4.2.1", "APPLY §4.3", "ADM §3.3.6", "GUIDE:adm-practitioners §3.2.1", "GUIDE:adm-practitioners §6.3.6"]
reading_minutes: 10
source: authored
status: draft
---
## What a scoping scenario looks like

The scenario gives you a large enterprise — a conglomerate, a federation of agencies, a group
with acquired subsidiaries — and a Request for Architecture Work whose breadth is unclear. Two
architecture teams overlap, a division wants its own architecture, or a segment programme has
been asked to describe "everything". The question is how to scope and organise the work so that
each architecture has an owner, a level of detail and a relationship to the architectures
around it (APPLY §4.1; APPLY §4.2.1).

## Levels of the Architecture Landscape

The Landscape is divided into three levels of granularity. Strategic Architecture is an
organising framework for operational and change activity and allows direction setting at
executive level; Segment Architecture does the same at programme or portfolio level and
supports effective roadmaps there; Capability Architecture organises change activity and the
roadmaps that realise capability increments (APPLY §3.2). The Architecture Continuum then
divides each level by abstraction, from foundation elements to organisation-specific
architecture, and is the tool for finding commonality and removing redundancy (APPLY §3.2).

Broad, summary architectures set the direction for narrow, detailed ones, so every architecture
sits in a governance hierarchy. Two strategies build that hierarchy: develop the levels through
iterations within one ADM cycle, or run a hierarchy of ADM cycles concurrently; in practice a
blend is chosen to fit the Request for Architecture Work (APPLY §3.3).

## The four organising characteristics

| Characteristic | What it means for scoping | Practitioner reading |
|---|---|---|
| Breadth | subject matter; the primary organising characteristic, decomposed into segments | the most important scoping dimension; gives the context of the analysis |
| Depth | broader subject areas need less detail to stay manageable; specific areas permit and require more | develop to the *least* detail that answers the question; more detail means longer time to market |
| Time | baseline and a set of targets; broader, shallower architectures stay valid longer | the planning horizon; detailed work must conform to the guidance active at that point in time, including transition states |
| Recency | accuracy rises to approval, then decays unless maintained | a hint that prior work must be reaffirmed or replaced; unapproved architecture is "hints only" |

The left two columns follow APPLY §3.4; the right column is the Practitioners' Approach reading
of the same four characteristics (GUIDE:adm-practitioners §3.2.1).

**Trap.** Recency is not a partitioning criterion for the current landscape — it organises
*historic* architectures. And the Landscape is generally not partitioned by abstraction: the
architectures that describe it are concrete, not abstract (APPLY §4.2).

<figure class="my-4">
<svg viewBox="0 0 760 330" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="11" role="img" aria-label="Decision path for partitioning: does more than one team own the architecture, then partition until one team owns each; do units conflict or need re-use, then partition by subject, time and maturity; then define relationships and integration standards; a superior architecture constrains the detailed one">
<defs><marker id="arr-p1-02a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
<text x="380" y="20" text-anchor="middle" font-size="12" font-weight="bold">Partitioning as a decision path (Preliminary Phase)</text>
<rect x="20" y="36" width="440" height="44" rx="6" fill="#fff" stroke="#666"/>
<text x="240" y="54" text-anchor="middle">Is more than one team expected to work on a single architecture?</text>
<text x="240" y="70" text-anchor="middle" font-size="10" fill="#555">responsibilities become hard to establish</text>
<line x1="460" y1="58" x2="500" y2="58" stroke="#555" marker-end="url(#arr-p1-02a)"/>
<text x="480" y="52" text-anchor="middle" font-size="10" fill="#c0392b">yes</text>
<rect x="502" y="36" width="238" height="44" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/>
<text x="621" y="54" text-anchor="middle">Partition until each architecture</text>
<text x="621" y="70" text-anchor="middle">has exactly one owning team</text>
<line x1="240" y1="80" x2="240" y2="104" stroke="#555" marker-end="url(#arr-p1-02a)"/>
<rect x="20" y="106" width="440" height="44" rx="6" fill="#fff" stroke="#666"/>
<text x="240" y="124" text-anchor="middle">Do unit architectures conflict, or must segments be re-used?</text>
<text x="240" y="140" text-anchor="middle" font-size="10" fill="#555">the three reasons to partition</text>
<line x1="460" y1="128" x2="500" y2="128" stroke="#555" marker-end="url(#arr-p1-02a)"/>
<text x="480" y="122" text-anchor="middle" font-size="10" fill="#c0392b">yes</text>
<rect x="502" y="106" width="238" height="44" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/>
<text x="621" y="124" text-anchor="middle">Classify by subject matter, time,</text>
<text x="621" y="140" text-anchor="middle">maturity/volatility; depth for architectures</text>
<line x1="240" y1="150" x2="240" y2="174" stroke="#555" marker-end="url(#arr-p1-02a)"/>
<rect x="20" y="176" width="440" height="44" rx="6" fill="#fff" stroke="#666"/>
<text x="240" y="194" text-anchor="middle">For each partition: subject areas, level of detail,</text>
<text x="240" y="210" text-anchor="middle">time periods, stakeholders — then the relationships between them</text>
<line x1="460" y1="198" x2="500" y2="198" stroke="#555" marker-end="url(#arr-p1-02a)"/>
<rect x="502" y="176" width="238" height="44" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/>
<text x="621" y="194" text-anchor="middle">Where do they overlap or drill down?</text>
<text x="621" y="210" text-anchor="middle">What compliance is required between them?</text>
<line x1="240" y1="220" x2="240" y2="244" stroke="#555" marker-end="url(#arr-p1-02a)"/>
<rect x="20" y="246" width="720" height="70" rx="6" fill="#fff1d6" stroke="#e0b060"/>
<text x="380" y="268" text-anchor="middle" font-weight="bold">Integration: content standards, governance as a condition of compliance, a federated framework for large enterprises</text>
<text x="380" y="286" text-anchor="middle" font-size="10">the Architecture Vision summarises the Architecture Definitions, which summarise the Transition Architectures</text>
<text x="380" y="304" text-anchor="middle" font-size="10">temporary project teams come under the governance of a standing team; a superior architecture guides and constrains the detailed one</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">Original drawing. The reasons and the one-owning-team rule follow APPLY §4.1 and §4.2.1; the classification criteria APPLY §4.2; integration APPLY §4.3; superior architecture GUIDE:adm-practitioners §3.2.1.</figcaption>
</figure>

## Why and how to partition

Partitions exist to simplify development and management, and they are the foundation of
governance — distinct from levels and from the Continuum. Architectures are partitioned because
organisational-unit architectures conflict, because different teams must work on different
elements at the same time and own them, and because re-use needs modular segments that can be
lifted into broader architectures. There is no definitive partitioning model; each enterprise
adopts one that fits its operating model (APPLY §4.1).

Solutions are classified by subject matter (applications, departments, products, sites), by
time (lifecycles on a timeline) and by maturity or volatility (volatile solutions suit rapid,
agile techniques and shape investment priority); architectures are additionally classified by
depth, because detail correlates with the stakeholder groups interested — executives at the
summary end, implementation and operations staff as detail rises (APPLY §4.2).

The work happens in the Preliminary Phase. Determine the organisation structure for
architecture (standing teams, their governance bodies, membership and reporting lines);
determine each standing team's responsibilities so that the whole enterprise is partitioned and
every partition is assigned to a single team, with subject areas, level of detail, time periods
and stakeholders defined; then determine the relationships between architectures — where they
overlap, dovetail or drill down, and what compliance is required between them. Temporary teams
mobilised for a change initiative come under the governance of a standing team (APPLY §4.2.1).

**Trap.** "Give each division its own architecture team and let them proceed independently" is
only half an answer. Partitioned architectures risk becoming a fragmented collection that cannot
form a big picture; the five-point answer adds content-integration standards, governance that
treats integration as a compliance condition, and — for governments and conglomerates — a
federated framework specifying interoperability, migration and conformance principles
(APPLY §4.3).

## Scope in Phase A follows the same dimensions

When Phase A defines scope it uses exactly these characteristics: breadth of coverage, level
of detail, the partitioning characteristics, the domains to cover, the time period and any
intermediate periods, and the repository assets to leverage. Baseline and target need not be
described at the same depth; the baseline is often more abstract so that time is spent on the
target (ADM §3.3.6).

The Practitioners' Approach adds the discipline: a Request for Architecture Work bounds the
Architecture Project within the existing Landscape, work outside that breadth, horizon and
detail "is not within the scope of this architecture initiative", and where a superior
architecture exists it guides and constrains the current work. Start and finish in the
Repository — is the answer already there, is there a superior architecture, what is the
minimum needed to fill the shortfall (GUIDE:adm-practitioners §3.2.1; GUIDE:adm-practitioners §6.3.6).

## How the 5-point answer differs from the 3-point one

| Points | What the answer does |
|---|---|
| 5 | Places the request at a Landscape level, partitions by breadth, depth and time so that each partition has one owning team, names the superior architecture that constrains it, and sets integration standards and governance across partitions |
| 3 | Partitions correctly but leaves integration to chance, or partitions by organisation chart alone without defining relationships and compliance between the pieces |
| 1 | Runs one enterprise-wide cycle at capability-level detail for everything, or partitions by abstraction |
| 0 | Assigns two teams to the same architecture, or lets a temporary project team own a standing partition with no governing team |

## Where to look in the book

Applying the ADM §3.2 (the three levels and the Continuum), §3.3 (the two strategies for
hierarchies), §3.4 (breadth, depth, time, recency), §4.1 (why partition), §4.2 (classification
criteria), §4.2.1 (the Preliminary Phase steps and the one-team rule), §4.3 (integration and
federation). ADM §3.3.6 (Define Scope). Practitioners' Approach §3.2.1 (the Landscape and
superior architecture) and §6.3.6 (start in the Repository).
