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

The ADM document says *what* may be done to define and deploy an EA; guidance on *how* to do it is
what the Series Guides are for (INTRO §3.4).

## Check yourself

- Which of the five benefit groups would "simpler buying decisions" fall under?
- Name the four triggers for starting an architecture effort.
- Is a Series Guide part of the Fundamental Content? Is it part of the Standard?
- Which document would you open for the metamodel? For the Architecture Board?
