---
title: The ADM cycle, its phases, and Requirements Management at the centre
unit: F3
objectives: ["3.1"]
refs: ["INTRO §3.4", "ADM §1.1", "ADM §1.2.1", "ADM §1.2.2", "ADM §13", "ADM §13.1", "ADM §13.2", "ADM §13.3", "ADM §13.4", "ADM §13.5.1", "ADM §13.5.2", "ADM §13.5.3"]
reading_minutes: 9
source: authored
status: draft
---
## What the ADM is

The Architecture Development Method is the core of the standard: a method for developing an
enterprise architecture and managing it over its lifecycle, integrating the other parts of the standard
and any available architecture assets to meet the business need (ADM §1.1). The Introduction
describes it as a tested, repeatable process covering four things: establishing an architecture
framework, developing architecture content, transitioning, and governing the realisation of
architectures, all inside an iterative cycle of continuous definition and realisation that lets an
enterprise transform in a controlled way (INTRO §3.4).

<figure class="my-4">
<svg viewBox="0 0 760 135" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="The four things the ADM covers, establish, develop, transition, govern, drawn as a repeating loop">
  <defs><marker id="arr-f3-10a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
  <rect x="15" y="20" width="170" height="50" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
  <text x="100" y="41.85" text-anchor="middle" font-size="11" fill="#345">establish an</text>
  <text x="100" y="55.85" text-anchor="middle" font-size="11" fill="#345">architecture framework</text>
  <line x1="185" y1="45" x2="198" y2="45" stroke="#555" marker-end="url(#arr-f3-10a)"/>
  <rect x="200" y="20" width="170" height="50" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
  <text x="285" y="41.85" text-anchor="middle" font-size="11" fill="#345">develop</text>
  <text x="285" y="55.85" text-anchor="middle" font-size="11" fill="#345">architecture content</text>
  <line x1="370" y1="45" x2="383" y2="45" stroke="#555" marker-end="url(#arr-f3-10a)"/>
  <rect x="385" y="20" width="170" height="50" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
  <text x="470" y="41.85" text-anchor="middle" font-size="11" fill="#345">transition</text>
  <text x="470" y="55.85" text-anchor="middle" font-size="11" fill="#345">to the new state</text>
  <line x1="555" y1="45" x2="568" y2="45" stroke="#555" marker-end="url(#arr-f3-10a)"/>
  <rect x="570" y="20" width="170" height="50" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
  <text x="655" y="41.85" text-anchor="middle" font-size="11" fill="#345">govern the</text>
  <text x="655" y="55.85" text-anchor="middle" font-size="11" fill="#345">realisation</text>
  <path d="M655 70 L655 105 L100 105 L100 72" fill="none" stroke="#c0392b" stroke-dasharray="5 4" marker-end="url(#arr-f3-10a)"/>
  <text x="380" y="120" text-anchor="middle" font-size="11" fill="#c0392b">an iterative cycle of continuous definition and realisation: the enterprise transforms in a controlled way</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">What one pass of the method covers, and why it loops. Original drawing; the four items follow INTRO §3.4.</figcaption>
</figure>

## The phases

| Phase | In one line (INTRO §3.4) |
|---|---|
| **Preliminary** | preparation and initiation to create an Architecture Capability, including customising the framework and defining Architecture Principles |
| **A. Architecture Vision** | the first phase of a cycle: scope, stakeholders, the Architecture Vision, approval to proceed |
| **B. Business Architecture** | develop the Business Architecture to support the agreed Vision |
| **C. Information Systems Architectures** | develop the Data and Application Architectures to support the Vision |
| **D. Technology Architecture** | develop the Technology Architecture to support the Vision |
| **E. Opportunities & Solutions** | initial implementation planning; identify delivery vehicles for the architecture defined so far |
| **F. Migration Planning** | how to move from Baseline to Target, finalising a detailed Implementation and Migration Plan |
| **G. Implementation Governance** | architectural oversight of the implementation |
| **H. Architecture Change Management** | procedures for managing change to the new architecture |
| **Requirements Management** | the process of managing architecture requirements throughout the ADM |

The phase descriptions in the ADM document are recommendations on *what* may be done; *how* is the
job of the Series Guides (INTRO §3.4).

> **Trap.** The ADM does *not* mandate that phases run in a fixed sequence, and it is not a
> waterfall. The graphic is better read as a reference model of what has to be done to deliver
> solutions in an architected way than as a process model (INTRO §3.4).

## Key points about the cycle

The standard lists the things every reader must know about the ADM (ADM §1.2.1):

- It is **iterative** over the whole process, between phases and within phases.
- For each iteration a **fresh decision** is taken on the breadth of the enterprise to cover, the
  level of detail, the time period including any intermediate periods, and the architecture
  assets to reuse, both those from earlier iterations and those from the wider industry.
- Those decisions rest on a practical assessment of available resources and competence, and on
  the value the enterprise can realistically expect from the chosen scope.
- It is a **generic** method for any geography or sector; it may be tailored but does not have to
  be, and it can be used with another framework's deliverables where those fit better.

Structurally, each phase is divided into steps defined in that phase's chapter. Results must be
validated frequently against the original expectations, both for the whole cycle and for the
current phase (ADM §1.2.2).

## Outputs, versions and status

Output is generated throughout, and output from an early phase may be modified in a later one, so
the lifecycle of outputs is managed by a version numbering policy the architect adapts to the
organisation and its tools (ADM §1.2.2). Two status labels are defined: a document that has not
been through formal review and approval is **draft**; once reviewed and approved it is
**approved**, though approved does not mean final. Approved documents can still evolve, but only
through change control and governance. The standard uses this to show how Baseline and Target
Architecture Definitions evolve (ADM §1.2.2).

## Requirements Management: the phase at the centre

Requirements Management is a **continuous** phase. It ensures changes to requirements pass through
appropriate governance and are reflected in all other phases; an enterprise may record all new
requirements, including those in scope of the current Statement of Architecture Work, in a single
Requirements Repository (ADM §1.2.2).

Its objectives are to keep the requirements management process running for all relevant phases, to
manage the architecture requirements identified during any cycle or phase, and to make the relevant
requirements available to each phase as it runs (ADM §13.1).

Two facts about it are tested constantly (ADM §13.5.1):

1. The circle in the middle of the graphic is not a static list of requirements; it is a **dynamic
   process** by which requirements and changes to them are identified, stored and fed into and out
   of the phases, and between cycles.
2. The Requirements Management process itself **does not dispose of, address or prioritise** any
   requirement. That is done inside the relevant ADM phase. Requirements Management is only the
   process for managing them across the whole ADM.

Requirements change constantly because architecture works in the uncertain space between
stakeholder aspiration and what can actually be engineered, and because drivers and constraints such as
markets and legislation are outside the enterprise's control (ADM §13.5.1). An **Architecture
Requirements Repository** is recommended for recording and managing all requirements; unlike the
Architecture Requirements Specification and the Requirements Impact Assessment, it can hold
information from *multiple* ADM cycles (ADM §13.5.1).

### Inputs, steps and outputs

Inputs are a populated Architecture Repository, the Organizational Model for EA, the Tailored
Architecture Framework, the Statement of Architecture Work, the Architecture Vision, architecture
requirements populating an Architecture Requirements Specification, and any Requirements Impact
Assessment (ADM §13.2).

The steps are laid out as a two-column table: some are performed by the Requirements Management
process, others by the ADM phase currently running (ADM §13.3).

| Requirements Management does | The current ADM phase does |
|---|---|
| establish baseline requirements: priorities, stakeholder agreement, document in the ARS and repository | identify requirements (via value streams, business scenarios, user experiences, management information) and document them |
| monitor baseline requirements | identify new and changed requirements: remove, add, modify and re-prioritise |
| identify changed requirements and record priorities; manage conflicts; generate a Requirements Impact Assessment; check stakeholder satisfaction | assess the impact on the current and previous phases; decide whether to implement now or defer to a later cycle; issue Requirements Impact Assessment version n+1 |
| update the Architecture Requirements Repository, including affected stakeholder views | implement requirements arising from Phase H |
| | implement the change in the current phase |
| | assess and revise gap analysis for past phases |

<figure class="my-4">
<svg viewBox="0 0 760 325" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="Two swimlanes: the steps Requirements Management performs and the steps the current ADM phase performs, alternating">
  <defs><marker id="arr-f3-10b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
  <rect x="10" y="10" width="360" height="285" rx="8" fill="#e0ecff" stroke="#7aa2e3"/>
  <rect x="390" y="10" width="360" height="285" rx="8" fill="#e3f5e1" stroke="#7fbf7a"/>
  <text x="190" y="30" text-anchor="middle" font-size="12" font-weight="bold">Requirements Management does</text>
  <text x="570" y="30" text-anchor="middle" font-size="12" font-weight="bold">The current ADM phase does</text>
  <rect x="25" y="45" width="330" height="52" rx="6" fill="#fff" stroke="#666"/>
  <text x="190" y="68.35" text-anchor="middle" font-size="11" font-weight="bold">1 establish baseline requirements</text>
  <text x="190" y="81.35" text-anchor="middle" font-size="11" fill="#345">priorities, agreement; into the ARS and repository</text>
  <rect x="405" y="45" width="330" height="52" rx="6" fill="#fff" stroke="#666"/>
  <text x="570" y="61.85" text-anchor="middle" font-size="11" font-weight="bold">2 identify requirements</text>
  <text x="570" y="74.85" text-anchor="middle" font-size="11" fill="#345">value streams, business scenarios, user</text>
  <text x="570" y="87.85" text-anchor="middle" font-size="11" fill="#345">experiences, management information</text>
  <rect x="25" y="108" width="330" height="52" rx="6" fill="#fff" stroke="#666"/>
  <text x="190" y="137.85" text-anchor="middle" font-size="11" font-weight="bold">3 monitor baseline requirements</text>
  <rect x="405" y="108" width="330" height="52" rx="6" fill="#fff" stroke="#666"/>
  <text x="570" y="131.35" text-anchor="middle" font-size="11" font-weight="bold">4 identify new and changed requirements</text>
  <text x="570" y="144.35" text-anchor="middle" font-size="11" fill="#345">remove, add, modify, re-prioritise</text>
  <rect x="25" y="171" width="330" height="52" rx="6" fill="#fff" stroke="#666"/>
  <text x="190" y="187.85" text-anchor="middle" font-size="11" font-weight="bold">5 record changed requirements and priorities</text>
  <text x="190" y="200.85" text-anchor="middle" font-size="11" fill="#345">manage conflicts; issue a Requirements Impact</text>
  <text x="190" y="213.85" text-anchor="middle" font-size="11" fill="#345">Assessment; check stakeholder satisfaction</text>
  <rect x="405" y="171" width="330" height="52" rx="6" fill="#fff" stroke="#666"/>
  <text x="570" y="194.35" text-anchor="middle" font-size="11" font-weight="bold">6 assess impact; implement now or defer</text>
  <text x="570" y="207.35" text-anchor="middle" font-size="11" fill="#345">to a later cycle; issue Impact Assessment n+1</text>
  <rect x="25" y="234" width="330" height="52" rx="6" fill="#fff" stroke="#666"/>
  <text x="190" y="257.35" text-anchor="middle" font-size="11" font-weight="bold">7 update the Architecture Requirements</text>
  <text x="190" y="270.35" text-anchor="middle" font-size="11" fill="#345">Repository, including affected views</text>
  <rect x="405" y="234" width="330" height="52" rx="6" fill="#fff" stroke="#666"/>
  <text x="570" y="250.85" text-anchor="middle" font-size="11" font-weight="bold">8 implement the change in this phase</text>
  <text x="570" y="263.85" text-anchor="middle" font-size="11" fill="#345">revise gap analysis for past phases;</text>
  <text x="570" y="276.85" text-anchor="middle" font-size="11" fill="#345">act on requirements from Phase H</text>
  <line x1="355" y1="65" x2="403" y2="65" stroke="#555" marker-end="url(#arr-f3-10b)"/>
  <line x1="380" y1="73" x2="380" y2="106" stroke="#555" marker-end="url(#arr-f3-10b)"/>
  <line x1="355" y1="128" x2="403" y2="128" stroke="#555" marker-end="url(#arr-f3-10b)"/>
  <line x1="380" y1="136" x2="380" y2="169" stroke="#555" marker-end="url(#arr-f3-10b)"/>
  <line x1="355" y1="191" x2="403" y2="191" stroke="#555" marker-end="url(#arr-f3-10b)"/>
  <line x1="380" y1="199" x2="380" y2="232" stroke="#555" marker-end="url(#arr-f3-10b)"/>
  <line x1="355" y1="254" x2="403" y2="254" stroke="#555" marker-end="url(#arr-f3-10b)"/>
  <text x="380" y="312" text-anchor="middle" font-size="11" fill="#666">Requirements Management manages the flow; the phase disposes, addresses and prioritises. Neither side owns the other's step.</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">The two-column step table drawn as swimlanes. Original drawing; the steps follow ADM §13.3 and the division of labour ADM §13.5.1.</figcaption>
</figure>

The last step is where the standard defines two kinds of gap: something present in the baseline
but not the target (eliminated, by accident or design) and something in the target but not the
baseline (new). A **gap requirement** is anything eliminated by accident, which therefore requires
a change to the Target Architecture (ADM §13.3).

Outputs may include a Requirements Impact Assessment and an updated Architecture Requirements
Specification; the Architecture Requirements Repository is updated as part of the phase
(ADM §13.4). When requirements arise or change, the Impact Assessment identifies which phases must
be revisited and iterates until a final version carries the full implications, such as cost,
timescale and business metrics (ADM §13.4).

### How requirements develop

The first high-level requirements come out of the Architecture Vision, produced with the business
scenario technique or an equivalent (ADM §13.5.2). Every phase from Preliminary to H selects the
approved requirements for that phase from the repository and the ARS, and updates their status on
completion. New requirements inside the scope of the current Statement of Architecture Work go
into the ARS; those outside it go into the Architecture Requirements Repository for management
(ADM §13.5.2). Both functional and non-functional requirements are identified, taking account of
assumptions, constraints, domain principles, policies, standards, organisational guidelines and
specifications (ADM §13.5.2).

The standard mandates no specific requirements process or tool; it states what a good process
should achieve, the "requirements for requirements". Business scenarios are the named technique for
analysing how a goal is met through a process or value stream, and there are many COTS
requirements tools (ADM §13.5.3).

<!-- figures:start -->
## Figures from the standard

The diagrams the cited sections carry, from your local copy of the publication. The exam reproduces these; know what each box is.

<div class="grid gap-4 md:grid-cols-2">
<figure class="max-w-lg"><img src="/figure/ADM:fig-1-1" alt="Figure 1-1. Architecture Development Cycle" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 1-1. Architecture Development Cycle (ADM)</figcaption></figure>
<figure class="max-w-lg"><img src="/figure/ADM:fig-13-1" alt="Figure 13-1: ADM Architecture Requirements" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 13-1: ADM Architecture Requirements (ADM)</figcaption></figure>
<figure class="max-w-lg"><img src="/figure/INTRO:fig-3-1" alt="Figure 3-1: Architecture Development Cycle" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 3-1: Architecture Development Cycle (INTRO)</figcaption></figure>
</div>
<!-- figures:end -->

## Check yourself

- Which phase precedes the cycle proper, and what does it set up?
- Does Requirements Management prioritise requirements? Who does?
- Which requirements artefact can span multiple ADM cycles?
- What is a "gap requirement"?
