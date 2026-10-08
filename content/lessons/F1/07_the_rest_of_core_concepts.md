---
title: "The rest of Core Concepts: services, principles, interoperability, views, the content framework, styles, agility and risk"
unit: F1
objectives: ["1.1", "1.3", "1.4", "1.5"]
refs: ["INTRO §3.5", "INTRO §3.8", "INTRO §3.9", "INTRO §3.11", "INTRO §3.14", "INTRO §3.15", "INTRO §3.16", "INTRO §3.17", "INTRO §3.18"]
reading_minutes: 9
source: authored
status: draft
---
Chapter 3 of the Introduction is the "core concepts" chapter, and the exam samples all of it.
This lesson covers the sections the other F1 lessons do not, each at the depth a Foundation
question needs.

## Enterprise Architecture services

The ADM's activities are often delivered through a service model, organised in six categories.
The first four are customer-centric and the last two are internal, aimed at architects
(INTRO §3.5).

| Category | Typical customer | Typical deliverables |
|---|---|---|
| Enterprise Support Services | C-level management | answers to questions, assessment reports, recommendations |
| Design Support Services | programme-level decision-makers | Minimum Viable Architectures (MVAs) for programmes, compliance guidance and reports |
| Development Support Services | project-level decision-makers | MVAs for projects and products, compliance guidance and reports |
| Requirements Elicitation and Understanding Services | product managers | stakeholder concerns, requirements, value and ability assessments |
| Architecture Planning Services | architecture team leaders | architecture project plans |
| EA Practice Development Support Services | architecture organisation decision-makers | EA Capability assessments and improvement recommendations |

Enterprise Support can be provided independently of any project; Design Support typically comes
after a project is funded and includes developing MVAs; Development Support runs during a
project's development; Requirements Elicitation goes a step beyond requirements management to get
closer to real need; Architecture Planning happens at the start of a project; Practice Development
improves the EA Capability itself (INTRO §3.5).

<figure class="my-4">
<svg viewBox="0 0 760 232" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="Six enterprise architecture service categories: four customer-centric and two internal">
  <defs><marker id="arr-f1-14a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
  <rect x="10" y="10" width="505" height="190" rx="8" fill="#e0ecff" stroke="#7aa2e3"/>
  <text x="262.5" y="28" text-anchor="middle" font-size="12" font-weight="bold">Customer-centric services (four)</text>
  <rect x="25" y="40" width="235" height="66" rx="6" fill="#fff" stroke="#666"/>
  <text x="142.5" y="57.35" text-anchor="middle" font-size="11" font-weight="bold">Enterprise Support</text>
  <text x="142.5" y="70.35" text-anchor="middle" font-size="11" fill="#345">for C-level management</text>
  <text x="142.5" y="83.35" text-anchor="middle" font-size="11" fill="#345">answers, assessments,</text>
  <text x="142.5" y="96.35" text-anchor="middle" font-size="11" fill="#345">recommendations</text>
  <rect x="270" y="40" width="235" height="66" rx="6" fill="#fff" stroke="#666"/>
  <text x="387.5" y="57.35" text-anchor="middle" font-size="11" font-weight="bold">Design Support</text>
  <text x="387.5" y="70.35" text-anchor="middle" font-size="11" fill="#345">for programme decision-makers</text>
  <text x="387.5" y="83.35" text-anchor="middle" font-size="11" fill="#345">MVAs for programmes,</text>
  <text x="387.5" y="96.35" text-anchor="middle" font-size="11" fill="#345">compliance guidance</text>
  <rect x="25" y="115" width="235" height="66" rx="6" fill="#fff" stroke="#666"/>
  <text x="142.5" y="132.35" text-anchor="middle" font-size="11" font-weight="bold">Development Support</text>
  <text x="142.5" y="145.35" text-anchor="middle" font-size="11" fill="#345">for project decision-makers</text>
  <text x="142.5" y="158.35" text-anchor="middle" font-size="11" fill="#345">MVAs for projects and products,</text>
  <text x="142.5" y="171.35" text-anchor="middle" font-size="11" fill="#345">compliance guidance</text>
  <rect x="270" y="115" width="235" height="66" rx="6" fill="#fff" stroke="#666"/>
  <text x="387.5" y="132.35" text-anchor="middle" font-size="11" font-weight="bold">Requirements Elicitation</text>
  <text x="387.5" y="145.35" text-anchor="middle" font-size="11" fill="#345">and Understanding, for product managers</text>
  <text x="387.5" y="158.35" text-anchor="middle" font-size="11" fill="#345">concerns, requirements,</text>
  <text x="387.5" y="171.35" text-anchor="middle" font-size="11" fill="#345">value and ability assessments</text>
  <rect x="535" y="10" width="215" height="190" rx="8" fill="#fff1d6" stroke="#e0b060"/>
  <text x="642.5" y="28" text-anchor="middle" font-size="12" font-weight="bold">Internal services (two)</text>
  <rect x="548" y="40" width="190" height="66" rx="6" fill="#fff" stroke="#666"/>
  <text x="643" y="63.85" text-anchor="middle" font-size="11" font-weight="bold">Architecture Planning</text>
  <text x="643" y="76.85" text-anchor="middle" font-size="11" fill="#345">for architecture team leaders</text>
  <text x="643" y="89.85" text-anchor="middle" font-size="11" fill="#345">architecture project plans</text>
  <rect x="548" y="115" width="190" height="66" rx="6" fill="#fff" stroke="#666"/>
  <text x="643" y="132.35" text-anchor="middle" font-size="11" font-weight="bold">EA Practice Development</text>
  <text x="643" y="145.35" text-anchor="middle" font-size="11" fill="#345">Support, for EA decision-makers</text>
  <text x="643" y="158.35" text-anchor="middle" font-size="11" fill="#345">capability assessments and</text>
  <text x="643" y="171.35" text-anchor="middle" font-size="11" fill="#345">improvement recommendations</text>
  <text x="380" y="222" text-anchor="middle" font-size="11" fill="#666">the first four face customers of the architecture; the last two are aimed at the architects themselves</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">The six service categories grouped as the standard groups them. Original drawing; the names follow INTRO §3.5.</figcaption>
</figure>

## Principles

Principles are general rules and guidelines, meant to endure and be seldom amended, that inform
how an organisation pursues its mission. Two domains of principle matter to architecture
(INTRO §3.8):

- **Enterprise Principles** underpin decision-making across the whole enterprise, govern the use
  of all resources and assets, reflect consensus, and are a key element of Architecture Governance.
  Subsidiary principles (for IT, HR, a region) may exist beneath them.
- **Architecture Principles** relate specifically to architecture work: they embody the spirit of
  the Enterprise Principles and govern the architecture process, affecting development,
  maintenance and use of the EA.

The hierarchy starts with Enterprise Principles; each lower level is informed by and elaborates the
level above and cannot overstep it. The architecture should be traceable to principles in how it
realises objectives that respond to drivers (INTRO §3.8). Detail on writing principles is in the
ADM Techniques document.

## Interoperability

Interoperability is the ability to share information and services, and the *degree* of sharing
required is a useful architecture requirement, especially in an extended enterprise (INTRO §3.9).
It is determined progressively through the ADM: revealed in business scenarios in Phase A, defined
in business terms in Phase B, detailed as information content in the Data Architecture and as
application sharing in the Application Architecture (both Phase C), given technical mechanisms in
Phase D, resolved into actual solutions such as COTS in Phase E, and logically implemented in
Phase F (INTRO §3.9).

<figure class="my-4">
<svg viewBox="0 0 760 170" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="Interoperability determined progressively from Phase A to Phase F, with the business and IT classifications">
  <defs><marker id="arr-f1-14b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
  <rect x="10" y="15" width="112" height="56" rx="6" fill="#fff" stroke="#666"/>
  <text x="66" y="33.5" text-anchor="middle" font-size="10" font-weight="bold">Phase A</text>
  <text x="66" y="46.5" text-anchor="middle" font-size="10" fill="#345">revealed in</text>
  <text x="66" y="59.5" text-anchor="middle" font-size="10" fill="#345">business scenarios</text>
  <line x1="122" y1="43" x2="132" y2="43" stroke="#555" marker-end="url(#arr-f1-14b)"/>
  <rect x="132" y="15" width="112" height="56" rx="6" fill="#fff" stroke="#666"/>
  <text x="188" y="33.5" text-anchor="middle" font-size="10" font-weight="bold">Phase B</text>
  <text x="188" y="46.5" text-anchor="middle" font-size="10" fill="#345">defined in</text>
  <text x="188" y="59.5" text-anchor="middle" font-size="10" fill="#345">business terms</text>
  <line x1="244" y1="43" x2="254" y2="43" stroke="#555" marker-end="url(#arr-f1-14b)"/>
  <rect x="254" y="15" width="112" height="56" rx="6" fill="#fff" stroke="#666"/>
  <text x="310" y="33.5" text-anchor="middle" font-size="10" font-weight="bold">Phase C</text>
  <text x="310" y="46.5" text-anchor="middle" font-size="10" fill="#345">information content,</text>
  <text x="310" y="59.5" text-anchor="middle" font-size="10" fill="#345">application sharing</text>
  <line x1="366" y1="43" x2="376" y2="43" stroke="#555" marker-end="url(#arr-f1-14b)"/>
  <rect x="376" y="15" width="112" height="56" rx="6" fill="#fff" stroke="#666"/>
  <text x="432" y="33.5" text-anchor="middle" font-size="10" font-weight="bold">Phase D</text>
  <text x="432" y="46.5" text-anchor="middle" font-size="10" fill="#345">technical</text>
  <text x="432" y="59.5" text-anchor="middle" font-size="10" fill="#345">mechanisms</text>
  <line x1="488" y1="43" x2="498" y2="43" stroke="#555" marker-end="url(#arr-f1-14b)"/>
  <rect x="498" y="15" width="112" height="56" rx="6" fill="#fff" stroke="#666"/>
  <text x="554" y="33.5" text-anchor="middle" font-size="10" font-weight="bold">Phase E</text>
  <text x="554" y="46.5" text-anchor="middle" font-size="10" fill="#345">actual solutions,</text>
  <text x="554" y="59.5" text-anchor="middle" font-size="10" fill="#345">e.g. COTS</text>
  <line x1="610" y1="43" x2="620" y2="43" stroke="#555" marker-end="url(#arr-f1-14b)"/>
  <rect x="620" y="15" width="112" height="56" rx="6" fill="#fff" stroke="#666"/>
  <text x="676" y="33.5" text-anchor="middle" font-size="10" font-weight="bold">Phase F</text>
  <text x="676" y="46.5" text-anchor="middle" font-size="10" fill="#345">logically</text>
  <text x="676" y="59.5" text-anchor="middle" font-size="10" fill="#345">implemented</text>
  <rect x="10" y="95" width="355" height="40" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
  <text x="187.5" y="111.85" text-anchor="middle" font-size="11" font-weight="bold">business classification</text>
  <text x="187.5" y="125.85" text-anchor="middle" font-size="11" fill="#345">operational (business), information, technical</text>
  <rect x="385" y="95" width="355" height="40" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/>
  <text x="562.5" y="111.85" text-anchor="middle" font-size="11" font-weight="bold">IT classification (modelled on EAI)</text>
  <text x="562.5" y="125.85" text-anchor="middle" font-size="11" fill="#345">presentation, information, application, technical</text>
  <text x="375" y="158" text-anchor="middle" font-size="11" fill="#666">the degree of sharing required is itself an architecture requirement, determined progressively through the cycle</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">Where interoperability is decided, phase by phase. Original drawing; the sequence follows INTRO §3.9.</figcaption>
</figure>

Two classifications are offered. The business one: operational (or business), information and
technical interoperability. The IT one, modelled on Enterprise Application Integration:
presentation, information, application and technical integration (INTRO §3.9).

## Views and viewpoints

Being able to create views of parts of a complex architecture is fundamental to communicating with
stakeholders and allaying their concerns; information has to be presented in a form each
stakeholder relates to. The concepts are adapted from ISO/IEC/IEEE 42010:2022 and 15288:2015
(INTRO §3.16). The definitions and the view/viewpoint distinction are drilled in unit F2.

## The Content Framework and the Enterprise Metamodel

When the EA Capability is set up in the Preliminary Phase, three things must be defined: a
**Content Framework**, the categorisation scheme for architecture descriptions and the models that
express them; an **Enterprise Metamodel**, a formal model of the entity types in the enterprise and
their relationships; and the specific artifacts to be developed (INTRO §3.11). The choice of
content framework is shaped by the architecture framework adopted and by the tooling; many
alternatives exist (the TOGAF Content Framework, Zachman, DoDAF, NAF), selecting one is essential
even though *which* one matters less, and the result is usually adapted (INTRO §3.11).

The TOGAF Content Framework aims to give a detailed model of work products, drive consistency in
ADM outputs, provide a checklist of possible outputs, reduce the risk of gaps, and help an
enterprise mandate standard concepts, terms and deliverables (INTRO §3.11). At the top level it is
organised by ADM phase: principles, vision, motivation and requirements models; Business
Architecture; Information Systems Architecture; Technology Architecture; Architecture
Realization/Transformation (roadmaps and binding statements); and Architecture Change Management
models (INTRO §3.11).

The Enterprise Metamodel defines the entity types that appear in models (for instance a type
*Role*, with instances such as Teller or Pilot) and their relationships. It gives architects a
starter set of things to investigate, provides a completeness check for any proposed modelling
language, and supports consistency, completeness and traceability. The standard does not constrain
the choice of artifacts or notation; ArchiMate, BPMN, UML, entity-relationship diagrams and
flowcharts are all acceptable (INTRO §3.11). The TOGAF Library supplies a Foundation-level Core
Enterprise Metamodel as a starting point (INTRO §3.11).

## Using the standard with other frameworks and styles

Any EA framework has two key elements: the deliverables it expects and the method for producing
them; most frameworks concentrate on the deliverables and say little about method. Because the
TOGAF Standard is generic, its content framework and generic deliverables can be used as they are,
or replaced or extended with a more specific set from another framework. Architects are expected
to tailor, which may mean adopting elements of other frameworks or integrating with ITIL, CMMI,
COBIT, PRINCE2, PMBOK, MSP, or reference material such as IT4IT (INTRO §3.14).

Architectural styles differ in focus, form, techniques, materials, subject and time period. To
support a style, first identify its distinctive features, then decide how to address them; that
should not require major changes to the framework, only adjustments to the models, viewpoints and
tools used, and typically extensions to the content metamodel plus specific notation and
viewpoints. A dominant style may send the practitioner back to the Preliminary Phase to adjust
the Architecture Capability (INTRO §3.15). SOA and integrated risk and security are the named
examples of styles with their own Series Guides (INTRO §3.15).

## Enterprise agility

Enterprise agility is broader than Agile software development; it matters because it lets an enterprise respond to change: closer to customers and
products, leaner, and more reliably compliant. The framework
responds through **partitions** (how work is broken into separate architecture initiatives) and
**levels** (developing the architecture at different granularities), plus the ADM's iteration
concepts. Detailed guidance is in the Agile Sprints and Enabling Enterprise Agility guides and the
Open Agile Architecture Standard (INTRO §3.17).

## Risk management

Every transformation carries risk; risks should be identified, classified and mitigated before
starting and tracked throughout, with monitoring of the context because triggers such as a merger
may lie outside the planners' control. The architect may identify and mitigate risks, but risks
are *accepted and managed* within the governance framework. Two levels are distinguished:
**initial** risk, before mitigation, and **residual** risk, after it. The process is
classification, identification, initial assessment, mitigation and residual assessment, and
monitoring (INTRO §3.18). The qualitative approach lives in ADM Techniques; a quantitative one is
the Open FAIR body of knowledge (INTRO §3.18).

<!-- figures:start -->
## Figures from the standard

The diagrams the cited sections carry, from your local copy of the publication. The exam reproduces these; know what each box is.

<div class="grid gap-4 md:grid-cols-2">
<figure class="max-w-lg"><img src="/figure/INTRO:fig-3-10" alt="Figure 3-10: Basic Architectural Concepts" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 3-10: Basic Architectural Concepts (INTRO)</figcaption></figure>
<figure class="max-w-lg"><img src="/figure/INTRO:fig-3-6" alt="Figure 3-6: Content Framework by ADM Phase" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 3-6: Content Framework by ADM Phase (INTRO)</figcaption></figure>
<figure class="max-w-lg"><img src="/figure/INTRO:fig-3-7" alt="Figure 3-7: Applying the Enterprise Continuum" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 3-7: Applying the Enterprise Continuum (INTRO)</figcaption></figure>
<figure class="max-w-lg"><img src="/figure/INTRO:fig-3-8" alt="Figure 3-8: The TOGAF Core Enterprise Metamodel" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 3-8: The TOGAF Core Enterprise Metamodel (INTRO)</figcaption></figure>
</div>
<!-- figures:end -->

## Check yourself

- Which service category delivers MVAs for programmes?
- Which principles sit at the top of the hierarchy?
- In which phase are interoperability considerations first revealed, and through what technique?
- What is residual risk?
