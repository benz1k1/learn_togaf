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

## Check yourself

- Which ISO definition of risk does the security guide adopt, and why does it matter?
- In which phases are the capabilities to *measure* security designed?
- What three things does the ADM not mandate, according to the agility guide?
