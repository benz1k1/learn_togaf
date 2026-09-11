---
title: Phases B to H and Requirements Management
unit: F4
objectives: ["4.3", "4.4", "4.5", "4.6", "4.7"]
refs: ["ADM §4", "ADM §5", "ADM §8", "ADM §9", "ADM §10", "ADM §11", "ADM §12", "ADM §13"]
reading_minutes: 12
source: authored
status: draft
---
## B, C, D: the same nine steps three times

Each development phase runs the same sequence: select reference models, viewpoints and tools;
describe the **Baseline**; describe the **Target**; **gap analysis**; define **candidate
roadmap components**; resolve impacts across the Landscape; formal stakeholder review;
finalise the architecture; create (add to) the **Architecture Definition Document**. Each phase
outputs a draft Architecture Definition Document, a draft **Architecture Requirements
Specification** with the gap results, and its domain's components of the Architecture Roadmap.

Phase C is *one* phase with two parts, Data and Application, developed in either order.

## E and F: from gaps to a plan

**Phase E** is the first phase concerned with implementation. It consolidates the gaps and
candidate components from B, C and D, groups them into **work packages**, decides whether
**Transition Architectures** are needed, and produces the **Architecture Roadmap** and an
*outline* Implementation and Migration Plan. Techniques: Implementation Factor Catalog,
Consolidated Gaps, Solutions and Dependencies Matrix.

**Phase F** finalises. It assigns **business value** to each work package, estimates resources
and timing, prioritises by cost/benefit and risk, confirms the Roadmap, completes the
**Implementation and Migration Plan**, produces the **Implementation Governance Model**, and
closes the development cycle with lessons learned. Techniques: Architecture Definition
Increments Table, Transition Architecture State Evolution Table, Business Value Assessment.

## G and H: governing and living with the architecture

**Phase G** is where the architecture and the solution meet. The **Architecture Contract** is
signed with the implementing organisation, development is guided, **compliance reviews** are
performed, and change requests arising from implementation are handled. Outputs: the signed
contract, Compliance Assessments, Change Requests, and an architecture-compliant deployed
solution.

**Phase H** keeps the architecture alive. It monitors business and technology change, runs a
value-realisation process, and classifies every change request as a **simplification**, an
**incremental** change, or a **re-architecting** change. Only re-architecting change starts a
new ADM cycle, through a new Request for Architecture Work.

## Requirements Management

Not a phase in the sequence but the process at the centre: it identifies, baselines, monitors
and stores requirements in the **Architecture Requirements Repository**, assesses the impact
of changes (the **Requirements Impact Assessment** names the phases to revisit), and feeds the
current set to every phase. The *disposal* of a requirement is done by the phase, not by the
process.

<figure class="my-4">
<svg viewBox="0 0 760 444" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="Phases B to H grouped as develop, deliver and govern around the ring, with Requirements Management in the centre">
  <defs><marker id="arr-f4-02" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
  <path d="M455.5 112.9 A232 145 0 0 1 502.9 127.0" fill="none" stroke="#555" marker-end="url(#arr-f4-02)"/><path d="M571.2 167.9 A232 145 0 0 1 609.7 229.8" fill="none" stroke="#555" marker-end="url(#arr-f4-02)"/><path d="M609.7 270.2 A232 145 0 0 1 571.2 332.1" fill="none" stroke="#555" marker-end="url(#arr-f4-02)"/><path d="M502.9 373.0 A232 145 0 0 1 455.5 387.1" fill="none" stroke="#555" marker-end="url(#arr-f4-02)"/><path d="M304.5 387.1 A232 145 0 0 1 257.1 373.0" fill="none" stroke="#555" marker-end="url(#arr-f4-02)"/><path d="M188.8 332.1 A232 145 0 0 1 150.3 270.2" fill="none" stroke="#555" marker-end="url(#arr-f4-02)"/><path d="M150.3 229.8 A232 145 0 0 1 188.8 167.9" fill="none" stroke="#555" marker-end="url(#arr-f4-02)"/><path d="M257.1 127.0 A232 145 0 0 1 304.5 112.9" fill="none" stroke="#c0392b" stroke-dasharray="5 4" marker-end="url(#arr-f4-02)"/><rect x="308" y="88" width="144" height="34" rx="6" fill="#f4f4f4" stroke="#999"/><text x="380" y="102.5" text-anchor="middle" font-size="10.5">Phase A</text><text x="380" y="115.5" text-anchor="middle" font-size="10.5">Architecture Vision</text><rect x="472.049" y="130.47" width="144" height="34" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/><text x="544.049" y="144.97" text-anchor="middle" font-size="10.5" font-weight="bold">Phase B</text><text x="544.049" y="157.97" text-anchor="middle" font-size="10.5" font-weight="bold">Business Architecture</text><rect x="540" y="233" width="144" height="34" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/><text x="612" y="247.5" text-anchor="middle" font-size="10.5" font-weight="bold">Phase C</text><text x="612" y="260.5" text-anchor="middle" font-size="10.5" font-weight="bold">Information Systems</text><rect x="472.049" y="335.53" width="144" height="34" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/><text x="544.049" y="350.03" text-anchor="middle" font-size="10.5" font-weight="bold">Phase D</text><text x="544.049" y="363.03" text-anchor="middle" font-size="10.5" font-weight="bold">Technology Architecture</text><rect x="308" y="378" width="144" height="34" rx="6" fill="#e0ecff" stroke="#7aa2e3"/><text x="380" y="392.5" text-anchor="middle" font-size="10.5" font-weight="bold">Phase E</text><text x="380" y="405.5" text-anchor="middle" font-size="10.5" font-weight="bold">Opportunities and Solutions</text><rect x="143.951" y="335.53" width="144" height="34" rx="6" fill="#e0ecff" stroke="#7aa2e3"/><text x="215.951" y="350.03" text-anchor="middle" font-size="10.5" font-weight="bold">Phase F</text><text x="215.951" y="363.03" text-anchor="middle" font-size="10.5" font-weight="bold">Migration Planning</text><rect x="76" y="233" width="144" height="34" rx="6" fill="#f3e3f7" stroke="#b58ac9"/><text x="148" y="247.5" text-anchor="middle" font-size="10.5" font-weight="bold">Phase G</text><text x="148" y="260.5" text-anchor="middle" font-size="10.5" font-weight="bold">Implementation Governance</text><rect x="143.951" y="130.47" width="144" height="34" rx="6" fill="#f3e3f7" stroke="#b58ac9"/><text x="215.951" y="144.97" text-anchor="middle" font-size="10.5" font-weight="bold">Phase H</text><text x="215.951" y="157.97" text-anchor="middle" font-size="10.5" font-weight="bold">Architecture Change Mgmt</text><rect x="308" y="27" width="144" height="34" rx="6" fill="#f4f4f4" stroke="#999"/><text x="380" y="41.5" text-anchor="middle" font-size="10.5">Preliminary Phase</text><text x="380" y="54.5" text-anchor="middle" font-size="10.5">capability set-up</text><line x1="380" y1="63" x2="380" y2="85" stroke="#555" marker-end="url(#arr-f4-02)"/><circle cx="380" cy="250" r="52" fill="#fff1d6" stroke="#e0b060"/><text x="380" y="246" text-anchor="middle" font-size="11" font-weight="bold">Requirements</text><text x="380" y="259" text-anchor="middle" font-size="11" font-weight="bold">Management</text><rect x="10" y="10" width="14" height="14" rx="3" fill="#e3f5e1" stroke="#7fbf7a"/><text x="30" y="21" font-size="11" fill="#345">B, C, D develop: the same nine steps three times</text><rect x="10" y="30" width="14" height="14" rx="3" fill="#e0ecff" stroke="#7aa2e3"/><text x="30" y="41" font-size="11" fill="#345">E, F deliver: from gaps to an approved plan</text><rect x="10" y="50" width="14" height="14" rx="3" fill="#f3e3f7" stroke="#b58ac9"/><text x="30" y="61" font-size="11" fill="#345">G, H govern: contract, compliance, change</text><rect x="10" y="70" width="14" height="14" rx="3" fill="#fff1d6" stroke="#e0b060"/><text x="30" y="81" font-size="11" fill="#345">centre: Requirements Management, alongside every phase</text><text x="655" y="400" text-anchor="middle" font-size="10.5" fill="#c0392b">dashed H → A: only a re-architecting</text><text x="655" y="412" text-anchor="middle" font-size="10.5" fill="#c0392b">change starts a new cycle, through</text><text x="655" y="424" text-anchor="middle" font-size="10.5" fill="#c0392b">a new Request for Architecture Work</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">Phases B to H in three groups, with the process in the centre. Original drawing; order per ADM §4 to ADM §13, the H → A loop per ADM §12.</figcaption>
</figure>

<!-- figures:start -->
## Figures from the standard

The diagrams the cited sections carry, from your local copy of the publication. The exam reproduces these; know what each box is.

<div class="grid gap-4 md:grid-cols-2">
<figure class="max-w-lg"><img src="/figure/ADM:fig-10-1" alt="Figure 10-1: Phase F: Migration Planning" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 10-1: Phase F: Migration Planning (ADM)</figcaption></figure>
<figure class="max-w-lg"><img src="/figure/ADM:fig-11-1" alt="Figure 11-1: Phase G: Implementation" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 11-1: Phase G: Implementation (ADM)</figcaption></figure>
<figure class="max-w-lg"><img src="/figure/ADM:fig-12-1" alt="Figure 12-1: Phase H: Architecture Change Management" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 12-1: Phase H: Architecture Change Management (ADM)</figcaption></figure>
<figure class="max-w-lg"><img src="/figure/ADM:fig-13-1" alt="Figure 13-1: ADM Architecture Requirements" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 13-1: ADM Architecture Requirements (ADM)</figcaption></figure>
</div>
<!-- figures:end -->
