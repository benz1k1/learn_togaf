---
title: The four architecture domains, and the abstraction levels that cross them
unit: F1
objectives: ["1.3"]
refs: ["INTRO §3.2", "INTRO §3.3", "INTRO §3.4", "INTRO §3.7", "INTRO §4.12", "ADM §1.5.2", "ADM §1.5.4"]
reading_minutes: 7
source: authored
status: draft
---
## Two definitions of "architecture"

The standard keeps two meanings of *architecture* and uses whichever fits the context. The first is
borrowed from ISO/IEC/IEEE 42010:2022: the fundamental concepts or properties of an entity in its
environment, together with the governing principles for realising and evolving it and its
lifecycle processes. The second is the older structural reading: the components, how they relate,
and the principles and guidelines that govern their design and evolution over time (INTRO §3.2).
The standard embraces ISO 42010 terminology without strictly adhering to it, and treats the
enterprise as a system (INTRO §3.2).

## The four domains

Four architecture domains are commonly accepted as subsets of an overall enterprise architecture,
and the standard supports all four (INTRO §3.3):

| Domain | What it describes |
|---|---|
| **Business Architecture** | business strategy, governance, organisation, key business processes |
| **Data Architecture** | the structure of logical and physical data assets and the data management resources |
| **Application Architecture** | a blueprint of the individual applications, how they interact, and how they relate to core business processes |
| **Technology Architecture** | the digital architecture plus the logical hardware and software infrastructure capabilities, and the standards, that business, data and application services need in order to be deployed |

The Technology domain is explicitly broad: the standard's own list runs from digital services,
IoT and social media infrastructure through cloud, general IT infrastructure and middleware to
networks, communications, processing and standards (INTRO §3.3).

Other "domains" are built by combining views drawn from these four. The standard's own examples
are Information Architecture, Risk and Security Architectures, and Digital Architecture
(INTRO §3.3). The definition of *architecture domain* says the same thing from the other side:
four primary domains, with others such as motivation, security and governance spanning them
(INTRO §4.12).

> **Trap.** "Security" is not a fifth domain. Neither is "Information". They are cross-cutting
> combinations of views over Business, Data, Application and Technology (INTRO §3.3).

## How the domains map onto the ADM

Phase B develops the Business Architecture, Phase C the Information Systems Architectures, and
Phase D the Technology Architecture, each in support of the agreed Architecture Vision
(INTRO §3.4). Phase C is one phase covering *two* domains, Data and Application, which is why the
standard writes "Information Systems Architectures" in the plural.

## Scoping by domain

A complete enterprise architecture description should cover all four domains, but time, money and
people usually do not stretch to a top-down description of everything, even when the enterprise
scope has already been narrowed (ADM §1.5.4). Every description is built for a purpose, a
particular set of business drivers, and clarifying that purpose is part of the first phase of the
ADM. If the purpose is, say, to compare technology options for a capability whose business
processes are fixed, a full Business Architecture may not be justified; but because Data,
Application and Technology all build on the business layer, it still has to be thought through
and understood (ADM §1.5.4).

Leaving domains out has a cost the architect must own: such an architecture is by definition not a
complete enterprise architecture, it risks inconsistency and therefore integration problems, and
either integration comes later with its own costs or the trade-offs are spelled out to management
(ADM §1.5.4). Whatever domains are in scope, they should be worked to a consistent, equal depth;
too little detail makes the architecture useless, too much exhausts the budget and clutters the
result (ADM §1.5.2).

## Architecture abstraction: four levels across all domains

Abstraction is a technique for making simplified views of a system so that stakeholders can
discuss, communicate and decide about some aspect of it. Levels are layered, moving from high-level
to detailed models (INTRO §3.7). Four abstraction levels cut across all four domains, each
answering a question (INTRO §3.7):

| Level | Question | Focus |
|---|---|---|
| **Contextual** | Why? | the environment, the motivation (goals, drivers, objectives), the scope of the work |
| **Conceptual** | What? | decomposing requirements to understand the problem, modelled as business, application and technology *services* (also called service or behaviour abstraction) |
| **Logical** | How? | the kinds of business, data, application and technology components needed, implementation-independent; several groupings give alternative logical solutions |
| **Physical** | With what? | allocating and implementing physical components to realise the logical ones; alternative physical solutions |

The standard adds a footnote worth remembering: its *why, what, how* have no connection to the
Zachman Framework's use of the same words (INTRO §3.7).

> **Trap.** Three different "levels" show up in this unit. *Domains* (B, D, A, T) are what is
> described; *abstraction levels* (contextual, conceptual, logical, physical) are how detailed the
> description is; *Architecture Landscape levels* (strategic, segment, capability, in lesson 13)
> are how wide the scope is. A question that offers "Strategic, Segment, Capability" as the four
> domains is mixing the first and third.

## Check yourself

- Which domain holds cloud services and IoT infrastructure?
- Which ADM phase covers two domains, and which two?
- Which abstraction level is also called service abstraction?
- Can an architecture that omits the Data domain be called a complete enterprise architecture?
