---
title: How the ADM uses the Enterprise Continuum and the Architecture Repository
unit: F3
objectives: ["3.3"]
refs: ["ADM §1.1.1", "ADM §1.1.2", "ADM §1.1.3", "ADM §1.4", "ADM §1.8", "CONTENT §6.2", "CONTENT §6.5", "CONTENT §6.6.2", "CONTENT §7.1", "CONTENT §7.2", "CONTENT §7.3.1", "CONTENT §7.6.1", "CONTENT §7.7"]
reading_minutes: 8
source: authored
status: draft
---
## The continuum as context, the repository as its implementation

The Enterprise Continuum gives the ADM a framework and context for leveraging relevant assets:
architecture descriptions, models and patterns from many sources. It categorises architectural
source material of two kinds, the organisation's own repository contents and the reference models
and standards available in the industry (ADM §1.1.1).

Its practical implementation is the **Architecture Repository**: reference architectures, models
and patterns accepted for use in the enterprise, plus the enterprise's own earlier architecture
work, plus work in progress. The architect should reuse as much relevant material from it as
possible (ADM §1.1.1). Throughout the ADM there are reminders to check which repository assets to
use; for a Technology Architecture that might be the TOGAF Foundation Architecture, for a Business
Architecture an industry e-commerce reference model (ADM §1.1.1).

Which source materials get into the repository is a matter for Architecture Governance, which
should weigh resources inside and outside the enterprise, deciding when generic material can be
adapted for the enterprise and when specific solutions can be generalised for wider reuse
(ADM §1.1.1).

## Each iteration populates the repository

Using the ADM, the architect builds a snapshot of the enterprise's decisions and their implications
at a point in time. Each iteration fills an organisation-specific landscape with the assets it
identified and used, including the final organisation-specific architecture (ADM §1.1.1).
Architecture development is continuous and cyclical, so repeated ADM cycles add more and more
content to the repository; seen this way, the ADM is also the process of populating the
enterprise's own repository with reusable building blocks drawn from the "left", more generic side
of the continuum (ADM §1.1.1).

> **Trap.** The **first** execution of the ADM is usually the hardest, because there is little to
> reuse; even then, external assets such as the standard itself and industry material are
> available. Later executions get easier as the repository fills (ADM §1.1.1). A question about
> which cycle benefits *least* from the repository wants the first.

The ADM can also be used to populate an enterprise's **Foundation Architecture**: business
requirements identify the definitions and selections needed, from reusable common models and
policy definitions to specific technology choices mandated by law. The same principles apply as
for an enterprise architecture, except that enterprise-wide requirements are restricted to overall
concerns and so are less complete. Integrating models from many sources does not automatically
give a coherent enterprise architecture (ADM §1.1.2).

The chapter summary makes the same point from the scoping side: each iteration adds resources to
the repository, and future iterations build on what the current one creates, adding width and
depth (ADM §1.8).

## Guidelines and techniques that support the ADM

The ADM is supported by an extended set of resources: the ADM Techniques document; the TOGAF
Series Guides, the guidance part of the standard on how to use and adapt it; and White Papers and
Guides in the TOGAF Library. They are kept separate so they can be referenced from the relevant
points of the ADM without cluttering the method's description (ADM §1.1.3).

## Governance material lives in the repository too

The ADM itself is managed like any other artifact classified through the continuum and held in the
repository, and the governance artifacts and processes, reference data, process status and audit
information, are part of the repository's contents (ADM §1.4).

## The continuum's view of the ADM

From the Architecture Content side, the ADM is the process of developing an enterprise-specific
architecture and solutions by adopting and adapting generic architectures and solutions, which is
movement from *left to right* on the continuum. In the other direction, specific architectures and
solutions that prove credible are generalised for reuse, *right to left* (CONTENT §6.5). The ADM
contains pointers to useful assets at the appropriate level of generality, including Open Group and
industry reference models, and the TOGAF Library supplies reference models to consider
(CONTENT §6.5).

The simplest way to think of the continuum is as a view of the repository of all architecture
assets, inside and outside the enterprise, that the enterprise considers available: descriptions,
models, building blocks, patterns, viewpoints. Internal examples are deliverables of previous work;
external ones are industry reference models and patterns, from the very generic TRM to
vertical-industry models from bodies such as the TM Forum. The enterprise architecture decides
which assets go into the repository, with reuse a major consideration (CONTENT §6.2). An
enterprise is advised to have its own Foundation Architecture governing all systems, Common Systems
Architectures for shared systems such as networking, possibly industry architectures, and
Organization-Specific Architectures per department; the ADM helps generate and maintain any of
them while leveraging existing assets (CONTENT §6.6.2).

## The repository areas the ADM reads and writes

A mature capability produces a huge volume of output, so the repository needs a formal taxonomy of
asset types and dedicated processes and tools. It is one part of the wider Enterprise Repository,
which links architecture assets to detailed design, deployment and service management repositories
(CONTENT §7.1). Its eight areas are the Architecture Metamodel, Architecture Capability,
Architecture Landscape, Standards Library, Reference Library, Governance Repository, Architecture
Requirements Repository and Solutions Landscape (CONTENT §7.1).

Three of them interact with the ADM most directly:

- The **Architecture Landscape** holds views of the enterprise at points in time at three levels,
  strategic, segment and capability, which is what each ADM cycle extends or changes
  (CONTENT §7.2).
- The **Reference Library** holds reference architectures, reference models, the viewpoint
  library and templates, sourced from standards bodies, vendors, industry forums and enterprise
  best practice; it can use the Architecture Continuum as its classification scheme, with more
  reusable material toward the left and the requirements for missing elements passed leftward for
  incorporation (CONTENT §7.3.1).
- The **Architecture Requirements Repository** is used by *all* phases to record and manage
  requirements at strategic, segment and capability level; Requirements Management is responsible
  for its contents, their integrity and their availability to every phase (CONTENT §7.6.1).

The **Solutions Landscape** holds the SBBs that support the specified ABBs, categorised by the
continuum and as strategic, segment or capability SBBs; it does not hold the data the solutions
produce (CONTENT §7.7).

## Check yourself

- Which body decides the criteria for admitting source material to the repository?
- Which direction on the continuum is "generalising a proven specific solution for reuse"?
- Which repository area can the Architecture Continuum serve as a classification scheme for?
- Which phase owns the contents of the Architecture Requirements Repository?
