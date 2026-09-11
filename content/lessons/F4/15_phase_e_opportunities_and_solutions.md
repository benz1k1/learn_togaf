---
title: Phase E, Opportunities and Solutions, in depth
unit: F4
objectives: ["4.3", "4.5"]
refs: ["ADM §9", "ADM §9.1", "ADM §9.2", "ADM §9.2.1", "ADM §9.2.2", "ADM §9.2.3", "ADM §9.3", "ADM §9.3.1", "ADM §9.3.2", "ADM §9.3.3", "ADM §9.3.4", "ADM §9.3.5", "ADM §9.3.6", "ADM §9.3.7", "ADM §9.3.8", "ADM §9.3.9", "ADM §9.3.10", "ADM §9.3.11", "ADM §9.4", "ADM §9.5"]
reading_minutes: 12
source: authored
status: draft
---
## What the phase is for

Phase E identifies the delivery vehicles — projects, programs or portfolios — that will deliver
the Target Architecture defined in Phases B to D (ADM §9). Three objectives (ADM §9.1):

| Objective | In plain words |
|---|---|
| Generate the **initial complete version of the Architecture Roadmap**, based on the gap analysis and candidate roadmap components from Phases B, C and D | one roadmap out of three sets of components |
| Determine whether an **incremental approach** is required and, if so, identify **Transition Architectures** that deliver continuous business value | decide on stepping stones |
| Define the overall **Solution Building Blocks (SBBs)** to finalize the Target Architecture based on the ABBs | pick solutions for the architecture building blocks |

The third objective is the one people forget. Phase E is the first place SBBs are defined.

## Approach

Phase E concentrates on **how** to deliver the architecture (ADM §9.5). It takes the complete
set of gaps across all domains and logically groups the changes into work packages within the
enterprise's portfolios, building a best-fit roadmap from stakeholder requirements, the
enterprise's transformation readiness, the opportunities and solutions identified, and the
implementation constraints. The guiding idea: focus on the final target while realizing
incremental business value.

Phase E is the *initial* step in creating the Implementation and Migration Plan, which Phase F
completes. Four concepts are key to moving from developing to delivering:

| Concept | Definition (ADM §9.5) |
|---|---|
| Architecture Roadmap | lists individual work packages on a timeline that realizes the Target Architecture |
| Work package | a logical group of changes needed to realize the Target Architecture |
| Transition Architecture | the enterprise at an architecturally significant state between Baseline and Target; an interim target the organization can converge on |
| Implementation and Migration Plan | a schedule of the projects that will realize the Target Architecture |

## Inputs

| Group | Inputs |
|---|---|
| External (ADM §9.2.1) | architecture reference materials; product information |
| Non-architectural (ADM §9.2.2) | Request for Architecture Work; Capability Assessment; Communications Plan; **planning methodologies** |
| Architectural (ADM §9.2.3) | Organizational Model; **governance models and frameworks** (corporate business planning, EA, portfolio/program/project management, system development, operations); Tailored Framework; Statement of Architecture Work; Architecture Vision; Architecture Repository; draft Architecture Definition Document; draft Architecture Requirements Specification (architectural requirements, gap results from all four domains, IT Service Management requirements); **Change Requests for existing business programs and projects**; **candidate Architecture Roadmap components from Phases B, C and D** |

## Steps

Eleven steps; everything started must be closed in step 11 (ADM §9.3).

| # | Step | Key point |
|---|---|---|
| 1 | Determine/confirm key corporate change attributes | create the **Implementation Factor catalog** as the record of implementation and migration decisions; assess the transition capabilities of the organization units (ADM §9.3.1) |
| 2 | Determine business constraints for implementation | business drivers that constrain the implementation sequence; review the maturity assessment (ADM §9.3.2) |
| 3 | Review and consolidate gap analysis results from Phases B to D | build the **Consolidated Gaps, Solutions and Dependencies matrix**; identify SBBs that address one or more gaps; SBBs are created from the candidate roadmap components (ADM §9.3.3) |
| 4 | Review consolidated requirements across related business functions | find the minimal set of requirements that shared solutions and services can satisfy (ADM §9.3.4) |
| 5 | Consolidate and reconcile interoperability requirements | minimize conflicts, especially those imposed by re-used SBBs, COTS products and third parties; either build a translating block or change the conflicting block's specification (ADM §9.3.5) |
| 6 | Refine and validate dependencies | dependencies determine implementation sequence and increments; "addressing dependencies serves as the basis for most migration planning" (ADM §9.3.6) |
| 7 | Confirm readiness and risk for business transformation | review the Business Transformation Readiness Assessment from Phase A; document risks in the consolidated matrix (ADM §9.3.7) |
| 8 | Formulate Implementation and Migration Strategy | three approaches: **greenfield, revolutionary, evolutionary**; three methodologies: **quick win, achievable targets, value chain** (ADM §9.3.8) |
| 9 | Identify and group major work packages | fill the "Solution" column (new development, existing product, purchase); classify current systems as **mainstream, contain or replace**; group packages into portfolios and projects (ADM §9.3.9) |
| 10 | Identify Transition Architectures | needed when the change requires an incremental approach; each must deliver measurable business value; spacing need not be uniform (ADM §9.3.10) |
| 11 | Create the Architecture Roadmap and Implementation and Migration Plan | the draft roadmap describes the timeline from Baseline to Target and frames Phase F; the draft plan shows the activity needed to realize it; update the Vision, Definition Document and Requirements Specification (ADM §9.3.11) |

## Outputs

(ADM §9.4)

| Output | Contents |
|---|---|
| Refined Architecture Vision phase deliverables | Architecture Vision, now including **types and degrees of interoperability**; Statement of Architecture Work |
| Draft Architecture Definition Document | all Baseline and Target domain architectures updated if necessary; **Transition Architecture**, number and scope as necessary; views |
| Draft Architecture Requirements Specification | the **Consolidated Gaps, Solutions and Dependencies Assessment** |
| **Capability Assessments** | Business Capability Assessment and IT Capability Assessment |
| **Architecture Roadmap** | work package portfolio (description, requirements, dependencies, business value, …), Implementation Factor catalog, identification of Transition Architectures, implementation recommendations, SBBs |
| **Implementation and Migration Plan, Draft** | including the Implementation and Migration Strategy |

> **Trap.** E versus F. Phase E produces the *initial complete* Architecture Roadmap and a
> *draft* Implementation and Migration Plan; Phase F *finalizes* both. If an option says Phase E
> "completes" or "approves" the plan, it is describing Phase F. If an option says Phase F
> "generates the initial Architecture Roadmap", it is describing Phase E.

> **Trap.** The Implementation Factor catalog and the Consolidated Gaps, Solutions and
> Dependencies matrix are created in Phase E (steps 1 and 3). Phase F *uses* them (risks are
> aggregated from the matrix; the catalog arrives as part of the draft roadmap).

## Check yourself

1. State the third objective of Phase E.
2. Name the three strategic implementation approaches and the three implementation methodologies.
3. What are the three classifications for a current system in step 9?
4. Which Phase A result is reviewed in step 7?
