---
title: The Business Scenarios guide — six steps, three phases, SMART outcomes
unit: G_BUSINESS_SCENARIOS
objectives: ["G3.1"]
refs: ["GUIDE:business-scenarios §1", "GUIDE:business-scenarios §2", "GUIDE:business-scenarios §3.1", "GUIDE:business-scenarios §3.2.2", "GUIDE:business-scenarios §3.2.5", "GUIDE:business-scenarios §3.3", "GUIDE:business-scenarios §3.3.1", "GUIDE:business-scenarios §4", "GUIDE:business-scenarios §5", "GUIDE:business-scenarios §6", "GUIDE:business-scenarios §7.2.1", "GUIDE:business-scenarios §9.2", "GUIDE:business-scenarios §10", "GUIDE:business-scenarios §12.8", "GUIDE:business-scenarios §13", "ADM §3.3.8"]
reading_minutes: 9
source: authored
status: draft
---
## What the guide is for

Architecture without an understanding of *why* produces "a fine warehouse for mechanical parts"
when household goods were needed. The Business Scenario method validates, elaborates or changes
the premise behind an architecture effort by documenting the key elements in successive
iterations until the understanding is fit for deciding to move forward; each iteration plans,
gathers, analyses, documents and reviews. The method is used principally in the Preliminary,
Architecture Vision and Business Architecture phases, and in other phases where requirements
must be derived (GUIDE:business-scenarios §1).

A business scenario is a uniform description of real business problems; the business and
technology environment; the value streams enabled by capabilities; the desired outcomes; and
the human and computing actors who provide the capabilities. It is SMART — specific,
measurable, actionable, realistic, time-bound. It is not a use-case (too detailed, software
oriented), not a business model or business case (though it can inform one), not a sales
technique, and not an engineering specification (GUIDE:business-scenarios §1).

**When it applies in a scenario.** The tell is a problem statement that is really a solution
("we need a CRM"), stakeholders who disagree about the problem, requirements that "do not add
up to a whole problem", or a vendor-led programme where the customer cannot say what it needs.
The benefits the guide lists are exactly the gaps such a scenario shows: without a complete
description the requirements can misguide the work, the business value is unclear and the
relevance of solutions is unclear; involving line management early gains buy-in; and a scenario
gives vendors a language for linking customer problems and solutions (GUIDE:business-scenarios §2).

<figure class="my-4">
<svg viewBox="0 0 760 300" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="10" role="img" aria-label="Business scenario method: six steps across the top (problem, environment, outcomes, human actors, computer actors, fitness check) and three phases below (premise formulation, initial verification, refinement), each phase running plan, gather, analyse, document, review; the released scenario goes to the Requirements Repository">
<defs><marker id="arr-g3-01a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
<text x="380" y="18" text-anchor="middle" font-size="12" font-weight="bold">Six steps capture five elements; three phases repeat plan → gather → analyse → document → review</text>
<g>
<rect x="10" y="36" width="115" height="46" rx="5" fill="#e3f0fb" stroke="#4a7fb5"/><text x="67" y="54" text-anchor="middle" font-size="9">1 Identify, document,</text><text x="67" y="67" text-anchor="middle" font-size="9">rank the problem</text>
<rect x="135" y="36" width="115" height="46" rx="5" fill="#e3f0fb" stroke="#4a7fb5"/><text x="192" y="54" text-anchor="middle" font-size="9">2 Business and tech.</text><text x="192" y="67" text-anchor="middle" font-size="9">environment, in models</text>
<rect x="260" y="36" width="115" height="46" rx="5" fill="#e3f0fb" stroke="#4a7fb5"/><text x="317" y="54" text-anchor="middle" font-size="9">3 Desired outcomes,</text><text x="317" y="67" text-anchor="middle" font-size="9">made SMART</text>
<rect x="385" y="36" width="115" height="46" rx="5" fill="#e3f0fb" stroke="#4a7fb5"/><text x="442" y="54" text-anchor="middle" font-size="9">4 Human actors and</text><text x="442" y="67" text-anchor="middle" font-size="9">their place</text>
<rect x="510" y="36" width="115" height="46" rx="5" fill="#e3f0fb" stroke="#4a7fb5"/><text x="567" y="54" text-anchor="middle" font-size="9">5 Computer actors</text><text x="567" y="67" text-anchor="middle" font-size="9">and their place</text>
<rect x="635" y="36" width="115" height="46" rx="5" fill="#e3f0fb" stroke="#4a7fb5"/><text x="692" y="54" text-anchor="middle" font-size="9">6 Check fitness for</text><text x="692" y="67" text-anchor="middle" font-size="9">purpose; refine only if needed</text>
</g>
<g>
<rect x="10" y="110" width="235" height="90" rx="6" fill="#fff1d6" stroke="#e0b060"/>
<text x="127" y="130" text-anchor="middle" font-weight="bold">Premise formulation</text>
<text x="127" y="146" text-anchor="middle" font-size="9">"we need an ERP" presumes an answer</text>
<text x="127" y="159" text-anchor="middle" font-size="9">to an unstated question</text>
<text x="127" y="177" text-anchor="middle" font-size="9">out: premise, key questions, a list of</text>
<text x="127" y="190" text-anchor="middle" font-size="9">stakeholders willing to validate it</text>
<line x1="245" y1="155" x2="260" y2="155" stroke="#555" marker-end="url(#arr-g3-01a)"/>
<rect x="262" y="110" width="235" height="90" rx="6" fill="#fff1d6" stroke="#e0b060"/>
<text x="379" y="130" text-anchor="middle" font-weight="bold">Initial verification</text>
<text x="379" y="146" text-anchor="middle" font-size="9">face to face with real stakeholders,</text>
<text x="379" y="159" text-anchor="middle" font-size="9">from different organisations where possible</text>
<text x="379" y="177" text-anchor="middle" font-size="9">out: draft, incomplete scenario with</text>
<text x="379" y="190" text-anchor="middle" font-size="9">recommended next steps</text>
<line x1="497" y1="155" x2="512" y2="155" stroke="#555" marker-end="url(#arr-g3-01a)"/>
<rect x="514" y="110" width="236" height="90" rx="6" fill="#fff1d6" stroke="#e0b060"/>
<text x="632" y="130" text-anchor="middle" font-weight="bold">Refinement</text>
<text x="632" y="146" text-anchor="middle" font-size="9">iterate until there is agreement to proceed;</text>
<text x="632" y="159" text-anchor="middle" font-size="9">beware paralysis by analysis</text>
<text x="632" y="177" text-anchor="middle" font-size="9">out: released scenario with agreed path</text>
<text x="632" y="190" text-anchor="middle" font-size="9">forward and commitments to standards</text>
</g>
<line x1="632" y1="200" x2="632" y2="222" stroke="#555" marker-end="url(#arr-g3-01a)"/>
<rect x="10" y="224" width="740" height="66" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/>
<text x="380" y="244" text-anchor="middle" font-weight="bold">Approved by business leaders → placed in the Requirements Repository as the high-level requirements statement</text>
<text x="380" y="262" text-anchor="middle" font-size="9">drives the architecture work downstream and is used to validate the quality of the architecture; optional part of the Architecture Vision</text>
<text x="380" y="278" text-anchor="middle" font-size="9">review step goal: shared understanding of the full scope of the problem — buy-in, or stop</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">Original drawing. Steps follow GUIDE:business-scenarios §3.1; phases and their outputs §3.3 and §3.3.1; the review goal §3.2.5; the Architecture Vision link ADM §3.3.8.</figcaption>
</figure>

## The method

Six steps capture the five elements: identify, document and rank the problem; identify the
business and technical environment and document it in models including value streams and
capabilities; identify desired outcomes and make them SMART; identify human actors; identify
computer actors; check fitness for purpose and refine only if necessary
(GUIDE:business-scenarios §3.1). The steps repeat in three phases — premise formulation, initial
verification, refinement — and the released document goes into the Requirements Repository as
the high-level requirements statement that drives and validates the architecture
(GUIDE:business-scenarios §3.3). Premise formulation treats the initial proposition as a premise
with unstated questions; its triggers include "problem looking for a solution", "solution
looking for a problem" and "dominance of technology speak" (GUIDE:business-scenarios §3.3.1).

Gathering favours preprocessing openly available material before workshops, and workshops with
a small, carefully selected group from high levels of the business and technical sides,
sometimes separated (GUIDE:business-scenarios §3.2.2). Reviewing feeds results back to the
sponsors for a shared understanding of the problem's scope and technical impact; "the goal is to
get buy-in or stop" (GUIDE:business-scenarios §3.2.5). The workshop questions start by testing
whether the problem is a *what* or a technology-push *how*, raise a red flag either way, and ask
where, when and at what cost the problem occurs (GUIDE:business-scenarios §7.2.1).

## Contents, contributions, roles

The document sequences the critical steps and interactions between actors, their
responsibilities, the pre-conditions and the technical requirements for acceptable quality; it
has graphics (models relating actors and interactions) and text, with a contents list running
from executive summary through business environment, technical environment, analysis
(problem, pain points, outcomes, requirements, principles and constraints) to prioritised areas
for standardisation (GUIDE:business-scenarios §4). Business management contributes most early,
the architect most later as solutions are described, and vendors — if involved — later still
(GUIDE:business-scenarios §5). The roles include project manager, consultant, analyst, author,
editor, facilitator, SME contributors and reviewers, host, sponsor, questioners and recorders,
several of which one person may fill (GUIDE:business-scenarios §10).

Objectives must be SMART, and the guide gives categories of goal — improve process performance,
decrease costs, improve business operations, management efficacy, reduce risk, improve IT
effectiveness, user productivity, portability, interoperability, vendor independence, lifecycle
cost, security, manageability — each with candidate objectives (GUIDE:business-scenarios §9.2).
When a workshop shows bias towards one approach, alternative analysis with a weighted decision
matrix (cost, resources, contribution, feasibility) restores the comparison
(GUIDE:business-scenarios §12.8).

## In the ADM

Business scenarios figure most prominently in Phase A, to define business requirements and build
consensus with business management; they are also used in Phase B to derive the architecture
from high-level requirements, and in any phase where requirements must be derived, including the
Preliminary Phase for the EA capability itself (GUIDE:business-scenarios §6). Phase A names them
as the appropriate technique to discover and document requirements and to articulate a Vision
that responds to them (ADM §3.3.8).

**Trap.** They are a tool, not the objective: stay focused, watch for feature creep, and address
the issues that return the greatest value (GUIDE:business-scenarios §13).

## How the 5-point answer differs from the 3-point one

| Points | What the answer does |
|---|---|
| 5 | Treats the sponsor's solution as a premise, runs the six steps through premise formulation, verification and refinement with the right participants, makes outcomes SMART, reviews with the sponsors for buy-in or stop, and places the released scenario in the Requirements Repository to drive Phase A and B |
| 3 | Runs the workshops and documents the scenario but skips the review readout, or stops at the first draft, or never makes the outcomes measurable |
| 1 | Writes use-cases or a business case and calls it a business scenario |
| 0 | Accepts the premise and moves to Phase B, or lets the vendors write the requirements |

## Where to look in the book

Series Guide: Business Scenarios §1 (definition, SMART, what it is not), §2 (benefits), §3.1
(six steps), §3.2.2 (gathering), §3.2.5 (reviewing), §3.3 and §3.3.1 (phases, premise), §4
(contents), §5 (contributions), §6 (ADM placement), §7.2.1 (questions), §9.2 (SMART
objectives), §10 (roles), §12.8 (decision matrix), §13. ADM §3.3.8.
