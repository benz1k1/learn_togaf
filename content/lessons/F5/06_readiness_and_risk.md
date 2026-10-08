---
title: Business Transformation Readiness Assessment, and Risk Management
unit: F5
objectives: ["5.4"]
refs: ["TECH §7", "TECH §7.1", "TECH §7.2", "TECH §7.3", "TECH §7.4", "TECH §7.4.1", "TECH §7.4.2", "TECH §7.4.3", "TECH §7.5", "TECH §7.6", "TECH §8.1", "TECH §8.2", "TECH §8.3", "TECH §8.4", "TECH §8.5", "TECH §8.6", "TECH §8.7", "ADM §3.3.5", "ADM §9.3.7"]
reading_minutes: 11
source: authored
status: draft
---
## Readiness assessment — the human side of transformation

Business Transformation Readiness Assessment evaluates and quantifies how ready an organisation is
to undergo change; the standard's version builds on the Canadian Government's Business
Transformation Enablement Program (BTEP) (TECH §7). An innovative vision and architecture will
demand considerable change, and the human element is the most important dimension — a
change-averse culture can stop a sound architecture. Understanding readiness and dealing with the
issues in the Implementation and Migration Plans is key to Phases E and F; it is a joint effort of
corporate staff (especially HR), lines of business and IT planners (TECH §7.1).

The recommended activities, in order (TECH §7.1):

1. Determine the readiness factors that will affect the organisation
2. Present the factors using **maturity models**
3. Assess the factors, including a readiness rating
4. Assess the risks for each factor and identify improvement actions
5. Work those actions into the Phase E and F Implementation and Migration Plan

### Determine factors

Factors are best found in a facilitated workshop across the organisation, starting from a
tentative list to re-use, reject, augment or replace. The BTEP example set: Vision; Desire,
Willingness and Resolve; Need; Business Case; Funding; Sponsorship and Leadership; Governance;
Accountability; Workable Approach and Execution Model; IT Capacity to Execute; Enterprise Capacity
to Execute; Enterprise Ability to Implement and Operate (TECH §7.2).

### Present and assess

Converting each factor into a maturity model (a re-usable governance asset) with a worksheet lets
participants assess current maturity, the target maturity needed for the Target Architecture, and
an achievable intermediate target (TECH §7.3). The assessment, ideally in a multi-disciplinary
workshop with templates per factor, addresses three things: readiness factor **vision**,
**rating**, and **risks and actions** (TECH §7.4). Vision is where the enterprise has to get to
for that factor — base state, then target, perhaps an intermediate (TECH §7.4.1).

| Rating dimension | Scale |
|---|---|
| **Urgency** | Urgent means action is needed before the transformation can begin |
| **Readiness Status** | Low (substantial work) · Fair (some work) · Acceptable (issues, no showstoppers) · Good (minor issues) · High (no issues) |
| **Degree of Difficulty to Fix** | No Action Needed · Easy · Moderate · Difficult |

A summary table consolidates the factors for management (TECH §7.4.2).

> **Trap.** The rating scheme is urgency, readiness status and difficulty to fix. Maturity models
> are how the factors are *presented* (TECH §7.3), not the rating scale (TECH §7.4.2).

Each factor is then assessed for risk — with an estimate of impact and frequency — and a set of
improvement actions is derived (checking existing actions first), formally incorporated into the
emerging Implementation and Migration Plan, and managed through the risk management process to an
acceptable residual risk (TECH §7.4.3).

<figure class="my-4">
<svg viewBox="0 0 760 200" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="Readiness assessment as five steps from factors through maturity models and rating to risks and the migration plan, landing in Phase A, feeding E and F and monitored in G">
<defs><marker id="arr-f5-14a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
<rect x="15" y="20" width="136" height="62" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="83.0" y="41.5" text-anchor="middle" font-size="10" font-weight="bold">1 Determine factors</text>
<text x="83.0" y="54.5" text-anchor="middle" font-size="10">facilitated workshop;</text>
<text x="83.0" y="67.5" text-anchor="middle" font-size="10">BTEP list to adapt</text>
<line x1="151" y1="51" x2="165" y2="51" stroke="#555" marker-end="url(#arr-f5-14a)"/>
<rect x="165" y="20" width="136" height="62" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="233.0" y="41.5" text-anchor="middle" font-size="10" font-weight="bold">2 Present</text>
<text x="233.0" y="54.5" text-anchor="middle" font-size="10">as maturity models:</text>
<text x="233.0" y="67.5" text-anchor="middle" font-size="10">current, target, interim</text>
<line x1="301" y1="51" x2="315" y2="51" stroke="#555" marker-end="url(#arr-f5-14a)"/>
<rect x="315" y="20" width="136" height="62" rx="6" fill="#fff1d6" stroke="#e0b060"/>
<text x="383.0" y="41.5" text-anchor="middle" font-size="10" font-weight="bold">3 Rate</text>
<text x="383.0" y="54.5" text-anchor="middle" font-size="10">urgency · readiness</text>
<text x="383.0" y="67.5" text-anchor="middle" font-size="10">status · difficulty to fix</text>
<line x1="451" y1="51" x2="465" y2="51" stroke="#555" marker-end="url(#arr-f5-14a)"/>
<rect x="465" y="20" width="136" height="62" rx="6" fill="#fff1d6" stroke="#e0b060"/>
<text x="533.0" y="41.5" text-anchor="middle" font-size="10" font-weight="bold">4 Risks and actions</text>
<text x="533.0" y="54.5" text-anchor="middle" font-size="10">impact and frequency;</text>
<text x="533.0" y="67.5" text-anchor="middle" font-size="10">improvement actions</text>
<line x1="601" y1="51" x2="615" y2="51" stroke="#555" marker-end="url(#arr-f5-14a)"/>
<rect x="615" y="20" width="136" height="62" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/>
<text x="683.0" y="35.0" text-anchor="middle" font-size="10" font-weight="bold">5 Into the plan</text>
<text x="683.0" y="48.0" text-anchor="middle" font-size="10">the Phase E and F</text>
<text x="683.0" y="61.0" text-anchor="middle" font-size="10">Implementation and</text>
<text x="683.0" y="74.0" text-anchor="middle" font-size="10">Migration Plan</text>
<rect x="15" y="100" width="586" height="28" rx="6" fill="#f1f1f1" stroke="#999"/>
<text x="308.0" y="117.5" text-anchor="middle" font-size="10">Phase A — the “Assess Readiness for Business Transformation” step; results join the Capability Assessment</text>
<rect x="615" y="100" width="130" height="28" rx="6" fill="#f1f1f1" stroke="#999"/>
<text x="680.0" y="117.5" text-anchor="middle" font-size="10">Phase E and F</text>
<line x1="680" y1="128" x2="680" y2="150" stroke="#555" marker-end="url(#arr-f5-14a)"/>
<rect x="300" y="152" width="445" height="34" rx="6" fill="#f3e3f7" stroke="#b58ac9"/>
<text x="522.5" y="166.0" text-anchor="middle" font-size="10">Phase G — factors monitored, corrective action through IT governance;</text>
<text x="522.5" y="179.0" text-anchor="middle" font-size="10">the assessment is a living document</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">Factors → maturity model → rating → risk → plan, and where each lands in the ADM. Original drawing; activities per TECH §7.1, rating per TECH §7.4, phases per TECH §7.5 and ADM §3.3.5.</figcaption>
</figure>

### Where it lands in the ADM

The assessment is a step of **Phase A**; its results are added to the Capability Assessment and
used to shape scope, identify activities and flag risk areas (ADM §3.3.5). It is a key input to
migration planning, initiated in Phase E and completed in Phase F; note whether transformation
actions sit on the critical path. The factors are monitored in **Phase G** with corrective action
through IT governance, and the assessment is a living document (TECH §7.5). In Phase E the
findings are reviewed for their impact on the roadmap and strategy, and risks are documented in
the Consolidated Gaps, Solutions, and Dependencies matrix (ADM §9.3.7). The Architecture
Definition should not be widely circulated until transformation issues are identified and
mitigated; the workshops are part of the Communications Plan and give participants ownership
(TECH §7.6).

## Risk management

Risk always accompanies transformation, so risks are identified, classified and mitigated before
starting and tracked throughout; triggers may lie outside the planners' scope (a merger), so the
context is monitored constantly. The architect may identify and mitigate risks, but risks must
first be **accepted and then managed within the governance framework**. Two levels are
distinguished — **initial** (before mitigation) and **residual** (after mitigation) — and the
process is: classification, identification, initial assessment, mitigation and residual
assessment, monitoring (TECH §8.1).

**Classification.** Risk is present in every ADM phase. A common classification is by impact on
the organisation, so that certain impacts go to certain levels of governance. Risks are normally
classified as time (schedule), cost (budget) and scope, and may include contractual,
technological, personnel, client-acceptance and other kinds; classifying by architecture domain is
another useful way. EA risks are corporate risks and should be managed the same way (TECH §8.2).

**Identification.** Maturity and readiness assessments generate many risks; CMMs help find
baseline and target states and the actions between them. Risks are documented in a Risk Management
Plan, using templates from PMBOK, PRINCE2 or similar (TECH §8.3).

**Initial assessment.** Classify each risk by **effect** and **frequency**, then combine them into
an impact (TECH §8.4):

| Effect | Frequency | Combined impact |
|---|---|---|
| Catastrophic · Critical · Marginal · Negligible | Frequent · Likely · Occasional · Seldom · Unlikely | Extremely High (E) · High (H) · Moderate (M) · Low (L) |

**Mitigation and residual assessment.** Mitigation is identifying, planning and carrying out
actions that reduce risk to an acceptable level — from simple monitoring or acceptance to a full
business-continuity contingency plan — taking frequent, high-impact risks first (TECH §8.5).
After mitigation is chosen, re-assess effect and frequency and recalculate; what remains is the
residual risk. The mitigation must genuinely reduce corporate impact, not shift the risk to an
equally bad cell: frequent/catastrophic becoming frequent/critical is still extremely high and the
mitigation must be reconsidered. Expensive mitigation that buys little should be challenged. The
deliverable is a transformation risk assessment worksheet (TECH §8.6).

<figure class="my-4">
<svg viewBox="0 0 760 198" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="Risk flows from an initial assessment of effect and frequency, through mitigation, to a residual assessment, looping back when the mitigation has not reduced the impact">
<defs><marker id="arr-f5-14b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
<rect x="15" y="24" width="170" height="34" rx="6" fill="#fff" stroke="#666"/>
<text x="100.0" y="38.0" text-anchor="middle" font-size="10" font-weight="bold">Effect</text>
<text x="100.0" y="51.0" text-anchor="middle" font-size="10">catastrophic … negligible</text>
<rect x="15" y="76" width="170" height="34" rx="6" fill="#fff" stroke="#666"/>
<text x="100.0" y="90.0" text-anchor="middle" font-size="10" font-weight="bold">Frequency</text>
<text x="100.0" y="103.0" text-anchor="middle" font-size="10">frequent … unlikely</text>
<path d="M185 41 L205 41 L205 67 L223 67" fill="none" stroke="#555" marker-end="url(#arr-f5-14b)"/>
<path d="M185 93 L205 93 L205 67" fill="none" stroke="#555"/>
<rect x="225" y="24" width="130" height="86" rx="6" fill="#fff1d6" stroke="#e0b060"/>
<text x="290.0" y="56.9" text-anchor="middle" font-size="11" font-weight="bold">Initial risk</text>
<text x="290.0" y="70.8" text-anchor="middle" font-size="11">impact:</text>
<text x="290.0" y="84.8" text-anchor="middle" font-size="11">E · H · M · L</text>
<line x1="355" y1="67" x2="385" y2="67" stroke="#555" marker-end="url(#arr-f5-14b)"/>
<rect x="387" y="24" width="170" height="86" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="472.0" y="51.0" text-anchor="middle" font-size="10" font-weight="bold">Mitigation</text>
<text x="472.0" y="64.0" text-anchor="middle" font-size="10">monitor, accept, …</text>
<text x="472.0" y="77.0" text-anchor="middle" font-size="10">up to a contingency plan;</text>
<text x="472.0" y="90.0" text-anchor="middle" font-size="10">frequent high-impact first</text>
<line x1="557" y1="67" x2="585" y2="67" stroke="#555" marker-end="url(#arr-f5-14b)"/>
<rect x="587" y="24" width="158" height="86" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/>
<text x="666.0" y="57.5" text-anchor="middle" font-size="10" font-weight="bold">Residual risk</text>
<text x="666.0" y="70.5" text-anchor="middle" font-size="10">re-assess effect and</text>
<text x="666.0" y="83.5" text-anchor="middle" font-size="10">frequency, recalculate</text>
<path d="M666 110 L666 140 L472 140 L472 112" fill="none" stroke="#c0392b" stroke-dasharray="5 4" marker-end="url(#arr-f5-14b)"/>
<text x="470" y="154" text-anchor="middle" font-size="10" fill="#c0392b">still Extremely High (frequent/catastrophic → frequent/critical)? reconsider the mitigation</text>
<text x="380" y="186" text-anchor="middle" font-size="10" fill="#666">Phase G: residual risks approved through governance, execution of mitigations monitored, worksheets kept current</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">Initial risk, mitigation, residual risk, and the loop back when mitigation only shifts the cell. Original drawing; levels per TECH §8.1, assessment per TECH §8.4 and §8.6, monitoring per TECH §8.7.</figcaption>
</figure>

**Monitoring — Phase G.** Residual risks are approved through IT governance and, where business
acceptance is needed, corporate governance. Execution of mitigations is then monitored to confirm
the enterprise is dealing with residual rather than initial risk; the worksheets are governance
artefacts kept current in Phase G, and critical unmitigated risks may require another full or
partial ADM cycle (TECH §8.7).

> **Trap.** Initial vs residual is the classic question. Risk *monitoring* is Phase G; the
> *assessment* begins in Phase A alongside readiness and is confirmed in Phase E (ADM §9.3.7).

<!-- figures:start -->
## Figures from the standard

The diagrams the cited sections carry, from your local copy of the publication. The exam reproduces these; know what each box is.

<div class="grid gap-4 md:grid-cols-2">
<figure class="max-w-lg"><img src="/figure/TECH:fig-7-1" alt="Figure 7-1: Business Transformation Readiness Assessment — Maturity Model" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 7-1: Business Transformation Readiness Assessment — Maturity Model (TECH)</figcaption></figure>
<figure class="max-w-lg"><img src="/figure/TECH:fig-7-2" alt="Figure 7-2: Summary Table of Business Transformation Readiness Assessment" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 7-2: Summary Table of Business Transformation Readiness Assessment (TECH)</figcaption></figure>
<figure class="max-w-lg"><img src="/figure/TECH:fig-8-1" alt="Figure 8-1: Risk Classification Scheme" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 8-1: Risk Classification Scheme (TECH)</figcaption></figure>
<figure class="max-w-lg"><img src="/figure/TECH:fig-8-2" alt="Figure 8-2: Sample Risk Identification and Mitigation Assessment Worksheet" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 8-2: Sample Risk Identification and Mitigation Assessment Worksheet (TECH)</figcaption></figure>
</div>
<!-- figures:end -->

## Check yourself

- Name the three dimensions of the BTEP readiness rating scheme.
- Which two measures are combined to produce a risk's impact?
- In which phase are the risk worksheets maintained as governance artefacts?
