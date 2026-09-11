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
