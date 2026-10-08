---
title: Three Phase A techniques — business scenarios, readiness assessment and risk management
unit: P3
objectives: ["P3.2"]
refs: ["ADM §3.3.5", "ADM §3.3.10", "ADM §3.5.2", "GUIDE:business-scenarios §1", "GUIDE:business-scenarios §2", "GUIDE:business-scenarios §3.1", "GUIDE:business-scenarios §3.2.5", "GUIDE:business-scenarios §3.3", "GUIDE:business-scenarios §3.3.1", "GUIDE:business-scenarios §6", "GUIDE:business-scenarios §13", "TECH §7.1", "TECH §7.2", "TECH §7.3", "TECH §7.4.2", "TECH §7.4.3", "TECH §7.5", "TECH §7.6", "TECH §8.1", "TECH §8.2", "TECH §8.4", "TECH §8.5", "TECH §8.6", "TECH §8.7"]
reading_minutes: 12
source: authored
status: draft
---
## Which planted fact calls for which technique

Practitioner scenarios in this area plant three kinds of fact and expect three different
techniques in reply. Stakeholders who cannot agree what the problem is, or a sponsor who has
already decided on an answer ("we need an ERP"), call for a **business scenario**. A
change-averse culture, a workforce with narrow skills, a shaky business case or a sponsor who
may not stay the course call for a **Business Transformation Readiness Assessment**. A hard
deadline, a regulator, a dependency on a merger or a technology nobody has run before call for
**risk management**. The five-point answer applies each to the fact that planted it, in Phase A,
and carries the results into the Statement of Architecture Work and on to Phases E and F
(ADM §3.5.2; ADM §3.3.5; ADM §3.3.10).

<figure class="my-4">
<svg viewBox="0 0 760 290" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="10" role="img" aria-label="Technique placement: three planted facts on the left each map to a technique in the middle and to where its result goes on the right. Disagreement on the problem maps to business scenario, whose output is a SMART requirements statement in the Requirements Repository. Culture, skills and sponsorship map to readiness assessment, whose actions go into the Implementation and Migration Plan and are monitored in Phase G. Deadlines, regulators and unknown technology map to risk management, whose worksheets are governance artefacts kept up to date in Phase G.">
<defs><marker id="arr-p3-03a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
<text x="380" y="18" text-anchor="middle" font-size="12" font-weight="bold">Planted fact → technique → where the result goes</text>
<rect x="10" y="40" width="220" height="64" rx="6" fill="#fff1d6" stroke="#e0b060"/>
<text x="120" y="60" text-anchor="middle" font-weight="bold">Stakeholders disagree on the problem</text>
<text x="120" y="76" text-anchor="middle">or the sponsor has "the answer" already</text>
<text x="120" y="92" text-anchor="middle">(a premise with an unstated question)</text>
<rect x="10" y="120" width="220" height="64" rx="6" fill="#fff1d6" stroke="#e0b060"/>
<text x="120" y="140" text-anchor="middle" font-weight="bold">Culture, skills, funding, sponsorship</text>
<text x="120" y="156" text-anchor="middle">"the last programme stalled",</text>
<text x="120" y="172" text-anchor="middle">"IT has never run anything this size"</text>
<rect x="10" y="200" width="220" height="64" rx="6" fill="#fff1d6" stroke="#e0b060"/>
<text x="120" y="220" text-anchor="middle" font-weight="bold">Deadline, regulator, merger,</text>
<text x="120" y="236" text-anchor="middle">a technology nobody has operated</text>
<text x="120" y="252" text-anchor="middle">(triggers may be outside your control)</text>
<line x1="230" y1="72" x2="268" y2="72" stroke="#555" marker-end="url(#arr-p3-03a)"/>
<line x1="230" y1="152" x2="268" y2="152" stroke="#555" marker-end="url(#arr-p3-03a)"/>
<line x1="230" y1="232" x2="268" y2="232" stroke="#555" marker-end="url(#arr-p3-03a)"/>
<rect x="270" y="40" width="220" height="64" rx="6" fill="#e3f0fb" stroke="#4a7fb5"/>
<text x="380" y="60" text-anchor="middle" font-weight="bold">Business scenario</text>
<text x="380" y="76" text-anchor="middle">problem, environment, outcomes (SMART),</text>
<text x="380" y="92" text-anchor="middle">human actors, computer actors, fit check</text>
<rect x="270" y="120" width="220" height="64" rx="6" fill="#e3f0fb" stroke="#4a7fb5"/>
<text x="380" y="140" text-anchor="middle" font-weight="bold">Readiness assessment</text>
<text x="380" y="156" text-anchor="middle">factors → maturity models → rate urgency,</text>
<text x="380" y="172" text-anchor="middle">status, difficulty → risks and actions</text>
<rect x="270" y="200" width="220" height="64" rx="6" fill="#e3f0fb" stroke="#4a7fb5"/>
<text x="380" y="220" text-anchor="middle" font-weight="bold">Risk management</text>
<text x="380" y="236" text-anchor="middle">classify → identify → effect × frequency</text>
<text x="380" y="252" text-anchor="middle">→ mitigate → residual → monitor</text>
<line x1="490" y1="72" x2="528" y2="72" stroke="#555" marker-end="url(#arr-p3-03a)"/>
<line x1="490" y1="152" x2="528" y2="152" stroke="#555" marker-end="url(#arr-p3-03a)"/>
<line x1="490" y1="232" x2="528" y2="232" stroke="#555" marker-end="url(#arr-p3-03a)"/>
<rect x="530" y="40" width="220" height="64" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/>
<text x="640" y="60" text-anchor="middle" font-weight="bold">Approved by business leaders,</text>
<text x="640" y="76" text-anchor="middle">placed in the Requirements Repository;</text>
<text x="640" y="92" text-anchor="middle">optional part of the Architecture Vision</text>
<rect x="530" y="120" width="220" height="64" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/>
<text x="640" y="140" text-anchor="middle" font-weight="bold">Capability Assessment; actions into the</text>
<text x="640" y="156" text-anchor="middle">Implementation and Migration Plan (E, F);</text>
<text x="640" y="172" text-anchor="middle">monitored in Phase G</text>
<rect x="530" y="200" width="220" height="64" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/>
<text x="640" y="220" text-anchor="middle" font-weight="bold">Mitigation into the SoAW; residual risk</text>
<text x="640" y="236" text-anchor="middle">accepted by governance; worksheets kept</text>
<text x="640" y="252" text-anchor="middle">up to date in Phase G</text>
<text x="380" y="282" text-anchor="middle" font-size="9">All three are Phase A activities whose results travel forward; none of them ends in Phase A.</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">Original drawing. Business scenario steps and destination follow GUIDE:business-scenarios §3.1 and §3.3; readiness follows TECH §7.1, §7.4.2, §7.4.3 and §7.5; risk follows TECH §8.1, §8.4 to §8.7; the Phase A steps are ADM §3.3.5 and §3.3.10.</figcaption>
</figure>

## Business scenarios: turning a premise into requirements

A business scenario is a uniform description of real business problems, the business and
technology environment they occur in, the value streams enabled by capabilities, the desired
outcomes of proper execution, and the human and computing actors who provide the capabilities.
A good one is SMART — specific, measurable, actionable, realistic, time-bound — and the method
is used principally in the Preliminary, Architecture Vision and Business Architecture phases
(GUIDE:business-scenarios §1). It exists because an architecture built on an incomplete set of
requirements can misguide the work, leave the business value unclear and make the relevance of
solutions unclear; and because involving line management early buys their support
(GUIDE:business-scenarios §2).

Creating one is six steps that capture the five elements: identify, document and rank the
problem; identify the business and technical environment and document it in models including
value streams and capabilities; identify desired outcomes and make them SMART; identify the
human actors; identify the computer actors; and check fitness for purpose, refining only if
necessary (GUIDE:business-scenarios §3.1). The steps repeat across three phases — premise
formulation, initial verification, refinement — and the released scenario is placed in the
Requirements Repository as the high-level requirements statement that drives the architecture
work and validates its quality (GUIDE:business-scenarios §3.3).

The premise-formulation phase is where the sponsor's "we should implement an ERP" is treated as
a premise that presumes an answer to an unstated question — do ERPs actually solve the
interoperability problem? Its triggers include "problem looking for a solution", "solution
looking for a problem", "dominance of technology speak" and "we just don't know how to start"
(GUIDE:business-scenarios §3.3.1). The reviewing step feeds results back to the sponsors to
create a shared understanding of the problem's scope and the depth of technical impact — the
goal is buy-in or stop, because the absence of shared expectations is a root cause of project
failure (GUIDE:business-scenarios §3.2.5).

**Trap.** Business scenarios figure most prominently in Phase A and are also used in Phase B to
derive the architecture from high-level requirements; they can be used in any phase where
requirements must be derived, including the Preliminary Phase to define requirements for the
EA capability itself. An answer that confines them to Phase A is a near miss
(GUIDE:business-scenarios §6). And they are a tool, not the objective — watch for feature creep
and "getting lost in them" (GUIDE:business-scenarios §13).

## Readiness: the human element, quantified

Innovative Visions and Definitions entail considerable change, and the human element is the
most important dimension of it; a sound architecture "could go nowhere" against a change-averse
culture and a narrowly skilled workforce. The five recommended activities are: determine the
readiness factors; present them using maturity models; assess them, including ratings; assess
the risk of each factor and identify improvement actions; and work those actions into the
Phase E and F Implementation and Migration Plan (TECH §7.1).

The factors are determined in a facilitated workshop with people from across the organisation,
starting from a tentative list to reuse, reject or replace. The example set: vision; desire,
willingness and resolve; need; business case; funding; sponsorship and leadership; governance;
accountability; workable approach and execution model; IT capacity to execute; enterprise
capacity to execute; enterprise ability to implement and operate (TECH §7.2). Each factor is
turned into a maturity model so participants can rate current maturity, the target level needed
for the Target Architecture, and an intermediate achievable target (TECH §7.3).

Each factor is then rated on three scales: **urgency** (action needed before the initiative can
begin), **readiness status** (low, fair, acceptable, good, high) and **degree of difficulty to
fix** (no action needed, easy, moderate, difficult), summarised in a management table
(TECH §7.4.2). For every factor, derive actions that move it to a favourable state — checking
existing actions before creating new ones — assess the risk with impact and frequency, and
formally incorporate the actions into the emerging Implementation and Migration Plan, where they
are managed as risks and monitored through implementation (TECH §7.4.3).

The assessment is a key input to migration planning that starts in Phase E and completes in
Phase F; note whether transformation actions sit on the critical path, because "there is no
point deploying new IT capability without employees trained to use it"; the factors are
monitored in Phase G and the assessment is a living document (TECH §7.5). Do not circulate the
Architecture Definition widely until the transformation issues are identified, mitigated and
part of a marketing plan for the Vision — and include a Communications Plan for affected staff
(TECH §7.6).

**Trap.** The readiness result is *added to the Capability Assessment* and used to shape the
scope, identify project activities and identify risk areas — it is not a separate deliverable
that sits beside the Vision (ADM §3.3.5).

## Risk: two levels, one governance framework

Every transformation carries risk; it must be identified, classified and mitigated before
starting so that it can be tracked throughout. The architect may identify and mitigate risks,
but "it is within the governance framework that risks have to be first accepted and then
managed". Two levels are always distinguished: the initial level, before mitigation, and the
residual level, after it. The process runs classification, identification, initial assessment,
mitigation with residual assessment, and monitoring (TECH §8.1).

Classification is commonly by impact on the organisation (with certain impacts escalating to
certain governance levels), by time, cost and scope, or by architecture domain; EA risks are
corporate risks and should be managed the corporate way (TECH §8.2). Initial assessment
combines **effect** — catastrophic, critical, marginal, negligible — with **frequency** —
frequent, likely, occasional, seldom, unlikely — into an impact class: extremely high, high,
moderate or low risk (TECH §8.4). Mitigation ranges from simple monitoring or acceptance to a
full contingency plan, with priority to frequent, high-impact risks (TECH §8.5).

After mitigation, re-assess effect and frequency: the effort must actually reduce corporate
impact, not move the risk to a similarly high quadrant — frequent/catastrophic to
frequent/critical is still extremely high risk — and expensive mitigation for little residual
change should be challenged. The deliverable is a transformation risk assessment worksheet
(TECH §8.6). Residual risks are approved by the IT governance framework, and by corporate
governance where business acceptance is required; the worksheets are governance artefacts kept
up to date in Phase G, where implementation governance may find unmitigated critical risks that
need another full or partial ADM cycle (TECH §8.7).

**Trap.** Readiness factors *generate* risks — the maturity and readiness assessments "will
generate a great many risks" — so the two techniques are chained, not alternatives. An answer
that runs readiness and then omits the risk step has left the chain half done (TECH §7.4.3).

## How the 5-point answer differs from the 3-point one

| Points | What the answer does |
|---|---|
| 5 | Uses a business scenario to test the premise and produce SMART outcomes with the sponsors; runs the readiness workshop, rates factors, derives actions and folds them into the plan and the Capability Assessment; assesses initial risk by effect and frequency, plans mitigation, checks residual risk, and has governance accept it |
| 3 | Applies the right technique to the right fact but stops early — the scenario without a sponsor readout, readiness without actions in the E/F plan, risk without a residual assessment |
| 1 | Runs one technique for every fact (a risk register for a disagreement about the problem), or does readiness in Phase E instead of A |
| 0 | Accepts the sponsor's premise as the requirement, or announces the Vision before the HR consequences are planned |

## Where to look in the book

Series Guide: Business Scenarios §1 (what and SMART), §2 (why), §3.1 (six steps), §3.3 (three
phases and the Requirements Repository), §3.3.1 (premise triggers), §3.2.5 (buy-in or stop),
§6 (where in the ADM), §13. ADM Techniques §7.1 (activities), §7.2 (factors), §7.3 (maturity
models), §7.4.2 (ratings), §7.4.3 (actions), §7.5 (migration planning and Phase G), §7.6
(circulation); §8.1 (two levels), §8.2, §8.4 (effect and frequency), §8.5, §8.6 (residual),
§8.7 (Phase G). ADM §3.3.5 and §3.3.10 for the Phase A steps that call them.
