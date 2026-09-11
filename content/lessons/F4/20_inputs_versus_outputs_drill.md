---
title: Inputs versus outputs across the ADM cycle
unit: F4
objectives: ["4.3"]
refs: ["ADM §2.2", "ADM §2.4", "ADM §3.2", "ADM §3.4", "ADM §4.2", "ADM §4.4", "ADM §6.2", "ADM §6.4", "ADM §7.2", "ADM §7.4", "ADM §8.2", "ADM §8.4", "ADM §9.2", "ADM §9.4", "ADM §10.2", "ADM §10.4", "ADM §11.2", "ADM §11.4", "ADM §12.2", "ADM §12.4", "ADM §13.2", "ADM §13.4"]
reading_minutes: 12
source: authored
status: draft
---
## How the standard structures every phase

Every phase chapter from 2 to 12 lists inputs in three groups — *reference materials external
to the enterprise*, *non-architectural inputs* and *architectural inputs* — and then lists
outputs that "may include, but are not restricted to" a set of deliverables (for example
ADM §3.2 and ADM §3.4). Requirements Management uses a single flat list (ADM §13.2). Nine of
forty exam marks sit in this unit, and the questions that cost the most marks ask **which phase
first produces a deliverable** and **which phases consume it**. The tables below are built
from the inputs and outputs sections only.

## The three constants

Three things come from the Preliminary Phase and are inputs to *every* later phase, including
Requirements Management:

| Deliverable | Produced | Consumed | Refined |
|---|---|---|---|
| Organizational Model for Enterprise Architecture | Preliminary (ADM §2.4) | A–H, Requirements Management | — |
| Tailored Architecture Framework | Preliminary (ADM §2.4) | A–H, Requirements Management | A produces one "for the engagement" (ADM §3.4) |
| Architecture Repository | Preliminary, initial (ADM §2.4) | A–H (populated), Requirements Management | A adds content; G populates it with solutions (ADM §11.4) |

## The Phase A set

| Deliverable | First produced | Consumed as input | Updated by |
|---|---|---|---|
| **Request for Architecture Work** | Preliminary, *optional* (ADM §2.4); new ones in F for a new iteration (ADM §10.4) and in H for another cycle (ADM §12.4) | A (its trigger, ADM §3.2), and every phase B–H lists it too | — |
| **Statement of Architecture Work** | A, approved (ADM §3.4) | B–H, Requirements Management | B, C, D, E, H update it "if necessary" |
| **Architecture Vision** | A (ADM §3.4) | B–H, Requirements Management | E adds types and degrees of interoperability (ADM §9.4); G updates it post-implementation (ADM §11.4) |
| **Capability Assessment** | A, including readiness results (ADM §3.4) | B, C, D, E, F, G | E produces Business and IT Capability Assessments (ADM §9.4) |
| **Communications Plan** | A (ADM §3.4) | B, C, D, E, F — **not G, not H** | — |
| Architecture Principles | Preliminary establishes them inside the Tailored Framework (ADM §2.4); A outputs them confirmed (ADM §3.4) | B (with business principles); data, application and technology principles into C and D "if existing" | B, C, D validate or generate domain principles |
| Business principles, goals and drivers | Preliminary restates them (ADM §2.4) | A, B | A refines, B validates |

## The development set (B, C, D)

| Deliverable | First produced | Consumed as input | Finalized |
|---|---|---|---|
| **Architecture Definition Document** (draft) | A may start it (ADM §3.4); B produces the first domain content (ADM §4.4) | B–F as draft; G, H as the finished document | **F** (ADM §10.4); G updates post-implementation |
| **Architecture Requirements Specification** (draft) | **B** (ADM §4.4) — it is *not* a B input | C (Data), C (Application), D, E, F as draft; G, H finished | **F** (ADM §10.4) |
| **Architecture Roadmap** components | B (business), C (data, application), D (technology) as "components" | E as "candidate components from Phases B, C and D" (ADM §9.2) | E produces the initial complete roadmap (ADM §9.4); **F** finalizes (ADM §10.4); G, H consume |
| Gap analysis results | B, inside the Requirements Specification | each following phase's Requirements Specification carries the results of the domains done so far; E consolidates | — |
| Constraints on the Technology Architecture | C, Data and Application parts (ADM §6.4, ADM §7.4) | D | — |
| Product information | — | D (candidate products, ADM §8.2) and E (ADM §9.2) | — |

## The delivery set (E, F)

| Deliverable | First produced | Consumed as input | Finalized |
|---|---|---|---|
| **Transition Architectures** | E, identified (inside the Definition Document and Roadmap, ADM §9.4) | F | F finalizes them inside the Definition Document (ADM §10.4); G deploys them as transitions |
| **Implementation and Migration Plan** | E, *draft* with the strategy (ADM §9.4) | F (draft), G, H (approved) | **F**, approved (ADM §10.4) |
| Implementation Factor catalog | E, step 1, part of the Roadmap (ADM §9.4) | F, inside the draft Roadmap (ADM §10.2) | — |
| Consolidated Gaps, Solutions and Dependencies matrix/assessment | E, inside the Requirements Specification (ADM §9.4) | F uses it to aggregate risks | — |
| Solution Building Blocks | E, inside the Roadmap (ADM §9.4) | F prices them; G's Solution Architects identify SBBs for remaining gaps | — |
| Change Requests for existing business programs and projects | — (arrive from outside) | E, F (ADM §9.2, ADM §10.2) | — |
| **Implementation Governance Model** | **F**, if any (ADM §10.4) | G, H | — |
| Re-usable ABBs | F (ADM §10.4) | — | G also lists ABBs among the deployed outputs |
| Change Requests for the Architecture Capability | F, from lessons learned (ADM §10.4) | H, as "Change Request — from lessons learned" (ADM §12.2) | — |
| Governance models and frameworks; planning methodologies | — (arrive from outside) | E, F (ADM §9.2, ADM §10.2) | — |

## The governance set (G, H)

| Deliverable | First produced | Consumed as input | Updated |
|---|---|---|---|
| **Architecture Contract** | enters G as a *standard* (ADM §11.2); G outputs it **signed** (ADM §11.4) | H, signed (ADM §12.2) | H, if necessary (ADM §12.4) |
| **Compliance Assessments** | **G** (ADM §11.4) | H (ADM §12.2) | H, if necessary (ADM §12.4) |
| **Change Requests** | G, implementation-driven (ADM §11.4) | H, as technology, business and lessons-learned Change Requests (ADM §12.2) | — |
| Architecture Governance Framework | Preliminary (ADM §2.4) | G (ADM §11.2) | H ensures it is executed |
| Architecture-compliant solutions deployed | G (ADM §11.4) | — | — |
| Architecture updates; changes to framework and principles | H, for maintenance changes (ADM §12.4) | — | — |
| New Request for Architecture Work | H, for major changes (ADM §12.4) | A, next cycle | — |

## Requirements Management

| Deliverable | Produced | Consumed |
|---|---|---|
| **Requirements Impact Assessment** | Requirements Management (ADM §13.4) | Requirements Management (ADM §13.2) — it iterates; the phase steps issue version n+1 |
| Architecture Requirements Specification (updated) | Requirements Management, if necessary (ADM §13.4) | every phase, via "architecture requirements populating an Architecture Requirements Specification" (ADM §13.2) |
| Architecture Requirements Repository | updated as part of the process, not listed as an output (ADM §13.4) | every phase selects its approved requirements from it |

## Reading a question

When a stem asks "which of the following is an output of Phase X", three checks settle almost
every item:

1. **Draft or finalized?** A draft Definition Document, Requirements Specification or Roadmap is
   B to E; finalized is F; "updated post-implementation" is G.
2. **Request or Statement?** The Request for Architecture Work is produced by Preliminary
   (optional), F (new iteration) and H (new cycle) and consumed by A. The Statement is produced
   by A and consumed by everything after.
3. **Standard or signed?** The Architecture Contract goes into G as a standard and comes out
   signed; H holds the signed one.

> **Trap.** Distractors are built by moving a deliverable one phase early or one phase late:
> a "finalized" Roadmap in E, a "signed" contract in F, a Communications Plan in G, a Requirements
> Specification out of A, an Implementation Governance Model out of E. Checking *first produced*
> against the tables above catches each of them.

## Check yourself

1. Which two phases both list Change Requests for existing business programs and projects as inputs?
2. Which deliverable is produced only in Phase F and consumed in G and H?
3. Which A-phase deliverable stops being listed as an input after Phase F?
4. Name every phase that can produce a Request for Architecture Work.
