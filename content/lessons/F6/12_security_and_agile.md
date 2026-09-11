---
title: Security in the ADM, and using the ADM with agile methods — a summary
unit: F6
objectives: ["6.3"]
refs: ["GUIDE:integrating-risk-and-security §1", "GUIDE:integrating-risk-and-security §1.2", "GUIDE:integrating-risk-and-security §1.3", "GUIDE:integrating-risk-and-security §3", "GUIDE:integrating-risk-and-security §4", "GUIDE:integrating-risk-and-security §5.1", "GUIDE:integrating-risk-and-security §5.2", "GUIDE:integrating-risk-and-security §5.3", "GUIDE:integrating-risk-and-security §5.4", "GUIDE:integrating-risk-and-security §5.5", "GUIDE:integrating-risk-and-security §5.6", "GUIDE:integrating-risk-and-security §5.7", "GUIDE:integrating-risk-and-security §5.8", "GUIDE:integrating-risk-and-security §5.9", "GUIDE:enabling-enterprise-agility §2.4", "GUIDE:enabling-enterprise-agility §3", "GUIDE:enabling-enterprise-agility §4.1", "GUIDE:enabling-enterprise-agility §4.2", "GUIDE:enabling-enterprise-agility §4.5", "GUIDE:enabling-enterprise-agility §4.7", "GUIDE:agile-sprints §2", "GUIDE:agile-sprints §3.1", "GUIDE:agile-sprints §3.3", "GUIDE:agile-sprints §4.4", "GUIDE:agile-sprints §4.5", "GUIDE:agile-sprints §5.3", "GUIDE:agile-sprints §5.4"]
reading_minutes: 12
source: authored
status: draft
---
> Both topics are covered by TOGAF Series Guides rather than the Applying the ADM document. The
> Foundation syllabus asks only for a summary-level understanding.

## Security and risk in the ADM

A **Security Architecture** is a structure of organisational, conceptual, logical and physical
components that interact coherently to achieve and maintain a state of managed risk and security.
Information security has too long been treated as a separate discipline; integrating it into the
Enterprise Architecture from the start is cheaper and more effective than bolting it on later, and
the guide gives Security Architects and Enterprise Architects a common language
(GUIDE:integrating-risk-and-security §1).

**Risk.** The ADM Techniques treatment of risk focuses on *architecture project* risk. Enterprise
Risk Management (ERM) is far broader — business, system, information, project, privacy, compliance
and organisational-change risk — and the guide concentrates on operational risk downstream of the
architecture. It adopts the ISO 31000 definition, risk as "the effect that uncertainty has on the
achievement of business objectives", which covers positive opportunities as well as negative
consequences; security practitioners usually treat risk as threat-bound and negative
(GUIDE:integrating-risk-and-security §1.2). A Security Architecture keeps a balanced view — negative
consequences at an acceptable level, opportunities exploited — and is business-driven: business
drivers give the context for risk assessment and justify security measures; security and risk are
considered as early as possible in the lifecycle, and the capabilities to measure security are
designed in Phases G and H (GUIDE:integrating-risk-and-security §3).

**No checklist.** Integrating security is not selecting controls from a list. In architecture
terms controls are bundled into **security services**, which are ABBs guiding SBBs across all four
domains — identity and access management, continuity, audit, network monitoring and so on —
described in a **Security Services Catalog** and positioned in the logical layer developed in
Phase C (GUIDE:integrating-risk-and-security §1.3).

**Cross-cutting.** Security Architecture is a cross-cutting concern pervading the whole Enterprise
Architecture: a coherent collection of views, viewpoints and artifacts that interacts with — and
informs — all four domains. It may be organised outside the architecture scope, but parts must be
developed integrally with it (GUIDE:integrating-risk-and-security §4).

| Phase | Security and risk emphasis |
|---|---|
| Preliminary | Establish the security context: security-relevant business drivers, Security Principles (a subset of the architecture principles), risk appetite, key risk areas / business impact analysis, security resource plan (§5.1) |
| A | Enough security design to satisfy security stakeholders that the end-state carries no unknown or unacceptable risk, and business stakeholders that security enables the benefits; **all** stakeholders have security concerns, so do not separate off "security stakeholders"; build on Security Principles, drivers, key risks and risk appetite (§5.2) |
| B | Business-level trust, risk and controls independent of IT: security policy architecture, security domain model, trust framework, risk assessment, business risk model / risk register, applicable law and regulation register, control framework register (§5.3) |
| C | Functional security services and security classification of assets (§5.4) |
| D | Usually no separate artifacts; verify the controls defined earlier are included and effective, including provision of system resources such as power, capacity and bandwidth; a security view may be requested (§5.5) |
| E | Evaluate security and risk when sequencing gaps; consult risk owners; security building blocks become SBBs; verify existing security services earmarked for re-use (§5.6) |
| F | Migration is itself a business process to secure: risk assessment and a Risk Mitigation Plan limited to the transition, regression planning to reverse a failed migration, and a security impact analysis (§5.7) |
| G | Assurance that design and implementation adhere to the Security Architecture: security audit, security training and awareness (§5.8) |
| H | No tangible security outputs, but two essential processes — ERM continuously evaluating the architecture against changing opportunity and threat, and architecture governance deciding changes; a small security change (a changed risk appetite) can trigger a whole new ADM cycle, and the change board needs security-skilled members (§5.9) |

(GUIDE:integrating-risk-and-security §5.1–§5.9)

<figure class="my-4">
<svg viewBox="0 0 760 178" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="Security and risk touchpoints in every phase of the ADM from the Preliminary Phase to H, over a cross-cutting bar spanning all four domains">
<defs><marker id="arr-f6-12a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
<rect x="15" y="12" width="76" height="28" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="53.0" y="30.2" text-anchor="middle" font-size="12" font-weight="bold">Prelim</text>
<text x="53" y="60" text-anchor="middle" font-size="9" fill="#333">security context,</text>
<text x="53" y="73" text-anchor="middle" font-size="9" fill="#333">Security Principles,</text>
<text x="53" y="86" text-anchor="middle" font-size="9" fill="#333">risk appetite</text>
<rect x="97" y="12" width="76" height="28" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="135.0" y="30.2" text-anchor="middle" font-size="12" font-weight="bold">A</text>
<text x="135" y="60" text-anchor="middle" font-size="9" fill="#333">no unknown or</text>
<text x="135" y="73" text-anchor="middle" font-size="9" fill="#333">unacceptable risk;</text>
<text x="135" y="86" text-anchor="middle" font-size="9" fill="#333">every stakeholder</text>
<rect x="179" y="12" width="76" height="28" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="217.0" y="30.2" text-anchor="middle" font-size="12" font-weight="bold">B</text>
<text x="217" y="60" text-anchor="middle" font-size="9" fill="#333">trust, risk and</text>
<text x="217" y="73" text-anchor="middle" font-size="9" fill="#333">controls; risk and</text>
<text x="217" y="86" text-anchor="middle" font-size="9" fill="#333">law registers</text>
<rect x="261" y="12" width="76" height="28" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="299.0" y="30.2" text-anchor="middle" font-size="12" font-weight="bold">C</text>
<text x="299" y="60" text-anchor="middle" font-size="9" fill="#333">security services;</text>
<text x="299" y="73" text-anchor="middle" font-size="9" fill="#333">asset</text>
<text x="299" y="86" text-anchor="middle" font-size="9" fill="#333">classification</text>
<rect x="343" y="12" width="76" height="28" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="381.0" y="30.2" text-anchor="middle" font-size="12" font-weight="bold">D</text>
<text x="381" y="60" text-anchor="middle" font-size="9" fill="#333">verify the controls</text>
<text x="381" y="73" text-anchor="middle" font-size="9" fill="#333">are present</text>
<text x="381" y="86" text-anchor="middle" font-size="9" fill="#333">and effective</text>
<rect x="425" y="12" width="76" height="28" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="463.0" y="30.2" text-anchor="middle" font-size="12" font-weight="bold">E</text>
<text x="463" y="60" text-anchor="middle" font-size="9" fill="#333">sequence gaps</text>
<text x="463" y="73" text-anchor="middle" font-size="9" fill="#333">with risk; re-use</text>
<text x="463" y="86" text-anchor="middle" font-size="9" fill="#333">security SBBs</text>
<rect x="507" y="12" width="76" height="28" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="545.0" y="30.2" text-anchor="middle" font-size="12" font-weight="bold">F</text>
<text x="545" y="60" text-anchor="middle" font-size="9" fill="#333">secure the</text>
<text x="545" y="73" text-anchor="middle" font-size="9" fill="#333">migration: risk and</text>
<text x="545" y="86" text-anchor="middle" font-size="9" fill="#333">regression plans</text>
<rect x="589" y="12" width="76" height="28" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="627.0" y="30.2" text-anchor="middle" font-size="12" font-weight="bold">G</text>
<text x="627" y="60" text-anchor="middle" font-size="9" fill="#333">assurance: audit,</text>
<text x="627" y="73" text-anchor="middle" font-size="9" fill="#333">training and</text>
<text x="627" y="86" text-anchor="middle" font-size="9" fill="#333">awareness</text>
<rect x="671" y="12" width="76" height="28" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="709.0" y="30.2" text-anchor="middle" font-size="12" font-weight="bold">H</text>
<text x="709" y="60" text-anchor="middle" font-size="9" fill="#333">ERM + change</text>
<text x="709" y="73" text-anchor="middle" font-size="9" fill="#333">governance; may</text>
<text x="709" y="86" text-anchor="middle" font-size="9" fill="#333">trigger a new cycle</text>
<rect x="15" y="112" width="730" height="30" rx="6" fill="#fff1d6" stroke="#e0b060"/>
<text x="380.0" y="130.8" text-anchor="middle" font-size="11">Security Architecture: a cross-cutting concern over Business, Data, Application and Technology — not a fifth domain</text>
<text x="380" y="166" text-anchor="middle" font-size="10" fill="#666">Risk appetite set in the Preliminary Phase frames every later decision; measurement capabilities are designed in G and H</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">One security emphasis per phase, over the cross-cutting bar. Original drawing; touchpoints per GUIDE:integrating-risk-and-security §5.1 to §5.9, cross-cutting per §4.</figcaption>
</figure>

> **Trap.** Security is not a fifth architecture domain; it is a cross-cutting concern across
> Business, Data, Application and Technology (GUIDE:integrating-risk-and-security §4).

## Using the ADM with agile

The ADM graphic looks like a lengthy waterfall, but the ADM does **not** mandate that steps run in
the order shown, does not mandate that a phase completes before the next begins, and does not
specify the duration of any phase or cycle; it is better read as a reference model of what must be
done — architects *understand* (A–D), *specify* (E–F) and *govern* (G–H). Agility is one of the
needs the ADM is adapted to (GUIDE:enabling-enterprise-agility §3).

Key definitions: a **Minimum Viable Architecture** is just enough architecture to deliver product
features in a given phase and satisfy known — especially quality-attribute — requirements, and no
more (GUIDE:enabling-enterprise-agility §2.4). A **sprint** is a short, time-boxed period in which
an agile team completes a set amount of work towards a working solution; a **backlog** is the
evolving, stakeholder-prioritised list of requirements; a **retrospective** examines the team's
process at the end of a sprint; **DORP** is the end-of-sprint set of demo, outcome management,
retrospective and planning (GUIDE:agile-sprints §2).

**Levels enable agility.** The three landscape levels — Enterprise Strategic, Segment, Capability —
must not be confused with the domains, which exist at every level. Strategic architecture gives the
broad context; segments provide direction at portfolio, program or product level; **Capability
Architectures** are detailed increments of business capability, tightly scoped to fit sprint time
boxes, and may align to one or several sprints. Feedback from delivered increments flows back up,
and the Strategic Architecture must evolve as strategy does (GUIDE:enabling-enterprise-agility
§4.1). A Transition Architecture — one state at an architecturally significant point, usually
holding several capability increments — is related to a release of business value and helps manage
risk (GUIDE:enabling-enterprise-agility §4.2).

Each level may cycle through all phases but focuses differently: the Strategic level on the
Preliminary Phase and A/B (courses of action, strategic themes); the Segment level on partitioning
courses of action across organisation units, with more B/C/D detail producing epics and a segment
backlog; the Capability level on B–D for ABBs, E–F for SBBs and contracts, completion in G and
benefits confirmation in H. Sprint backlogs are refined to units deliverable in weeks, at most a
month; pushing beyond the architecture runway creates technical debt, which Phase H must manage
(GUIDE:enabling-enterprise-agility §4.5). Agile is one delivery style among several — rapid
(solution–iteration), agile (backlog–sprint), robust small-scale (PRINCE project–stage) and robust
large-scale (MSP program–project) — and the ADM accommodates them all
(GUIDE:enabling-enterprise-agility §4.7).

**Sprints with the ADM.** Sprints suit the ADM because competition demands speed, short cycles
absorb late-arriving information and risk, decisions rest on what is known and on real outcomes,
and monolithic waterfall delivery is a recognised anti-pattern; adapting means adapting both the
solutions and how the ADM is applied (GUIDE:agile-sprints §3.1). Four collaboration patterns are
offered: **Enterprise Architecture development agility** (A–F delivered as sprints of ADM slices),
**solution collaboration** (EA and solution sprints together; EA creates MVAs), **cross-development
collaboration** (business, EA and solution sprints; MVBDs and MVAs) and **cross-functional agility**
(mixed teams with all competencies) (GUIDE:agile-sprints §3.3).

In sprints, Phase G compliance becomes an **ongoing, less formal** process rather than a gate, and
short cycles expose non-compliance early; an increment can be deployed after each approved demo
(GUIDE:agile-sprints §4.4). Phase H splits into a value-realisation process with monitoring tools
and a change-management process that runs in parallel with the sprints, collecting risks from
demos and retrospectives (GUIDE:agile-sprints §4.5). Sprints last one to four weeks — generally two
— and should be fixed in length for predictable planning; a set of transition architectures can act
as releases, akin to an Agile Release Train (GUIDE:agile-sprints §5.3). Governance moves into the
sprint process and becomes mutual accountability; decisions that can be rolled back are delegated
to teams, irreversible ones go to the wider stakeholder group (GUIDE:agile-sprints §5.4).

<figure class="my-4">
<svg viewBox="0 0 760 262" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="The ADM with agile: understand, specify and govern across the phases; the three levels narrowing to sprint-sized capability increments; Phase G and H reshaped for sprints">
<defs><marker id="arr-f6-12b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
<rect x="15" y="12" width="240" height="28" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="135.0" y="29.9" text-anchor="middle" font-size="11" font-weight="bold">understand — A to D</text>
<rect x="265" y="12" width="240" height="28" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/>
<text x="385.0" y="29.9" text-anchor="middle" font-size="11" font-weight="bold">specify — E to F</text>
<rect x="515" y="12" width="230" height="28" rx="6" fill="#f3e3f7" stroke="#b58ac9"/>
<text x="630.0" y="29.9" text-anchor="middle" font-size="11" font-weight="bold">govern — G to H</text>
<rect x="15" y="56" width="240" height="32" rx="6" fill="#fff" stroke="#666"/>
<text x="135.0" y="75.8" text-anchor="middle" font-size="11"></text>
<text x="25" y="76" text-anchor="start" font-size="11" fill="#222" font-weight="bold">Strategic</text>
<text x="110" y="76" text-anchor="start" font-size="10" fill="#333">Preliminary Phase, A/B: courses of action, strategic themes</text>
<rect x="15" y="96" width="490" height="32" rx="6" fill="#fff" stroke="#666"/>
<text x="260.0" y="115.8" text-anchor="middle" font-size="11"></text>
<text x="25" y="116" text-anchor="start" font-size="11" fill="#222" font-weight="bold">Segment</text>
<text x="110" y="116" text-anchor="start" font-size="10" fill="#333">B/C/D detail across organisation units → epics, a segment backlog</text>
<rect x="15" y="136" width="730" height="32" rx="6" fill="#fff" stroke="#666"/>
<text x="380.0" y="155.8" text-anchor="middle" font-size="11"></text>
<text x="25" y="156" text-anchor="start" font-size="11" fill="#222" font-weight="bold">Capability</text>
<text x="110" y="156" text-anchor="start" font-size="10" fill="#333">B–D ABBs · E–F SBBs and contracts · G completion · H benefits; scoped to sprint time boxes</text>
<line x1="745" y1="175" x2="745" y2="60" stroke="#999" stroke-dasharray="4 3" marker-end="url(#arr-f6-12b)"/>
<text x="700" y="190" text-anchor="end" font-size="9" fill="#666">feedback from delivered increments flows back up</text>
<rect x="15" y="200" width="360" height="50" rx="6" fill="#f3e3f7" stroke="#b58ac9"/>
<text x="195.0" y="215.5" text-anchor="middle" font-size="10" font-weight="bold">Phase G in sprints</text>
<text x="195.0" y="228.5" text-anchor="middle" font-size="10">compliance becomes ongoing and less formal;</text>
<text x="195.0" y="241.5" text-anchor="middle" font-size="10">deploy after each approved demo</text>
<rect x="390" y="200" width="355" height="50" rx="6" fill="#f3e3f7" stroke="#b58ac9"/>
<text x="567.5" y="215.5" text-anchor="middle" font-size="10" font-weight="bold">Phase H in sprints</text>
<text x="567.5" y="228.5" text-anchor="middle" font-size="10">value realisation and change management</text>
<text x="567.5" y="241.5" text-anchor="middle" font-size="10">run alongside the sprints</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">Agile touchpoints: three moves, three levels, and what G and H become in sprints. Original drawing; moves per GUIDE:enabling-enterprise-agility §3, levels per §4.5, G and H per GUIDE:agile-sprints §4.4 and §4.5.</figcaption>
</figure>

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
<figure class="max-w-lg"><img src="/figure/GUIDE:enabling-enterprise-agility:fig-4-2" alt="Figure 4-2: Transition Architectures" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 4-2: Transition Architectures (GUIDE:enabling-enterprise-agility)</figcaption></figure>
<figure class="max-w-lg"><img src="/figure/GUIDE:enabling-enterprise-agility:fig-4-4" alt="Figure 4-4: ADM Levels Mapped to Agile Delivery Concepts" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 4-4: ADM Levels Mapped to Agile Delivery Concepts (GUIDE:enabling-enterprise-agility)</figcaption></figure>
</div>
<!-- figures:end -->

## Check yourself

- Which ISO definition of risk does the security guide adopt, and why does it matter?
- In which phases are the capabilities to *measure* security designed?
- What three things does the ADM not mandate, according to the agility guide?
