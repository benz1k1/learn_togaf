---
title: Preliminary Phase in depth
unit: F4
objectives: ["4.1", "4.3"]
refs: ["ADM §2", "ADM §2.1", "ADM §2.2", "ADM §2.2.1", "ADM §2.2.2", "ADM §2.2.3", "ADM §2.3", "ADM §2.3.1", "ADM §2.3.2", "ADM §2.3.3", "ADM §2.3.4", "ADM §2.3.5", "ADM §2.3.6", "ADM §2.4", "ADM §2.5", "ADM §2.5.1", "ADM §2.5.5", "ADM §2.5.7"]
reading_minutes: 10
source: authored
status: draft
---
## What the phase is for

The Preliminary Phase prepares the enterprise to do architecture at all. It is not about any
one architecture project; it is about building the *capability* that projects will later use:
the team, the governance, the principles, the tailored framework and the tools (ADM §2). The
standard's own summary is that it answers "where, what, why, who and how" architecture is done
in this enterprise (ADM §2.5).

Two objectives, and the exam expects you to know both verbs (ADM §2.1):

| Objective | What it covers |
|---|---|
| **Determine** the Architecture Capability the organization wants | review the organizational context; identify and scope the enterprise organizations affected; identify the frameworks, methods and processes that intersect with the capability; set a Capability Maturity target |
| **Establish** the Architecture Capability | define the Organizational Model for Enterprise Architecture; define the process and resources for Architecture Governance; select and implement tools; define the Architecture Principles |

## Approach — the seven aspects

The approach section lists what "where, what, why, who and how" turns into in practice
(ADM §2.5): defining the enterprise; identifying key drivers and the organizational context;
defining the requirements for architecture work; defining the Architecture Principles; defining
the framework to be used; defining the relationships between management frameworks; and
evaluating Enterprise Architecture maturity.

Three points from the approach come up repeatedly:

- **A sponsor must be appointed at this stage** so the work has resources and management support
  (ADM §2.5.1).
- The TOGAF framework has to co-exist with four other management frameworks — Business Capability
  Management, Project/Portfolio Management, Operations Management and Solution Development Methods
  (ADM §2.5.5).
- Maturity is assessed with a Capability Maturity Model; the standard recommends taking an
  existing model and customizing it rather than inventing one (ADM §2.5.7).

The phase **may be revisited from Phase A** when the capability in place turns out not to suit
the architecture problem at hand (ADM §2.5).

## Inputs

The standard groups inputs three ways in every phase. For the Preliminary Phase almost
everything is *non-architectural*, because the architecture capability does not exist yet
(ADM §2.2).

| Group | Inputs |
|---|---|
| Reference materials external to the enterprise (ADM §2.2.1) | the TOGAF Library; other architecture frameworks, if required |
| Non-architectural (ADM §2.2.2) | board strategies and business plans, business strategy, IT strategy, business principles, goals and drivers (when pre-existing); the major frameworks operating in the business, e.g. project/portfolio management; governance and legal frameworks, including any existing Architecture Governance strategy; the architecture capability; partnership and contract agreements |
| Architectural (ADM §2.2.3) | a pre-existing Organizational Model for Enterprise Architecture used as a baseline; an existing Architecture Framework, if any (method, content, tools, principles, repository) |

## Steps

Six steps, and the order may be adapted to the situation under the established governance
(ADM §2.3):

| # | Step | What it produces |
|---|---|---|
| 1 | Scope the enterprise organizations impacted | core, soft and extended enterprise units; communities; governance and legal frameworks involved (ADM §2.3.1) |
| 2 | Confirm governance and support frameworks | the shape of Architecture Governance (centralized/federated, light/heavy) and its repository needs (ADM §2.3.2) |
| 3 | Define and establish the Enterprise Architecture team and organization | maturity assessment, gaps, roles and responsibilities, constraints, budget, agreement with sponsors and board (ADM §2.3.3) |
| 4 | Identify and establish Architecture Principles | principles based on business principles, the foundation for governance (ADM §2.3.4) |
| 5 | Tailor the TOGAF framework and any other selected frameworks | terminology, process and content tailoring (ADM §2.3.5) |
| 6 | Develop a strategy and implementation plan for tools and techniques | a tools strategy matched to stakeholder formality and maturity (ADM §2.3.6) |

The three kinds of tailoring in step 5 are worth memorizing: **terminology** (an agreed glossary),
**process** (remove, add and align ADM tasks with portfolio, project, operations and procurement
processes) and **content** (structure and classification of deliverables and artifacts).

## Outputs

The outputs "may include, but are not restricted to" (ADM §2.4):

| Output | Note |
|---|---|
| Organizational Model for Enterprise Architecture | scope of organizations impacted, maturity assessment, roles and responsibilities, constraints, budget, governance and support strategy |
| Tailored Architecture Framework | tailored method, tailored content, **Architecture Principles**, configured and deployed tools |
| Initial Architecture Repository | populated with framework content |
| Restatement of, or reference to, business principles, goals and drivers | |
| Request for Architecture Work | **optional** |
| Architecture Governance Framework | |
| The Architecture of the Enterprise Architecture Capability | |
| Principles catalog | the one artifact named for this phase |

<figure class="my-4">
<svg viewBox="0 0 760 288" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="Preliminary Phase: its inputs, six steps and outputs, with the deliverables it produces first">
  <defs><marker id="arr-f4-10" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
  <text x="107.5" y="18" text-anchor="middle" font-size="12" font-weight="bold" fill="#345">Inputs</text><text x="652.5" y="18" text-anchor="middle" font-size="12" font-weight="bold" fill="#345">Outputs</text><text x="380" y="18" text-anchor="middle" font-size="12" font-weight="bold" fill="#345">Steps</text><rect x="235" y="34" width="290" height="220" rx="8" fill="#fff1d6" stroke="#e0b060"/><text x="380" y="52" text-anchor="middle" font-size="12" font-weight="bold">Preliminary Phase</text><text x="245" y="114" font-size="11">1 Scope the enterprise organizations impacted</text><text x="245" y="129" font-size="11">2 Confirm governance and support frameworks</text><text x="245" y="144" font-size="11">3 Define and establish the EA team</text><text x="245" y="159" font-size="11">4 Identify and establish Architecture Principles</text><text x="245" y="174" font-size="11">5 Tailor the TOGAF framework</text><text x="245" y="189" font-size="11">6 Strategy and plan for tools and techniques</text><rect x="10" y="34" width="195" height="46" rx="6" fill="#e0ecff" stroke="#7aa2e3"/><text x="107.5" y="54.5" text-anchor="middle" font-size="10.5">TOGAF Library; other</text><text x="107.5" y="67.5" text-anchor="middle" font-size="10.5">frameworks if required</text><line x1="205" y1="57" x2="233" y2="57" stroke="#555" marker-end="url(#arr-f4-10)"/><rect x="10" y="92" width="195" height="46" rx="6" fill="#e0ecff" stroke="#7aa2e3"/><text x="107.5" y="112.5" text-anchor="middle" font-size="10.5">Business strategy, principles,</text><text x="107.5" y="125.5" text-anchor="middle" font-size="10.5">goals and drivers; IT strategy</text><line x1="205" y1="115" x2="233" y2="115" stroke="#555" marker-end="url(#arr-f4-10)"/><rect x="10" y="150" width="195" height="46" rx="6" fill="#e0ecff" stroke="#7aa2e3"/><text x="107.5" y="170.5" text-anchor="middle" font-size="10.5">Governance and legal frameworks;</text><text x="107.5" y="183.5" text-anchor="middle" font-size="10.5">partnership and contract agreements</text><line x1="205" y1="173" x2="233" y2="173" stroke="#555" marker-end="url(#arr-f4-10)"/><rect x="10" y="208" width="195" height="46" rx="6" fill="#e0ecff" stroke="#7aa2e3"/><text x="107.5" y="228.5" text-anchor="middle" font-size="10.5">Pre-existing Organizational Model</text><text x="107.5" y="241.5" text-anchor="middle" font-size="10.5">and Architecture Framework, if any</text><line x1="205" y1="231" x2="233" y2="231" stroke="#555" marker-end="url(#arr-f4-10)"/><rect x="555" y="34" width="195" height="46" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/><text x="652.5" y="54.5" text-anchor="middle" font-size="10.5">Organizational Model for</text><text x="652.5" y="67.5" text-anchor="middle" font-size="10.5">Enterprise Architecture</text><rect x="711" y="26" width="35" height="15" rx="7" fill="#f3e3f7" stroke="#b58ac9"/><text x="728.5" y="37" text-anchor="middle" font-size="9.5" fill="#5b2d6e">first</text><line x1="525" y1="57" x2="553" y2="57" stroke="#555" marker-end="url(#arr-f4-10)"/><rect x="555" y="92" width="195" height="46" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/><text x="652.5" y="112.5" text-anchor="middle" font-size="10.5">Tailored Architecture Framework,</text><text x="652.5" y="125.5" text-anchor="middle" font-size="10.5">with the Architecture Principles</text><rect x="711" y="84" width="35" height="15" rx="7" fill="#f3e3f7" stroke="#b58ac9"/><text x="728.5" y="95" text-anchor="middle" font-size="9.5" fill="#5b2d6e">first</text><line x1="525" y1="115" x2="553" y2="115" stroke="#555" marker-end="url(#arr-f4-10)"/><rect x="555" y="150" width="195" height="46" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/><text x="652.5" y="177" text-anchor="middle" font-size="10.5">Initial Architecture Repository</text><rect x="711" y="142" width="35" height="15" rx="7" fill="#f3e3f7" stroke="#b58ac9"/><text x="728.5" y="153" text-anchor="middle" font-size="9.5" fill="#5b2d6e">first</text><line x1="525" y1="173" x2="553" y2="173" stroke="#555" marker-end="url(#arr-f4-10)"/><rect x="555" y="208" width="195" height="46" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/><text x="652.5" y="235" text-anchor="middle" font-size="10.5">Request for Architecture Work</text><rect x="694.8" y="200" width="51.2" height="15" rx="7" fill="#f3e3f7" stroke="#b58ac9"/><text x="720.4" y="211" text-anchor="middle" font-size="9.5" fill="#5b2d6e">optional</text><line x1="525" y1="231" x2="553" y2="231" stroke="#555" marker-end="url(#arr-f4-10)"/><text x="380" y="272" text-anchor="middle" font-size="11" fill="#666">Almost every input is non-architectural: the capability does not exist yet (ADM §2.2)</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">Inputs, steps and outputs of the Preliminary Phase. Original drawing; inputs and outputs per ADM §2.2 and ADM §2.4, steps per ADM §2.3.</figcaption>
</figure>

> **Trap.** The exam likes to place the Request for Architecture Work. It is an *optional
> output* of the Preliminary Phase and the *triggering input* of Phase A. Likewise Architecture
> Principles are *established* here (step 4) and only *confirmed and elaborated* in Phase A.
> If an option says Phase A "defines" the principles for the first time, that is only the
> fallback when the Preliminary Phase did not do it.

> **Trap.** "Determine" and "establish" are the two objectives. Distractors use verbs from other
> phases: "develop a vision" (A), "develop the Target Business Architecture" (B), "generate the
> Architecture Roadmap" (E), "ensure conformance by implementation projects" (G).

<!-- figures:start -->
## Figures from the standard

The diagrams the cited sections carry, from your local copy of the publication. The exam reproduces these; know what each box is.

<div class="grid gap-4 md:grid-cols-2">
<figure class="max-w-lg"><img src="/figure/ADM:fig-2-2" alt="Figure 2-2: Management Frameworks to Co-ordinate with the TOGAF Framework" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 2-2: Management Frameworks to Co-ordinate with the TOGAF Framework (ADM)</figcaption></figure>
<figure class="max-w-lg"><img src="/figure/ADM:fig-2-3" alt="Figure 2-3: Interoperability and Relationships between Management Frameworks" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 2-3: Interoperability and Relationships between Management Frameworks (ADM)</figcaption></figure>
</div>
<!-- figures:end -->

## Check yourself

1. Which two objectives does the Preliminary Phase have, and which one contains the maturity target?
2. Name the three kinds of tailoring.
3. Which Preliminary output is optional, and where does it go next?
4. Which four management frameworks must the TOGAF framework co-ordinate with?
