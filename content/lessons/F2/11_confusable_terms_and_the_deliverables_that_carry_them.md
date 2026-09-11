---
title: Confusable terms, and the deliverables that carry them
unit: F2
objectives: ["2.2"]
refs: ["INTRO §4.9", "INTRO §4.16", "INTRO §4.20", "INTRO §4.21", "INTRO §4.22", "INTRO §4.23", "INTRO §4.26", "INTRO §4.40", "INTRO §4.45", "INTRO §4.74", "CONTENT §4.1", "CONTENT §4.2.2", "CONTENT §4.2.3", "CONTENT §4.2.6", "CONTENT §4.2.7", "CONTENT §4.2.8", "CONTENT §4.2.10", "CONTENT §4.2.11", "CONTENT §4.2.13", "CONTENT §4.2.14", "CONTENT §4.2.15", "CONTENT §4.2.16", "CONTENT §4.2.17", "CONTENT §4.2.18", "CONTENT §4.2.20", "CONTENT §4.2.21"]
reading_minutes: 10
source: authored
status: draft
---
Most lost marks in this unit come from pairs of terms that sound alike. For each pair below the
first line gives the distinction; the rest gives the detail the exam draws its distractors from,
mostly from the deliverable descriptions in the Architecture Content document.

## Artifact, deliverable, building block

An **artifact** describes *one aspect* of the architecture (a catalog, matrix or diagram); a
**deliverable** is the *contractually specified, signed-off* work product; a **building block** is
a *potentially reusable component* (INTRO §4.23, INTRO §4.40, INTRO §4.26). Deliverables contain
artifacts; artifacts describe building blocks. The deliverable list itself says that two entries,
Architecture Building Blocks and Solution Building Blocks, are simply "architecture documentation
and models" and "implementation-specific building blocks" drawn from the repository, so building
blocks can appear as deliverables when a phase hands them over (CONTENT §4.1).

## ABB versus SBB

An **ABB** specifies what is needed at a logical, supplier-independent level; an **SBB** is the
physical or implementation-specific component that realises one or more ABBs (INTRO §4.9,
INTRO §4.74). ABBs are output from Phases B, C, D, F and H and input to every phase from A to H;
SBBs are output from Phase G and input to A through G (CONTENT §4.1).

## View versus viewpoint

A **view** is a representation of the system from the perspective of a set of concerns; a
**viewpoint** specifies the conventions for a kind of view, its definition or schema
(INTRO §4.20, INTRO §4.21). The viewpoint is reusable across architectures; the view is specific
to one. Every view has a viewpoint, at least implicitly.

## Architecture Vision versus Architecture Definition Document versus Architecture Requirements Specification

The **Architecture Vision** is a succinct description of the Target Architecture, its business
value and the changes it will bring; it is aspirational and sets a boundary for detailed work
(INTRO §4.22). As a deliverable it is created early, gives key stakeholders a formally agreed
outcome so the architects can focus on validating feasibility, and serves as a summary version of
the full definition. It typically contains the problem description (stakeholders and concerns,
business scenarios, issues), the objective of the Statement of Architecture Work, summary views
such as the Value Chain and Solution Concept diagrams, mapped requirements, and a reference to the
draft Architecture Definition Document (CONTENT §4.2.8). It is an output of Phases A and E
(CONTENT §4.1).

The **Architecture Definition Document** is the deliverable *container* for the core artifacts of
a project. It spans all four domains and all relevant states (Baseline, Transition, Target); its
contents run from scope, goals and principles through the domain models for each state, rationale,
mapping to the repository, gap analysis and impact assessment to the Transition Architectures
(CONTENT §4.2.3). It is output from A through F.

The **Architecture Requirements Specification** is the ADD's companion with a complementary aim:
the ADD gives the *qualitative* view and communicates the architects' intent; the ARS gives the
*quantitative* view, the measurable criteria an implementation must meet, and typically forms a
major part of an implementation contract. Its contents include success measures, requirements,
business and application service contracts, implementation guidelines, specifications and
standards, interoperability requirements, IT service management requirements, constraints and
assumptions (CONTENT §4.2.6).

> **Trap.** Qualitative is the ADD; quantitative is the ARS. "Aspirational summary for the sponsor"
> is the Vision.

## Request for Architecture Work versus Statement of Architecture Work

The **Request** is sent *from the sponsoring organisation to the architecture organisation* to
trigger an architecture development cycle; it can come out of the Preliminary Phase, from an
approved Change Request, or as terms of reference from migration planning. It is high-level:
sponsors, mission, goals, strategic plans, time limits, constraints, budget, current system
descriptions, available resources (CONTENT §4.2.17). It is output from Preliminary, F and H and
input to A and G (CONTENT §4.1).

The **Statement** is the architect's response: it defines the scope and approach for completing a
cycle, is the yardstick for measuring the project, and may form the basis of a contract between
supplier and consumer of architecture services. It carries the project request and background,
description and scope, an overview of the Vision, change-of-scope procedures, roles and
deliverables, acceptance criteria, plan and schedule, and approvals (CONTENT §4.2.20). It is
output from A through H.

<figure class="my-4">
<svg viewBox="0 0 760 232" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="The Request for Architecture Work flows from the sponsoring organisation to the architects; the Statement of Architecture Work flows back">
  <defs><marker id="arr-f2-11a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
  <rect x="10" y="70" width="175" height="70" rx="6" fill="#f4f4f4" stroke="#bbb"/>
  <text x="97.5" y="101.85" text-anchor="middle" font-size="11" font-weight="bold">Sponsoring</text>
  <text x="97.5" y="115.85" text-anchor="middle" font-size="11" fill="#345">organisation</text>
  <rect x="575" y="70" width="175" height="70" rx="6" fill="#f4f4f4" stroke="#bbb"/>
  <text x="662.5" y="101.85" text-anchor="middle" font-size="11" font-weight="bold">Architecture</text>
  <text x="662.5" y="115.85" text-anchor="middle" font-size="11" fill="#345">organisation</text>
  <rect x="225" y="10" width="310" height="70" rx="6" fill="#fff1d6" stroke="#e0b060"/>
  <text x="380" y="29.35" text-anchor="middle" font-size="11" font-weight="bold">Request for Architecture Work</text>
  <text x="380" y="42.35" text-anchor="middle" font-size="11" fill="#345">the trigger: sponsors, mission, goals, budget,</text>
  <text x="380" y="55.35" text-anchor="middle" font-size="11" fill="#345">constraints, time limits, current systems</text>
  <text x="380" y="68.35" text-anchor="middle" font-size="11" fill="#345">output of Preliminary, F, H; input to A and G</text>
  <line x1="185" y1="45" x2="223" y2="45" stroke="#555" marker-end="url(#arr-f2-11a)"/>
  <line x1="535" y1="45" x2="573" y2="45" stroke="#555" marker-end="url(#arr-f2-11a)"/>
  <path d="M97 70 L97 45 L185 45" fill="none" stroke="#555"/>
  <path d="M573 45 L662 45 L662 70" fill="none" stroke="#555"/>
  <rect x="225" y="130" width="310" height="70" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
  <text x="380" y="149.35" text-anchor="middle" font-size="11" font-weight="bold">Statement of Architecture Work</text>
  <text x="380" y="162.35" text-anchor="middle" font-size="11" fill="#345">the response: scope, approach, deliverables,</text>
  <text x="380" y="175.35" text-anchor="middle" font-size="11" fill="#345">acceptance criteria, plan, approvals</text>
  <text x="380" y="188.35" text-anchor="middle" font-size="11" fill="#345">output of A through H; basis of a contract</text>
  <line x1="573" y1="165" x2="537" y2="165" stroke="#555" marker-end="url(#arr-f2-11a)"/>
  <line x1="223" y1="165" x2="187" y2="165" stroke="#555" marker-end="url(#arr-f2-11a)"/>
  <path d="M662 140 L662 165 L573 165" fill="none" stroke="#555"/>
  <path d="M187 165 L97 165 L97 140" fill="none" stroke="#555"/>
  <text x="380" y="222" text-anchor="middle" font-size="11" fill="#666">the Request comes in; the Statement goes back and becomes the yardstick for measuring the project</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">Request in, Statement back. Original drawing; the contents and phases follow CONTENT §4.2.17, CONTENT §4.2.20 and CONTENT §4.1.</figcaption>
</figure>

## Architecture Roadmap versus Implementation and Migration Plan

The **Roadmap** lists the *work packages* that will realise the Target Architecture and lays them
on a timeline from Baseline to Target, highlighting business value at each stage and identifying
Transition Architectures as intermediate steps. It is built incrementally in Phases E and F from
roadmap components identified in B, C and D. Contents: work package portfolio, Implementation
Factor catalog, Consolidated Gaps, Solutions and Dependencies matrix, Transition Architectures,
implementation recommendations (CONTENT §4.2.7).

The **Implementation and Migration Plan** is the *schedule of projects* that realise the target,
grouped into portfolios and programmes; the Implementation and Migration Strategy is a key element
of it. Contents: the strategy (direction, sequencing approach), the project and portfolio
breakdown (work packages allocated to projects, capabilities delivered, milestones, work breakdown
structure), and optionally project charters (CONTENT §4.2.14). It is output from E and F

<figure class="my-4">
<svg viewBox="0 0 760 255" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="The Architecture Roadmap as work packages on a timeline beside the Implementation and Migration Plan as projects grouped into a programme and portfolio">
  <defs><marker id="arr-f2-11b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
  <rect x="10" y="10" width="350" height="235" rx="8" fill="#fff1d6" stroke="#e0b060"/>
  <text x="185.0" y="28" text-anchor="middle" font-size="12" font-weight="bold">Architecture Roadmap: work packages on a timeline</text>
  <text x="60" y="50" text-anchor="middle" font-size="10" fill="#666">Baseline</text>
  <text x="190" y="50" text-anchor="middle" font-size="10" fill="#666">Transition</text>
  <text x="320" y="50" text-anchor="middle" font-size="10" fill="#666">Target</text>
  <line x1="25" y1="58" x2="345" y2="58" stroke="#555" marker-end="url(#arr-f2-11b)"/>
  <rect x="25" y="66" width="58" height="26" rx="6" fill="#fff" stroke="#666"/>
  <text x="54" y="82.85" text-anchor="middle" font-size="11" fill="#345">WP1</text>
  <rect x="88" y="66" width="58" height="26" rx="6" fill="#fff" stroke="#666"/>
  <text x="117" y="82.85" text-anchor="middle" font-size="11" fill="#345">WP2</text>
  <rect x="151" y="66" width="58" height="26" rx="6" fill="#fff" stroke="#666"/>
  <text x="180" y="82.85" text-anchor="middle" font-size="11" fill="#345">WP3</text>
  <rect x="214" y="66" width="58" height="26" rx="6" fill="#fff" stroke="#666"/>
  <text x="243" y="82.85" text-anchor="middle" font-size="11" fill="#345">WP4</text>
  <rect x="277" y="66" width="58" height="26" rx="6" fill="#fff" stroke="#666"/>
  <text x="306" y="82.85" text-anchor="middle" font-size="11" fill="#345">WP5</text>
  <text x="185" y="110" text-anchor="middle" font-size="11" fill="#345">business value shown at each stage</text>
  <text x="185" y="135" text-anchor="middle" font-size="11" fill="#345">contents: work package portfolio,</text>
  <text x="185" y="150" text-anchor="middle" font-size="11" fill="#345">Implementation Factor catalog,</text>
  <text x="185" y="165" text-anchor="middle" font-size="11" fill="#345">Consolidated Gaps, Solutions and</text>
  <text x="185" y="180" text-anchor="middle" font-size="11" fill="#345">Dependencies matrix, Transition</text>
  <text x="185" y="195" text-anchor="middle" font-size="11" fill="#345">Architectures, recommendations</text>
  <text x="185" y="228" text-anchor="middle" font-size="10" fill="#c0392b">built in E and F from B, C, D components</text>
  <rect x="400" y="10" width="350" height="235" rx="8" fill="#e0ecff" stroke="#7aa2e3"/>
  <text x="575.0" y="28" text-anchor="middle" font-size="12" font-weight="bold">Implementation and Migration Plan: the projects</text>
  <rect x="412" y="38" width="326" height="152" rx="8" fill="#f4f4f4" stroke="#bbb" stroke-dasharray="6 4"/>
  <text x="575.0" y="56" text-anchor="middle" font-size="11" font-weight="bold">portfolio</text>
  <rect x="424" y="62" width="302" height="118" rx="8" fill="#fff" stroke="#666" stroke-dasharray="6 4"/>
  <text x="575.0" y="80" text-anchor="middle" font-size="11" font-weight="bold">programme</text>
  <rect x="436" y="90" width="135" height="44" rx="6" fill="#fff" stroke="#666"/>
  <text x="503.5" y="109.35" text-anchor="middle" font-size="11" font-weight="bold">project 1</text>
  <text x="503.5" y="122.35" text-anchor="middle" font-size="11" fill="#345">WP1, WP2  |  milestones</text>
  <rect x="580" y="90" width="135" height="44" rx="6" fill="#fff" stroke="#666"/>
  <text x="647.5" y="109.35" text-anchor="middle" font-size="11" font-weight="bold">project 2</text>
  <text x="647.5" y="122.35" text-anchor="middle" font-size="11" fill="#345">WP3, WP4  |  milestones</text>
  <text x="575" y="160" text-anchor="middle" font-size="10" fill="#345">work breakdown structure, capabilities delivered</text>
  <text x="575" y="208" text-anchor="middle" font-size="11" fill="#345">plus the Implementation and Migration Strategy:</text>
  <text x="575" y="223" text-anchor="middle" font-size="11" fill="#345">direction and sequencing; output of E and F</text>
  <line x1="362" y1="128" x2="398" y2="128" stroke="#555" marker-end="url(#arr-f2-11b)"/>
  <text x="380" y="116" text-anchor="middle" font-size="9" fill="#666">allocated</text>
  <text x="380" y="143" text-anchor="middle" font-size="9" fill="#666">to projects</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">Roadmap on the left, plan on the right. Original drawing; the contents follow CONTENT §4.2.7 and CONTENT §4.2.14.</figcaption>
</figure>

(CONTENT §4.1).

## Enterprise Continuum versus Architecture Repository

The **Continuum** is a categorisation mechanism for classifying architecture and solution building
blocks from generic to specific (INTRO §4.45). The **Repository** is the holding area for all
architecture-related projects, where they manage deliverables, find reusable assets and publish
outputs (CONTENT §4.2.5 describes it as a deliverable output of Preliminary through D and input to
every phase including Requirements Management, CONTENT §4.1). One classifies, the other stores.

## Architecture Level versus Architecture Partition

**Levels** divide the Landscape by granularity (strategic, segment, capability); a **partition** is
a subset of the architecture created to ease development and management. The definition of level
explicitly says the two are distinct (INTRO §4.16).

## Change Request versus Requirements Impact Assessment

A **Change Request** is raised during implementation when the original definition proves
unsuitable or insufficient, or when external factors open opportunities; it may kick-start a
further cycle of architecture work. Its contents are the description and rationale of the change,
an impact assessment and a repository reference (CONTENT §4.2.11). It is output from F, G and H
and input to H (CONTENT §4.1).

A **Requirements Impact Assessment** is produced by Requirements Management when new facts
invalidate existing requirements; it identifies the changes to make and their implications,
including the phases to revisit and which phase leads on re-prioritisation (CONTENT §4.2.18). Its
content list is the same as the impact-assessment part of a Change Request, which is exactly why the
two get confused: the Change Request is raised *by a project*, the Impact Assessment is produced
*by Requirements Management*.

## Compliance Assessment versus Capability Assessment

A **Compliance Assessment** is a Phase G governance product: periodic reviews of implementation
projects against the architecture, containing project progress, an overview of the design, and
completed architecture checklists (hardware, software services, applications, information,
security, system management, system engineering, methods and tools) (CONTENT §4.2.13). It is
output from G and input to H (CONTENT §4.1).

A **Capability Assessment** is done *before* detailed definition to understand baseline and target
capability of the enterprise, the IT function and the architecture function, plus readiness to
transform; it contains a Business Capability Assessment, an IT Capability Assessment, an
architecture maturity assessment and a Business Transformation Readiness Assessment
(CONTENT §4.2.10). It is output from A and E (CONTENT §4.1).

## Architecture Contract versus Statement of Architecture Work versus Implementation Governance Model

The **Architecture Contract** is a joint agreement, between the development partners and the
sponsors, about what will be delivered, to what quality, and whether it is fit for purpose; two forms
are described, the
Architecture Design and Development Contract and the Business Users' Architecture Contract
(CONTENT §4.2.2). It is output from G and input to G and H (CONTENT §4.1). The **Implementation
Governance Model** plans how the Transition Architecture will be governed through implementation:
governance processes, organisation, roles and responsibilities, checkpoints and success/failure
criteria (CONTENT §4.2.15); it is output from F. The Statement of Architecture Work, above, is the
contract-like document for the *architecture* project rather than the *implementation*.

## Organizational Model for Enterprise Architecture versus Tailored Architecture Framework

Both are Preliminary Phase outputs. The **Organizational Model** is about people and boundaries:
scope of organisations impacted, maturity assessment and gaps, roles and responsibilities,
constraints, budget, governance and support strategy (CONTENT §4.2.16). The **Tailored
Architecture Framework** is about the method: tailoring at two levels, first to the enterprise
(integration with management frameworks, terminology, presentation styles, tools) and then to the
specific project (selecting deliverables and artifacts); contents are the tailored method,
tailored content, configured tools, and interfaces with governance models and other frameworks
(CONTENT §4.2.21).

## Check yourself

- Which deliverable gives the quantitative view of the solution?
- Who sends the Request for Architecture Work, and to whom?
- Which document lists work packages on a timeline, and which schedules projects?
- Which is raised by a project and which by Requirements Management: Change Request or Requirements Impact Assessment?
