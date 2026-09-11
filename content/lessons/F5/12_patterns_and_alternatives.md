---
title: Architecture Patterns, and Architecture Alternatives and Trade-Offs
unit: F5
objectives: ["5.5"]
refs: ["TECH §4.1", "TECH §4.1.1", "TECH §4.1.2", "TECH §4.1.3", "TECH §9.1", "TECH §9.2", "TECH §9.2.1", "TECH §9.2.2", "TECH §9.2.3"]
reading_minutes: 9
source: authored
status: draft
---
## Patterns

Patterns are increasingly important for describing enterprise architectures across disciplines,
domains and levels of detail. There is no single standard for describing an enterprise
architecture pattern — but there is a pattern for describing patterns (TECH §4.1).

A pattern is "an idea that has been useful in one practical context and will probably be useful
in others". In the TOGAF Standard a pattern is a way of **putting building blocks into context**:
building blocks are *what* you use; patterns tell you *how*, *when* and *why* to use them and
what trade-offs you make. They help the architect find combinations of ABBs and SBBs that have
proved effective before. The idea originates with the buildings architect Christopher Alexander
and was taken up by software architects (TECH §4.1.1).

> **Trap.** A pattern is not itself a building block. "Building blocks are what you use; patterns
> tell you how" is the sentence to remember (TECH §4.1.1).

### Content of a pattern

No single format is universal, but most patterns contain these elements (TECH §4.1.2):

| Element | Meaning |
|---|---|
| Name | Memorable label |
| Problem | The intent — goals and objectives to reach within the context and forces |
| Context | Preconditions; the initial state before the pattern is applied |
| Forces | The constraints and qualities in tension — security, performance, scalability, maintainability and so on — which make the trade-offs explicit |
| Solution | How to achieve the goals: static structure and dynamic behaviour, actors and collaborations |
| Resulting context | Post-conditions; which forces were resolved and which remain; other patterns now applicable |
| Examples | Sample applications illustrating the other elements |
| Rationale | Why the pattern works — its internal workings |
| Related patterns | Predecessor, successor, alternative and co-dependent patterns |
| Known uses | Existing systems that prove the pattern solves a recurring problem |

A pattern may open with an *abstract* describing the problems it addresses and its audience
(TECH §4.1.2).

### Terminology

Three kinds of software pattern are distinguished: an **architecture pattern** gives a fundamental
structural organisation of subsystems and their relationships; a **design pattern** refines
subsystems or components; an **idiom** is a low-level pattern tied to one programming language.
Those definitions cover software only; the standard is concerned with patterns for architecting
enterprise information systems — software, hardware, networks and people. Patterns are re-usable
assets of the Architecture Continuum to be considered in **Phases A to D**, they help in composing
views, and relevant patterns may be discovered during business-scenario work (TECH §4.1.3).

## Architecture Alternatives and Trade-Offs

More than one Target Architecture will usually conform to the Architecture Vision, principles and
requirements. Identifying alternatives, and presenting them with their trade-offs to stakeholders,
builds understanding and draws out hidden agendas, principles and requirements that could affect
the final target (TECH §9.1).

Rarely does one alternative satisfy every stakeholder concern. Alternatives are **commonly defined
per domain** to simplify analysis, then merged for the whole architecture. The method has three
parts — select criteria; define alternatives and understand each; choose one or combine features
into the proposed alternative — done in just enough detail to decide, and usable in any phase at
any level (TECH §9.2).

| Part | What it involves |
|---|---|
| Criteria | Derived from principles, requirements, vision and stakeholder concerns; example criteria include flexibility, time and cost including transitions and "islands of stability", benefit period, adherence to styles, delivery method (re-use / develop / buy), minimal business impact, minimised risk (TECH §9.2.1) |
| Identify alternatives | For each: define overview criteria; describe the architecture with the necessary views without excess detail; estimate gaps between baseline and this alternative (informally if the baseline is undefined); understand impacts and trade-offs across the Architecture Landscape, running projects and other phases (TECH §9.2.2) |
| Choose and define in detail | Understand strengths and weaknesses; compare against criteria; select or combine with stakeholders; assemble the alternative through all viewpoints; resolve landscape impacts; conduct a formal stakeholder review to decide and fund (TECH §9.2.3) |

> **Trap.** The trade-off technique is used in Phase E to investigate different Target
> Architecture alternatives with stakeholders when consolidating gaps, but the standard says the
> method "can be used for any phase at any level" (TECH §9.2).

## Check yourself

- Which pattern element records which forces remain unresolved?
- In which phases does the standard say re-usable assets such as patterns should be considered?
- Why are alternatives usually defined per domain first?
