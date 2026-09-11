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

## Check yourself

- Name the two continua inside the Enterprise Continuum and the four stages each runs through.
- Which repository class holds the SBBs that have been planned or deployed?
- Which Landscape level is used at programme or portfolio level?
- Which domain architecture of the EA practice defines the structure of the repository?
