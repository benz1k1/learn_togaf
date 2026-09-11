---
title: Applying iteration to the ADM — the four cycles, engagement classes and baseline/target first
unit: F6
objectives: ["6.1"]
refs: ["APPLY §2.1", "APPLY §2.2", "APPLY §2.3", "APPLY §2.4", "APPLY §2.5", "APPLY §2.5.1", "APPLY §2.5.2", "APPLY §2.6"]
reading_minutes: 10
source: authored
status: draft
---
## The ADM is not a waterfall

The ADM graphic and the phase-by-phase description can be read as a deterministic waterfall; that
presentation simply communicates the basics quickly. In practice two tightly linked concepts manage
complexity: **iteration** and **levels**. The standard uses "iteration" for three things: describing
a comprehensive Architecture Landscape through multiple ADM cycles, each bound to a Request for
Architecture Work; the integrated process within one cycle where phases interact; and managing
change to the Architecture Capability (APPLY §2.1).

| Kind of iteration | What it looks like |
|---|---|
| Landscape (between cycles) | Each project runs a full cycle from Phase A, bound by its Request for Architecture Work, and extends or changes the landscape; projects may run concurrently; one project may trigger another when it finds a need for more detailed work or impacts outside its scope |
| Within a cycle (Architecture Development) | Phases run concurrently (to manage B/C/D interrelationships); phases cycle in planned loops (to converge on a target when no higher-level context exists); phases are revisited to update work products (to converge on an executable roadmap or plan) |
| Capability | A new Preliminary Phase iteration to (re)establish the capability for a Request, or to adjust it after a Phase H Change Request |

(APPLY §2.1)

## The four iteration cycles

| Cycle | Purpose |
|---|---|
| **Architecture Capability** | Create and evolve the required capability — mobilise the activity by establishing or adjusting approach, principles, scope, vision and governance |
| **Architecture Development** | Create architecture content by cycling through or integrating the Business, Information Systems and Technology phases; stakeholder reviews are typically broader; as it converges, extensions into Opportunities & Solutions and Migration Planning check implementability |
| **Transition Planning** | Create formal change roadmaps for a defined architecture |
| **Architecture Governance** | Govern change activity progressing towards a defined Target Architecture |

(APPLY §2.2)

> **Trap.** Architecture Development is not confined to B, C, D: as the iterations converge, the
> cycle *extends into* Phases E and F so that implementability is considered while the
> architecture is finalised (APPLY §2.2).

## Classes of engagement

Architects are engaged in three areas: **identification of required change** (architecture as
visibility of IT capability for strategic decisions, outside any change initiative),
**definition of change** (structuring the nature and extent of an identified change), and
**implementation of change** (design governance — big-picture visibility, structural constraints,
evaluation criteria). Six engagement classes sit under them, and each has a characteristic focus
(APPLY §2.3):

| Area | Engagement class | Focus iteration cycles | Scope focus |
|---|---|---|---|
| Identification | Supporting Business Strategy | Capability; Development (baseline first) | Broad, shallow view to answer a strategic question |
| Identification | Portfolio Management of the Landscape | Capability; Development (baseline first) | Physical assessment of baseline applications and infrastructure for improvement opportunities |
| Identification | Portfolio Management of Projects | Transition Planning; Governance | Project dependencies and landscape impacts to sequence projects |
| Definition | Foundational Change Initiatives (known objective, not tightly scoped) | Capability; Development (baseline first); Transition Planning | Elaborate a vision by defining the baseline and what must change |
| Definition | Bounded Change Initiatives (outcome already agreed) | Development (**target first**); Transition Planning | Elaborate the target to an agreed vision; avoid perpetuating a sub-optimal baseline |
| Implementation | Governance of Change Implementation | Governance | Use vision, principles, requirements, target and roadmap so projects realise their benefit and align |

(APPLY §2.3)

## Baseline first or target first

**Baseline First** assesses the current landscape to find problem areas and opportunities; it suits
a baseline that is complex, poorly understood or not agreed, which is common where units have had
high autonomy. **Target First** elaborates the target in detail and maps back to the baseline to
find the change activity; it suits a target already agreed at a high level. If the baseline is
broadly understood, more value comes from focusing on the target first and describing the baseline
only as far as needed to identify changes. A team always considers the other state informally,
but should give one state priority to keep focus (APPLY §2.4).

## Iteration considerations

Some cycles run once; others have a natural minimum number of iterations, and the process differs
slightly between iterations. Checkpoints are placed according to stakeholder involvement: highly
involved stakeholders suit very frequent, informal checkpoints; less involved ones suit less
frequent, more formal ones — commonly at the end of each cycle or of several (APPLY §2.5).

**Between cycles**, each iteration completes an ADM cycle at a single level of description, and
**Phase F is used to initiate** new, more detailed architecture projects — higher-level
architecture guiding and constraining the more detailed (APPLY §2.5.1). **Within a cycle**, each
iteration crosses several phases, with activity that is *core* (primary focus), *light* (secondary)
or *informal* (APPLY §2.5.2):

| Cycle | Iteration 1 | Iteration 2 | Iteration n |
|---|---|---|---|
| Development, baseline first | Define the Baseline Architecture (B, C, D; E/F considered to test feasibility) | Define the Target and gaps against the baseline | Refine baseline, target and gaps |
| Development, target first | Define the Target Architecture | Define the Baseline and gaps against the target | Refine baseline, target and gaps |
| Transition Planning | Agree improvement opportunities against a provisional Transition Architecture; provisional Migration Plan | — | Agree the Transition Architecture, refining opportunities to fit |
| Architecture Governance | Mobilise governance and change management processes, people and technology | — | Periodic reviews of change initiatives; a Change Request may send a requirement back to the Preliminary Phase or the development phases |

(APPLY §2.5.2)

## What decides how you iterate

The ADM should always be used iteratively; how depends on: the formality and nature of process
checkpoints; the expected level of stakeholder involvement; the number of teams and their
relationships; the maturity of the solution area and expected rework; attitude to risk (does
partial work circulate? must solutions be proved in a trial?); and the class of engagement
(APPLY §2.6).

## Check yourself

- Which cycle does a Bounded Change Initiative focus on, and which approach — baseline or target first?
- Which phase initiates new, more detailed architecture projects in iteration between cycles?
- What is the first iteration of the Architecture Governance cycle for?
