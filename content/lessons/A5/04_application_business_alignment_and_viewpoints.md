---
title: "Application and business alignment; the Application Cooperation and Usage viewpoints"
unit: A5
objectives: ["A5.4", "A5.1", "A5.2", "A5.3"]
refs: ["ARCHIMATE §11", "ARCHIMATE §11.1", "ARCHIMATE §9.2.3", "ARCHIMATE §9.3.5", "ARCHIMATE §9.4.1", "ARCHIMATE §5.7", "ARCHIMATE §C.1", "ARCHIMATE §C.1.11", "ARCHIMATE §C.1.8", "ARCHIMATE §C.1.2"]
reading_minutes: 10
source: authored
status: draft
---
## Business-IT alignment as relationships

The chapters on the three layers describe each in isolation; Chapter 11 answers the central
Enterprise Architecture question of how they are matched. The language offers a small number of
cross-layer relationships for the link between business and applications, and between
applications and technology (ARCHIMATE §11). This lesson covers the business-application pair;
the application-technology pair is in unit A6.

<figure class="max-w-lg"><img src="/figure/ARCHIMATE:fig-104" alt="Relationships between Business Layer and Application and Technology Layer elements" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 104. Relationships Between Business Layer and Application and Technology Layer Elements (ARCHIMATE)</figcaption></figure>

Two kinds of relationship do the work. *Serving* relationships express support: an application
service serves the business behaviour elements, and an application interface serves a business
role. The reverse is also allowed — a business service may serve application behaviour and a
business interface may serve an application component. *Realization* relationships express that
something lower is the concrete form of something higher: an application process or function may
realize a business process or function, and a data object (or a technology passive element) may
realize a business object, meaning it is the digital or physical representation of it
(ARCHIMATE §11.1).

| From (application) | Relationship | To (business) | Meaning |
|---|---|---|---|
| Application service | serving | Business process / function / interaction / event / service; business actor / role | The application supports the business behaviour |
| Application interface | serving | Business role / collaboration | The role reaches the application through this channel |
| Application process / function | realization | Business process / function | The business behaviour is automated by application behaviour |
| Data object | realization | Business object | The data object is the digital form of the business concept |
| Application service, data object | aggregation (into) | Product | Offered directly to a customer as part of the product |

**Trap:** there is *no* realization of a business actor, role or collaboration by an application
or technology element, because people cannot be realized by software. The correct modelling is
that the *behaviour* of those active elements is realized by application behaviour, to which an
application component is then assigned (ARCHIMATE §11.1). Any option that has an application
component realizing a business role is wrong.

**Trap:** a product may aggregate an application service or a data object directly — the product
is the one business element that reaches into other layers by aggregation. Do not "correct" this
to realization (ARCHIMATE §11.1).

## Derivation across layers

Because the derivation rules of §5.7 chain relationships, the intermediate element can be
skipped. If a business process is served by an application service that is realized by an
application function performed by a component, a modeller may draw the component serving the
process. The exam asks whether such a shortcut is permitted; the answer is that a derived
relationship is valid when the chain permits it (ARCHIMATE §5.7, ARCHIMATE §11.1).

## Application cooperation viewpoint

This cooperation-category viewpoint describes the relationships between application components,
either as the information flows between them or as the services they offer and use. It is the
usual way to draw an overview of the application landscape, and it can also express the
orchestration of services that together support one business process (ARCHIMATE §C.1.11).

| Application cooperation viewpoint | |
|---|---|
| Stakeholders | Enterprise, process, application and domain architects |
| Concerns | Relationships and dependencies between applications; orchestration/choreography of services; consistency and completeness; reduction of complexity |
| Purpose | Designing |
| Scope | Application layer, multiple aspects |
| Elements | Location; application component/collaboration; application interface; application process/function/interaction; application event; application service; data object |

**Trap:** the application cooperation viewpoint is the one basic viewpoint whose scope is stated
as "application layer, multiple aspects". It contains no business elements. If a question asks for
a viewpoint that shows how applications support business processes, this is not it
(ARCHIMATE §C.1, ARCHIMATE §C.1.11).

## Application usage viewpoint

The application usage viewpoint, in the support category, shows how applications are used to
support business processes and how they are used by other applications. Designing an application
by finding the services processes need, designing processes from the services available, and
showing an operational manager which applications a process depends on are its three stated uses
(ARCHIMATE §C.1.8).

| Application usage viewpoint | |
|---|---|
| Stakeholders | Enterprise, process and application architects; operational managers |
| Concerns | Consistency and completeness; reduction of complexity |
| Purpose | Designing, deciding |
| Scope | Multiple layers, multiple aspects |
| Elements | Business actor, role, collaboration; business process/function/interaction, event, object; application component/collaboration, interface, process/function/interaction, event, service; data object |

**Trap:** application usage is multi-layer and includes business actors, roles and processes;
application cooperation is single-layer and does not. The word "usage" is the cue: usage means
*by the business*, cooperation means *among applications* (ARCHIMATE §C.1.8, ARCHIMATE §C.1.11).

## Application structure viewpoint, for contrast

The composition-category application structure viewpoint shows the internal structure of one or
more applications and their data — useful for breaking down a system under construction or
identifying legacy components suitable for migration. Its elements are only application component,
interface, collaboration and data object; its stakeholders are application and solution
architects; its scope is single layer, multiple aspects (ARCHIMATE §C.1.2). Three viewpoints, three
questions: *what is inside* an application (structure), *how applications relate* (cooperation),
*how the business uses them* (usage).

## Recap of the serving direction

A service is what the exam most often asks to place across layers. Application services serve
business behaviour and active structure; application interfaces serve business roles; and, in
the same figure, technology services serve application behaviour. Serving always runs from the
provider's external behaviour or interface to the consumer, upward through the layers in the
common case (ARCHIMATE §9.3.5, ARCHIMATE §9.2.3, ARCHIMATE §11.1).
