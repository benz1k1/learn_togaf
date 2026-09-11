---
title: Business Scenarios, and Business Capability Planning (from the Series Guides)
unit: F5
objectives: ["5.4", "5.5"]
refs: ["GUIDE:business-scenarios §1", "GUIDE:business-scenarios §2", "GUIDE:business-scenarios §3.1", "GUIDE:business-scenarios §3.3", "GUIDE:business-scenarios §4", "GUIDE:business-scenarios §5", "GUIDE:business-scenarios §6", "GUIDE:business-scenarios §9.2", "GUIDE:business-scenarios §13", "GUIDE:business-capability-planning §1", "GUIDE:business-capability-planning §5.1", "GUIDE:business-capability-planning §6", "GUIDE:business-capability-planning §6.2", "GUIDE:business-capability-planning §6.3", "GUIDE:business-capability-planning §6.4", "GUIDE:business-capability-planning §7.1", "GUIDE:business-capability-planning §7.2"]
reading_minutes: 11
source: authored
status: draft
---
> In the 10th Edition neither technique lives in the ADM Techniques document. Business Scenarios
> is a TOGAF Series Guide, and capability-based planning is covered by the *Business Capability
> Planning* Series Guide (GUIDE:business-scenarios §1; GUIDE:business-capability-planning §1).

## Business Scenarios

An architecture succeeds to the extent that it is linked to business requirements; building
without understanding "why" gives a fine solution to the wrong problem. The Business Scenario
method validates, elaborates or changes the premise behind an architecture effort by documenting
the key elements of a scenario in successive iterations — each planned, gathered, analysed,
documented and reviewed — until the understanding is fit for purpose. It is used principally in the
Preliminary, Architecture Vision and Business Architecture phases, and elsewhere when requirements
must be derived (GUIDE:business-scenarios §1).

A Business Scenario is a uniform description of five things (GUIDE:business-scenarios §1):

| Element |
|---|
| Real business problems |
| The business and technology environment in which they occur |
| Value streams enabled by capabilities |
| The desired outcome(s) of proper execution |
| The human and computing actors that provide the capabilities |

A good scenario is **SMART**: *Specific* (what must be done), *Measurable* (clear success
metrics), *Actionable* (segments the problem and gives a basis for the solution), *Realistic*
(solvable within physical, time and cost bounds), *Time-bound* (a clear statement of when the
opportunity expires) (GUIDE:business-scenarios §1).

> **Trap.** The "A" is *Actionable* and the "R" is *Realistic* — not "Achievable" or
> "Relevant". And a Business Scenario is **not** a use-case (more detailed human–computer
> interaction), not a business model, business case or plan, not SPIN selling, and not an
> engineering specification (GUIDE:business-scenarios §1).

**Benefits.** A scenario is a complete description of a problem in both business and
architectural terms, so individual requirements are seen in context; without it the architecture
may rest on an incomplete requirement set, the business value is unclear and the relevance of
solutions is unclear. It brings business line management in early — winning buy-in — and gives
vendors a language for linking problems and solutions. Done right it yields better solutions,
faster capability realisation and lower cost (GUIDE:business-scenarios §2).

**Creating one.** Six steps capture the five elements: identify, document and rank the problem;
identify the business and technical environment and model it (value streams, capabilities);
identify and document desired outcomes and make them SMART; identify the human actors and their
place in the business model; identify the computer actors and their place in the technology
model; check fitness for purpose and refine only if necessary. Each iteration runs the steps
*plan → gather → analyse → document → review* (GUIDE:business-scenarios §3.1). Those steps
repeat across three phases — **Premise Formulation**, **Initial Verification** and
**Refinement** — that go from a premise to a scenario approved by business leaders, which is
then placed in the **Requirements Repository** as the high-level requirements statement that
drives and validates the architecture work (GUIDE:business-scenarios §3.3).

**Content and contributors.** The document sequences the critical steps and interactions between
actors and declares their responsibilities, pre-conditions and technical requirements; it mixes
graphics (models that relate actors and interactions) with descriptive text
(GUIDE:business-scenarios §4). Business management contributes most early while the problem is
explored; the architect's contribution peaks later as solutions are described; vendors, if
involved, contribute last (GUIDE:business-scenarios §5).

**In the ADM.** Scenarios figure most prominently in **Phase A**, to define business requirements
and build consensus, and are also used in Phase B to derive the architecture's characteristics
from high-level requirements; they can serve any phase where requirements must be derived — even
the Preliminary Phase, to define requirements for the EA capability itself
(GUIDE:business-scenarios §6). Goals need measures attached to become SMART objectives, giving a
yardstick for fitness-for-purpose and letting decisions be traced back to criteria
(GUIDE:business-scenarios §9.2). Scenarios are a tool, not the objective — watch for feature creep
(GUIDE:business-scenarios §13).

## Business Capability Planning

Planning starts with homework: the mission, vision and values; the organisation chart, financials
and plans; a logical catalog of IT. Value streams show how the organisation delivers value in
stages with exit criteria and outcomes; stages map to business capabilities; a **business
capability catalog** defines each capability. Capabilities are instantiated with people, processes
and tools, and capabilities are building blocks for value streams, not ends in themselves
(GUIDE:business-capability-planning §1).

A **value stream** is an end-to-end collection of value-adding activities that produce an overall
result for a customer, stakeholder or end user; its stages each add incremental stakeholder value.
Streams may be externally triggered (a customer buying) or internally triggered (a manager hiring),
and value is always defined from the stakeholder's perspective, not by the cost to produce
(GUIDE:business-capability-planning §5.1).

A **business capability** is an ability an organisation possesses, expressed in general,
high-level terms and requiring a combination of people, processes and tools. It says *what* the
business does, not how, why or where — those details appear once it is mapped to value streams and
modelled as an instance. A capability may exist today, be needed for a new value stream, or be
retired (GUIDE:business-capability-planning §6).

| Building the catalog | |
|---|---|
| Top-down | Start with the 20–30 highest-level capabilities with senior leaders; efficient, but needs their real involvement |
| Bottom-up | Defined within parts of the business when time allows; harder to reconcile without strong governance |
| Incremental | Applying the catalog to value streams and instances reveals missing, redundant or additional capabilities |

The catalog is the complete, stable set for the organisation, grouped into categories for
navigation, and independent of organisation structure, processes, IT and product portfolio. Past
about **100 items**, entries are probably instances, components or value stream stages. A small
curation group of two to four people and a change process work best
(GUIDE:business-capability-planning §6.2).

Cross-mapping capabilities to value stream stages shows which capabilities are critical to
stakeholder value and must be instantiated to a sufficient standard
(GUIDE:business-capability-planning §6.3). Capabilities as used in a value stream are
**instances**, which avoids duplicates in the catalog; modelling instances reveals gaps in actors,
resources, applications or processes and lets an investment plan for capability increments be
made. For the architect, instances link the TOGAF domains, with the value stream giving business
context (GUIDE:business-capability-planning §6.4).

Improvement is planned in four scenarios, always grounded in improving the value streams:
**optimise** (change one or more components of an instance — most common), **consolidate**
(usually via application rationalisation, e.g. post-merger), **create** (new streams or
instances, taking care not to duplicate) and **retire** (rare; remove the capability from the
catalog, checking for hidden dependent value streams) (GUIDE:business-capability-planning §7.1).
Capabilities often cannot reach the target in one step; gaps addressed together that keep the
value stream functional form a **plateau**, and the gaps carry dependencies that sequence the
increments delivered through work packages (GUIDE:business-capability-planning §7.2).

## Check yourself

- List the five elements of a Business Scenario and the five letters of SMART.
- Where does an approved Business Scenario go, and what is it used for downstream?
- What does a business capability describe, and what does it deliberately leave out?
