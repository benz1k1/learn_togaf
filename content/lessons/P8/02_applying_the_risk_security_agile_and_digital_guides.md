---
title: Applying the risk and security, agile and digital guides to a situation
unit: P8
objectives: ["P8.2"]
refs: ["GUIDE:integrating-risk-and-security §1.3", "GUIDE:integrating-risk-and-security §3.1.1", "GUIDE:integrating-risk-and-security §4", "GUIDE:integrating-risk-and-security §5.1.3", "GUIDE:integrating-risk-and-security §5.2", "GUIDE:integrating-risk-and-security §5.6.1", "GUIDE:integrating-risk-and-security §5.9", "GUIDE:enabling-enterprise-agility §4.1", "GUIDE:enabling-enterprise-agility §4.4.4", "GUIDE:enabling-enterprise-agility §4.7.1", "GUIDE:agile-sprints §3.3", "GUIDE:agile-sprints §3.3.4", "GUIDE:agile-sprints §4.4", "GUIDE:digital-technology-adoption §4", "GUIDE:digital-technology-adoption §5.1", "GUIDE:digital-technology-adoption §5.4", "GUIDE:using-the-togaf-standard-in-the-digital-enterprise §4.2", "GUIDE:digital-business-reference-model §3.1"]
reading_minutes: 11
source: authored
status: draft
---
## Which guide is the scenario pointing at?

Objective P8.2 asks you to apply three families of guides. The scenario rarely names them; it
plants a cue. Learn the cues and the guide answers itself.

| Cue in the scenario | Guide family | What the five-point answer does |
|---|---|---|
| a breach, a regulator, "how much risk will the board accept", privacy, controls | Integrating Risk and Security | treats security as a cross-cutting concern, uses the ERM and ISM concepts at the right phase: risk appetite and key risk areas in Preliminary, all stakeholders' security concerns in A, risk assessment and registers in B, Security Services Catalog and classification in C, Risk Mitigation Plan in E, regression planning in F, audit in G, security-skilled governance in H |
| sprints, product owner, "the architecture team is a bottleneck", backlog | Enabling Enterprise Agility and Applying the ADM using Agile Sprints | partitions by Strategic, Segment and Capability Architecture, delivers just-enough Minimum Viable Architecture just in time, embeds governance in sprints, chooses a collaboration pattern and a delivery style that matches risk |
| "go digital", cloud adoption, DPBoK, a start-up inside a corporate, a new digital product | Digital Technology Adoption, Using the TOGAF Standard in the Digital Enterprise, Digital Business Reference Model | runs a readiness assessment before committing, selects an adoption approach, matches EA services to the DPBoK context, uses the DBRM's four domains to structure the business view |

## Risk and security, phase by phase

The guide's foundation is a broader definition of risk than the ADM Techniques chapter uses:
risk is the effect of uncertainty on objectives, positive and negative, and enterprise risk
management balances opportunity and threat
(GUIDE:integrating-risk-and-security §3.1.1). Security is a cross-cutting concern that
interacts with all four architecture domains and is more than a dataset, it rests on the ISM
and ERM processes (GUIDE:integrating-risk-and-security §4). Integrating security is not
choosing controls from a checklist; controls are bundled into security services, which are
ABBs that guide SBBs, described in a Security Services Catalog
(GUIDE:integrating-risk-and-security §1.3).

The exam plants the phase. Risk appetite, the enterprise's attitude to risk and the
mitigation strategy for risks above the acceptable level, is set in the Preliminary Phase and
can be expressed as principles or a stand-alone deliverable
(GUIDE:integrating-risk-and-security §5.1.3). In Phase A the *complete* list of stakeholders
is identified, because all stakeholders have security and risk concerns and separating out
"security stakeholders" narrows the requirements; the security blueprint must satisfy the
budget holders that security enables the business benefits
(GUIDE:integrating-risk-and-security §5.2). In Phase E the Risk Mitigation Plan implements a
strategy, increase control, transfer, avoid, delay or compensate, and must also cover risks the
new architecture creates (GUIDE:integrating-risk-and-security §5.6.1). In Phase H a
seemingly small security requirement change, a change of risk appetite for instance, can
trigger a whole new cycle, and the change board must include security-skilled people
(GUIDE:integrating-risk-and-security §5.9).

**Trap.** A scenario that lists "the CISO and the security team" as *the* stakeholders for
security is baiting the Phase A error; the guide says every stakeholder has security concerns
(GUIDE:integrating-risk-and-security §5.2).

## Agility, levels and sprints

The agility guide's first move is the Architecture Landscape: Enterprise Strategic, Segment
and Capability Architectures, not to be confused with the domains, which exist at every level.
Capability Architectures are detailed enough to hand to developers, align to sprints and are
tightly scoped to fit sprint time-boxes; feedback flows bottom-up so higher levels evolve
(GUIDE:enabling-enterprise-agility §4.1). Governance is embedded and continuous, the
governor an intelligent advisor within the team rather than a visiting policeman, providing
guardrails and standards without slowing delivery; deferring governance to the last
iteration loses the benefit of agile (GUIDE:enabling-enterprise-agility §4.4.4). Not every
change should be agile: Rapid, Agile and Robust delivery styles suit different profiles, and
high-risk, large-scale, long-horizon, quality-driven change is Robust
(GUIDE:enabling-enterprise-agility §4.7.1).

The sprints guide gives four collaboration patterns of increasing maturity: EA development
agility, solution collaboration, cross-development collaboration and cross-functional agility
(GUIDE:agile-sprints §3.3). It recommends a first "sprint zero" that builds the business change
backlog from business needs, value streams, capabilities and a high-level roadmap, makes the
no-regret decisions, and prioritises by value, by risk, by a slice through all ADM phases or
by ease (GUIDE:agile-sprints §3.3.4). In Phase G, compliance becomes an ongoing activity rather
than a gate at a point in time, and a solution increment can be deployed after each approved
demo (GUIDE:agile-sprints §4.4).

<figure class="my-4">
<svg viewBox="0 0 760 300" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="11" role="img" aria-label="Guide selector: a cue in the scenario points to one of three guide families and to the phase or step in which the five-point answer applies it">
<defs><marker id="arr-p8g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
<rect x="240" y="10" width="280" height="36" rx="8" fill="#f1f1f1" stroke="#999"/>
<text x="380" y="33" text-anchor="middle" font-weight="bold">What did the scenario plant?</text>
<line x1="300" y1="46" x2="130" y2="90" stroke="#555" marker-end="url(#arr-p8g)"/>
<line x1="380" y1="46" x2="380" y2="90" stroke="#555" marker-end="url(#arr-p8g)"/>
<line x1="460" y1="46" x2="630" y2="90" stroke="#555" marker-end="url(#arr-p8g)"/>
<text x="180" y="70" text-anchor="middle" fill="#c0392b">threat, regulator, appetite</text>
<text x="380" y="70" text-anchor="middle" fill="#3a7d3a">sprints, backlog, product owner</text>
<text x="580" y="70" text-anchor="middle" fill="#345">digital product, cloud, DPBoK</text>
<rect x="15" y="92" width="230" height="150" rx="8" fill="#fde8e6" stroke="#c0392b"/>
<text x="130" y="112" text-anchor="middle" font-weight="bold">Integrating Risk and Security</text>
<text x="130" y="132" text-anchor="middle">Prelim: appetite, key risk areas, principles</text>
<text x="130" y="148" text-anchor="middle">A: all stakeholders' security concerns</text>
<text x="130" y="164" text-anchor="middle">B: risk register, law and control registers</text>
<text x="130" y="180" text-anchor="middle">C: Security Services Catalog, classification</text>
<text x="130" y="196" text-anchor="middle">E: Risk Mitigation Plan  F: regression planning</text>
<text x="130" y="212" text-anchor="middle">G: security audit, training</text>
<text x="130" y="228" text-anchor="middle">H: security change may trigger a new cycle</text>
<rect x="265" y="92" width="230" height="150" rx="8" fill="#e3f5e1" stroke="#7fbf7a"/>
<text x="380" y="112" text-anchor="middle" font-weight="bold">Agility and Sprints</text>
<text x="380" y="132" text-anchor="middle">Strategic, Segment, Capability levels</text>
<text x="380" y="148" text-anchor="middle">Minimum Viable Architecture, just in time</text>
<text x="380" y="164" text-anchor="middle">sprint zero builds the business change backlog</text>
<text x="380" y="180" text-anchor="middle">four collaboration patterns, DORP each sprint</text>
<text x="380" y="196" text-anchor="middle">governance embedded, guardrails and runway</text>
<text x="380" y="212" text-anchor="middle">G: compliance is ongoing, not a gate</text>
<text x="380" y="228" text-anchor="middle">Rapid, Agile or Robust by risk and scale</text>
<rect x="515" y="92" width="230" height="150" rx="8" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="630" y="112" text-anchor="middle" font-weight="bold">Digital guides</text>
<text x="630" y="132" text-anchor="middle">DTRA before adopting: foundational,</text>
<text x="630" y="148" text-anchor="middle">impact and sustaining factors</text>
<text x="630" y="164" text-anchor="middle">ABCD adoption approach, then plug gaps</text>
<text x="630" y="180" text-anchor="middle">DPBoK contexts: founder, team, team of</text>
<text x="630" y="196" text-anchor="middle">teams, enduring enterprise, EA services per context</text>
<text x="630" y="212" text-anchor="middle">DBRM: Digital, Strategy, Structural,</text>
<text x="630" y="228" text-anchor="middle">Operational domains, ten elements</text>
<text x="380" y="275" text-anchor="middle" fill="#666">the three-point answer usually names the right guide but applies it in the wrong phase, or to the wrong context</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">A selector for the three guide families and where each applies. Original drawing; the phase mappings follow chapter 5 of the risk and security guide, chapters 3 and 4 of the sprints guide, and chapters 4 and 5 of the digital adoption guide.</figcaption>
</figure>

## Digital: readiness first, then context

The Digital Technology Adoption guide's factors come in three groups: foundational (vision,
sponsorship and direction, IT capability, culture, scope and scale, business rationale,
implementation approach), impact (business model adaptability, skills and competence,
technology maturity, ecosystem, governance and compliance) and sustaining (value realisation,
policy and regulations, funding and resources) (GUIDE:digital-technology-adoption §4). Its
four steps are: select the adoption approach with the ABCD framework, Avant-Garde, Big-Bang,
Cohesive or Discreet, by ubiquity and velocity (GUIDE:digital-technology-adoption §5.1);
perform the readiness assessment; identify factors needing attention; and address the
shortcomings, noting that if the foundational factors are not met it is futile to evaluate
the others (GUIDE:digital-technology-adoption §5.4).

The digital enterprise guide is organised around the DPBoK emergence model: Individual/
Founder, Team, Team of Teams and Enduring Enterprise, where the Enterprise Architect supports
the current context and "peeks ahead" to the next; in the first two contexts architecture is
a role, not a dedicated architect, while Team of Teams is where EA's traditional strengths,
coordination and interoperability across a portfolio, pay off
(GUIDE:using-the-togaf-standard-in-the-digital-enterprise §4.2). The DBRM structures the
digital business view into ten elements across four domains, Digital, Strategy, Structural and
Operational, so that stakeholder concerns can be addressed consistently
(GUIDE:digital-business-reference-model §3.1).

**Trap.** "Adopt the new platform now, we are a Big-Bang organisation" skips the readiness
assessment; the guide makes the assessment a prerequisite and the adoption approach a separate,
justified choice (GUIDE:digital-technology-adoption §5.1, §5.4).

## How the 5, 3 and 1 differ

| Answer | Why it scores that |
|---|---|
| 5 | Names the guide the cue points at, applies its concept in the phase or step the guide assigns (risk appetite in Preliminary, MVA per sprint, DTRA before adoption), and connects it to the ADM deliverable it lands in |
| 3 | Right guide, wrong place: risk assessed only in Phase D, governance applied at the end of the sprint series, adoption approach chosen without assessing readiness |
| 1 | Right family, wrong instrument: a controls checklist instead of security services, a waterfall EA "before any sprint starts", an org chart instead of the DBRM domains |
| 0 | Treats the guide's subject as out of scope for architecture: "security is the CISO's job", "agile teams do not need architecture", "digital is a technology purchase" |

## Where to look in the book

Integrating Risk and Security: §1.3 for services not checklists, §3.1.1 for the definition
of risk, §4 for cross-cutting, §5 for the phase-by-phase concepts. Enabling Enterprise
Agility: §4.1 levels, §4.4.4 governance, §4.7.1 delivery styles. Applying the ADM using
Agile Sprints: §3.3 patterns, §3.3.4 sprint zero, §4 phase adaptations. Digital Technology
Adoption: §4 factors, §5 the four steps. Using the TOGAF Standard in the Digital
Enterprise: §4.2 contexts, §4.4 services. Digital Business Reference Model: §3 elements.

## Check yourself

- Which phase sets risk appetite, and where may it be expressed?
- What does the sprints guide say changes about compliance reviews in Phase G?
- Why is it futile to evaluate impact factors if foundational factors are missing?
