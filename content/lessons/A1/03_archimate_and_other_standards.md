---
title: "ArchiMate beside TOGAF, BIZBOK, BPMN, UML and BMM"
unit: A1
objectives: ["A1.3"]
refs: ["ARCHIMATE §D.1", "ARCHIMATE §D.2", "ARCHIMATE §D.3", "ARCHIMATE §D.4", "ARCHIMATE §D.5", "ARCHIMATE §D.6", "ARCHIMATE §3.6"]
reading_minutes: 8
source: authored
status: draft
---
## ArchiMate and the TOGAF framework

The two standards are complementary, not competing: TOGAF defines an architecture *development
process* (the ADM) and ArchiMate defines a *modelling language*. The language supplies a
vendor-neutral set of concepts and a notation for the consistent, integrated model "below the
waterline" that TOGAF views are then drawn from (ARCHIMATE §D.1).

The correspondence is structural. The three core layers map closely onto the three main
architectures of the ADM — Business Architecture (Phase B), Information Systems Architecture
(Phase C, covering data and application) and Technology Architecture (Phase D). The strategy,
motivation, and implementation & migration elements map approximately onto the rest of the cycle —
Phase A and Requirements Management for motivation and strategy, Phases E–G for implementation and
migration — though they may be used in Phases B–D as well (ARCHIMATE §D.1).

<figure class="max-w-lg"><img src="/figure/ARCHIMATE:fig-116" alt="Correspondence between the ArchiMate language and the TOGAF ADM" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 116. Correspondence Between the ArchiMate Language and the TOGAF ADM (ARCHIMATE)</figcaption></figure>

Viewpoints are where the two overlap most and differ most. Both use the ISO 42010 vocabulary of
views and viewpoints and both assume a common repository of models. But ArchiMate is a language,
so its viewpoint definitions are precise — stakeholders, concerns, abstraction level, permitted
element types — while TOGAF describes viewpoints more generally. There is no one-to-one mapping;
some TOGAF viewpoints need interpretation, and the ArchiMate viewpoint mechanism can be used to
define TOGAF-style viewpoints out of ArchiMate concepts (ARCHIMATE §D.1).

| Claim | TOGAF | ArchiMate |
|---|---|---|
| What it standardizes | a process (ADM) plus content framework | a modelling language plus notation |
| Views and viewpoints | ISO 42010 sense, described generally | ISO 42010 sense, defined precisely |
| Repository | yes | yes — the common foundation |
| Combined use | supports better stakeholder communication | (same) |

**Trap:** "ArchiMate is a framework" — no, the specification reiterates that it is a *modelling
language and not a framework* (ARCHIMATE §D.1). Building blocks (ABBs/SBBs) are typically modelled
with the Grouping element (ARCHIMATE §3.6).

## BIZBOK

The BIZBOK Guide's core Business Architecture domains — capabilities, value streams, organization
and information — are covered directly by the strategy elements and the Business Layer, and its
other domains (stakeholders, strategies, policies, products, initiatives, metrics) also have
natural ArchiMate counterparts. Capability mapping, organization mapping, information mapping and
value-stream mapping are all supported, including cross-mappings such as value stream to capability.
BIZBOK-style value streams, where stages produce value items aggregated into a value proposition
with explicit entry and exit conditions, are modelled with aggregation for the value items and
constraints for the conditions (ARCHIMATE §D.2).

## The "umbrella" idea

ArchiMate deliberately *overlaps* with other languages. Shared concepts act as bridges, so an
ArchiMate model is a high-level umbrella tying together detailed models — a BPMN process model, a
UML component model — and you can drill from the enterprise level into the detail and back
(ARCHIMATE §D.3).

<figure class="max-w-lg"><img src="/figure/ARCHIMATE:fig-117" alt="Correspondence between the ArchiMate language and other modeling languages" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 117. Correspondence Between the ArchiMate Language and Other Modeling Languages (ARCHIMATE)</figcaption></figure>

## BPMN

Both model business processes, but at different levels. ArchiMate shows high-level processes and
their relationship to the enterprise context — the application services that support them, the
goals and requirements they fulfil — and is *not* meant for detailed workflow. BPMN goes down to
executable task and sub-process detail but has no enterprise context. Shared concepts: business
process and event. ArchiMate has one process element decomposed with flow, triggering and
junctions; BPMN has many event, task and gateway types. A BPMN participant (pool) corresponds to an
ArchiMate business role or actor, or to an application component for automated processes. Mapping
downward from ArchiMate to BPMN is straightforward; mapping upward loses detail (ARCHIMATE §D.4).

## UML

Several ArchiMate concepts were derived from UML. Correspondences: business process → activity
diagram; business actor and role → UML actor; application component → UML component;
application function → activity diagram; application service → use-case diagram; collaborations
correspond; node, artifact, device, system software and path have direct counterparts (system
software is UML's *execution environment*). Association, composition, aggregation, specialization
and realization have direct UML counterparts (ARCHIMATE §D.5).

Three differences are examinable (ARCHIMATE §D.5):

- **Serving is not UML dependency.** The notations look alike but the *direction* differs:
  serving points in the direction of service delivery, regardless of who calls whom.
- **UML has no service concept.** ArchiMate separates a service from the interface it is offered
  through, so one service can be offered via several interfaces; an ArchiMate application
  interface is therefore not a UML interface.
- **UML has fixed diagram types**; ArchiMate's viewpoint mechanism lets you build custom,
  stakeholder-oriented views.

## BMM

The Business Motivation Model partly inspired the strategy and motivation elements. BMM's *course
of action* corresponds directly to ArchiMate's Course of Action; BMM *directives* map to Principle,
Requirement and Constraint; BMM *ends* map mostly onto Goal; BMM *influencers* map onto Driver; and
BMM *assessments* map straight onto Assessment. BMM is more fine-grained; ArchiMate trades detail
for breadth and cross-domain linkage (ARCHIMATE §D.6).

**Trap:** which BMM concept maps to Driver? *Influencer* — not "end" (that is Goal) and not
"directive" (that is Principle/Requirement/Constraint) (ARCHIMATE §D.6).
