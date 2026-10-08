---
title: Gap analysis and building blocks — from baseline-to-target gaps to candidate roadmap components
unit: P4
objectives: ["P4.2"]
refs: ["TECH §5.1", "TECH §5.2", "ADM §4.3.4", "ADM §4.3.5", "ADM §4.5.3", "ADM §8.3.3", "CONTENT §5.2.3", "CONTENT §5.2.4", "CONTENT §5.3.1", "CONTENT §5.3.2", "GUIDE:selecting-building-blocks §2", "GUIDE:selecting-building-blocks §3", "GUIDE:selecting-building-blocks §3.1", "GUIDE:selecting-building-blocks §3.4"]
reading_minutes: 10
source: authored
status: draft
---
## What a gap scenario looks like

The baseline and target for a domain exist. The scenario then plants something missing: a
service in the baseline that nobody carried into the target, a target capability with no
baseline counterpart, a stakeholder concern from Phase A that no model addresses, or a request
to "list what the projects will have to build". The five-point answer builds the gap matrix,
classifies each gap as correctly eliminated, accidentally omitted or new, turns the new and
reinstated items into candidate roadmap components for Phase E, and keeps the distinction
between an Architecture Building Block and a Solution Building Block (TECH §5.2; ADM §4.3.5;
CONTENT §5.2.3).

## What counts as a gap

Gap analysis validates an architecture by highlighting the shortfall between baseline and
target: items deliberately omitted, accidentally left out, or not yet defined. The most critical
source of gaps is stakeholder concerns not addressed in prior architecture work. Sources include
business gaps (people, process, tools, information, measurement, financial, facilities), data
gaps (currency, location, availability, not created or consumed, relationships), and
applications and technologies impacted, eliminated or created (TECH §5.1).

Inside the ADM step, gap analysis is preceded by verification: perform trade-off analysis to
resolve conflicts among views, validate that models support the principles, objectives and
constraints, note changes to viewpoints selected from the Repository, and test the models for
completeness against requirements — then identify the baseline-to-target gaps with the
technique (ADM §4.3.4). Heat-mapping the capability map is the Phase B expression of the same
idea: a gap is only relevant in the context of the business need, and it provides focus for more
mapping now or priorities later (ADM §4.5.3).

## The matrix, step by step

Draw a matrix with the baseline ABBs down the vertical axis and the target ABBs across the
horizontal axis. Add a final row "New" to the baseline axis and a final column "Eliminated" to
the target axis. Where an ABB is in both, mark the cell "Included". Where a baseline ABB is
missing from the target, review it: if correctly eliminated, mark it so in the Eliminated cell;
if not, an accidental omission has been found and the ABB is reinstated in the next iteration.
Where a target ABB has no baseline counterpart, mark it in the New row as a gap to be filled by
developing or procuring the building block. Everything under Eliminated or New is a gap that is
either explained or marked to be addressed (TECH §5.2).

<figure class="my-4">
<svg viewBox="0 0 760 330" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="10" role="img" aria-label="An original gap analysis matrix: baseline building blocks down the left including a final New row, target building blocks across the top including a final Eliminated column; Included cells where a block is in both, an Eliminated cell marked correctly eliminated, one marked accidental omission to reinstate, and New-row cells marked as gaps to develop or procure">
<defs><marker id="arr-p4-03a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
<text x="380" y="18" text-anchor="middle" font-size="12" font-weight="bold">The gap matrix (customer-service example, invented)</text>
<rect x="150" y="34" width="120" height="30" fill="#f1f1f1" stroke="#999"/><text x="210" y="53" text-anchor="middle" font-size="9">Target: Case mgmt</text>
<rect x="270" y="34" width="120" height="30" fill="#f1f1f1" stroke="#999"/><text x="330" y="53" text-anchor="middle" font-size="9">Target: Self-service portal</text>
<rect x="390" y="34" width="120" height="30" fill="#f1f1f1" stroke="#999"/><text x="450" y="53" text-anchor="middle" font-size="9">Target: Identity service</text>
<rect x="510" y="34" width="120" height="30" fill="#fde8e6" stroke="#c0392b"/><text x="570" y="53" text-anchor="middle" font-size="9" font-weight="bold">Eliminated</text>
<rect x="20" y="64" width="130" height="40" fill="#f1f1f1" stroke="#999"/><text x="85" y="88" text-anchor="middle" font-size="9">Baseline: Case mgmt</text>
<rect x="150" y="64" width="120" height="40" fill="#e3f5e1" stroke="#999"/><text x="210" y="88" text-anchor="middle" font-size="9">Included</text>
<rect x="270" y="64" width="120" height="40" fill="#fff" stroke="#999"/>
<rect x="390" y="64" width="120" height="40" fill="#fff" stroke="#999"/>
<rect x="510" y="64" width="120" height="40" fill="#fff" stroke="#999"/>
<rect x="20" y="104" width="130" height="40" fill="#f1f1f1" stroke="#999"/><text x="85" y="128" text-anchor="middle" font-size="9">Baseline: Fax intake</text>
<rect x="150" y="104" width="120" height="40" fill="#fff" stroke="#999"/>
<rect x="270" y="104" width="120" height="40" fill="#fff" stroke="#999"/>
<rect x="390" y="104" width="120" height="40" fill="#fff" stroke="#999"/>
<rect x="510" y="104" width="120" height="40" fill="#e3f5e1" stroke="#999"/><text x="570" y="122" text-anchor="middle" font-size="9">Correctly</text><text x="570" y="134" text-anchor="middle" font-size="9">eliminated</text>
<rect x="20" y="144" width="130" height="40" fill="#f1f1f1" stroke="#999"/><text x="85" y="162" text-anchor="middle" font-size="9">Baseline: Complaint</text><text x="85" y="174" text-anchor="middle" font-size="9">escalation</text>
<rect x="150" y="144" width="120" height="40" fill="#fff" stroke="#999"/>
<rect x="270" y="144" width="120" height="40" fill="#fff" stroke="#999"/>
<rect x="390" y="144" width="120" height="40" fill="#fff" stroke="#999"/>
<rect x="510" y="144" width="120" height="40" fill="#fff1d6" stroke="#e0b060"/><text x="570" y="162" text-anchor="middle" font-size="9">Accidental omission —</text><text x="570" y="174" text-anchor="middle" font-size="9">reinstate next iteration</text>
<rect x="20" y="184" width="130" height="40" fill="#fde8e6" stroke="#c0392b"/><text x="85" y="208" text-anchor="middle" font-size="9" font-weight="bold">New</text>
<rect x="150" y="184" width="120" height="40" fill="#fff" stroke="#999"/>
<rect x="270" y="184" width="120" height="40" fill="#fff1d6" stroke="#e0b060"/><text x="330" y="202" text-anchor="middle" font-size="9">Gap: develop</text><text x="330" y="214" text-anchor="middle" font-size="9">or procure</text>
<rect x="390" y="184" width="120" height="40" fill="#fff1d6" stroke="#e0b060"/><text x="450" y="202" text-anchor="middle" font-size="9">Gap: develop</text><text x="450" y="214" text-anchor="middle" font-size="9">or procure</text>
<rect x="510" y="184" width="120" height="40" fill="#fff" stroke="#999"/>
<line x1="330" y1="224" x2="330" y2="250" stroke="#555" marker-end="url(#arr-p4-03a)"/>
<line x1="570" y1="184" x2="570" y2="250" stroke="#555" marker-end="url(#arr-p4-03a)"/>
<rect x="20" y="252" width="710" height="70" rx="6" fill="#fff" stroke="#666"/>
<text x="375" y="272" text-anchor="middle" font-weight="bold">Everything in the New row or the Eliminated column is a gap</text>
<text x="375" y="290" text-anchor="middle" font-size="9">explained as correctly eliminated, or marked to be addressed by reinstating, developing or procuring the building block</text>
<text x="375" y="308" text-anchor="middle" font-size="9">the addressed gaps become the domain's candidate roadmap components — raw material for the consolidated roadmap in Phase E</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">Original drawing with invented content. The matrix construction and the three outcomes follow TECH §5.2; the destination of the gaps follows ADM §4.3.5.</figcaption>
</figure>

## From gaps to candidate roadmap components

Following the baseline, target and gap results, a domain roadmap is required to prioritise
activities over the coming phases. This initial roadmap is "raw material" for the more detailed,
consolidated cross-discipline roadmap defined in Opportunities and Solutions (ADM §4.3.5).

**Trap.** Consolidating gaps, solutions and dependencies across all domains is Phase E's job.
An answer that produces the consolidated roadmap, work packages or Transition Architectures
inside Phase B, C or D has run ahead of the method (ADM §4.3.5).

## ABBs and SBBs

Architecture Building Blocks relate to the Architecture Continuum and are defined or selected
by applying the ADM. They capture architecture requirements — business, data, application and
technology — and direct and guide the development of SBBs. An ABB specification includes at
minimum: fundamental functionality and attributes (including security and manageability);
interfaces; interoperability and relationships with other building blocks; dependent building
blocks; and the map to business entities and policies (CONTENT §5.2.3). Solution Building Blocks
relate to the Solutions Continuum, may be procured or developed, define what products and
components implement the functionality, fulfil business requirements, and are product- or
vendor-aware; their specification adds the implemented interface set, mapping to the IT
topology, shared attributes, performance, design drivers and the relationships back to ABBs
(CONTENT §5.2.4).

An architecture is a set of building blocks in a model plus a specification of how they connect
to meet the business requirements. It need only contain the blocks relevant to the problem;
blocks may support several others or part of one; and they must conform to standards for their
type and the enterprise's principles. Design considers three classes — re-usable blocks such as
legacy items, blocks to be developed, and blocks to be purchased (COTS) — and uses the desired
level of integration to bind functions together, treating legacy elements as large blocks to
avoid breaking them apart (CONTENT §5.3.1). Definition proceeds gradually, mainly in Phases A to
D: identify the ABBs that meet the goals, then refine iteratively into a set of SBBs that can be
bought or built (CONTENT §5.3.2). In Phase D, conceptualising ABBs — functionality and how it may
be implemented, without configuration detail — is "a key process" in building the target
(ADM §8.3.3).

**Trap.** "Vendor-aware" is the tell. A building block named after a product is an SBB, and it
belongs to solution selection in Phase E, not to the target architecture of Phase B, C or D
(CONTENT §5.2.4).

## Choosing how much to specify: change profiles

The Series Guide on selecting building blocks adds a dial the exam can turn. Change comes in
three profiles: **rapid** (near-immediate implementation of simple components, prototyping),
**functional** (fast cycles of bounded capability, agile techniques) and **robust** (longer-term,
complex, risk- and architecture-driven, often interoperable across enterprises, run with
approaches such as COBIT, SABSA or PRINCE2). Most transitions are functional; some need speed;
some need care (GUIDE:selecting-building-blocks §2). Each profile has a starting set of
metamodel entities — the rapid set is minimal (location, requirement, work package, actor,
organisation unit, physical components), functional adds gap, principle, capability, value
stream, service, process, role, data entity, and robust adds assumption, policy and standard,
control, contract, event, function and the logical components (GUIDE:selecting-building-blocks §3).

The rapid profile creates SBBs to deliver working services quickly and may leave many ABBs out —
the executing solution "speaks for itself"; the robust profile creates ABBs first so that the
proposed architecture "speaks for itself" before anything is built, and whichever choice is
made, the reasons and implications are documented (GUIDE:selecting-building-blocks §3.1). Robust
change approaches the problem from a threat or risk perspective, avoids debt, carries significant
assurance activity, and explores every level of abstraction in detail — the profile for nuclear
control or aircraft systems (GUIDE:selecting-building-blocks §3.4).

## How the 5-point answer differs from the 3-point one

| Points | What the answer does |
|---|---|
| 5 | Verifies the models, builds the ABB matrix with New and Eliminated, explains or reinstates each eliminated block, marks new blocks to develop or procure, hands the results to Phase E as candidate roadmap components, keeps ABBs vendor-neutral, and sizes the specification to the change profile |
| 3 | Finds the new items but never reviews the eliminated column, so the accidental omission ships; or builds the matrix on SBBs |
| 1 | Consolidates a cross-domain roadmap and work packages inside Phase B |
| 0 | Treats a stakeholder concern with no model as "out of scope", or lets a vendor product stand as an ABB |

## Where to look in the book

ADM Techniques §5.1 (sources of gaps, stakeholder concerns first) and §5.2 (the matrix, step
by step). ADM §4.3.4 (verification then gaps), §4.3.5 (candidate roadmap components and Phase
E), §4.5.3 (heat maps as gap analysis), §8.3.3 (ABBs in Phase D). Architecture Content §5.2.3
(ABBs), §5.2.4 (SBBs), §5.3.1 (principles and the three classes), §5.3.2 (specification across
Phases A to D). Series Guide: An Approach to Selecting Building Blocks §2 (change profiles), §3
(entities per profile), §3.1, §3.4.
