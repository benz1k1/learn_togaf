---
title: Phase F in practice, finalising the plan with the portfolio
unit: P5
objectives: ["P5.1"]
refs: ["ADM §10", "ADM §10.1", "ADM §10.3", "ADM §10.3.1", "ADM §10.3.2", "ADM §10.3.3", "ADM §10.3.4", "ADM §10.3.5", "ADM §10.3.6", "ADM §10.3.7", "ADM §10.4", "ADM §10.5", "CONTENT §3.6.9", "CONTENT §4.2.14", "CONTENT §4.2.15", "TECH §7.5", "TECH §7.6"]
reading_minutes: 9
source: authored
status: draft
---
## What a Phase F scenario looks like

The draft Architecture Roadmap and the draft Implementation and Migration Plan exist. The
scenario now introduces the people Phase E did not need: a portfolio manager with a change
calendar already full, a finance director who wants each project justified, an operations
head worried about running two systems in parallel, and a sponsor who wants to know which
transition comes first. Phase F's objectives are exactly those concerns: finalise the roadmap
and plan, co-ordinate them with the enterprise's approach to managing change, and make sure
key stakeholders understand the business value and cost of each work package and Transition
Architecture (ADM §10.1). Its focus is a plan built *in co-operation with* the project and
portfolio managers, not handed to them (ADM §10.5).

The five-point answer walks the seven Phase F steps, beginning with the management
frameworks; the three-point answer prioritises and costs the projects but never
co-ordinates with the other frameworks, or forgets to update the Definition Document with
the transitions; the one-point answer restarts gap analysis; the zero-point answer asks the
portfolio office to schedule the work packages without value or risk being assigned.

## The seven steps and the questions they answer

| Step | The question the scenario planted | What the standard says |
|---|---|---|
| 10.3.1 Confirm management framework interactions | "The PMO has its own plan" | Four frameworks must work together: Business Planning, Enterprise Architecture, Project/Portfolio Management, Operations Management. The plan is inserted, in summary, into each of their plans, and it may end up as part of a plan owned by one of them (ADM §10.3.1) |
| 10.3.2 Assign business value to each work package | "Finance wants a justification" | Define what business value means here, then performance evaluation criteria, ROI criteria, critical success factors, measures of effectiveness and strategic fit; aggregate risks from the Phase E matrix; use the Business Value and Risk matrix (ADM §10.3.2) |
| 10.3.3 Estimate resources, timings, delivery vehicle | "How much, how long, who" | Split capital from operations and maintenance cost; look for decommissioning that offsets cost (ADM §10.3.3) |
| 10.3.4 Prioritise by cost/benefit and risk | "Which first" | Net benefit of the SBBs, risks mitigated, then *stakeholder consensus* on a prioritised list; a project can rank high because it is on the path to a large benefit; review residual risk against the funding line (ADM §10.3.4) |
| 10.3.5 Confirm the roadmap, update the ADD | "Do the transitions still make sense" | Reassess the time-spans between transitions; use the Transition Architecture State Evolution table and the Architecture Definition Increments table (ADM §10.3.5, CONTENT §3.6.9) |
| 10.3.6 Complete the plan | "One integrated plan" | Integrate projects, dependencies and impact of change; Transition Architectures act as portfolio milestones; capture external dependencies (ADM §10.3.6) |
| 10.3.7 Close the cycle, document lessons | "What did we learn, who governs now" | Governance moves from developing to realising the architecture; an Implementation Governance Model if maturity warrants; lessons go to Phase H (ADM §10.3.7) |

**Trap.** The four management frameworks are Business Planning, Enterprise Architecture,
Project/Portfolio Management and Operations Management. An answer that co-ordinates only
with "the PMO" has covered one of four (ADM §10.3.1).

<figure class="my-4">
<svg viewBox="0 0 760 290" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="11" role="img" aria-label="Phase F: the draft plan is co-ordinated with four management frameworks, valued, costed, prioritised and completed, then governance hands over to realisation">
<defs><marker id="arr-p5f" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
<rect x="10" y="14" width="150" height="50" rx="6" fill="#f3e3f7" stroke="#b58ac9"/>
<text x="85" y="34" text-anchor="middle" font-weight="bold">from Phase E</text>
<text x="85" y="50" text-anchor="middle">draft roadmap, draft plan</text>
<g fill="#fff" stroke="#666">
<rect x="180" y="14" width="120" height="50" rx="6"/>
<rect x="320" y="14" width="120" height="50" rx="6"/>
<rect x="460" y="14" width="120" height="50" rx="6"/>
<rect x="600" y="14" width="150" height="50" rx="6"/>
</g>
<text x="240" y="34" text-anchor="middle">10.3.2 value</text><text x="240" y="50" text-anchor="middle">10.3.3 cost and time</text>
<text x="380" y="34" text-anchor="middle">10.3.4 prioritise</text><text x="380" y="50" text-anchor="middle">consensus, residual risk</text>
<text x="520" y="34" text-anchor="middle">10.3.5 confirm roadmap</text><text x="520" y="50" text-anchor="middle">10.3.6 complete plan</text>
<text x="675" y="34" text-anchor="middle" font-weight="bold">10.3.7 close cycle</text><text x="675" y="50" text-anchor="middle">lessons learned, governance model</text>
<line x1="160" y1="39" x2="180" y2="39" stroke="#555" marker-end="url(#arr-p5f)"/>
<line x1="300" y1="39" x2="320" y2="39" stroke="#555" marker-end="url(#arr-p5f)"/>
<line x1="440" y1="39" x2="460" y2="39" stroke="#555" marker-end="url(#arr-p5f)"/>
<line x1="580" y1="39" x2="600" y2="39" stroke="#555" marker-end="url(#arr-p5f)"/>
<rect x="60" y="110" width="640" height="34" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="380" y="131" text-anchor="middle" font-weight="bold">10.3.1 confirm interactions with the four management frameworks (runs first and frames every later step)</text>
<g fill="#fff" stroke="#7aa2e3">
<rect x="60" y="170" width="150" height="40" rx="6"/><rect x="223" y="170" width="150" height="40" rx="6"/><rect x="386" y="170" width="150" height="40" rx="6"/><rect x="549" y="170" width="151" height="40" rx="6"/>
</g>
<text x="135" y="195" text-anchor="middle">Business Planning</text>
<text x="298" y="195" text-anchor="middle">Enterprise Architecture</text>
<text x="461" y="195" text-anchor="middle">Project / Portfolio Mgmt</text>
<text x="624" y="195" text-anchor="middle">Operations Management</text>
<line x1="135" y1="144" x2="135" y2="170" stroke="#555" marker-end="url(#arr-p5f)"/>
<line x1="298" y1="144" x2="298" y2="170" stroke="#555" marker-end="url(#arr-p5f)"/>
<line x1="461" y1="144" x2="461" y2="170" stroke="#555" marker-end="url(#arr-p5f)"/>
<line x1="624" y1="144" x2="624" y2="170" stroke="#555" marker-end="url(#arr-p5f)"/>
<line x1="240" y1="64" x2="240" y2="110" stroke="#555" stroke-dasharray="4 3"/>
<text x="380" y="245" text-anchor="middle" fill="#666">the plan is inserted, in summary, into each framework's own plan; it may end up owned by one of them with EA participation (ADM §10.3.1)</text>
<text x="380" y="268" text-anchor="middle" fill="#666">outputs: Implementation and Migration Plan (approved), finalized ADD, ARS and Roadmap, re-usable ABBs, Requests for Architecture Work (ADM §10.4)</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">Phase F: the value, cost and priority steps sit inside a frame set by the four management frameworks. Original drawing; the steps follow ADM §10.3.</figcaption>
</figure>

## Value is defined before it is assigned

The step that separates a five from a three is 10.3.2. The standard says first establish
*what constitutes business value in this organisation and how it is measured*, then apply
it; it names performance evaluation criteria for portfolio managers, return-on-investment
criteria signed off by executives, critical success factors, measures of effectiveness and
strategic fit against the whole Enterprise Architecture (ADM §10.3.2). The Business Value
and Risk matrix carries a weighted value index (principles compliance, financial
contribution, strategic alignment, competitive position) and a weighted risk index (size and
complexity, technology, organisational capacity, impact of failure), and the criteria and
weights are approved by senior management *before the options are known* (CONTENT §3.6.9).
A scenario in which one executive insists on ranking projects by personal preference is
pointing you at that sentence.

Readiness findings belong in this plan too. The readiness assessment is a living document
that is a key input to migration planning in E and F; if a transformation action is on the
critical path it must shape the implementation, there is no point deploying capability that
staff cannot use or support, and the plan should carry a Communications Plan for affected
personnel (TECH §7.5, TECH §7.6).

## The outputs, and which are "approved"

Phase F outputs the Implementation and Migration Plan, *approved*, with the strategy, the
project and portfolio breakdown, milestones, work breakdown and optional project charters;
the *finalized* Architecture Definition Document including any Transition Architectures; the
finalized Architecture Requirements Specification and Roadmap; re-usable ABBs; Requests for
Architecture Work for a new iteration if one is needed; an Implementation Governance Model if
produced; and Change Requests for the Architecture Capability arising from lessons learned
(ADM §10.4, CONTENT §4.2.14). The Implementation Governance Model defines processes,
organisation structure, roles and responsibilities, checkpoints and success criteria so that
a project moving into implementation also moves into architecture governance
(CONTENT §4.2.15).

**Trap.** "Complete the architecture development cycle" does not mean the architecture is
finished; it means governance transitions from development to realisation, and if the next
phase needs much more detail, another ADM cycle at a lower level may follow (ADM §10.3.7).

## How the 5, 3 and 1 differ

| Answer | Why it scores that |
|---|---|
| 5 | Confirms the four framework interactions, defines value criteria with the executives and applies them per work package, costs capital and operations separately, wins stakeholder consensus on priority with residual risk understood, confirms transitions with the State Evolution table, completes one integrated plan with transitions as milestones, records lessons and an Implementation Governance Model |
| 3 | Costs and prioritises correctly but treats the plan as an EA document, never inserting it into business planning, portfolio and operations plans (ADM §10.3.1) |
| 1 | Reopens the domain architectures to "re-check the gaps" before planning; Phase F does not redo gap analysis, it finalises what E produced (ADM §10.5) |
| 0 | Sends the work packages to the PMO to schedule by capacity; value, cost and risk were never assigned and stakeholders never agreed the priority (ADM §10.3.2, §10.3.4) |

## Where to look in the book

ADM chapter 10: §10.3.1 for the four frameworks, §10.3.2 for the value criteria, §10.3.4 for
the prioritisation rules, §10.3.5 for the two tables, §10.4 for which outputs are approved or
finalized. Architecture Content §3.6.9 for the Transition Architecture State Evolution table
and the Business Value and Risk matrix, §4.2.14 and §4.2.15 for the plan and the governance
model. ADM Techniques §7.5 and §7.6 for readiness in migration planning.

## Check yourself

- Name the four management frameworks without looking.
- What must be agreed before the project options are known?
- Which Phase F output is "approved" and which are "finalized"?
