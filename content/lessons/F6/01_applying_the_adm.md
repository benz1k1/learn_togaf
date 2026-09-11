---
title: Iteration, the Architecture Landscape, partitioning, security and agile
unit: F6
objectives: ["6.1", "6.2", "6.3"]
refs: ["APPLY §2", "APPLY §3", "APPLY §4", "GUIDE:integrating-risk-and-security §4", "GUIDE:agile-sprints §3.3", "GUIDE:enabling-enterprise-agility §4.1"]
reading_minutes: 8
source: authored
status: draft
---
## Four iteration cycles (APPLY §2)

| Cycle | Phases | Purpose |
|---|---|---|
| Architecture Capability | Preliminary, A | establish or adjust the capability |
| Architecture Development | A, B, C, D | create the architecture content |
| Transition Planning | E, F | plan the change |
| Architecture Governance | G, H | govern implementation and change |

Iteration can be baseline-first (describe what exists, then the target) or target-first
(describe the target, then find the baseline needed to plan the gaps).

<figure class="my-4">
<svg viewBox="0 0 760 328" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="The four iteration cycles drawn as arcs on the ADM ring: Capability over the Preliminary Phase and A, Development over A to D, Transition Planning over E and F, Governance over G and H">
<defs><marker id="arr-f6-01a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
<circle cx="300" cy="178" r="100" fill="none" stroke="#bbb" stroke-width="2"/>
<path d="M228.9 76.4 A124 124 0 0 1 371.1 76.4" fill="none" stroke="#7aa2e3" stroke-width="7" stroke-linecap="round" opacity="0.85"/>
<path d="M300.0 38.0 A140 140 0 0 1 399.0 277.0" fill="none" stroke="#7fbf7a" stroke-width="7" stroke-linecap="round" opacity="0.85"/>
<path d="M300.0 302.0 A124 124 0 0 1 212.3 265.7" fill="none" stroke="#e0b060" stroke-width="7" stroke-linecap="round" opacity="0.85"/>
<path d="M160.0 178.0 A140 140 0 0 1 201.0 79.0" fill="none" stroke="#b58ac9" stroke-width="7" stroke-linecap="round" opacity="0.85"/>
<rect x="40" y="20" width="110" height="28" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="95.0" y="37.9" text-anchor="middle" font-size="11" font-weight="bold">Preliminary</text>
<line x1="150" y1="34" x2="282.0" y2="72.0" stroke="#7aa2e3" stroke-width="2" marker-end="url(#arr-f6-01a)"/>
<circle cx="300.0" cy="78.0" r="17" fill="#fff" stroke="#666"/>
<text x="300.0" y="82.5" text-anchor="middle" font-size="13" fill="#222" font-weight="bold">A</text>
<circle cx="370.7" cy="107.3" r="17" fill="#fff" stroke="#666"/>
<text x="370.7" y="111.8" text-anchor="middle" font-size="13" fill="#222" font-weight="bold">B</text>
<circle cx="400.0" cy="178.0" r="17" fill="#fff" stroke="#666"/>
<text x="400.0" y="182.5" text-anchor="middle" font-size="13" fill="#222" font-weight="bold">C</text>
<circle cx="370.7" cy="248.7" r="17" fill="#fff" stroke="#666"/>
<text x="370.7" y="253.2" text-anchor="middle" font-size="13" fill="#222" font-weight="bold">D</text>
<circle cx="300.0" cy="278.0" r="17" fill="#fff" stroke="#666"/>
<text x="300.0" y="282.5" text-anchor="middle" font-size="13" fill="#222" font-weight="bold">E</text>
<circle cx="229.3" cy="248.7" r="17" fill="#fff" stroke="#666"/>
<text x="229.3" y="253.2" text-anchor="middle" font-size="13" fill="#222" font-weight="bold">F</text>
<circle cx="200.0" cy="178.0" r="17" fill="#fff" stroke="#666"/>
<text x="200.0" y="182.5" text-anchor="middle" font-size="13" fill="#222" font-weight="bold">G</text>
<circle cx="229.3" cy="107.3" r="17" fill="#fff" stroke="#666"/>
<text x="229.3" y="111.8" text-anchor="middle" font-size="13" fill="#222" font-weight="bold">H</text>
<text x="300" y="174" text-anchor="middle" font-size="10" fill="#666">Requirements</text>
<text x="300" y="188" text-anchor="middle" font-size="10" fill="#666">Management</text>
<rect x="490" y="70" width="16" height="16" rx="3" fill="#7aa2e3"/>
<text x="514" y="83" text-anchor="start" font-size="12" fill="#222" font-weight="bold">Architecture Capability</text>
<text x="514" y="100" text-anchor="start" font-size="10" fill="#555">Preliminary, A</text>
<rect x="490" y="126" width="16" height="16" rx="3" fill="#7fbf7a"/>
<text x="514" y="139" text-anchor="start" font-size="12" fill="#222" font-weight="bold">Architecture Development</text>
<text x="514" y="156" text-anchor="start" font-size="10" fill="#555">A, B, C, D — extends into E, F as it converges</text>
<rect x="490" y="182" width="16" height="16" rx="3" fill="#e0b060"/>
<text x="514" y="195" text-anchor="start" font-size="12" fill="#222" font-weight="bold">Transition Planning</text>
<text x="514" y="212" text-anchor="start" font-size="10" fill="#555">E, F</text>
<rect x="490" y="238" width="16" height="16" rx="3" fill="#b58ac9"/>
<text x="514" y="251" text-anchor="start" font-size="12" fill="#222" font-weight="bold">Architecture Governance</text>
<text x="514" y="268" text-anchor="start" font-size="10" fill="#555">G, H</text>
<text x="380" y="318" text-anchor="middle" font-size="10" fill="#666">One ADM cycle can be run as several passes round each of these four arcs</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">The four iteration cycles as arcs on the ring. Original drawing; cycles per APPLY §2.</figcaption>
</figure>

## Three levels of the Architecture Landscape (APPLY §3)

**Strategic** Architecture is the executive, long-term summary; **Segment** Architecture is
the programme or portfolio level; **Capability** Architecture is the detailed, project-level
description of one capability increment. Lower levels are constrained by higher ones.

<figure class="my-4">
<svg viewBox="0 0 760 206" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="The three Architecture Landscape levels as a pyramid: Strategic at the top, Segment in the middle, Capability at the base">
<defs><marker id="arr-f6-01b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
<path d="M320 18 L440 18 L520 74 L240 74 Z" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="380" y="43" text-anchor="middle" font-size="13" fill="#222" font-weight="bold">Strategic</text>
<text x="380" y="61" text-anchor="middle" font-size="10" fill="#444">executive, long-term summary</text>
<path d="M240 78 L520 78 L600 134 L160 134 Z" fill="#e3f5e1" stroke="#7fbf7a"/>
<text x="380" y="103" text-anchor="middle" font-size="13" fill="#222" font-weight="bold">Segment</text>
<text x="380" y="121" text-anchor="middle" font-size="10" fill="#444">programme or portfolio level</text>
<path d="M160 138 L600 138 L680 194 L80 194 Z" fill="#fff1d6" stroke="#e0b060"/>
<text x="380" y="163" text-anchor="middle" font-size="13" fill="#222" font-weight="bold">Capability</text>
<text x="380" y="181" text-anchor="middle" font-size="10" fill="#444">one capability increment, project level</text>
<line x1="40" y1="30" x2="40" y2="190" stroke="#555" marker-end="url(#arr-f6-01b)"/>
<text x="30" y="110" text-anchor="middle" font-size="10" fill="#345" transform="rotate(-90 30 110)">higher constrains lower</text>
<line x1="720" y1="30" x2="720" y2="190" stroke="#555" marker-end="url(#arr-f6-01b)"/>
<text x="732" y="110" text-anchor="middle" font-size="10" fill="#345" transform="rotate(90 732 110)">more detail, narrower breadth</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">The three levels as a pyramid: higher levels constrain lower ones. Original drawing; levels per APPLY §3.</figcaption>
</figure>

## Partitioning (APPLY §4)

Architectures are partitioned by subject matter, time and level of detail, so that different
teams can work in parallel without conflict and so that reuse is possible. The Preliminary
Phase decides the partitions; each partition has its own Architecture Repository contents.

## Security and agile (Series Guides — not in APPLY)

Security is addressed in every phase, not as a separate domain; the Series Guide on risk and
security integration goes deeper. The ADM works with agile delivery by treating an architecture
increment as a backlog item, iterating in short cycles at the capability level, and keeping
governance light but present.

<!-- figures:start -->
## Figures from the standard

The diagrams the cited sections carry, from your local copy of the publication. The exam reproduces these; know what each box is.

<div class="grid gap-4 md:grid-cols-2">
<figure class="max-w-lg"><img src="/figure/GUIDE:agile-sprints:fig-3-1" alt="Figure 3-1: Agile Enterprise Architecture Ways of Collaboration" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 3-1: Agile Enterprise Architecture Ways of Collaboration (GUIDE:agile-sprints)</figcaption></figure>
<figure class="max-w-lg"><img src="/figure/GUIDE:agile-sprints:fig-3-2" alt="Figure 3-2: Enterprise Architecture Development Sprints in the ADM" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 3-2: Enterprise Architecture Development Sprints in the ADM (GUIDE:agile-sprints)</figcaption></figure>
<figure class="max-w-lg"><img src="/figure/GUIDE:agile-sprints:fig-3-3" alt="Figure 3-3: Architecture and Solution Sprints in the ADM" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 3-3: Architecture and Solution Sprints in the ADM (GUIDE:agile-sprints)</figcaption></figure>
<figure class="max-w-lg"><img src="/figure/GUIDE:agile-sprints:fig-3-4" alt="Figure 3-4: Cross-Development Collaboration" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 3-4: Cross-Development Collaboration (GUIDE:agile-sprints)</figcaption></figure>
<figure class="max-w-lg"><img src="/figure/GUIDE:agile-sprints:fig-3-5" alt="Figure 3-5: Agile Improved Enterprise using Sprints" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 3-5: Agile Improved Enterprise using Sprints (GUIDE:agile-sprints)</figcaption></figure>
<figure class="max-w-lg"><img src="/figure/GUIDE:enabling-enterprise-agility:fig-4-1" alt="Figure 4-1: Summary Classification Model for Architecture Landscapes" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 4-1: Summary Classification Model for Architecture Landscapes (GUIDE:enabling-enterprise-agility)</figcaption></figure>
</div>
<!-- figures:end -->
