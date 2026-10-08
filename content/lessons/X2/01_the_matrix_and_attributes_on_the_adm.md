---
title: "W117: the SABSA Matrix and the Business Attributes Profile on the ADM phases"
unit: X2
objectives: ["X2.1"]
refs: ["WP:w117 §3", "WP:w117 §4", "SABSA §3", "SABSA §5", "GUIDE:integrating-risk-and-security §2.8", "GUIDE:integrating-risk-and-security §5.2", "GUIDE:integrating-risk-and-security §5.10.1", "GUIDE:integrating-risk-and-security §5.11"]
reading_minutes: 9
source: authored
status: draft
---
## What W117 set out to do

The 2011 white paper *TOGAF and SABSA Integration* (W117), written jointly by The Open Group and the SABSA Institute, asked a practical question: an enterprise runs the ADM, and it also has a security architecture team that thinks in SABSA — where does each SABSA artefact go in the ADM? Its answer has two parts. The **SABSA Matrix** layers are laid across the ADM phases, so that each phase knows which cells it is expected to fill; and the **Business Attributes Profile** is adopted as the *form* that security requirements take, from Phase A through Requirements Management. The TOGAF risk and security guide (G152) later absorbed both ideas, which is why the `G_RISK_SECURITY` lesson already reads like a SABSA summary (WP:w117 §3, §4; GUIDE:integrating-risk-and-security §2.8).

## The Matrix across the phases

| ADM phase | SABSA layers | Cells the phase fills | Artefacts (as the crosswalk names them) |
|---|---|---|---|
| Preliminary | Contextual | People, Process | Security governance model, risk-management policy — the policy authority inside the EA capability |
| A | Contextual, Conceptual | Contextual × Motivation; Conceptual × Motivation, × Assets | Business Attributes Profile, risk appetite, business risk model |
| B | Logical | Process, People, Location | Security services catalogue, domain model, trust model |
| C | Logical, Physical | Logical × Assets; Physical × Assets, × Process | Information classification, security mechanisms |
| D | Physical, Component | Physical × Location; Component × Assets, × Process | Mechanisms, products and tools, security standards |
| E | Conceptual, Logical | Conceptual × Time; Logical × Time | Control gap analysis, security roadmap |
| F | Physical, Component | Physical × Time; Component × Time | Control implementation schedule |
| G | Service Management | Process, People | Assurance framework, compliance evidence |
| H | Service Management | Motivation, Time | Security metrics, risk review |
| Requirements Management | Conceptual | Motivation | Business Attributes Profile, maintained across the cycle |

(WP:w117 §4; the per-phase panels on `/adm/{phase}` render the same rows.)

Read down the layer column and the diagonal is obvious: the ADM walks the Matrix top to bottom, then the Service Management row takes over for governance. Read the *Time* column and a second pattern appears: Phases E and F are where SABSA's *When* cells are filled — control gaps and their scheduling — because that is when TOGAF sequences change (WP:w117 §4; SABSA §3).

**Trap:** the Conceptual layer appears in A, E *and* Requirements Management. That is not a mistake in the table; the Business Attributes Profile is created in A, drives the control gap analysis in E, and is maintained by Requirements Management throughout. A question that asks "in which single phase is the Conceptual layer completed" has a false premise (WP:w117 §4; GUIDE:integrating-risk-and-security §5.10.1).

## The Business Attributes Profile as Phase A requirements

W117's central argument is that TOGAF already has a place for SABSA's signature artefact: the requirements. TOGAF asks Phase A to capture the requirements the vision must satisfy and hands them to Requirements Management; SABSA says a security requirement is a **business attribute** (Available, Confidential, Auditable, Recoverable, Reputable…) with a *metric type*, a *measurement approach* and a *performance target*. Put the two together and the Business Attributes Profile *is* the security section of Phase A's requirements — written in business words, measurable, and owned by a business stakeholder rather than the security team (WP:w117 §3; SABSA §5; GUIDE:integrating-risk-and-security §5.2).

| TOGAF asks for | SABSA supplies |
|---|---|
| Requirements in Phase A, refined in B–D | Business attributes selected from the taxonomy for this engagement |
| Measurable acceptance criteria | Metric type, measurement approach and performance target per attribute |
| A stakeholder who owns each requirement | The business owner of each attribute |
| Requirements Management across the cycle | The profile maintained and re-baselined as drivers change |
| The basis of the business case | Attributes whose targets show what the architecture enables, not only what it prevents |

(WP:w117 §3; GUIDE:integrating-risk-and-security §5.2, §5.10.1.)

The G152 guide keeps the point almost verbatim: business attribute profiling "translates goals and drivers into requirements with metrics and targets", and it is the basis of the business case in Phase A. The `G_RISK_SECURITY` lesson's phase table is the place to see the same idea from the TOGAF side (GUIDE:integrating-risk-and-security §5.10.1).

## The content metamodel and the Matrix

W117 also asked whether the TOGAF content metamodel can *hold* the SABSA cells. Its answer, adopted by the guide, is that the metamodel's motivation entities (driver, goal, objective, requirement) and its extension mechanism accommodate business attributes, control objectives and security services without a second repository: attributes are requirements, security services are ABBs in the Security Services Catalog, and domains and trust relationships are relationships between actors, roles and locations (WP:w117 §4; GUIDE:integrating-risk-and-security §5.11).

**Trap:** the integration does not add phases. There is no "security phase" of the ADM; W117 and G152 both insist that security is a cross-cutting concern inside every existing phase, with the Security Architect as a stakeholder of each. An answer that inserts a phase is wrong in both frameworks (GUIDE:integrating-risk-and-security §4).

## Using the mapping to study

- When a TOGAF question asks what security content Phase B produces, answer with the Logical layer's cells: services, domain model, trust.
- When an SCF question asks where in an EA method the Business Attributes Profile would appear, answer Phase A and Requirements Management.
- When either asks how governance meets the Service Management layer, answer Phases G and H (WP:w117 §4; SABSA §3.6).

## Check yourself

- Which Matrix layers does Phase D fill, and which artefacts?
- Why does the Conceptual layer appear in three places on the phase table?
- In what form does W117 say security requirements enter Phase A?
