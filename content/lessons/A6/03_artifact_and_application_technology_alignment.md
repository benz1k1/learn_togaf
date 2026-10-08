---
title: "Artifact, technology passive structure, and the application–technology alignment"
unit: A6
objectives: ["A6.3", "A6.1", "A6.2"]
refs: ["ARCHIMATE §10.4", "ARCHIMATE §10.4.1", "ARCHIMATE §11", "ARCHIMATE §11.2", "ARCHIMATE §5.7", "ARCHIMATE §10.2.1", "ARCHIMATE §10.2.3", "ARCHIMATE §10.9", "ARCHIMATE §C.1.9", "ARCHIMATE §C.1.13"]
reading_minutes: 10
source: authored
status: draft
---
## Technology passive structure

Technology passive structure elements are the things the infrastructure uses and processes:
the informational and physical objects it manipulates. The generic "technology passive structure
element" is abstract and never drawn; its concrete forms are artifact (files and the like) and
material (physical matter, from the physical extension) (ARCHIMATE §10.4). Any technology
behaviour — function, process, interaction, event or service — may access them; they may have
association, specialization, aggregation or composition with one another; and specific internal
active elements may be *assigned to* them, which is how deployment is drawn: a device assigned to
an artifact means the artifact is deployed on that device (ARCHIMATE §10.4).

<figure class="max-w-lg"><img src="/figure/ARCHIMATE:fig-97" alt="Technology passive structure elements" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 97. Technology Passive Structure Elements (ARCHIMATE)</figcaption></figure>

| Element | Aspect | Notation | Definition in plain words | Typical confusion |
|---|---|---|---|---|
| Artifact | Passive structure | Green rectangle with a folded-corner page icon | A piece of data used or produced in software development, or by deploying and operating an IT system | Confusing it with a data object (logical) or a representation (business); artifact is the physical file |
| Material | Passive structure | Green rectangle with a material icon | Tangible physical matter or energy | Modelling it as an artifact because it is "passive" |

## Artifact

An artifact is the "physical" element of the IT world: source files, executables, scripts,
database tables, messages, documents, specifications and model files are all artifacts. It is a
specialization of technology passive structure element and can be created, deleted, read and
written by technology behaviour. An instance — a copy — of an artifact is deployed on a device or
system software, and that deployment is an assignment relationship (ARCHIMATE §10.4.1).

Artifacts have two typical uses, and the specification suggests they could be defined as
specializations: as an *execution component* (the artifact realizes an application component or
system software) and as a *data file* (the artifact realizes a data object). A device or system
software element assigned to an artifact means the artifact is deployed on it. Name an artifact
after the file — "order.jar" — and remember it may consist of sub-artifacts (ARCHIMATE §10.4.1).

**Trap:** an artifact *realizes* an application component. It does not "serve" it, it is not
"assigned to" it, and the component does not realize the artifact. Assignment is between the
artifact and the device or system software it is deployed on (ARCHIMATE §10.4.1).

**Trap — artifact vs data object vs representation:** three passive elements, three layers. A
representation is a human-perceptible business document; a data object is logical data
structured for automated processing; an artifact is the physical file or table. Realization runs
upward: artifact → data object → business object (ARCHIMATE §10.4.1).

## Application–technology alignment

Figure 105 gives the relationships between the Application and Technology Layers, and as with
business–application alignment there are two kinds (ARCHIMATE §11, ARCHIMATE §11.2).

<figure class="max-w-lg"><img src="/figure/ARCHIMATE:fig-105" alt="Relationships between Application Layer and Technology Layer elements" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 105. Relationships Between Application Layer and Technology Layer Elements (ARCHIMATE)</figcaption></figure>

*Serving* relationships: a technology service serves the application behaviour elements, and a
technology interface serves an application component. The reverse also exists — an application
service may serve technology behaviour and an application interface may serve a technology
internal active element (ARCHIMATE §11.2). *Realization* relationships: a technology process or
function may realize an application process or function; an artifact may realize a data object
(a physical data file holds the logical data); and an artifact may realize an application
component (an executable implements the application). In the second case the artifact is the
"physical" component deployed on a device or system software by assignment, so the logical
component is realized by the artifact and, indirectly, by whatever the artifact is deployed on
(ARCHIMATE §11.2).

| From (technology) | Relationship | To (application) |
|---|---|---|
| Technology service | serving | Application process / function / interaction / event / service; application component |
| Technology interface | serving | Application component |
| Technology process / function | realization | Application process / function |
| Artifact | realization | Data object |
| Artifact | realization | Application component |
| Node / device / system software | assignment | Artifact (deployment) |

**Trap:** a node is not directly "assigned to" an application component in the metamodel figure;
the path is node → (assignment) → artifact → (realization) → application component. Derivation
lets a modeller draw the shortcut, and the exam accepts it as a *derived* relationship, but the
direct relationship the specification states is artifact realizes component (ARCHIMATE §11.2,
ARCHIMATE §5.7).

## Business to technology in one hop

Because derivation chains relationships, business and technology elements may be related
directly: a business object realized by a data object realized by an artifact means the artifact
indirectly realizes the business object, and a diagram may show that single relationship
(ARCHIMATE §11.2, ARCHIMATE §5.7).

## The example

A "Web Archive" artifact (which may realize an application component) is *composed of* two
Java-archive artifacts; two specializations of it exist for the purchase and quotation
applications; and a "Travel Insurance Database" artifact (which may realize a data object) is
*associated* with the web archive. Both uses of artifact — execution component and data file —
appear side by side (ARCHIMATE §10.4).

## The two viewpoints built on this alignment

The technology usage viewpoint (support category) shows how applications are supported by
technology: the services delivered by devices, system software and networks to the applications.
It is used for performance and scalability analysis because it ties the physical infrastructure
to the logical applications, and its elements are the application active and behaviour elements,
data object, and the whole technology set including artifact (ARCHIMATE §C.1.9). The
implementation and deployment viewpoint (realization category) shows how applications are
realized on the infrastructure: the mapping of components onto artifacts and of application
information onto storage. Its elements are the application elements plus system software,
technology interface, path, technology behaviour, technology service and artifact; its concern is
the structure of application platforms (ARCHIMATE §C.1.13).

**Trap:** technology usage is about *serving* (what technology does for applications);
implementation and deployment is about *realization* (how applications are built onto artifacts
and platforms). A stem about mapping components onto artifacts wants the second (ARCHIMATE §C.1.9,
ARCHIMATE §C.1.13).

Table 8's definition of artifact — data used or produced in development or by deploying and
operating an IT system — is the one to memorise, alongside the fact that node, device and
system software can all be assigned to it for deployment (ARCHIMATE §10.9, ARCHIMATE §10.2.1,
ARCHIMATE §10.2.3).
