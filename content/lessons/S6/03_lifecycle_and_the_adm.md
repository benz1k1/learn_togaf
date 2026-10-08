---
title: "The SABSA Lifecycle and Service Management against the ADM and architecture governance"
unit: S6
objectives: ["S6.3"]
refs: ["SABSA §4", "SABSA §3.6", "GUIDE:integrating-risk-and-security §5.8", "GUIDE:integrating-risk-and-security §5.9", "GUIDE:integrating-risk-and-security §2.8", "WP:w117 §4"]
reading_minutes: 9
source: authored
status: draft
---
## Two loops, one enterprise

TOGAF's ADM and the SABSA Lifecycle are both loops that start with the business, design, deliver, govern and return. They were not written together, but the Open Group and the SABSA Institute have published how they fit (W117, and the TOGAF risk and security guide that grew from it), and the SCF exam expects a candidate to place one against the other without confusing them (WP:w117 §4; GUIDE:integrating-risk-and-security §2.8).

| SABSA Lifecycle phase | ADM phases | What is shared |
|---|---|---|
| Strategy and Planning | Preliminary, A (with Requirements Management) | Drivers, principles, risk appetite, the Business Attributes Profile as Phase A requirements |
| Design | B, C, D | Services, domains, trust, mechanisms, platforms, components — the security content of the three architecture domains |
| Implement | E, F, G | Roadmap and migration planning; implementation under governance; SBBs |
| Manage and Measure | G (compliance), H | Compliance reviews, attribute metrics, change management, the decision to start a new cycle |

(SABSA §4; WP:w117 §4; GUIDE:integrating-risk-and-security §5.)

**Trap:** the boundaries are bands, not lines. Phase G belongs to both Implement (the building is governed) and Manage and Measure (the compliance review produces the first measurement). A question that insists on a one-to-one mapping is testing whether you know the mapping is approximate (WP:w117 §4).

## Strategy and Planning ↔ Preliminary and A

Both start by asking what the business is for. TOGAF's Preliminary Phase establishes the capability, the principles and — per the risk and security guide — the risk appetite and the Security Architect's mandate; Phase A produces the vision and the first requirements. SABSA's Strategy and Planning produces the Contextual and Conceptual layers, and its Business Attributes Profile is what the requirements of Phase A look like when the security architect writes them: each with a metric and a target, ready for Requirements Management to track (SABSA §4, §5; GUIDE:integrating-risk-and-security §5.1, §5.2, §5.10.1).

## Design ↔ B, C and D

SABSA's Design phase runs down the Logical, Physical, Component and Service Management layers; the ADM runs across Business, Data, Application and Technology. The two grids cross rather than coincide: a security *service* (Logical) may be designed in Phase B or C depending on whether it is a business or an application service; a *mechanism* (Physical) in C or D; a *component* in D or E. The crosswalk panels on `/adm/B`, `/adm/C` and `/adm/D` show the cells each phase fills (SABSA §4; GUIDE:integrating-risk-and-security §5.3–5.5).

## Implement ↔ E, F and G

TOGAF separates *deciding* the work (E), *scheduling* it (F) and *governing its delivery* (G). SABSA's Implement phase covers all three, and its contribution is the insistence that the delivered component be verified against the designed mechanism — which is exactly what Phase G's compliance review and the guide's security audit do (SABSA §4; GUIDE:integrating-risk-and-security §5.6–5.8).

## Manage and Measure ↔ G and H, and TOGAF governance

This is where the two frameworks are closest. Set the SABSA Service Management layer beside TOGAF architecture governance:

| SABSA Service Management | TOGAF governance |
|---|---|
| Operational risk management (continuous risk assessment, monitoring, reporting) | Phase H: ERM continuously evaluates the architecture against changed threat and opportunity |
| Change management for controls | Phase H change management; the Architecture Board decides minor change versus new cycle |
| Assurance: evidence that controls meet their targets | Architecture Compliance Reviews; compliance assessments filed in the Governance Log |
| Audit: independent examination | Phase G security audit; the Architecture Board as the hearing body |
| Attribute metrics against performance targets | Performance measurements in the Governance Repository |
| Feedback into Strategy and Planning | A change of risk appetite can trigger a new ADM cycle |

(SABSA §3.6, §4; GUIDE:integrating-risk-and-security §5.8, §5.9.)

The Architecture Contract deserves its own line. TOGAF signs a contract in Phase G between the architecture function and the implementers, fixing deliverables, quality and fitness for purpose. In SABSA terms the contract is the point at which the designed mechanisms and components become *commitments* whose performance the Service Management layer will measure. The contract without measurement is a promise; the measurement without a contract is data nobody owns (GUIDE:integrating-risk-and-security §5.8; SABSA §3.6).

**Trap:** TOGAF's Phase H has *no tangible outputs of its own* in the risk and security guide's account — it runs two processes, ERM and governance, and decides whether to start again. SABSA's Manage and Measure likewise produces measurements and decisions rather than architecture. Do not answer that either phase "produces the Target Architecture" (GUIDE:integrating-risk-and-security §5.9; SABSA §4).

## What each framework adds to the other

| TOGAF brings | SABSA brings |
|---|---|
| A defined method with steps, inputs and outputs per phase | The Business Attributes Profile as the requirement type for security |
| The content framework and repository to hold the artefacts | The Matrix as the completeness check on what the artefacts cover |
| Governance bodies, contracts and compliance levels | Two-way traceability and an assurance framework with measurable targets |
| Phase H change management | Operational risk management as a continuous process |

(WP:w117 §4; GUIDE:integrating-risk-and-security §2.8.)

Unit X2 walks the W117 mapping phase by phase; this lesson's job is only that the two loops are recognised as one.

## Check yourself

- Which ADM phases correspond to SABSA's Design phase, and why is the correspondence a band?
- Name the TOGAF governance element that matches each of assurance, audit and change management.
- What triggers a new ADM cycle from the Manage and Measure loop?

*Source note: written from the SABSA framework as published by the SABSA Institute; section numbers refer to the SABSA White Paper and are to be verified against the registered PDF.*
