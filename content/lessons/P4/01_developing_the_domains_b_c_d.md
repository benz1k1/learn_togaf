---
title: Developing the domains — the nine steps of Phases B, C and D and the decisions they hide
unit: P4
objectives: ["P4.1"]
refs: ["ADM §4.1", "ADM §4.3", "ADM §4.3.1", "ADM §4.3.2", "ADM §4.3.3", "ADM §4.3.4", "ADM §4.3.5", "ADM §4.3.6", "ADM §4.3.7", "ADM §4.4", "ADM §4.5.1", "ADM §5.1", "ADM §5.2", "ADM §6.3.7", "ADM §6.4", "ADM §6.5.2", "ADM §7.3.7", "ADM §8.1", "ADM §8.3.3", "ADM §8.4", "GUIDE:adm-practitioners §6.3", "GUIDE:adm-practitioners §6.3.2"]
reading_minutes: 11
source: authored
status: draft
---
## What a Phase B, C or D scenario looks like

The Statement of Architecture Work is approved, the Vision exists, and the scenario drops you
into one domain: a Business Architecture for a merger, a Data Architecture for a replacement
platform, a Technology Architecture for a cloud move. It plants a sequencing question (baseline
or target first? data or application first?), a stakeholder whose concern has no model, an
in-flight project the new architecture will collide with, and an ask to "finalise" something.
The five-point answer walks the nine steps, in the order the situation demands, and knows what
the formal stakeholder review and the impact resolution step are for (ADM §4.3;
GUIDE:adm-practitioners §6.3).

Each of the three phases shares a pair of objectives: develop the Target architecture for that
domain in a way that addresses the Statement of Architecture Work and stakeholder concerns, and
identify candidate Architecture Roadmap components from the gaps between baseline and target
(ADM §4.1; ADM §5.1; ADM §8.1). The Business Architecture describes how the enterprise needs to
operate to achieve its goals and respond to the drivers in the Vision; Information Systems
describes how they enable the Business Architecture and the Vision; Technology enables the
Vision and the target business, data and application building blocks through technology
components and services (ADM §4.1; ADM §5.1; ADM §8.1).

## The nine steps, once

The steps are the same in B, C (data), C (application) and D, and the Practitioners' Approach
explains why: the approach to developing an architecture, confirming it fits and confirming
approval is identical; what changes is level of detail, precision and formality. Steps can be
skipped, "but the final outcome could be at risk", so use them as a checklist
(GUIDE:adm-practitioners §6.3).

| # | Step | The decision it hides |
|---|---|---|
| 1 | Select reference models, viewpoints and tools | choose from the Repository on the basis of drivers and concerns; every stakeholder concern must be covered by a viewpoint |
| 2 | Develop Baseline description | only to the extent needed to support the target; re-use existing descriptions |
| 3 | Develop Target description | to the extent needed to support the Vision; investigate alternatives with stakeholders using trade-off |
| 4 | Perform gap analysis | verify consistency, principles, completeness against requirements, then baseline-to-target gaps |
| 5 | Define candidate roadmap components | raw material for the consolidated roadmap in Phase E |
| 6 | Resolve impacts across the Architecture Landscape | pre-existing architectures, recent changes, re-use, projects planned and in flight |
| 7 | Conduct formal stakeholder review | check the original motivation and the Statement of Architecture Work against the proposal; in C, an impact analysis on the other domains |
| 8 | Finalize the architecture | select standards per building block, document each, cross-check against goals, traceability report, publish re-usable blocks |
| 9 | Create / update the Architecture Definition Document | document the rationale for building block decisions; route for review |

(ADM §4.3.1 to §4.3.7; the finalise and create/update steps ADM §4.3; GUIDE:adm-practitioners §6.3.2.)

<figure class="my-4">
<svg viewBox="0 0 760 320" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="10" role="img" aria-label="The nine development steps as a strip repeated for Phases B, C and D, with three decision points called out: the order of baseline and target, the order of data and application inside Phase C, and the stakeholder review that may send the work back to another domain">
<defs><marker id="arr-p4-01a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
<text x="380" y="18" text-anchor="middle" font-size="12" font-weight="bold">One strip of nine steps, run for B, then C (data and application in either order), then D</text>
<g>
<rect x="10" y="40" width="74" height="46" rx="5" fill="#e3f0fb" stroke="#4a7fb5"/><text x="47" y="58" text-anchor="middle" font-size="9">1 Select ref.</text><text x="47" y="70" text-anchor="middle" font-size="9">models, viewpoints</text>
<rect x="92" y="40" width="74" height="46" rx="5" fill="#e3f0fb" stroke="#4a7fb5"/><text x="129" y="58" text-anchor="middle" font-size="9">2 Baseline</text><text x="129" y="70" text-anchor="middle" font-size="9">description</text>
<rect x="174" y="40" width="74" height="46" rx="5" fill="#e3f0fb" stroke="#4a7fb5"/><text x="211" y="58" text-anchor="middle" font-size="9">3 Target</text><text x="211" y="70" text-anchor="middle" font-size="9">description</text>
<rect x="256" y="40" width="74" height="46" rx="5" fill="#fff1d6" stroke="#e0b060"/><text x="293" y="58" text-anchor="middle" font-size="9">4 Gap</text><text x="293" y="70" text-anchor="middle" font-size="9">analysis</text>
<rect x="338" y="40" width="74" height="46" rx="5" fill="#fff1d6" stroke="#e0b060"/><text x="375" y="58" text-anchor="middle" font-size="9">5 Candidate</text><text x="375" y="70" text-anchor="middle" font-size="9">roadmap parts</text>
<rect x="420" y="40" width="74" height="46" rx="5" fill="#fff1d6" stroke="#e0b060"/><text x="457" y="58" text-anchor="middle" font-size="9">6 Resolve</text><text x="457" y="70" text-anchor="middle" font-size="9">landscape impacts</text>
<rect x="502" y="40" width="74" height="46" rx="5" fill="#e3f5e1" stroke="#7fbf7a"/><text x="539" y="58" text-anchor="middle" font-size="9">7 Formal stake-</text><text x="539" y="70" text-anchor="middle" font-size="9">holder review</text>
<rect x="584" y="40" width="74" height="46" rx="5" fill="#e3f5e1" stroke="#7fbf7a"/><text x="621" y="58" text-anchor="middle" font-size="9">8 Finalize the</text><text x="621" y="70" text-anchor="middle" font-size="9">architecture</text>
<rect x="666" y="40" width="84" height="46" rx="5" fill="#e3f5e1" stroke="#7fbf7a"/><text x="708" y="58" text-anchor="middle" font-size="9">9 Create/update</text><text x="708" y="70" text-anchor="middle" font-size="9">the ADD</text>
</g>
<rect x="92" y="104" width="156" height="30" rx="5" fill="#fff" stroke="#c0392b"/>
<text x="170" y="123" text-anchor="middle" font-size="9" fill="#c0392b">order decided per situation (Applying the ADM)</text>
<line x1="170" y1="104" x2="170" y2="88" stroke="#c0392b" marker-end="url(#arr-p4-01a)"/>
<rect x="470" y="104" width="180" height="30" rx="5" fill="#fff" stroke="#c0392b"/>
<text x="560" y="123" text-anchor="middle" font-size="9" fill="#c0392b">may send you back to B or C, or into a short C iteration</text>
<line x1="539" y1="104" x2="539" y2="88" stroke="#c0392b" marker-end="url(#arr-p4-01a)"/>
<g>
<rect x="10" y="160" width="230" height="60" rx="6" fill="#f1f1f1" stroke="#999"/>
<text x="125" y="182" text-anchor="middle" font-weight="bold">Phase B — Business</text>
<text x="125" y="198" text-anchor="middle" font-size="9">first, unless already done elsewhere;</text>
<text x="125" y="211" text-anchor="middle" font-size="9">capabilities, value streams, org and information maps</text>
<line x1="240" y1="190" x2="264" y2="190" stroke="#555" marker-end="url(#arr-p4-01a)"/>
<rect x="266" y="160" width="230" height="60" rx="6" fill="#f1f1f1" stroke="#999"/>
<text x="381" y="182" text-anchor="middle" font-weight="bold">Phase C — Data ⇄ Application</text>
<text x="381" y="198" text-anchor="middle" font-size="9">either order; data-driven (EAP) or application-driven</text>
<text x="381" y="211" text-anchor="middle" font-size="9">(ERP/CRM as core); review checks impact on the other</text>
<line x1="496" y1="190" x2="520" y2="190" stroke="#555" marker-end="url(#arr-p4-01a)"/>
<rect x="522" y="160" width="228" height="60" rx="6" fill="#f1f1f1" stroke="#999"/>
<text x="636" y="182" text-anchor="middle" font-weight="bold">Phase D — Technology</text>
<text x="636" y="198" text-anchor="middle" font-size="9">taxonomy first (TRM), ABBs conceptualised,</text>
<text x="636" y="211" text-anchor="middle" font-size="9">constraints received from B and C</text>
</g>
<rect x="10" y="240" width="740" height="70" rx="6" fill="#fff" stroke="#666"/>
<text x="380" y="260" text-anchor="middle" font-weight="bold">Every phase ends with the same three deliverables</text>
<text x="380" y="278" text-anchor="middle" font-size="9">Draft Architecture Definition Document (baseline and target for the domain, views for the selected viewpoints)</text>
<text x="380" y="292" text-anchor="middle" font-size="9">Draft Architecture Requirements Specification (gap results, interoperability and technical requirements, constraints on the next domain) &#183; domain components of the Architecture Roadmap</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">Original drawing. Steps follow ADM §4.3; the sequencing choices follow ADM §4.3 and §5.2; the review's impact analysis follows ADM §6.3.7 and §7.3.7; the outputs follow ADM §4.4, §6.4 and §8.4.</figcaption>
</figure>

## The sequencing decisions

**Baseline or target first.** The order of steps, and their start and finish, is adapted to the
situation under governance; in particular, decide whether to develop the baseline or the target
first, as described in Applying the ADM (ADM §4.3). The Practitioners' Approach gives the
rule of thumb: if the current state is accepted, the baseline is described only to the extent
necessary to determine gaps; if stakeholders dispute the current state, describing it to get
alignment is useful; describe it with the same techniques at the same detail as the target so
that gaps can be found (GUIDE:adm-practitioners §6.3.2).

**Business first.** Knowledge of the Business Architecture is a prerequisite for work in any
other domain, so it is the first architecture activity unless already catered for by enterprise
planning, strategic planning or process re-engineering; where it has been done elsewhere the job
is to verify, update and bridge from drivers to specific requirements, and where little has been
done the team must research and gain buy-in. Gather only what allows informed decisions in
scope: a process-definition effort needs detailed Phase B work, an IT-focused effort needs a
complete picture without unnecessary detail (ADM §4.5.1).

**Data or application first.** Phase C is some combination of the two "in either order".
Advocates exist for both: a data-driven approach such as Enterprise Architecture Planning, or an
application-driven approach where core packages such as ERP and CRM provide infrastructure and
business logic together and their integration is the primary architecture focus (ADM §5.2).

**Trap.** A scenario in which the enterprise's strategy is a single ERP platform is nudging you
towards the application-driven order; one in which master-data ownership is the problem is
nudging towards data-driven. Either is correct if you say why; "the standard requires data
first" is not (ADM §5.2).

## Two steps the near-miss answers skip

**Resolve impacts across the Architecture Landscape** asks, once the domain is finalised: does
it impact pre-existing architectures; have recent changes impacted it; can work be leveraged
elsewhere; does it impact other projects, planned or in progress; will it be impacted by them
(ADM §4.3.6). The scenario's in-flight project is planted for this step.

**Conduct formal stakeholder review** checks the original motivation and the Statement of
Architecture Work against the proposal and refines it only if necessary (ADM §4.3.7). In the
Information Systems phases the review also runs an impact analysis on the other domains: a Data
Architecture change may require the Business and Application Architectures to be revisited, may
warrant "a short iteration of the Application Architecture", and identifies constraints on the
Technology Architecture about to be designed (ADM §6.3.7; ADM §7.3.7).

## Domain-specific things the exam checks

In Phase D, converting the existing environment into the organisation's taxonomy of technology
services and components (for example the TRM) is the way to start the baseline, and the target is
built by conceptualising ABBs that describe functionality without configuration detail
(ADM §8.3.3). In Phase C data, the approach flags data management (which components are the
system of record, how entities are created, stored, transported and reported), data migration
(the level of transformation and cleansing needed so the target application has quality data)
and data governance in three dimensions — structure, management system, people (ADM §6.5.2).

## Outputs — the same three, every phase

Each phase produces refined Vision-phase deliverables where needed; a draft Architecture
Definition Document with the approved baseline and target for the domain and the views for the
selected viewpoints; a draft Architecture Requirements Specification carrying gap results,
interoperability and technical requirements and the constraints on the domain about to be
designed; and the domain's components of the Architecture Roadmap (ADM §4.4; ADM §6.4;
ADM §8.4).

## How the 5-point answer differs from the 3-point one

| Points | What the answer does |
|---|---|
| 5 | Selects viewpoints from the stakeholders' concerns, decides baseline/target and data/application order for the stated reason, develops both descriptions to the necessary depth, runs gap analysis, resolves landscape impacts against the in-flight project, holds the formal review (with impact analysis on the other domains), finalises building blocks with standards and traceability, and updates the ADD, ARS and roadmap |
| 3 | Right steps but skips the landscape impact step or the formal review, or produces the ADD without the Architecture Requirements Specification and roadmap components |
| 1 | Models the whole baseline in full detail before touching the target, or consolidates the roadmap in Phase B |
| 0 | Selects products (SBBs) in Phase B, or treats the review as approval to proceed without the sponsor's original motivation being checked |

## Where to look in the book

ADM §4.3 (the steps and the baseline/target decision), §4.3.1 to §4.3.9 (one per step), §4.4
(outputs), §4.5.1 (business first, re-use); §5.2 (data or application first); §6.3.7 and §7.3.7
(review with impact analysis); §6.5.2 (data management, migration, governance); §8.3.3 (TRM and
ABBs); §8.4. Practitioners' Approach §6.3 (identical steps as a checklist) and §6.3.2 (just
enough baseline).
