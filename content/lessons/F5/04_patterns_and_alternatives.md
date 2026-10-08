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

<figure class="my-4">
<svg viewBox="0 0 760 174" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="The content of a pattern read as a flow: context, problem and forces, solution, resulting context, with the supporting elements beneath">
<defs><marker id="arr-f5-12a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
<rect x="15" y="10" width="730" height="24" rx="6" fill="#f1f1f1" stroke="#999"/>
<text x="380.0" y="25.9" text-anchor="middle" font-size="11">Name — and often an abstract: which problems, for whom</text>
<rect x="15" y="48" width="160" height="58" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="95.0" y="66.8" text-anchor="middle" font-size="11" font-weight="bold">Context</text>
<text x="95.0" y="80.8" text-anchor="middle" font-size="11">pre-conditions;</text>
<text x="95.0" y="94.8" text-anchor="middle" font-size="11">the initial state</text>
<line x1="175" y1="77" x2="205" y2="77" stroke="#555" marker-end="url(#arr-f5-12a)"/>
<rect x="205" y="48" width="160" height="58" rx="6" fill="#fff1d6" stroke="#e0b060"/>
<text x="285.0" y="66.8" text-anchor="middle" font-size="11" font-weight="bold">Problem + Forces</text>
<text x="285.0" y="80.8" text-anchor="middle" font-size="11">the intent, and the</text>
<text x="285.0" y="94.8" text-anchor="middle" font-size="11">qualities in tension</text>
<line x1="365" y1="77" x2="395" y2="77" stroke="#555" marker-end="url(#arr-f5-12a)"/>
<rect x="395" y="48" width="160" height="58" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/>
<text x="475.0" y="66.8" text-anchor="middle" font-size="11" font-weight="bold">Solution</text>
<text x="475.0" y="80.8" text-anchor="middle" font-size="11">static structure and</text>
<text x="475.0" y="94.8" text-anchor="middle" font-size="11">dynamic behaviour</text>
<line x1="555" y1="77" x2="585" y2="77" stroke="#555" marker-end="url(#arr-f5-12a)"/>
<rect x="585" y="48" width="160" height="58" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="665.0" y="66.8" text-anchor="middle" font-size="11" font-weight="bold">Resulting context</text>
<text x="665.0" y="80.8" text-anchor="middle" font-size="11">post-conditions; forces</text>
<text x="665.0" y="94.8" text-anchor="middle" font-size="11">resolved and remaining</text>
<rect x="15" y="132" width="730" height="30" rx="6" fill="#fff" stroke="#666"/>
<text x="380.0" y="150.8" text-anchor="middle" font-size="11">supporting elements: Examples · Rationale (why it works) · Related patterns · Known uses</text>
<line x1="665" y1="106" x2="665" y2="130" stroke="#999" stroke-dasharray="4 3" marker-end="url(#arr-f5-12a)"/>
<text x="600" y="122" text-anchor="end" font-size="10" fill="#666">→ other patterns now applicable</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">A pattern's elements read as a story from pre-conditions to post-conditions. Original drawing; elements per TECH §4.1.2.</figcaption>
</figure>

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

<figure class="my-4">
<svg viewBox="0 0 760 190" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="Alternatives are defined per domain and merged, scored against criteria chosen first, then one is chosen or features are combined">
<defs><marker id="arr-f5-12b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
<rect x="15" y="50" width="160" height="28" rx="6" fill="#fff" stroke="#666"/>
<text x="95.0" y="67.8" text-anchor="middle" font-size="11">Business alternatives</text>
<path d="M175 64 L215 64 L240 137" fill="none" stroke="#555" marker-end="url(#arr-f5-12b)"/>
<rect x="15" y="88" width="160" height="28" rx="6" fill="#fff" stroke="#666"/>
<text x="95.0" y="105.8" text-anchor="middle" font-size="11">Data alternatives</text>
<path d="M175 102 L215 102 L240 137" fill="none" stroke="#555" marker-end="url(#arr-f5-12b)"/>
<rect x="15" y="126" width="160" height="28" rx="6" fill="#fff" stroke="#666"/>
<text x="95.0" y="143.8" text-anchor="middle" font-size="11">Application alternatives</text>
<path d="M175 140 L215 140 L240 137" fill="none" stroke="#555" marker-end="url(#arr-f5-12b)"/>
<rect x="15" y="164" width="160" height="28" rx="6" fill="#fff" stroke="#666"/>
<text x="95.0" y="181.8" text-anchor="middle" font-size="11">Technology alternatives</text>
<path d="M175 178 L215 178 L240 137" fill="none" stroke="#555" marker-end="url(#arr-f5-12b)"/>
<text x="95" y="38" text-anchor="middle" font-size="10" fill="#666">defined per domain, then merged</text>
<rect x="242" y="100" width="165" height="72" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="324.5" y="125.8" text-anchor="middle" font-size="11" font-weight="bold">2 Identify alternatives</text>
<text x="324.5" y="139.8" text-anchor="middle" font-size="11">whole-architecture</text>
<text x="324.5" y="153.8" text-anchor="middle" font-size="11">candidates; gaps and impacts</text>
<rect x="242" y="12" width="165" height="52" rx="6" fill="#fff1d6" stroke="#e0b060"/>
<text x="324.5" y="28.5" text-anchor="middle" font-size="10" font-weight="bold">1 Select criteria</text>
<text x="324.5" y="41.5" text-anchor="middle" font-size="10">from principles, requirements,</text>
<text x="324.5" y="54.5" text-anchor="middle" font-size="10">vision, concerns</text>
<line x1="324" y1="64" x2="324" y2="98" stroke="#555" marker-end="url(#arr-f5-12b)"/>
<line x1="407" y1="136" x2="440" y2="136" stroke="#555" marker-end="url(#arr-f5-12b)"/>
<rect x="442" y="100" width="150" height="72" rx="6" fill="#fff" stroke="#666"/>
<text x="517.0" y="125.8" text-anchor="middle" font-size="11" font-weight="bold">Compare</text>
<text x="517.0" y="139.8" text-anchor="middle" font-size="11">strengths and weaknesses</text>
<text x="517.0" y="153.8" text-anchor="middle" font-size="11">against the criteria</text>
<line x1="592" y1="136" x2="620" y2="136" stroke="#555" marker-end="url(#arr-f5-12b)"/>
<rect x="622" y="100" width="123" height="72" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/>
<text x="683.5" y="126.5" text-anchor="middle" font-size="10" font-weight="bold">3 Choose</text>
<text x="683.5" y="139.5" text-anchor="middle" font-size="10">or combine; stakeholder</text>
<text x="683.5" y="152.5" text-anchor="middle" font-size="10">review decides and funds</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">Criteria first, then per-domain alternatives merged and compared, then a choice. Original drawing; method per TECH §9.2.</figcaption>
</figure>

> **Trap.** The trade-off technique is used in Phase E to investigate different Target
> Architecture alternatives with stakeholders when consolidating gaps, but the standard says the
> method "can be used for any phase at any level" (TECH §9.2).

<!-- figures:start -->
## Figures from the standard

The diagrams the cited sections carry, from your local copy of the publication. The exam reproduces these; know what each box is.

<div class="grid gap-4 md:grid-cols-2">
<figure class="max-w-lg"><img src="/figure/TECH:fig-9-1" alt="Figure 9-1: Architecture Trade-Off Method" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 9-1: Architecture Trade-Off Method (TECH)</figcaption></figure>
</div>
<!-- figures:end -->

## Check yourself

- Which pattern element records which forces remain unresolved?
- In which phases does the standard say re-usable assets such as patterns should be considered?
- Why are alternatives usually defined per domain first?
