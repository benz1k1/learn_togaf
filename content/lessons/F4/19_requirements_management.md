---
title: Requirements Management in depth
unit: F4
objectives: ["4.3", "4.7"]
refs: ["ADM §13", "ADM §13.1", "ADM §13.2", "ADM §13.3", "ADM §13.4", "ADM §13.5", "ADM §13.5.1", "ADM §13.5.2", "ADM §13.5.3"]
reading_minutes: 9
source: authored
status: draft
---
## What it is for

Requirements Management is the process of managing architecture requirements throughout the ADM
(ADM §13). The standard's chapter calls it a "phase" in its headings, but the approach section
is explicit that it is a *process*, the circle in the centre of the ADM graphic. Three
objectives (ADM §13.1):

| Objective | In plain words |
|---|---|
| Ensure the Requirements Management process is **sustained** and operates for all relevant ADM phases | it never stops |
| **Manage** architecture requirements identified during any execution of the cycle or a phase | store, track, change |
| Ensure relevant requirements are **available** to each phase as it is executed | every phase can see the current set |

## Approach

The centre circle denotes **a dynamic process, not a static set of requirements**: requirements
and their changes are identified, stored and fed into and out of the phases, and between cycles
(ADM §13.5.1). Architecture deals with uncertainty and with drivers outside the enterprise's
control, so requirements will change. The sentence the exam tests most: **the Requirements
Management process itself does not dispose of, address or prioritize any requirements; that is
done within the relevant phase.** An **Architecture Requirements Repository** is recommended for
recording all requirements; unlike the Architecture Requirements Specification and the
Requirements Impact Assessment, it can hold information from multiple ADM cycles.

Requirements development (ADM §13.5.2): the first high-level requirements come from the
Architecture Vision, via the business scenario or a similar technique. Every phase from
Preliminary to H selects the approved requirements for that phase from the repository and
specification, and updates their status at the end. New requirements within the scope of the
current Statement of Architecture Work go into the Architecture Requirements Specification;
requirements outside it go into the Repository for management by the process. Requirements are
functional and non-functional; when defining them the architect considers assumptions,
constraints, domain principles, policies, standards, organization guidelines and specifications.

Resources (ADM §13.5.3): the standard does not mandate any requirements process or tool — it
states what an effective process should achieve ("requirements for requirements"). Business
scenarios are the named technique; COTS requirements tools exist.

## Inputs

(ADM §13.2) — a short, flat list, with no external/non-architectural/architectural split:

| Input |
|---|
| A populated Architecture Repository |
| Organizational Model for Enterprise Architecture |
| Tailored Architecture Framework |
| Statement of Architecture Work |
| Architecture Vision |
| Architecture requirements, populating an Architecture Requirements Specification |
| **Requirements Impact Assessment** |

## Steps

The steps are a table with **two columns**: some are done by the Requirements Management
process, others by the ADM phase that is running (ADM §13.3).

| # | Done by | Step |
|---|---|---|
| 1 | ADM phase | Identify requirements (via value streams, business scenarios, user experiences, management information) and document them in the Architecture Requirements Specification and Requirements Repository |
| 2 | Requirements Management | Establish baseline requirements: priorities, stakeholder agreement, documentation |
| 3 | Requirements Management | Monitor baseline requirements |
| 4 | ADM phase | Identify new and changed requirements: remove, add, modify, re-assess priorities |
| 5 | Requirements Management | Identify changed requirements and record priorities; identify and manage conflicts; **generate the Requirements Impact Assessment** |
| 6 | ADM phase | Assess the impact of changed requirements on the current and previous phases; decide to implement or defer; issue Requirements Impact Assessment version n+1 |
| 7 | ADM phase | Implement requirements arising from Phase H |
| 8 | Requirements Management | Update the Architecture Requirements Repository, including the stakeholder views affected |
| 9 | ADM phase | Implement change in the current phase |
| 10 | ADM phase | Assess and revise gap analysis for past phases; a **gap requirement** is something eliminated by accident and needs a Target Architecture change |

## Outputs

(ADM §13.4)

| Output | Note |
|---|---|
| **Requirements Impact Assessment** | identifies the phases of the ADM that need to be revisited; iterates until a final version with full implications (costs, timescales, metrics) |
| Updated Architecture Requirements Specification | if necessary; updated once the cycle's requirements are finalized |

The Architecture Requirements Repository is updated as part of the process, but the standard
does not list it under outputs.

> **Trap.** Two things Requirements Management does *not* do: it does not dispose of, address or
> prioritize requirements (the phase does), and it is not a step in the sequence A to H (it runs
> alongside all of them, including the Preliminary Phase). Options that make it "the phase after
> H" or "the phase that decides which requirements to implement" are wrong.

> **Trap.** The Requirements Impact Assessment is both an *input* and an *output* — it comes back
> in each iteration. Do not confuse it with the Architecture Requirements *Specification* (a
> Phase B to F deliverable) or the Architecture Requirements *Repository* (holds many cycles).

## Check yourself

1. Which document identifies the ADM phases that must be revisited?
2. What can the Architecture Requirements Repository hold that the Specification cannot?
3. Which of the ten steps does the Requirements Management process itself perform?
4. Where do the first high-level requirements come from?
