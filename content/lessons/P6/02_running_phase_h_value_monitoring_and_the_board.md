---
title: Running Phase H, value realisation, monitoring and the board's decision
unit: P6
objectives: ["P6.1"]
refs: ["ADM §12.2.3", "ADM §12.3", "ADM §12.3.1", "ADM §12.3.2", "ADM §12.3.4", "ADM §12.3.6", "ADM §12.3.7", "ADM §12.5", "ADM §12.5.1", "ADM §10.3.7", "ADM §13.3", "GOV §4.4.3", "GOV §3.2.1"]
reading_minutes: 8
source: authored
status: draft
---
## The other Phase H scenario

Not every Phase H question is about a change request. A second pattern describes an
architecture that was deployed a year ago and asks what the architecture function should
*now be doing*: usage has grown, a service level is slipping, the board wants to know whether
the promised value arrived, and the lessons from the last cycle were never written down. The
standard's answer is the seven Phase H steps, and the five-point answer names them in order
rather than jumping straight to "raise a change request" (ADM §12.3).

| Step | What the scenario plants | What the answer does |
|---|---|---|
| 12.3.1 Establish value realisation process | "Did we get the benefits?" | Influence business projects to exploit the architecture for value outcomes (ADM §12.3.1) |
| 12.3.2 Deploy monitoring tools | "We only find out when something breaks" | Monitor technology and business change that could affect the baseline, business value tracking, capability maturity, asset programmes, quality of service and usage, business continuity requirements (ADM §12.3.2) |
| 12.3.3 Manage risks | "The vendor is being acquired" | Manage Enterprise Architecture risks and make IT strategy recommendations |
| 12.3.4 Provide analysis | "The SLA is being missed" | Analyse performance, hold performance reviews with service management, assess Change Requests against expected value and SLA expectations, run a gap analysis of the architecture's performance, ensure requests adhere to the governance framework (ADM §12.3.4) |
| 12.3.5 Develop change requirements | "What should we change?" | Recommend change requirements to meet performance targets and a position to act |
| 12.3.6 Manage governance process | "Who decides?" | Arrange and hold the Architecture Board meeting to decide on business and technology changes and dispensations (ADM §12.3.6) |
| 12.3.7 Activate the process to implement change | "Now what?" | Produce a new Request for Architecture Work and request for investment; record every change made in this phase in the Architecture Repository (ADM §12.3.7) |

## Value and capacity are the point of the phase

The goal of architecture change management is to ensure the architecture achieves its
original target business value, and to manage change in a cohesive, architected way; the
process continually monitors governance requests, technology developments and the business
environment and decides whether to initiate a new evolution cycle (ADM §12.5). Two things the
standard stresses are easy to miss in an exam answer. First, monitoring business growth and
decline: "usage of the Enterprise Architecture is the most important part of the
architecture development cycle", and an architecture that worked for yesterday's
organisation may not give back enough capability today (ADM §12.5). Second, capacity: the
architecture specification may still fit while the *solutions* under it do not scale or
become uneconomic, so capacity measurement and planning recommendations are a key aspect of
this phase (ADM §12.5).

**Trap.** The inputs to Phase H include three kinds of Change Request: technology changes,
business changes, and Change Requests from *lessons learned*; plus the signed contract, the
Compliance Assessments, the Implementation Governance Model and the plan (ADM §12.2.3). An
answer that only looks at requests from the business has ignored two of the three sources.

<figure class="my-4">
<svg viewBox="0 0 760 250" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="11" role="img" aria-label="Phase H as a loop: monitor value and change, analyse, recommend, board decides, then either maintain the architecture or start a new cycle with a Request for Architecture Work">
<defs><marker id="arr-p6l" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
<g fill="#fff" stroke="#666">
<rect x="15" y="20" width="130" height="54" rx="8"/>
<rect x="170" y="20" width="130" height="54" rx="8"/>
<rect x="325" y="20" width="130" height="54" rx="8"/>
<rect x="480" y="20" width="130" height="54" rx="8"/>
</g>
<text x="80" y="42" text-anchor="middle" font-weight="bold">monitor</text><text x="80" y="58" text-anchor="middle">12.3.1 value, 12.3.2 tools</text>
<text x="235" y="42" text-anchor="middle" font-weight="bold">analyse</text><text x="235" y="58" text-anchor="middle">12.3.3 risks, 12.3.4 analysis</text>
<text x="390" y="42" text-anchor="middle" font-weight="bold">recommend</text><text x="390" y="58" text-anchor="middle">12.3.5 change requirements</text>
<text x="545" y="42" text-anchor="middle" font-weight="bold">decide</text><text x="545" y="58" text-anchor="middle">12.3.6 Architecture Board</text>
<line x1="145" y1="47" x2="170" y2="47" stroke="#555" marker-end="url(#arr-p6l)"/>
<line x1="300" y1="47" x2="325" y2="47" stroke="#555" marker-end="url(#arr-p6l)"/>
<line x1="455" y1="47" x2="480" y2="47" stroke="#555" marker-end="url(#arr-p6l)"/>
<rect x="640" y="20" width="110" height="54" rx="8" fill="#f1f1f1" stroke="#999"/>
<text x="695" y="42" text-anchor="middle" font-weight="bold">12.3.7 act</text><text x="695" y="58" text-anchor="middle">and record</text>
<line x1="610" y1="47" x2="640" y2="47" stroke="#555" marker-end="url(#arr-p6l)"/>
<rect x="120" y="130" width="230" height="54" rx="8" fill="#e3f5e1" stroke="#7fbf7a"/>
<text x="235" y="152" text-anchor="middle" font-weight="bold">maintenance change</text>
<text x="235" y="168" text-anchor="middle">architecture, framework, principles updated</text>
<rect x="410" y="130" width="230" height="54" rx="8" fill="#fde8e6" stroke="#c0392b"/>
<text x="525" y="152" text-anchor="middle" font-weight="bold">major change</text>
<text x="525" y="168" text-anchor="middle">new Request for Architecture Work, new cycle</text>
<line x1="670" y1="74" x2="300" y2="130" stroke="#555" marker-end="url(#arr-p6l)"/>
<line x1="700" y1="74" x2="560" y2="130" stroke="#555" marker-end="url(#arr-p6l)"/>
<path d="M235 184 L235 215 L80 215 L80 74" fill="none" stroke="#555" stroke-dasharray="5 4" marker-end="url(#arr-p6l)"/>
<text x="380" y="235" text-anchor="middle" fill="#666">everything changed in this phase is captured in the Architecture Repository (ADM §12.3.7); the criteria for update versus new cycle sharpen as governance matures (ADM §12.5)</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">Phase H as a monitoring loop with two exits. Original drawing; the steps follow ADM §12.3 and the exits §12.4.</figcaption>
</figure>

## The board meeting is where the decision is recorded

Step 12.3.6 is literally "arrange and hold the Architecture Board meeting", and the board's
standing agenda shows what the meeting must cover: minutes, Requests for Change made within
the authority levels of the Architecture Contract, dispensations for changes outside normal
parameters, compliance assessments against SLAs, OLAs, cost targets and required refreshes,
dispute resolution, strategy and direction documents, assigned actions with an action
tracker, and contract documentation management (GOV §4.4.3). A scenario that mentions an
overdue action, an unresolved dispute between two projects or a request "outside normal
parameters" is quoting one of those agenda items. Dispensations granted here are time-bound
with enforced criteria (GOV §3.2.1).

Lessons learned deserve their own sentence in the answer. Phase F's last step captures the
lessons of the development cycle "by the appropriate governance process in Phase H" as
inputs to managing the capability (ADM §10.3.7), and Phase H's driver section says a lessons
learned process ensures mistakes are made once and not repeated, from anywhere and anyone, at
any level (ADM §12.5.1). Requirements that arise from Phase H flow into Requirements
Management through step 7 of its steps table, so the change is managed as a requirement
rather than as an ad hoc edit (ADM §13.3).

## How the 5, 3 and 1 differ

| Answer | Why it scores that |
|---|---|
| 5 | Establishes value tracking and monitoring, analyses the missed SLA with service management, assesses the requests against expected value, takes them to the Architecture Board with a compliance position, records decisions and the lessons learned in the repository, and issues a Request for Architecture Work only for the change that warrants a new cycle |
| 3 | Monitors and analyses, but the architecture team decides the changes itself and informs the board afterwards; the board is the governance body that decides on changes and dispensations (ADM §12.3.6, GOV §4.4.3) |
| 1 | Raises a Request for Architecture Work in response to the first SLA miss; the phase first analyses whether the solutions rather than the architecture are at fault and whether a maintenance change suffices (ADM §12.5) |
| 0 | Treats Phase H as "the architecture is finished" and waits for the next planned programme; the phase exists to keep the architecture dynamic and monitor usage continuously (ADM §12.5) |

## Where to look in the book

ADM §12.3 for the seven steps and §12.3.2 for the monitoring list; §12.5 for value, usage and
capacity; §12.2.3 for the three Change Request inputs. EA Capability and Governance §4.4.3
for the board agenda and §3.2.1 for dispensations. ADM §10.3.7 for how lessons reach Phase
H, and ADM §13.3 step 7 for how Phase H requirements enter Requirements Management.

## Check yourself

- List four things the Phase H monitoring tools must enable.
- Why does the standard say the architecture can still fit while the solutions do not?
- Which body decides on business and technology changes and dispensations in step 12.3.6?
