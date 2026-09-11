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

## Check yourself

- Name the four scope dimensions and the order in which scope is usually expressed.
- Which of Target and Transition Architectures should not change during implementation?
- Which iteration cycle would a Bounded Change Initiative focus on, and in which approach?
- What three information areas does a governance repository hold?
