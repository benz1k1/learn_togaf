---
title: "The Project, Migration, and Implementation and Migration viewpoints"
unit: A8
objectives: ["A8.3"]
refs: ["ARCHIMATE §C.4", "ARCHIMATE §C.4.1", "ARCHIMATE §C.4.2", "ARCHIMATE §C.4.3", "ARCHIMATE §12.5", "ARCHIMATE §12.2.4"]
reading_minutes: 8
source: authored
status: draft
---
## Three viewpoints, three questions

Appendix C closes with three viewpoints built on the implementation and migration elements. Each
answers a different management question: the **Project** viewpoint asks *how is the change being
run*, the **Migration** viewpoint asks *through which states does the architecture pass*, and the
**Implementation and Migration** viewpoint asks *which projects touch which parts of the
architecture*. Each viewpoint description lists its elements, the concerns it frames, its purpose
and its scope (ARCHIMATE §C.4).

| Viewpoint | Stakeholders | Concerns | Purpose | Scope | Elements |
|---|---|---|---|---|---|
| **Project** | operational managers, enterprise and ICT architects, employees, shareholders | architecture vision and policies, motivation | deciding, informing | implementation and migration | goal, outcome, work package, implementation event, deliverable, business actor, business role |
| **Migration** | enterprise, process, application, infrastructure and domain architects, employees, shareholders | history of models | designing, deciding, informing | implementation and migration | plateau, gap |
| **Implementation and Migration** | operational managers, enterprise and ICT architects, employees, shareholders | architecture vision and policies, motivation | deciding, informing | multiple layers, multiple aspects | goal, requirement, constraint, work package, implementation event, deliverable, plateau, gap, business actor, business role, location, any core element |

## Project viewpoint

The Project viewpoint models the *management of architecture change*. Its framing is that
moving from a current to a target enterprise architecture is itself an architecture problem with
long-term consequences: the programme may run for years; every system must stay operational
throughout; the technology standards being adopted may be immature; and the change lands on
people, culture and ways of working. Governance constraints — portfolio management, project
deliverables and goals, plateau planning, finance and law — shape what the models must show
(ARCHIMATE §C.4.1).

Its element list is the delivery side of the layer plus the people: work packages, the events
that start and end them, the deliverables they produce, the actors and roles responsible, and the
goals and outcomes the work serves. Plateaus and gaps are *absent* — this viewpoint is about
projects, not states (ARCHIMATE §C.4.1).

## Migration viewpoint

The Migration viewpoint is deliberately thin: plateaus and the gaps between them, nothing else.
It specifies the transition from an existing architecture to a desired one as a sequence of
stable states, and its listed concern is the *history of models* — which architecture was valid
when. Because the plateau and gap elements are fully described in chapter 12, the viewpoint
section only positions them (ARCHIMATE §C.4.2).

**Trap:** the Migration viewpoint contains no work packages. A question that asks for the
viewpoint showing "baseline, two transition architectures and the target, and what differs
between each" wants Migration; add the projects that get you from one to the next and you have
moved to the Implementation and Migration viewpoint (ARCHIMATE §C.4.2).

## Implementation and Migration viewpoint

This is the widest of the three: it relates programmes and projects to the *parts of the
architecture they implement*, so its scope is multiple layers and multiple aspects and its element
list includes any core element. A project's scope can be expressed either as the plateaus it
realizes or as the individual elements it affects, with the relationships annotated to say how
they are affected (ARCHIMATE §C.4.3).

The specification pairs it with the Project viewpoint for portfolio management. The Project
viewpoint relates business goals to programmes and projects, which answers whether the portfolio
covers the goals; the Implementation and Migration viewpoint runs the trace further, from goals and
requirements through projects to architecture elements, which exposes overlap between projects and
lets you check that project dependencies agree with the dependencies between plateaus and elements
(ARCHIMATE §C.4.3).

## Choosing between them

| The stakeholder wants to see… | Viewpoint |
|---|---|
| the projects, their milestones, who owns them and which goals they serve | Project |
| the sequence of architecture states and what changes between them | Migration |
| which projects deliver which plateaus or touch which components | Implementation and Migration |
| whether two projects both change the same application | Implementation and Migration |
| whether every strategic goal has a project behind it | Project |

**Trap — purpose:** Migration is the only one of the three whose purpose includes *designing*.
Project and Implementation and Migration are for *deciding and informing*. A question about
designing the transition path is pointing at Migration (ARCHIMATE §C.4).

## The TOGAF reading

These three viewpoints are the drawing conventions for Phases E, F and G. Phase E's Transition
Architectures are plateaus and its consolidated gaps are gap elements, so E draws Migration and
Implementation and Migration views. Phase F's Implementation and Migration Plan is work packages,
deliverables and implementation events in sequence, with plateaus as the milestones, so F draws
Implementation and Migration and Project views. Phase G governs the same work packages, so it keeps
the Project view (ARCHIMATE §12.2.4).

## Worked model

"Plateau Baseline —triggers→ Plateau Transition 1 —triggers→ Plateau Target. Gap 'No online
claims' associated with Baseline and Transition 1. Work package 'Claims portal' realizes
deliverable 'Portal release 1', which realizes Transition 1 and realizes application component
'Claims Portal'. Role 'Portal project manager' assigned to 'Claims portal'. Event 'Portal go-live'
triggered by 'Claims portal'." Strip it to the plateaus and the gap and you have a Migration view.
Strip it to the work package, role, event, deliverable and a goal and you have a Project view.
Keep all of it, including the component, and it is an Implementation and Migration view
(ARCHIMATE §C.4.3).

## Check yourself

- Which of the three viewpoints contains only two element types?
- Which viewpoint includes core elements, and why does that make it the right one for overlap analysis?
- Which viewpoint's purpose includes designing?
