---
title: The reference-model guides, the Government Reference Model, microservices and selecting building blocks
unit: G_REFERENCE_MODELS
objectives: ["G8.1"]
refs: ["GUIDE:government-reference-model §1", "GUIDE:government-reference-model §1.2", "GUIDE:government-reference-model §1.3", "GUIDE:government-reference-model §1.4", "GUIDE:government-reference-model §13", "GUIDE:microservices-architecture §2", "GUIDE:microservices-architecture §3.1", "GUIDE:microservices-architecture §4", "GUIDE:microservices-architecture §5", "GUIDE:microservices-architecture §5.1", "GUIDE:microservices-architecture §5.2", "GUIDE:microservices-architecture §5.3", "GUIDE:microservices-architecture §10.3", "GUIDE:microservices-architecture §11.2", "GUIDE:microservices-architecture §12.2", "GUIDE:microservices-architecture §13", "GUIDE:microservices-architecture §14", "GUIDE:selecting-building-blocks §2", "GUIDE:selecting-building-blocks §3", "GUIDE:selecting-building-blocks §3.1", "GUIDE:selecting-building-blocks §4", "GUIDE:selecting-building-blocks §5", "GUIDE:selecting-building-blocks §9", "CONTENT §7.3"]
reading_minutes: 11
source: authored
status: draft
---
## What "reference model" means in this unit

A reference model is a pre-built, reusable description that an architecture engagement can
adopt, extend or customise instead of starting from a blank page; the Architecture
Repository's Reference Library is where such models are kept (CONTENT §7.3). Three Series
Guides in the source store fit here: the Government Reference Model, a Business Architecture
taxonomy for the public sector; Microservices Architecture, an architecture style described
phase by phase; and An Approach to Selecting Building Blocks, a way of configuring the
metamodel entities to the profile of a change. The Technical Reference Model, the III-RM and
the SOA guide named in the unit title are not in this app's source store, so this lesson covers
what is grounded and flags that gap.

| Cue | Guide | What it gives you |
|---|---|---|
| a government department, "we need a common language across agencies" | Government Reference Model | eleven sectors with functions and services, drivers for change, used in Phase B |
| "break up the monolith", DevOps squads, polyglot, cloud-native | Microservices Architecture | MSA principles adopted in the Preliminary Phase, federated governance, phase-by-phase considerations |
| "how much architecture does this change need?" | Selecting Building Blocks | Rapid, Functional and Robust change profiles, each with its own set of metamodel entities and checklists |

## The Government Reference Model

The GRM gives public sector organisations a common way to view themselves in order to plan and
execute transformational change, responding to inconsistent application of architecture
standards across governments (GUIDE:government-reference-model §1). It categorises and
segments operational departments so an architecture function can determine the impact of
change and map dependencies between architecture layers; it can be used out of the box,
extended or customised (GUIDE:government-reference-model §1.2). It is an exhaustive, mutually
exclusive taxonomy in three levels, sectors, functions and services, plus drivers for change
per sector; the sectors are International Affairs and Trade, Defense and Security, General
Government and Local Services, Young People and Education, Health and Community Wellbeing,
Judiciary, Justice and Home Affairs, Financial, Growth, Housing and Environment, Policy,
Performance, Population and Innovation, Shared Services, and Transport and Operations
(GUIDE:government-reference-model §1.3). Its intended home is Phase B, as a reference and a
pattern for accelerating the development of a business reference model
(GUIDE:government-reference-model §1.4), and its purpose is Business Architecture assets that
help decision-makers resolve problems, manage change and plan
(GUIDE:government-reference-model §13).

**Trap.** The GRM is a *business* taxonomy for Phase B, not a technology reference model. An
answer that uses it to structure the Technology Architecture has the wrong domain
(GUIDE:government-reference-model §1.4).

## Microservices Architecture

MSA is an architecture style, not a product or platform: systems composed of independent,
self-contained services, each implementing an atomic business function; its three key
characteristics are service independence, single responsibility and self-containment, and its
benefits include technology independence, re-use, deployment flexibility, flexible scaling and
decoupling (GUIDE:microservices-architecture §2). In a distributed world the Enterprise
Architecture's mandate is congruency of capabilities and standards across modular solutions
while allowing each its polyglot independence: standardised API contracts, a reference
architecture for interoperability, visibility, operations and security, enterprise standards
each unit inherits and extends, and a federated rather than centralised governance model
(GUIDE:microservices-architecture §3.1). The guide covers only the microservices layer, so a
subset of the ADM applies (GUIDE:microservices-architecture §4).

The Preliminary Phase does the heavy lifting: the team adopts the MSA principles as
architecture principles, even if the enterprise is already service-oriented, and this affects
the governance and support strategy and the initial repository; cycles for MSA are short,
weeks rather than months (GUIDE:microservices-architecture §5). Service independence is the
principle that distinguishes MSA from SOA, and a project that departs from enterprise
principles needs a waiver from the Architecture Review Board
(GUIDE:microservices-architecture §5.1). Readiness covers SOA maturity via OSIMM, team
organisation, whether one team owns a service for its whole life, and Agile/DevOps methods;
start with a small pilot through a rapid TOGAF cycle and learn
(GUIDE:microservices-architecture §5.2). Governance runs on two parallel tracks, the team's
own decisions inside enterprise guardrails, needs review before releases, least privilege on
pipelines, change monitoring and automation, and is a continuous process rather than a project
(GUIDE:microservices-architecture §5.3).

Later phases add: Phase E's organisational transformation to single-team ownership and lean
federated governance (GUIDE:microservices-architecture §10.3); Phase F's blend of intentional
work packages, environment and team formation, with emergent microservice creation allowed
only where guardrails permit (GUIDE:microservices-architecture §11.2); Phase G governance that
prevents arbitrary technology divergence and keeps a service catalog with provenance,
non-functional expectations and stable addresses (GUIDE:microservices-architecture §12.2); and
Phase H's review of solutions for appropriate and inappropriate use of microservices, the
service catalog, authentication approach and service contracts, with no arbitrary changes to a
service others depend on (GUIDE:microservices-architecture §13). The purpose varies by level:
strategic work decides whether MSA is needed and where, segment work describes its structure,
capability work specifies the services (GUIDE:microservices-architecture §14).

<figure class="my-4">
<svg viewBox="0 0 760 300" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="11" role="img" aria-label="Three reference-model guides: the GRM as a three-level public sector taxonomy placed in Phase B; the microservices guide concentrating Preliminary Phase work on principles, readiness and federated governance; the building-block guide's three change profiles with growing entity sets">
<defs><marker id="arr-g8r" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
<rect x="15" y="15" width="230" height="130" rx="8" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="130" y="36" text-anchor="middle" font-weight="bold">Government Reference Model</text>
<text x="130" y="56" text-anchor="middle">Level 1 sectors (11)</text>
<text x="130" y="72" text-anchor="middle">Level 2 functions</text>
<text x="130" y="88" text-anchor="middle">Level 3 services</text>
<text x="130" y="104" text-anchor="middle">drivers for change per sector</text>
<text x="130" y="128" text-anchor="middle" font-weight="bold">sits in Phase B (§1.4)</text>
<rect x="265" y="15" width="230" height="130" rx="8" fill="#e3f5e1" stroke="#7fbf7a"/>
<text x="380" y="36" text-anchor="middle" font-weight="bold">Microservices Architecture</text>
<text x="380" y="56" text-anchor="middle">Preliminary: MSA principles adopted,</text>
<text x="380" y="72" text-anchor="middle">readiness (OSIMM, teams, DevOps),</text>
<text x="380" y="88" text-anchor="middle">federated governance, repository</text>
<text x="380" y="104" text-anchor="middle">E: single-team ownership  G: service catalog</text>
<text x="380" y="128" text-anchor="middle" font-weight="bold">a subset of the ADM, short cycles (§4, §5)</text>
<rect x="515" y="15" width="230" height="130" rx="8" fill="#fff1d6" stroke="#e0b060"/>
<text x="630" y="36" text-anchor="middle" font-weight="bold">Selecting Building Blocks</text>
<text x="630" y="56" text-anchor="middle">Rapid: fewest entities, SBBs first</text>
<text x="630" y="72" text-anchor="middle">Functional: adds capability, value stream,</text>
<text x="630" y="88" text-anchor="middle">services, process, role, data entity</text>
<text x="630" y="104" text-anchor="middle">Robust: adds contracts, controls, logical components</text>
<text x="630" y="128" text-anchor="middle" font-weight="bold">profile chosen in Phase A (§5)</text>
<g fill="#fff" stroke="#e0b060">
<rect x="530" y="180" width="60" height="70" rx="4"/>
<rect x="600" y="180" width="60" height="70" rx="4"/>
<rect x="670" y="180" width="60" height="70" rx="4"/>
</g>
<rect x="530" y="230" width="60" height="20" fill="#fff1d6"/>
<rect x="600" y="210" width="60" height="40" fill="#fff1d6"/>
<rect x="670" y="185" width="60" height="65" fill="#fff1d6"/>
<text x="560" y="266" text-anchor="middle" font-size="10">Rapid</text>
<text x="630" y="266" text-anchor="middle" font-size="10">Functional</text>
<text x="700" y="266" text-anchor="middle" font-size="10">Robust</text>
<text x="630" y="286" text-anchor="middle" font-size="10" fill="#666">entities considered grow with the profile (§3)</text>
<text x="255" y="200" text-anchor="middle" fill="#666">all three are reusable assets in the Reference Library of the Architecture Repository (CONTENT §7.3);</text>
<text x="255" y="218" text-anchor="middle" fill="#666">each may be used out of the box, extended or customised (GUIDE:government-reference-model §1.2)</text>
<text x="255" y="246" text-anchor="middle" fill="#666">not in the source store: TRM, III-RM, SOA guide; cite the Fundamental Content for those</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">The three guides at a glance. Original drawing; section numbers refer to the respective guides.</figcaption>
</figure>

## Selecting building blocks by change profile

The guide identifies three change profiles reflecting different risk and integrity concerns:
Rapid (short, delivery-driven, near immediate implementation of simple components), Functional
(implementable-capability-driven, fast cycles for bounded functionality, typically agile) and
Robust (risk and architecture-driven, longer-term delivery of complex, riskier, larger-scale
components, often using COBIT, SABSA, PRINCE2 or MSP); most transitions use the functional
profile, all three usually appear in any change of scale, and the right blend of intentional
and emergent architecture is the goal (GUIDE:selecting-building-blocks §2). For each profile
the guide lists the metamodel entities to consider: Rapid stays with location, requirement, work
package, constraint, drivers, goals, objectives, actors, organisation units, courses of action,
business information and the physical components; Functional adds gap, principle, capability,
value stream, business service, service quality, measure, use case or user story, process,
product, role, data entity and application and technology services; Robust adds assumption,
policy and standard, business and operating model, control, contract, event, business function
and the logical components (GUIDE:selecting-building-blocks §3). Rapid change creates SBBs as a
proxy for the specification and lets the running solution "speak for itself"; Robust change
creates ABBs so the proposed architecture speaks for itself before anything is built; whichever
is chosen, the reasons must be documented (GUIDE:selecting-building-blocks §3.1).

The approach uses four abstraction levels, why (context), what (concept), how (logical) and
with what (physical) (GUIDE:selecting-building-blocks §4), and a ten-step table that starts in
Phase H, where the nature of the change is decided, then establishes context and concept in
Phase A including choosing the profile and the KPIs, identifies logical elements in B to D,
activities and solution components in E, contracts and checklists in F, oversees realisation in
G and assures benefits in H (GUIDE:selecting-building-blocks §5). The checklists have two
groups, one for Phases A to F asking whether the right things are being done and one for G and
H asking whether they were done well; each item is marked for the profiles it applies to, so a
Rapid change needs customer needs, KPIs and sign-off while only Robust change needs full logical
data, application and technology specifications and approved detailed plans
(GUIDE:selecting-building-blocks §9).

**Trap.** The profile is chosen per unit of change, not per enterprise; a large change usually
contains all three, and a safety-critical component inside an otherwise agile programme is
Robust (GUIDE:selecting-building-blocks §2).

## How the 5, 3 and 1 differ

| Answer | Why it scores that |
|---|---|
| 5 | Adopts the GRM taxonomy in Phase B and customises it; for microservices, adopts the MSA principles and federated governance in the Preliminary Phase, assesses readiness and pilots; for the building-block question, chooses the change profile in Phase A, selects the matching entities and checklists, and documents why |
| 3 | Right guide, wrong phase or scope: GRM used for technology, MSA principles introduced during Phase D, one profile applied to every unit of change |
| 1 | Treats a reference model as mandatory rather than adoptable, extendable or customisable, or treats MSA as a product to procure (GUIDE:government-reference-model §1.2, GUIDE:microservices-architecture §2) |
| 0 | Ignores the reference models and starts from a blank page, or lets each squad choose its own standards without enterprise guardrails (GUIDE:microservices-architecture §3.1) |

## Where to look in the book

Government Reference Model: §1.3 the taxonomy and sectors, §1.4 the Phase B placement, §13
the purpose. Microservices Architecture: §2 definition, §3.1 EA in a distributed world, §5
Preliminary Phase, §10 to §13 later phases, §14 summary. Selecting Building Blocks: §2 profiles,
§3 entities per profile, §4 abstraction levels, §5 the ten steps, §9 checklists. Architecture
Content §7.3 for the Reference Library.

## Check yourself

- Which ADM phase does the GRM guide say it sits in?
- Name the three key characteristics of a microservice.
- Which entities does the Functional profile add to the Rapid set?
