---
title: Architecture Repository — structure and initial content
deliverable: Architecture Repository
phase: PRELIM
kind: DELIVERABLE
summary: What Northgate's repository contains after the Preliminary Phase, laid out by the standard's six-part structure, and what each phase of the cycle adds to it.
refs: ["CONTENT §4.2.5", "CONTENT §7", "ADM §2.4"]
source: authored
status: draft
---

> **What to notice.** The repository is a deliverable *and* the place deliverables live. The standard's structure — Architecture Metamodel, Architecture Capability, Architecture Landscape, Standards Information Base, Reference Library, Governance Log (plus the Architecture Requirements Repository and Solutions Landscape) — is what the exam tests; the Enterprise Continuum is the classification the Reference Library and Landscape use, not a part of the repository. An "initial" repository is a Preliminary Phase output; every later phase updates it.

| | |
|---|---|
| Location | Confluence space *Architecture Repository*, modelling tool project *Northgate 2026* |
| Custodian | Chief Architect; read access for the whole bank from 1 March 2026 |

## Structure and contents at the end of the Preliminary Phase

| Part | What Northgate keeps there | Initial content (February 2026) |
|---|---|---|
| **Architecture Metamodel** | The tailored content metamodel: which entity types and relationships the bank models, and naming rules | Core content metamodel plus the Governance and Process extensions; entity naming rules; the artefact list from the Tailored Architecture Framework |
| **Architecture Capability** | How the capability itself is organised and run | Organizational Model for EA; Tailored Architecture Framework; Architecture Principles; the ACMM scorecard |
| **Architecture Landscape** | Architectural representations of the enterprise at Strategic, Segment and Capability level, each with a state and a date | Strategic: the 2025 Core Banking target (retain to 2029). Segment: Retail Banking baseline — 40 diagrams migrated from the old tool, dated and marked *baseline, unverified* |
| **Standards Information Base** | Standards the bank has adopted, each with a lifecycle state | Technology standards (PostgreSQL 16, OpenJDK 21, Kafka 3.7, RHEL 9 — *adopted*; Oracle 11g — *retire*); ISO 8583 card messaging — *mandated by the network*; OpenAPI 3 for every new interface — *adopted* |
| **Reference Library** | Templates, patterns and reference models, internal and external | Core Banking vendor reference architecture; card network integration guide; the bank's deliverable templates (this cycle's documents become templates at Phase H) |
| **Governance Log** | Decisions, waivers, compliance assessments, capability assessments, calendar | Board minutes AB-2026-02 to -04; principle-conflict decision (PR-03 v PR-05); the waiver register (empty) |
| **Architecture Requirements Repository** | Every requirement, assumption, constraint and gap, with its status | Jira project ARCH, empty except the constraints from the Request for Architecture Work (CN-01 onwards) |
| **Solutions Landscape** | Solution Building Blocks as deployed | Core Banking v12, Card Switch, Mobile App v3, Data Warehouse — recorded from the CMDB |

## Classification: the Enterprise Continuum applied

Everything in the Landscape and Reference Library is tagged on the continuum so re-use is findable:

| Continuum position | Northgate example |
|---|---|
| Foundation | The TOGAF content metamodel; the technology standards |
| Common systems | The API-layer pattern and the security patterns from the vendor reference architecture |
| Industry | ISO 8583 card messaging; the open-banking API standard the app will expose |
| Organization-specific | Northgate's capability map, principles, and every architecture in the Landscape |

## What each phase adds

| Phase | Adds to the repository |
|---|---|
| A | Architecture Vision, Statement of Architecture Work, stakeholder map, Communications Plan, Capability Assessment; Landscape gets the *Digital Channels* segment, state *target, draft* |
| B–D | Architecture Definition Document and Architecture Requirements Specification drafts; catalogs, matrices and diagrams per domain; Architecture Building Blocks; new requirements in the Requirements Repository |
| E–F | Architecture Roadmap, Transition Architectures, Implementation and Migration Plan, Implementation Governance Model; Landscape gains two transition states with dates |
| G | Architecture Contracts, Compliance Assessments and Change Requests into the Governance Log; Solution Building Blocks into the Solutions Landscape |
| H | Change classifications, the re-scored ACMM, lessons learned; templates promoted to the Reference Library |

## Access and rules

- Everyone in the bank can read. Only EA writes to the Landscape, Standards Information Base and Governance Log; delivery teams write to the Solutions Landscape through the CMDB feed.
- Every item carries an owner, a state (draft / approved / superseded / retired) and a review date; the Governance Log records who changed state and why.
- Nothing is deleted; superseded items stay for the audit trail the regulator expects.
