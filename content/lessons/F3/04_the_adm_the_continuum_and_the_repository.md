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

<figure class="my-4">
<svg viewBox="0 0 760 285" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="A triangle: the ADM reads from and writes to the Architecture Repository, moves left to right and right to left along the Enterprise Continuum, and the continuum classifies what the repository stores">
  <defs><marker id="arr-f3-12a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
  <rect x="270" y="15" width="220" height="56" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
  <text x="380" y="33.85" text-anchor="middle" font-size="11" font-weight="bold">The ADM</text>
  <text x="380" y="46.85" text-anchor="middle" font-size="11" fill="#345">every phase of every cycle</text>
  <text x="380" y="59.85" text-anchor="middle" font-size="11" fill="#345">checks what it can reuse</text>
  <rect x="15" y="190" width="300" height="62" rx="6" fill="#fff1d6" stroke="#e0b060"/>
  <text x="165" y="211.85" text-anchor="middle" font-size="11" font-weight="bold">Enterprise Continuum</text>
  <text x="165" y="224.85" text-anchor="middle" font-size="11" fill="#345">classifies: generic on the left,</text>
  <text x="165" y="237.85" text-anchor="middle" font-size="11" fill="#345">organisation-specific on the right</text>
  <rect x="445" y="190" width="300" height="62" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/>
  <text x="595" y="211.85" text-anchor="middle" font-size="11" font-weight="bold">Architecture Repository</text>
  <text x="595" y="224.85" text-anchor="middle" font-size="11" fill="#345">stores: reference models, patterns, standards,</text>
  <text x="595" y="237.85" text-anchor="middle" font-size="11" fill="#345">earlier work, work in progress, the Landscape</text>
  <line x1="455" y1="71" x2="590" y2="188" stroke="#555" marker-end="url(#arr-f3-12a)"/>
  <line x1="575" y1="188" x2="440" y2="71" stroke="#555" marker-end="url(#arr-f3-12a)"/>
  <text x="560" y="118" text-anchor="start" font-size="10" fill="#666">reads assets to reuse</text>
  <text x="560" y="133" text-anchor="start" font-size="10" fill="#666">writes each result back</text>
  <line x1="305" y1="71" x2="170" y2="188" stroke="#555" marker-end="url(#arr-f3-12a)"/>
  <line x1="185" y1="188" x2="320" y2="71" stroke="#555" marker-end="url(#arr-f3-12a)"/>
  <text x="215" y="118" text-anchor="end" font-size="10" fill="#666">adopt and adapt: left to right</text>
  <text x="215" y="133" text-anchor="end" font-size="10" fill="#666">generalise proven work: right to left</text>
  <line x1="315" y1="221" x2="443" y2="221" stroke="#555" stroke-dasharray="5 4" marker-end="url(#arr-f3-12a)"/>
  <text x="380" y="213" text-anchor="middle" font-size="10" fill="#666">classification scheme for</text>
  <text x="380" y="236" text-anchor="middle" font-size="10" fill="#666">what is stored</text>
  <text x="380" y="165" text-anchor="middle" font-size="10" fill="#c0392b">Architecture Governance decides what is admitted to the repository</text>
  <text x="380" y="275" text-anchor="middle" font-size="11" fill="#666">the first cycle has the least to reuse; every later cycle adds to the repository and finds more there</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">Method, classification and store as a triangle. Original drawing; the relationships follow ADM §1.1.1 and CONTENT §6.5.</figcaption>
</figure>

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

<figure class="my-4">
<svg viewBox="0 0 760 250" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="The ADM in the centre exchanging content with the Architecture Landscape, Reference Library, Architecture Requirements Repository and Solutions Landscape">
  <defs><marker id="arr-f3-12b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
  <rect x="290" y="90" width="180" height="70" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
  <text x="380" y="109.35" text-anchor="middle" font-size="11" font-weight="bold">ADM phases</text>
  <text x="380" y="122.35" text-anchor="middle" font-size="11" fill="#345">Preliminary to H, with</text>
  <text x="380" y="135.35" text-anchor="middle" font-size="11" fill="#345">Requirements Management</text>
  <text x="380" y="148.35" text-anchor="middle" font-size="11" fill="#345">at the centre</text>
  <rect x="10" y="15" width="250" height="62" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/>
  <text x="135" y="36.85" text-anchor="middle" font-size="11" font-weight="bold">Architecture Landscape</text>
  <text x="135" y="49.85" text-anchor="middle" font-size="11" fill="#345">strategic, segment, capability views</text>
  <text x="135" y="62.85" text-anchor="middle" font-size="11" fill="#345">at points in time; each cycle extends it</text>
  <rect x="10" y="175" width="250" height="62" rx="6" fill="#fff1d6" stroke="#e0b060"/>
  <text x="135" y="196.5" text-anchor="middle" font-size="10" font-weight="bold">Reference Library</text>
  <text x="135" y="209.5" text-anchor="middle" font-size="10" fill="#345">reference models, viewpoint library,</text>
  <text x="135" y="222.5" text-anchor="middle" font-size="10" fill="#345">templates; classified by the Architecture Continuum</text>
  <rect x="500" y="15" width="250" height="62" rx="6" fill="#f3e3f7" stroke="#b58ac9"/>
  <text x="625" y="36.85" text-anchor="middle" font-size="11" font-weight="bold">Architecture Requirements Repository</text>
  <text x="625" y="49.85" text-anchor="middle" font-size="11" fill="#345">used by all phases; its contents owned</text>
  <text x="625" y="62.85" text-anchor="middle" font-size="11" fill="#345">by Requirements Management</text>
  <rect x="500" y="175" width="250" height="62" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/>
  <text x="625" y="196.85" text-anchor="middle" font-size="11" font-weight="bold">Solutions Landscape</text>
  <text x="625" y="209.85" text-anchor="middle" font-size="11" fill="#345">the SBBs that support the specified ABBs;</text>
  <text x="625" y="222.85" text-anchor="middle" font-size="11" fill="#345">not the data those solutions produce</text>
  <line x1="300" y1="90" x2="190" y2="79" stroke="#555" marker-end="url(#arr-f3-12b)"/>
  <text x="255" y="100" text-anchor="end" font-size="10" fill="#666">writes and changes</text>
  <line x1="190" y1="173" x2="300" y2="160" stroke="#555" marker-end="url(#arr-f3-12b)"/>
  <text x="255" y="150" text-anchor="end" font-size="10" fill="#666">reads for reuse</text>
  <line x1="470" y1="100" x2="570" y2="79" stroke="#555" marker-end="url(#arr-f3-12b)"/>
  <line x1="585" y1="79" x2="485" y2="92" stroke="#555" marker-end="url(#arr-f3-12b)"/>
  <text x="525" y="105" text-anchor="start" font-size="10" fill="#666">records and retrieves</text>
  <line x1="470" y1="150" x2="580" y2="173" stroke="#555" marker-end="url(#arr-f3-12b)"/>
  <text x="520" y="150" text-anchor="start" font-size="10" fill="#666">Phase G output</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">The four repository areas the method touches most. Original drawing; the areas follow CONTENT §7.2, CONTENT §7.3.1, CONTENT §7.6.1 and CONTENT §7.7.</figcaption>
</figure>

<!-- figures:start -->
## Figures from the standard

The diagrams the cited sections carry, from your local copy of the publication. The exam reproduces these; know what each box is.

<div class="grid gap-4 md:grid-cols-2">
<figure class="max-w-lg"><img src="/figure/CONTENT:fig-7-1" alt="Figure 7-1: Overview of Architecture Repository" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 7-1: Overview of Architecture Repository (CONTENT)</figcaption></figure>
<figure class="max-w-lg"><img src="/figure/CONTENT:fig-7-2" alt="Figure 7-2: Architecture Continuum" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 7-2: Architecture Continuum (CONTENT)</figcaption></figure>
</div>
<!-- figures:end -->

## Check yourself

- Which body decides the criteria for admitting source material to the repository?
- Which direction on the continuum is "generalising a proven specific solution for reuse"?
- Which repository area can the Architecture Continuum serve as a classification scheme for?
- Which phase owns the contents of the Architecture Requirements Repository?
