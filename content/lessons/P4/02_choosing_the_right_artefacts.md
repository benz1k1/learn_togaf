---
title: Choosing the right artefacts — viewpoints, catalogs, matrices and diagrams per domain
unit: P4
objectives: ["P4.1"]
refs: ["CONTENT §3.1", "CONTENT §3.6.1", "CONTENT §3.6.3", "CONTENT §3.6.4", "CONTENT §3.6.5", "CONTENT §3.6.6", "CONTENT §3.6.7", "ADM §4.3.1", "ADM §4.5.3", "ADM §4.5.4", "ADM §4.5.5", "ADM §4.5.6", "TECH §3.3.4", "TECH §3.4", "GUIDE:adm-practitioners §5.1"]
reading_minutes: 12
source: authored
status: draft
---
## What an artefact-selection scenario looks like

The scenario names a stakeholder and a question — the CFO wants to see how the programme's
spend traces to goals; the security officer wants to know who can reach personal data; the
operations manager wants to know which applications sit where; the migration lead wants to know
what moves in each stage — and asks which artefact you produce. The five-point answer names the
specific catalog, matrix or diagram, the phase it belongs to, and the concern it answers; the
three-point answer names a plausible artefact from the wrong phase or a generic "model"
(CONTENT §3.6.1; TECH §3.3.4).

The rule behind every such question is the first step of Phases B, C and D: select relevant
viewpoints — those that will let the architect demonstrate how the stakeholder concerns are
addressed — and for each viewpoint the models needed; if a concern is not covered, create or
augment a model (ADM §4.3.1). To select a viewpoint you must know the stakeholder and the
concern, and any information not required to address a concern should not be gathered
(GUIDE:adm-practitioners §5.1).

## Three kinds of artefact

Catalogs are lists of building blocks of one or related types, used for governance or reference,
carrying metamodel metadata for query. Matrices are grids showing relationships between two or
more entities, for relationships that are list-based rather than graphical — a CRUD matrix is
the standard's example of something hard to draw. Diagrams render content graphically for
stakeholders to retrieve information, and may be produced several times with different style or
coverage to suit different concerns (CONTENT §3.6.1). Views are what stakeholders see and are
built from selected parts of models to demonstrate that concerns are addressed; viewpoints are
the re-usable conventions for producing them (CONTENT §3.1).

<figure class="my-4">
<svg viewBox="0 0 760 360" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="10" role="img" aria-label="A placement chart with four phase columns, A, B, C and D, and rows for catalogs, matrices and diagrams; typical artefacts are placed in each cell and a strip along the bottom shows which stakeholder concern each family answers">
<defs><marker id="arr-p4-02a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
<text x="380" y="18" text-anchor="middle" font-size="12" font-weight="bold">Artefact placement: phase across, kind down</text>
<rect x="70" y="30" width="150" height="24" fill="#f1f1f1" stroke="#999"/><text x="145" y="46" text-anchor="middle" font-weight="bold">Phase A</text>
<rect x="222" y="30" width="200" height="24" fill="#f1f1f1" stroke="#999"/><text x="322" y="46" text-anchor="middle" font-weight="bold">Phase B — Business</text>
<rect x="424" y="30" width="200" height="24" fill="#f1f1f1" stroke="#999"/><text x="524" y="46" text-anchor="middle" font-weight="bold">Phase C — Data / Application</text>
<rect x="626" y="30" width="124" height="24" fill="#f1f1f1" stroke="#999"/><text x="688" y="46" text-anchor="middle" font-weight="bold">Phase D — Tech.</text>
<rect x="10" y="56" width="58" height="80" fill="#e3f0fb" stroke="#4a7fb5"/><text x="39" y="100" text-anchor="middle" font-weight="bold">Catalogs</text>
<rect x="70" y="56" width="150" height="80" fill="#fff" stroke="#999"/>
<text x="145" y="76" text-anchor="middle">Stakeholder catalog</text>
<text x="145" y="92" text-anchor="middle" font-size="9">(informal; no metamodel</text>
<text x="145" y="104" text-anchor="middle" font-size="9">entities — sensitive)</text>
<rect x="222" y="56" width="200" height="80" fill="#fff" stroke="#999"/>
<text x="322" y="72" text-anchor="middle" font-size="9">Organization/Actor &#183; Driver/Goal/Objective</text>
<text x="322" y="86" text-anchor="middle" font-size="9">Role &#183; Business Service/Function &#183; Location</text>
<text x="322" y="100" text-anchor="middle" font-size="9">Process/Event/Control/Product &#183; Contract/Measure</text>
<text x="322" y="114" text-anchor="middle" font-size="9">Business Capabilities &#183; Value Stream (+ Stages)</text>
<text x="322" y="128" text-anchor="middle" font-size="9">Business Glossary</text>
<rect x="424" y="56" width="200" height="80" fill="#fff" stroke="#999"/>
<text x="524" y="76" text-anchor="middle" font-size="9">Data Entity / Data Component</text>
<text x="524" y="96" text-anchor="middle" font-size="9">Application Portfolio (the start point of C-app)</text>
<text x="524" y="110" text-anchor="middle" font-size="9">Interface catalog (dependencies scoped early)</text>
<rect x="626" y="56" width="124" height="80" fill="#fff" stroke="#999"/>
<text x="688" y="80" text-anchor="middle" font-size="9">Technology Standards</text>
<text x="688" y="100" text-anchor="middle" font-size="9">Technology Portfolio</text>
<text x="688" y="114" text-anchor="middle" font-size="9">(the start point of D)</text>
<rect x="10" y="138" width="58" height="70" fill="#e3f0fb" stroke="#4a7fb5"/><text x="39" y="177" text-anchor="middle" font-weight="bold">Matrices</text>
<rect x="70" y="138" width="150" height="70" fill="#fff" stroke="#999"/><text x="145" y="177" text-anchor="middle" font-size="9">—</text>
<rect x="222" y="138" width="200" height="70" fill="#fff" stroke="#999"/>
<text x="322" y="156" text-anchor="middle" font-size="9">Business Interaction &#183; Actor/Role</text>
<text x="322" y="170" text-anchor="middle" font-size="9">Value Stream/Capability &#183; Strategy/Capability</text>
<text x="322" y="184" text-anchor="middle" font-size="9">Capability/Organization</text>
<rect x="424" y="138" width="200" height="70" fill="#fff" stroke="#999"/>
<text x="524" y="156" text-anchor="middle" font-size="9">Data Entity/Business Function &#183; Application/Data</text>
<text x="524" y="172" text-anchor="middle" font-size="9">Application/Organization &#183; Role/Application</text>
<text x="524" y="188" text-anchor="middle" font-size="9">Application/Function &#183; Application Interaction</text>
<rect x="626" y="138" width="124" height="70" fill="#fff" stroke="#999"/>
<text x="688" y="177" text-anchor="middle" font-size="9">Application/Technology</text>
<rect x="10" y="210" width="58" height="96" fill="#e3f0fb" stroke="#4a7fb5"/><text x="39" y="262" text-anchor="middle" font-weight="bold">Diagrams</text>
<rect x="70" y="210" width="150" height="96" fill="#fff" stroke="#999"/>
<text x="145" y="230" text-anchor="middle" font-size="9">Value Chain &#183; Solution Concept</text>
<text x="145" y="246" text-anchor="middle" font-size="9">Business Model diagram</text>
<text x="145" y="262" text-anchor="middle" font-size="9">Business Capability Map</text>
<text x="145" y="278" text-anchor="middle" font-size="9">Value Stream Map</text>
<rect x="222" y="210" width="200" height="96" fill="#fff" stroke="#999"/>
<text x="322" y="228" text-anchor="middle" font-size="9">Business Footprint &#183; Business Service/Information</text>
<text x="322" y="242" text-anchor="middle" font-size="9">Functional Decomposition &#183; Product Lifecycle</text>
<text x="322" y="256" text-anchor="middle" font-size="9">Goal/Objective/Business Service &#183; Business Use-Case</text>
<text x="322" y="270" text-anchor="middle" font-size="9">Organization Decomposition &#183; Process Flow &#183; Event</text>
<text x="322" y="284" text-anchor="middle" font-size="9">Capability Map &#183; Value Stream Map &#183; Org. Map &#183; Info. Map</text>
<rect x="424" y="210" width="200" height="96" fill="#fff" stroke="#999"/>
<text x="524" y="228" text-anchor="middle" font-size="9">Conceptual &#183; Logical Data &#183; Data Dissemination</text>
<text x="524" y="242" text-anchor="middle" font-size="9">Data Security &#183; Data Migration &#183; Data Lifecycle</text>
<text x="524" y="258" text-anchor="middle" font-size="9">Application Communication &#183; App. and User Location</text>
<text x="524" y="272" text-anchor="middle" font-size="9">Application Use-Case &#183; Enterprise Manageability</text>
<text x="524" y="286" text-anchor="middle" font-size="9">Process/App. Realization &#183; Software Eng. &#183; App. Migration &#183; Software Distribution</text>
<rect x="626" y="210" width="124" height="96" fill="#fff" stroke="#999"/>
<text x="688" y="230" text-anchor="middle" font-size="9">Environments and Locations</text>
<text x="688" y="246" text-anchor="middle" font-size="9">Platform Decomposition</text>
<text x="688" y="262" text-anchor="middle" font-size="9">Processing</text>
<text x="688" y="278" text-anchor="middle" font-size="9">Networked Computing/Hardware</text>
<text x="688" y="294" text-anchor="middle" font-size="9">Network and Communications</text>
<rect x="10" y="316" width="740" height="36" rx="6" fill="#fff1d6" stroke="#e0b060"/>
<text x="380" y="331" text-anchor="middle" font-size="9">Read the concern first: "traceability to goals" → Business Footprint &#183; "who reaches which data" → Data Security &#183; "what moves per stage" → Application / Data Migration</text>
<text x="380" y="345" text-anchor="middle" font-size="9">"which locations host what" → Environments and Locations &#183; "how many licences / where is support" → Application and User Location &#183; "load and deployment units" → Processing</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">Original drawing. The artefacts per phase follow CONTENT §3.6.3 to §3.6.7; the concern-to-artefact readings follow the purpose statements in those sections.</figcaption>
</figure>

## Phase B: the business artefacts and the four maps

The Business Architecture is decomposed with business capability mapping, information mapping,
organisation mapping, process modelling, structured analysis, use-case analysis and value stream
mapping, at a rigour that varies with the effort's goals (ADM §4.3.1). Four maps carry the
approach: the capability map is a self-contained view independent of structure, process,
systems and portfolio, and heat mapping over it shows maturity, effectiveness, performance and
value or cost (ADM §4.5.3); value streams give the *why* behind capabilities and are analysed by
heat-mapping stages or developing use-cases (ADM §4.5.4); the organisation map shows the units,
partners and stakeholder groups and their working relationships, "as distinct from an
organizational chart", and tells you which units to involve and when (ADM §4.5.5); the
information map starts from what matters most to the business and pays off in matrices between
information and capabilities (ADM §4.5.6).

Among the diagrams, the Business Footprint links goals, organisation units, functions and
services to the technical components delivering them and is "a communication platform for
senior-level (CxO) stakeholders"; the Business Service/Information diagram shows the data a
service consumes and produces and is the basis for Phase C data; the Functional Decomposition
diagram shows capabilities on one page and takes heat maps for scope decisions; the
Organization Decomposition diagram shows the chain of command of owners and decision-makers
(CONTENT §3.6.4). Among the matrices, Business Interaction shows relationships between
organisations and functions, and Actor/Role supports security and skills definition and
training needs (CONTENT §3.6.4).

## Phase C: data and application

The Data Entity/Business Function matrix assigns ownership of entities to organisations, defines
application of origin, record and reference, and supports data governance programmes; the
Application/Data matrix shows which applications create, read, update and delete which
entities, exposing duplication and where the same data is updated in more than one place
(CONTENT §3.6.5). The Data Dissemination diagram shows how logical entities are realised by
application components, including replication and master-copy relationships; the Data Security
diagram shows which data is accessed by which roles, units and applications and demonstrates
compliance with privacy law; the Data Migration diagram shows extraction, transformation and
loading from source to target, at overview level in Phase C (CONTENT §3.6.5).

The Application Portfolio catalog is "typically the start point of the Application Architecture
phase" and defines the horizontal scope of change; the Interface catalog scopes dependencies
between applications as early as possible; the Application Communication diagram shows
components and interfaces, logically, with intermediary technology only where relevant; the
Application and User Location diagram supports licence, support-centre and server-sizing
decisions; the Application Migration diagram shows precisely which applications and interfaces
map between migration stages, including temporary applications and parallel-run environments
(CONTENT §3.6.6).

## Phase D: technology

The Technology Portfolio catalog lists all technology in use, classified against the adopted
taxonomy such as the TRM, and is the start point of Phase D; the Technology Standards catalog
records agreed standards, versions, lifecycles and refresh cycles, and applying it to the
portfolio gives a baseline view of compliance (CONTENT §3.6.7). The Application/Technology
matrix maps applications to platforms and complements the Platform Decomposition diagram; the
Environments and Locations diagram shows which locations host which applications and where
non-production environments live; the Processing diagram groups components into deployment
units and shows how usage patterns create load; the Networked Computing/Hardware diagram shows
the "as deployed" mapping of applications to servers across development and production; the
Network and Communications diagram addresses protocol and capacity, not content (CONTENT §3.6.7).

**Trap.** The Stakeholder catalog belongs to Phase A and, because of its sensitivity and the
informal modelling of that phase, uses no metamodel entities; the Value Chain and Solution
Concept diagrams are Phase A on-boarding sketches, not Phase B models (CONTENT §3.6.3).

## The stakeholder map tells you who gets what

The template stakeholder map is an answer key: Enterprise Security gets Data Security, Data
Dissemination and Actor/Role; Procurement gets the Technology Portfolio and Standards catalogs;
IT Operations infrastructure gets Platform Decomposition, Environments and Locations and
Processing; Regulators get Business Footprint and Application Communication; HR gets
Organization Decomposition, Organization/Actor and Location catalogs and the Application and
User Location diagram (TECH §3.4). That is the step "tailor engagement deliverables" done
(TECH §3.3.4).

## How the 5-point answer differs from the 3-point one

| Points | What the answer does |
|---|---|
| 5 | Names the exact artefact and its phase, ties it to the stakeholder's concern via a selected viewpoint, and stops gathering at what that concern needs |
| 3 | Names a related artefact from the right family but the wrong phase (a Phase A Solution Concept for a Phase C question), or the right diagram without the matrix that gives it its data |
| 1 | Produces "the full set of catalogs, matrices and diagrams for the phase" regardless of concern |
| 0 | Hands the CxO the platform decomposition, or answers a data-privacy concern with an organisation chart |

## Where to look in the book

Architecture Content §3.6.1 (catalog, matrix, diagram), §3.6.3 (Phase A), §3.6.4 (Phase B),
§3.6.5 (Phase C data), §3.6.6 (Phase C application), §3.6.7 (Phase D) — each artefact has a
purpose paragraph that is the exam's answer key. ADM §4.3.1 (select viewpoints), §4.5.3 to
§4.5.6 (the four maps). ADM Techniques §3.3.4 and §3.4 (artefacts per stakeholder class).
