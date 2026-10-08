---
title: The governance-related guides, project management, maturity models, skills, partitioning and the repository
unit: G_GOVERNANCE
objectives: ["G7.1"]
refs: ["GUIDE:architecture-project-management §2.1", "GUIDE:architecture-project-management §2.2", "GUIDE:architecture-project-management §2.3", "GUIDE:architecture-project-management §2.4", "GUIDE:architecture-project-management §3.1", "GUIDE:architecture-project-management §4", "GUIDE:architecture-project-management §4.1.1", "GUIDE:architecture-project-management §4.1.2", "GUIDE:architecture-project-management §5", "GUIDE:architecture-maturity-models §1.2", "GUIDE:architecture-maturity-models §2.2", "GUIDE:architecture-skills-framework §1.2", "GUIDE:architecture-skills-framework §4.3", "GUIDE:architecture-roles-and-skills §3", "GUIDE:architecture-roles-and-skills §4", "GUIDE:architecture-roles-and-skills §5", "APPLY §4.1", "APPLY §4.2", "CONTENT §7.1", "CONTENT §7.5"]
reading_minutes: 11
source: authored
status: draft
---
## Which guide, for which governance question

Unit G_GOVERNANCE groups the guides an architect reaches for when the question is about how
the architecture *work* is run rather than what the architecture contains: how to manage an
architecture engagement as a project, how mature the practice is, what roles and skills it
needs, how to partition the work, and how the repository is organised. The scenario cue tells
you which:

| Cue | Guide | The idea it contributes |
|---|---|---|
| "the PMO wants a project plan and stages for the architecture work" | Architecture Project Management | an Architecture Project is Phases A to F plus Requirements Management, run in stages and mapped to PRINCE2 and PMBOK |
| "how good is our architecture practice, what do we fix first" | Architecture Maturity Models | assess against a model such as the ACMM, six levels and nine elements, and direct effort at the weak elements |
| "what is an Enterprise Architect, whom do we hire" | Architecture Skills Framework and Architecture Roles and Skills | roles, skill categories and proficiency levels; Chief, Enterprise, Segment and Solution Architect |
| "three teams need to work on the landscape at once" | Architecture Partitioning (Applying the ADM) | partition by subject matter, time and level of detail, decided in the Preliminary Phase |
| "where do decisions and assessments get recorded" | Architecture Repository (Architecture Content) | the Governance Repository and the other repository areas |

## Architecture Project Management

An Architecture Project is an endeavour undertaken to define and describe the Enterprise
Architecture to be implemented; it encompasses Phases A to F and Requirements Management, and
it explicitly excludes the Preliminary Phase (which establishes capability and may initiate a
project), Phase G (implementing, not defining, and possibly a separate project or programme)
and Phase H (a continuous operational process). It starts with a Request for Architecture
Work, delivers an Architecture Definition, a Roadmap and an Implementation Plan, and finishes
when those are handed over for implementation; it covers one architecture level, strategic,
segment or capability, and can be stand-alone or part of a larger effort
(GUIDE:architecture-project-management §2.1). It is usually divided into stages planned in
detail just before they start, and the lifecycle is start-up, planning, planning a stage,
execute-monitor-control a stage, ending a stage, and closing with handover; each iteration of
the ADM can be a stage, and a stage need not equal a phase
(GUIDE:architecture-project-management §2.2).

The guide's concept table is a source of exam traps. The Executive is the owner of the business
goal, comparable to the Architecture Sponsor. "Phase" is reserved for ADM phases and "stage"
for project phases. "Scope" in project management means the scope of work, broader than the
Phase A Define Scope step, which limits the scope of the *architecture*. "Work package" in TOGAF
is a change initiative that may be a whole programme, while in PRINCE2 and PMBOK it is the
lowest unit of project work, so the guide says "Project Work Package" for the latter. Risk in
TOGAF is a threat of the transformation to the technical environment and compliance, while
the project methods also count risk to the project's own timeline, budget and quality
(GUIDE:architecture-project-management §2.3). Project management is communication; the
artefacts should be written down, even as email, so that decisions can be traced
(GUIDE:architecture-project-management §2.4).

Start-up maps the ADM's brief "Establish the Architecture Project" step to PRINCE2's Starting
up a Project and PMBOK's Develop Project Charter: appoint the Executive and Project Manager,
capture previous lessons, prepare an outline business case, select the approach, appoint the
team, assemble the brief, define the management approach
(GUIDE:architecture-project-management §3.1). Phase A maps to PRINCE2 Starting up and
Initiation, with the Statement of Architecture Work becoming part of the Project Initiation
Documentation (GUIDE:architecture-project-management §4.1.1), and Phases B to F are PRINCE2
work delivery stages planned under Managing Stage Boundary, controlled under Controlling a
Stage and delivered under Managing Product Delivery
(GUIDE:architecture-project-management §4.1.2). PMBOK maps Phase A to the initiating and
planning process groups, B to F to delivery, and closing to the last step of Phase F
(GUIDE:architecture-project-management §5). The Project Manager can be an Enterprise
Architect or a project management professional (GUIDE:architecture-project-management §2.3).

**Trap.** The Architecture Project does not include Phase G. An answer that plans
implementation inside the architecture project's stages has merged two different endeavours
(GUIDE:architecture-project-management §2.1).

<figure class="my-4">
<svg viewBox="0 0 760 280" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="11" role="img" aria-label="An Architecture Project spans Phases A to F and Requirements Management, excluding Preliminary, G and H; its lifecycle stages map to PRINCE2 and PMBOK process groups">
<defs><marker id="arr-g7p" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
<rect x="15" y="20" width="80" height="44" rx="6" fill="#f1f1f1" stroke="#999"/>
<text x="55" y="38" text-anchor="middle">Preliminary</text><text x="55" y="54" text-anchor="middle" font-size="10">capability</text>
<rect x="110" y="12" width="470" height="60" rx="10" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="345" y="30" text-anchor="middle" font-weight="bold">Architecture Project: Phases A to F and Requirements Management (§2.1)</text>
<g fill="#fff" stroke="#7aa2e3">
<rect x="120" y="38" width="60" height="26" rx="4"/><rect x="190" y="38" width="60" height="26" rx="4"/><rect x="260" y="38" width="60" height="26" rx="4"/><rect x="330" y="38" width="60" height="26" rx="4"/><rect x="400" y="38" width="60" height="26" rx="4"/><rect x="470" y="38" width="100" height="26" rx="4"/>
</g>
<text x="150" y="55" text-anchor="middle">A</text><text x="220" y="55" text-anchor="middle">B</text><text x="290" y="55" text-anchor="middle">C</text><text x="360" y="55" text-anchor="middle">D</text><text x="430" y="55" text-anchor="middle">E</text><text x="520" y="55" text-anchor="middle">F and handover</text>
<rect x="595" y="20" width="70" height="44" rx="6" fill="#f1f1f1" stroke="#999"/>
<text x="630" y="38" text-anchor="middle">G</text><text x="630" y="54" text-anchor="middle" font-size="10">separate</text>
<rect x="675" y="20" width="70" height="44" rx="6" fill="#f1f1f1" stroke="#999"/>
<text x="710" y="38" text-anchor="middle">H</text><text x="710" y="54" text-anchor="middle" font-size="10">operational</text>
<line x1="95" y1="42" x2="110" y2="42" stroke="#555" marker-end="url(#arr-g7p)"/>
<text x="102" y="80" text-anchor="middle" font-size="9" fill="#666">RfAW</text>
<line x1="580" y1="42" x2="595" y2="42" stroke="#555" marker-end="url(#arr-g7p)"/>
<g fill="#e3f5e1" stroke="#7fbf7a">
<rect x="15" y="110" width="140" height="40" rx="6"/><rect x="165" y="110" width="140" height="40" rx="6"/><rect x="315" y="110" width="140" height="40" rx="6"/><rect x="465" y="110" width="140" height="40" rx="6"/><rect x="615" y="110" width="130" height="40" rx="6"/>
</g>
<text x="85" y="127" text-anchor="middle" font-weight="bold">start-up</text><text x="85" y="142" text-anchor="middle" font-size="10">Executive, PM, brief</text>
<text x="235" y="127" text-anchor="middle" font-weight="bold">planning</text><text x="235" y="142" text-anchor="middle" font-size="10">scope, WBS, SoAW approval</text>
<text x="385" y="127" text-anchor="middle" font-weight="bold">plan a stage</text><text x="385" y="142" text-anchor="middle" font-size="10">just before it starts</text>
<text x="535" y="127" text-anchor="middle" font-weight="bold">execute, monitor, control</text><text x="535" y="142" text-anchor="middle" font-size="10">issues, risks, highlights</text>
<text x="680" y="127" text-anchor="middle" font-weight="bold">end stage, close</text><text x="680" y="142" text-anchor="middle" font-size="10">handover, lessons</text>
<line x1="155" y1="130" x2="165" y2="130" stroke="#555" marker-end="url(#arr-g7p)"/>
<line x1="305" y1="130" x2="315" y2="130" stroke="#555" marker-end="url(#arr-g7p)"/>
<line x1="455" y1="130" x2="465" y2="130" stroke="#555" marker-end="url(#arr-g7p)"/>
<line x1="605" y1="130" x2="615" y2="130" stroke="#555" marker-end="url(#arr-g7p)"/>
<path d="M535 150 L535 170 L385 170 L385 150" fill="none" stroke="#555" stroke-dasharray="4 3" marker-end="url(#arr-g7p)"/>
<text x="460" y="185" text-anchor="middle" font-size="10" fill="#666">next stage</text>
<text x="380" y="215" text-anchor="middle" fill="#345">PRINCE2: Starting up and Initiation for Phase A; B to F as work delivery stages (Managing Stage Boundary, Controlling a Stage, Managing Product Delivery) (§4)</text>
<text x="380" y="235" text-anchor="middle" fill="#345">PMBOK: initiating and planning for Phase A; delivery for B to F; closing as the last step of Phase F (§5)</text>
<text x="380" y="265" text-anchor="middle" fill="#666">"stage" is a project section; "phase" is reserved for the ADM; "work package" means a change initiative in TOGAF (§2.3)</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">The Architecture Project's boundary, lifecycle and method mappings. Original drawing; section numbers refer to the Architecture Project Management guide.</figcaption>
</figure>

## Maturity models and skills, in one paragraph each

Capability Maturity Models describe the practices an organisation must perform, give a
yardstick to measure improvement, a framework to manage it, and organise practices into levels;
an assessment finds the current level and the practices with the best return
(GUIDE:architecture-maturity-models §1.2). The ACMM example has six levels, None, Initial, Under
Development, Defined, Managed, Measured, and nine elements from architecture process to IT
investment strategy, scored as a weighted mean and as a percentage per level per element
(GUIDE:architecture-maturity-models §2.2). Unit P9's second lesson works through the level
characteristics.

A skills framework defines the roles in a work area, the skills each needs and the depth
required; its value is fast identification of matches and gaps, and in EA it exists because
"Enterprise Architect" is used inconsistently (GUIDE:architecture-skills-framework §1.2). The
original framework lists seven skill categories, generic, business, EA, programme or project
management, IT general, technical IT, legal (GUIDE:architecture-skills-framework §4.3). The
Architecture Roles and Skills guide that supersedes it says a practice needs a clear mandate,
defined competencies, formal recognition and a development path
(GUIDE:architecture-roles-and-skills §3), describes Chief, Enterprise, Segment and Solution
Architect with activities, stakeholders and KPIs (GUIDE:architecture-roles-and-skills §4), and
rates eight categories at four levels, Background, Aware, Knowledgeable, Expert, per role
(GUIDE:architecture-roles-and-skills §5).

## Partitioning and the repository

The unit's name also lists partitioning and repository patterns, which live in the Fundamental
Content rather than a Series Guide. Architectures are partitioned because a single architecture
cannot address every need and because parallel teams, differing scope and different detail
create conflicts; partitioning by subject matter, time and level of detail, with teams and
governance aligned to the partitions, is decided in the Preliminary Phase (APPLY §4.1,
APPLY §4.2). The Architecture Repository is the framework's structure for the assets governance
uses, and its Governance Repository holds the decision log, compliance and capability
assessments, calendar, project portfolio and performance measurement (CONTENT §7.1,
CONTENT §7.5). The Series Guides on partitioning and repository patterns named in some syllabi
are not in this app's source store; the Fundamental Content sections above are the grounded
reference.

## How the 5, 3 and 1 differ

| Answer | Why it scores that |
|---|---|
| 5 | Scopes the Architecture Project as Phases A to F plus Requirements Management with a Request for Architecture Work as trigger, appoints an Executive and Project Manager, plans stages just before they start with Phase A mapped to initiation and B to F to delivery, assesses maturity per element to direct improvement, and defines roles with proficiency levels |
| 3 | Manages the work as a project but includes Phase G implementation in its stages, or reports one maturity level with no element breakdown |
| 1 | Treats "work package" in the project sense, or plans every stage in detail at the start; the guide plans each stage just before it begins (§2.2, §2.3) |
| 0 | Runs the architecture engagement with no project management at all because "the ADM is the method"; the standard says ADM cycles are conducted within the enterprise's project management framework (§3.1) |

## Where to look in the book

Architecture Project Management: §2.1 definition and exclusions, §2.2 lifecycle, §2.3 the
concept table, §3.1 start-up, §4 PRINCE2, §5 PMBOK. Architecture Maturity Models §1.2 and
§2.2. Architecture Skills Framework §1.2 and §4.3; Architecture Roles and Skills §3 to §5.
Applying the ADM §4 for partitioning; Architecture Content §7 for the repository.

## Check yourself

- Which three ADM phases are outside an Architecture Project, and why each?
- What does "work package" mean in TOGAF versus in PRINCE2 and PMBOK?
- Which PRINCE2 processes govern Phases B to F?
