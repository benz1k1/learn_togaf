---
title: Phase C, Information Systems Architectures (Data and Application), in depth
unit: F4
objectives: ["4.3", "4.4"]
refs: ["ADM §5", "ADM §5.1", "ADM §5.2", "ADM §6", "ADM §6.1", "ADM §6.2", "ADM §6.2.1", "ADM §6.2.2", "ADM §6.2.3", "ADM §6.3", "ADM §6.3.1", "ADM §6.3.7", "ADM §6.3.9", "ADM §6.4", "ADM §6.5", "ADM §6.5.1", "ADM §6.5.2", "ADM §6.5.3", "ADM §7", "ADM §7.1", "ADM §7.2", "ADM §7.2.1", "ADM §7.2.2", "ADM §7.2.3", "ADM §7.3", "ADM §7.3.1", "ADM §7.3.7", "ADM §7.4", "ADM §7.5", "ADM §7.5.1"]
reading_minutes: 12
source: authored
status: draft
---
## One phase, two chapters

Phase C covers the Data and Application Architectures for the project (ADM §5). The standard
gives the objectives and approach once (chapter 5), then describes inputs, steps and outputs
separately for the Data part (chapter 6) and the Application part (chapter 7).

Objectives (ADM §5.1):

| Objective | Pattern |
|---|---|
| Develop the **Target Information Systems Architectures**, describing how they will enable the Business Architecture and the Architecture Vision, addressing the Statement of Architecture Work and stakeholder concerns | develop the target |
| Identify candidate Architecture Roadmap components from the gaps between Baseline and Target Information Systems (Data and Application) Architectures | gaps → roadmap components |

The Data part restates them for the Target Data Architecture (ADM §6.1) and the Application part
for the Target Application Architecture (ADM §7.1).

## Approach

Phase C is "some combination of Data and Application Architecture, **in either order**"
(ADM §5.2). A data-driven approach (Spewak's Enterprise Architecture Planning) starts with data;
an application-driven approach starts from core packaged applications (ERP, CRM) that underpin
mission-critical processes and treats their implementation and integration as the main focus.

The Data approach (ADM §6.5): a Data Architecture should handle **data at rest, data in motion,
data in use and open data** (ADM §6.5.1), and is built from three metamodel entities — data
entity, logical data component and physical data component. Key considerations are **data
management** (systems of record, enterprise-wide standards, where data is created, stored,
transported and reported), **data migration** (transformation, weeding and cleansing when an
application is replaced) and **data governance** (structure, management system, people)
(ADM §6.5.2). The repository supplies generic data models for the industry vertical (ADM §6.5.3).

The Application approach is shorter: consider what application resources the repository holds —
industry business and application models, models for common functions such as e-commerce and
supply chain, and the Integrated Information Infrastructure Reference Model (III-RM)
(ADM §7.5.1).

## Inputs

Both parts share the standard set; the differences are the domain-specific principles, the
reference guides and what has already been produced.

| Group | Data part (ADM §6.2) | Application part (ADM §7.2) |
|---|---|---|
| External | architecture reference materials **plus** the Information Architecture Series Guides (customer master data management; BI and analytics and metadata management reference models) (ADM §6.2.1) | architecture reference materials (ADM §7.2.1) |
| Non-architectural | Request for Architecture Work; Capability Assessment; Communications Plan (ADM §6.2.2) | the same three (ADM §7.2.2) |
| Architectural | Organizational Model; Tailored Framework; **data principles**, if existing; Statement of Architecture Work; Architecture Vision; Architecture Repository (in particular definitions of current data); draft Architecture Definition Document; draft Architecture Requirements Specification with gap results **from Business Architecture**; **Business Architecture** components of the roadmap (ADM §6.2.3) | the same, with **application principles**; gap results from Business **and Data** Architecture, if available; Business **and Data** roadmap components, if available (ADM §7.2.3) |

## Steps

Each part runs the nine development steps (ADM §6.3, ADM §7.3): select reference models,
viewpoints and tools; develop the Baseline description; develop the Target description; perform
gap analysis; define candidate roadmap components; resolve impacts across the Architecture
Landscape; conduct formal stakeholder review; finalize the Data (or Application) Architecture;
create/update the Architecture Definition Document.

Domain-specific detail inside step 1:

- Data (ADM §6.3.1): review or generate the data principles; example modeling techniques are the
  entity relationship diagram and the class diagram; the recommended process collects data models
  from Business and Application material, rationalizes them into a data inventory, builds
  matrices relating data to business service, capability, function, access rights and
  application, then examines how data is created, distributed, migrated, secured and archived.
- Application (ADM §7.3.1): review or generate the application principles; consider
  platform-independent descriptions of business logic (the OMG Model-Driven Architecture is the
  example); the recommended process lists required applications, decomposes complicated ones,
  removes duplicated functionality, identifies logical and physical applications, builds
  matrices to business services, capabilities, data and processes, and elaborates views.

Step 7 in both parts includes an impact analysis on the *other* architectures: the Data review
asks whether Business and Application Architectures must change and identifies constraints on
the Technology Architecture about to be designed (ADM §6.3.7); the Application review does the
same for Business and Data and flags constraints on the Technology Architecture, especially
infrastructure (ADM §7.3.7). Either may "drop into a short iteration" of the other part.

## Outputs

| Output | Data part (ADM §6.4) | Application part (ADM §7.4) |
|---|---|---|
| Refined Architecture Vision phase deliverables | Statement of Architecture Work; validated or new **data principles** | Statement of Architecture Work; validated or new **application principles** |
| Draft Architecture Definition Document | Baseline and Target Data Architecture: business data model, logical data model, data management process models, **Data Entity/Business Function matrix**, views | Baseline and Target Application Architecture, views |
| Draft Architecture Requirements Specification | gap results, **data interoperability requirements**, technical requirements, **constraints on the Technology Architecture** about to be designed, updated business and application requirements | gap results, **application interoperability requirements**, technical requirements, constraints on the Technology Architecture, updated business and data requirements |
| Roadmap components | Data Architecture components of an Architecture Roadmap | Application Architecture components of an Architecture Roadmap |

The Data sections of the Architecture Definition Document are spelled out in step 9: business
data model, logical data model, data management process model, Data Entity/Business Function
matrix and data interoperability requirements (ADM §6.3.9).

<figure class="my-4">
<svg viewBox="0 0 760 350" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="Phase C as one phase with a Data lane and an Application lane, each running the nine steps in either order, between shared inputs and outputs">
  <defs><marker id="arr-f4-13" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
  <text x="105" y="18" text-anchor="middle" font-size="12" font-weight="bold" fill="#345">Inputs</text><text x="659" y="18" text-anchor="middle" font-size="12" font-weight="bold" fill="#345">Outputs</text><text x="380" y="18" text-anchor="middle" font-size="12" font-weight="bold" fill="#345">One phase, two lanes</text><rect x="232" y="34" width="296" height="282" rx="8" fill="#fff1d6" stroke="#e0b060"/><text x="380" y="52" text-anchor="middle" font-size="12" font-weight="bold">Phase C: Information Systems Architectures</text><rect x="240" y="64" width="280" height="108" rx="6" fill="#e0ecff" stroke="#7aa2e3"/><text x="248" y="80" font-size="11.5" font-weight="bold">Data Architecture</text><text x="512" y="80" font-size="10.5" text-anchor="end" fill="#345">ADM chapter 6</text><text x="248" y="98" font-size="10.5">1 select models, viewpoints, tools (review or</text><text x="248" y="111" font-size="10.5">   generate the domain principles)</text><text x="248" y="124" font-size="10.5">2 baseline · 3 target · 4 gap analysis</text><text x="248" y="137" font-size="10.5">5 roadmap candidates · 6 resolve impacts</text><text x="248" y="150" font-size="10.5">7 review — flag constraints on Technology</text><text x="248" y="163" font-size="10.5">8 finalize · 9 create/update the ADD</text><rect x="240" y="200" width="280" height="108" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/><text x="248" y="216" font-size="11.5" font-weight="bold">Application Architecture</text><text x="512" y="216" font-size="10.5" text-anchor="end" fill="#345">ADM chapter 7</text><text x="248" y="234" font-size="10.5">1 select models, viewpoints, tools (review or</text><text x="248" y="247" font-size="10.5">   generate the domain principles)</text><text x="248" y="260" font-size="10.5">2 baseline · 3 target · 4 gap analysis</text><text x="248" y="273" font-size="10.5">5 roadmap candidates · 6 resolve impacts</text><text x="248" y="286" font-size="10.5">7 review — flag constraints on Technology</text><text x="248" y="299" font-size="10.5">8 finalize · 9 create/update the ADD</text><line x1="310" y1="175" x2="310" y2="197" stroke="#555" marker-end="url(#arr-f4-13)"/><line x1="450" y1="197" x2="450" y2="175" stroke="#555" marker-end="url(#arr-f4-13)"/><text x="380" y="190" text-anchor="middle" font-size="10.5" fill="#345" font-style="italic">in either order (ADM §5.2)</text><rect x="10" y="65" width="190" height="46" rx="6" fill="#e0ecff" stroke="#7aa2e3"/><text x="105" y="85.5" text-anchor="middle" font-size="10.5">Statement of Architecture Work;</text><text x="105" y="98.5" text-anchor="middle" font-size="10.5">Architecture Vision</text><line x1="200" y1="88" x2="230" y2="88" stroke="#555" marker-end="url(#arr-f4-13)"/><rect x="10" y="123" width="190" height="46" rx="6" fill="#e0ecff" stroke="#7aa2e3"/><text x="105" y="137" text-anchor="middle" font-size="10.5">Draft Architecture Definition Doc.;</text><text x="105" y="150" text-anchor="middle" font-size="10.5">draft Requirements Specification</text><text x="105" y="163" text-anchor="middle" font-size="10.5">with gap results from Phase B</text><line x1="200" y1="146" x2="230" y2="146" stroke="#555" marker-end="url(#arr-f4-13)"/><rect x="10" y="181" width="190" height="46" rx="6" fill="#e0ecff" stroke="#7aa2e3"/><text x="105" y="201.5" text-anchor="middle" font-size="10.5">Business Architecture components</text><text x="105" y="214.5" text-anchor="middle" font-size="10.5">of the Architecture Roadmap</text><line x1="200" y1="204" x2="230" y2="204" stroke="#555" marker-end="url(#arr-f4-13)"/><rect x="10" y="239" width="190" height="46" rx="6" fill="#e0ecff" stroke="#7aa2e3"/><text x="105" y="259.5" text-anchor="middle" font-size="10.5">Data principles / application</text><text x="105" y="272.5" text-anchor="middle" font-size="10.5">principles, if existing</text><line x1="200" y1="262" x2="230" y2="262" stroke="#555" marker-end="url(#arr-f4-13)"/><rect x="564" y="65" width="190" height="46" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/><text x="659" y="85.5" text-anchor="middle" font-size="10.5">Validated or new data principles</text><text x="659" y="98.5" text-anchor="middle" font-size="10.5">and application principles</text><line x1="528" y1="88" x2="562" y2="88" stroke="#555" marker-end="url(#arr-f4-13)"/><rect x="564" y="123" width="190" height="46" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/><text x="659" y="143.5" text-anchor="middle" font-size="10.5">Draft Architecture Definition Doc.:</text><text x="659" y="156.5" text-anchor="middle" font-size="10.5">Data, then Application (or reverse)</text><line x1="528" y1="146" x2="562" y2="146" stroke="#555" marker-end="url(#arr-f4-13)"/><rect x="564" y="181" width="190" height="46" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/><text x="659" y="195" text-anchor="middle" font-size="10.5">Draft Requirements Specification:</text><text x="659" y="208" text-anchor="middle" font-size="10.5">interoperability requirements and</text><text x="659" y="221" text-anchor="middle" font-size="10.5">constraints on the Technology Arch.</text><rect x="715" y="173" width="35" height="15" rx="7" fill="#f3e3f7" stroke="#b58ac9"/><text x="732.5" y="184" text-anchor="middle" font-size="9.5" fill="#5b2d6e">first</text><line x1="528" y1="204" x2="562" y2="204" stroke="#555" marker-end="url(#arr-f4-13)"/><rect x="564" y="239" width="190" height="46" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/><text x="659" y="259.5" text-anchor="middle" font-size="10.5">Data and Application components</text><text x="659" y="272.5" text-anchor="middle" font-size="10.5">of the Architecture Roadmap</text><line x1="528" y1="262" x2="562" y2="262" stroke="#555" marker-end="url(#arr-f4-13)"/><text x="380" y="334" text-anchor="middle" font-size="11" fill="#666">The Application lane also takes the Data lane's gap results and roadmap components as inputs, if available (ADM §7.2)</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">Phase C: two lanes inside one phase. Original drawing; inputs and outputs per ADM §6.2, ADM §6.4, ADM §7.2 and ADM §7.4, steps per ADM §6.3 and ADM §7.3.</figcaption>
</figure>

> **Trap.** Phase C is *one* phase. An option that lists "Phase C: Data Architecture" and "Phase
> C: Application Architecture" as two of the ADM's phases is wrong; there are two chapters, not
> two phases, and the standard allows either order.

> **Trap.** Data principles and application principles enter Phase C as inputs "if existing" and
> are reviewed or generated in step 1 of the relevant part. They are not Preliminary Phase steps.

## Check yourself

1. What are the four kinds of data a Data Architecture must handle?
2. Which extra external reference materials does the Data part list that the Application part does not?
3. Which two other domains does the Application stakeholder review check for impact, and which domain does it constrain?
4. What three dimensions does data governance cover?
