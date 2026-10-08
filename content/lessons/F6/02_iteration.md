---
title: Applying iteration to the ADM — the four cycles, engagement classes and baseline/target first
unit: F6
objectives: ["6.1"]
refs: ["APPLY §2.1", "APPLY §2.2", "APPLY §2.3", "APPLY §2.4", "APPLY §2.5", "APPLY §2.5.1", "APPLY §2.5.2", "APPLY §2.6"]
reading_minutes: 10
source: authored
status: draft
---
## The ADM is not a waterfall

The ADM graphic and the phase-by-phase description can be read as a deterministic waterfall; that
presentation simply communicates the basics quickly. In practice two tightly linked concepts manage
complexity: **iteration** and **levels**. The standard uses "iteration" for three things: describing
a comprehensive Architecture Landscape through multiple ADM cycles, each bound to a Request for
Architecture Work; the integrated process within one cycle where phases interact; and managing
change to the Architecture Capability (APPLY §2.1).

| Kind of iteration | What it looks like |
|---|---|
| Landscape (between cycles) | Each project runs a full cycle from Phase A, bound by its Request for Architecture Work, and extends or changes the landscape; projects may run concurrently; one project may trigger another when it finds a need for more detailed work or impacts outside its scope |
| Within a cycle (Architecture Development) | Phases run concurrently (to manage B/C/D interrelationships); phases cycle in planned loops (to converge on a target when no higher-level context exists); phases are revisited to update work products (to converge on an executable roadmap or plan) |
| Capability | A new Preliminary Phase iteration to (re)establish the capability for a Request, or to adjust it after a Phase H Change Request |

(APPLY §2.1)

## The four iteration cycles

| Cycle | Purpose |
|---|---|
| **Architecture Capability** | Create and evolve the required capability — mobilise the activity by establishing or adjusting approach, principles, scope, vision and governance |
| **Architecture Development** | Create architecture content by cycling through or integrating the Business, Information Systems and Technology phases; stakeholder reviews are typically broader; as it converges, extensions into Opportunities & Solutions and Migration Planning check implementability |
| **Transition Planning** | Create formal change roadmaps for a defined architecture |
| **Architecture Governance** | Govern change activity progressing towards a defined Target Architecture |

(APPLY §2.2)

> **Trap.** Architecture Development is not confined to B, C, D: as the iterations converge, the
> cycle *extends into* Phases E and F so that implementability is considered while the
> architecture is finalised (APPLY §2.2).

<figure class="my-4">
<svg viewBox="0 0 760 328" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="The four iteration cycles drawn as arcs on the ADM ring: Capability over the Preliminary Phase and A, Development over A to D and extending into E and F, Transition Planning over E and F, Governance over G and H">
<defs><marker id="arr-f6-10a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
<circle cx="300" cy="178" r="100" fill="none" stroke="#bbb" stroke-width="2"/>
<path d="M228.9 76.4 A124 124 0 0 1 371.1 76.4" fill="none" stroke="#7aa2e3" stroke-width="7" stroke-linecap="round" opacity="0.85"/>
<path d="M300.0 38.0 A140 140 0 0 1 399.0 277.0" fill="none" stroke="#7fbf7a" stroke-width="7" stroke-linecap="round" opacity="0.85"/>
<path d="M300.0 302.0 A124 124 0 0 1 212.3 265.7" fill="none" stroke="#e0b060" stroke-width="7" stroke-linecap="round" opacity="0.85"/>
<path d="M160.0 178.0 A140 140 0 0 1 201.0 79.0" fill="none" stroke="#b58ac9" stroke-width="7" stroke-linecap="round" opacity="0.85"/>
<rect x="40" y="20" width="110" height="28" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="95.0" y="37.9" text-anchor="middle" font-size="11" font-weight="bold">Preliminary</text>
<line x1="150" y1="34" x2="282.0" y2="72.0" stroke="#7aa2e3" stroke-width="2" marker-end="url(#arr-f6-10a)"/>
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
<text x="380" y="318" text-anchor="middle" font-size="10" fill="#666">Each arc can be repeated; the Development arc is where baseline-first or target-first applies</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">The four cycles mapped onto the ring, with Development reaching into E and F. Original drawing; cycles per APPLY §2.2.</figcaption>
</figure>

## Classes of engagement

Architects are engaged in three areas: **identification of required change** (architecture as
visibility of IT capability for strategic decisions, outside any change initiative),
**definition of change** (structuring the nature and extent of an identified change), and
**implementation of change** (design governance — big-picture visibility, structural constraints,
evaluation criteria). Six engagement classes sit under them, and each has a characteristic focus
(APPLY §2.3):

| Area | Engagement class | Focus iteration cycles | Scope focus |
|---|---|---|---|
| Identification | Supporting Business Strategy | Capability; Development (baseline first) | Broad, shallow view to answer a strategic question |
| Identification | Portfolio Management of the Landscape | Capability; Development (baseline first) | Physical assessment of baseline applications and infrastructure for improvement opportunities |
| Identification | Portfolio Management of Projects | Transition Planning; Governance | Project dependencies and landscape impacts to sequence projects |
| Definition | Foundational Change Initiatives (known objective, not tightly scoped) | Capability; Development (baseline first); Transition Planning | Elaborate a vision by defining the baseline and what must change |
| Definition | Bounded Change Initiatives (outcome already agreed) | Development (**target first**); Transition Planning | Elaborate the target to an agreed vision; avoid perpetuating a sub-optimal baseline |
| Implementation | Governance of Change Implementation | Governance | Use vision, principles, requirements, target and roadmap so projects realise their benefit and align |

(APPLY §2.3)

## Baseline first or target first

**Baseline First** assesses the current landscape to find problem areas and opportunities; it suits
a baseline that is complex, poorly understood or not agreed, which is common where units have had
high autonomy. **Target First** elaborates the target in detail and maps back to the baseline to
find the change activity; it suits a target already agreed at a high level. If the baseline is
broadly understood, more value comes from focusing on the target first and describing the baseline
only as far as needed to identify changes. A team always considers the other state informally,
but should give one state priority to keep focus (APPLY §2.4).

## Iteration considerations

Some cycles run once; others have a natural minimum number of iterations, and the process differs
slightly between iterations. Checkpoints are placed according to stakeholder involvement: highly
involved stakeholders suit very frequent, informal checkpoints; less involved ones suit less
frequent, more formal ones — commonly at the end of each cycle or of several (APPLY §2.5).

**Between cycles**, each iteration completes an ADM cycle at a single level of description, and
**Phase F is used to initiate** new, more detailed architecture projects — higher-level
architecture guiding and constraining the more detailed (APPLY §2.5.1). **Within a cycle**, each
iteration crosses several phases, with activity that is *core* (primary focus), *light* (secondary)
or *informal* (APPLY §2.5.2):

| Cycle | Iteration 1 | Iteration 2 | Iteration n |
|---|---|---|---|
| Development, baseline first | Define the Baseline Architecture (B, C, D; E/F considered to test feasibility) | Define the Target and gaps against the baseline | Refine baseline, target and gaps |
| Development, target first | Define the Target Architecture | Define the Baseline and gaps against the target | Refine baseline, target and gaps |
| Transition Planning | Agree improvement opportunities against a provisional Transition Architecture; provisional Migration Plan | — | Agree the Transition Architecture, refining opportunities to fit |
| Architecture Governance | Mobilise governance and change management processes, people and technology | — | Periodic reviews of change initiatives; a Change Request may send a requirement back to the Preliminary Phase or the development phases |

(APPLY §2.5.2)

<figure class="my-4">
<svg viewBox="0 0 760 218" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="Baseline first and target first compared iteration by iteration: which state is defined first, which second, and the refinement that follows">
<defs><marker id="arr-f6-10b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
<text x="15" y="42" text-anchor="start" font-size="12" fill="#222" font-weight="bold">Baseline First</text>
<text x="15" y="58" text-anchor="start" font-size="9" fill="#666">suits:</text>
<text x="15" y="70" text-anchor="start" font-size="9" fill="#666">a complex, poorly</text>
<text x="15" y="82" text-anchor="start" font-size="9" fill="#666">understood or disputed</text>
<text x="15" y="94" text-anchor="start" font-size="9" fill="#666">baseline</text>
<rect x="160" y="18" width="180" height="60" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="250.0" y="38.5" text-anchor="middle" font-size="10" font-weight="bold">Iteration 1</text>
<text x="250.0" y="51.5" text-anchor="middle" font-size="10">define the Baseline (B, C, D;</text>
<text x="250.0" y="64.5" text-anchor="middle" font-size="10">E and F test feasibility)</text>
<line x1="340" y1="48" x2="360" y2="48" stroke="#555" marker-end="url(#arr-f6-10b)"/>
<rect x="360" y="18" width="180" height="60" rx="6" fill="#fff" stroke="#666"/>
<text x="450.0" y="38.5" text-anchor="middle" font-size="10" font-weight="bold">Iteration 2</text>
<text x="450.0" y="51.5" text-anchor="middle" font-size="10">define the Target and the</text>
<text x="450.0" y="64.5" text-anchor="middle" font-size="10">gaps against the baseline</text>
<line x1="540" y1="48" x2="560" y2="48" stroke="#555" marker-end="url(#arr-f6-10b)"/>
<rect x="560" y="18" width="180" height="60" rx="6" fill="#fff" stroke="#666"/>
<text x="650.0" y="38.5" text-anchor="middle" font-size="10" font-weight="bold">Iteration n</text>
<text x="650.0" y="51.5" text-anchor="middle" font-size="10">refine baseline,</text>
<text x="650.0" y="64.5" text-anchor="middle" font-size="10">target and gaps</text>
<text x="15" y="134" text-anchor="start" font-size="12" fill="#222" font-weight="bold">Target First</text>
<text x="15" y="150" text-anchor="start" font-size="9" fill="#666">suits:</text>
<text x="15" y="162" text-anchor="start" font-size="9" fill="#666">a target already agreed at</text>
<text x="15" y="174" text-anchor="start" font-size="9" fill="#666">a high level</text>
<rect x="160" y="110" width="180" height="60" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/>
<text x="250.0" y="130.5" text-anchor="middle" font-size="10" font-weight="bold">Iteration 1</text>
<text x="250.0" y="143.5" text-anchor="middle" font-size="10">define the Target</text>
<text x="250.0" y="156.5" text-anchor="middle" font-size="10">Architecture</text>
<line x1="340" y1="140" x2="360" y2="140" stroke="#555" marker-end="url(#arr-f6-10b)"/>
<rect x="360" y="110" width="180" height="60" rx="6" fill="#fff" stroke="#666"/>
<text x="450.0" y="130.5" text-anchor="middle" font-size="10" font-weight="bold">Iteration 2</text>
<text x="450.0" y="143.5" text-anchor="middle" font-size="10">define the Baseline and the</text>
<text x="450.0" y="156.5" text-anchor="middle" font-size="10">gaps against the target</text>
<line x1="540" y1="140" x2="560" y2="140" stroke="#555" marker-end="url(#arr-f6-10b)"/>
<rect x="560" y="110" width="180" height="60" rx="6" fill="#fff" stroke="#666"/>
<text x="650.0" y="130.5" text-anchor="middle" font-size="10" font-weight="bold">Iteration n</text>
<text x="650.0" y="143.5" text-anchor="middle" font-size="10">refine baseline,</text>
<text x="650.0" y="156.5" text-anchor="middle" font-size="10">target and gaps</text>
<text x="380" y="206" text-anchor="middle" font-size="10" fill="#666">Give one state priority to keep focus; the other is always considered informally</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">Baseline-first and target-first as iteration sequences. Original drawing; approaches per APPLY §2.4, iterations per APPLY §2.5.2.</figcaption>
</figure>

## What decides how you iterate

The ADM should always be used iteratively; how depends on: the formality and nature of process
checkpoints; the expected level of stakeholder involvement; the number of teams and their
relationships; the maturity of the solution area and expected rework; attitude to risk (does
partial work circulate? must solutions be proved in a trial?); and the class of engagement
(APPLY §2.6).

<!-- figures:start -->
## Figures from the standard

The diagrams the cited sections carry, from your local copy of the publication. The exam reproduces these; know what each box is.

<div class="grid gap-4 md:grid-cols-2">
<figure class="max-w-lg"><img src="/figure/APPLY:fig-2-1" alt="Figure 2-1: Iteration Cycles" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 2-1: Iteration Cycles (APPLY)</figcaption></figure>
<figure class="max-w-lg"><img src="/figure/APPLY:fig-2-2" alt="Figure 2-2: Classes of Enterprise Architecture Engagement" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 2-2: Classes of Enterprise Architecture Engagement (APPLY)</figcaption></figure>
<figure class="max-w-lg"><img src="/figure/APPLY:fig-2-3" alt="Figure 2-3: A Hierarchy of ADM Processes Example" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 2-3: A Hierarchy of ADM Processes Example (APPLY)</figcaption></figure>
<figure class="max-w-lg"><img src="/figure/APPLY:fig-2-4" alt="Figure 2-4: Activity by Iteration for Baseline First Architecture Definition" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 2-4: Activity by Iteration for Baseline First Architecture Definition (APPLY)</figcaption></figure>
<figure class="max-w-lg"><img src="/figure/APPLY:fig-2-5" alt="Figure 2-5: Activity by Iteration for Target First Architecture Definition" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 2-5: Activity by Iteration for Target First Architecture Definition (APPLY)</figcaption></figure>
</div>
<!-- figures:end -->

## Check yourself

- Which cycle does a Bounded Change Initiative focus on, and which approach — baseline or target first?
- Which phase initiates new, more detailed architecture projects in iteration between cycles?
- What is the first iteration of the Architecture Governance cycle for?
