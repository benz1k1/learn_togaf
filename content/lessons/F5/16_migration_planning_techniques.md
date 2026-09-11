---
title: Migration planning techniques in Phases E and F
unit: F5
objectives: ["5.3"]
refs: ["ADM §9.1", "ADM §9.3.3", "ADM §9.3.6", "ADM §9.3.8", "ADM §9.3.9", "ADM §9.3.10", "ADM §9.3.11", "ADM §9.5", "ADM §10.1", "ADM §10.3.1", "ADM §10.3.2", "ADM §10.3.3", "ADM §10.3.4", "ADM §10.3.5", "ADM §10.3.6", "ADM §10.5", "CONTENT §3.6.8", "CONTENT §3.6.9"]
reading_minutes: 11
source: authored
status: draft
---
> In the 10th Edition the migration planning techniques are described inside the Phase E and
> Phase F chapters of the ADM document, and the tables and matrices themselves are catalogued as
> Phase E and F artifacts in the Architecture Content document (ADM §9.3; CONTENT §3.6.8).

## Four concepts that bridge developing and delivering

Phase E is about *how* to deliver the architecture: it takes the complete set of gaps across all
domains, groups the changes into work packages within the enterprise's portfolios, and builds a
best-fit roadmap from stakeholder requirements, transformation readiness, opportunities and
constraints — focusing on the final target while realising incremental value. Four concepts are
key (ADM §9.5):

| Concept | One-line meaning |
|---|---|
| Architecture Roadmap | Work packages on a timeline that realise the Target Architecture |
| Work Package | A logical group of changes needed to realise the target |
| Transition Architecture | The enterprise at an architecturally significant state between baseline and target — an interim target to converge on |
| Implementation and Migration Plan | The schedule of projects that will realise the target |

Phase E's objectives are to produce the initial complete Architecture Roadmap from the gap results
and candidate roadmap components of B–D, decide whether an incremental approach is needed and if
so identify Transition Architectures that deliver continuous business value, and define the SBBs
that finalise the target (ADM §9.1). Phase F then finalises the roadmap and plan, co-ordinates the
plan with the enterprise's wider change portfolio, and makes sure key stakeholders understand the
value and cost of work packages and Transition Architectures (ADM §10.1).

## Phase E techniques

**Consolidated Gaps, Solutions, and Dependencies matrix.** The B–D gap results are consolidated
into one list with potential solutions and dependencies; the matrix identifies SBBs that could
address one or more gaps. Similar gaps are grouped, referring to the **Implementation Factor
catalog** — which records the factors that affect the plan: risks, issues, assumptions,
dependencies, actions and impacts, each with a description and the deductions drawn from it (ADM
§9.3.3; CONTENT §3.6.8). Dependencies drive implementation sequence and the co-ordination
required; grouping them is the basis for projects and increments — "addressing dependencies serves
as the basis for most migration planning" (ADM §9.3.6).

**Implementation and Migration Strategy.** First choose an overall approach — **Greenfield** (a
completely new implementation), **Revolutionary** (radical switch-on/switch-off) or
**Evolutionary** (convergence: parallel running or phased introduction) — then a methodology to
address the risks in the matrix: **quick win (snapshots)**, **achievable targets** or the **value
chain method**. Together with the dependencies these become the basis for the work packages (ADM
§9.3.8).

**Work packages.** Using the matrix and the factor catalog, group activities into work packages
and fill in the "Solution" column: new development, an existing product, or a purchase, and
in-house versus contract. Classify every current system as **Mainstream** (part of the future
system), **Contain** (to be replaced or modified within the planning horizon of about three years)
or **Replace**. Decompose top-level packages into increments delivering capability increments, and
group packages into portfolios and projects (ADM §9.3.9).

**Transition Architectures.** Where an incremental approach is needed, one or more Transition
Architectures give clear targets along the roadmap. Each should deliver **measurable business
value**, and the intervals between them need not be uniform. They are based on the chosen approach,
the matrix, the project list and the enterprise's capacity to absorb change; unless there is a
compelling reason, do the difficult activities after those that most easily deliver missing
capability (ADM §9.3.10).

**Roadmap and plan, draft.** Work packages and Transition Architectures are consolidated into the
draft Architecture Roadmap (a timeline from baseline to target) which frames Phase F, and into the
draft Implementation and Migration Plan, at a level of detail matching the Architecture Definition
Document. A data-driven sequence (build the systems that create data before those that process
it) is one approach. Finally the Vision, ADD and Requirements Specification are updated (ADM
§9.3.11).

## Phase F techniques

**Management framework interactions.** Four frameworks must work together for the plan to
succeed — Business Planning, Enterprise Architecture, Project/Portfolio Management and Operations
Management — and the plan must be reflected in each, possibly ending up as part of another
framework's plan (ADM §10.3.1).

**Business value per work package.** Establish what value means and how it is measured, then apply
it to each project and increment. Issues to settle: performance evaluation criteria, return-on-
investment criteria, a definition of business value (using techniques such as the value chain),
critical success factors, measures of effectiveness, and strategic fit. Risks from the Phase E
matrix are aggregated onto the projects, and value is estimated with the **Business Value and Risk
Matrix** — a value index (e.g. compliance to principles, financial contribution, strategic
alignment, competitive position) against a risk index (size and complexity, technology,
organisational capacity, impact of failure), with weighted criteria approved by senior management
*before* the options are known (ADM §10.3.2; CONTENT §3.6.9).

**Resources and timing.** Estimate resources and timing per project and increment, splitting costs
into capital and operations/maintenance, and look for decommissioning offsets (ADM §10.3.3).
**Prioritise** projects by business value against delivery cost — net benefit of the SBBs over
time, risks verified as mitigated — and gain stakeholder consensus on the prioritised list; a
project may rank high because it is a critical step towards a large benefit even if its own
benefit is small (ADM §10.3.4).

**Confirm the roadmap and update the ADD.** Review the time-spans between Transition
Architectures against value and risk, then consolidate deliverables by project. A **Transition
Architecture State Evolution Table** shows the proposed state of the domain architectures over the
transitions (services marked new / retain / transition / replace); an **Architecture Definition
Increments Table** aligns projects and their deliverables with the Transition Architectures (ADM
§10.3.5; CONTENT §3.6.9). The completed plan integrates all projects, dependencies and impacts,
with Transition Architectures as portfolio milestones (ADM §10.3.6).

> **Trap.** Where each table lives: the ADM *creates* both the State Evolution Table and the
> Increments Table in the Phase F step "Confirm Architecture Roadmap and update the ADD" (ADM
> §10.3.5), while the Content document *lists* the Increments Table among Phase E artifacts and
> the State Evolution Table and Business Value and Risk Matrix among Phase F artifacts (CONTENT
> §3.6.8, §3.6.9). The Implementation Factor catalog and the Consolidated Gaps matrix are Phase E
> in both documents.

Phase E hands over an incomplete roadmap and plan; Phase F integrates them with the enterprise's
other change activity, adding portfolio- and project-level detail, and closes the cycle with
lessons learned (ADM §10.5).

## Check yourself

- Name the three strategic implementation approaches and the three common methodologies.
- What are the three classifications for a current system?
- Which Phase F step uses the Business Value and Risk Matrix, and who approves its criteria?
