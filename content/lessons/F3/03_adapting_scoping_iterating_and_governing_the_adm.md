---
title: Adapting, scoping, iterating and governing the ADM
unit: F3
objectives: ["3.2"]
refs: ["ADM §1.3", "ADM §1.4", "ADM §1.5", "ADM §1.5.1", "ADM §1.5.2", "ADM §1.5.3", "ADM §1.5.4", "ADM §1.6", "ADM §1.7", "ADM §1.8", "APPLY §2.1", "APPLY §2.2", "APPLY §2.3", "APPLY §2.4", "APPLY §2.5", "APPLY §2.5.1", "APPLY §2.5.2", "APPLY §2.6"]
reading_minutes: 10
source: authored
status: draft
---
## Adapting the ADM

The ADM is generic and copes with most needs, but it will often have to be modified or extended.
Before using it, review its components for applicability and tailor them to the enterprise; the
result may be an "enterprise-specific" ADM (ADM §1.3). The reasons the standard gives, and the
exam asks for, are:

| Reason | What it means |
|---|---|
| **Architecture maturity** | the *order* of phases depends partly on how mature the discipline is; if the case for architecture is not yet accepted, a Vision is essential and a detailed Business Architecture usually comes next to underpin it and win stakeholder participation; elsewhere a baseline inventory may come first |
| **Principles** | business principles may dictate that processes adapt to a packaged solution, in which case Business Architecture may *follow* the Information Systems or Technology Architecture |
| **Integration with another framework** | e.g. using the ADM alongside Zachman or a vertical-sector framework with its own deliverables; the ADM is designed for this |
| **Corporate governance** | the ADM is one of many corporate processes and must sit beside authorisation, risk, budgeting, systems development and procurement processes |
| **Outsourcing** | a prime contractor mandates the ADM and must reconcile its own practices with the client's requirements |
| **Small-to-medium enterprise** | a cut-down method suited to fewer resources and simpler systems |
| **Very large, complex enterprise** | many interlinked enterprises in one collaborative framework; planning may be top-down, via a generic reference architecture that each enterprise adapts, or by replication of a proven instance |
| **Vendor / product line** | a generic architecture for a family of products (Product Line Architecture), developed by an analogous process |

The phase descriptions list deliverables and artifacts applicable to any enterprise; those too
must be adapted to the enterprise's needs, which is done through the Content Framework and
Enterprise Metamodel in the Architecture Content document (ADM §1.3). The ADM can also be adapted
to an Agile delivery style; the Enabling Enterprise Agility and Agile Sprints guides, Applying the
ADM, and the Practitioners' Approach guide carry the detail (ADM §1.3).

## Governance of the method itself

Whether adapted or not, the ADM is itself a key process, managed like any other artifact that the
Enterprise Continuum classifies and the Architecture Repository holds. The **Architecture Board**
should satisfy itself that the method is applied correctly across every
phase; compliance with the ADM is fundamental to governance, ensuring all considerations are made
and all required deliverables produced (ADM §1.4). Artifacts, governance and related processes
need a controlled environment, typically repositories with versioned objects, process control and
status (ADM §1.4).

A governance repository manages three kinds of information (ADM §1.4):

- **Reference data**: collateral from the organisation's own repositories and the continuum,
  including external material such as COBIT or IT4IT, used for guidance during implementation;
  it includes a description of the governance procedures themselves.
- **Process status**: the state of any governance process, such as outstanding compliance requests,
  dispensation requests and compliance assessment investigations.
- **Audit information**: completed governance actions, recording key decisions and responsible
  people for sanctioned projects and serving as precedent for future work.

The governance artifacts and process are themselves part of the Architecture Repository (ADM §1.4).

## Scoping the architecture

Scope is constrained for three kinds of reason: the organisational authority of the team, the
objectives and stakeholder concerns to be addressed, and the availability of people, money and
other resources (ADM §1.5). The chosen scope should let all architects' work be governed and
integrated, which needs aligned **architecture partitions** so nobody duplicates or conflicts,
with reuse and compliance relationships defined between them (ADM §1.5).

Four dimensions define and limit scope (ADM §1.5). Scope is usually expressed first in breadth,
depth and time, and then the right combination of domains is chosen (ADM §1.5).

| Dimension | The question it answers |
|---|---|
| **Breadth** | how far does the enterprise extend, and how much of that extent will this effort cover? |
| **Depth** | how much detail; how much architecture is enough; where architecture stops and design or engineering begins? |
| **Time period** | what period does the Vision cover; can the detailed description cover the same period; how many Transition Architectures and over what periods? |
| **Architecture domains** | which of Business, Data, Application and Technology are in scope? |

<figure class="my-4">
<svg viewBox="0 0 760 250" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="Four panels for the four scope dimensions: breadth as a subset of the enterprise, depth as where architecture stops, time period as a horizon with transitions, and the domain mix">
  <defs><marker id="arr-f3-11a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
  <rect x="10" y="10" width="175" height="205" rx="8" fill="#e0ecff" stroke="#7aa2e3"/>
  <text x="97.5" y="28" text-anchor="middle" font-size="12" font-weight="bold">Breadth</text>
  <rect x="22" y="45" width="24" height="24" rx="3" fill="#fff" stroke="#666"/>
  <rect x="49" y="45" width="24" height="24" rx="3" fill="#fff1d6" stroke="#e0b060"/>
  <rect x="76" y="45" width="24" height="24" rx="3" fill="#fff1d6" stroke="#e0b060"/>
  <rect x="103" y="45" width="24" height="24" rx="3" fill="#fff1d6" stroke="#e0b060"/>
  <rect x="130" y="45" width="24" height="24" rx="3" fill="#fff" stroke="#666"/>
  <rect x="157" y="45" width="24" height="24" rx="3" fill="#fff" stroke="#666"/>
  <path d="M49 40 L49 34 L127 34 L127 40" fill="none" stroke="#c0392b"/>
  <text x="97" y="90" text-anchor="middle" font-size="11" fill="#345">how much of the enterprise</text>
  <text x="97" y="105" text-anchor="middle" font-size="11" fill="#345">does this effort cover?</text>
  <text x="97" y="130" text-anchor="middle" font-size="11" fill="#345">large enterprises federate</text>
  <text x="97" y="145" text-anchor="middle" font-size="11" fill="#345">several architectures under</text>
  <text x="97" y="160" text-anchor="middle" font-size="11" fill="#345">one integration framework</text>
  <rect x="200" y="10" width="175" height="205" rx="8" fill="#e3f5e1" stroke="#7fbf7a"/>
  <text x="287.5" y="28" text-anchor="middle" font-size="12" font-weight="bold">Depth</text>
  <rect x="215" y="40" width="145" height="22" rx="3" fill="#fff1d6" stroke="#e0b060"/>
  <text x="287.5" y="54.5" text-anchor="middle" font-size="10" fill="#345">architecture</text>
  <rect x="215" y="67" width="145" height="22" rx="3" fill="#fff1d6" stroke="#e0b060"/>
  <text x="287.5" y="81.5" text-anchor="middle" font-size="10" fill="#345">architecture</text>
  <rect x="215" y="94" width="145" height="22" rx="3" fill="#fff1d6" stroke="#e0b060"/>
  <text x="287.5" y="108.5" text-anchor="middle" font-size="10" fill="#345">architecture</text>
  <rect x="215" y="121" width="145" height="22" rx="3" fill="#fff" stroke="#666"/>
  <text x="287.5" y="135.5" text-anchor="middle" font-size="10" fill="#345">design</text>
  <rect x="215" y="148" width="145" height="22" rx="3" fill="#fff" stroke="#666"/>
  <text x="287.5" y="162.5" text-anchor="middle" font-size="10" fill="#345">engineering</text>
  <path d="M212 121 L363 121" fill="none" stroke="#c0392b" stroke-dasharray="5 4"/>
  <text x="287" y="190" text-anchor="middle" font-size="11" fill="#345">how much detail; where does</text>
  <text x="287" y="205" text-anchor="middle" font-size="11" fill="#345">architecture stop?</text>
  <rect x="390" y="10" width="175" height="205" rx="8" fill="#fff1d6" stroke="#e0b060"/>
  <text x="477.5" y="28" text-anchor="middle" font-size="12" font-weight="bold">Time period</text>
  <line x1="405" y1="60" x2="550" y2="60" stroke="#555" marker-end="url(#arr-f3-11a)"/>
  <rect x="400" y="48" width="40" height="24" rx="3" fill="#fff" stroke="#666"/>
  <text x="420" y="63.5" text-anchor="middle" font-size="10" fill="#345">now</text>
  <rect x="455" y="48" width="34" height="24" rx="3" fill="#fff" stroke="#666"/>
  <text x="472" y="63.5" text-anchor="middle" font-size="10" fill="#345">T1</text>
  <rect x="495" y="48" width="34" height="24" rx="3" fill="#fff" stroke="#666"/>
  <text x="512" y="63.5" text-anchor="middle" font-size="10" fill="#345">T2</text>
  <rect x="515" y="85" width="45" height="24" rx="3" fill="#e3f5e1" stroke="#7fbf7a"/>
  <text x="537.5" y="100.5" text-anchor="middle" font-size="10" fill="#345">Target</text>
  <path d="M537 72 L537 83" fill="none" stroke="#555"/>
  <text x="477" y="130" text-anchor="middle" font-size="11" fill="#345">what horizon does the Vision</text>
  <text x="477" y="145" text-anchor="middle" font-size="11" fill="#345">cover; how many Transition</text>
  <text x="477" y="160" text-anchor="middle" font-size="11" fill="#345">Architectures, over what</text>
  <text x="477" y="175" text-anchor="middle" font-size="11" fill="#345">periods?</text>
  <rect x="580" y="10" width="170" height="205" rx="8" fill="#f3e3f7" stroke="#b58ac9"/>
  <text x="665.0" y="28" text-anchor="middle" font-size="12" font-weight="bold">Architecture domains</text>
  <rect x="595" y="40" width="140" height="24" rx="3" fill="#fff1d6" stroke="#e0b060"/>
  <text x="665" y="55.5" text-anchor="middle" font-size="10" fill="#345">Business  in scope</text>
  <rect x="595" y="70" width="140" height="24" rx="3" fill="#fff1d6" stroke="#e0b060"/>
  <text x="665" y="85.5" text-anchor="middle" font-size="10" fill="#345">Data  in scope</text>
  <rect x="595" y="100" width="140" height="24" rx="3" fill="#fff" stroke="#666"/>
  <text x="665" y="115.5" text-anchor="middle" font-size="10" fill="#345">Application  out</text>
  <rect x="595" y="130" width="140" height="24" rx="3" fill="#fff1d6" stroke="#e0b060"/>
  <text x="665" y="145.5" text-anchor="middle" font-size="10" fill="#345">Technology  in scope</text>
  <text x="665" y="180" text-anchor="middle" font-size="11" fill="#345">which of the four are in?</text>
  <text x="665" y="195" text-anchor="middle" font-size="11" fill="#345">chosen last</text>
  <text x="380" y="238" text-anchor="middle" font-size="11" fill="#666">scope is usually stated as breadth, depth and time first, then the right combination of domains is chosen</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">The four dimensions of scope, one panel each. Original drawing; the dimensions follow ADM §1.5.</figcaption>
</figure>

In each dimension there is a danger of optimising within one's own scope instead of at enterprise
level; it is often necessary to sub-optimise locally to optimise the whole, always seeking the
highest commonality and reusable modules (ADM §1.5).

**Breadth** (ADM §1.5.1): large enterprises typically have several architectures for different
timeframes, functions or requirements, combined as a *federation* under an integration framework
that sets the principles for interoperability, migration and conformance. A publish-and-subscribe
model brings this under governance: producers and consumers of architecture sign up to a framework
that keeps material good, current and published, and monitors usage through a Compliance
Assessment process and a dispensation process for justified exceptions.

**Depth** (ADM §1.5.2): judge detail by intended use and the decisions to be made; keep an equal
depth across the domains in scope; enough for the purpose and no more; structure for future
tailoring and reuse; too broad a scope deters stakeholders who see no return.

**Time period** (ADM §1.5.3): the ADM is described as one cycle producing a Vision and a set of
Target Architectures. A wider view has several architecture instances, a baseline, a possibly
partial target end-state, and Transition Architectures between them. Target work is then staged:
first Target descriptions for the whole system over a distant horizon (six years is the example),
then Transition Architectures as increments converging on it. Targets are evolutionary and
periodically reviewed; Transitions are incremental and, by design, should *not* change during
their implementation, to avoid a "moving target", which works only when implementation is under
tight control and short (typically under two years). Detailed decisions are deliberately postponed
into the Transitions. The ultimate vision may never be reached as first described.

**Domains** (ADM §1.5.4): covered in unit F1; an architecture missing a domain is not a complete
enterprise architecture, and the trade-off must be communicated.

## Alternatives and integration

There is usually more than one Target Architecture that would satisfy the Vision, principles and
requirements, so alternatives and their trade-offs should be identified and presented; doing so
draws out hidden agendas, principles and requirements (ADM §1.6). The technique, from ADM
Techniques, defines alternatives per domain to simplify analysis, then merges them: first select
criteria from vision, principles and requirements; second define alternatives against the criteria;
third select one or combine features from several. It works in any phase at any level (ADM §1.6).

Architectures built for subsets of the enterprise need a consistent frame of reference so they can
be treated as a group. The dimensions that scope one architecture are the same dimensions that
govern integrating many. Today integration is achievable only at the low end of the
"integratability" spectrum; granularity, level of detail and the maturity of interchange standards
are the key factors, and standards governance will always be needed to limit manual
co-ordination (ADM §1.7).

The chapter's summary: the ADM recommends a sequence but cannot recommend a scope; the enterprise
decides scope, knowing the process is iterative, that depth and breadth grow with each iteration,
and that each iteration adds to the repository. Focus on what creates value and choose horizontal
and vertical scope and time periods accordingly (ADM §1.8).

## Iteration

The ADM graphic and the phase chapters read like a waterfall, but that is only a presentation
device; in practice **iteration** and **levels** manage the complexity, and the two are tightly
linked (APPLY §2.1). Iteration means three different things (APPLY §2.1):

1. describing a comprehensive Architecture Landscape through **multiple ADM cycles**, each bound
   by a Request for Architecture Work; separate projects may run cycles concurrently, and one
   project may trigger another when it finds impacts outside its own request;
2. **iteration within a cycle** (Architecture Development iteration): running several phases
   concurrently (typically B, C and D), cycling between phases in planned loops to converge on a
   target when no higher-level architecture constrains it, and returning to earlier phases to
   update work products, typically to converge on an executable Roadmap or Migration Plan;
3. **managing the Architecture Capability**: a new pass through the Preliminary Phase to
   (re-)establish the capability identified in Phase A, or to adjust it after a Phase H Change
   Request.

<figure class="my-4">
<svg viewBox="0 0 760 262" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="Three panels for the three meanings of iteration: multiple ADM cycles, iteration between and within phases of one cycle, and re-entering the Preliminary Phase to manage the capability">
  <defs><marker id="arr-f3-11b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
  <rect x="10" y="10" width="235" height="220" rx="8" fill="#e0ecff" stroke="#7aa2e3"/>
  <text x="127.5" y="28" text-anchor="middle" font-size="12" font-weight="bold">1  Multiple ADM cycles</text>
  <circle cx="60" cy="80" r="26" fill="#fff" stroke="#666"/>
  <text x="60" y="84" text-anchor="middle" font-size="10">cycle</text>
  <circle cx="127" cy="80" r="26" fill="#fff" stroke="#666"/>
  <text x="127" y="84" text-anchor="middle" font-size="10">cycle</text>
  <circle cx="194" cy="80" r="26" fill="#fff" stroke="#666"/>
  <text x="194" y="84" text-anchor="middle" font-size="10">cycle</text>
  <line x1="88" y1="80" x2="99" y2="80" stroke="#555" marker-end="url(#arr-f3-11b)"/>
  <line x1="155" y1="80" x2="166" y2="80" stroke="#555" marker-end="url(#arr-f3-11b)"/>
  <text x="127" y="125" text-anchor="middle" font-size="11" fill="#345">each bound by a Request for</text>
  <text x="127" y="140" text-anchor="middle" font-size="11" fill="#345">Architecture Work; one project's</text>
  <text x="127" y="155" text-anchor="middle" font-size="11" fill="#345">findings can trigger another;</text>
  <text x="127" y="170" text-anchor="middle" font-size="11" fill="#345">together they describe the</text>
  <text x="127" y="185" text-anchor="middle" font-size="11" fill="#345">whole Architecture Landscape</text>
  <text x="127" y="215" text-anchor="middle" font-size="10" fill="#c0392b">the outermost level</text>
  <rect x="262" y="10" width="235" height="220" rx="8" fill="#e3f5e1" stroke="#7fbf7a"/>
  <text x="379.5" y="28" text-anchor="middle" font-size="12" font-weight="bold">2  Iteration within a cycle</text>
  <rect x="275" y="45" width="55" height="34" rx="6" fill="#fff" stroke="#666"/>
  <text x="302.5" y="65.85" text-anchor="middle" font-size="11" font-weight="bold">A</text>
  <rect x="340" y="45" width="45" height="34" rx="6" fill="#fff1d6" stroke="#e0b060"/>
  <text x="362.5" y="65.85" text-anchor="middle" font-size="11" font-weight="bold">B</text>
  <rect x="392" y="45" width="45" height="34" rx="6" fill="#fff1d6" stroke="#e0b060"/>
  <text x="414.5" y="65.85" text-anchor="middle" font-size="11" font-weight="bold">C</text>
  <rect x="444" y="45" width="45" height="34" rx="6" fill="#fff1d6" stroke="#e0b060"/>
  <text x="466.5" y="65.85" text-anchor="middle" font-size="11" font-weight="bold">D</text>
  <path d="M455 79 L455 98 L362 98 L362 82" fill="none" stroke="#c0392b" stroke-dasharray="5 4" marker-end="url(#arr-f3-11b)"/>
  <path d="M478 79 L478 112 L302 112 L302 82" fill="none" stroke="#c0392b" stroke-dasharray="5 4" marker-end="url(#arr-f3-11b)"/>
  <text x="380" y="135" text-anchor="middle" font-size="11" fill="#345">B, C and D run concurrently or</text>
  <text x="380" y="150" text-anchor="middle" font-size="11" fill="#345">in planned loops to converge;</text>
  <text x="380" y="165" text-anchor="middle" font-size="11" fill="#345">later phases return to earlier</text>
  <text x="380" y="180" text-anchor="middle" font-size="11" fill="#345">ones to update their outputs</text>
  <text x="380" y="215" text-anchor="middle" font-size="10" fill="#c0392b">Architecture Development iteration</text>
  <rect x="514" y="10" width="236" height="220" rx="8" fill="#fff1d6" stroke="#e0b060"/>
  <text x="632.0" y="28" text-anchor="middle" font-size="12" font-weight="bold">3  Managing the capability</text>
  <rect x="560" y="45" width="145" height="40" rx="6" fill="#fff" stroke="#666"/>
  <text x="632.5" y="62.35" text-anchor="middle" font-size="11" font-weight="bold">Preliminary Phase</text>
  <text x="632.5" y="75.35" text-anchor="middle" font-size="11" fill="#345">(re-)establish the capability</text>
  <rect x="527" y="120" width="100" height="40" rx="6" fill="#fff" stroke="#666"/>
  <text x="577" y="137" text-anchor="middle" font-size="10" font-weight="bold">Phase A</text>
  <text x="577" y="150" text-anchor="middle" font-size="10" fill="#345">capability need found</text>
  <rect x="642" y="120" width="100" height="40" rx="6" fill="#fff" stroke="#666"/>
  <text x="692" y="137" text-anchor="middle" font-size="10" font-weight="bold">Phase H</text>
  <text x="692" y="150" text-anchor="middle" font-size="10" fill="#345">Change Request</text>
  <line x1="577" y1="120" x2="610" y2="87" stroke="#c0392b" stroke-dasharray="5 4" marker-end="url(#arr-f3-11b)"/>
  <line x1="692" y1="120" x2="660" y2="87" stroke="#c0392b" stroke-dasharray="5 4" marker-end="url(#arr-f3-11b)"/>
  <text x="632" y="185" text-anchor="middle" font-size="11" fill="#345">a new pass through Preliminary</text>
  <text x="632" y="200" text-anchor="middle" font-size="11" fill="#345">to adjust the Architecture Capability</text>
  <text x="380" y="250" text-anchor="middle" font-size="11" fill="#666">iteration and levels are tightly linked: the waterfall look of the graphic is only a presentation device</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">The three levels at which the ADM iterates. Original drawing; the three meanings follow APPLY §2.1.</figcaption>
</figure>

The four suggested **iteration cycles** group related activity to a purpose (APPLY §2.2):

| Cycle | Purpose |
|---|---|
| **Architecture Capability** | create and evolve the capability: mobilise for a given engagement by establishing or adjusting approach, principles, scope, vision and governance |
| **Architecture Development** | create content by cycling through or integrating B, C and D so the architecture is considered as a whole; stakeholder reviews are broader; as it converges, extensions into E and F check implementability |
| **Transition Planning** | create formal change roadmaps for a defined architecture |
| **Architecture Governance** | govern change activity progressing towards a defined target |

Architecture Development can be run **Baseline First**, assessing the baseline to find problems
and opportunities, best when the baseline is complex, poorly understood or disputed, common where
units have been autonomous; or **Target First**, elaborating the target then mapping back to the
baseline to find change, best when a target is agreed at a high level. If the baseline is broadly
understood, more value comes from target first with only as much baseline as needed. Teams always
consider both informally, but should prioritise one to keep focus (APPLY §2.4).

Three areas of engagement, split into six engagement classes, show which cycles dominate
(APPLY §2.3):

| Area | Engagement class | Focus cycles |
|---|---|---|
| Identification of required change | Supporting Business Strategy | Capability, Development (Baseline First) |
| | Architectural Portfolio Management of the Landscape | Capability, Development (Baseline First) |
| | Architectural Portfolio Management of Projects | Transition Planning, Governance |
| Definition of change | Definition of Foundational Change Initiatives (objective known, not tightly scoped) | Capability, Development (Baseline First), Transition Planning |
| | Definition of Bounded Change Initiatives (outcome already agreed) | Development (Target First), Transition Planning |
| Implementation of change | Architectural Governance of Change Implementation | Governance |

Some cycles can run once, others have a natural minimum; checkpoints are placed according to
stakeholder involvement, frequent and informal when it is high, rarer and more formal when it is
low (APPLY §2.5). Iteration **between** cycles completes one cycle per level of description, with
Phase F initiating more detailed projects, so higher-level architecture guides and constrains the
detail (APPLY §2.5.1). Iteration **within** a cycle crosses several phases, with activity marked as
core, light or informal per iteration (APPLY §2.5.2). In the Baseline First table, iteration 1
defines the baseline, iteration 2 the target and gaps, and later iterations refine; Target First
reverses the first two. Transition Planning's first iteration wins buy-in to a portfolio of
opportunities and a provisional Migration Plan; Governance's first iteration mobilises governance
and change management, and later ones review and control, possibly feeding a Change Request back
to the Preliminary Phase or to development (APPLY §2.5.2).

The ADM should always be used iteratively; how depends on the formality of checkpoints, the level
of stakeholder involvement, the number of teams and their relationships, the maturity of the
solution area and expected rework, attitude to risk, and the class of engagement (APPLY §2.6).

<!-- figures:start -->
## Figures from the standard

The diagrams the cited sections carry, from your local copy of the publication. The exam reproduces these; know what each box is.

<div class="grid gap-4 md:grid-cols-2">
<figure class="max-w-lg"><img src="/figure/ADM:fig-1-2" alt="Figure 1-2. Architecture Alternatives Method" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 1-2. Architecture Alternatives Method (ADM)</figcaption></figure>
<figure class="max-w-lg"><img src="/figure/ADM:fig-1-3" alt="Figure 1-3. Integration of Architecture Artifacts" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 1-3. Integration of Architecture Artifacts (ADM)</figcaption></figure>
<figure class="max-w-lg"><img src="/figure/APPLY:fig-2-1" alt="Figure 2-1: Iteration Cycles" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 2-1: Iteration Cycles (APPLY)</figcaption></figure>
<figure class="max-w-lg"><img src="/figure/APPLY:fig-2-2" alt="Figure 2-2: Classes of Enterprise Architecture Engagement" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 2-2: Classes of Enterprise Architecture Engagement (APPLY)</figcaption></figure>
<figure class="max-w-lg"><img src="/figure/APPLY:fig-2-3" alt="Figure 2-3: A Hierarchy of ADM Processes Example" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 2-3: A Hierarchy of ADM Processes Example (APPLY)</figcaption></figure>
<figure class="max-w-lg"><img src="/figure/APPLY:fig-2-4" alt="Figure 2-4: Activity by Iteration for Baseline First Architecture Definition" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 2-4: Activity by Iteration for Baseline First Architecture Definition (APPLY)</figcaption></figure>
<figure class="max-w-lg"><img src="/figure/APPLY:fig-2-5" alt="Figure 2-5: Activity by Iteration for Target First Architecture Definition" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 2-5: Activity by Iteration for Target First Architecture Definition (APPLY)</figcaption></figure>
</div>
<!-- figures:end -->

## Check yourself

- Name the four scope dimensions and the order in which scope is usually expressed.
- Which of Target and Transition Architectures should not change during implementation?
- Which iteration cycle would a Bounded Change Initiative focus on, and in which approach?
- What three information areas does a governance repository hold?
