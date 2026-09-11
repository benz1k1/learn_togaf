---
title: Requirements Management in depth
unit: F4
objectives: ["4.3", "4.7"]
refs: ["ADM §13", "ADM §13.1", "ADM §13.2", "ADM §13.3", "ADM §13.4", "ADM §13.5", "ADM §13.5.1", "ADM §13.5.2", "ADM §13.5.3"]
reading_minutes: 9
source: authored
status: draft
---
## What it is for

Requirements Management is the process of managing architecture requirements throughout the ADM
(ADM §13). The standard's chapter calls it a "phase" in its headings, but the approach section
is explicit that it is a *process*, the circle in the centre of the ADM graphic. Three
objectives (ADM §13.1):

| Objective | In plain words |
|---|---|
| Ensure the Requirements Management process is **sustained** and operates for all relevant ADM phases | it never stops |
| **Manage** architecture requirements identified during any execution of the cycle or a phase | store, track, change |
| Ensure relevant requirements are **available** to each phase as it is executed | every phase can see the current set |

## Approach

The centre circle denotes **a dynamic process, not a static set of requirements**: requirements
and their changes are identified, stored and fed into and out of the phases, and between cycles
(ADM §13.5.1). Architecture deals with uncertainty and with drivers outside the enterprise's
control, so requirements will change. The sentence the exam tests most: **the Requirements
Management process itself does not dispose of, address or prioritize any requirements; that is
done within the relevant phase.** An **Architecture Requirements Repository** is recommended for
recording all requirements; unlike the Architecture Requirements Specification and the
Requirements Impact Assessment, it can hold information from multiple ADM cycles.

Requirements development (ADM §13.5.2): the first high-level requirements come from the
Architecture Vision, via the business scenario or a similar technique. Every phase from
Preliminary to H selects the approved requirements for that phase from the repository and
specification, and updates their status at the end. New requirements within the scope of the
current Statement of Architecture Work go into the Architecture Requirements Specification;
requirements outside it go into the Repository for management by the process. Requirements are
functional and non-functional; when defining them the architect considers assumptions,
constraints, domain principles, policies, standards, organization guidelines and specifications.

Resources (ADM §13.5.3): the standard does not mandate any requirements process or tool — it
states what an effective process should achieve ("requirements for requirements"). Business
scenarios are the named technique; COTS requirements tools exist.

## Inputs

(ADM §13.2) — a short, flat list, with no external/non-architectural/architectural split:

| Input |
|---|
| A populated Architecture Repository |
| Organizational Model for Enterprise Architecture |
| Tailored Architecture Framework |
| Statement of Architecture Work |
| Architecture Vision |
| Architecture requirements, populating an Architecture Requirements Specification |
| **Requirements Impact Assessment** |

## Steps

The steps are a table with **two columns**: some are done by the Requirements Management
process, others by the ADM phase that is running (ADM §13.3).

| # | Done by | Step |
|---|---|---|
| 1 | ADM phase | Identify requirements (via value streams, business scenarios, user experiences, management information) and document them in the Architecture Requirements Specification and Requirements Repository |
| 2 | Requirements Management | Establish baseline requirements: priorities, stakeholder agreement, documentation |
| 3 | Requirements Management | Monitor baseline requirements |
| 4 | ADM phase | Identify new and changed requirements: remove, add, modify, re-assess priorities |
| 5 | Requirements Management | Identify changed requirements and record priorities; identify and manage conflicts; **generate the Requirements Impact Assessment** |
| 6 | ADM phase | Assess the impact of changed requirements on the current and previous phases; decide to implement or defer; issue Requirements Impact Assessment version n+1 |
| 7 | ADM phase | Implement requirements arising from Phase H |
| 8 | Requirements Management | Update the Architecture Requirements Repository, including the stakeholder views affected |
| 9 | ADM phase | Implement change in the current phase |
| 10 | ADM phase | Assess and revise gap analysis for past phases; a **gap requirement** is something eliminated by accident and needs a Target Architecture change |

## Outputs

(ADM §13.4)

| Output | Note |
|---|---|
| **Requirements Impact Assessment** | identifies the phases of the ADM that need to be revisited; iterates until a final version with full implications (costs, timescales, metrics) |
| Updated Architecture Requirements Specification | if necessary; updated once the cycle's requirements are finalized |

The Architecture Requirements Repository is updated as part of the process, but the standard
does not list it under outputs.

<figure class="my-4">
<svg viewBox="0 0 760 370" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="Requirements Management: a flat input list, ten steps split between the process and the running phase, and the Requirements Impact Assessment looping back as an input">
  <defs><marker id="arr-f4-19" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
  <text x="105" y="18" text-anchor="middle" font-size="12" font-weight="bold" fill="#345">Inputs (one flat list)</text><text x="655" y="18" text-anchor="middle" font-size="12" font-weight="bold" fill="#345">Outputs</text><text x="380" y="18" text-anchor="middle" font-size="12" font-weight="bold" fill="#345">Steps: who does which</text><rect x="230" y="34" width="300" height="278" rx="8" fill="#fff1d6" stroke="#e0b060"/><text x="380" y="52" text-anchor="middle" font-size="12" font-weight="bold">Requirements Management</text><rect x="238" y="62" width="38" height="13" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/><text x="257" y="72" text-anchor="middle" font-size="9">phase</text><text x="282" y="72" font-size="10.5">1 Identify requirements; document them</text><rect x="238" y="77" width="38" height="13" rx="6" fill="#f3e3f7" stroke="#b58ac9"/><text x="257" y="87" text-anchor="middle" font-size="9">RM</text><text x="282" y="87" font-size="10.5">2 Establish baseline requirements</text><rect x="238" y="92" width="38" height="13" rx="6" fill="#f3e3f7" stroke="#b58ac9"/><text x="257" y="102" text-anchor="middle" font-size="9">RM</text><text x="282" y="102" font-size="10.5">3 Monitor baseline requirements</text><rect x="238" y="107" width="38" height="13" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/><text x="257" y="117" text-anchor="middle" font-size="9">phase</text><text x="282" y="117" font-size="10.5">4 Identify new and changed requirements</text><rect x="238" y="122" width="38" height="13" rx="6" fill="#f3e3f7" stroke="#b58ac9"/><text x="257" y="132" text-anchor="middle" font-size="9">RM</text><text x="282" y="132" font-size="10.5">5 Record changes; generate the Impact Assessment</text><rect x="238" y="137" width="38" height="13" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/><text x="257" y="147" text-anchor="middle" font-size="9">phase</text><text x="282" y="147" font-size="10.5">6 Assess impact; decide to implement or defer</text><rect x="238" y="152" width="38" height="13" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/><text x="257" y="162" text-anchor="middle" font-size="9">phase</text><text x="282" y="162" font-size="10.5">7 Implement requirements arising from Phase H</text><rect x="238" y="167" width="38" height="13" rx="6" fill="#f3e3f7" stroke="#b58ac9"/><text x="257" y="177" text-anchor="middle" font-size="9">RM</text><text x="282" y="177" font-size="10.5">8 Update the Requirements Repository</text><rect x="238" y="182" width="38" height="13" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/><text x="257" y="192" text-anchor="middle" font-size="9">phase</text><text x="282" y="192" font-size="10.5">9 Implement change in the current phase</text><rect x="238" y="197" width="38" height="13" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/><text x="257" y="207" text-anchor="middle" font-size="9">phase</text><text x="282" y="207" font-size="10.5">10 Revise gap analysis for past phases</text><rect x="240" y="282" width="12" height="12" rx="4" fill="#f3e3f7" stroke="#b58ac9"/><text x="257" y="292" font-size="10">the process itself</text><rect x="380" y="282" width="12" height="12" rx="4" fill="#e3f5e1" stroke="#7fbf7a"/><text x="397" y="292" font-size="10">the ADM phase running</text><rect x="10" y="34" width="190" height="46" rx="6" fill="#e0ecff" stroke="#7aa2e3"/><text x="105" y="61" text-anchor="middle" font-size="10.5">Populated Architecture Repository</text><line x1="200" y1="57" x2="228" y2="57" stroke="#555" marker-end="url(#arr-f4-19)"/><rect x="10" y="92" width="190" height="46" rx="6" fill="#e0ecff" stroke="#7aa2e3"/><text x="105" y="112.5" text-anchor="middle" font-size="10.5">Organizational Model for EA;</text><text x="105" y="125.5" text-anchor="middle" font-size="10.5">Tailored Architecture Framework</text><line x1="200" y1="115" x2="228" y2="115" stroke="#555" marker-end="url(#arr-f4-19)"/><rect x="10" y="150" width="190" height="46" rx="6" fill="#e0ecff" stroke="#7aa2e3"/><text x="105" y="170.5" text-anchor="middle" font-size="10.5">Statement of Architecture Work;</text><text x="105" y="183.5" text-anchor="middle" font-size="10.5">Architecture Vision</text><line x1="200" y1="173" x2="228" y2="173" stroke="#555" marker-end="url(#arr-f4-19)"/><rect x="10" y="208" width="190" height="46" rx="6" fill="#e0ecff" stroke="#7aa2e3"/><text x="105" y="222" text-anchor="middle" font-size="10.5">Architecture requirements populating</text><text x="105" y="235" text-anchor="middle" font-size="10.5">an Architecture Requirements</text><text x="105" y="248" text-anchor="middle" font-size="10.5">Specification</text><line x1="200" y1="231" x2="228" y2="231" stroke="#555" marker-end="url(#arr-f4-19)"/><rect x="10" y="266" width="190" height="46" rx="6" fill="#e0ecff" stroke="#7aa2e3"/><text x="105" y="286.5" text-anchor="middle" font-size="10.5">Requirements Impact Assessment</text><text x="105" y="299.5" text-anchor="middle" font-size="10.5">(the previous version)</text><line x1="200" y1="289" x2="228" y2="289" stroke="#555" marker-end="url(#arr-f4-19)"/><rect x="560" y="92" width="190" height="46" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/><text x="655" y="112.5" text-anchor="middle" font-size="10.5">Requirements Impact Assessment:</text><text x="655" y="125.5" text-anchor="middle" font-size="10.5">the ADM phases to revisit</text><rect x="711" y="84" width="35" height="15" rx="7" fill="#f3e3f7" stroke="#b58ac9"/><text x="728.5" y="95" text-anchor="middle" font-size="9.5" fill="#5b2d6e">first</text><line x1="530" y1="115" x2="558" y2="115" stroke="#555" marker-end="url(#arr-f4-19)"/><rect x="560" y="150" width="190" height="46" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/><text x="655" y="170.5" text-anchor="middle" font-size="10.5">Architecture Requirements</text><text x="655" y="183.5" text-anchor="middle" font-size="10.5">Specification, updated if necessary</text><line x1="530" y1="173" x2="558" y2="173" stroke="#555" marker-end="url(#arr-f4-19)"/><rect x="560" y="208" width="190" height="46" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/><text x="655" y="222" text-anchor="middle" font-size="10.5">Architecture Requirements Repository</text><text x="655" y="235" text-anchor="middle" font-size="10.5">updated as part of the process,</text><text x="655" y="248" text-anchor="middle" font-size="10.5">not listed as an output</text><line x1="530" y1="231" x2="558" y2="231" stroke="#555" marker-end="url(#arr-f4-19)"/><path d="M750 115 L756 115 L756 326 L4 326 L4 289 L8 289" fill="none" stroke="#c0392b" stroke-dasharray="5 4" marker-end="url(#arr-f4-19)"/><text x="380" y="340" text-anchor="middle" font-size="10.5" fill="#c0392b">the Impact Assessment iterates: each pass issues version n+1 and returns as an input (ADM §13.2, ADM §13.4)</text><text x="380" y="360" text-anchor="middle" font-size="11" fill="#666">The process never disposes of, addresses or prioritizes a requirement — the phase does (ADM §13.5.1)</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">Requirements Management: inputs, the two-column steps and outputs, with the iterating Impact Assessment. Original drawing; inputs and outputs per ADM §13.2 and ADM §13.4, steps per ADM §13.3.</figcaption>
</figure>

> **Trap.** Two things Requirements Management does *not* do: it does not dispose of, address or
> prioritize requirements (the phase does), and it is not a step in the sequence A to H (it runs
> alongside all of them, including the Preliminary Phase). Options that make it "the phase after
> H" or "the phase that decides which requirements to implement" are wrong.

> **Trap.** The Requirements Impact Assessment is both an *input* and an *output* — it comes back
> in each iteration. Do not confuse it with the Architecture Requirements *Specification* (a
> Phase B to F deliverable) or the Architecture Requirements *Repository* (holds many cycles).

<!-- figures:start -->
## Figures from the standard

The diagrams the cited sections carry, from your local copy of the publication. The exam reproduces these; know what each box is.

<div class="grid gap-4 md:grid-cols-2">
<figure class="max-w-lg"><img src="/figure/ADM:fig-13-1" alt="Figure 13-1: ADM Architecture Requirements" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 13-1: ADM Architecture Requirements (ADM)</figcaption></figure>
</div>
<!-- figures:end -->

## Check yourself

1. Which document identifies the ADM phases that must be revisited?
2. What can the Architecture Requirements Repository hold that the Specification cannot?
3. Which of the ten steps does the Requirements Management process itself perform?
4. Where do the first high-level requirements come from?
