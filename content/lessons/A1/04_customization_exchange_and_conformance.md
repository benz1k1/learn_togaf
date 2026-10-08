---
title: "Customization, the exchange format and conformance"
unit: A1
objectives: ["A1.4"]
refs: ["ARCHIMATE §1.1", "ARCHIMATE §1.3", "ARCHIMATE §14", "ARCHIMATE §14.1", "ARCHIMATE §14.2", "ARCHIMATE §14.2.1", "ARCHIMATE §14.2.2", "ARCHIMATE §14.2.3", "ARCHIMATE §14.2.5", "ARCHIMATE §14.2.6", "ARCHIMATE §14.2.7", "ARCHIMATE §14.2.9"]
reading_minutes: 8
source: authored
status: draft
---
## Why customization, and why it is not "extension"

The metamodel contains only what general Enterprise Architecture modelling needs. Anything more
specific — inputs for a particular analysis, a sector's vocabulary, a communication style — is
handled by *customizing* the language rather than adding concepts most users would never touch.
Chapter 14 was renamed from "Language Extension Mechanisms" precisely because these mechanisms do
not extend the language; they tailor it (ARCHIMATE §14).

There are two mechanisms, and a tool must support both in an implementation-defined way
(ARCHIMATE §1.3):

| Mechanism | What it does | Section |
|---|---|---|
| **Adding attributes (profiles)** | attaches typed supplementary data to any concept | §14.1 |
| **Specialization of concepts** | defines a new element or relationship type from an existing one | §14.2 |

## Attributes and profiles

Every concept in a model may carry attributes. They are added through a *profiling* mechanism: a
**profile** is a data structure defined separately from the language and coupled dynamically to
concepts — the modeller decides whether and when to assign one. A profile is a set of typed
attributes, each possibly with a default the user may change (ARCHIMATE §14.1).

Two kinds of profile exist: **pre-defined** profiles with a fixed attribute structure that a tool
can implement in advance (for example the inputs of a standard analysis), and **user-defined**
profiles created through a profile definition language (ARCHIMATE §14.1).

Basic attribute types: string, integer, real, boolean, currency, date, URL. Complex types:
*structure* (fields of basic types) and *list*. The Model Exchange File Format defines how these
are encoded when a model is exchanged (ARCHIMATE §14.1).

The specification's own examples are analysis profiles — a *weight* on each serving relationship,
fixed and variable *cost* and *service time* on each service, cost and *capacity* on each structure
element — and a generic cardinality-and-role profile for relationships (ARCHIMATE §14.1).

**Trap:** attributes do *not* create new element types; a profile with a name used as a
specialization does (see below). Attributes alone are for data, e.g. cost or capacity
(ARCHIMATE §14.1).

## Specialization of concepts

Specialization defines a new element or relationship from an existing one. The specialized
concept *inherits* the properties of its parent, including the relationships the parent may have,
but it may be further restricted. It may have its own notation, preferably resembling the parent's
— an added icon or marker — and it may predefine attributes. It closely resembles a UML
stereotype, and the default notation is UML's guillemets, «name»; several specializations on one
concept are listed comma-separated. Analysis and visualization built for the base language still
work, because the underlying definitions are preserved (ARCHIMATE §14.2).

Mechanically, a specialization *is* a profile: the profile's name is the specialization's name,
and assigning the profile to a general concept makes it the specialized concept (ARCHIMATE §14.2).

Relationships specialize the same way, inheriting the parent's properties with possible extra
restrictions — for example two specializations of assignment for responsibility versus
accountability, or a flow specialized as material flow (ARCHIMATE §14.2).

## The informative examples

The tables in §14.2 are *informative*, but their pairings are exactly what a question tests:
"which parent concept would you specialize to model X?"

| Specialized concept | Parent | Section |
|---|---|---|
| Individual, Organizational Unit, Organization, Threat Agent | Business Actor | §14.2.1 |
| Business Activity | Business Process | §14.2.1 |
| Threat Event, Loss Event | Business Event | §14.2.1 |
| Logical / Physical Application Component | Application Component | §14.2.2 |
| Graphical User Interface, Application-to-Application Interface | Application Interface | §14.2.2 |
| Logical / Physical Technology Component | Node | §14.2.3 |
| Mobile Device, Embedded Device | Device | §14.2.3 |
| Processing / Storage / Communication Service | Technology Service | §14.2.3 |
| Metric | Driver | §14.2.5 |
| Vulnerability, Risk | Assessment | §14.2.5 |
| Business Objective, Control Objective | Goal | §14.2.5 |
| Business Policy | Principle | §14.2.5 |
| Business Rule, Control Measure | Requirement | §14.2.5 |
| Capability Increment | Capability | §14.2.6 |
| Strategy, Tactic | Course of Action | §14.2.6 |
| Program, Project | Work Package | §14.2.7 |
| Money Flow | Flow | §14.2.9 |
| Or-join | Or-junction | §14.2.9 |

**Trap:** *Risk* and *Vulnerability* specialize **Assessment**, not Driver; *Metric* specializes
**Driver**; *Business Rule* is a **Requirement**, *Business Policy* is a **Principle**
(ARCHIMATE §14.2.5). Logical and physical application components are specializations of one
element, Application Component, which is how TOGAF's ABB/SBB distinction is carried
(ARCHIMATE §14.2.2).

## The Model Exchange File Format

The ArchiMate ecosystem includes an **XML** exchange format that lets models and diagrams move
between tools; it is referenced from the objective of the standard and again for how attribute
types are encoded (ARCHIMATE §1.1, §14.1). The exam expects you to know it exists, that it is XML,
and that it carries the model *and* its diagrams — not that it is a modelling notation of its own.

## Conformance and certification

A conforming implementation of the language **shall** support: the language structure, generic
metamodel, relationships, layers and cross-layer dependencies (chapters 3–12); the standard
iconography (summarized in Appendix A); the viewpoint mechanism (chapter 13); the customization
mechanisms (chapter 14) in an implementation-defined manner; and the relationship tables (Appendix
B). It **may** support the example viewpoints of Appendix C (ARCHIMATE §1.3).

**Trap:** the example viewpoints are the one optional item — "may", not "shall". Everything else
in the list is mandatory (ARCHIMATE §1.3). Tool conformance and *people* certification are
separate programmes; the specification points to The Open Group website for the certification
requirements that reference the standard (ARCHIMATE §1.3).
