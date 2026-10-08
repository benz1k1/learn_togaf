---
title: Purpose before method — the EA Capability, its four purposes and the business cycle
unit: P1
objectives: ["P1.1"]
refs: ["GUIDE:togaf-leaders-guide §3.3", "GUIDE:togaf-leaders-guide §5", "GUIDE:togaf-leaders-guide §5.2", "GUIDE:togaf-leaders-guide §5.4", "GUIDE:togaf-leaders-guide §6.2", "GUIDE:adm-practitioners §3.2.2", "GUIDE:adm-practitioners §4.1", "GUIDE:adm-practitioners §11.2", "GUIDE:adm-practitioners §11.2.1", "GOV §2.1", "GOV §2.2"]
reading_minutes: 10
source: authored
status: draft
---
## What a "context for EA" scenario looks like

The scenario describes an enterprise, a sponsor with a broad ambition ("we need an
architecture"), an EA team that is new, re-booted or mis-aligned, and a request that could be
answered at several different levels. The question is rarely "which phase" — it is "what must
the architect establish *before* any phase is worth running". The five-point answer names the
purpose the capability is being asked to serve, the decision it must inform, and the point in
the enterprise's planning cycle where that decision is taken (GUIDE:togaf-leaders-guide §5).

The Leader's Guide is blunt that the two most important activities are understanding the
enterprise context and the objective of the EA Capability, and that implicit assumptions about
either "invariably lead to failures". The answer that starts by extracting the objective from
the sponsor explicitly — playing executive talk back as capabilities, go-to-market moves or
operational requirements — is the one the exam rewards (GUIDE:togaf-leaders-guide §5).

## The four purposes

An EA Capability is established to support one or more of four purposes. Each one fixes the
breadth, the level of detail and the planning horizon of the work, and therefore which
deliverables matter (GUIDE:togaf-leaders-guide §5.2; GUIDE:adm-practitioners §3.2.2).

| Purpose | Typical span | Horizon and detail | What the architecture is used for |
|---|---|---|---|
| Support Strategy | many programmes or portfolios | 3–10 years, not very detailed, more guidance than constraint | identify change initiatives, set terms of reference, find synergies, govern execution through portfolios |
| Support Portfolio | a single portfolio | 2–5 years, not very detailed | identify projects, set their terms of reference, align approaches, govern project execution |
| Support Project | a single project | under 2 years, detailed, more constraint than guidance | clarify purpose and value, capture synergy and dependency requirements, assure compliance, align between projects |
| Support Solution Delivery | a project or a large part of one | under 2 years, the most detailed, constraints only | define how the change is designed and delivered; constraints, controls and architecture requirements for the design |

**Trap.** The purposes are not "levels of seniority". A strategy-purpose architecture may
contain a very detailed point constraint where value depends on tight control; a solution
delivery architecture carries guidance forward from its superior architecture rather than
inventing it. The scenario tests whether you match the *work product* to the purpose, not
whether you can rank the purposes (GUIDE:adm-practitioners §3.2.2).

<figure class="my-4">
<svg viewBox="0 0 760 300" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="11" role="img" aria-label="Four EA purposes laid against the budget cycle: strategy before budget planning, portfolio before budget preparation, project before budget allocation, solution delivery during budget control">
<defs><marker id="arr-p1-01a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
<text x="380" y="22" text-anchor="middle" font-size="12" font-weight="bold">Architecture before the decision: purpose against the budget cycle</text>
<line x1="30" y1="150" x2="730" y2="150" stroke="#555" stroke-width="2" marker-end="url(#arr-p1-01a)"/>
<text x="740" y="154" font-size="10">time</text>
<g>
<rect x="40" y="160" width="150" height="40" rx="6" fill="#f1f1f1" stroke="#999"/>
<text x="115" y="184" text-anchor="middle">Budget planning</text>
<rect x="215" y="160" width="150" height="40" rx="6" fill="#f1f1f1" stroke="#999"/>
<text x="290" y="184" text-anchor="middle">Budget preparation</text>
<rect x="390" y="160" width="150" height="40" rx="6" fill="#f1f1f1" stroke="#999"/>
<text x="465" y="184" text-anchor="middle">Budget allocation</text>
<rect x="565" y="160" width="150" height="40" rx="6" fill="#f1f1f1" stroke="#999"/>
<text x="640" y="184" text-anchor="middle">Budget control</text>
</g>
<g>
<rect x="40" y="60" width="150" height="60" rx="6" fill="#e3f0fb" stroke="#4a7fb5"/>
<text x="115" y="82" text-anchor="middle" font-weight="bold">EA to support Strategy</text>
<text x="115" y="98" text-anchor="middle" font-size="10">3–10 years, guidance</text>
<text x="115" y="111" text-anchor="middle" font-size="10">what initiatives to start</text>
<rect x="215" y="60" width="150" height="60" rx="6" fill="#e3f0fb" stroke="#4a7fb5"/>
<text x="290" y="82" text-anchor="middle" font-weight="bold">EA to support Portfolio</text>
<text x="290" y="98" text-anchor="middle" font-size="10">2–5 years, roadmap ready</text>
<text x="290" y="111" text-anchor="middle" font-size="10">what to fund or defer</text>
<rect x="390" y="60" width="150" height="60" rx="6" fill="#e3f0fb" stroke="#4a7fb5"/>
<text x="465" y="82" text-anchor="middle" font-weight="bold">EA to support Project</text>
<text x="465" y="98" text-anchor="middle" font-size="10">under 2 years, constraints</text>
<text x="465" y="111" text-anchor="middle" font-size="10">business case, contract</text>
<rect x="565" y="60" width="150" height="60" rx="6" fill="#e3f0fb" stroke="#4a7fb5"/>
<text x="640" y="82" text-anchor="middle" font-weight="bold">EA to support Solution Delivery</text>
<text x="640" y="98" text-anchor="middle" font-size="10">most detailed, Phase G</text>
<text x="640" y="111" text-anchor="middle" font-size="10">governs the implementation</text>
</g>
<line x1="115" y1="120" x2="115" y2="158" stroke="#4a7fb5" marker-end="url(#arr-p1-01a)"/>
<line x1="290" y1="120" x2="290" y2="158" stroke="#4a7fb5" marker-end="url(#arr-p1-01a)"/>
<line x1="465" y1="120" x2="465" y2="158" stroke="#4a7fb5" marker-end="url(#arr-p1-01a)"/>
<line x1="640" y1="120" x2="640" y2="158" stroke="#4a7fb5" marker-end="url(#arr-p1-01a)"/>
<rect x="40" y="220" width="675" height="60" rx="6" fill="#fde8e6" stroke="#c0392b"/>
<text x="377" y="243" text-anchor="middle" font-size="11" font-weight="bold" fill="#c0392b">Failure pattern: architecture after the decision</text>
<text x="377" y="262" text-anchor="middle" font-size="10">at best it validates a decision already taken; at worst it proves the decision wrong after the money has moved</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">Original drawing. Purposes and horizons follow GUIDE:adm-practitioners §3.2.2; the alignment to budget planning, preparation, allocation and control follows §4.1; the failure pattern is §11.2.1.</figcaption>
</figure>

## The business cycle: architecture before the decision

The Practitioners' Approach ties each purpose to a milestone of the budget cycle: strategy
architecture feeds budget planning, portfolio architecture must be ready at the *start* of
budget preparation, project architecture supports the allocation of funds through a business
case or charter, and solution delivery architecture runs alongside budget control in Phase G.
"Architecture before the decision" is the whole point — good architecture that informs a
decision is worth more than perfect architecture produced after it (GUIDE:adm-practitioners §4.1).

Missing the cycle is a named failure pattern. Practitioners who wait for an invitation, or for
clarity that only arrives at the end of the planning process, have already missed their place
in it; a candidate Target Architecture and roadmap for a budget finalised in the third quarter
must exist in the second (GUIDE:adm-practitioners §11.2). Architecture produced after the
decision is "not only late but may cause conflict" (GUIDE:adm-practitioners §11.2.1).

**Trap.** A scenario in which the board has already chosen a product and the sponsor asks the
EA team to "architect it" is describing a jump to Phase G. The five-point answer does not
refuse the work; it re-scopes it to the decision that is still open (the portfolio or the next
allocation) and provides risk-focused support to the project that is already running
(GUIDE:adm-practitioners §11.2.1).

## Establishing the capability is itself an ADM cycle

The standard treats an architecture practice like any other business capability: set it up
with the ADM, with an Architecture Vision whose subject is the practice itself, and design its
four domain architectures — the governance, processes and structure of the practice, the
Continuum and Repository as its data, the tooling as its applications, and the infrastructure
under them (GOV §2.1). The practice is an ongoing discipline, not a phase or a one-off project;
an architecture project may raise a change to the practice that triggers another cycle (GOV §2.1).

In Phase A for the practice, the steps take on a specific meaning: secure endorsement of
corporate management, identify the practice's stakeholders and drivers, define the practice's
scope for the next period, define enterprise-wide constraints, and review the principles that
govern the *practice* (its organisation, content, tools and process) as distinct from the
principles that govern deliverables. A maturity assessment can be added here (GOV §2.2).

## What the sponsor must be asked

The Leader's Guide gives the questions whose answers frame everything downstream: what the
capability is expected to achieve and why; the usage of the EA produced; how success is
measured; whether it is doing the right thing for the context; its depth and breadth; and its
organisation model (GUIDE:togaf-leaders-guide §5). Success measures are derived from the
purpose; two named "death traps" are adopting the team's own common-sense ideas as objectives
without validation, and confusing *supporting* decision-making with *making* decisions
(GUIDE:togaf-leaders-guide §5.4).

Governance follows the same rule. Decision rights over the target architecture, relief and
enforcement are vested in the stakeholders; an EA governance board owns the *process* and a
recommendation about completeness and confidence. A scenario in which the architecture board
"approves the target" is planting this failure pattern (GUIDE:togaf-leaders-guide §6.2).

## How the 5-point answer differs from the 3-point one

| Points | What the answer does |
|---|---|
| 5 | Names the purpose (strategy / portfolio / project / solution delivery), the decision and its date in the business cycle, extracts objectives and success measures from the sponsor, and sizes breadth, depth and horizon to that purpose |
| 3 | Right purpose and right deliverables, but silent on the cycle — the roadmap arrives after budgets are prepared, or objectives are assumed from documents rather than validated with the sponsor |
| 1 | Runs a full ADM cycle at solution detail regardless of the question; or lets the architecture board decide the target |
| 0 | Takes the sponsor's product choice as the architecture and starts design; or waits for an invitation |

## Where to look in the book

Leader's Guide §3.3 and §5.2 (the four purposes), §5 (the questions to answer), §5.4 (success
measures and the death traps), §6.2 (who holds decision rights). Practitioners' Approach §3.2.2
(purpose against breadth, detail, time, recency), §4.1 (the budget cycle), §11.2 and §11.2.1
(missing the business cycle, architecture after decision). EA Capability and Governance §2.1
and §2.2 for establishing the practice with the ADM.
