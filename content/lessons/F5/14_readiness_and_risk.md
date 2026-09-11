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

**Monitoring — Phase G.** Residual risks are approved through IT governance and, where business
acceptance is needed, corporate governance. Execution of mitigations is then monitored to confirm
the enterprise is dealing with residual rather than initial risk; the worksheets are governance
artefacts kept current in Phase G, and critical unmitigated risks may require another full or
partial ADM cycle (TECH §8.7).

> **Trap.** Initial vs residual is the classic question. Risk *monitoring* is Phase G; the
> *assessment* begins in Phase A alongside readiness and is confirmed in Phase E (ADM §9.3.7).

## Check yourself

- Name the three dimensions of the BTEP readiness rating scheme.
- Which two measures are combined to produce a risk's impact?
- In which phase are the risk worksheets maintained as governance artefacts?
