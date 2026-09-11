---
title: The ADM techniques and where each is used
unit: F5
objectives: ["5.1", "5.2", "5.3", "5.4", "5.5"]
refs: ["TECH §2", "TECH §3", "TECH §4", "TECH §5", "TECH §6", "TECH §7", "TECH §8", "TECH §9", "GUIDE:business-scenarios §1", "GUIDE:business-capability-planning §6", "ADM §9.3", "ADM §10.3"]
reading_minutes: 10
source: authored
status: draft
---
## Principles (TECH §2)

A principle has a **name**, a **statement**, a **rationale** and **implications**. A good set
of principles is *understandable, robust, complete, consistent and stable*. Established in
the Preliminary Phase, confirmed in Phase A, and used to evaluate every later decision.

## Stakeholder Management (TECH §3)

Identify stakeholders, classify them on the **power/interest grid** (Key Players; Keep
Satisfied; Keep Informed; Minimal Effort), record concerns and the views each needs in the
**Stakeholder Map Matrix**, and plan communication. Done early in Phase A.

## Business Scenarios (GUIDE:business-scenarios §1 — a Series Guide, not in TECH)

A structured way to discover business requirements: the problem, the business and technical
environment, the desired outcome, the human and computer actors and their roles. A good
scenario is **SMART**: specific, measurable, actionable, realistic, time-bound.

## Gap Analysis (TECH §5)

A matrix with Baseline ABBs down the side and Target ABBs across the top, plus an
*Eliminated* column and a *New* row, so that every baseline element is either carried forward
or deliberately eliminated and every new element is visible. Used as a step in B, C and D.

## Migration planning techniques (ADM §9.3 and §10.3)

| Technique | Phase |
|---|---|
| Implementation Factor Catalog | E |
| Consolidated Gaps, Solutions and Dependencies Matrix | E |
| Architecture Definition Increments Table | F |
| Transition Architecture State Evolution Table | F |
| Business Value Assessment | F |

## Readiness, risk, interoperability, capability-based planning

**Business Transformation Readiness Assessment** (TECH §7) rates readiness factors for
urgency, readiness status and difficulty to fix in Phase A; results feed Phase E. **Risk Management** (TECH §8)
distinguishes the *initial* level of risk from the *residual* level after mitigation.
**Interoperability requirements** (TECH §6) are defined across phases and reconciled in Phase
E. **Business Capability Planning** (GUIDE:business-capability-planning §6 — a Series Guide) plans strategic business capabilities delivered
as increments through Transition Architectures.

<figure class="my-4">
<svg viewBox="0 0 760 330" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="The ADM techniques placed along the phases: principles and stakeholders in the Preliminary Phase and A, gap analysis in B to D, readiness, interoperability and migration planning converging on E and F, monitoring in G">
<defs><marker id="arr-f5-01" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
<rect x="160" y="18" width="62" height="28" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="191.0" y="36.2" text-anchor="middle" font-size="12" font-weight="bold">Prelim</text>
<rect x="226" y="18" width="62" height="28" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="257.0" y="36.2" text-anchor="middle" font-size="12" font-weight="bold">A</text>
<rect x="292" y="18" width="62" height="28" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="323.0" y="36.2" text-anchor="middle" font-size="12" font-weight="bold">B</text>
<rect x="358" y="18" width="62" height="28" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="389.0" y="36.2" text-anchor="middle" font-size="12" font-weight="bold">C</text>
<rect x="424" y="18" width="62" height="28" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="455.0" y="36.2" text-anchor="middle" font-size="12" font-weight="bold">D</text>
<rect x="490" y="18" width="62" height="28" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="521.0" y="36.2" text-anchor="middle" font-size="12" font-weight="bold">E</text>
<rect x="556" y="18" width="62" height="28" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="587.0" y="36.2" text-anchor="middle" font-size="12" font-weight="bold">F</text>
<rect x="622" y="18" width="62" height="28" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="653.0" y="36.2" text-anchor="middle" font-size="12" font-weight="bold">G</text>
<rect x="688" y="18" width="62" height="28" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="719.0" y="36.2" text-anchor="middle" font-size="12" font-weight="bold">H</text>
<text x="150" y="81" text-anchor="end" font-size="11" fill="#222">Principles</text>
<rect x="160" y="66" width="128" height="22" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="224.0" y="80.5" text-anchor="middle" font-size="10">set → confirmed</text>
<line x1="294" y1="77" x2="750" y2="77" stroke="#999" stroke-dasharray="4 3" marker-end="url(#arr-f5-01)"/>
<text x="520" y="73" text-anchor="middle" font-size="10" fill="#666">used to evaluate every later decision</text>
<text x="150" y="111" text-anchor="end" font-size="11" fill="#222">Stakeholder Management</text>
<rect x="226" y="96" width="62" height="22" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="257.0" y="110.5" text-anchor="middle" font-size="10">grid, map</text>
<line x1="294" y1="107" x2="750" y2="107" stroke="#999" stroke-dasharray="4 3" marker-end="url(#arr-f5-01)"/>
<text x="520" y="103" text-anchor="middle" font-size="10" fill="#666">updated in every later phase</text>
<text x="150" y="141" text-anchor="end" font-size="11" fill="#222">Business Scenarios</text>
<rect x="160" y="126" width="194" height="22" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="257.0" y="140.5" text-anchor="middle" font-size="10">SMART requirements</text>
<text x="150" y="171" text-anchor="end" font-size="11" fill="#222">Gap Analysis</text>
<rect x="292" y="156" width="194" height="22" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="389.0" y="170.5" text-anchor="middle" font-size="10">a step in each of B, C, D</text>
<rect x="490" y="156" width="62" height="22" rx="6" fill="#fff1d6" stroke="#e0b060"/>
<text x="521.0" y="170.5" text-anchor="middle" font-size="10">consolidate</text>
<text x="150" y="201" text-anchor="end" font-size="11" fill="#222">Readiness and Risk</text>
<rect x="226" y="186" width="62" height="22" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="257.0" y="200.5" text-anchor="middle" font-size="10">assess</text>
<rect x="490" y="186" width="128" height="22" rx="6" fill="#fff1d6" stroke="#e0b060"/>
<text x="554.0" y="200.5" text-anchor="middle" font-size="10">into the Migration Plan</text>
<rect x="622" y="186" width="62" height="22" rx="6" fill="#f3e3f7" stroke="#b58ac9"/>
<text x="653.0" y="200.5" text-anchor="middle" font-size="10">monitor</text>
<text x="150" y="231" text-anchor="end" font-size="11" fill="#222">Interoperability</text>
<rect x="226" y="216" width="260" height="22" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="356.0" y="230.5" text-anchor="middle" font-size="10">revealed → defined, phase by phase</text>
<rect x="490" y="216" width="62" height="22" rx="6" fill="#fff1d6" stroke="#e0b060"/>
<text x="521.0" y="230.5" text-anchor="middle" font-size="10">reconcile</text>
<text x="150" y="261" text-anchor="end" font-size="11" fill="#222">Migration planning</text>
<rect x="490" y="246" width="128" height="22" rx="6" fill="#fff1d6" stroke="#e0b060"/>
<text x="554.0" y="260.5" text-anchor="middle" font-size="10">two in E, three in F</text>
<text x="150" y="291" text-anchor="end" font-size="11" fill="#222">Capability planning</text>
<rect x="490" y="276" width="128" height="22" rx="6" fill="#fff1d6" stroke="#e0b060"/>
<text x="554.0" y="290.5" text-anchor="middle" font-size="10">via Transition Architectures</text>
<line x1="290" y1="197" x2="488" y2="197" stroke="#999" marker-end="url(#arr-f5-01)"/>
<text x="380" y="318" text-anchor="middle" font-size="11" fill="#666">Where each technique from this unit does its work along the ADM; E is where results converge</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">The techniques of this unit placed on the phases where they are used. Original drawing; placement per TECH §2, §3, §5, §6, §7 and §8, and ADM §9.3 and §10.3.</figcaption>
</figure>
