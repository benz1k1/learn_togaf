---
title: Architecture Principles — what one is, what it contains, what makes a set good
unit: F5
objectives: ["5.1"]
refs: ["TECH §2.1", "TECH §2.2", "TECH §2.3", "TECH §2.4", "TECH §2.4.1", "TECH §2.5", "ADM §3.3.7"]
reading_minutes: 9
source: authored
status: draft
---
## What a principle is

A principle is a general rule or guideline that is meant to last and to be changed rarely; it
shapes how the organisation goes about its mission. Principles sit inside a wider ladder of
guiding ideas that runs from values down to actions and results (TECH §2.1).

Two domains of principle matter to architecture work. **Enterprise principles** guide decisions
across the whole enterprise and are a key part of an Architecture Governance strategy; they often
have subsidiary sets for units such as IT or HR. **Architecture Principles** are the subset that
governs the architecture process itself — how the Enterprise Architecture is developed,
maintained and used. Sets form a hierarchy: architecture principles are informed and constrained
by enterprise principles, and segment principles elaborate on enterprise ones (TECH §2.1).

Architecture Principles express the underlying rules for using and deploying all IT resources and
assets, reflect consensus across the enterprise, and are the basis for future IT decisions. Each
one should trace clearly back to business objectives and key architecture drivers (TECH §2.2).

## The four-part template

| Part | What it must do | Watch for |
|---|---|---|
| **Name** | Capture the essence of the rule and be easy to remember | No technology platform names; avoid fuzzy words such as "support", "open", "consider", "avoid", and be careful with "manage" |
| **Statement** | State the fundamental rule succinctly and without ambiguity | Statements for managing information tend to look alike from one organisation to the next — that is expected |
| **Rationale** | Explain the business benefit of following the rule, in business terms; describe the relationship to other principles and when one outweighs another | Written in business language, not technical language |
| **Implications** | Spell out what the business and IT must do — resources, costs, tasks — and the consequences of adopting the principle; the reader should see "how does this affect me?" | Do not trivialise, oversimplify or pass judgement on the impact; some implications will be speculative |

(TECH §2.3)

<figure class="my-4">
<svg viewBox="0 0 760 232" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="A principle in four parts: name and statement give the rule; rationale and implications give the reason and the cost">
<defs><marker id="arr-f5-10a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
<rect x="40" y="18" width="150" height="38" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="115.0" y="41.2" text-anchor="middle" font-size="12" font-weight="bold">Name</text>
<text x="205" y="42" text-anchor="start" font-size="11" fill="#333">the essence of the rule, easy to remember — no platform names, no fuzzy verbs</text>
<line x1="115" y1="56" x2="115" y2="68" stroke="#555" marker-end="url(#arr-f5-10a)"/>
<rect x="40" y="68" width="150" height="38" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="115.0" y="91.2" text-anchor="middle" font-size="12" font-weight="bold">Statement</text>
<text x="205" y="92" text-anchor="start" font-size="11" fill="#333">the fundamental rule itself, succinct and unambiguous</text>
<line x1="115" y1="106" x2="115" y2="118" stroke="#555" marker-end="url(#arr-f5-10a)"/>
<rect x="40" y="118" width="150" height="38" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/>
<text x="115.0" y="141.2" text-anchor="middle" font-size="12" font-weight="bold">Rationale</text>
<text x="205" y="142" text-anchor="start" font-size="11" fill="#333">the business benefit, in business language; how it relates to other principles</text>
<line x1="115" y1="156" x2="115" y2="168" stroke="#555" marker-end="url(#arr-f5-10a)"/>
<rect x="40" y="168" width="150" height="38" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/>
<text x="115.0" y="191.2" text-anchor="middle" font-size="12" font-weight="bold">Implications</text>
<text x="205" y="192" text-anchor="start" font-size="11" fill="#333">what business and IT must do — resources, costs, tasks — “how does this affect me?”</text>
<path d="M28 20 L20 20 L20 106 L28 106" fill="none" stroke="#7aa2e3"/>
<text x="12" y="66" text-anchor="middle" font-size="10" fill="#345" transform="rotate(-90 12 66)">the rule</text>
<path d="M28 120 L20 120 L20 206 L28 206" fill="none" stroke="#7fbf7a"/>
<text x="12" y="166" text-anchor="middle" font-size="10" fill="#345" transform="rotate(-90 12 166)">why, and the cost</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">The anatomy of one principle: two parts state the rule, two parts justify it. Original drawing; parts per TECH §2.3.</figcaption>
</figure>

> **Trap.** The standard's template has exactly four parts: name, statement, rationale,
> implications. Options that add "owner", "priority", "measure" or "review date" are describing
> something else. "Goal / objective / measure" is a business-scenario or requirements structure;
> "problem / context / forces / solution" is the shape of an architecture pattern (TECH §2.3).

## Who writes them, and what shapes them

Architecture Principles are typically developed by the Enterprise Architects together with the key
stakeholders and are **approved by the Architecture Board**. They must be traceable and clearly
articulated so that they guide decisions, and they are chosen to keep the Target Architecture and
its implementation aligned to business strategy (TECH §2.4).

Five influences typically shape their development: the enterprise mission and plans; enterprise
strategic initiatives (strengths, weaknesses, opportunities, threats, current initiatives);
external constraints (market factors, legislation); current systems and technology; and emerging
industry trends (TECH §2.4).

<figure class="my-4">
<svg viewBox="0 0 760 212" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="Five influences feed the drafting of Architecture Principles, which the Architecture Board approves">
<defs><marker id="arr-f5-10b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
<rect x="15" y="12" width="200" height="28" rx="6" fill="#fff" stroke="#666"/>
<text x="115.0" y="29.9" text-anchor="middle" font-size="11">enterprise mission and plans</text>
<path d="M215 26 L300 26 L318 102" fill="none" stroke="#555" marker-end="url(#arr-f5-10b)"/>
<rect x="15" y="48" width="200" height="28" rx="6" fill="#fff" stroke="#666"/>
<text x="115.0" y="65.8" text-anchor="middle" font-size="11">strategic initiatives (SWOT)</text>
<path d="M215 62 L300 62 L318 102" fill="none" stroke="#555" marker-end="url(#arr-f5-10b)"/>
<rect x="15" y="84" width="200" height="28" rx="6" fill="#fff" stroke="#666"/>
<text x="115.0" y="101.8" text-anchor="middle" font-size="11">external constraints (market, law)</text>
<path d="M215 98 L300 98 L318 102" fill="none" stroke="#555" marker-end="url(#arr-f5-10b)"/>
<rect x="15" y="120" width="200" height="28" rx="6" fill="#fff" stroke="#666"/>
<text x="115.0" y="137.8" text-anchor="middle" font-size="11">current systems and technology</text>
<path d="M215 134 L300 134 L318 102" fill="none" stroke="#555" marker-end="url(#arr-f5-10b)"/>
<rect x="15" y="156" width="200" height="28" rx="6" fill="#fff" stroke="#666"/>
<text x="115.0" y="173.8" text-anchor="middle" font-size="11">emerging industry trends</text>
<path d="M215 170 L300 170 L318 102" fill="none" stroke="#555" marker-end="url(#arr-f5-10b)"/>
<rect x="320" y="66" width="200" height="72" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="420.0" y="91.8" text-anchor="middle" font-size="11" font-weight="bold">Architecture Principles</text>
<text x="420.0" y="105.8" text-anchor="middle" font-size="11">drafted by the Enterprise Architects</text>
<text x="420.0" y="119.8" text-anchor="middle" font-size="11">with the key stakeholders</text>
<line x1="520" y1="102" x2="555" y2="102" stroke="#555" marker-end="url(#arr-f5-10b)"/>
<rect x="557" y="66" width="188" height="72" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/>
<text x="651.0" y="98.8" text-anchor="middle" font-size="11" font-weight="bold">Architecture Board</text>
<text x="651.0" y="112.8" text-anchor="middle" font-size="11">approves the set</text>
<text x="117" y="202" text-anchor="middle" font-size="10" fill="#666">five influences (TECH §2.4)</text>
<text x="532" y="160" text-anchor="middle" font-size="10" fill="#666">traceable to business objectives and drivers;</text>
<text x="532" y="174" text-anchor="middle" font-size="10" fill="#666">keeps the Target Architecture aligned to strategy</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">What shapes the principles and who approves them. Original drawing; influences and approval per TECH §2.4.</figcaption>
</figure>

## The five qualities of a good set

A written statement labelled "principle" is not automatically a good one. A good set is grounded in
the organisation's beliefs and values, expressed in language the business uses, few in number,
future-oriented, and championed by senior management; principles drive behaviour. A poor set falls
into disuse and makes the resulting architectures and standards look arbitrary (TECH §2.4.1).

| Quality | Meaning in one line |
|---|---|
| **Understandable** | Quickly grasped by people across the organisation; intent is unambiguous so violations are minimised |
| **Robust** | Precise enough to support consistent decisions in complex, controversial situations, and to create enforceable policies and standards |
| **Complete** | Every potentially important principle for managing information and technology is defined; the set covers every situation perceived |
| **Consistent** | Strict adherence to one may need a looser reading of another; the set must not be contradictory to the point that following one violates the spirit of another |
| **Stable** | Enduring, yet with an amendment process for adding, removing or altering principles after ratification |

(TECH §2.4.1)

> **Trap.** The five are *understandable, robust, complete, consistent, stable*. "Measurable",
> "achievable" and "time-bound" belong to SMART objectives, not to principles (TECH §2.4.1).

## How principles are used

Principles capture the fundamental truths about how the enterprise will use IT resources. They are
used to give a framework for conscious architecture decisions; to establish evaluation criteria
that steer product and solution selection during compliance work; to drive functional
requirements; to assess existing implementations and the portfolio for compliance; and — through
their rationale and implications — to guide difficult decisions and feed transition planning. In
governance they act as a "back-stop" for compliance assessments where interpretation is allowed,
and support the decision to raise a dispensation request (TECH §2.5).

Principles are applied as a set and will sometimes compete: accessibility and security pull in
opposite directions, so each is read "all other things being equal", and when one is given
precedence the rationale for that decision is documented. A principle that looks obvious is still
worth writing down, because obvious guidance is not always followed. No penalties are prescribed,
but violations tend to cause operational problems (TECH §2.5).

## Where they sit in the ADM

Principles are established as part of setting up the Architecture Capability and are then
confirmed and elaborated — including the business principles — as a step of Phase A, so that the
Architecture Vision is developed against an agreed set (ADM §3.3.7).

## Check yourself

- Which of the four parts is written in business terminology and explains the benefit?
- Which quality says the set must cover every situation perceived?
- Who approves Architecture Principles?
