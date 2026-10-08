---
title: Tailored Architecture Framework — Northgate adaptation of the TOGAF Standard
deliverable: Tailored Architecture Framework
phase: PRELIM
kind: DELIVERABLE
summary: How Northgate adapted the method, the content and the tools to a small team, a PRINCE2 change process and a two-year programme.
refs: ["CONTENT §4.2.21", "ADM §2.3", "ADM §2.4"]
source: authored
status: draft
---

> **What to notice.** Tailoring happens at two levels: once for the *enterprise* (terminology, management frameworks, tools) and again for the *project* (which deliverables and artefacts this cycle will actually produce). Both are in this one document. It is produced in the Preliminary Phase, may be refined in Phase A, and is an input to every phase.

| | |
|---|---|
| Version | 1.0, 20 February 2026 (project tailoring added 10 March 2026 as v1.1) |
| Owner | Chief Architect |

## 1. Tailored architecture method

**Enterprise level.**

| Aspect | Tailoring |
|---|---|
| Cycle | The full ADM, run once per programme. Small changes use a "lite" path: Phase A vision note, one combined B–D pass, then E–G. |
| Terminology | "Deliverable" and "artefact" keep their TOGAF meaning. "Work package" is called a *project* once it enters the PRINCE2 portfolio; the roadmap keeps the TOGAF term. "Transition Architecture" is called a *release* in delivery plans; the mapping is kept in the roadmap. |
| Iteration | Phases B, C and D are run once for the baseline and once for the target, rather than baseline-then-target inside each phase, because the same three architects do all three domains. |
| Phase gates | Every phase ends at the Architecture Board. Phases B–D share one gate to save calendar time. |
| Requirements Management | The Requirements Catalog is the single requirements store; delivery projects link their backlog items to catalog ids. |

**Project level (Digital Channels).**

- Phase A: Business Scenario workshop *is* the stakeholder engagement; no separate interviews.
- Phases B–D produce one Architecture Definition Document with a chapter per domain, not four documents.
- Phase E produces two Transition Architectures because the Q3 2027 card re-issue splits the programme in two.
- Phase G compliance reviews at two checkpoints per project, not the vendor's five.

## 2. Tailored architecture content (deliverables and artefacts)

| Deliverable | Produced? | Tailoring |
|---|---|---|
| Request for Architecture Work, Statement of Architecture Work, Architecture Vision | Yes | Vision is limited to four pages plus the Value Chain and Solution Concept diagrams |
| Communications Plan | Yes | Merged into the programme's PRINCE2 communication management approach after Phase A |
| Capability Assessment | Yes | Business Transformation Readiness Assessment uses the standard's readiness factors; IT capability section is one page |
| Architecture Definition Document, Architecture Requirements Specification | Yes | One document each, chapters per domain |
| Architecture Roadmap, Implementation and Migration Plan | Yes | The Implementation and Migration Plan is written in PRINCE2 project-brief form so the PMO can consume it unchanged |
| Implementation Governance Model, Architecture Contract | Yes | One contract per delivery project, signed at project initiation |
| Compliance Assessment, Change Request, Requirements Impact Assessment | Yes | Templates in the repository; a Change Request under £50k impact is handled by the Chief Architect without a Board meeting |
| Architecture Building Blocks, Solution Building Blocks | Yes | Held as repository pages, not documents |

Artefacts selected for this project (of the catalog in the Architecture Content Framework): Principles catalog; Stakeholder Map matrix; Value Chain, Solution Concept, Business Capability Map and Value Stream diagrams; Organization/Actor, Driver/Goal/Objective, Business Service/Function and Role catalogs; Process Flow diagram; Data Entity/Data Component catalog; Conceptual and Logical Data diagrams; Application Portfolio and Interface catalogs; Application Communication diagram; Technology Standards and Portfolio catalogs; Environments and Locations diagram; Project Context and Benefits diagrams; Requirements catalog. Everything else is produced only if a stakeholder concern needs it.

## 3. Configured and deployed tools

| Purpose | Tool | Configuration |
|---|---|---|
| Modelling | The bank's ArchiMate tool | One model per cycle; views named `<phase>-<artefact>`; exported weekly as read-only pages |
| Repository | Confluence space "Architecture Repository" | Structured as Architecture Metamodel / Landscape / Reference Library / Standards Information Base / Governance Log |
| Requirements | Jira project ARCH | Issue types Requirement, Assumption, Constraint, Gap with the catalog id as key |
| Publishing | Confluence public-to-bank pages | Every deliverable published at its phase gate |

## 4. Interfaces with governance models and other frameworks

| Framework | Interface |
|---|---|
| Corporate business planning | The Retail Strategy supplies the business drivers; the Architecture Roadmap feeds the annual investment plan each September |
| Enterprise Architecture governance | Architecture Board, fortnightly; waivers and compliance in the Governance Log |
| Portfolio, programme and project management (PRINCE2 / PMO) | Work packages become PRINCE2 projects; the Implementation and Migration Plan is the programme's plan of record; project boards include an EA member |
| System development and engineering (Retail IT's Scrum) | Architecture requirements enter backlogs as linked stories; a compliance review is a definition-of-done item at two checkpoints |
| Operations (ITIL service management) | Transition Architectures map to releases; the Implementation Governance Model names the change-advisory board hand-off |
