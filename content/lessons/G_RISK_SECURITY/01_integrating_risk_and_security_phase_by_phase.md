---
title: Integrating risk and security, the guide phase by phase
unit: G_RISK_SECURITY
objectives: ["G6.1"]
refs: ["GUIDE:integrating-risk-and-security §1", "GUIDE:integrating-risk-and-security §1.2", "GUIDE:integrating-risk-and-security §1.3", "GUIDE:integrating-risk-and-security §2.8", "GUIDE:integrating-risk-and-security §3", "GUIDE:integrating-risk-and-security §3.1.1", "GUIDE:integrating-risk-and-security §3.1.2", "GUIDE:integrating-risk-and-security §3.2", "GUIDE:integrating-risk-and-security §3.2.1", "GUIDE:integrating-risk-and-security §3.2.3", "GUIDE:integrating-risk-and-security §4", "GUIDE:integrating-risk-and-security §5.1", "GUIDE:integrating-risk-and-security §5.1.3", "GUIDE:integrating-risk-and-security §5.1.4", "GUIDE:integrating-risk-and-security §5.1.5", "GUIDE:integrating-risk-and-security §5.2", "GUIDE:integrating-risk-and-security §5.3", "GUIDE:integrating-risk-and-security §5.4", "GUIDE:integrating-risk-and-security §5.5", "GUIDE:integrating-risk-and-security §5.6", "GUIDE:integrating-risk-and-security §5.7", "GUIDE:integrating-risk-and-security §5.8", "GUIDE:integrating-risk-and-security §5.9", "GUIDE:integrating-risk-and-security §5.10", "TECH §8.1"]
reading_minutes: 12
source: authored
status: draft
---
## When the guide applies

Any scenario in which security has been "bolted on", a regulator or auditor is in the room,
the board asks how much risk it is accepting, or a change in the threat environment arrives
after deployment is pointing at *Integrating Risk and Security within a TOGAF Enterprise
Architecture*. The guide's premise is that security has too long been a separate discipline;
a Security Architecture is a structure of organisational, conceptual, logical and physical
components that achieve and maintain a state of managed risk, it builds on and feeds the
Enterprise Architecture, and doing it right first time is cheaper than bolting it on later, so
security architects and enterprise architects need a common language
(GUIDE:integrating-risk-and-security §1). The guide was developed with the SABSA Institute,
whose framework and Business Attribute model it draws on; SABSA's fundamental idea, that the
Security Architecture exists to facilitate the business, aligns with the standard
(GUIDE:integrating-risk-and-security §2.8).

## Two processes, one broader definition of risk

The ADM Techniques chapter on risk focuses on architecture project risk and is the place for
initial and residual risk, effect and frequency classification and mitigation worksheets
(TECH §8.1). This guide widens the scope to Enterprise Risk Management across business, system,
information, project, privacy, compliance and organisational change risk, with particular
attention to operational risk downstream of the architecture work
(GUIDE:integrating-risk-and-security §1.2). It adopts the ISO 31000 definition: risk is the
effect of uncertainty on objectives, positive and negative; risk management optimises outcomes
by balancing opportunity and threat at strategic, tactical and operational level
(GUIDE:integrating-risk-and-security §3.1.1), and its core ERM concepts are key risk areas,
business impact analysis, risk assessment, the business risk model or risk register, risk
appetite and the risk mitigation or treatment plan
(GUIDE:integrating-risk-and-security §3.1.2).

Information Security Management is the companion process: it defines security objectives,
assigns ownership of information security risks, supports implementation of measures, reports
on status and handles incidents (GUIDE:integrating-risk-and-security §3.2). The guide moves
away from the overloaded confidentiality, integrity, availability triad to the richer,
business-friendly SABSA Business Attribute model, and reframes the question from "is it
secure?" to "is it secure enough?", which risk evaluation answers
(GUIDE:integrating-risk-and-security §3.2.1). Its ISM concepts are grouped by the ISO 27001
categories: context (security domain model, business drivers, law and regulation register,
control framework register, trust framework), leadership (security policy architecture),
planning (security principles, business attribute profile, control objectives, data quality,
risk register, Security Services Catalog), support (resource plan, training and awareness,
standards), operation (classification) and performance evaluation (audit)
(GUIDE:integrating-risk-and-security §3.2.3).

Integrating security is not selecting controls from a checklist; controls are bundled into
security services, which are ABBs guiding SBBs and are described in a Security Services
Catalog: identity and access management, continuity management, security intelligence,
digital forensics, audit, network monitoring, compliance management, training and awareness
(GUIDE:integrating-risk-and-security §1.3). Security is a cross-cutting concern that interacts
with all four domains; it may be organised outside the architecture scope but parts of it must
be developed in an integrated fashion at defined touch-points
(GUIDE:integrating-risk-and-security §4). Security and risk are considered as early as possible
in the lifecycle, and the capabilities to measure security are designed in Phases G and H even
though operation begins after the first cycle (GUIDE:integrating-risk-and-security §3).

## The touch-points by phase

| Phase | Security and risk concepts the guide plants there |
|---|---|
| Preliminary | business drivers affecting security; Security Principles as a subset of the principles; risk appetite, the level of risk accepted and the mitigation strategy for risks above it, expressible as principles or a stand-alone deliverable; key risk areas and business impact analysis; the Security Resource Plan and the mandate of the Security Architect (GUIDE:integrating-risk-and-security §5.1, §5.1.3, §5.1.4, §5.1.5) |
| A | enough security design to satisfy security stakeholders that the end state carries no unknown or unacceptable risk, and budget holders that security enables the benefits; the *complete* list of stakeholders, since all have security concerns; a security blueprint; the Business Attribute Profile as the basis of the business case (§5.2) |
| B | business-level trust, risk and controls: Security Policy Architecture, Security Domain Model, Trust Framework, Risk Assessment producing the Business Risk Model or Risk Register with security classification, the Applicable Law and Regulation Register and the Applicable Control Framework Register (§5.3) |
| C | functional security services in the Security Services Catalog, security classification of assets, data quality as a security requirement (§5.4) |
| D | usually no separate security artefacts, but the Security Architect verifies the controls are included and effective; a security view may be requested that justifies each technology by the risk it mitigates (§5.5) |
| E | security and risk evaluated when sequencing the roadmap, risk owners consulted, work package value including security value; security building blocks become SBBs; existing services re-used only after efficacy is verified; the Risk Mitigation Plan implements a strategy, control, transfer, avoid, delay, compensate, and covers risks the new architecture creates (§5.6) |
| F | migration is itself a business process to secure: a risk assessment and Risk Mitigation Plan limited to the transition, regression planning to reverse a failed migration, and a security impact analysis (§5.7) |
| G | security audit: reviews of processes, designs, code and configuration, and security testing; security training and awareness with documented results (§5.8) |
| H | no tangible outputs but two processes: ERM continuously evaluates the architecture against changed opportunity and threat, and architecture governance decides on minor change or a new iteration; security changes are often more disruptive than simplification or incremental change, a change of risk appetite can trigger a new cycle, and the change board needs security-skilled members (§5.9) |
| Requirements Management | Business Attribute Profiling translates goals and drivers into requirements with metrics and targets; control objectives derived from business objectives; security standards added to the Standards Library (§5.10) |

<figure class="my-4">
<svg viewBox="0 0 760 310" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="10" role="img" aria-label="The ADM phases in a ring with the security and risk concept the guide assigns to each, ERM and ISM as the two processes feeding them, and security services as the ABBs">
<defs><marker id="arr-g6s" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
<rect x="15" y="15" width="150" height="60" rx="8" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="90" y="35" text-anchor="middle" font-weight="bold">ERM (ISO 31000)</text>
<text x="90" y="50" text-anchor="middle">appetite, key risk areas,</text>
<text x="90" y="64" text-anchor="middle">register, mitigation plan</text>
<rect x="15" y="235" width="150" height="60" rx="8" fill="#e3f5e1" stroke="#7fbf7a"/>
<text x="90" y="255" text-anchor="middle" font-weight="bold">ISM (ISO 27001)</text>
<text x="90" y="270" text-anchor="middle">policy, domains, trust,</text>
<text x="90" y="284" text-anchor="middle">services, classification, audit</text>
<g fill="#fff" stroke="#666">
<rect x="200" y="15" width="130" height="44" rx="6"/>
<rect x="345" y="15" width="130" height="44" rx="6"/>
<rect x="490" y="15" width="130" height="44" rx="6"/>
<rect x="625" y="15" width="120" height="44" rx="6"/>
<rect x="200" y="85" width="130" height="44" rx="6"/>
<rect x="345" y="85" width="130" height="44" rx="6"/>
<rect x="490" y="85" width="130" height="44" rx="6"/>
<rect x="625" y="85" width="120" height="44" rx="6"/>
<rect x="200" y="155" width="130" height="44" rx="6"/>
<rect x="345" y="155" width="130" height="44" rx="6"/>
</g>
<text x="265" y="33" text-anchor="middle" font-weight="bold">Preliminary</text><text x="265" y="48" text-anchor="middle">appetite, principles, resources</text>
<text x="410" y="33" text-anchor="middle" font-weight="bold">A</text><text x="410" y="48" text-anchor="middle">all stakeholders, blueprint</text>
<text x="555" y="33" text-anchor="middle" font-weight="bold">B</text><text x="555" y="48" text-anchor="middle">policy, domains, trust, register</text>
<text x="685" y="33" text-anchor="middle" font-weight="bold">C</text><text x="685" y="48" text-anchor="middle">services catalog, classification</text>
<text x="265" y="103" text-anchor="middle" font-weight="bold">D</text><text x="265" y="118" text-anchor="middle">controls verified, security view</text>
<text x="410" y="103" text-anchor="middle" font-weight="bold">E</text><text x="410" y="118" text-anchor="middle">Risk Mitigation Plan, SBBs</text>
<text x="555" y="103" text-anchor="middle" font-weight="bold">F</text><text x="555" y="118" text-anchor="middle">transition risk, regression plan</text>
<text x="685" y="103" text-anchor="middle" font-weight="bold">G</text><text x="685" y="118" text-anchor="middle">security audit, training</text>
<text x="265" y="173" text-anchor="middle" font-weight="bold">H</text><text x="265" y="188" text-anchor="middle">ERM and governance, new cycle?</text>
<text x="410" y="173" text-anchor="middle" font-weight="bold">Requirements Mgmt</text><text x="410" y="188" text-anchor="middle">Business Attribute Profile</text>
<line x1="165" y1="45" x2="200" y2="37" stroke="#555" marker-end="url(#arr-g6s)"/>
<line x1="165" y1="265" x2="200" y2="185" stroke="#555" marker-end="url(#arr-g6s)"/>
<rect x="490" y="155" width="255" height="44" rx="6" fill="#fff1d6" stroke="#e0b060"/>
<text x="617" y="173" text-anchor="middle" font-weight="bold">Security services are ABBs, not checklist items</text>
<text x="617" y="188" text-anchor="middle">Security Services Catalog, logical layer, Phase C (§1.3)</text>
<text x="470" y="245" text-anchor="middle" fill="#666">security is cross-cutting through Business, Data, Application and Technology (§4);</text>
<text x="470" y="262" text-anchor="middle" fill="#666">"is it secure enough?" is answered by risk evaluation against appetite (§3.2.1)</text>
<text x="470" y="290" text-anchor="middle" fill="#666">risk in ADM Techniques is project risk; this guide widens it to operational and enterprise risk (§1.2, TECH §8.1)</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">The guide's concepts placed on the phases, fed by the two processes. Original drawing; the placements follow chapter 5 of the guide.</figcaption>
</figure>

## The three sentences that decide scenarios

First: "In Phase A, it is essential to identify the complete list of all stakeholders ...
Separating security stakeholders ensures that the architecture will address a subset of
stakeholders and a subset of requirements" (GUIDE:integrating-risk-and-security §5.2). An
answer that hands security to the CISO's team alone is wrong on the guide's own terms.

Second: risk appetite is set in the Preliminary Phase and confirmed per project in Phase A,
and it defines both the level accepted and the strategy for risks above it
(GUIDE:integrating-risk-and-security §5.1.3, §5.1.4). Everything downstream, the risk
register's classification, the mitigation plan's choice of transfer or avoid, the Phase H
decision, is measured against it.

Third: in Phase H "a seemingly small security requirement change can easily trigger a new
architecture development cycle", and the change board must comprise suitably security-skilled
individuals (GUIDE:integrating-risk-and-security §5.9). A change in the threat environment or a
new compliance requirement is not automatically incremental.

**Trap.** Phase D usually needs no separate security artefact; the work is verifying that
controls defined earlier are present and effective. An answer that invents a Phase D security
architecture from scratch has the guide's emphasis backwards
(GUIDE:integrating-risk-and-security §5.5).

## How the 5, 3 and 1 differ

| Answer | Why it scores that |
|---|---|
| 5 | Confirms appetite and key risk areas, identifies every stakeholder's security concerns in Phase A, builds the risk register and law and control registers in B, defines security services in C, treats risks in the Phase E Risk Mitigation Plan and plans regression for the migration in F, audits and trains in G, and puts security skills on the change board in H |
| 3 | Right concepts, wrong phase: risk assessed for the first time in Phase D or E, appetite defined after the register, the mitigation plan written in Phase F for the whole architecture instead of the transition |
| 1 | Selects a control framework's checklist as the architecture's security; the guide insists on services as building blocks, chosen by risk against appetite (§1.3, §3.2.1) |
| 0 | Defers security to the implementation project or the CISO; security is a cross-cutting concern developed with the architecture (§1, §4) |

## Where to look in the book

Integrating Risk and Security: §1.2 for the scope of risk, §1.3 for services versus checklists,
§3.1 for ERM concepts, §3.2 for ISM concepts and Business Attributes, §4 for cross-cutting,
§5.1 to §5.10 for the phase-by-phase concepts, each with a "location in the architecture
framework" line that tells you whether the concept lives in the TOGAF deliverables or in the
Security Architecture. ADM Techniques §8 for the project-risk method the guide extends.

## Check yourself

- Which phase introduces the Security Services Catalog, and what is a security service in TOGAF terms?
- What must the Phase F Risk Mitigation Plan be limited to, and what planning must it include?
- Why does the guide reject the CIA triad as the vocabulary for business owners?
