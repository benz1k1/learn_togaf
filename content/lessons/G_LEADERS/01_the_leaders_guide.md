---
title: The Leader's Guide — establishing and evolving an EA Capability, and when it applies
unit: G_LEADERS
objectives: ["G1.1"]
refs: ["GUIDE:togaf-leaders-guide §1.1", "GUIDE:togaf-leaders-guide §3.3", "GUIDE:togaf-leaders-guide §3.4", "GUIDE:togaf-leaders-guide §4", "GUIDE:togaf-leaders-guide §5", "GUIDE:togaf-leaders-guide §5.2", "GUIDE:togaf-leaders-guide §5.4", "GUIDE:togaf-leaders-guide §6.2", "GUIDE:togaf-leaders-guide §9.2", "GUIDE:togaf-leaders-guide §11.1", "GUIDE:togaf-leaders-guide §12.5", "GUIDE:togaf-leaders-guide §13.1", "GOV §2.1"]
reading_minutes: 10
source: authored
status: draft
---
## What the guide is and who it is for

The Leader's Guide is written for the *EA Capability Leader* — the person tasked to establish or
evolve an Enterprise Architecture Capability, whatever their title — and proposes a configured
path through the ADM for standing up or enhancing that capability. It moves between setting up a
new practice and re-booting an existing one, because at the time of writing the most common
industry practice "is a re-boot after a failed attempt" (GUIDE:togaf-leaders-guide §1.1;
GUIDE:togaf-leaders-guide §3.4). In TOGAF terms, establishing an EA Capability is the purpose of
the Preliminary Phase, and the guide is in-depth commentary on executing that phase: customising
the ADM, defining a content framework, selecting tools and practices (GUIDE:togaf-leaders-guide §1.1).

**When it applies in a scenario.** Whenever the question is about the capability rather than an
architecture: a new CIO asks what an EA function should do; a team that "produces standards
nobody reads" is being re-chartered; two EA teams in a merged group must be aligned; a board
wants to know how the value of EA will be measured. If the scenario is about a *specific*
change initiative, the Practitioners' Approach applies instead (GUIDE:togaf-leaders-guide §5).

## The core idea: context and purpose first

An EA Capability is "the ability to develop, use, and sustain the architecture of a particular
enterprise, and use the architecture to govern change", and it is established for one or more
of four purposes — support strategy, portfolio, project, or solution delivery
(GUIDE:togaf-leaders-guide §3.3). The guide insists that context and objectives be made
explicit with the sponsor; implicit assumptions "invariably lead to failures", and purpose
directly shapes the organisation model, the governance framework, the architecture contents and
the process model (GUIDE:togaf-leaders-guide §5).

The context questions: what is the enterprise (its boundary, deliberately flexible — an extended
enterprise, a mission-joined set of organisations, or part of one); what is its purpose; what
is its strategic position, approach and environment; what is the special context for the EA
Capability; and what principles will drive choices. Existing material is confirmed, not
rewritten, and it is "too early in the process to start creating principles"
(GUIDE:togaf-leaders-guide §4).

<figure class="my-4">
<svg viewBox="0 0 760 330" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="10" role="img" aria-label="The Leader's Guide chapters mapped onto ADM phases: context to partial strategic Phase B, business objectives to capability-level Phase A, governance and organisation model to partial Phase B, content and metamodel to Phase C data, process model to Phases B, C application and D, the capability roadmap to Phase E, and establishing and evolving to Phases F and G">
<defs><marker id="arr-g1-01a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
<text x="380" y="18" text-anchor="middle" font-size="12" font-weight="bold">The Leader's journey as a configured path through the ADM</text>
<g>
<rect x="10" y="40" width="130" height="58" rx="6" fill="#e3f0fb" stroke="#4a7fb5"/><text x="75" y="60" text-anchor="middle" font-weight="bold">Ch 4 Context</text><text x="75" y="75" text-anchor="middle" font-size="9">enterprise and EA context</text><text x="75" y="88" text-anchor="middle" font-size="9">→ partial strategic B</text>
<rect x="150" y="40" width="130" height="58" rx="6" fill="#e3f0fb" stroke="#4a7fb5"/><text x="215" y="60" text-anchor="middle" font-weight="bold">Ch 5 Objectives</text><text x="215" y="75" text-anchor="middle" font-size="9">purpose, measures, model</text><text x="215" y="88" text-anchor="middle" font-size="9">→ capability-level A</text>
<rect x="290" y="40" width="130" height="58" rx="6" fill="#e3f0fb" stroke="#4a7fb5"/><text x="355" y="60" text-anchor="middle" font-weight="bold">Ch 6 Governance</text><text x="355" y="75" text-anchor="middle" font-size="9">decision rights, tiers, ERM</text><text x="355" y="88" text-anchor="middle" font-size="9">→ partial B</text>
<rect x="430" y="40" width="130" height="58" rx="6" fill="#e3f0fb" stroke="#4a7fb5"/><text x="495" y="60" text-anchor="middle" font-weight="bold">Ch 7 Frameworks</text><text x="495" y="75" text-anchor="middle" font-size="9">catalog and touch-points</text><text x="495" y="88" text-anchor="middle" font-size="9">→ partial B and C data</text>
<rect x="570" y="40" width="180" height="58" rx="6" fill="#e3f0fb" stroke="#4a7fb5"/><text x="660" y="60" text-anchor="middle" font-weight="bold">Ch 8 Contents and metamodel</text><text x="660" y="75" text-anchor="middle" font-size="9">content framework, repository</text><text x="660" y="88" text-anchor="middle" font-size="9">→ capability-level C data</text>
</g>
<line x1="380" y1="98" x2="380" y2="120" stroke="#555" marker-end="url(#arr-g1-01a)"/>
<g>
<rect x="10" y="122" width="240" height="58" rx="6" fill="#fff1d6" stroke="#e0b060"/><text x="130" y="142" text-anchor="middle" font-weight="bold">Ch 9 Organisation model for the team</text><text x="130" y="157" text-anchor="middle" font-size="9">alignment (function-, IT-, strategy-centric), roles, capacity</text><text x="130" y="170" text-anchor="middle" font-size="9">→ partial capability-level B</text>
<rect x="260" y="122" width="240" height="58" rx="6" fill="#fff1d6" stroke="#e0b060"/><text x="380" y="142" text-anchor="middle" font-weight="bold">Ch 10 Process model</text><text x="380" y="157" text-anchor="middle" font-size="9">touch-points with enterprise processes; iteration</text><text x="380" y="170" text-anchor="middle" font-size="9">→ partial B, C application, D</text>
<rect x="510" y="122" width="240" height="58" rx="6" fill="#fff1d6" stroke="#e0b060"/><text x="630" y="142" text-anchor="middle" font-weight="bold">Ch 11 EA Capability roadmap</text><text x="630" y="157" text-anchor="middle" font-size="9">multi-year plan, value map, capability model</text><text x="630" y="170" text-anchor="middle" font-size="9">→ capability-level E</text>
</g>
<line x1="380" y1="180" x2="380" y2="202" stroke="#555" marker-end="url(#arr-g1-01a)"/>
<rect x="10" y="204" width="740" height="52" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/>
<text x="380" y="224" text-anchor="middle" font-weight="bold">Ch 12 Establishing and evolving the EA Capability → capability-level F and G</text>
<text x="380" y="242" text-anchor="middle" font-size="9">transition the roadmap to an Implementation and Migration Plan and execute it; sustain and mature; trusted advisor; community and mentoring</text>
<rect x="10" y="266" width="740" height="56" rx="6" fill="#fff" stroke="#666"/>
<text x="380" y="286" text-anchor="middle" font-weight="bold">Whole journey = the Preliminary Phase, done as a customised path through the ADM</text>
<text x="380" y="304" text-anchor="middle" font-size="9">"partial" means only as much of a phase as answers the question at hand — the concept of iteration in practice</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">Original drawing. The chapter-to-phase mapping is the guide's own Table 13-1 (GUIDE:togaf-leaders-guide §13.1); the framing as the Preliminary Phase follows §1.1 and §13.1.</figcaption>
</figure>

## What each part decides

**Objectives and measures.** The questions to answer: what is expected and why; how the EA will
be used (strategy, programme, segment, capability, project, third party); how success is
measured; whether it is right for the context; depth and breadth; organisation model
(GUIDE:togaf-leaders-guide §5). Depth and breadth follow from the four purposes
(GUIDE:togaf-leaders-guide §5.2). Measures derive from purpose; the guide's death traps are
adopting unvalidated common-sense objectives and confusing supporting decisions with making
them; it also lists the problems a capability is often set up to solve — M&A, stalled growth,
disruption, restructuring, complexity that prevents decisions — each with its own measures
(GUIDE:togaf-leaders-guide §5.4).

**Governance.** Decision rights over the target, relief and enforcement belong to the
stakeholders; an EA board owns the process and a recommendation on completeness and
confidence. The guide gives a nine-question decision tree for assessing a target (correct
stakeholders? superior architecture respected? SMEs agree? views reflect concerns? stakeholders
understand value, work and limits of confidence? approved?) and a parallel checklist for
non-compliance, where the choices are enforce, grant time-bound relief, or change the target —
and relief must be re-assessed or the enterprise has quietly changed its architecture
(GUIDE:togaf-leaders-guide §6.2).

**Organisation model.** Teams fall into function-centric, IT-centric and strategy-centric
alignments, each with a different charter; the EA Capability must integrate with strategy and
planning, portfolio management, solutions delivery, finance, security and operations; and
where there are multiple EA teams "there is one EA Capability and there should be one Leader"
(GUIDE:togaf-leaders-guide §9.2).

**Roadmap and evolution.** Create a multi-year plan for three efforts — capability management,
project engagement, and maturity and quality — treat capability implementation like any other
project, and keep the rationale for the chosen path; a common mistake is doing without a project
manager (GUIDE:togaf-leaders-guide §11.1). Sustaining and maturing means periodically validating
capacity and charter with the sponsors and nurturing the three styles of thinking the guide
calls star gazers, anthropologists and planners (GUIDE:togaf-leaders-guide §12.5).

**Trap.** The guide does not describe an "EA department". It explicitly discusses a capability,
not an organisational element, and warns that no single correct EA Capability model exists
(GUIDE:togaf-leaders-guide §3.3). And it is companion to, not a replacement for, the standard's
own guidance on establishing a capability with the ADM, which treats the practice as an ongoing
discipline rather than a project (GOV §2.1).

## How the 5-point answer differs from the 3-point one

| Points | What the answer does |
|---|---|
| 5 | Treats the request as Preliminary-Phase work: confirms enterprise and EA context, extracts purpose and success measures from the sponsor, sizes depth and breadth to the purpose, designs governance with stakeholder decision rights, aligns the team model and touch-points, and builds a multi-year roadmap under one Leader |
| 3 | Sets purpose and governance but reads objectives off documents rather than validating them with the sponsor, or builds the roadmap without a project manager and rationale |
| 1 | Starts by hiring a team and choosing a tool, then works out what they are for |
| 0 | Gives the architecture board decision rights over the target, or measures success by the number of models produced |

## Where to look in the book

Leader's Guide §1.1 (what it is: the Preliminary Phase in depth), §3.3 (EA Capability and the
four purposes), §3.4 (lifecycle and re-boots), §4 (context questions), §5 (objective questions),
§5.2 (depth and breadth), §5.4 (measures and death traps), §6.2 (essential governance and the
two checklists), §9.2 (team alignment), §11.1 (roadmap), §12.5 (sustaining), §13.1 (the
chapter-to-ADM mapping). EA Capability and Governance §2.1.
