---
title: The agility guides, architecture levels, sprints and delivery styles
unit: G_DIGITAL_AGILE
objectives: ["G5.1"]
refs: ["GUIDE:enabling-enterprise-agility §4.1", "GUIDE:enabling-enterprise-agility §4.2", "GUIDE:enabling-enterprise-agility §4.3", "GUIDE:enabling-enterprise-agility §4.4.1", "GUIDE:enabling-enterprise-agility §4.4.2", "GUIDE:enabling-enterprise-agility §4.4.3", "GUIDE:enabling-enterprise-agility §4.4.4", "GUIDE:enabling-enterprise-agility §4.5", "GUIDE:enabling-enterprise-agility §4.7.1", "GUIDE:enabling-enterprise-agility §5.1", "GUIDE:enabling-enterprise-agility §5.2.5", "GUIDE:agile-sprints §2", "GUIDE:agile-sprints §3.1", "GUIDE:agile-sprints §3.3", "GUIDE:agile-sprints §3.3.2", "GUIDE:agile-sprints §3.3.4", "GUIDE:agile-sprints §4.3", "GUIDE:agile-sprints §4.4", "GUIDE:agile-sprints §5.3", "GUIDE:agile-sprints §5.4"]
reading_minutes: 11
source: authored
status: draft
---
## When these guides apply

Two Series Guides cover agility. *Enabling Enterprise Agility* explains how the ADM's levels
of detail, iteration and governance make agile delivery possible at enterprise scale; *Applying
the TOGAF ADM using Agile Sprints* shows patterns for doing the architecture work itself in
sprints alongside agile business and solution teams. A scenario that says "our agile teams see
the architecture function as a bottleneck" or "the CIO wants the architecture delivered in
sprints" is pointing at them. The exam expects you to know the three levels, the Minimum
Viable Architecture, how governance changes, the four collaboration patterns, sprint zero and
the phase adaptations, and, most often missed, that not every change should be delivered in
an agile style (GUIDE:enabling-enterprise-agility §4.7.1).

## Levels of detail enable agility

The framework partitions architecture development into three levels: Enterprise Strategic
Architecture, a high-level view of the area of the enterprise affected, broad enough to set
the context; Segment Architectures giving direction at portfolio, programme or product level;
and Capability Architectures, detailed descriptions of increments of business capability,
tightly scoped to sprint time-boxes and detailed enough to hand to developers. The levels
must not be confused with the four domains, which exist at every level; feedback from
implementing capability increments flows bottom-up, and the strategic architecture is not
static (GUIDE:enabling-enterprise-agility §4.1). A Transition Architecture is a formal
description of one state at an architecturally significant point, usually including several
capability increments, related to releases of value and a means of managing risk
(GUIDE:enabling-enterprise-agility §4.2). A hierarchy of ADM cycles lets segment work start as
soon as the strategic architecture identifies the area, and capability work as soon as the
segment identifies it, in parallel; the balance between enough detail for alignment and too
much too soon, Big Design Up Front, is the Minimum Viable Architecture
(GUIDE:enabling-enterprise-agility §4.3).

| Level | Iteration focus | What it produces for agile teams |
|---|---|---|
| Strategic | Phase A, elaborated in B, sometimes high-level C and D; context, guardrails, organisational capabilities | input to define the backlog for segments (GUIDE:enabling-enterprise-agility §4.4.1) |
| Segment | the product or business solution: just enough architecture for features and requirements; KPIs; prototypes and proofs of concept | capability-level backlogs, epics (GUIDE:enabling-enterprise-agility §4.4.2) |
| Capability | just enough detail from the higher levels to define implementation, developed just in time as a forward solution runway; user stories; traceability | the solution specification consumed by delivery sprints, feeding CI/CD (GUIDE:enabling-enterprise-agility §4.4.3) |

Governance in this model is a collaborative, continuous effort across levels and between
architects and delivery teams; the governor is an intelligent advisor embedded in a team
rather than an occasionally visiting policeman, and deferring governance to the final
iteration forfeits agile's benefit through rework (GUIDE:enabling-enterprise-agility §4.4.4).
Mapped to agile concepts, the Strategic level generates strategic themes and the top of the
product portfolio backlog, the Segment level generates epics and a segment backlog, and the
Capability level takes specifications through E and F to SBBs and contracts, is operationally
completed in Phase G and confirms benefits in Phase H, where runway overrun becomes technical
debt to be managed (GUIDE:enabling-enterprise-agility §4.5).

<figure class="my-4">
<svg viewBox="0 0 760 290" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="11" role="img" aria-label="Three architecture levels, strategic, segment, capability, each producing a backlog for the level below, with feedback upward, and the delivery styles Rapid, Agile and Robust chosen by risk and scale">
<defs><marker id="arr-g5a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
<rect x="15" y="15" width="440" height="56" rx="8" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="235" y="36" text-anchor="middle" font-weight="bold">Strategic Architecture: Phase A (and B), context and guardrails</text>
<text x="235" y="54" text-anchor="middle">output: strategic themes, top of the portfolio backlog (§4.4.1, §4.5)</text>
<rect x="15" y="105" width="440" height="56" rx="8" fill="#e3f5e1" stroke="#7fbf7a"/>
<text x="235" y="126" text-anchor="middle" font-weight="bold">Segment Architecture: just enough for the product or solution</text>
<text x="235" y="144" text-anchor="middle">output: epics, segment backlog, KPIs, prototypes (§4.4.2)</text>
<rect x="15" y="195" width="440" height="56" rx="8" fill="#fff1d6" stroke="#e0b060"/>
<text x="235" y="216" text-anchor="middle" font-weight="bold">Capability Architecture: just in time, the solution runway</text>
<text x="235" y="234" text-anchor="middle">output: user stories, sprint backlog, SBBs, contracts; done in G, benefits in H (§4.4.3, §4.5)</text>
<line x1="235" y1="71" x2="235" y2="105" stroke="#555" marker-end="url(#arr-g5a)"/>
<line x1="235" y1="161" x2="235" y2="195" stroke="#555" marker-end="url(#arr-g5a)"/>
<path d="M440 251 L470 251 L470 43 L455 43" fill="none" stroke="#555" stroke-dasharray="5 4" marker-end="url(#arr-g5a)"/>
<text x="478" y="150" text-anchor="start" fill="#666" font-size="10">feedback up</text>
<rect x="540" y="15" width="205" height="236" rx="8" fill="#fff" stroke="#666"/>
<text x="642" y="38" text-anchor="middle" font-weight="bold">Delivery style (§4.7.1)</text>
<text x="642" y="62" text-anchor="middle" font-weight="bold" fill="#3a7d3a">Rapid</text>
<text x="642" y="78" text-anchor="middle">small, simple, tried technology,</text>
<text x="642" y="92" text-anchor="middle">low risk, near immediate</text>
<text x="642" y="120" text-anchor="middle" font-weight="bold" fill="#e0b060">Agile</text>
<text x="642" y="136" text-anchor="middle">small scale, bounded functionality,</text>
<text x="642" y="150" text-anchor="middle">new technology or process tolerated</text>
<text x="642" y="178" text-anchor="middle" font-weight="bold" fill="#c0392b">Robust</text>
<text x="642" y="194" text-anchor="middle">large, complex, long horizon,</text>
<text x="642" y="208" text-anchor="middle">quality or architecture driven,</text>
<text x="642" y="222" text-anchor="middle">high risk; nested with the others</text>
<text x="380" y="278" text-anchor="middle" fill="#666">a sprint is most often a capability increment; transitions are releases of value (GUIDE:enabling-enterprise-agility §4.1, §4.2)</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">The three levels feeding backlogs downward and feedback upward, beside the three delivery styles. Original drawing; section numbers refer to Enabling Enterprise Agility.</figcaption>
</figure>

## Choosing a delivery style

Agile is one of three lifecycle approaches that work with the standard: Rapid, near immediate
implementation of simple components; Agile, fast cycles for bounded functionality; and Robust,
risk and architecture driven, longer-term delivery of complex, large-scale, interoperable
components such as managed PRINCE2 or MSP programmes. They nest: a change of scale will usually
involve all three across its iterations, and high risk or significant consequences call for
the Robust style; the table of project profiles puts large scale, complexity, long horizon,
quality-driven, structure-driven and high-risk work in the Robust column only
(GUIDE:enabling-enterprise-agility §4.7.1). A scenario about a safety-critical control system
delivered "in two-week sprints because we are an agile company" is testing this section.

For the product management side, the Preliminary Phase shifts from project to product focus,
establishes a single product owner as a principle, and expects a more holistic, cross-domain
approach (GUIDE:enabling-enterprise-agility §5.1). Governance is embedded in sprint
retrospectives and planning: guardrails (standard components, limits, policies) and the runway,
impact of change on higher levels, feedback to evolve them, and compliance metrics that can be
expressed as OKRs (GUIDE:enabling-enterprise-agility §5.2.5).

## Sprinting the ADM itself

The sprints guide defines its vocabulary carefully: a sprint is a short time-boxed period; a
backlog is a prioritised, evolving list, with a business change backlog at the top and a sprint
backlog per team; a DORP is the demo, outcome management, retrospective and planning that end
every sprint; a Minimum Viable Architecture is the minimum architecture that is realisable and
adds value, and a Minimum Viable Business Development the minimum business change that delivers
significant value (GUIDE:agile-sprints §2). Sprints suit the standard because iteration is
already deep-rooted in it, monolithic waterfall delivery is an anti-pattern, and short cycles
handle unpredictability and late-arriving information (GUIDE:agile-sprints §3.1).

The four collaboration patterns, often matching the enterprise's agile maturity, are EA
development agility (the architecture itself in sprints, a slice of Phases A to F per sprint),
solution collaboration (architecture and solution sprints together, the EA team producing
just-in-time MVAs), cross-development collaboration (business development, EA and solution
sprints, with MVBDs feeding MVAs feeding solutions) and cross-functional agility (mixed
self-organising teams with all three competencies) (GUIDE:agile-sprints §3.3). At the end of
each sprint the demo shows a testable outcome, the retrospective adjusts the way of working,
and planning selects the next sprint's work from the business change backlog against a sprint
goal; unfinished work returns to the backlog (GUIDE:agile-sprints §3.3.2). The recommended
first sprint, sprint zero or the strategic sprint, is an enough-design-upfront preparation
sprint that builds the business change backlog from business needs, value streams,
capabilities and a high-level roadmap, identifies no-regret decisions, and picks a
prioritisation strategy: most value first, riskiest first, a slice through all phases, or
easiest first; only the next sprint is planned in detail (GUIDE:agile-sprints §3.3.4).

Phases E and F are adapted so that not every step runs every sprint but each step is scaled to
the sprint: constraints, interoperability, dependencies, readiness, strategy and work packages
per sprint, the roadmap becoming the backlog defined with the product owner, and the plan
becoming the next sprint's backlog (GUIDE:agile-sprints §4.3). In Phase G compliance becomes
ongoing rather than a gate, and an increment can deploy after each approved demo
(GUIDE:agile-sprints §4.4). Sprints are typically two weeks and should be fixed in length; if
one sprint is not enough to create value, let the work span sprints or define a set of
Transition Architectures as releases, a pattern close to an Agile Release Train
(GUIDE:agile-sprints §5.3). Governance moves into the sprint process, becoming a way of
collaborating and delegating with accountability for outcomes; the guide offers the seven
delegation levels and the rule that reversible decisions go to teams and irreversible ones to
the wider group (GUIDE:agile-sprints §5.4).

**Trap.** Sprint zero is not universally accepted by agile practitioners, and the guide says
so; the five-point answer recommends it for EA work while acknowledging that
(GUIDE:agile-sprints §3.3.4).

## How the 5, 3 and 1 differ

| Answer | Why it scores that |
|---|---|
| 5 | Partitions into Strategic, Segment and Capability Architectures, produces just-in-time MVAs for the teams, runs a sprint zero to build the business change backlog, embeds governance and compliance in each sprint's DORP, and chooses Robust delivery for the high-risk component |
| 3 | Adopts sprints for the architecture work but keeps the compliance gate at the end, or delivers the whole architecture before any solution sprint when solution collaboration was called for |
| 1 | Applies the same two-week sprint cadence to every part of the change, including the safety-critical one; the guide reserves Robust delivery for high-risk, large-scale change (GUIDE:enabling-enterprise-agility §4.7.1) |
| 0 | Concludes that agile teams do not need architecture, or that the ADM cannot be used with sprints; iteration is inherent in the ADM (GUIDE:agile-sprints §3.1) |

## Where to look in the book

Enabling Enterprise Agility: §4.1 to §4.5 for levels, transitions, hierarchy, iterations and
governance; §4.7.1 for delivery styles; §5.1, §5.2.5 for product management and governance.
Applying the ADM using Agile Sprints: §2 definitions, §3.3 patterns, §3.3.2 DORP, §3.3.4 sprint
zero, §4.3 and §4.4 phase adaptations, §5.3 sprint length, §5.4 governance.

## Check yourself

- Which level produces the solution runway, and how far ahead is it developed?
- Name the four collaboration patterns in order of maturity.
- Which profile characteristics appear only in the Robust column?
