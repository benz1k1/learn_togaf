---
title: Gap Analysis, and Interoperability Requirements
unit: F5
objectives: ["5.3", "5.4"]
refs: ["TECH §5", "TECH §5.1", "TECH §5.2", "TECH §6.1", "TECH §6.2", "TECH §6.3", "TECH §6.4", "TECH §6.5", "TECH §6.6", "ADM §9.3.3", "ADM §9.3.5"]
reading_minutes: 10
source: authored
status: draft
---
## Gap analysis — validating what has been left out

Gap analysis is used widely in the ADM to **validate** an architecture under development. Its
premise is to highlight the shortfall between the Baseline and the Target: items deliberately
omitted, accidentally left out, or not yet defined (TECH §5).

Validating means asking what may have been forgotten; the architecture must support all of the
organisation's essential information-processing needs. The most critical source of gaps is
**stakeholder concerns not addressed in earlier work**. Other sources, by domain (TECH §5.1):

| Domain | Example gaps |
|---|---|
| Business | People (cross-training), process inefficiencies, duplicate or missing tools, information, measurement, financial, facilities |
| Data | Data not current enough, not where needed, not the data needed, not available when needed, not created, not consumed, relationship gaps |
| Application | Applications impacted, eliminated or created |
| Technology | Technologies impacted, eliminated or created |

### The matrix

| Step | Action |
|---|---|
| 1 | Baseline ABBs down the **vertical** axis; Target ABBs across the **horizontal** axis |
| 2 | Add a final row **"New"** to the baseline axis and a final column **"Eliminated"** to the target axis |
| 3 | An ABB in both → mark the intersection **"Included"** |
| 4 | A baseline ABB missing from the target → review it; if correctly eliminated mark it so in the Eliminated cell; if not, an accidental omission has been found and the ABB is reinstated in the next iteration |
| 5 | A target ABB with no baseline counterpart → mark it in the New row as a gap to fill by developing or procuring |

When done, everything under "Eliminated" or "New" is a gap, to be explained as correctly
eliminated or marked for reinstatement, development or procurement (TECH §5.2).

> **Trap.** "New" is a *row* on the baseline axis; "Eliminated" is a *column* on the target axis.
> An Eliminated cell can hold either a deliberate removal or an accidental omission — the
> review step is what tells them apart (TECH §5.2).

<figure class="my-4">
<svg viewBox="0 0 760 266" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="Gap analysis matrix: baseline building blocks as rows, target building blocks as columns, Included on the diagonal, an Eliminated column for baseline items missing from the target and a New row for target items with no baseline">
<defs><marker id="arr-f5-13a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
<text x="355" y="20" text-anchor="middle" font-size="11" fill="#345" font-weight="bold">Target ABBs →</text>
<rect x="175" y="30" width="120" height="36" rx="3" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="235.0" y="51.9" text-anchor="middle" font-size="11">Target A</text>
<rect x="295" y="30" width="120" height="36" rx="3" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="355.0" y="51.9" text-anchor="middle" font-size="11">Target B</text>
<rect x="415" y="30" width="120" height="36" rx="3" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="475.0" y="51.9" text-anchor="middle" font-size="11">Target C</text>
<rect x="535" y="30" width="160" height="36" rx="3" fill="#fff1d6" stroke="#e0b060"/>
<text x="615.0" y="51.9" text-anchor="middle" font-size="11" font-weight="bold">Eliminated</text>
<text x="8" y="150" text-anchor="middle" font-size="11" fill="#345" font-weight="bold" transform="rotate(-90 8 150)">Baseline ABBs ↓</text>
<rect x="15" y="66" width="160" height="40" rx="3" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="95.0" y="89.8" text-anchor="middle" font-size="11">Baseline A</text>
<rect x="175" y="66" width="120" height="40" rx="0" fill="#e3f5e1" stroke="#7fbf7a"/>
<text x="235.0" y="89.8" text-anchor="middle" font-size="11">Included</text>
<rect x="295" y="66" width="120" height="40" rx="0" fill="#fff" stroke="#666"/>
<text x="355.0" y="89.8" text-anchor="middle" font-size="11"></text>
<rect x="415" y="66" width="120" height="40" rx="0" fill="#fff" stroke="#666"/>
<text x="475.0" y="89.8" text-anchor="middle" font-size="11"></text>
<rect x="535" y="66" width="160" height="40" rx="0" fill="#fff" stroke="#666"/>
<text x="615.0" y="89.8" text-anchor="middle" font-size="11"></text>
<rect x="15" y="106" width="160" height="40" rx="3" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="95.0" y="129.8" text-anchor="middle" font-size="11">Baseline B</text>
<rect x="175" y="106" width="120" height="40" rx="0" fill="#fff" stroke="#666"/>
<text x="235.0" y="129.8" text-anchor="middle" font-size="11"></text>
<rect x="295" y="106" width="120" height="40" rx="0" fill="#e3f5e1" stroke="#7fbf7a"/>
<text x="355.0" y="129.8" text-anchor="middle" font-size="11">Included</text>
<rect x="415" y="106" width="120" height="40" rx="0" fill="#fff" stroke="#666"/>
<text x="475.0" y="129.8" text-anchor="middle" font-size="11"></text>
<rect x="535" y="106" width="160" height="40" rx="0" fill="#fff" stroke="#666"/>
<text x="615.0" y="129.8" text-anchor="middle" font-size="11"></text>
<rect x="15" y="146" width="160" height="40" rx="3" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="95.0" y="169.8" text-anchor="middle" font-size="11">Baseline C</text>
<rect x="175" y="146" width="120" height="40" rx="0" fill="#fff" stroke="#666"/>
<text x="235.0" y="169.8" text-anchor="middle" font-size="11"></text>
<rect x="295" y="146" width="120" height="40" rx="0" fill="#fff" stroke="#666"/>
<text x="355.0" y="169.8" text-anchor="middle" font-size="11"></text>
<rect x="415" y="146" width="120" height="40" rx="0" fill="#fff" stroke="#666"/>
<text x="475.0" y="169.8" text-anchor="middle" font-size="11"></text>
<rect x="535" y="146" width="160" height="40" rx="0" fill="#fff1d6" stroke="#e0b060"/>
<text x="615.0" y="163.0" text-anchor="middle" font-size="10">correctly eliminated?</text>
<text x="615.0" y="176.0" text-anchor="middle" font-size="10">or an omission → reinstate</text>
<rect x="15" y="186" width="160" height="40" rx="3" fill="#fff1d6" stroke="#e0b060"/>
<text x="95.0" y="209.8" text-anchor="middle" font-size="11" font-weight="bold">New</text>
<rect x="175" y="186" width="120" height="40" rx="0" fill="#fff" stroke="#666"/>
<text x="235.0" y="209.8" text-anchor="middle" font-size="11"></text>
<rect x="295" y="186" width="120" height="40" rx="0" fill="#fff" stroke="#666"/>
<text x="355.0" y="209.8" text-anchor="middle" font-size="11"></text>
<rect x="415" y="186" width="120" height="40" rx="0" fill="#fff1d6" stroke="#e0b060"/>
<text x="475.0" y="203.0" text-anchor="middle" font-size="10">gap: develop</text>
<text x="475.0" y="216.0" text-anchor="middle" font-size="10">or procure</text>
<rect x="535" y="186" width="160" height="40" rx="0" fill="#f1f1f1" stroke="#999"/>
<text x="615.0" y="209.8" text-anchor="middle" font-size="11"></text>
<text x="380" y="252" text-anchor="middle" font-size="11" fill="#666">Everything in the Eliminated column or the New row is a gap, to be explained or acted on</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">The gap matrix with one item carried forward twice, one eliminated and one new. Original drawing; steps per TECH §5.2.</figcaption>
</figure>

Gap analysis is performed as a step in each of Phases B, C and D; in Phase E the domain results
are consolidated into a single list — the **Consolidated Gaps, Solutions, and Dependencies
matrix** — which identifies SBBs that could address one or more gaps and their dependencies.
Dependencies are found using views such as the Business Interaction, Data Entity/Business
Function and Application/Function matrices; similar gaps are grouped, with reference to the
Implementation Factor catalog (ADM §9.3.3).

## Interoperability requirements

Interoperability is "the ability to share information and services"; defining *the degree* to
which they are shared is a useful requirement, especially in a complex or extended enterprise.
It appears throughout the ADM: revealed in business scenarios in Phase A; defined in business
terms in B; the content of information exchanges detailed in the Data Architecture and the way
applications share in the Application Architecture (C); technical mechanisms in D; actual
solutions selected in E; logically implemented in F (TECH §6.1).

### Categories

Many organisations categorise interoperability as **operational or business** (how processes are
shared), **information** (how information is shared) and **technical** (how technical services
are shared or connected). From an IT/EAI perspective there is also presentation, information,
application and technical integration (TECH §6.2).

### Operating model, degrees and matrices

The corporate **operating model** — the required level of business process integration and
standardisation — usually indicates the appropriate interoperability approach. It should be
determined in Phase A, if not in Phase B, and definitely by Phase E; an extended enterprise may
have a different model from the internal one (TECH §6.3).

Implementing interoperability needs realistic **SMART** standards and clear measures. An example
scheme is the four *Degrees of Interoperability*: 1 unstructured data exchange; 2 structured data
exchange with manual handling; 3 seamless sharing of data on a common exchange model; 4 seamless
sharing of information through co-operating applications. Degree 3 can be refined further (3A
formal message exchange … 3D real-time). Measures go into the strategic direction and the
transformation strategy, and the consolidated gap results are updated afterwards (TECH §6.4).

Co-existence of old and new systems is the hard part; operations staff must be involved, and a
"wrapper" between a legacy application and new infrastructure may become permanent. A
**Business Information Interoperability Matrix** starts in Phase B (sharing between stakeholders)
and evolves in Phase C into an **Information Systems Interoperability Matrix** (specific systems,
refined degrees). Sharing is not necessarily symmetrical (TECH §6.5).

<figure class="my-4">
<svg viewBox="0 0 760 190" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="Interoperability requirements move through the phases from being revealed in A to implemented in F, with the business matrix of Phase B evolving into the information systems matrix of Phase C">
<defs><marker id="arr-f5-13b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
<rect x="15" y="15" width="116" height="30" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="73.0" y="34.2" text-anchor="middle" font-size="12" font-weight="bold">Phase A</text>
<line x1="131" y1="30" x2="137" y2="30" stroke="#555" marker-end="url(#arr-f5-13b)"/>
<text x="73" y="66" text-anchor="middle" font-size="10" fill="#333">revealed in</text>
<text x="73" y="80" text-anchor="middle" font-size="10" fill="#333">business scenarios;</text>
<text x="73" y="94" text-anchor="middle" font-size="10" fill="#333">operating model</text>
<rect x="137" y="15" width="116" height="30" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="195.0" y="34.2" text-anchor="middle" font-size="12" font-weight="bold">Phase B</text>
<line x1="253" y1="30" x2="259" y2="30" stroke="#555" marker-end="url(#arr-f5-13b)"/>
<text x="195" y="66" text-anchor="middle" font-size="10" fill="#333">defined in</text>
<text x="195" y="80" text-anchor="middle" font-size="10" fill="#333">business terms</text>
<rect x="259" y="15" width="116" height="30" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="317.0" y="34.2" text-anchor="middle" font-size="12" font-weight="bold">Phase C</text>
<line x1="375" y1="30" x2="381" y2="30" stroke="#555" marker-end="url(#arr-f5-13b)"/>
<text x="317" y="66" text-anchor="middle" font-size="10" fill="#333">data exchanges;</text>
<text x="317" y="80" text-anchor="middle" font-size="10" fill="#333">how applications</text>
<text x="317" y="94" text-anchor="middle" font-size="10" fill="#333">share; degrees</text>
<rect x="381" y="15" width="116" height="30" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="439.0" y="34.2" text-anchor="middle" font-size="12" font-weight="bold">Phase D</text>
<line x1="497" y1="30" x2="503" y2="30" stroke="#555" marker-end="url(#arr-f5-13b)"/>
<text x="439" y="66" text-anchor="middle" font-size="10" fill="#333">technical</text>
<text x="439" y="80" text-anchor="middle" font-size="10" fill="#333">mechanisms</text>
<rect x="503" y="15" width="116" height="30" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="561.0" y="34.2" text-anchor="middle" font-size="12" font-weight="bold">Phase E</text>
<line x1="619" y1="30" x2="625" y2="30" stroke="#555" marker-end="url(#arr-f5-13b)"/>
<text x="561" y="66" text-anchor="middle" font-size="10" fill="#333">solutions selected;</text>
<text x="561" y="80" text-anchor="middle" font-size="10" fill="#333">conflicts reconciled</text>
<rect x="625" y="15" width="116" height="30" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="683.0" y="34.2" text-anchor="middle" font-size="12" font-weight="bold">Phase F</text>
<text x="683" y="66" text-anchor="middle" font-size="10" fill="#333">logically</text>
<text x="683" y="80" text-anchor="middle" font-size="10" fill="#333">implemented</text>
<rect x="137" y="122" width="238" height="34" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/>
<text x="256.0" y="136.0" text-anchor="middle" font-size="10">Business Information</text>
<text x="256.0" y="149.0" text-anchor="middle" font-size="10">Interoperability Matrix (stakeholders)</text>
<line x1="375" y1="139" x2="400" y2="139" stroke="#555" marker-end="url(#arr-f5-13b)"/>
<text x="388" y="117" text-anchor="middle" font-size="9" fill="#666">evolves</text>
<rect x="402" y="122" width="200" height="34" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/>
<text x="502.0" y="136.0" text-anchor="middle" font-size="10">Information Systems</text>
<text x="502.0" y="149.0" text-anchor="middle" font-size="10">Interoperability Matrix (systems)</text>
<text x="380" y="178" text-anchor="middle" font-size="10" fill="#666">sharing is not necessarily symmetrical; the operating model is needed by Phase E at the latest</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">Interoperability from Phase A to F, and the matrix that evolves between B and C. Original drawing; sequence per TECH §6.1, matrices per TECH §6.5.</figcaption>
</figure>

### Reconciling with solutions

The biggest issue when re-using SBBs or COTS is **business interoperability**: packages embed
their own business processes, and changing them can cost more than re-use saves. Any change to
business interoperability requirements must be signed off by the Business Architects and sponsors
in a **revised Statement of Architecture Work** (TECH §6.6). In Phase E the requirements from
earlier phases are consolidated and conflicts minimised; there are two basic responses to a
conflict — create a building block that translates between the conflicting ones, or change the
specification of the conflicting building blocks (ADM §9.3.5).

<!-- figures:start -->
## Figures from the standard

The diagrams the cited sections carry, from your local copy of the publication. The exam reproduces these; know what each box is.

<div class="grid gap-4 md:grid-cols-2">
<figure class="max-w-lg"><img src="/figure/TECH:fig-6-1" alt="Figure 6-1: Business Information Interoperability Matrix" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 6-1: Business Information Interoperability Matrix (TECH)</figcaption></figure>
<figure class="max-w-lg"><img src="/figure/TECH:fig-6-2" alt="Figure 6-2: Information Systems Interoperability Matrix" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 6-2: Information Systems Interoperability Matrix (TECH)</figcaption></figure>
</div>
<!-- figures:end -->

## Check yourself

- Which axis carries the "Eliminated" column?
- In which phase is the operating model "definitely" needed, at the latest?
- What document records an agreed change to business interoperability requirements?
