---
title: Enterprise architecture, and what the TOGAF Standard is made of
unit: F1
objectives: ["1.1", "1.2"]
refs: ["INTRO §1", "INTRO §1.1", "INTRO §2.1", "INTRO §2.2", "INTRO §2.3", "INTRO §3.1", "INTRO §3.4"]
reading_minutes: 9
source: authored
status: draft
---
## What counts as an "enterprise"

The standard uses *enterprise* loosely on purpose: any group of organisations that share a set
of goals. That can be a whole corporation or one division, a government agency or a single
department, a chain of sites held together by common ownership, several governments working on
a shared deliverable, or a partnership such as a consortium or a supply chain (INTRO §1.1).

Two consequences matter for the exam. First, the "enterprise" in *enterprise architecture* can be
the whole organisation *or* a chosen area of interest inside it, and it may reach out to partners,
suppliers and customers. Second, a large organisation often contains several enterprises, each with
its own architecture; a shared framework then pays off through common building blocks and a
repository everyone can reuse (INTRO §1.1).

## Why an enterprise architecture is needed

The stated purpose is to take the fragmented legacy of processes, manual and automated, and turn
it into an integrated environment that can respond to change and carries the business strategy
(INTRO §1.1). Three pressures are named alongside it: information management and digital
transformation as the route to competitive advantage; the need to balance transformation against
day-to-day operational efficiency, letting business units innovate safely; and privacy legislation
that demands personal-data processes be documented in a form a lay reader can follow (INTRO §1.1).

The benefits are grouped under five headings. Learn the headings; the bullets underneath are
illustrations (INTRO §1.1).

| Benefit group | Flavour of the examples |
|---|---|
| More effective strategic decision-making | agility, transformation, digital, operating-model change |
| More effective and efficient business operations | lower cost, shared capabilities, flexible workforce, M&A integration |
| More effective and efficient digital transformation and operations | harmonised components, interoperability, easier upgrades |
| Better return on existing investment, reduced risk for future investment | less complexity, make/buy/outsource flexibility |
| Faster, simpler, cheaper procurement | coherent plan, multi-vendor open systems |

What actually *starts* an architecture effort is one of four triggers: a business-driven
transformation, a technology-driven efficiency or consolidation drive, a merger or acquisition, or
the technical debt that accumulates from Agile delivery (INTRO §1.1). In every case the job is
to manage complexity where change spans many interdependent systems. The people who identify the
needed change are the **stakeholders**, and the architect serves them by refining their
requirements, producing views that show how their concerns are met, and making the trade-offs
between conflicting concerns visible (INTRO §1.1).

<figure class="my-4">
<svg viewBox="0 0 760 220" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="Four triggers start an architecture effort; stakeholders identify the change and the architect serves them">
  <defs><marker id="arr-f1-10a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
  <rect x="10" y="12" width="215" height="36" rx="6" fill="#fff1d6" stroke="#e0b060"/>
  <text x="117.5" y="27.35" text-anchor="middle" font-size="11" fill="#345">business-driven</text>
  <text x="117.5" y="40.35" text-anchor="middle" font-size="11" fill="#345">transformation</text>
  <line x1="225" y1="30" x2="262" y2="95" stroke="#555" marker-end="url(#arr-f1-10a)"/>
  <rect x="10" y="54" width="215" height="36" rx="6" fill="#fff1d6" stroke="#e0b060"/>
  <text x="117.5" y="69.35" text-anchor="middle" font-size="11" fill="#345">technology-driven efficiency</text>
  <text x="117.5" y="82.35" text-anchor="middle" font-size="11" fill="#345">or consolidation drive</text>
  <line x1="225" y1="72" x2="262" y2="95" stroke="#555" marker-end="url(#arr-f1-10a)"/>
  <rect x="10" y="96" width="215" height="36" rx="6" fill="#fff1d6" stroke="#e0b060"/>
  <text x="117.5" y="111.35" text-anchor="middle" font-size="11" fill="#345">a merger</text>
  <text x="117.5" y="124.35" text-anchor="middle" font-size="11" fill="#345">or acquisition</text>
  <line x1="225" y1="114" x2="262" y2="95" stroke="#555" marker-end="url(#arr-f1-10a)"/>
  <rect x="10" y="138" width="215" height="36" rx="6" fill="#fff1d6" stroke="#e0b060"/>
  <text x="117.5" y="153.35" text-anchor="middle" font-size="11" fill="#345">technical debt</text>
  <text x="117.5" y="166.35" text-anchor="middle" font-size="11" fill="#345">from Agile delivery</text>
  <line x1="225" y1="156" x2="262" y2="95" stroke="#555" marker-end="url(#arr-f1-10a)"/>
  <text x="240" y="190" text-anchor="end" font-size="11" font-weight="bold" fill="#666">four triggers</text>
  <rect x="265" y="55" width="200" height="80" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
  <text x="365" y="77.85" text-anchor="middle" font-size="11" font-weight="bold">an architecture effort</text>
  <text x="365" y="91.85" text-anchor="middle" font-size="11" fill="#345">manage complexity where</text>
  <text x="365" y="105.85" text-anchor="middle" font-size="11" fill="#345">change spans many</text>
  <text x="365" y="119.85" text-anchor="middle" font-size="11" fill="#345">interdependent systems</text>
  <line x1="465" y1="95" x2="518" y2="95" stroke="#555" marker-end="url(#arr-f1-10a)"/>
  <rect x="520" y="15" width="230" height="44" rx="6" fill="#fff" stroke="#666"/>
  <text x="635" y="33.85" text-anchor="middle" font-size="11" font-weight="bold">Stakeholders</text>
  <text x="635" y="47.85" text-anchor="middle" font-size="11" fill="#345">identify the change that is needed</text>
  <rect x="520" y="100" width="230" height="72" rx="6" fill="#fff" stroke="#666"/>
  <text x="635" y="120.35" text-anchor="middle" font-size="11" font-weight="bold">The architect serves them by</text>
  <text x="635" y="133.35" text-anchor="middle" font-size="11" fill="#345">refining their requirements,</text>
  <text x="635" y="146.35" text-anchor="middle" font-size="11" fill="#345">producing views that show concerns met,</text>
  <text x="635" y="159.35" text-anchor="middle" font-size="11" fill="#345">making trade-offs visible</text>
  <line x1="635" y1="60" x2="635" y2="98" stroke="#555" marker-end="url(#arr-f1-10a)"/>
  <text x="635" y="80" text-anchor="start" font-size="10" fill="#666">serves</text>
  <text x="400" y="210" text-anchor="middle" font-size="11" fill="#c0392b">do it early and throughout the change; architecture done after the decisions is only documentation of them</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">What starts the work and who it is for. Original drawing; the triggers and roles follow INTRO §1.1.</figcaption>
</figure>

> **Trap.** "When should EA be done?" The standard's answer is *early and throughout* the change.
> Architecture produced after the decisions are taken is just documentation of them, or at best
> enforcement; the insight into consequences has been lost (INTRO §1.1).

## An architecture framework, and why this one

An architecture framework is a foundational structure (or set of structures) for building many
different architectures. It should carry a method for describing baseline and target states in
terms of building blocks, for showing how those blocks fit together, and for planning the move
from one state to the other. Frameworks are tailored to the organisation, and the tailoring
should yield a toolset and a shared vocabulary (INTRO §1.1).

The case for the TOGAF Standard specifically: it was built by a broad community, so using it
gives architectures that are consistent, reflect stakeholder needs, apply best practice and weigh
current against future needs; it standardises and de-risks a technically complex process; and it is
meant to be adapted, so it fits Agile enterprises and digital transformation as well as
traditional programmes (INTRO §1.1). Anyone planning an EA for business transformation benefits,
as do organisations chasing Boundaryless Information Flow or an open-systems procurement
specification (INTRO §1.1).

In the standard's own summary, it is an architecture framework offering methods and tools for
the acceptance, production, use and maintenance of an enterprise architecture, resting on an
iterative process model, best practice and a reusable set of architecture assets (INTRO §3.1).

## Where it came from, and how freely it can be used

Version 1 dates from 1995 and was built, with explicit permission, on the US Department of
Defense's TAFIM. It is maintained by The Open Group's Architecture Forum, which publishes each
edition on the public website (INTRO §1). Any organisation may use it freely to develop an
architecture for its own internal use; commercial reproduction needs permission (INTRO §1). The
standard expects adopters to customise: keep some parts, tailor others, drop some and add their
own, for instance adopting the metamodel while ignoring the Technology Architecture guidance
because the enterprise is cloud-heavy (INTRO §1).

## The structure of the 10th Edition

The documentation set is a portfolio. The **TOGAF Standard** comes as a set of separate
documents that are designed to be used together; the **TOGAF Library** is a separate portfolio of
additional guidance supporting practical application (INTRO §2.1).

The Standard is described as an open, industry-consensus and *foundational* framework, meaning it
applies to any kind of architecture in any context; the Library supplements it with guidance for
specific contexts (INTRO §2.2). Its structure mirrors the structure of an Architecture Capability
inside an enterprise (INTRO §2.2).

The **TOGAF Fundamental Content** is six documents (INTRO §2.2):

| Document | What it holds |
|---|---|
| Introduction and Core Concepts | this overview, the core concepts, the definitions |
| Architecture Development Method | the ADM: an iterative approach to developing an EA |
| ADM Techniques | a collection of techniques used when applying the ADM |
| Applying the ADM | guidelines for adapting the ADM to a style of architecture in a practical context |
| Architecture Content | the Content Framework, the metamodel, reusable ABBs, and an overview of typical deliverables |
| EA Capability and Governance | organisation, processes, skills, roles and responsibilities for an architecture function, plus a governance framework |

Splitting the content this way is deliberate: areas of specialisation can be studied and even
adopted in isolation. The standard names two situations where partial adoption is encouraged:
organisations new to TOGAF adopting incrementally, and organisations that already run another
framework and want to merge in parts of this one (INTRO §2.2).

The Standard as a whole is the Fundamental Content **plus** the **TOGAF Series Guides**, which give
practical guidance for applying it. Guides serve practitioners who need more detail than the core,
not every guide is relevant to every situation, and they are revised faster than the core through
a continuous delivery pipeline in the Architecture Forum (INTRO §2.2). The example areas include
strategy and business-value decisions, business architecture and operating models, information
and data management, reference and integration models, adopting technology trends, security
architecture and risk, the Agile enterprise, the digital enterprise, and using the standard with
other Open Group standards such as O-AA, DPBoK, IT4IT, ArchiMate and Microservices Architecture
(INTRO §2.2).

> **Trap.** Series Guides versus the TOGAF Library. The Series Guides are *part of the Standard*.
> The Library is the accompanying reference library of guidelines, templates, patterns and other
> reference material, governed by the Architecture Forum, and it feeds the **Reference Library**
> class of the Architecture Repository (INTRO §2.3). A question that asks what supports the
> Reference Library wants the TOGAF Library; one that asks what the Standard comprises wants
> Fundamental Content plus Series Guides.

<figure class="my-4">
<svg viewBox="0 0 760 275" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="The Standard is the six Fundamental Content documents plus the Series Guides; the TOGAF Library is separate and feeds the Reference Library of the repository">
  <defs><marker id="arr-f1-10b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
  <rect x="10" y="10" width="740" height="255" rx="8" fill="#f4f4f4" stroke="#bbb" stroke-dasharray="6 4"/>
  <text x="380.0" y="28" text-anchor="middle" font-size="12" font-weight="bold">The TOGAF Documentation Set: a portfolio of separate documents designed to be used together</text>
  <rect x="25" y="40" width="505" height="210" rx="8" fill="#fff" stroke="#666"/>
  <text x="277.5" y="58" text-anchor="middle" font-size="12" font-weight="bold">The TOGAF Standard = Fundamental Content + Series Guides</text>
  <rect x="40" y="70" width="310" height="170" rx="8" fill="#e0ecff" stroke="#7aa2e3"/>
  <text x="195.0" y="88" text-anchor="middle" font-size="12" font-weight="bold">Fundamental Content (six documents)</text>
  <rect x="50" y="95" width="140" height="40" rx="6" fill="#fff" stroke="#666"/>
  <text x="120" y="111.85" text-anchor="middle" font-size="11" fill="#345">Introduction and</text>
  <text x="120" y="125.85" text-anchor="middle" font-size="11" fill="#345">Core Concepts</text>
  <rect x="200" y="95" width="140" height="40" rx="6" fill="#fff" stroke="#666"/>
  <text x="270" y="111.85" text-anchor="middle" font-size="11" fill="#345">Architecture</text>
  <text x="270" y="125.85" text-anchor="middle" font-size="11" fill="#345">Development Method</text>
  <rect x="50" y="142" width="140" height="40" rx="6" fill="#fff" stroke="#666"/>
  <text x="120" y="165.85" text-anchor="middle" font-size="11" fill="#345">ADM Techniques</text>
  <rect x="200" y="142" width="140" height="40" rx="6" fill="#fff" stroke="#666"/>
  <text x="270" y="165.85" text-anchor="middle" font-size="11" fill="#345">Applying the ADM</text>
  <rect x="50" y="189" width="140" height="40" rx="6" fill="#fff" stroke="#666"/>
  <text x="120" y="212.85" text-anchor="middle" font-size="11" fill="#345">Architecture Content</text>
  <rect x="200" y="189" width="140" height="40" rx="6" fill="#fff" stroke="#666"/>
  <text x="270" y="205.85" text-anchor="middle" font-size="11" fill="#345">EA Capability</text>
  <text x="270" y="219.85" text-anchor="middle" font-size="11" fill="#345">and Governance</text>
  <text x="362" y="160" text-anchor="middle" font-size="20" font-weight="bold">+</text>
  <rect x="375" y="70" width="145" height="170" rx="8" fill="#fff1d6" stroke="#e0b060"/>
  <text x="447.5" y="88" text-anchor="middle" font-size="12" font-weight="bold">Series Guides</text>
  <text x="447" y="108" text-anchor="middle" font-size="11" fill="#345">how to apply the</text>
  <text x="447" y="124" text-anchor="middle" font-size="11" fill="#345">Standard in practice;</text>
  <text x="447" y="140" text-anchor="middle" font-size="11" fill="#345">not every guide fits</text>
  <text x="447" y="156" text-anchor="middle" font-size="11" fill="#345">every situation;</text>
  <text x="447" y="172" text-anchor="middle" font-size="11" fill="#345">revised faster, by</text>
  <text x="447" y="188" text-anchor="middle" font-size="11" fill="#345">continuous delivery</text>
  <rect x="555" y="40" width="180" height="210" rx="8" fill="#f3e3f7" stroke="#b58ac9"/>
  <text x="645.0" y="58" text-anchor="middle" font-size="12" font-weight="bold">The TOGAF Library</text>
  <text x="645" y="72" text-anchor="middle" font-size="11" fill="#345">a separate portfolio:</text>
  <text x="645" y="87" text-anchor="middle" font-size="11" fill="#345">guidelines, templates,</text>
  <text x="645" y="102" text-anchor="middle" font-size="11" fill="#345">patterns, reference material;</text>
  <text x="645" y="117" text-anchor="middle" font-size="11" fill="#345">governed by the</text>
  <text x="645" y="132" text-anchor="middle" font-size="11" fill="#345">Architecture Forum</text>
  <line x1="645" y1="150" x2="645" y2="172" stroke="#555" marker-end="url(#arr-f1-10b)"/>
  <rect x="570" y="175" width="150" height="60" rx="6" fill="#fff" stroke="#666"/>
  <text x="645" y="194.85" text-anchor="middle" font-size="11" fill="#345">feeds the Reference Library</text>
  <text x="645" y="208.85" text-anchor="middle" font-size="11" fill="#345">class of the Architecture</text>
  <text x="645" y="222.85" text-anchor="middle" font-size="11" fill="#345">Repository</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">What the Standard comprises, and what sits outside it. Original drawing; the structure follows INTRO §2.2 and INTRO §2.3.</figcaption>
</figure>

The ADM document says *what* may be done to define and deploy an EA; guidance on *how* to do it is
what the Series Guides are for (INTRO §3.4).

<!-- figures:start -->
## Figures from the standard

The diagrams the cited sections carry, from your local copy of the publication. The exam reproduces these; know what each box is.

<div class="grid gap-4 md:grid-cols-2">
<figure class="max-w-lg"><img src="/figure/INTRO:fig-2-1" alt="Figure 2-1: The TOGAF Documentation Set" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 2-1: The TOGAF Documentation Set (INTRO)</figcaption></figure>
<figure class="max-w-lg"><img src="/figure/INTRO:fig-2-2" alt="Figure 2-2: Structure of the TOGAF Standard" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 2-2: Structure of the TOGAF Standard (INTRO)</figcaption></figure>
<figure class="max-w-lg"><img src="/figure/INTRO:fig-2-3" alt="Figure 2-3: The TOGAF Standard" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 2-3: The TOGAF Standard (INTRO)</figcaption></figure>
<figure class="max-w-lg"><img src="/figure/INTRO:fig-2-4" alt="Figure 2-4: The TOGAF Library Continuum" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 2-4: The TOGAF Library Continuum (INTRO)</figcaption></figure>
<figure class="max-w-lg"><img src="/figure/INTRO:fig-3-1" alt="Figure 3-1: Architecture Development Cycle" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 3-1: Architecture Development Cycle (INTRO)</figcaption></figure>
</div>
<!-- figures:end -->

## Check yourself

- Which of the five benefit groups would "simpler buying decisions" fall under?
- Name the four triggers for starting an architecture effort.
- Is a Series Guide part of the Fundamental Content? Is it part of the Standard?
- Which document would you open for the metamodel? For the Architecture Board?
