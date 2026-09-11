---
title: Phase A in practice, open book
unit: P3
objectives: ["P3.1", "P3.2"]
refs: ["ADM §3", "TECH §3", "TECH §5", "TECH §9", "TECH §8"]
reading_minutes: 8
source: authored
status: draft
---
## What a Phase A scenario looks like

A Practitioner scenario plants a sponsor, a conflicting set of stakeholders, a constraint or
two (a regulator, a budget holder who has not been consulted), and asks what you do first. The
five-point answer walks Phase A **in order** and names the technique for each planted fact:

1. Establish the project and **identify stakeholders and concerns** (Stakeholder Management):
   the answer must name the stakeholder the scenario left out.
2. Capture the business problem with a **business scenario** when the stakeholders disagree
   about what the problem is.
3. **Assess readiness** and **identify risks** when the scenario mentions culture, capacity or
   a hard deadline.
4. Define scope, confirm principles, write the **Architecture Vision**, and produce the
   **Statement of Architecture Work** for the sponsor's approval.

The three-point answer usually has the right deliverables but skips the stakeholder or
scenario step. The one-point answer starts in Phase B. The zero-point answer takes one
stakeholder's demand as the requirement.

<figure class="my-4">
<svg viewBox="0 0 760 344" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="The Phase A scenario as a decision path: taking one stakeholder's demand scores zero, starting in Phase B scores one, skipping the stakeholder or scenario step scores three, walking Phase A in order scores five">
<defs><marker id="arr-p3" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
<rect x="15" y="12" width="730" height="32" rx="6" fill="#f1f1f1" stroke="#999"/>
<text x="380.0" y="31.5" text-anchor="middle" font-size="10">Scenario: a sponsor, stakeholders who disagree, a planted constraint (a regulator, an unconsulted budget holder, a deadline)</text>
<line x1="300" y1="44" x2="300" y2="66" stroke="#555" marker-end="url(#arr-p3)"/>
<rect x="15" y="68" width="570" height="44" rx="6" fill="#fff" stroke="#666"/>
<text x="300.0" y="93.8" text-anchor="middle" font-size="11">Do you take one stakeholder's demand as the requirement?</text>
<line x1="585" y1="90" x2="615" y2="90" stroke="#555" marker-end="url(#arr-p3)"/>
<text x="600" y="84" text-anchor="middle" font-size="10" fill="#c0392b">yes</text>
<rect x="617" y="66" width="128" height="48" rx="6" fill="#fde8e6" stroke="#c0392b"/>
<text x="681.0" y="80.5" text-anchor="middle" font-size="10" font-weight="bold">0 points</text>
<text x="681.0" y="93.5" text-anchor="middle" font-size="10">one voice is not</text>
<text x="681.0" y="106.5" text-anchor="middle" font-size="10">a requirement</text>
<line x1="300" y1="112" x2="300" y2="138" stroke="#555" marker-end="url(#arr-p3)"/>
<text x="308" y="130" text-anchor="start" font-size="10" fill="#3a7d3a">no</text>
<rect x="15" y="140" width="570" height="44" rx="6" fill="#fff" stroke="#666"/>
<text x="300.0" y="165.8" text-anchor="middle" font-size="11">Do you start in Phase A — or jump to Phase B?</text>
<line x1="585" y1="162" x2="615" y2="162" stroke="#555" marker-end="url(#arr-p3)"/>
<text x="600" y="156" text-anchor="middle" font-size="10" fill="#c0392b">B</text>
<rect x="617" y="138" width="128" height="48" rx="6" fill="#fff1d6" stroke="#e0b060"/>
<text x="681.0" y="159.0" text-anchor="middle" font-size="10" font-weight="bold">1 point</text>
<text x="681.0" y="172.0" text-anchor="middle" font-size="10">started in the wrong phase</text>
<line x1="300" y1="184" x2="300" y2="210" stroke="#555" marker-end="url(#arr-p3)"/>
<text x="308" y="202" text-anchor="start" font-size="10" fill="#3a7d3a">A</text>
<rect x="15" y="212" width="570" height="44" rx="6" fill="#fff" stroke="#666"/>
<text x="300.0" y="230.8" text-anchor="middle" font-size="11">Do you name the left-out stakeholder, and use a business scenario, readiness and risk</text>
<text x="300.0" y="244.8" text-anchor="middle" font-size="11">for the planted facts?</text>
<line x1="585" y1="234" x2="615" y2="234" stroke="#555" marker-end="url(#arr-p3)"/>
<text x="600" y="228" text-anchor="middle" font-size="10" fill="#c0392b">no</text>
<rect x="617" y="210" width="128" height="48" rx="6" fill="#fff1d6" stroke="#e0b060"/>
<text x="681.0" y="224.5" text-anchor="middle" font-size="10" font-weight="bold">3 points</text>
<text x="681.0" y="237.5" text-anchor="middle" font-size="10">right deliverables,</text>
<text x="681.0" y="250.5" text-anchor="middle" font-size="10">a step skipped</text>
<line x1="300" y1="256" x2="300" y2="282" stroke="#555" marker-end="url(#arr-p3)"/>
<text x="308" y="274" text-anchor="start" font-size="10" fill="#3a7d3a">yes</text>
<rect x="15" y="286" width="730" height="46" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/>
<text x="380.0" y="306.0" text-anchor="middle" font-size="10" font-weight="bold">5 points — Phase A in order</text>
<text x="380.0" y="319.0" text-anchor="middle" font-size="10">stakeholders and concerns → business scenario → readiness and risk → scope, principles, Architecture Vision, Statement of Architecture Work</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">The scoring as a decision path: each wrong turn drops off to the right. Original drawing; the Phase A order follows ADM §3.3, the techniques TECH §3, §7 and §8.</figcaption>
</figure>

## Where to look in the book

ADM §3 (Phase A: objectives, approach, steps, outputs); ADM Techniques §3 (stakeholder map,
power/interest grid), §5 (business scenarios), §9 (readiness), §10 (risk). In the exam, search
the section headings first; the answer's wording tracks the step names.
