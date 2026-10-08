---
title: "ADM phases to ArchiMate viewpoints, content-metamodel entities to language elements"
unit: X1
objectives: ["X1.1"]
refs: ["ARCHIMATE §D.1", "ARCHIMATE §13.4", "ARCHIMATE §C.1", "ARCHIMATE §C.2", "ARCHIMATE §C.3", "ARCHIMATE §C.4", "WP:w14c §3", "GUIDE:integrating-risk-and-security §5.12"]
reading_minutes: 10
source: authored
status: draft
---
## Why the two standards fit

The ArchiMate specification says it in its own TOGAF appendix: the language *complements* the framework by supplying a vendor-independent set of concepts, with a notation, for the models "below the waterline" that TOGAF views are cut from. The ArchiMate core layers correspond to the ADM's three main architecture phases (Business, Information Systems, Technology), while its strategy, motivation and implementation-and-migration elements cover most of the rest of the cycle. The mapping is not one-to-one — ArchiMate viewpoints are more precisely specified than TOGAF's — but the two share the viewpoint idea and a common repository of models, so they combine easily (ARCHIMATE §D.1).

The detailed harmonization is the Open Group white paper W14C, which the appendix cites: it gives a minimal ArchiMate-based metamodel that covers the whole ADM cycle and maps content-metamodel entities to elements. The tables below encode that mapping as the app uses it on `/adm/{phase}` (the crosswalk panel) and `/artefact` (the `archimate` column of every artefact) (WP:w14c §3; ARCHIMATE §D.1).

## Phase by phase: which viewpoints draw which phase

| ADM phase | ArchiMate viewpoints | Principal elements |
|---|---|---|
| Preliminary | Motivation, Organization | Stakeholder, Driver, Principle, Business Actor, Business Role, Grouping |
| A — Vision | Motivation, Stakeholder, Goal Realization, Strategy, Outcome Realization | Stakeholder, Driver, Assessment, Goal, Outcome, Principle, Requirement, Capability, Course of Action |
| B — Business | Organization, Business Process Cooperation, Product, Capability Map, Value Stream | Business Actor, Role, Process, Function, Service, Object, Product, Capability, Value Stream |
| C — Information Systems | Information Structure, Application Cooperation, Application Usage | Business Object, Data Object, Application Component, Interface, Service, Function |
| D — Technology | Technology, Technology Usage, Physical, Layered | Node, Device, System Software, Technology Service, Communication Network, Artifact, Facility, Equipment |
| E — Opportunities and Solutions | Migration, Implementation and Migration | Plateau, Gap, Work Package, Deliverable |
| F — Migration Planning | Implementation and Migration, Project | Work Package, Deliverable, Implementation Event, Plateau, Business Role |
| G — Implementation Governance | Implementation and Migration, Project | Work Package, Deliverable, Business Role, Contract |
| H — Change Management | Motivation, Migration | Driver, Assessment, Requirement, Plateau, Gap |
| Requirements Management | Requirements Realization, Motivation | Requirement, Constraint, Goal, Principle |

(ARCHIMATE §D.1; the viewpoint definitions are in ARCHIMATE §C.1–C.4.)

Three regularities make the table learnable. The **motivation** viewpoints open and close the cycle (Preliminary, A, H, Requirements Management) because those phases are about *why*. The **core-layer** viewpoints sit in B, C and D, one layer per phase. The **implementation-and-migration** viewpoints run through E, F and G, because those phases are about *change over time*: Plateaus for the states, Gaps between them, Work Packages and Deliverables for the work (ARCHIMATE §C.2, §C.1, §C.4).

**Trap:** Phase E is *Migration* (Plateaus and Gaps), Phase F is *Implementation and Migration* and *Project* (Work Packages in sequence, Implementation Events as milestones). Learners swap them because both phases mention migration. Remember that E decides *what* changes (states and gaps) and F decides *when* (packages and events) (ARCHIMATE §C.4).

## Entity by entity: which element expresses which content-metamodel entity

The content metamodel's entities and ArchiMate's elements were designed by the same organisation but not at the same time, so the mapping has some approximate cells. The table gives the reading W14C establishes and the ArchiMate appendix endorses; the `archimate` mapping on each artefact page uses the same pairs.

| TOGAF content-metamodel entity | ArchiMate element | Note |
|---|---|---|
| Organization Unit, Actor | Business Actor | An organisation unit is an actor composed of actors |
| Role | Business Role | Actor → Role is Assignment |
| Location | Location | Composite element; aggregates what is sited there |
| Business Service | Business Service | |
| Business Function | Business Function | |
| Process | Business Process | Steps chained by Triggering |
| Event | Business Event | |
| Product | Product | Composite: services plus a Contract |
| Contract | Contract | Specialisation of Business Object |
| Driver, Goal | Driver, Goal | |
| Objective | Outcome | A measurable objective is an Outcome realizing a Goal |
| Principle | Principle | |
| Requirement, Constraint | Requirement, Constraint | |
| Assumption | Assessment (or Requirement) | No direct element; W14C treats it as motivation |
| Capability | Capability | Strategy element |
| Value Stream | Value Stream | Strategy element |
| Course of Action | Course of Action | Strategy element |
| Data Entity | Business Object | Conceptual data; Data Object for the logical level |
| Logical Data Component | Data Object | |
| Physical Data Component | Artifact | The file or database that realizes the Data Object |
| Information System Service | Application Service | |
| Logical Application Component | Application Component | |
| Physical Application Component | Application Component realized by an Artifact | The deployed instance |
| Platform Service | Technology Service | |
| Logical Technology Component | Node, System Software | |
| Physical Technology Component | Device, System Software, Artifact | |
| Gap | Gap | Between two Plateaus |
| Work Package | Work Package | |
| Architecture Building Block | any element at the logical level | An ABB is a modelling *role*, not an element |
| Solution Building Block | the realizing product: Artifact, System Software, or a specialised element | Also a role; W14C recommends specialization |
| Measure, Service Quality | attribute on the element | Language customization: add an attribute |

(WP:w14c §3; ARCHIMATE §D.1, §14.1.)

**Trap:** *artifact* means two different things. A TOGAF artifact is a catalog, matrix or diagram — a work product. An ArchiMate Artifact is a technology-layer passive element — a file, a deployable. The TOGAF artifact that *lists physical data components* is drawn *using* ArchiMate Artifacts, which is where the confusion starts. The glossary entries `artifact` and `archimate_artifact` are confusables for this reason (ARCHIMATE §10.4).

## Reading the two tables together on an artefact page

Open `/artefact` and pick, say, the Application Communication Diagram. Its `archimate` mapping names the viewpoint (Application Cooperation), the elements (Application Component, Application Interface, Data Object) and the relationships (Flow, Serving, Access). That is the entity-by-entity table applied to one work product, and the viewpoint it names is the one the phase table lists for Phase C. Every artefact page is a cell of this crosswalk; every `/adm/{phase}` page is a row (ARCHIMATE §C.1; WP:w14c §3).

The TOGAF risk and security guide adds the security twist: it recommends the ArchiMate language for drawing the security concepts it plants in each phase, with motivation elements for the risk side — which is where unit X3 picks up (GUIDE:integrating-risk-and-security §5.12).

## What the mapping does not do

The appendix is candid: some TOGAF viewpoints cannot be mapped cleanly, because a TOGAF viewpoint is described generally and an ArchiMate viewpoint specifies stakeholders, concerns, abstraction level and element types. So the mapping is a *starting point* for defining TOGAF viewpoints with ArchiMate concepts using the viewpoint mechanism, not a translation table to apply blindly. When a TOGAF diagram has no listed ArchiMate viewpoint, define one: pick the element types, name the concern, and it is a legitimate custom viewpoint (ARCHIMATE §D.1, §13.4).

## Check yourself

- Which viewpoints draw Phases E and F, and how do they differ?
- Give the ArchiMate element for Objective, Physical Data Component and Information System Service.
- Why is Artifact a confusable, and which meaning applies on a Phase D diagram?
