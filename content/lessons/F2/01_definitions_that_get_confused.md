---
title: The definitions the exam tests, and the pairs it confuses
unit: F2
objectives: ["2.1", "2.2"]
refs: ["INTRO §3"]
reading_minutes: 8
source: authored
status: draft
---
## How Part 1 asks definitions

Three of forty questions are pure recall from the *Definitions* chapter, and many more depend on
it. The glossary page carries every term as a flashcard; this lesson is the map of the pairs
that lose marks.

| Confusable pair | The difference in one line |
|---|---|
| **View / viewpoint** | a viewpoint is the template (the conventions); a view is the instance built with it |
| **Stakeholder / concern** | a stakeholder is the person or group; a concern is their interest in the system |
| **Artifact / deliverable / building block** | one aspect; a signed-off container; a reusable component |
| **Architecture Vision / Architecture Definition Document** | Phase A's aspirational summary for the sponsor; the B–D container of the full description |
| **Enterprise Continuum / Architecture Repository** | a way of *classifying* assets from generic to specific; the *store* that holds them |
| **Architecture Continuum / Solutions Continuum** | the same classification applied to ABBs and to SBBs respectively |
| **Baseline / Target / Transition Architecture** | where you are; where you are going; a significant state in between with business value of its own |
| **Request for Architecture Work / Statement of Architecture Work** | the sponsor's trigger, an input to Phase A; the architect's proposal, Phase A's output |
| **Architecture Roadmap / Implementation and Migration Plan** | the work packages on a timeline; the schedule of projects that delivers them |
| **Segment / Strategic / Capability Architecture** | programme level; executive summary level; project level of the Architecture Landscape |

<figure class="my-4">
<svg viewBox="0 0 760 345" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="Four confusable pairs as side-by-side cards: view and viewpoint, stakeholder and concern, Request and Statement of Architecture Work, Roadmap and Implementation and Migration Plan">
  <defs><marker id="arr-f2-01a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
  <rect x="10" y="10" width="360" height="155" rx="8" fill="#e0ecff" stroke="#7aa2e3"/>
  <text x="190.0" y="28" text-anchor="middle" font-size="11" font-weight="bold">View / viewpoint</text>
  <rect x="20" y="42" width="165" height="110" rx="6" fill="#fff" stroke="#666"/>
  <text x="102.5" y="72.85" text-anchor="middle" font-size="11" font-weight="bold">View</text>
  <text x="102.5" y="86.85" text-anchor="middle" font-size="11" fill="#345">the instance: the system</text>
  <text x="102.5" y="100.85" text-anchor="middle" font-size="11" fill="#345">seen from one set of</text>
  <text x="102.5" y="114.85" text-anchor="middle" font-size="11" fill="#345">concerns; specific to</text>
  <text x="102.5" y="128.85" text-anchor="middle" font-size="11" fill="#345">one architecture</text>
  <text x="190" y="102" text-anchor="middle" font-size="11" font-weight="bold" fill="#666">vs</text>
  <rect x="195" y="42" width="165" height="110" rx="6" fill="#fff" stroke="#666"/>
  <text x="277.5" y="72.85" text-anchor="middle" font-size="11" font-weight="bold">Viewpoint</text>
  <text x="277.5" y="86.85" text-anchor="middle" font-size="11" fill="#345">the template: conventions</text>
  <text x="277.5" y="100.85" text-anchor="middle" font-size="11" fill="#345">for a kind of view, its</text>
  <text x="277.5" y="114.85" text-anchor="middle" font-size="11" fill="#345">definition or schema;</text>
  <text x="277.5" y="128.85" text-anchor="middle" font-size="11" fill="#345">reusable</text>
  <rect x="390" y="10" width="360" height="155" rx="8" fill="#e3f5e1" stroke="#7fbf7a"/>
  <text x="570.0" y="28" text-anchor="middle" font-size="11" font-weight="bold">Stakeholder / concern</text>
  <rect x="400" y="42" width="165" height="110" rx="6" fill="#fff" stroke="#666"/>
  <text x="482.5" y="79.85" text-anchor="middle" font-size="11" font-weight="bold">Stakeholder</text>
  <text x="482.5" y="93.85" text-anchor="middle" font-size="11" fill="#345">the person, team or</text>
  <text x="482.5" y="107.85" text-anchor="middle" font-size="11" fill="#345">class of them with an</text>
  <text x="482.5" y="121.85" text-anchor="middle" font-size="11" fill="#345">interest in the system</text>
  <text x="570" y="102" text-anchor="middle" font-size="11" font-weight="bold" fill="#666">vs</text>
  <rect x="575" y="42" width="165" height="110" rx="6" fill="#fff" stroke="#666"/>
  <text x="657.5" y="79.85" text-anchor="middle" font-size="11" font-weight="bold">Concern</text>
  <text x="657.5" y="93.85" text-anchor="middle" font-size="11" fill="#345">the interest itself:</text>
  <text x="657.5" y="107.85" text-anchor="middle" font-size="11" fill="#345">performance, security,</text>
  <text x="657.5" y="121.85" text-anchor="middle" font-size="11" fill="#345">cost, evolvability</text>
  <rect x="10" y="175" width="360" height="155" rx="8" fill="#fff1d6" stroke="#e0b060"/>
  <text x="190.0" y="193" text-anchor="middle" font-size="11" font-weight="bold">Request for Architecture Work / Statement of Architecture Work</text>
  <rect x="20" y="207" width="165" height="110" rx="6" fill="#fff" stroke="#666"/>
  <text x="102.5" y="244.85" text-anchor="middle" font-size="11" font-weight="bold">Request for Architecture Work</text>
  <text x="102.5" y="258.85" text-anchor="middle" font-size="11" fill="#345">the sponsor's trigger,</text>
  <text x="102.5" y="272.85" text-anchor="middle" font-size="11" fill="#345">sent to the architects;</text>
  <text x="102.5" y="286.85" text-anchor="middle" font-size="11" fill="#345">an input to Phase A</text>
  <text x="190" y="267" text-anchor="middle" font-size="11" font-weight="bold" fill="#666">vs</text>
  <rect x="195" y="207" width="165" height="110" rx="6" fill="#fff" stroke="#666"/>
  <text x="277.5" y="244.85" text-anchor="middle" font-size="11" font-weight="bold">Statement of Architecture Work</text>
  <text x="277.5" y="258.85" text-anchor="middle" font-size="11" fill="#345">the architect's proposal:</text>
  <text x="277.5" y="272.85" text-anchor="middle" font-size="11" fill="#345">scope and approach;</text>
  <text x="277.5" y="286.85" text-anchor="middle" font-size="11" fill="#345">Phase A's output</text>
  <rect x="390" y="175" width="360" height="155" rx="8" fill="#f3e3f7" stroke="#b58ac9"/>
  <text x="570.0" y="193" text-anchor="middle" font-size="11" font-weight="bold">Architecture Roadmap / Implementation and Migration Plan</text>
  <rect x="400" y="207" width="165" height="110" rx="6" fill="#fff" stroke="#666"/>
  <text x="482.5" y="244.85" text-anchor="middle" font-size="11" font-weight="bold">Architecture Roadmap</text>
  <text x="482.5" y="258.85" text-anchor="middle" font-size="11" fill="#345">the work packages laid</text>
  <text x="482.5" y="272.85" text-anchor="middle" font-size="11" fill="#345">on a timeline from</text>
  <text x="482.5" y="286.85" text-anchor="middle" font-size="11" fill="#345">Baseline to Target</text>
  <text x="570" y="267" text-anchor="middle" font-size="11" font-weight="bold" fill="#666">vs</text>
  <rect x="575" y="207" width="165" height="110" rx="6" fill="#fff" stroke="#666"/>
  <text x="657.5" y="244.85" text-anchor="middle" font-size="11" font-weight="bold">Implementation and Migration Plan</text>
  <text x="657.5" y="258.85" text-anchor="middle" font-size="11" fill="#345">the schedule of projects,</text>
  <text x="657.5" y="272.85" text-anchor="middle" font-size="11" fill="#345">grouped in portfolios and</text>
  <text x="657.5" y="286.85" text-anchor="middle" font-size="11" fill="#345">programmes, that delivers them</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">The four pairs that lose the most marks, side by side. Original drawing; the terms follow INTRO §3.</figcaption>
</figure>

## Terms with a precise TOGAF meaning

- **Capability**: an ability an organisation, person or system possesses. Requires people,
  process and technology together.
- **Value stream**: an end-to-end collection of value-adding activities producing a result for
  a customer or stakeholder.
- **Work package**: a set of actions to achieve one or more objectives; can be part of a
  project, a project, or a programme.
- **Metamodel**: a model of how the architecture will be described: the entity types and their
  relationships.
- **Gap**: a difference between Baseline and Target found by gap analysis; a gap can be a new
  thing, an eliminated thing, or a thing that must change.

<figure class="my-4">
<svg viewBox="0 0 760 170" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="Three precise terms drawn: a capability as people, process and technology; a work package at three sizes; the three kinds of gap">
  <defs><marker id="arr-f2-01b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
  <rect x="10" y="10" width="235" height="150" rx="8" fill="#e0ecff" stroke="#7aa2e3"/>
  <text x="127.5" y="28" text-anchor="middle" font-size="12" font-weight="bold">Capability: an ability possessed</text>
  <rect x="22" y="45" width="68" height="34" rx="6" fill="#fff" stroke="#666"/>
  <text x="56" y="65.85" text-anchor="middle" font-size="11" fill="#345">people</text>
  <rect x="96" y="45" width="68" height="34" rx="6" fill="#fff" stroke="#666"/>
  <text x="130" y="65.85" text-anchor="middle" font-size="11" fill="#345">process</text>
  <rect x="170" y="45" width="68" height="34" rx="6" fill="#fff" stroke="#666"/>
  <text x="204" y="65.85" text-anchor="middle" font-size="11" fill="#345">technology</text>
  <text x="127" y="105" text-anchor="middle" font-size="11" fill="#345">all three together;</text>
  <text x="127" y="120" text-anchor="middle" font-size="11" fill="#345">remove one and the ability goes</text>
  <rect x="262" y="10" width="235" height="150" rx="8" fill="#e3f5e1" stroke="#7fbf7a"/>
  <text x="379.5" y="28" text-anchor="middle" font-size="12" font-weight="bold">Work package: a set of actions</text>
  <rect x="275" y="42" width="210" height="100" rx="6" fill="#f4f4f4" stroke="#bbb" stroke-dasharray="5 4"/>
  <text x="380" y="95.85" text-anchor="middle" font-size="11" fill="#345">a programme</text>
  <rect x="290" y="62" width="180" height="66" rx="6" fill="#fff" stroke="#666" stroke-dasharray="5 4"/>
  <text x="380" y="98.85" text-anchor="middle" font-size="11" fill="#345">a project</text>
  <rect x="305" y="82" width="150" height="34" rx="6" fill="#fff" stroke="#666"/>
  <text x="380" y="102.85" text-anchor="middle" font-size="11" fill="#345">part of a project</text>
  <text x="380" y="152" text-anchor="middle" font-size="10" fill="#345">any of the three sizes</text>
  <rect x="514" y="10" width="236" height="150" rx="8" fill="#fff1d6" stroke="#e0b060"/>
  <text x="632.0" y="28" text-anchor="middle" font-size="12" font-weight="bold">Gap: Baseline versus Target</text>
  <rect x="526" y="45" width="212" height="28" rx="6" fill="#fff" stroke="#666"/>
  <text x="632" y="62.85" text-anchor="middle" font-size="11" fill="#345">new: in Target, not in Baseline</text>
  <rect x="526" y="80" width="212" height="28" rx="6" fill="#fff" stroke="#666"/>
  <text x="632" y="97.85" text-anchor="middle" font-size="11" fill="#345">eliminated: in Baseline, not Target</text>
  <rect x="526" y="115" width="212" height="28" rx="6" fill="#fff" stroke="#666"/>
  <text x="632" y="132.85" text-anchor="middle" font-size="11" fill="#345">changed: in both, but different</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">Three terms with a precise meaning. Original drawing; the definitions follow INTRO §3.</figcaption>
</figure>
