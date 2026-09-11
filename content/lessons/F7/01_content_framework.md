---
title: The content framework, artifacts by phase, building blocks, repository and continuum
unit: F7
objectives: ["7.1", "7.2", "7.3", "7.4", "7.5"]
refs: ["CONTENT §3", "CONTENT §4", "CONTENT §5", "CONTENT §8", "CONTENT §9"]
reading_minutes: 10
source: authored
status: draft
---
## The content metamodel (CONTENT §3)

The metamodel defines the entity types an architecture description uses (actors, roles,
functions, business services, processes, data entities, application components, technology
components, and the motivation entities: drivers, goals, objectives) and the relationships
between them. It has a **core** and optional **extensions** (governance, services, process
modelling, data, infrastructure consolidation, motivation).

## Artifacts by phase (CONTENT §4)

Every artifact is a catalog, a matrix or a diagram, and each belongs to a phase. The artefact
catalogue page lists all of them with a filter; the ones the exam tests most:

- **Preliminary**: Principles Catalog.
- **A**: Stakeholder Map Matrix, Value Chain Diagram, Solution Concept Diagram.
- **B**: Organization/Actor and Role catalogs, Business Interaction and Actor/Role matrices,
  Business Footprint and Functional Decomposition diagrams.
- **C (Data)**: Data Entity/Data Component Catalog, Data Entity/Business Function and
  Application/Data matrices, Conceptual and Logical Data diagrams.
- **C (Application)**: Application Portfolio and Interface catalogs, Application/Organization
  and Application Interaction matrices, Application Communication diagram.
- **D**: Technology Standards and Technology Portfolio catalogs, Application/Technology
  matrix, Environments and Locations diagram.
- **E**: Project Context and Benefits diagrams.
- **Requirements Management**: Requirements Catalog.

## Building blocks (CONTENT §5)

An **ABB** captures architecture requirements and guides SBBs; an **SBB** is a candidate
physical solution. Building blocks are identified in B, C and D and re-used from the
repository whenever possible.

<figure class="my-4">
<svg viewBox="0 0 760 218" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="The content framework as three layers, metamodel to artifacts to deliverables, beside an architecture building block being realised by a solution building block">
<defs><marker id="arr-f7-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
<rect x="15" y="15" width="500" height="50" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="265.0" y="37.0" text-anchor="middle" font-size="10" font-weight="bold">Enterprise Metamodel</text>
<text x="265.0" y="50.0" text-anchor="middle" font-size="10">the entity types and relationships an architecture description may use; core + extensions</text>
<line x1="265" y1="65" x2="265" y2="85" stroke="#555" marker-end="url(#arr-f7-a)"/>
<rect x="15" y="85" width="500" height="50" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/>
<text x="265.0" y="107.0" text-anchor="middle" font-size="10" font-weight="bold">Artifacts</text>
<text x="265.0" y="120.0" text-anchor="middle" font-size="10">catalogs · matrices · diagrams — each belongs to a phase</text>
<line x1="265" y1="135" x2="265" y2="155" stroke="#555" marker-end="url(#arr-f7-a)"/>
<rect x="15" y="155" width="500" height="50" rx="6" fill="#fff1d6" stroke="#e0b060"/>
<text x="265.0" y="177.0" text-anchor="middle" font-size="10" font-weight="bold">Deliverables</text>
<text x="265.0" y="190.0" text-anchor="middle" font-size="10">contractually specified outputs assembled from artifacts, e.g. the Architecture Definition Document</text>
<text x="280" y="76" text-anchor="start" font-size="9" fill="#666">defines the content of</text>
<text x="280" y="146" text-anchor="start" font-size="9" fill="#666">are assembled into</text>
<rect x="545" y="40" width="200" height="56" rx="6" fill="#fff" stroke="#666"/>
<text x="645.0" y="58.5" text-anchor="middle" font-size="10" font-weight="bold">ABB</text>
<text x="645.0" y="71.5" text-anchor="middle" font-size="10">captures architecture requirements;</text>
<text x="645.0" y="84.5" text-anchor="middle" font-size="10">guides the SBB</text>
<line x1="645" y1="96" x2="645" y2="128" stroke="#555" marker-end="url(#arr-f7-a)"/>
<text x="655" y="116" text-anchor="start" font-size="9" fill="#666">realised by</text>
<rect x="545" y="130" width="200" height="56" rx="6" fill="#fff" stroke="#666"/>
<text x="645.0" y="148.5" text-anchor="middle" font-size="10" font-weight="bold">SBB</text>
<text x="645.0" y="161.5" text-anchor="middle" font-size="10">a candidate physical solution</text>
<text x="645.0" y="174.5" text-anchor="middle" font-size="10">re-used from the repository if possible</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">Three layers of the content framework, and ABB to SBB beside them. Original drawing; metamodel per CONTENT §2, artifacts per CONTENT §3, deliverables per CONTENT §4, building blocks per CONTENT §5.</figcaption>
</figure>

## The Architecture Repository (CONTENT §9)

Architecture Metamodel; Architecture Capability; **Architecture Landscape**; **Standards
Library** (Standards Information Base); **Reference Library**; **Governance Repository**
(decisions, compliance assessments, dispensations); **Architecture Requirements Repository**;
**Solutions Landscape**. Questions ask *which part holds X*.

## The Enterprise Continuum (CONTENT §8)

A classification from generic to specific: **Foundation** → **Common Systems** → **Industry**
→ **Organization-Specific**. The **Architecture Continuum** applies it to ABBs, the
**Solutions Continuum** to SBBs. The continuum classifies; the repository stores.

<figure class="my-4">
<svg viewBox="0 0 760 312" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="The Enterprise Continuum as a left to right spectrum from Foundation to Organization-Specific above the eight parts of the Architecture Repository">
<defs><marker id="arr-f7-b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
<rect x="15" y="26" width="175" height="34" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="102.5" y="46.9" text-anchor="middle" font-size="11" font-weight="bold">Foundation</text>
<line x1="190" y1="43" x2="200" y2="43" stroke="#555" marker-end="url(#arr-f7-b)"/>
<rect x="200" y="26" width="175" height="34" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/>
<text x="287.5" y="46.9" text-anchor="middle" font-size="11" font-weight="bold">Common Systems</text>
<line x1="375" y1="43" x2="385" y2="43" stroke="#555" marker-end="url(#arr-f7-b)"/>
<rect x="385" y="26" width="175" height="34" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="472.5" y="46.9" text-anchor="middle" font-size="11" font-weight="bold">Industry</text>
<line x1="560" y1="43" x2="570" y2="43" stroke="#555" marker-end="url(#arr-f7-b)"/>
<rect x="570" y="26" width="175" height="34" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/>
<text x="657.5" y="46.9" text-anchor="middle" font-size="11" font-weight="bold">Organization-Specific</text>
<text x="15" y="16" text-anchor="start" font-size="10" fill="#666">generic</text>
<text x="745" y="16" text-anchor="end" font-size="10" fill="#666">specific</text>
<rect x="15" y="68" width="730" height="22" rx="6" fill="#f1f1f1" stroke="#999"/>
<text x="380.0" y="82.5" text-anchor="middle" font-size="10">Architecture Continuum — classifies ABBs along this spectrum</text>
<rect x="15" y="94" width="730" height="22" rx="6" fill="#f1f1f1" stroke="#999"/>
<text x="380.0" y="108.5" text-anchor="middle" font-size="10">Solutions Continuum — classifies SBBs along the same spectrum</text>
<text x="380" y="140" text-anchor="middle" font-size="11" fill="#345" font-weight="bold">the Enterprise Continuum classifies</text>
<rect x="15" y="150" width="730" height="150" rx="10" fill="#fafafa" stroke="#999"/>
<text x="30" y="170" text-anchor="start" font-size="11" fill="#345" font-weight="bold">the Architecture Repository stores</text>
<rect x="30" y="180" width="168" height="44" rx="6" fill="#fff" stroke="#666"/>
<text x="114.0" y="205.5" text-anchor="middle" font-size="10">Architecture Metamodel</text>
<rect x="210" y="180" width="168" height="44" rx="6" fill="#fff" stroke="#666"/>
<text x="294.0" y="205.5" text-anchor="middle" font-size="10">Architecture Capability</text>
<rect x="390" y="180" width="168" height="44" rx="6" fill="#fff" stroke="#666"/>
<text x="474.0" y="205.5" text-anchor="middle" font-size="10">Architecture Landscape</text>
<rect x="570" y="180" width="168" height="44" rx="6" fill="#fff" stroke="#666"/>
<text x="654.0" y="205.5" text-anchor="middle" font-size="10">Standards Library (SIB)</text>
<rect x="30" y="234" width="168" height="44" rx="6" fill="#fff" stroke="#666"/>
<text x="114.0" y="253.0" text-anchor="middle" font-size="10">Reference Library</text>
<text x="114.0" y="266.0" text-anchor="middle" font-size="10">reference models, patterns</text>
<rect x="210" y="234" width="168" height="44" rx="6" fill="#fff" stroke="#666"/>
<text x="294.0" y="246.5" text-anchor="middle" font-size="10">Governance Repository</text>
<text x="294.0" y="259.5" text-anchor="middle" font-size="10">decisions, compliance,</text>
<text x="294.0" y="272.5" text-anchor="middle" font-size="10">dispensations</text>
<rect x="390" y="234" width="168" height="44" rx="6" fill="#fff" stroke="#666"/>
<text x="474.0" y="259.5" text-anchor="middle" font-size="10">Requirements Repository</text>
<rect x="570" y="234" width="168" height="44" rx="6" fill="#fff" stroke="#666"/>
<text x="654.0" y="259.5" text-anchor="middle" font-size="10">Solutions Landscape</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">The continuum as a spectrum, the repository as boxes. Original drawing; continuum per CONTENT §6.3 and §6.4, repository parts per CONTENT §7.1.</figcaption>
</figure>
