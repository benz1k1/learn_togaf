---
title: Stakeholder Management — identify, classify, decide the approach, tailor the deliverables
unit: F5
objectives: ["5.2"]
refs: ["TECH §3.1", "TECH §3.2", "TECH §3.3", "TECH §3.3.1", "TECH §3.3.2", "TECH §3.3.3", "TECH §3.3.4", "TECH §3.4", "ADM §3.3.2"]
reading_minutes: 9
source: authored
status: draft
---
## Why the technique exists

Stakeholder management is how practitioners win support so that the engagement succeeds. Its
benefits: the most powerful stakeholders are found early and their input shapes the architecture;
their backing brings resources; early and frequent communication builds understanding of the
architecture process; likely reactions can be anticipated and planned for; and conflicting
objectives between stakeholders surface early enough to resolve. Every initiative should identify
who contributes, who gains, who loses, and then decide how to deal with each (TECH §3.1).

## When it is done

Stakeholder analysis is used during **Phase A** to identify the key players and is **updated in
every later phase** — new stakeholders tend to appear as work moves into Opportunities &
Solutions, Migration Planning and Architecture Change Management. Just as a building architect
draws wiring diagrams and floor plans for different audiences, the enterprise architect creates
different architecture views for stakeholders with different concerns. The standard supports this
through four concepts: architecture view, architecture viewpoint, concern and stakeholder
(TECH §3.2).

In the ADM, the Phase A step "Identify Stakeholders, Concerns, and Business Requirements" produces
the **stakeholder map** for the engagement — who is involved, how deeply, and their key concerns —
which then feeds the Architecture Vision (relevant concerns and viewpoints), the Communications
Plan (who to communicate with) and the Statement of Architecture Work (roles and responsibilities)
(ADM §3.3.2).

## The four steps

| Step | What happens |
|---|---|
| 1. Identify stakeholders | Work out who is affected, who has power over the work and who has an interest in its outcome |
| 2. Classify stakeholder positions | Record understanding, commitment and readiness to support, per stakeholder |
| 3. Determine stakeholder management approach | Place stakeholders on the power/interest grid to choose the engagement strategy |
| 4. Tailor engagement deliverables | Decide which catalogs, matrices and diagrams each stakeholder group needs |

(TECH §3.3)

<figure class="my-4">
<svg viewBox="0 0 760 212" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="The four stakeholder management steps produce the stakeholder map, which feeds the Architecture Vision, the Communications Plan and the Statement of Architecture Work">
<defs><marker id="arr-f5-11a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
<rect x="15" y="15" width="170" height="54" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="100.0" y="31.9" text-anchor="middle" font-size="11" font-weight="bold">1 Identify</text>
<text x="100.0" y="45.9" text-anchor="middle" font-size="11">who is affected, has power,</text>
<text x="100.0" y="59.9" text-anchor="middle" font-size="11">has an interest</text>
<line x1="185" y1="42" x2="200" y2="42" stroke="#555" marker-end="url(#arr-f5-11a)"/>
<rect x="200" y="15" width="170" height="54" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="285.0" y="31.9" text-anchor="middle" font-size="11" font-weight="bold">2 Classify positions</text>
<text x="285.0" y="45.9" text-anchor="middle" font-size="11">understanding, commitment,</text>
<text x="285.0" y="59.9" text-anchor="middle" font-size="11">readiness to support</text>
<line x1="370" y1="42" x2="385" y2="42" stroke="#555" marker-end="url(#arr-f5-11a)"/>
<rect x="385" y="15" width="170" height="54" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="470.0" y="31.9" text-anchor="middle" font-size="11" font-weight="bold">3 Determine approach</text>
<text x="470.0" y="45.9" text-anchor="middle" font-size="11">place on the</text>
<text x="470.0" y="59.9" text-anchor="middle" font-size="11">power / interest grid</text>
<line x1="555" y1="42" x2="570" y2="42" stroke="#555" marker-end="url(#arr-f5-11a)"/>
<rect x="570" y="15" width="170" height="54" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="655.0" y="31.9" text-anchor="middle" font-size="11" font-weight="bold">4 Tailor deliverables</text>
<text x="655.0" y="45.9" text-anchor="middle" font-size="11">catalogs, matrices, diagrams</text>
<text x="655.0" y="59.9" text-anchor="middle" font-size="11">per stakeholder group</text>
<path d="M100 69 L100 84 L380 84" fill="none" stroke="#555"/>
<path d="M655 69 L655 84 L380 84 L380 96" fill="none" stroke="#555" marker-end="url(#arr-f5-11a)"/>
<rect x="230" y="98" width="300" height="30" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/>
<text x="380.0" y="116.8" text-anchor="middle" font-size="11" font-weight="bold">Stakeholder Map — the Phase A step's output</text>
<line x1="380" y1="128" x2="127" y2="158" stroke="#555" marker-end="url(#arr-f5-11a)"/>
<rect x="15" y="160" width="225" height="40" rx="6" fill="#fff" stroke="#666"/>
<text x="127.5" y="176.8" text-anchor="middle" font-size="11" font-weight="bold">Architecture Vision</text>
<text x="127.5" y="190.8" text-anchor="middle" font-size="11">relevant concerns and viewpoints</text>
<line x1="380" y1="128" x2="382" y2="158" stroke="#555" marker-end="url(#arr-f5-11a)"/>
<rect x="270" y="160" width="225" height="40" rx="6" fill="#fff" stroke="#666"/>
<text x="382.5" y="176.8" text-anchor="middle" font-size="11" font-weight="bold">Communications Plan</text>
<text x="382.5" y="190.8" text-anchor="middle" font-size="11">who to communicate with</text>
<line x1="380" y1="128" x2="637" y2="158" stroke="#555" marker-end="url(#arr-f5-11a)"/>
<rect x="525" y="160" width="225" height="40" rx="6" fill="#fff" stroke="#666"/>
<text x="637.5" y="176.8" text-anchor="middle" font-size="11" font-weight="bold">Statement of Architecture Work</text>
<text x="637.5" y="190.8" text-anchor="middle" font-size="11">roles and responsibilities</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">Four steps in, three deliverables out. Original drawing; steps per TECH §3.3, downstream use per ADM §3.3.2.</figcaption>
</figure>

### 1. Identify

Think about everyone affected by, influential over, or interested in the Enterprise Architecture:
executives, project and client roles, developers, partners, suppliers, IT operations, customers.
Do not lean only on the formal organisation chart — informal groups can be just as powerful, and
influencers may hold no formal position. Stakeholders can be organisations or people, but in the
end the team communicates with individuals, so name the right individual in each stakeholder
organisation. A sample analysis distinguishes **22 stakeholder types in five categories**, and
the analysis should cover both the *visible* team (obviously involved) and the *invisible* team
(support providers who must contribute for success) (TECH §3.3.1).

### 2. Classify positions

Record, for the most important stakeholders, their ability to disrupt the change, current and
required understanding, current and required commitment, and required support. Also judge each
person's readiness to act supportively: are they ready to move towards the target, can they be a
credible advocate, how involved do they need to be, and have they made a contractual commitment?
For those whose commitment is critical, note current and desired levels (TECH §3.3.2).

### 3. Determine the approach — the power/interest grid

Work out each stakeholder's power, influence and interest and place them on a **power / level of
interest** matrix, which also indicates the engagement strategy for each quadrant (TECH §3.3.3).

| | Low interest | High interest |
|---|---|---|
| **High power** | Keep Satisfied | **Key Players** |
| **Low power** | Minimal Effort | Keep Informed |

(TECH §3.3.3, Figure 3-2)

> **Trap.** Exam questions swap the axes. Power is the vertical axis, interest the horizontal.
> High power + low interest = *Keep Satisfied*; low power + high interest = *Keep Informed*.
> Only high/high are *Key Players* (TECH §3.3.3).

<figure class="my-4">
<svg viewBox="0 0 760 300" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="The power and interest grid as a two by two: power up the vertical axis, interest along the horizontal; Key Players top right, Keep Satisfied top left, Keep Informed bottom right, Minimal Effort bottom left">
<defs><marker id="arr-f5-11b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
<rect x="130" y="30" width="285.0" height="110.0" fill="#fff1d6" stroke="#e0b060"/>
<text x="272.5" y="81.0" text-anchor="middle" font-size="14" fill="#222" font-weight="bold">Keep Satisfied</text>
<text x="272.5" y="101.0" text-anchor="middle" font-size="11" fill="#555">high power · low interest</text>
<rect x="415.0" y="30" width="285.0" height="110.0" fill="#e3f5e1" stroke="#7fbf7a"/>
<text x="557.5" y="81.0" text-anchor="middle" font-size="14" fill="#222" font-weight="bold">Key Players</text>
<text x="557.5" y="101.0" text-anchor="middle" font-size="11" fill="#555">high power · high interest</text>
<rect x="130" y="140.0" width="285.0" height="110.0" fill="#f1f1f1" stroke="#999"/>
<text x="272.5" y="191.0" text-anchor="middle" font-size="14" fill="#222" font-weight="bold">Minimal Effort</text>
<text x="272.5" y="211.0" text-anchor="middle" font-size="11" fill="#555">low power · low interest</text>
<rect x="415.0" y="140.0" width="285.0" height="110.0" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="557.5" y="191.0" text-anchor="middle" font-size="14" fill="#222" font-weight="bold">Keep Informed</text>
<text x="557.5" y="211.0" text-anchor="middle" font-size="11" fill="#555">low power · high interest</text>
<line x1="105" y1="250" x2="105" y2="22" stroke="#555" marker-end="url(#arr-f5-11b)"/>
<text x="60" y="144.0" text-anchor="middle" font-size="12" fill="#222" font-weight="bold" transform="rotate(-90 60 144.0)">Power</text>
<text x="95" y="44" text-anchor="end" font-size="10" fill="#666">high</text>
<text x="95" y="246" text-anchor="end" font-size="10" fill="#666">low</text>
<line x1="130" y1="268" x2="708" y2="268" stroke="#555" marker-end="url(#arr-f5-11b)"/>
<text x="415.0" y="292" text-anchor="middle" font-size="12" fill="#222" font-weight="bold">Level of interest</text>
<text x="134" y="282" text-anchor="start" font-size="10" fill="#666">low</text>
<text x="696" y="282" text-anchor="end" font-size="10" fill="#666">high</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">The four quadrants, with power vertical and interest horizontal. Original drawing; quadrants per TECH §3.3.3.</figcaption>
</figure>

### 4. Tailor engagement deliverables

Identify the catalogs, matrices and diagrams the engagement must produce and validate with each
stakeholder group, so the architecture can be communicated to, and understood by, every
stakeholder, and each can confirm that their concerns are addressed (TECH §3.3.4).

## The template stakeholder map

The stakeholder map is a table with four columns: **stakeholder**, **key concerns**, **class**
(the grid quadrant, e.g. KEEP SATISFIED, KEY PLAYERS, KEEP INFORMED) and the **catalogs, matrices
and diagrams** that address those concerns. For example, CxOs are concerned with high-level
drivers, goals and objectives and are classed Keep Satisfied; Enterprise Security is a Key Player
concerned with access and tamper protection and is served by Data Security and Network diagrams;
Regulatory Bodies are Keep Satisfied and need the Business Footprint and Application Communication
diagrams (TECH §3.4).

<!-- figures:start -->
## Figures from the standard

The diagrams the cited sections carry, from your local copy of the publication. The exam reproduces these; know what each box is.

<div class="grid gap-4 md:grid-cols-2">
<figure class="max-w-lg"><img src="/figure/TECH:fig-3-1" alt="Figure 3-1: Sample Stakeholders and Categories" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 3-1: Sample Stakeholders and Categories (TECH)</figcaption></figure>
<figure class="max-w-lg"><img src="/figure/TECH:fig-3-2" alt="Figure 3-2: Stakeholder Power Grid" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 3-2: Stakeholder Power Grid (TECH)</figcaption></figure>
</div>
<!-- figures:end -->

## Check yourself

- Which phase first produces the stakeholder map, and what three outputs does it feed?
- What are the four columns of the template stakeholder map?
- Which quadrant holds a stakeholder with high power but little interest?
