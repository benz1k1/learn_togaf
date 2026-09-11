---
title: Phases B to H and Requirements Management
unit: F4
objectives: ["4.3", "4.4", "4.5", "4.6", "4.7"]
refs: ["ADM §4", "ADM §5", "ADM §8", "ADM §9", "ADM §10", "ADM §11", "ADM §12", "ADM §13"]
reading_minutes: 12
source: authored
status: draft
---
## B, C, D: the same nine steps three times

Each development phase runs the same sequence: select reference models, viewpoints and tools;
describe the **Baseline**; describe the **Target**; **gap analysis**; define **candidate
roadmap components**; resolve impacts across the Landscape; formal stakeholder review;
finalise the architecture; create (add to) the **Architecture Definition Document**. Each phase
outputs a draft Architecture Definition Document, a draft **Architecture Requirements
Specification** with the gap results, and its domain's components of the Architecture Roadmap.

Phase C is *one* phase with two parts, Data and Application, developed in either order.

## E and F: from gaps to a plan

**Phase E** is the first phase concerned with implementation. It consolidates the gaps and
candidate components from B, C and D, groups them into **work packages**, decides whether
**Transition Architectures** are needed, and produces the **Architecture Roadmap** and an
*outline* Implementation and Migration Plan. Techniques: Implementation Factor Catalog,
Consolidated Gaps, Solutions and Dependencies Matrix.

**Phase F** finalises. It assigns **business value** to each work package, estimates resources
and timing, prioritises by cost/benefit and risk, confirms the Roadmap, completes the
**Implementation and Migration Plan**, produces the **Implementation Governance Model**, and
closes the development cycle with lessons learned. Techniques: Architecture Definition
Increments Table, Transition Architecture State Evolution Table, Business Value Assessment.

## G and H: governing and living with the architecture

**Phase G** is where the architecture and the solution meet. The **Architecture Contract** is
signed with the implementing organisation, development is guided, **compliance reviews** are
performed, and change requests arising from implementation are handled. Outputs: the signed
contract, Compliance Assessments, Change Requests, and an architecture-compliant deployed
solution.

**Phase H** keeps the architecture alive. It monitors business and technology change, runs a
value-realisation process, and classifies every change request as a **simplification**, an
**incremental** change, or a **re-architecting** change. Only re-architecting change starts a
new ADM cycle, through a new Request for Architecture Work.

## Requirements Management

Not a phase in the sequence but the process at the centre: it identifies, baselines, monitors
and stores requirements in the **Architecture Requirements Repository**, assesses the impact
of changes (the **Requirements Impact Assessment** names the phases to revisit), and feeds the
current set to every phase. The *disposal* of a requirement is done by the phase, not by the
process.
