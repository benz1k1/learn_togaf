---
title: "Reading the relationship table: which relationship may connect X to Y"
unit: A7
objectives: ["A7.5"]
refs: ["ARCHIMATE §B.5", "ARCHIMATE §B.6", "ARCHIMATE §5", "ARCHIMATE §5.7", "ARCHIMATE §B.4", "ARCHIMATE §4.5.1", "ARCHIMATE §5.2.2"]
reading_minutes: 10
source: authored
status: draft
---
## What the table is

Appendix B.5 is a grid of every element type against every element type. Each cell holds a
string of letters — the relationships permitted from the row element to the column element. The
grid is not hand-drawn: it is *computed* from the metamodel figures of chapters 3 to 12 plus the
derivation rules and restrictions of §B.1–B.4. That is why it contains far more than the diagrams
show, and why the exam treats it as the final word on "which relationship may connect X to Y"
(ARCHIMATE §B.5).

| Letter | Relationship | Letter | Relationship |
|---|---|---|---|
| **a** | access | **o** | association |
| **c** | composition | **r** | realization |
| **f** | flow | **s** | specialization |
| **g** | aggregation | **t** | triggering |
| **i** | assignment | **v** | serving |
| **n** | influence | | |

**Trap:** the letters are not all initials. **i** is ass*i*gnment (not influence), **n** is
i*n*fluence, **o** is ass*o*ciation, **v** is ser*v*ing, **g** is a*gg*regation. A question that
shows a cell reading `iorv` and asks whether influence is allowed is testing the legend, not the
metamodel — the answer is no (ARCHIMATE §B.5).

## Cells you can fill without looking

Some rows follow directly from chapter 5 and save a lookup (ARCHIMATE §5):

- Same type against same type: **c**, **g** and **s** are always present (composition,
  aggregation, specialization), plus whatever else the metamodel adds.
- Any element against any element: **o** is always present.
- An element against a *relationship*: only **o**, unless the source is a grouping, location or
  plateau, which may also **c** or **g** the relationship.

## Rows and columns that follow from the metamodel

The overloading of the relationships means the same letter carries a different sentence in each
cell. The table below is a reading aid for the cells that come up most; it is a summary of the
metamodel fragments, not a substitute for them (ARCHIMATE §B.5).

| From | To | Permitted (among others) | The sentence it makes |
|---|---|---|---|
| Business Actor | Business Role | **i** | actor fulfils role |
| Business Role | Business Process | **i** | role performs process |
| Business Process | Business Service | **r** | process realizes service |
| Business Process | Business Object | **a** | process accesses object |
| Business Service | Business Process | **v** | service serves process |
| Application Component | Application Function | **i** | component performs function |
| Application Function | Application Service | **r** | function realizes service |
| Application Service | Business Process | **v** | application service serves business process |
| Application Interface | Business Role | **v** | interface serves role |
| Data Object | Business Object | **r** | data object realizes business object |
| Artifact | Data Object | **r** | artifact realizes data object |
| Artifact | Application Component | **r** | artifact realizes component |
| Node | Artifact | **i** | node stores artifact |
| Technology Service | Application Component | **v** | technology service serves component |
| Application Process | Business Process | **r** | application behaviour realizes business behaviour |
| any core element | Requirement / Goal | **r**, **n** | core element realizes or influences motivation |
| Deliverable | any core element | **r** | deliverable realizes part of the architecture |
| Business Role | Work Package | **i** | role is responsible for work package |

Two cross-layer patterns underlie most of these. **Serving upward**: application services and
interfaces serve business behaviour and actors; technology services and interfaces serve
application components and behaviour. **Realization upward**: application behaviour may realize
business behaviour; a data object realizes a business object; an artifact realizes a data object
or a component. The derivation rules then extend both: because a component is assigned to a
function that realizes a service, the table also grants the component **r** to the service and
**v** to the process the service serves (ARCHIMATE §5.7).

## Direction is half the answer

The table is directional — the cell (Business Process, Business Service) and the cell (Business
Service, Business Process) hold different letters. Reading the wrong one is the commonest error.
Ask *from which element is the relationship drawn*, then look up that row (ARCHIMATE §B.5).

**Trap — access:** the row is always the behaviour or active-structure element and the column the
passive one, whatever the arrowhead says. There is no **a** in the (Business Object, Business
Process) cell, because a business object never accesses anything (ARCHIMATE §5.2.2).

**Trap — realization and serving:** "service realizes process" and "process serves service" both
read the wrong row. Realization goes from the concrete to the abstract; serving goes from the
provider to the user (ARCHIMATE §B.5).

## Passive structure rows and columns

The restrictions in §B.4 explain a pattern you will see in every passive-structure column: a
non-passive source may reach a passive element only by **a**, **i** or **o**; a passive source may
reach another passive element only by **r** (and **o**, plus the same-type **c g s**); and a passive
source may reach a non-passive element only by **r**, **n** or **o**. So a data object may realize a
business object but may not serve, trigger or be assigned to anything (ARCHIMATE §B.4).

## Grouping, plateau and location: the table's wildcards

Grouping and location may aggregate or compose *any* concept — elements, relationships,
junctions. A grouping may in addition be the source or the target of any relationship with any
element, provided that element could be the target or source of that relationship in the first
place, and groupings may relate to each other in any way. Plateaus share the "compose anything"
power over core concepts and relationships, but only the specific aggregation shown in their own
metamodel fragment. Any relationship may be associated with any element (ARCHIMATE §B.6).

| From → To | Grouping | Plateau / Location | Ordinary element | A relationship | A junction |
|---|---|---|---|---|---|
| **Grouping** | any | c, g and any the target permits | any the target permits | o | a f i n o r t v |
| **Ordinary element** | any the source permits | see metamodel | see metamodel | o | a f i n o r t v |
| **A relationship** | c, g, o | c, g, o | o | — | o |

Because the group's relationship is read as a *collective* relationship of its contents, a
grouping that realizes a service says its members together realize it; PDR 12 lets you push that
realization (or assignment) down onto a member only where the member's own row allows it
(ARCHIMATE §4.5.1).

## A method for table questions

1. Fix the direction: which element is the source?
2. Same type? Then **c g s** (and **o**) are already there.
3. Is the target passive? Then the source is limited to **a i o** (non-passive) or **r o** (passive).
4. Is the target motivation? Then the source is limited to **i r n o** — and only **n** for influence.
5. Is either end a grouping or location? Then the wildcards of §B.6 apply.
6. Otherwise read the metamodel fragment for the layer and the cross-layer figure, and remember the derived extensions (ARCHIMATE §B.5).

## Check yourself

- What does the letter **i** stand for in the table, and what does **n** stand for?
- Which letters may appear in a cell whose source is a data object and whose target is a business process?
- May a grouping compose a relationship? May an application component?
