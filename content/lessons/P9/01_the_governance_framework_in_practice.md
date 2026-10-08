---
title: The Architecture Governance Framework in practice, processes, structures and the board
unit: P9
objectives: ["P9.1"]
refs: ["GOV §3.1.1", "GOV §3.1.5", "GOV §3.2", "GOV §3.2.1", "GOV §3.2.2", "GOV §3.3.1", "GOV §3.3.2", "GOV §4.1", "GOV §4.2", "GOV §4.3.1", "GOV §4.3.2", "GOV §4.4.3", "GOV §6.1", "CONTENT §7.5"]
reading_minutes: 10
source: authored
status: draft
---
## What a governance scenario looks like

The scenario describes an enterprise whose architecture decisions are not sticking: projects
buy what they like, a regional unit runs its own standards, the CIO sponsors the architecture
but nobody else does, and a new regulation has to be "taken on" by every project. It asks how
to establish or repair Architecture Governance. The five-point answer applies the framework
the standard describes, its processes, its organisational structure and the three elements of
an effective strategy, and it establishes a properly sized, executive-sponsored,
cross-organisational Architecture Board. The three-point answer creates a board but gives it
no executive sponsor or no compliance strategy; the one-point answer writes a policy document
and calls it governance; the zero-point answer treats governance as a project gate at the end.

Architecture Governance is the practice by which enterprise and other architectures are
managed and controlled at enterprise level, inside a hierarchy of corporate, technology, IT
and architecture governance that may repeat at global, regional and local levels
(GOV §3.1.1). It includes a system of controls over the creation and monitoring of
architectural components, a system to ensure compliance with internal and external standards
and regulation, processes to manage those within agreed parameters, and practices that ensure
accountability to an identified stakeholder community; implementation governance in Phase G is
only one aspect of it (GOV §3.1.5).

## The framework: process, content, context

Conceptually, governance is an approach, a series of processes, a cultural orientation and a
set of owned responsibilities that ensure the integrity and effectiveness of the
architectures; splitting process from content from context lets new governance material,
legal, regulatory or standards-based, be introduced without disturbing the processes, and the
framework is integral to the Enterprise Continuum (GOV §3.2.1). The key processes are the ones
a scenario will name obliquely:

| Process | What it does | The cue in the scenario |
|---|---|---|
| Policy management and take-on | register, validate, ratify, manage and publish new or updated content, contracts and amendments | "a new regulation must apply to all projects" |
| Compliance | assess against SLAs, OLAs, standards and regulation on an ongoing basis; accept or reject by the framework's criteria | "the project has chosen a different product" |
| Dispensation (waiver) | when an assessment is rejected: adjust, or grant a time-bound dispensation with enforced criteria, never indefinite | "can they carry on for six months?" |
| Monitoring and reporting | performance management against SLAs and OLAs, feedback and reporting | "how do we know it is working?" |
| Business control | ensure compliance with business policies | "premium-rate calls must be barred" |
| Environment management | the repository-based environment: physical and logical repositories, access, training, accreditation | "where are the decisions recorded?" (GOV §3.2.1) |

The Governance Repository is where that environment lives: a decision log of architecturally
significant decisions (product selections, standards deviations, Change Request evaluations,
re-use assessments), the compliance assessments, capability assessments, a calendar of in-flight
projects and reviews, the project portfolio and performance measurement (CONTENT §7.5).

<figure class="my-4">
<svg viewBox="0 0 760 300" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="11" role="img" aria-label="The Architecture Governance Framework: governance processes in a loop around the Governance Repository, an organisational structure of global and local boards, design authorities and working parties, and the three elements of an effective strategy">
<defs><marker id="arr-p9g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
<g fill="#fff" stroke="#666">
<rect x="15" y="20" width="120" height="44" rx="6"/>
<rect x="160" y="20" width="120" height="44" rx="6"/>
<rect x="305" y="20" width="120" height="44" rx="6"/>
<rect x="450" y="20" width="120" height="44" rx="6"/>
</g>
<text x="75" y="38" text-anchor="middle" font-weight="bold">policy take-on</text><text x="75" y="54" text-anchor="middle">register, ratify, publish</text>
<text x="220" y="38" text-anchor="middle" font-weight="bold">compliance</text><text x="220" y="54" text-anchor="middle">assess, accept or reject</text>
<text x="365" y="38" text-anchor="middle" font-weight="bold">dispensation</text><text x="365" y="54" text-anchor="middle">time-bound, criteria</text>
<text x="510" y="38" text-anchor="middle" font-weight="bold">monitoring</text><text x="510" y="54" text-anchor="middle">SLAs, OLAs, reporting</text>
<line x1="135" y1="42" x2="160" y2="42" stroke="#555" marker-end="url(#arr-p9g)"/>
<line x1="280" y1="42" x2="305" y2="42" stroke="#555" marker-end="url(#arr-p9g)"/>
<line x1="425" y1="42" x2="450" y2="42" stroke="#555" marker-end="url(#arr-p9g)"/>
<path d="M570 42 L600 42 L600 100 L75 100 L75 64" fill="none" stroke="#555" stroke-dasharray="5 4" marker-end="url(#arr-p9g)"/>
<text x="340" y="96" text-anchor="middle" fill="#666">dispensation expiry triggers the next compliance activity (GOV §3.2.1)</text>
<rect x="615" y="20" width="130" height="80" rx="8" fill="#fff1d6" stroke="#e0b060"/>
<text x="680" y="42" text-anchor="middle" font-weight="bold">Governance Repository</text>
<text x="680" y="58" text-anchor="middle">decision log, assessments,</text>
<text x="680" y="72" text-anchor="middle">calendar, portfolio,</text>
<text x="680" y="86" text-anchor="middle">performance (CONTENT §7.5)</text>
<rect x="15" y="130" width="355" height="110" rx="8" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="192" y="150" text-anchor="middle" font-weight="bold">Organisational structure (GOV §3.2.2)</text>
<text x="192" y="170" text-anchor="middle">global governance board</text>
<text x="192" y="186" text-anchor="middle">local governance boards</text>
<text x="192" y="202" text-anchor="middle">design authorities</text>
<text x="192" y="218" text-anchor="middle">working parties</text>
<text x="192" y="234" text-anchor="middle">areas: Develop (the ADM), Implement (Phase G), Deploy</text>
<rect x="390" y="130" width="355" height="110" rx="8" fill="#e3f5e1" stroke="#7fbf7a"/>
<text x="567" y="150" text-anchor="middle" font-weight="bold">Three elements of an effective strategy (GOV §3.3.2)</text>
<text x="567" y="172" text-anchor="middle">1 a cross-organisational Architecture Board with executive backing</text>
<text x="567" y="192" text-anchor="middle">2 a comprehensive set of Architecture Principles</text>
<text x="567" y="212" text-anchor="middle">3 an Architecture Compliance strategy: impact assessments,</text>
<text x="567" y="228" text-anchor="middle">a formal review process, perhaps involvement in procurement</text>
<text x="380" y="275" text-anchor="middle" fill="#666">an architecture imposed without executive support and political alignment is bound to fail (GOV §3.3.2)</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">The governance framework as a process loop, a structure and a strategy. Original drawing; the processes follow GOV §3.2.1, the structure §3.2.2 and the strategy elements §3.3.2.</figcaption>
</figure>

## Structure and success factors

The organisational structure typically has a global governance board, local governance
boards, design authorities and working parties, and three key areas, Develop (linked to the
ADM), Implement (linked to Phase G) and Deploy, with the Enterprise Continuum supporting all of
them (GOV §3.2.2). The key success factors include best practices for the submission,
adoption, re-use and retirement of policies, roles and structures; organisational
responsibilities to support the processes; integration of tools and processes both procedurally
and culturally; criteria for controlling dispensations, compliance assessments, SLAs and OLAs;
and requirements for the confidentiality, integrity, availability and reliability of
governance information (GOV §3.3.1). An architecture imposed without executive support and
corporate political alignment is bound to fail; the three elements that make a strategy
effective are a cross-organisational Architecture Board with executive backing, a
comprehensive set of principles, and a compliance strategy that is more than a policy
statement: project impact assessments, a formal review process and possibly involvement of the
architecture team in product procurement (GOV §3.3.2). The compliance chapter adds that the IT
governance function normally defines two complementary processes: project-specific
Project Architectures prepared by the architecture function, and a formal compliance review
process for all projects (GOV §6.1).

## The Architecture Board

The board is representative of all key stakeholders and typically a group of executives
responsible for review and maintenance of the overall architecture; in larger enterprises it
exists at local and global level, each with articulated responsibilities, decision-making
capability, remit and authority limits (GOV §4.1). It is accountable for the basis of all
architecture decisions, consistency between sub-architectures, re-use targets, flexibility,
enforcement of compliance, improving maturity, adoption of architecture-based development and
a visible escalation capability; operationally it monitors and controls the Architecture
Contract, meets regularly, resolves escalated conflicts, grants dispensations in keeping with
strategy, and considers policy changes where similar dispensations keep being requested
(GOV §4.2).

Two numbers and one relationship matter for the exam. The recommended size is four or five
permanent members and no more than ten, with rotation, representational membership and
staggered terms for continuity (GOV §4.3.2). The board is the sponsor of the architecture,
but it needs its own executive sponsor from the highest level, and a frequently overlooked
source of members is the company's Board of Directors (GOV §4.3.1). The standing agenda is
minutes, Requests for Change, dispensations, compliance assessments, dispute resolution,
strategy and direction documents (global board only), assigned actions with a tracker,
contract documentation management, any other business and the schedule (GOV §4.4.3).

**Trap.** A board of fifteen department heads chaired by the CIO fails two rules at once: more
than ten members, and no sponsor above the CIO (GOV §4.3.1, GOV §4.3.2).

## How the 5, 3 and 1 differ

| Answer | Why it scores that |
|---|---|
| 5 | Establishes the board at four to five members with an executive sponsor at the top of the corporation and representation for the regions, publishes principles, adopts a compliance strategy with impact assessments and a formal review process, takes the regulation on through policy management, records decisions in the Governance Repository, and handles the deviating project through compliance and a time-bound dispensation |
| 3 | Creates the board and the review process but leaves the regional unit outside its remit, or gives it no executive sponsor; governance without political alignment fails (GOV §3.3.2, GOV §4.3.1) |
| 1 | Publishes an architecture policy and asks projects to comply; a compliance strategy must be specific measures, more than a statement of policy (GOV §3.3.2) |
| 0 | Reviews projects only at go-live; governance extends across development, implementation and operation, and the review's value is catching errors early (GOV §3.2.2, GOV §6.1) |

## Where to look in the book

EA Capability and Governance chapter 3: §3.1.5 for what governance includes, §3.2.1 for the
processes, §3.2.2 for the structure, §3.3.1 for success factors, §3.3.2 for the three
elements. Chapter 4: §4.1 role, §4.2 responsibilities, §4.3.1 sponsorship, §4.3.2 size, §4.4.3
agenda. Chapter 6 §6.1 for the two complementary compliance processes. Architecture Content
§7.5 for the Governance Repository.

## Check yourself

- Name the six governance processes.
- What is the recommended board size, and who sponsors the board?
- What three things make a compliance strategy more than a policy statement?
