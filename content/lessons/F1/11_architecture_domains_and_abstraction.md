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

<figure class="my-4">
<svg viewBox="0 0 760 250" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="The four domains map to Phases B, C and D, Phase C spanning Data and Application; Information, Security and Digital Architectures cut across all four">
  <defs><marker id="arr-f1-11a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
  <rect x="20" y="15" width="160" height="44" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
  <text x="100" y="33.85" text-anchor="middle" font-size="11" font-weight="bold">Business</text>
  <text x="100" y="47.85" text-anchor="middle" font-size="11" fill="#345">Architecture</text>
  <rect x="200" y="15" width="160" height="44" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/>
  <text x="280" y="33.85" text-anchor="middle" font-size="11" font-weight="bold">Data</text>
  <text x="280" y="47.85" text-anchor="middle" font-size="11" fill="#345">Architecture</text>
  <rect x="380" y="15" width="160" height="44" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/>
  <text x="460" y="33.85" text-anchor="middle" font-size="11" font-weight="bold">Application</text>
  <text x="460" y="47.85" text-anchor="middle" font-size="11" fill="#345">Architecture</text>
  <rect x="560" y="15" width="160" height="44" rx="6" fill="#fff1d6" stroke="#e0b060"/>
  <text x="640" y="33.85" text-anchor="middle" font-size="11" font-weight="bold">Technology</text>
  <text x="640" y="47.85" text-anchor="middle" font-size="11" fill="#345">Architecture</text>
  <rect x="20" y="90" width="160" height="36" rx="6" fill="#fff" stroke="#666"/>
  <text x="100" y="111.85" text-anchor="middle" font-size="11" font-weight="bold">Phase B</text>
  <rect x="200" y="90" width="340" height="36" rx="6" fill="#fff" stroke="#666"/>
  <text x="370" y="111.85" text-anchor="middle" font-size="11" font-weight="bold">Phase C: Information Systems Architectures (plural)</text>
  <rect x="560" y="90" width="160" height="36" rx="6" fill="#fff" stroke="#666"/>
  <text x="640" y="111.85" text-anchor="middle" font-size="11" font-weight="bold">Phase D</text>
  <line x1="100" y1="60" x2="100" y2="88" stroke="#555" marker-end="url(#arr-f1-11a)"/>
  <line x1="280" y1="60" x2="280" y2="88" stroke="#555" marker-end="url(#arr-f1-11a)"/>
  <line x1="460" y1="60" x2="460" y2="88" stroke="#555" marker-end="url(#arr-f1-11a)"/>
  <line x1="640" y1="60" x2="640" y2="88" stroke="#555" marker-end="url(#arr-f1-11a)"/>
  <rect x="20" y="150" width="700" height="22" rx="6" fill="#f4f4f4" stroke="#bbb" stroke-dasharray="5 4"/>
  <text x="370" y="164.85" text-anchor="middle" font-size="11" fill="#345">Information Architecture: built by combining views drawn from the four, not a domain of its own</text>
  <rect x="20" y="176" width="700" height="22" rx="6" fill="#f4f4f4" stroke="#bbb" stroke-dasharray="5 4"/>
  <text x="370" y="190.85" text-anchor="middle" font-size="11" fill="#345">Risk and Security Architectures: built by combining views drawn from the four, not a domain of its own</text>
  <rect x="20" y="202" width="700" height="22" rx="6" fill="#f4f4f4" stroke="#bbb" stroke-dasharray="5 4"/>
  <text x="370" y="216.85" text-anchor="middle" font-size="11" fill="#345">Digital Architecture: built by combining views drawn from the four, not a domain of its own</text>
  <text x="370" y="240" text-anchor="middle" font-size="11" fill="#666">the four primary domains are what is described; the dashed rows are cross-cutting combinations of views over them</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">Domains, the phases that develop them, and the cross-cutting combinations. Original drawing; the terms follow INTRO §3.3 and INTRO §3.4.</figcaption>
</figure>

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

<figure class="my-4">
<svg viewBox="0 0 760 250" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="A grid of four abstraction levels, contextual to physical, each cutting across the four domains">
  <defs><marker id="arr-f1-11b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
  <text x="375" y="22" text-anchor="middle" font-size="11" font-weight="bold">Business</text>
  <text x="480" y="22" text-anchor="middle" font-size="11" font-weight="bold">Data</text>
  <text x="585" y="22" text-anchor="middle" font-size="11" font-weight="bold">Application</text>
  <text x="690" y="22" text-anchor="middle" font-size="11" font-weight="bold">Technology</text>
  <rect x="10" y="35" width="730" height="40" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
  <text x="20" y="52" text-anchor="start" font-size="12" font-weight="bold">Contextual</text>
  <text x="20" y="67" text-anchor="start" font-size="11" fill="#345">Why?  environment, motivation, scope</text>
  <rect x="330" y="41" width="90" height="28" rx="4" fill="#fff" fill-opacity="0.6" stroke="#7aa2e3"/>
  <rect x="435" y="41" width="90" height="28" rx="4" fill="#fff" fill-opacity="0.6" stroke="#7aa2e3"/>
  <rect x="540" y="41" width="90" height="28" rx="4" fill="#fff" fill-opacity="0.6" stroke="#7aa2e3"/>
  <rect x="645" y="41" width="90" height="28" rx="4" fill="#fff" fill-opacity="0.6" stroke="#7aa2e3"/>
  <rect x="10" y="81" width="730" height="40" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/>
  <text x="20" y="98" text-anchor="start" font-size="12" font-weight="bold">Conceptual</text>
  <text x="20" y="113" text-anchor="start" font-size="11" fill="#345">What?  the problem as services (service abstraction)</text>
  <rect x="330" y="87" width="90" height="28" rx="4" fill="#fff" fill-opacity="0.6" stroke="#7fbf7a"/>
  <rect x="435" y="87" width="90" height="28" rx="4" fill="#fff" fill-opacity="0.6" stroke="#7fbf7a"/>
  <rect x="540" y="87" width="90" height="28" rx="4" fill="#fff" fill-opacity="0.6" stroke="#7fbf7a"/>
  <rect x="645" y="87" width="90" height="28" rx="4" fill="#fff" fill-opacity="0.6" stroke="#7fbf7a"/>
  <rect x="10" y="127" width="730" height="40" rx="6" fill="#fff1d6" stroke="#e0b060"/>
  <text x="20" y="144" text-anchor="start" font-size="12" font-weight="bold">Logical</text>
  <text x="20" y="159" text-anchor="start" font-size="11" fill="#345">How?  kinds of components, implementation-independent</text>
  <rect x="330" y="133" width="90" height="28" rx="4" fill="#fff" fill-opacity="0.6" stroke="#e0b060"/>
  <rect x="435" y="133" width="90" height="28" rx="4" fill="#fff" fill-opacity="0.6" stroke="#e0b060"/>
  <rect x="540" y="133" width="90" height="28" rx="4" fill="#fff" fill-opacity="0.6" stroke="#e0b060"/>
  <rect x="645" y="133" width="90" height="28" rx="4" fill="#fff" fill-opacity="0.6" stroke="#e0b060"/>
  <rect x="10" y="173" width="730" height="40" rx="6" fill="#f3e3f7" stroke="#b58ac9"/>
  <text x="20" y="190" text-anchor="start" font-size="12" font-weight="bold">Physical</text>
  <text x="20" y="205" text-anchor="start" font-size="11" fill="#345">With what?  physical components realising the logical</text>
  <rect x="330" y="179" width="90" height="28" rx="4" fill="#fff" fill-opacity="0.6" stroke="#b58ac9"/>
  <rect x="435" y="179" width="90" height="28" rx="4" fill="#fff" fill-opacity="0.6" stroke="#b58ac9"/>
  <rect x="540" y="179" width="90" height="28" rx="4" fill="#fff" fill-opacity="0.6" stroke="#b58ac9"/>
  <rect x="645" y="179" width="90" height="28" rx="4" fill="#fff" fill-opacity="0.6" stroke="#b58ac9"/>
  <line x1="752" y1="40" x2="752" y2="215" stroke="#555" marker-end="url(#arr-f1-11b)"/>
  <text x="370" y="240" text-anchor="middle" font-size="11" fill="#666">top to bottom runs from high-level to detailed; each level cuts across Business, Data, Application and Technology</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">Four abstraction levels across all four domains. Original drawing; the levels and their questions follow INTRO §3.7.</figcaption>
</figure>

The standard adds a footnote worth remembering: its *why, what, how* have no connection to the
Zachman Framework's use of the same words (INTRO §3.7).

> **Trap.** Three different "levels" show up in this unit. *Domains* (B, D, A, T) are what is
> described; *abstraction levels* (contextual, conceptual, logical, physical) are how detailed the
> description is; *Architecture Landscape levels* (strategic, segment, capability, in lesson 13)
> are how wide the scope is. A question that offers "Strategic, Segment, Capability" as the four
> domains is mixing the first and third.

<!-- figures:start -->
## Figures from the standard

The diagrams the cited sections carry, from your local copy of the publication. The exam reproduces these; know what each box is.

<div class="grid gap-4 md:grid-cols-2">
<figure class="max-w-lg"><img src="/figure/INTRO:fig-3-1" alt="Figure 3-1: Architecture Development Cycle" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 3-1: Architecture Development Cycle (INTRO)</figcaption></figure>
</div>
<!-- figures:end -->

## Check yourself

- Which domain holds cloud services and IoT infrastructure?
- Which ADM phase covers two domains, and which two?
- Which abstraction level is also called service abstraction?
- Can an architecture that omits the Data domain be called a complete enterprise architecture?
