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

## Check yourself

- Which phase precedes the cycle proper, and what does it set up?
- Does Requirements Management prioritise requirements? Who does?
- Which requirements artefact can span multiple ADM cycles?
- What is a "gap requirement"?
