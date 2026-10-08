---
title: Maturity models and the skills framework applied to an organisation
unit: P9
objectives: ["P9.1"]
refs: ["GUIDE:architecture-maturity-models §1.2", "GUIDE:architecture-maturity-models §1.3", "GUIDE:architecture-maturity-models §2.1", "GUIDE:architecture-maturity-models §2.2", "GUIDE:architecture-maturity-models §2.3", "GUIDE:architecture-maturity-models §3.1.3", "GUIDE:architecture-skills-framework §1.2", "GUIDE:architecture-skills-framework §3.1", "GUIDE:architecture-skills-framework §4.2", "GUIDE:architecture-skills-framework §4.3", "GUIDE:architecture-skills-framework §4.4", "GUIDE:architecture-skills-framework §6.2", "GUIDE:architecture-roles-and-skills §3", "GUIDE:architecture-roles-and-skills §4", "GUIDE:architecture-roles-and-skills §5", "TECH §7.3", "TECH §8.3"]
reading_minutes: 9
source: authored
status: draft
---
## What the scenario looks like

An enterprise wants to know how good its architecture practice is and what to fix first, or
it is hiring and cannot agree what an "Enterprise Architect" is. The maturity scenario asks
for an assessment and an improvement path; the skills scenario asks for role definitions,
proficiency levels and a development or certification programme. Both are governance
questions because the Architecture Board is responsible for improving the maturity level of
the architecture discipline, and because the Preliminary Phase sets up the team the skills
framework describes. The five-point answer assesses against a model and uses the result to
direct effort; the three-point answer assesses but does not act on the weakest elements; the
one-point answer sets a target level by decree; the zero-point answer hires by job title.

## Maturity models

Capability Maturity Models give an organisation a proven way to gain control over its change
processes: they describe the practices needed, provide a yardstick to measure improvement,
give a framework to manage the improvement and organise practices into levels; an
"assessment" against the model shows where the organisation stands and which practices give
the greatest improvement and return (GUIDE:architecture-maturity-models §1.2). The models
address the state of the architecture processes, the completeness of the description and the
organisation's buy-in, and the guide points to the skills framework as the closely related
tool for planning target skills (GUIDE:architecture-maturity-models §1.3).

The worked example is the US Department of Commerce ACMM, built to find weak areas and give a
defined evolutionary path; it has three sections: the maturity model, the characteristics of
operating units' processes at each level, and a scorecard used to derive the level reported
to the CIO (GUIDE:architecture-maturity-models §2.1). It has six levels and nine elements, and
two scoring methods, a weighted mean maturity level and the percentage achieved at each level
per element (GUIDE:architecture-maturity-models §2.2).

| Level | Name | The flavour of the characteristics |
|---|---|---|
| 0 | None | no EA programme |
| 1 | Initial | informal, ad hoc, localised; success depends on individuals; no explicit governance of standards |
| 2 | Under development | basic process documented, roles and responsibilities clear; vision, principles, baseline and target identified; TRM and standards profile established; governance of a few standards |
| 3 | Defined | detailed written procedures; gap analysis and migration plan done; integrated with capital planning; senior management supportive; explicit governance of most IT investments |
| 4 | Managed | part of the culture; quality metrics captured; senior management directly in the review process; explicit governance of all investments; variances fed back |
| 5 | Measured | continuous improvement; a standards and waivers process improves the process; every decision-maker uses the architecture documents; no unplanned IT investment (GUIDE:architecture-maturity-models §2.3) |

The nine elements are architecture process, architecture development, business linkage,
senior management involvement, operating unit participation, architecture communication, IT
security, Architecture Governance, and IT investment and acquisition strategy
(GUIDE:architecture-maturity-models §2.2). A scenario that reports "the architecture is
documented but the business units ignore it and investments bypass it" is describing low
scores on elements 5 and 9, which is where the improvement effort goes. CMMI and its SCAMPI
appraisal method are the broader family, used to identify strengths, weaknesses and ratings
against reference models (GUIDE:architecture-maturity-models §3.1.3). Maturity models also
reappear as the presentation vehicle for readiness factors (TECH §7.3) and as a source of risk
identification when the target state is not reached (TECH §8.3).

**Trap.** A maturity level is derived from an assessment against the model's characteristics,
not chosen; and the ACMM scores each of the nine elements, so "we are level 3" hides which
elements are dragging (GUIDE:architecture-maturity-models §2.2).

<figure class="my-4">
<svg viewBox="0 0 760 270" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="11" role="img" aria-label="Maturity as a ladder from level 0 None to level 5 Measured, scored across nine elements; the skills framework beside it lists roles, seven skill categories and four proficiency levels">
<defs><marker id="arr-p9m" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
<g fill="#e0ecff" stroke="#7aa2e3">
<rect x="20" y="220" width="90" height="28" rx="4"/>
<rect x="80" y="186" width="90" height="28" rx="4"/>
<rect x="140" y="152" width="90" height="28" rx="4"/>
<rect x="200" y="118" width="90" height="28" rx="4"/>
<rect x="260" y="84" width="90" height="28" rx="4"/>
<rect x="320" y="50" width="90" height="28" rx="4"/>
</g>
<text x="65" y="238" text-anchor="middle">0 None</text>
<text x="125" y="204" text-anchor="middle">1 Initial</text>
<text x="185" y="170" text-anchor="middle">2 Under dev.</text>
<text x="245" y="136" text-anchor="middle">3 Defined</text>
<text x="305" y="102" text-anchor="middle">4 Managed</text>
<text x="365" y="68" text-anchor="middle">5 Measured</text>
<text x="215" y="30" text-anchor="middle" font-weight="bold">ACMM: six levels, scored per element</text>
<text x="215" y="262" text-anchor="middle" fill="#666">nine elements: process, development, business linkage, senior mgmt, operating units, communication, IT security, governance, investment</text>
<rect x="450" y="20" width="295" height="230" rx="8" fill="#e3f5e1" stroke="#7fbf7a"/>
<text x="597" y="42" text-anchor="middle" font-weight="bold">Skills framework</text>
<text x="597" y="62" text-anchor="middle">roles: board members, sponsor, manager,</text>
<text x="597" y="76" text-anchor="middle">enterprise, business, data, application, technology</text>
<text x="597" y="90" text-anchor="middle">architects, programme and project managers,</text>
<text x="597" y="104" text-anchor="middle">IT designer, solution architect</text>
<text x="597" y="128" text-anchor="middle">seven skill categories: generic, business,</text>
<text x="597" y="142" text-anchor="middle">EA, programme or project mgmt, IT general,</text>
<text x="597" y="156" text-anchor="middle">technical IT, legal</text>
<text x="597" y="180" text-anchor="middle">four proficiency levels per skill per role</text>
<text x="597" y="204" text-anchor="middle">Roles and Skills guide: chief, enterprise,</text>
<text x="597" y="218" text-anchor="middle">segment, solution architect; eight categories;</text>
<text x="597" y="232" text-anchor="middle">background, aware, knowledgeable, expert</text>
<line x1="410" y1="130" x2="450" y2="130" stroke="#555" marker-end="url(#arr-p9m)"/>
<text x="430" y="120" text-anchor="middle" fill="#345">plan</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">The maturity ladder and the skills framework that plans the climb. Original drawing; the levels and elements follow GUIDE:architecture-maturity-models §2.2, the roles and categories the skills guides.</figcaption>
</figure>

## The skills framework

A skills framework defines the roles in a work area, the skills each role requires and the
depth of knowledge needed to fulfil it; its value is rapidly identifying skill matches and
gaps, and in EA it matters because the discipline is immature and its terms are inconsistently
used (GUIDE:architecture-skills-framework §1.2). An internal certification programme has three
purposes: define the competencies and align staff skills with the architecture tasks, formally
recognise practising architects, and provide a competency development path with a minimum
level (GUIDE:architecture-skills-framework §3.1). The roles in a typical team are Architecture
Board members, the Architecture Sponsor, the Architecture Manager, architects for enterprise,
business, data, application and technology, programme and project managers, IT designer and
Solution Architect (GUIDE:architecture-skills-framework §4.2). Skills fall into seven
categories, generic, business skills and methods, Enterprise Architecture, programme or
project management, IT general knowledge, technical IT and legal environment
(GUIDE:architecture-skills-framework §4.3), and each role needs one of four proficiency levels
in each skill (GUIDE:architecture-skills-framework §4.4).

The framework also separates the Enterprise Architect (landscape and reference-model level,
enterprise capabilities), the Segment Architect (a business problem or domain such as finance
or HR, re-using other architects' output, similar skills without whole-enterprise scope) and
the Solution Architect (system or subsystem level, more IT-centred, shielding the others from
product detail), with a lead Enterprise Architect managing a team of them
(GUIDE:architecture-skills-framework §6.2). The newer Architecture Roles and Skills guide,
which supersedes it, adds the Chief Architect as a special case, defines job, role and
assignment, lists activities, stakeholders and KPIs per role (GUIDE:architecture-roles-and-skills §4),
and rates eight skill categories on four levels, Background, Aware, Knowledgeable and Expert
(GUIDE:architecture-roles-and-skills §5). Setting up a practice needs a clear mandate,
defined competencies, formal recognition and a development path, and the benefit is simpler
recruiting, consistent assignment decisions, self-assessment and a career path
(GUIDE:architecture-roles-and-skills §3).

**Trap.** "Enterprise Architect" and "Solution Architect" are different roles with different
skill profiles; a scenario hiring a "senior architect" to own the landscape and also design a
product's integration is asking for two roles (GUIDE:architecture-skills-framework §6.2).

## How the 5, 3 and 1 differ

| Answer | Why it scores that |
|---|---|
| 5 | Assesses the practice against a maturity model element by element, targets the weakest elements for improvement with a yardstick to re-measure, and uses the skills framework to define the roles, required proficiency levels and a certification and development path that closes the gaps |
| 3 | Assesses and reports a single level, but the improvement plan is generic, or defines roles without proficiency levels, so nothing can be measured or matched (GUIDE:architecture-maturity-models §2.2, GUIDE:architecture-skills-framework §4.4) |
| 1 | Declares a target level and a hiring plan by job title; levels are derived from assessment, and titles are exactly the ambiguity the framework exists to remove (GUIDE:architecture-skills-framework §1.2) |
| 0 | Treats maturity and skills as HR matters outside architecture governance; the board is responsible for improving the maturity of the discipline (GOV §4.2) |

## Where to look in the book

Architecture Maturity Models: §1.2 for what CMMs give you, §2.2 for the six levels and nine
elements, §2.3 for the characteristics per level, §3.1.3 for SCAMPI. Architecture Skills
Framework: §3.1 purposes of certification, §4.2 roles, §4.3 categories, §4.4 levels, §6.2 the
three architect types. Architecture Roles and Skills: §3 for setting up a practice, §4 for
the four roles, §5 for the eight categories and four proficiency levels. ADM Techniques §7.3
and §8.3 for maturity models in readiness and risk.

## Check yourself

- Name the six ACMM levels in order.
- Which nine elements are scored?
- What are the four proficiency levels in the Roles and Skills guide?
