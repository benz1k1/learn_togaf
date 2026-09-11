---
title: Phase D, Technology Architecture, in depth
unit: F4
objectives: ["4.3", "4.4"]
refs: ["ADM §8", "ADM §8.1", "ADM §8.2", "ADM §8.2.1", "ADM §8.2.2", "ADM §8.2.3", "ADM §8.3", "ADM §8.3.1", "ADM §8.3.2", "ADM §8.3.3", "ADM §8.3.7", "ADM §8.3.9", "ADM §8.4", "ADM §8.5", "ADM §8.5.1", "ADM §8.5.2"]
reading_minutes: 10
source: authored
status: draft
---
## What the phase is for

Phase D develops the Technology Architecture for the project (ADM §8). Objectives (ADM §8.1):

| Objective | Pattern |
|---|---|
| Develop the **Target Technology Architecture** that enables the Architecture Vision and the target business, data and application building blocks to be delivered through **technology components and technology services**, addressing the Statement of Architecture Work and stakeholder concerns | develop the target |
| Identify candidate Architecture Roadmap components from the gaps between Baseline and Target Technology Architectures | gaps → roadmap components |

The wording of the first objective is the distinctive bit: Phase D exists so that the building
blocks decided in B and C can be *delivered* through technology.

## Approach

Two short sections. **Emerging technologies** (ADM §8.5.1): new technology is a major driver for
change, so the Technology Architecture must capture the transformation opportunities it opens
up. The ADM's flexibility lets technology change be a driver and strategic resource rather than
merely the recipient of Change Requests — the Technology Architecture may both drive business
capabilities and respond to information system requirements at the same time.

**Architecture Repository** (ADM §8.5.2): consider existing IT services in the IT service
catalog, the adopted technical reference model (if any), generic technology models for the
industry sector, and technology models for Common Systems Architectures, including the III-RM.

## Inputs

| Group | Inputs |
|---|---|
| External (ADM §8.2.1) | architecture reference materials; **product information on candidate products** |
| Non-architectural (ADM §8.2.2) | Request for Architecture Work; Capability Assessment; Communications Plan |
| Architectural (ADM §8.2.3) | Organizational Model for EA; Tailored Architecture Framework; **technology principles**, if existing; Statement of Architecture Work; Architecture Vision; Architecture Repository; draft Architecture Definition Document; draft Architecture Requirements Specification with gap results from the Business, Data **and** Application Architectures and technical requirements from previous phases; **Business, Data and Application** components of an Architecture Roadmap |

Phase D is the only development phase whose external inputs name product information — a hint
that product selection can happen here.

## Steps

The nine development steps (ADM §8.3). Existing technology building blocks may have to be
*redefined* here to ensure interoperability and fitness within this particular Technology
Architecture.

| # | Step | Technology-specific detail |
|---|---|---|
| 1 | Select reference models, viewpoints and tools | review the technology principles; the modeling process defines a taxonomy of technology services and logical components, inventories deployed technology, checks fitness for purpose, selects and configures products, and determines impact (sizing, capacity, migration); service granularity decided earlier affects performance, maintainability, location/latency and availability; product selection that deviates from standards or has wide impact is flagged as an opportunity for Phase E (ADM §8.3.1) |
| 2 | Develop Baseline Technology Architecture Description | convert the existing environment into the organization's taxonomy of technology services and components, e.g. the Technical Reference Model (ADM §8.3.2) |
| 3 | Develop Target Technology Architecture Description | conceptualize ABBs — functionality and how it may be implemented, without configuration or design detail; consider alternatives (ADM §8.3.3) |
| 4 | Perform gap analysis | as in B and C |
| 5 | Define candidate roadmap components | an initial technology roadmap for Phase E |
| 6 | Resolve impacts across the Architecture Landscape | as in B and C |
| 7 | Conduct formal stakeholder review | check motivation and the Statement of Architecture Work; refine only if necessary (ADM §8.3.7) |
| 8 | Finalize the Technology Architecture | standards per block, documentation, traceability, re-use |
| 9 | Create/Update the Architecture Definition Document | technology sections: fundamental functionality and attributes, dependent building blocks, interfaces, mapping to business entities and policies (ADM §8.3.9) |

Step 1 also has a **Select Services** sub-activity: build a non-conflicting portfolio of
services from the taxonomy for each building block and test that it supports the applications
(ADM §8.3.1).

## Outputs

(ADM §8.4)

| Output | Contents |
|---|---|
| Refined Architecture Vision phase deliverables | Statement of Architecture Work; validated or new technology principles |
| Draft Architecture Definition Document | Baseline and Target Technology Architecture: technology components and their relationship to information systems, platforms and their decomposition ("stacks"), environments and locations, expected processing load, physical network communications, hardware and network specifications, views |
| Draft Architecture Requirements Specification | gap analysis results, **requirements output from Phases B and C**, updated technology requirements |
| Technology Architecture components of an Architecture Roadmap | |

<figure class="my-4">
<svg viewBox="0 0 760 288" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="Phase D: its inputs, nine steps and outputs, with the Technology components of the roadmap marked as first produced here">
  <defs><marker id="arr-f4-14" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
  <text x="107.5" y="18" text-anchor="middle" font-size="12" font-weight="bold" fill="#345">Inputs</text><text x="652.5" y="18" text-anchor="middle" font-size="12" font-weight="bold" fill="#345">Outputs</text><text x="380" y="18" text-anchor="middle" font-size="12" font-weight="bold" fill="#345">Steps</text><rect x="235" y="34" width="290" height="220" rx="8" fill="#fff1d6" stroke="#e0b060"/><text x="380" y="52" text-anchor="middle" font-size="12" font-weight="bold">Phase D: Technology Architecture</text><text x="245" y="84" font-size="11">1 Select reference models, viewpoints, tools</text><text x="245" y="99" font-size="11">   (taxonomy of services; select products)</text><text x="245" y="114" font-size="11">2 Develop Baseline Technology Architecture</text><text x="245" y="129" font-size="11">3 Develop Target Technology Architecture</text><text x="245" y="144" font-size="11">4 Perform gap analysis</text><text x="245" y="159" font-size="11">5 Define candidate roadmap components</text><text x="245" y="174" font-size="11">6 Resolve impacts across the Landscape</text><text x="245" y="189" font-size="11">7 Conduct formal stakeholder review</text><text x="245" y="204" font-size="11">8 Finalize the Technology Architecture</text><text x="245" y="219" font-size="11">9 Create/Update Architecture Definition Doc.</text><rect x="10" y="34" width="195" height="46" rx="6" fill="#e0ecff" stroke="#7aa2e3"/><text x="107.5" y="54.5" text-anchor="middle" font-size="10.5">Product information on</text><text x="107.5" y="67.5" text-anchor="middle" font-size="10.5">candidate products (external)</text><line x1="205" y1="57" x2="233" y2="57" stroke="#555" marker-end="url(#arr-f4-14)"/><rect x="10" y="92" width="195" height="46" rx="6" fill="#e0ecff" stroke="#7aa2e3"/><text x="107.5" y="119" text-anchor="middle" font-size="10.5">Technology principles, if existing</text><line x1="205" y1="115" x2="233" y2="115" stroke="#555" marker-end="url(#arr-f4-14)"/><rect x="10" y="150" width="195" height="46" rx="6" fill="#e0ecff" stroke="#7aa2e3"/><text x="107.5" y="164" text-anchor="middle" font-size="10.5">Draft Requirements Specification</text><text x="107.5" y="177" text-anchor="middle" font-size="10.5">with gap results from Business,</text><text x="107.5" y="190" text-anchor="middle" font-size="10.5">Data and Application</text><line x1="205" y1="173" x2="233" y2="173" stroke="#555" marker-end="url(#arr-f4-14)"/><rect x="10" y="208" width="195" height="46" rx="6" fill="#e0ecff" stroke="#7aa2e3"/><text x="107.5" y="228.5" text-anchor="middle" font-size="10.5">Business, Data and Application</text><text x="107.5" y="241.5" text-anchor="middle" font-size="10.5">components of the Roadmap</text><line x1="205" y1="231" x2="233" y2="231" stroke="#555" marker-end="url(#arr-f4-14)"/><rect x="555" y="34" width="195" height="46" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/><text x="652.5" y="54.5" text-anchor="middle" font-size="10.5">Validated or new</text><text x="652.5" y="67.5" text-anchor="middle" font-size="10.5">technology principles</text><line x1="525" y1="57" x2="553" y2="57" stroke="#555" marker-end="url(#arr-f4-14)"/><rect x="555" y="92" width="195" height="46" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/><text x="652.5" y="112.5" text-anchor="middle" font-size="10.5">Draft Architecture Definition Doc.:</text><text x="652.5" y="125.5" text-anchor="middle" font-size="10.5">Baseline and Target Technology</text><line x1="525" y1="115" x2="553" y2="115" stroke="#555" marker-end="url(#arr-f4-14)"/><rect x="555" y="150" width="195" height="46" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/><text x="652.5" y="164" text-anchor="middle" font-size="10.5">Draft Requirements Specification:</text><text x="652.5" y="177" text-anchor="middle" font-size="10.5">gap results plus requirements</text><text x="652.5" y="190" text-anchor="middle" font-size="10.5">output from Phases B and C</text><line x1="525" y1="173" x2="553" y2="173" stroke="#555" marker-end="url(#arr-f4-14)"/><rect x="555" y="208" width="195" height="46" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/><text x="652.5" y="228.5" text-anchor="middle" font-size="10.5">Technology Architecture components</text><text x="652.5" y="241.5" text-anchor="middle" font-size="10.5">of an Architecture Roadmap</text><rect x="711" y="200" width="35" height="15" rx="7" fill="#f3e3f7" stroke="#b58ac9"/><text x="728.5" y="211" text-anchor="middle" font-size="9.5" fill="#5b2d6e">first</text><line x1="525" y1="231" x2="553" y2="231" stroke="#555" marker-end="url(#arr-f4-14)"/><text x="380" y="272" text-anchor="middle" font-size="11" fill="#666">D is the only development phase whose external inputs name product information (ADM §8.2)</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">Inputs, steps and outputs of Phase D. Original drawing; inputs and outputs per ADM §8.2 and ADM §8.4, steps per ADM §8.3.</figcaption>
</figure>

> **Trap.** Distractors for Phase D borrow from the *Architecture Repository* and from *Phase E*.
> The Technology Standards Catalog and Technology Portfolio Catalog are Phase D artifacts; the
> Standards Library is a repository part. Product selection may start in D, but consolidating
> gaps and defining Solution Building Blocks are Phase E work.

> **Trap.** "Which phase's Architecture Requirements Specification carries the requirements output
> from Phases B and C?" — Phase D. It is the last development phase, so its specification
> accumulates everything before Phase E consolidates.

## Check yourself

1. What does the Phase D objective say the Target Technology Architecture enables?
2. Which input group names product information, and in which other phase does product information reappear?
3. What four technology-service qualities are affected by decisions on service granularity?
4. Where does a product selection go if it deviates from existing standards?
