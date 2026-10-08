---
title: The Enterprise Continuum, the Architecture Repository and the EA Capability, in outline
unit: F1
objectives: ["1.5"]
refs: ["INTRO §3.10", "INTRO §3.10.1", "INTRO §3.12", "INTRO §3.13", "CONTENT §6.1", "CONTENT §6.3", "CONTENT §6.4.1", "CONTENT §6.4.2", "CONTENT §7.1", "CONTENT §7.2", "GOV §2.1", "GOV §2.4"]
reading_minutes: 9
source: authored
status: draft
---
## The Enterprise Continuum: a way of classifying

The Enterprise Continuum is the standard's answer to "where does this asset sit between
generic and specific?". It is a categorisation for the assets held in the enterprise's
repositories, classifying architecture and solution artifacts as they evolve from generic
**Foundation Architectures** towards **Organization-Specific Architectures**. It has two
complementary parts, the **Architecture Continuum** and the **Solutions Continuum** (INTRO §3.10).

Its value is communication. Architectures are always context-specific, and people discussing
"the architecture" often talk past each other because they are pointing at different points on
the continuum without noticing; a consistent language for those differences is what the continuum
supplies, on both the buy side and the supply side (CONTENT §6.1). It also organises reusable
assets so the investment in architecture pays back (CONTENT §6.1).

The Architecture Content document describes it as three nested continua (CONTENT §6.3):

| Continuum | What it classifies |
|---|---|
| **Enterprise Continuum** (outermost) | contextual assets that influence architectures but are not used directly in ADM development: policies, standards, strategic initiatives, organisational structures, enterprise-level capabilities; it can also classify solutions, and it contains the two specialisations below |
| **Architecture Continuum** | Architecture Building Blocks: the generic rules, representations and relationships, including traceability from an organisation-specific architecture back to an industry or generic standard; used to guide selection in the Solutions Continuum; a tool for finding commonality and removing redundancy |
| **Solutions Continuum** | the implementation of what the Architecture Continuum defines: the reusable SBBs available in the organisation, the products, systems and services of implemented systems |

## Four stages on each continuum

Both continua run left to right through the same four stages, with detail and specificity
increasing to the right and reusable material more likely to be found on the left
(CONTENT §6.4.1, CONTENT §6.4.2).

| Stage | Architecture Continuum | Solutions Continuum |
|---|---|---|
| Foundation | generic components, relationships, principles and guidelines that more specific architectures build on; the TOGAF TRM is the example | highly generic tools, products and services: programming languages, operating systems, ITIL or IT4IT as ways of organising IT operations |
| Common Systems | selects and integrates Foundation services into an architecture for common, highly reusable solutions across many domains; each is complete for one problem domain (security, management, network, operations) but incomplete as a whole system; the III-RM is the example | an implementation of a Common Systems Architecture as a set of products and services, e.g. an enterprise management or security product; vendors and SaaS providers typically supply these |
| Industry | integrates common systems components with industry-specific ones; carries industry data and process models, business rules, testing guidelines | an implementation of an Industry Architecture: reusable packages specific to an industry, such as an industry point-of-service device or physical schema |
| Organization-Specific | describes and guides final deployment for one enterprise or connected network of enterprises; may be several, at increasing detail or per entity | an implementation of the Organization-Specific Architecture; the most unique content, structured to support specific SLAs |

The four types are illustrative points, not fixed process stages; other architecture types can sit
between them. The progression runs at several levels at once: logical to physical, horizontal
(IT-focused) to vertical (business-focused), generalisation to specialisation, and taxonomy to a
complete, specific specification (CONTENT §6.4.1). On the Solutions Continuum, moving right is
about providing solution value and moving left is about addressing enterprise needs
(CONTENT §6.4.2).

> **Trap.** The TRM is a Foundation Architecture; the III-RM is a Common Systems Architecture
> (in the Application domain, about Boundaryless Information Flow). Swapping them is a common
> distractor (CONTENT §6.4.1).

<figure class="my-4">
<svg viewBox="0 0 760 330" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="The Architecture and Solutions Continua running Foundation, Common Systems, Industry, Organization-Specific, beside the repository parts they classify">
  <defs><marker id="arr-f1-13a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
  <rect x="10" y="10" width="525" height="290" rx="8" fill="#f4f4f4" stroke="#bbb" stroke-dasharray="6 4"/>
  <text x="272.5" y="28" text-anchor="middle" font-size="12" font-weight="bold">Enterprise Continuum: classifies, generic on the left to specific on the right</text>
  <rect x="25" y="45" width="495" height="105" rx="8" fill="#e0ecff" stroke="#7aa2e3"/>
  <text x="272.5" y="63" text-anchor="middle" font-size="12" font-weight="bold">Architecture Continuum (ABBs)</text>
  <rect x="35" y="72" width="112" height="50" rx="6" fill="#fff" stroke="#666"/>
  <text x="91" y="94.35" text-anchor="middle" font-size="11" font-weight="bold">Foundation</text>
  <text x="91" y="107.35" text-anchor="middle" font-size="11" fill="#345">e.g. the TRM</text>
  <line x1="147" y1="97" x2="157" y2="97" stroke="#555" marker-end="url(#arr-f1-13a)"/>
  <rect x="157" y="72" width="112" height="50" rx="6" fill="#fff" stroke="#666"/>
  <text x="213" y="94.35" text-anchor="middle" font-size="11" font-weight="bold">Common Systems</text>
  <text x="213" y="107.35" text-anchor="middle" font-size="11" fill="#345">e.g. the III-RM</text>
  <line x1="269" y1="97" x2="279" y2="97" stroke="#555" marker-end="url(#arr-f1-13a)"/>
  <rect x="279" y="72" width="112" height="50" rx="6" fill="#fff" stroke="#666"/>
  <text x="335" y="87.85" text-anchor="middle" font-size="11" font-weight="bold">Industry</text>
  <text x="335" y="100.85" text-anchor="middle" font-size="11" fill="#345">industry models,</text>
  <text x="335" y="113.85" text-anchor="middle" font-size="11" fill="#345">business rules</text>
  <line x1="391" y1="97" x2="401" y2="97" stroke="#555" marker-end="url(#arr-f1-13a)"/>
  <rect x="401" y="72" width="112" height="50" rx="6" fill="#fff" stroke="#666"/>
  <text x="457" y="87.85" text-anchor="middle" font-size="11" font-weight="bold">Organization-</text>
  <text x="457" y="100.85" text-anchor="middle" font-size="11" fill="#345">Specific</text>
  <text x="457" y="113.85" text-anchor="middle" font-size="11" fill="#345">one enterprise</text>
  <text x="272" y="140" text-anchor="middle" font-size="11" fill="#345">more reusable on the left; more detail and specificity on the right</text>
  <rect x="25" y="170" width="495" height="105" rx="8" fill="#e3f5e1" stroke="#7fbf7a"/>
  <text x="272.5" y="188" text-anchor="middle" font-size="12" font-weight="bold">Solutions Continuum (SBBs)</text>
  <rect x="35" y="197" width="112" height="50" rx="6" fill="#fff" stroke="#666"/>
  <text x="91" y="212.85" text-anchor="middle" font-size="11" font-weight="bold">Foundation</text>
  <text x="91" y="225.85" text-anchor="middle" font-size="11" fill="#345">Solutions</text>
  <text x="91" y="238.85" text-anchor="middle" font-size="11" fill="#345">languages, OS, ITIL</text>
  <line x1="147" y1="222" x2="157" y2="222" stroke="#555" marker-end="url(#arr-f1-13a)"/>
  <rect x="157" y="197" width="112" height="50" rx="6" fill="#fff" stroke="#666"/>
  <text x="213" y="212.85" text-anchor="middle" font-size="11" font-weight="bold">Common Systems</text>
  <text x="213" y="225.85" text-anchor="middle" font-size="11" fill="#345">Solutions</text>
  <text x="213" y="238.85" text-anchor="middle" font-size="11" fill="#345">e.g. a security product</text>
  <line x1="269" y1="222" x2="279" y2="222" stroke="#555" marker-end="url(#arr-f1-13a)"/>
  <rect x="279" y="197" width="112" height="50" rx="6" fill="#fff" stroke="#666"/>
  <text x="335" y="212.85" text-anchor="middle" font-size="11" font-weight="bold">Industry</text>
  <text x="335" y="225.85" text-anchor="middle" font-size="11" fill="#345">Solutions</text>
  <text x="335" y="238.85" text-anchor="middle" font-size="11" fill="#345">e.g. a POS device</text>
  <line x1="391" y1="222" x2="401" y2="222" stroke="#555" marker-end="url(#arr-f1-13a)"/>
  <rect x="401" y="197" width="112" height="50" rx="6" fill="#fff" stroke="#666"/>
  <text x="457" y="212.85" text-anchor="middle" font-size="11" font-weight="bold">Organization-</text>
  <text x="457" y="225.85" text-anchor="middle" font-size="11" fill="#345">Specific Solutions</text>
  <text x="457" y="238.85" text-anchor="middle" font-size="11" fill="#345">built to its SLAs</text>
  <text x="272" y="265" text-anchor="middle" font-size="11" fill="#345">each stage implements the architecture stage above it</text>
  <line x1="272" y1="152" x2="272" y2="168" stroke="#555" marker-end="url(#arr-f1-13a)"/>
  <text x="285" y="163" text-anchor="start" font-size="10" fill="#666">guides selection</text>
  <rect x="555" y="10" width="195" height="290" rx="8" fill="#fff1d6" stroke="#e0b060"/>
  <text x="652.5" y="28" text-anchor="middle" font-size="12" font-weight="bold">Architecture Repository: stores</text>
  <rect x="568" y="45" width="170" height="56" rx="6" fill="#fff" stroke="#666"/>
  <text x="653" y="63.85" text-anchor="middle" font-size="11" font-weight="bold">Reference Library</text>
  <text x="653" y="76.85" text-anchor="middle" font-size="11" fill="#345">may use the Architecture</text>
  <text x="653" y="89.85" text-anchor="middle" font-size="11" fill="#345">Continuum as its scheme</text>
  <rect x="568" y="115" width="170" height="50" rx="6" fill="#fff" stroke="#666"/>
  <text x="653" y="136.85" text-anchor="middle" font-size="11" font-weight="bold">Architecture Landscape</text>
  <text x="653" y="150.85" text-anchor="middle" font-size="11" fill="#345">ABBs in use or planned</text>
  <rect x="568" y="180" width="170" height="50" rx="6" fill="#fff" stroke="#666"/>
  <text x="653" y="201.85" text-anchor="middle" font-size="11" font-weight="bold">Solutions Landscape</text>
  <text x="653" y="215.85" text-anchor="middle" font-size="11" fill="#345">SBBs planned or deployed</text>
  <rect x="568" y="245" width="170" height="40" rx="6" fill="#fff" stroke="#666"/>
  <text x="653" y="261.85" text-anchor="middle" font-size="11" font-weight="bold">Standards Library</text>
  <text x="653" y="275.85" text-anchor="middle" font-size="11" fill="#345">what new work must meet</text>
  <line x1="520" y1="97" x2="566" y2="73" stroke="#555" stroke-dasharray="5 4" marker-end="url(#arr-f1-13a)"/>
  <line x1="520" y1="110" x2="566" y2="138" stroke="#555" stroke-dasharray="5 4" marker-end="url(#arr-f1-13a)"/>
  <line x1="520" y1="222" x2="566" y2="205" stroke="#555" stroke-dasharray="5 4" marker-end="url(#arr-f1-13a)"/>
  <text x="380" y="318" text-anchor="middle" font-size="11" fill="#666">the continuum classifies; the repository stores. Reference and Standards Libraries are repository parts, not continuum stages</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">The two continua and their four stages, beside the repository parts that hold what they classify. Original drawing; the stages follow CONTENT §6.3, CONTENT §6.4.1 and CONTENT §6.4.2.</figcaption>
</figure>

## The Architecture Repository: where assets are stored

Supporting the continuum is the Architecture Repository, which stores the different classes of
architectural output, at different levels of abstraction, that the ADM produces. Through the two
together, architects are pushed to reuse every relevant asset when building an organisation-specific
architecture; the ADM can be seen as a lifecycle process operating at several levels inside a
governance framework and producing aligned outputs that live in the repository (INTRO §3.10.1).

The repository is one part of the wider **Enterprise Repository**, which also links architecture
assets to detailed design, deployment and service management repositories (CONTENT §7.1). Its
eight classes of content (INTRO §3.10.1, CONTENT §7.1):

| Class | Holds |
|---|---|
| **Architecture Metamodel** | the organisation's tailored application of the framework, including the content metamodel (and, per CONTENT, the method) |
| **Architecture Capability** | the parameters, structures and processes that support governance of the repository |
| **Architecture Landscape** | the architectural representation of assets in use, or planned, at particular points in time, at several levels of abstraction |
| **Standards Library** | the standards new architectures must comply with: industry standards, selected supplier products and services, shared services already deployed |
| **Reference Library** | guidelines, templates, patterns and other reference material to accelerate new architectures |
| **Governance Repository** | the record of governance activity across the enterprise |
| **Architecture Requirements Repository** | all authorised architecture requirements agreed with the Architecture Board |
| **Solutions Landscape** | the SBBs, planned or deployed, that support the Architecture Landscape |

The Architecture Landscape is split into three levels of granularity to cope with volume and
varied stakeholders: **Strategic Architectures** give a long-term summary of the whole enterprise
for executive direction-setting; **Segment Architectures** give more detailed operating models for
areas, used at programme or portfolio level; **Capability Architectures** show in detail how one
unit of capability is supported, including current, target and capability increments, so that
work packages and projects can be grouped into portfolios and programmes (CONTENT §7.2).

<figure class="my-4">
<svg viewBox="0 0 760 250" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="The eight content classes of the Architecture Repository, with the Architecture Landscape broken into strategic, segment and capability levels">
  <defs><marker id="arr-f1-13b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
  <rect x="10" y="10" width="740" height="230" rx="8" fill="#fff1d6" stroke="#e0b060"/>
  <text x="380.0" y="28" text-anchor="middle" font-size="12" font-weight="bold">Architecture Repository: eight classes of content</text>
  <rect x="25" y="40" width="170" height="48" rx="6" fill="#fff" stroke="#666"/>
  <text x="110" y="61.35" text-anchor="middle" font-size="11" font-weight="bold">Architecture Metamodel</text>
  <text x="110" y="74.35" text-anchor="middle" font-size="11" fill="#345">tailored framework, metamodel</text>
  <rect x="205" y="40" width="170" height="48" rx="6" fill="#fff" stroke="#666"/>
  <text x="290" y="61.35" text-anchor="middle" font-size="11" font-weight="bold">Architecture Capability</text>
  <text x="290" y="74.35" text-anchor="middle" font-size="11" fill="#345">governance of the repository</text>
  <rect x="385" y="40" width="170" height="48" rx="6" fill="#fff" stroke="#666"/>
  <text x="470" y="61.35" text-anchor="middle" font-size="11" font-weight="bold">Standards Library</text>
  <text x="470" y="74.35" text-anchor="middle" font-size="11" fill="#345">what new work must meet</text>
  <rect x="565" y="40" width="170" height="48" rx="6" fill="#fff" stroke="#666"/>
  <text x="650" y="61.35" text-anchor="middle" font-size="11" font-weight="bold">Reference Library</text>
  <text x="650" y="74.35" text-anchor="middle" font-size="11" fill="#345">guidelines, templates, patterns</text>
  <rect x="25" y="98" width="170" height="48" rx="6" fill="#fff" stroke="#666"/>
  <text x="110" y="119.35" text-anchor="middle" font-size="11" font-weight="bold">Governance Repository</text>
  <text x="110" y="132.35" text-anchor="middle" font-size="11" fill="#345">record of governance activity</text>
  <rect x="205" y="98" width="170" height="48" rx="6" fill="#fff" stroke="#666"/>
  <text x="290" y="119.35" text-anchor="middle" font-size="11" font-weight="bold">Requirements Repository</text>
  <text x="290" y="132.35" text-anchor="middle" font-size="11" fill="#345">all authorised requirements</text>
  <rect x="385" y="98" width="170" height="48" rx="6" fill="#fff" stroke="#666"/>
  <text x="470" y="119.35" text-anchor="middle" font-size="11" font-weight="bold">Architecture Landscape</text>
  <text x="470" y="132.35" text-anchor="middle" font-size="11" fill="#345">assets in use or planned</text>
  <rect x="565" y="98" width="170" height="48" rx="6" fill="#fff" stroke="#666"/>
  <text x="650" y="119.35" text-anchor="middle" font-size="11" font-weight="bold">Solutions Landscape</text>
  <text x="650" y="132.35" text-anchor="middle" font-size="11" fill="#345">SBBs planned or deployed</text>
  <rect x="205" y="175" width="170" height="52" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
  <text x="290" y="191.85" text-anchor="middle" font-size="11" font-weight="bold">Strategic</text>
  <text x="290" y="204.85" text-anchor="middle" font-size="11" fill="#345">whole enterprise, long-term;</text>
  <text x="290" y="217.85" text-anchor="middle" font-size="11" fill="#345">executive direction-setting</text>
  <rect x="385" y="175" width="170" height="52" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
  <text x="470" y="191.85" text-anchor="middle" font-size="11" font-weight="bold">Segment</text>
  <text x="470" y="204.85" text-anchor="middle" font-size="11" fill="#345">areas as operating models;</text>
  <text x="470" y="217.85" text-anchor="middle" font-size="11" fill="#345">programme or portfolio level</text>
  <rect x="565" y="175" width="170" height="52" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
  <text x="650" y="191.85" text-anchor="middle" font-size="11" font-weight="bold">Capability</text>
  <text x="650" y="204.85" text-anchor="middle" font-size="11" fill="#345">one unit of capability, with</text>
  <text x="650" y="217.85" text-anchor="middle" font-size="11" fill="#345">current, target and increments</text>
  <path d="M470 146 L470 150 L290 150 L290 173" fill="none" stroke="#555" marker-end="url(#arr-f1-13b)"/>
  <path d="M470 150 L470 173" fill="none" stroke="#555" marker-end="url(#arr-f1-13b)"/>
  <path d="M470 150 L650 150 L650 173" fill="none" stroke="#555" marker-end="url(#arr-f1-13b)"/>
  <text x="470" y="165" text-anchor="middle" font-size="10" fill="#666">the Landscape is split into three levels of granularity</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">The repository's eight classes and the three Landscape levels. Original drawing; the classes follow CONTENT §7.1 and the levels CONTENT §7.2.</figcaption>
</figure>

> **Trap.** Continuum versus repository. The continuum *classifies*; the repository *stores*.
> Reference Library and Standards Library are parts of the repository, not of the continuum, though
> the Reference Library can use the Architecture Continuum as its classification scheme.

## The Enterprise Architecture Capability

Doing architecture well needs a business capability for architecture: organisation structures,
roles, responsibilities, skills and processes (INTRO §3.12). The standard's stronger claim is that
an EA practice must be run like any other operational unit, that is, like a business. Beyond the
ADM's own processes it should build capabilities in ten areas: financial, performance, service,
risk and opportunity, resource, communications and stakeholder, quality, supplier, configuration
and environment management (INTRO §3.13).

Governance is central to running an ongoing architecture: all architecturally significant activity
is controlled and aligned within one framework. The benefits listed for Architecture Governance
include clearer accountability and delegated authority, proactive risk and opportunity management,
protecting the asset base through reuse, proactive control and monitoring, reuse across business
units, value creation through measurement and feedback, visibility of decisions at lower levels so
they get oversight at the right level, greater shareholder value, and integration with existing
processes by adding control (INTRO §3.13).

The EA Capability and Governance document shows how to *establish* the capability by running the
ADM with an Architecture Vision aimed at the practice itself. Establishing the practice is an
ongoing discipline, not a phase of a project or a one-off; a later project may request a change
to the practice, which triggers another ADM cycle (GOV §2.1). Like any capability it needs all
four domain architectures: a Business Architecture of the practice (governance, processes,
organisation, products), a Data Architecture defining the structure of the Enterprise Continuum
and Architecture Repository, an Application Architecture of the tooling, and a Technology
Architecture for its infrastructure (GOV §2.1). That Data Architecture is sometimes called the
metamodel of the practice (GOV §2.4).

<!-- figures:start -->
## Figures from the standard

The diagrams the cited sections carry, from your local copy of the publication. The exam reproduces these; know what each box is.

<div class="grid gap-4 md:grid-cols-2">
<figure class="max-w-lg"><img src="/figure/CONTENT:fig-6-1" alt="Figure 6-1: Enterprise Continuum" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 6-1: Enterprise Continuum (CONTENT)</figcaption></figure>
<figure class="max-w-lg"><img src="/figure/CONTENT:fig-6-2" alt="Figure 6-2: Architecture Continuum" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 6-2: Architecture Continuum (CONTENT)</figcaption></figure>
<figure class="max-w-lg"><img src="/figure/CONTENT:fig-6-3" alt="Figure 6-3: Solutions Continuum" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 6-3: Solutions Continuum (CONTENT)</figcaption></figure>
<figure class="max-w-lg"><img src="/figure/CONTENT:fig-7-1" alt="Figure 7-1: Overview of Architecture Repository" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 7-1: Overview of Architecture Repository (CONTENT)</figcaption></figure>
<figure class="max-w-lg"><img src="/figure/INTRO:fig-3-4" alt="Figure 3-4: Enterprise Continuum" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 3-4: Enterprise Continuum (INTRO)</figcaption></figure>
<figure class="max-w-lg"><img src="/figure/INTRO:fig-3-5" alt="Figure 3-5: TOGAF Architecture Repository Structure" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 3-5: TOGAF Architecture Repository Structure (INTRO)</figcaption></figure>
<figure class="max-w-lg"><img src="/figure/INTRO:fig-3-9" alt="Figure 3-9: TOGAF Architecture Capability Overview" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 3-9: TOGAF Architecture Capability Overview (INTRO)</figcaption></figure>
</div>
<!-- figures:end -->

## Check yourself

- Name the two continua inside the Enterprise Continuum and the four stages each runs through.
- Which repository class holds the SBBs that have been planned or deployed?
- Which Landscape level is used at programme or portfolio level?
- Which domain architecture of the EA practice defines the structure of the repository?
