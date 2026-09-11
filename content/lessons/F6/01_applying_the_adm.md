---
title: Iteration, the Architecture Landscape, partitioning, security and agile
unit: F6
objectives: ["6.1", "6.2", "6.3"]
refs: ["APPLY §2", "APPLY §3", "APPLY §4", "GUIDE:integrating-risk-and-security §4", "GUIDE:agile-sprints §3.3", "GUIDE:enabling-enterprise-agility §4.1"]
reading_minutes: 8
source: authored
status: draft
---
## Four iteration cycles (APPLY §2)

| Cycle | Phases | Purpose |
|---|---|---|
| Architecture Capability | Preliminary, A | establish or adjust the capability |
| Architecture Development | A, B, C, D | create the architecture content |
| Transition Planning | E, F | plan the change |
| Architecture Governance | G, H | govern implementation and change |

Iteration can be baseline-first (describe what exists, then the target) or target-first
(describe the target, then find the baseline needed to plan the gaps).

## Three levels of the Architecture Landscape (APPLY §3)

**Strategic** Architecture is the executive, long-term summary; **Segment** Architecture is
the programme or portfolio level; **Capability** Architecture is the detailed, project-level
description of one capability increment. Lower levels are constrained by higher ones.

## Partitioning (APPLY §4)

Architectures are partitioned by subject matter, time and level of detail, so that different
teams can work in parallel without conflict and so that reuse is possible. The Preliminary
Phase decides the partitions; each partition has its own Architecture Repository contents.

## Security and agile (Series Guides — not in APPLY)

Security is addressed in every phase, not as a separate domain; the Series Guide on risk and
security integration goes deeper. The ADM works with agile delivery by treating an architecture
increment as a backlog item, iterating in short cycles at the capability level, and keeping
governance light but present.
