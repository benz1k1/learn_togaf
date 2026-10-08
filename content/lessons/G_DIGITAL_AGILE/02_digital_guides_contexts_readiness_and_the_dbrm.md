---
title: The digital guides, DPBoK contexts, technology readiness and the DBRM
unit: G_DIGITAL_AGILE
objectives: ["G5.1"]
refs: ["GUIDE:using-the-togaf-standard-in-the-digital-enterprise §2.1", "GUIDE:using-the-togaf-standard-in-the-digital-enterprise §2.2", "GUIDE:using-the-togaf-standard-in-the-digital-enterprise §2.3", "GUIDE:using-the-togaf-standard-in-the-digital-enterprise §2.4", "GUIDE:using-the-togaf-standard-in-the-digital-enterprise §2.5", "GUIDE:using-the-togaf-standard-in-the-digital-enterprise §4.2", "GUIDE:using-the-togaf-standard-in-the-digital-enterprise §4.2.1", "GUIDE:using-the-togaf-standard-in-the-digital-enterprise §4.2.3", "GUIDE:using-the-togaf-standard-in-the-digital-enterprise §4.2.4", "GUIDE:using-the-togaf-standard-in-the-digital-enterprise §4.3.3", "GUIDE:using-the-togaf-standard-in-the-digital-enterprise §4.4", "GUIDE:digital-technology-adoption §2.2", "GUIDE:digital-technology-adoption §2.4", "GUIDE:digital-technology-adoption §4", "GUIDE:digital-technology-adoption §5.1", "GUIDE:digital-technology-adoption §5.3", "GUIDE:digital-technology-adoption §5.4", "GUIDE:digital-technology-adoption §6", "GUIDE:digital-business-reference-model §3.1", "GUIDE:digital-business-reference-model §3.3", "GUIDE:digital-business-reference-model §5.3", "GUIDE:digital-business-reference-model §6.2", "GUIDE:digital-business-reference-model §6.4"]
reading_minutes: 11
source: authored
status: draft
---
## Three guides, three questions

The digital guides answer three different questions and a scenario tends to ask one of them.
*Using the TOGAF Standard in the Digital Enterprise* answers "what does architecture offer a
digital organisation at its current stage of growth?"; *Digital Technology Adoption* answers
"are we ready to adopt this technology, and how should we go about it?"; the *Digital Business
Reference Model* answers "how do we structure a business view of a digital enterprise so that
stakeholders' concerns are addressed consistently?". Pick the guide by the question, then
apply its concepts in the phase it names.

## Why the standard supports the digital enterprise

The guide's argument starts from technical debt. Enterprise Architecture supports agile
delivery by reactively managing technical debt from sprints in a connected way, proactively
managing it by identifying standards and reusable components with governance as guardrails,
and by maturing digital products for operational excellence; an agile culture does not by
itself produce products with agile characteristics, because the quickest delivery is often
the hardest to connect to the rest of the ecosystem
(GUIDE:using-the-togaf-standard-in-the-digital-enterprise §2.1). Reactive management puts most
debt in the product backlog to be paid down in sprints, but cross-cutting or systemic debt
across many teams is better handled at enterprise level, where the ADM uncovers overlaps
(GUIDE:using-the-togaf-standard-in-the-digital-enterprise §2.2). Proactive management uses
standards and their lifecycle, an Architecture Board acting more like guardrails than a gate
in agile environments, the Architecture Repository and Enterprise Continuum as assets teams can
draw on, and TOGAF techniques applied to product architectures
(GUIDE:using-the-togaf-standard-in-the-digital-enterprise §2.3). Every system has an
architecture whether documented or not; the architect's job is just enough architecture, just
in time, avoiding both the complex undocumented system and the mandate for architecture before
viability is tested (GUIDE:using-the-togaf-standard-in-the-digital-enterprise §2.4). The ADM
describes the wider digital ecosystem, partitions it into segments, treats digital products as
solution architectures and is right-sized for the context
(GUIDE:using-the-togaf-standard-in-the-digital-enterprise §2.5).

## The four DPBoK contexts and the peek-ahead strategy

The DPBoK emergence model has four contexts, Individual/Founder, Team, Team of Teams and
Enduring Enterprise; the Enterprise Architect supports the current context and "peeks ahead"
to prepare the next, ensuring risk is understood and cross-team communication does not add
cognitive load (GUIDE:using-the-togaf-standard-in-the-digital-enterprise §4.2).

| Context | What EA contributes | Watch for |
|---|---|---|
| Individual/Founder | conception of digital value, communicating infrastructure choices, on-demand risk advice; architecture is a role or activity, not a dedicated architect (§4.2.1) | an answer that installs an EA function in a two-person start-up |
| Team | product architecture models, simple process and workflow depictions, operations models; shared understanding of risk, lightweight communication at the team's tempo | heavy documentation that slows the team |
| Team of Teams | coordination across teams: culture, process mechanisms, portfolio consequences; where EA's traditional strengths increase in value; interoperability across a portfolio of products (§4.2.3) | over-complex coordination that degrades team cohesion |
| Enduring Enterprise | governance, risk, security and compliance; information management; architecture and portfolio management; mergers and third parties; a digital governance framework (§4.2.4) | treating EA itself as outside the portfolio it should be managed in |

Principles are mapped per context, for example Common Use Applications, Data is an Asset,
Technology Independence, Control Technical Diversity and Interoperability arrive at Team of
Teams because that is where duplication, portability and integration risk grow
(GUIDE:using-the-togaf-standard-in-the-digital-enterprise §4.3.3). The guide also packages EA
capabilities as *services* delivered at the tempo of the context: business value assessment,
stakeholder management, sustainability, architecture and standards guidance and risk
management from the Founder context; change management added at Team; project planning,
tailoring, vision and strategy, modelling of MVAs, integration, release support, portfolio
support and enterprise assessment at Team of Teams; compliance criteria development,
compliance assessment, capability planning and EA process improvement at Enduring Enterprise
(GUIDE:using-the-togaf-standard-in-the-digital-enterprise §4.4).

<figure class="my-4">
<svg viewBox="0 0 760 300" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="11" role="img" aria-label="The four DPBoK contexts as an emergence staircase with the EA services added at each step, beside the four-step digital technology adoption roadmap and the DBRM's four domains">
<defs><marker id="arr-g5d" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
<g fill="#e0ecff" stroke="#7aa2e3">
<rect x="15" y="200" width="110" height="60" rx="6"/>
<rect x="115" y="150" width="110" height="110" rx="6"/>
<rect x="215" y="100" width="110" height="160" rx="6"/>
<rect x="315" y="50" width="110" height="210" rx="6"/>
</g>
<text x="70" y="222" text-anchor="middle" font-weight="bold">I Founder</text>
<text x="70" y="240" text-anchor="middle" font-size="10">value, risk advice,</text>
<text x="70" y="252" text-anchor="middle" font-size="10">standards guidance</text>
<text x="170" y="172" text-anchor="middle" font-weight="bold">II Team</text>
<text x="170" y="190" text-anchor="middle" font-size="10">+ change management,</text>
<text x="170" y="202" text-anchor="middle" font-size="10">product and ops models</text>
<text x="270" y="122" text-anchor="middle" font-weight="bold">III Team of Teams</text>
<text x="270" y="140" text-anchor="middle" font-size="10">+ planning, tailoring,</text>
<text x="270" y="152" text-anchor="middle" font-size="10">MVA modelling, integration,</text>
<text x="270" y="164" text-anchor="middle" font-size="10">portfolio support</text>
<text x="370" y="72" text-anchor="middle" font-weight="bold">IV Enduring</text>
<text x="370" y="90" text-anchor="middle" font-size="10">+ compliance criteria,</text>
<text x="370" y="102" text-anchor="middle" font-size="10">compliance assessment,</text>
<text x="370" y="114" text-anchor="middle" font-size="10">capability planning</text>
<text x="220" y="30" text-anchor="middle" font-weight="bold">DPBoK contexts: support now, peek ahead (§4.2)</text>
<text x="220" y="282" text-anchor="middle" fill="#666" font-size="10">services delivered at the tempo of the context (§4.4)</text>
<rect x="460" y="20" width="285" height="118" rx="8" fill="#e3f5e1" stroke="#7fbf7a"/>
<text x="602" y="40" text-anchor="middle" font-weight="bold">Digital Technology Adoption, four steps (§5)</text>
<text x="602" y="60" text-anchor="middle">1 select the approach: Avant-Garde, Big-Bang, Cohesive, Discreet</text>
<text x="602" y="78" text-anchor="middle">2 perform the readiness assessment (DTRA)</text>
<text x="602" y="96" text-anchor="middle">3 identify factors needing attention, their consequences</text>
<text x="602" y="114" text-anchor="middle">4 address shortcomings, foundational first, then adopt</text>
<text x="602" y="130" text-anchor="middle" font-size="10">DTRA initiates Phase A of the cycle (§6)</text>
<rect x="460" y="160" width="285" height="100" rx="8" fill="#fff1d6" stroke="#e0b060"/>
<text x="602" y="180" text-anchor="middle" font-weight="bold">DBRM: ten elements in four domains (§3.1)</text>
<text x="602" y="200" text-anchor="middle">Digital: customer focus, digital enterprise</text>
<text x="602" y="216" text-anchor="middle">Strategy: context, motivation, services and products</text>
<text x="602" y="232" text-anchor="middle">Structural: ecosystem and business model, operating model, capability model</text>
<text x="602" y="248" text-anchor="middle">Operational: business operating environment, digital enablement</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">The three digital guides side by side: contexts, adoption steps and reference model domains. Original drawing; section numbers refer to the respective guides.</figcaption>
</figure>

## Digital technology readiness

A readiness assessment measures how prepared an enterprise is for a large transformation; it
gives decision-makers assurance that the endeavour can succeed and saves the reputation cost
of a high-profile failure, assessing goals, expectations, leadership support, ability to adapt,
governance, internal capability and programme needs (GUIDE:digital-technology-adoption §2.2).
The drivers behind adoption include evolving business models, modernised channels and customer
reach, cloud computing power, the Internet as platform, open source, technopreneurs and digital
disruptors (GUIDE:digital-technology-adoption §2.4). The factors split into foundational
(vision, sponsorship and direction, IT capability, culture, scope and scale, business rationale,
implementation approach), impact (business model adaptability, skills and competence,
technology maturity, ecosystem, governance and compliance) and sustaining (value realisation,
policy and regulations, funding and resources), with a dependency diagram showing how they
reinforce each other (GUIDE:digital-technology-adoption §4).

The roadmap has four steps. Select the adoption approach with the ABCD framework, ubiquity
against velocity: Avant-Garde lets one part adopt first, Big-Bang rolls out enterprise-wide at
once, Cohesive takes everyone along by consensus, Discreet starts slow and builds competence;
no quadrant is better than another (GUIDE:digital-technology-adoption §5.1). Perform the
assessment with the questionnaire, involving key leaders in dialogue. Identify the factors
needing attention and read the consequence of each missing factor, a missing implementation
approach for instance meaning missed opportunities through trial and error
(GUIDE:digital-technology-adoption §5.3). Address shortcomings progressively: enterprises that
meet only the foundational factors are Type 1, foundational and impact Type 2, all three Type 3;
if the foundational factors are unmet it is futile to evaluate the rest
(GUIDE:digital-technology-adoption §5.4). The assessment should initiate Phase A and the
factors are then analysed per phase, Preliminary for capability and principles, A for the
vision and stakeholders, E for a holistic readiness view, F for the strategy, G for conformance
and H for maintaining the change cycle (GUIDE:digital-technology-adoption §6).

## The Digital Business Reference Model

The DBRM has ten core elements in four domains: Digital (Customer Focus, Digital Enterprise),
Strategy (Strategic Context, Business Motivation, Business Services and Products), Structural
(Ecosystem and Business Model, Operating Model, Business Capability Model) and Operational
(Business Operating Environment, Digital Enablement), so that specific stakeholder concerns
can be addressed consistently (GUIDE:digital-business-reference-model §3.1). The Strategy
domain is the "why" of the business, the Structural domain the "what", the Operational domain
the "how" (GUIDE:digital-business-reference-model §3.3). Digital architecture development
adds the O-AA building blocks, value creation, agile strategy, experience design, product
architecture, operations architecture, data and analytics and technology architecture,
developed concurrently (GUIDE:digital-business-reference-model §5.3). The guide maps the
elements to ADM phases and content framework categories, the Preliminary Phase and Phase A to
Strategic Context and the Ecosystem and Business Model, Phase B to Business Motivation, Services
and Products, Operating Model and Capability Model, Phases C and D to the Business Operating
Environment, Phase E to Digital Enablement (GUIDE:digital-business-reference-model §6.2), and to
the landscape levels, Strategic to the Digital and Strategy elements, Segment to services,
operating model and capability model, Capability to the Operational domain
(GUIDE:digital-business-reference-model §6.4).

**Trap.** The DBRM's four domains are Digital, Strategy, Structural and Operational, not the
four TOGAF architecture domains; the guide maps between them but they are different lists
(GUIDE:digital-business-reference-model §3.1).

## How the 5, 3 and 1 differ

| Answer | Why it scores that |
|---|---|
| 5 | Identifies the DPBoK context and offers the EA services that fit it at its tempo, runs the readiness assessment before choosing an adoption approach and plugs foundational gaps first, and structures the business view with the DBRM domains |
| 3 | Right guide, wrong stage: Enduring Enterprise governance imposed on a Team, or the ABCD approach chosen before the assessment |
| 1 | Applies the standard as a document-heavy mandate to a founder-stage product; the guide warns that too much architecture before viability is as wrong as none (§2.4) |
| 0 | Treats digital transformation as a technology purchase with no readiness assessment and no architecture; seventy percent of such programmes fail for exactly the reasons the factors capture (§2.3) |

## Where to look in the book

Using the TOGAF Standard in the Digital Enterprise: §2 for the technical debt argument, §4.2
for the contexts, §4.3 for principles per context, §4.4 for services per context, §4.5 for
artefacts and guides per context. Digital Technology Adoption: §2.2 the assessment, §4 the
factors, §5 the four steps, §6 the ADM mapping. Digital Business Reference Model: §3 the
elements and domains, §5 the O-AA building blocks, §6 the ADM and landscape mapping.

## Check yourself

- In which context do EA's traditional coordination strengths increase most in value?
- Name the four ABCD approaches and the two axes.
- Which DBRM domain answers "how", and which elements sit in it?
