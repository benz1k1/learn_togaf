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

## The Architecture Repository (CONTENT §9)

Architecture Metamodel; Architecture Capability; **Architecture Landscape**; **Standards
Library** (Standards Information Base); **Reference Library**; **Governance Repository**
(decisions, compliance assessments, dispensations); **Architecture Requirements Repository**;
**Solutions Landscape**. Questions ask *which part holds X*.

## The Enterprise Continuum (CONTENT §8)

A classification from generic to specific: **Foundation** → **Common Systems** → **Industry**
→ **Organization-Specific**. The **Architecture Continuum** applies it to ABBs, the
**Solutions Continuum** to SBBs. The continuum classifies; the repository stores.
