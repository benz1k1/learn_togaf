---
title: The Practitioners' Approach — architecture for a purpose, ahead of the decision
unit: G_PRACTITIONERS
objectives: ["G2.1"]
refs: ["GUIDE:adm-practitioners §3.1", "GUIDE:adm-practitioners §3.2.1", "GUIDE:adm-practitioners §3.2.2", "GUIDE:adm-practitioners §3.3", "GUIDE:adm-practitioners §3.3.1", "GUIDE:adm-practitioners §3.3.2", "GUIDE:adm-practitioners §4.1", "GUIDE:adm-practitioners §5.1", "GUIDE:adm-practitioners §5.1.4", "GUIDE:adm-practitioners §6.1.2", "GUIDE:adm-practitioners §6.3", "GUIDE:adm-practitioners §7.2", "GUIDE:adm-practitioners §11.2", "GUIDE:adm-practitioners §11.3"]
reading_minutes: 10
source: authored
status: draft
---
## What the guide is and when it applies

The Practitioners' Approach is the standard's practical companion for the architect who has to
*develop* an architecture with the ADM — as opposed to the Leader who establishes the capability.
Its premise is that an EA exists for one reason, to guide effective change, and that
understanding "comes from purpose": the same concepts serve big and little questions; what
differs is what the documented architecture looks like (GUIDE:adm-practitioners §3.1).

It applies in any scenario where an architecture project is under way and the question is how
much to do, for whom, and by when: an architect asked to "model everything", a roadmap needed
for budget season, a stakeholder who cannot approve because the view does not speak to their
concern, an organisation that has already picked the solution. The guide's walk-throughs cover
architecture to support strategy, portfolio, project and solution delivery
(GUIDE:adm-practitioners §3.2.2; GUIDE:adm-practitioners §7.2).

## The EA Landscape and superior architecture

The EA Landscape is the complete set of architecture descriptions the enterprise holds; every
Architecture Project populates just enough of it to serve the need at hand, in the context of
prior architecture that guides or constrains the work. Four characteristics frame it — breadth,
level of detail, time (the planning horizon) and recency — and the rule is to develop to the
least detail required, because "the more detail required, the longer the time to market". A
Request for Architecture Work bounds the project within the landscape; work outside that scope
"is not within the scope of this architecture initiative". Where a broader architecture exists,
it is the *superior architecture* and the current work is subject to it
(GUIDE:adm-practitioners §3.2.1).

<figure class="my-4">
<svg viewBox="0 0 760 300" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="10" role="img" aria-label="Three communities the practitioner communicates with: stakeholders get views that address concerns and hold approval rights; implementers get context, gaps, specifications and controls through an Architecture Contract; decision-makers get other useful things about timing, trade-off, status, budget, compliance and confidence">
<defs><marker id="arr-g2-01a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
<text x="380" y="18" text-anchor="middle" font-size="12" font-weight="bold">Three communities, three kinds of communication</text>
<rect x="290" y="36" width="180" height="50" rx="6" fill="#f1f1f1" stroke="#999"/>
<text x="380" y="56" text-anchor="middle" font-weight="bold">The architecture</text>
<text x="380" y="72" text-anchor="middle" font-size="9">models in the EA Landscape (poor communication tools)</text>
<line x1="330" y1="86" x2="130" y2="118" stroke="#555" marker-end="url(#arr-g2-01a)"/>
<line x1="380" y1="86" x2="380" y2="118" stroke="#555" marker-end="url(#arr-g2-01a)"/>
<line x1="430" y1="86" x2="630" y2="118" stroke="#555" marker-end="url(#arr-g2-01a)"/>
<rect x="10" y="120" width="240" height="110" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/>
<text x="130" y="140" text-anchor="middle" font-weight="bold">Stakeholders</text>
<text x="130" y="156" text-anchor="middle" font-size="9">approval rights over the target,</text>
<text x="130" y="168" text-anchor="middle" font-size="9">decision rights on the implementation's suitability</text>
<text x="130" y="188" text-anchor="middle" font-size="9">get: views that address a concern</text>
<text x="130" y="200" text-anchor="middle" font-size="9">(six to nine concern topics from strategy)</text>
<text x="130" y="216" text-anchor="middle" font-size="9">they approve views, not architecture descriptions</text>
<rect x="260" y="120" width="240" height="110" rx="6" fill="#fff1d6" stroke="#e0b060"/>
<text x="380" y="140" text-anchor="middle" font-weight="bold">Implementers</text>
<text x="380" y="156" text-anchor="middle" font-size="9">need guidance and constraint</text>
<text x="380" y="176" text-anchor="middle" font-size="9">get, via the Architecture Contract: project context,</text>
<text x="380" y="188" text-anchor="middle" font-size="9">scope (work packages and gaps, and gaps not theirs),</text>
<text x="380" y="200" text-anchor="middle" font-size="9">conformance (specifications and controls)</text>
<text x="380" y="216" text-anchor="middle" font-size="9">specifications are exclusionary; a reasonable-interpretation test</text>
<rect x="510" y="120" width="240" height="110" rx="6" fill="#e3f0fb" stroke="#4a7fb5"/>
<text x="630" y="140" text-anchor="middle" font-weight="bold">Decision-makers</text>
<text x="630" y="156" text-anchor="middle" font-size="9">execution rights on change</text>
<text x="630" y="176" text-anchor="middle" font-size="9">get "other useful things": timing, trade-off decisions,</text>
<text x="630" y="188" text-anchor="middle" font-size="9">status, budget, compliance, confidence</text>
<text x="630" y="208" text-anchor="middle" font-size="9">often overlap with stakeholders, but the</text>
<text x="630" y="220" text-anchor="middle" font-size="9">stakeholder/concern/view construct is kept for approval</text>
<rect x="10" y="246" width="740" height="46" rx="6" fill="#fff" stroke="#666"/>
<text x="380" y="266" text-anchor="middle" font-weight="bold">An effectively communicated architecture is one that provides confidence</text>
<text x="380" y="282" text-anchor="middle" font-size="9">the informal communication outside models, views and roadmaps is often the most important the practitioner will do</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">Original drawing. The three communities and what each receives follow GUIDE:adm-practitioners §3.3, §3.3.1 and §3.3.2; the closing rule follows the chapter's conclusion.</figcaption>
</figure>

## Purpose, breadth, detail and time

Four purposes — support strategy (3–10 years, broad, guidance more than constraint), portfolio
(2–5 years, a single portfolio), project (under 2 years, detailed, constraint more than
guidance) and solution delivery (the most detailed, constraints only) — each produce different
contents in the landscape with a different mix of the four characteristics
(GUIDE:adm-practitioners §3.2.2). The purposes align to the budget cycle: strategy to budget
planning, portfolio to budget preparation (the roadmap must be ready when the budget materials
are being prepared), project to budget allocation (the business case or charter), solution
delivery to budget control in Phase G. "Architecture before the decision" is the operating
principle (GUIDE:adm-practitioners §4.1).

## Communicating with three communities

Stakeholders, implementers and decision-makers use the architecture differently. Pragmatically
a stakeholder holds approval rights over the target and decision rights over the implementation's
suitability; a concern consolidates requirements around a topic; a view demonstrates how the
architecture addresses the concern, not that the stakeholder should be happy
(GUIDE:adm-practitioners §3.3; GUIDE:adm-practitioners §3.3.1). Implementers are best served by
an Architecture Contract that states project context, scope (work packages and gaps, including
the gaps the project is *not* responsible for) and conformance (specifications and controls);
specifications should be exclusionary — what is prohibited — and assessed by a reasonable
interpretation test, each linked to a requirement (GUIDE:adm-practitioners §3.3.2).

## The repository, trade-off and the identical steps

A well-run repository ruthlessly minimises information: nothing is captured that the current
project or minimal traceability does not require, the three most powerful components are the
Architecture Requirements Specification, controls and gaps, and stakeholders "approve views, not
architecture descriptions" (GUIDE:adm-practitioners §5.1). Requirements look different per
purpose — "be agile" is a strategy requirement, a score of one to five on process maturity is a
portfolio requirement — and the practitioner is a guardian of value who assesses whether an
injected requirement conforms to the superior architecture (GUIDE:adm-practitioners §5.1.4).

Facilitating stakeholder trade-off is "often more valuable than finalizing an architecture
description", because stakeholders underperform when a trade-off crosses their span of control
(GUIDE:adm-practitioners §6.1.2). The steps of Phases B, C and D are identical because the
approach to developing, confirming and approving an architecture is identical; the detail,
precision and formality vary; treat the steps as a mandatory checklist (GUIDE:adm-practitioners §6.3).

## The failure patterns the exam plants

Missing the business cycle: waiting for an invitation or for clarity that only arrives at the end
of planning; architecture after the decision is late and may cause conflict
(GUIDE:adm-practitioners §11.2). Not doing architecture: being so busy as the stakeholder's
agent, SME and implementer that the architecture is never described and approved, leaving
"compliance by assertion" (GUIDE:adm-practitioners §11.3).

**Trap.** "Enterprise Architecture versus Solution Architecture" is, for this guide, a
distinction without a practical difference; and the guide is emphatic that the ADM diagram is a
stylised information flow, not a process sequence to be run linearly (GUIDE:adm-practitioners §4.1).

## How the 5-point answer differs from the 3-point one

| Points | What the answer does |
|---|---|
| 5 | Names the purpose and its place in the budget cycle, scopes breadth, detail and horizon to it, respects the superior architecture, produces views per concern for approval and a contract for implementers, facilitates the trade-off, and minimises what is gathered |
| 3 | Right purpose and deliverables, but produces them after the decision milestone, or gathers a comprehensive model first |
| 1 | Produces implementation designs and standards and calls them the architecture |
| 0 | Sells the architecture to stakeholders, or expects implementers to infer their gaps from diagrams |

## Where to look in the book

Practitioners' Approach §3.1 (why EA), §3.2.1 (EA Landscape, superior architecture), §3.2.2
(four purposes and Table 3-1), §3.3 with §3.3.1 and §3.3.2 (three communities, concern and
view, Architecture Contract), §4.1 (budget cycle), §5.1 and §5.1.4 (repository and
requirements), §6.1.2 (trade-off), §6.3 (identical steps), §7.2 (strategy walk-through context),
§11.2 and §11.3 (failure patterns).
