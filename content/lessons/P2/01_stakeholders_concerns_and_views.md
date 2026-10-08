---
title: Stakeholders, concerns and the views that answer them
unit: P2
objectives: ["P2.1"]
refs: ["TECH §3.1", "TECH §3.2", "TECH §3.3.1", "TECH §3.3.4", "TECH §3.4", "CONTENT §3.1", "CONTENT §3.4.1", "ADM §3.3.2", "ADM §4.3.1", "GUIDE:adm-practitioners §3.3.1", "GUIDE:adm-practitioners §5.1"]
reading_minutes: 10
source: authored
status: draft
---
## What a stakeholder scenario looks like

The scenario plants a list of people: a sponsor, a business head with a fixed view, an
operations manager nobody invited, a regulator, a supplier, and usually one influencer with no
formal position. It then asks what you do with them. The five-point answer identifies the
*complete* set — formal and informal, visible and invisible — records their concerns, and
chooses the views that will let each of them verify that the architecture addresses those
concerns (TECH §3.3.1; CONTENT §3.1).

Stakeholder management is positioned by the standard as the discipline "successful architecture
practitioners can use to win support from others". The named benefits are the reasons the
scenario exists: powerful stakeholders found early shape the architecture and lend it
resources; early and frequent communication builds support; likely reactions can be anticipated
and planned for; and conflicting objectives surface early enough to be resolved (TECH §3.1).

## When and where

Stakeholder analysis is used during Phase A to identify the key players and is updated through
every phase, because new stakeholders appear as the engagement moves into Opportunities and
Solutions, Migration Planning and Change Management (TECH §3.2). In Phase A the step *Identify
Stakeholders, Concerns and Business Requirements* produces the stakeholder map, which feeds the
concerns and viewpoints recorded in the Architecture Vision, the starting list for the
Communications Plan, and the roles and responsibilities in the Statement of Architecture Work
(ADM §3.3.2).

**Trap.** Requirements discovered in Phase A that are inside the selected scope go into the
Architecture Requirements Specification; those outside it go to the Requirements Repository
through Requirements Management. A scenario that has the architect "park" an out-of-scope
stakeholder demand is testing this routing (ADM §3.3.2).

## Step 1 — identify, including the invisible team

The first task is to work out who the main stakeholders are: everyone affected, everyone with
power or influence, everyone with an interest in success or failure — executives, project and
client roles, developers, partners, suppliers, operations, customers. The standard warns against
relying on the formal organisation: informal groups may be just as powerful, and influencers —
well respected, on the important committees, not necessarily in a position of power — must be
found. Communicate with named people, not just organisations, and consider both the visible
team and the invisible team who must contribute but are not obviously associated with the
change (TECH §3.3.1).

The eight questions to ask are the ones the scenario answers for you if you read it closely:
who gains and who loses; who controls change management of processes; who designs new systems;
who makes the decisions; who procures and decides what to buy; who controls resources; who has
the specialist skills; who has influence (TECH §3.3.1).

<figure class="my-4">
<svg viewBox="0 0 760 250" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="11" role="img" aria-label="From a stakeholder to a view: a stakeholder has concerns; a viewpoint is the convention for a kind of view that addresses those concerns; a view built from architecture models lets the stakeholder verify the concern is addressed">
<defs><marker id="arr-p2-01a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
<text x="380" y="20" text-anchor="middle" font-size="12" font-weight="bold">From stakeholder to view</text>
<rect x="20" y="50" width="160" height="70" rx="6" fill="#e3f0fb" stroke="#4a7fb5"/>
<text x="100" y="74" text-anchor="middle" font-weight="bold">Stakeholder</text>
<text x="100" y="92" text-anchor="middle" font-size="10">individual, team, organisation</text>
<text x="100" y="106" text-anchor="middle" font-size="10">or class with an interest</text>
<line x1="180" y1="85" x2="210" y2="85" stroke="#555" marker-end="url(#arr-p2-01a)"/>
<text x="195" y="78" text-anchor="middle" font-size="9">has</text>
<rect x="212" y="50" width="160" height="70" rx="6" fill="#e3f0fb" stroke="#4a7fb5"/>
<text x="292" y="74" text-anchor="middle" font-weight="bold">Concern</text>
<text x="292" y="92" text-anchor="middle" font-size="10">an interest relevant to them:</text>
<text x="292" y="106" text-anchor="middle" font-size="10">performance, security, cost, evolvability</text>
<line x1="372" y1="85" x2="402" y2="85" stroke="#555" marker-end="url(#arr-p2-01a)"/>
<text x="387" y="78" text-anchor="middle" font-size="9">framed by</text>
<rect x="404" y="50" width="160" height="70" rx="6" fill="#fff1d6" stroke="#e0b060"/>
<text x="484" y="74" text-anchor="middle" font-weight="bold">Viewpoint</text>
<text x="484" y="92" text-anchor="middle" font-size="10">where you look from: generic,</text>
<text x="484" y="106" text-anchor="middle" font-size="10">re-usable, kept in a library</text>
<line x1="564" y1="85" x2="594" y2="85" stroke="#555" marker-end="url(#arr-p2-01a)"/>
<text x="579" y="78" text-anchor="middle" font-size="9">governs</text>
<rect x="596" y="50" width="144" height="70" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/>
<text x="668" y="74" text-anchor="middle" font-weight="bold">View</text>
<text x="668" y="92" text-anchor="middle" font-size="10">what you see: specific to</text>
<text x="668" y="106" text-anchor="middle" font-size="10">this architecture</text>
<rect x="212" y="150" width="352" height="44" rx="6" fill="#f1f1f1" stroke="#999"/>
<text x="388" y="168" text-anchor="middle">Architecture models (one or more, possibly different tools)</text>
<text x="388" y="184" text-anchor="middle" font-size="10">a view is selected parts of one or more models</text>
<line x1="388" y1="150" x2="620" y2="122" stroke="#555" marker-end="url(#arr-p2-01a)"/>
<rect x="20" y="212" width="720" height="28" rx="6" fill="#fff" stroke="#666"/>
<text x="380" y="230" text-anchor="middle" font-size="10">Test: can the stakeholder verify from the view that their concern is addressed? If not, the view — not the stakeholder — is wrong.</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">Original drawing. Definitions follow CONTENT §3.1 (stakeholder, concern, view, viewpoint, model; "a view is what you see, a viewpoint is where you are looking from"); the test follows GUIDE:adm-practitioners §3.3.1.</figcaption>
</figure>

## Concern, viewpoint, view

The vocabulary is precise and the exam expects it. A *concern* is an interest in the system
relevant to one or more stakeholders — performance, reliability, security, evolvability — and it
may determine acceptability. An *architecture view* is a representation from the perspective of
a related set of concerns, built from one or more models. An *architecture viewpoint* is the
specification of the conventions for a kind of view: generic, re-usable, stored in a viewpoint
library in the Reference Library. A view is what you see; a viewpoint is where you look from
(CONTENT §3.1).

The pilot and the air-traffic controller share one system but hold different concerns
(passengers and fuel versus other aircraft); each viewpoint constrains what its holder sees, and
the two overlap only in the shared model of location and vectors that safety depends on. Neither
view describes the whole system, and neither is wrong (CONTENT §3.4.1).

The Practitioners' Approach narrows the working definition for governance: a stakeholder is
someone with approval rights over the target and decision rights over the implementation's
suitability; a concern is a consistent set of subjects that consolidates requirements; a view
demonstrates how the architecture addresses the concern — not that the stakeholder should be
happy. Most requirements cluster into six to nine concern topics derived from strategy, such as
agility, efficiency, IT complexity or customer journey, and high-functioning teams keep a
viewpoint library for the questions they are expected to answer (GUIDE:adm-practitioners §3.3.1).

## Step 4 — tailor the deliverables to the stakeholder

Identify the catalogs, matrices and diagrams the engagement must produce and validate with each
stakeholder group, so that the architecture can be communicated to, and understood by, all of
them and they can verify that their concerns are addressed (TECH §3.3.4). The template
stakeholder map does this for a typical project: CxOs get the Business Footprint and
Goal/Objective/Business Service diagrams; Procurement gets the Technology Portfolio and
Standards catalogs; Enterprise Security gets Data Security and Data Dissemination diagrams;
Regulators get the Business Footprint and Application Communication diagrams; HR gets the
Organization Decomposition diagram and Organization/Actor and Location catalogs (TECH §3.4).

That is also why the first step of Phases B, C and D is *select viewpoints*: to select one you
must know the stakeholder and the concern, and any information not needed to address a concern
should not be gathered (ADM §4.3.1; GUIDE:adm-practitioners §5.1).

## How the 5-point answer differs from the 3-point one

| Points | What the answer does |
|---|---|
| 5 | Finds the missing stakeholder (informal, invisible, external), records concerns per stakeholder, selects viewpoints that address them, tailors the artefacts per group, and routes out-of-scope requirements to the Repository |
| 3 | Covers the formal stakeholders and their concerns but produces one generic set of diagrams for everyone, or omits the invisible team |
| 1 | Builds all the models first and presents them to whoever asks |
| 0 | Treats the loudest stakeholder's position as the requirement, or treats a concern as something to be "sold" rather than addressed |

## Where to look in the book

ADM Techniques §3.1 (benefits), §3.2 (Phase A, updated every phase), §3.3.1 (identify: the
eight questions, influencers, visible and invisible teams), §3.3.4 (tailor deliverables), §3.4
(template stakeholder map with artefacts per class). Architecture Content §3.1 (stakeholder,
concern, view, viewpoint, model) and §3.4.1 (the airport example). ADM §3.3.2 (the Phase A step
and where its products go). Practitioners' Approach §3.3.1 (the pragmatic definitions and the
six-to-nine concern topics).
