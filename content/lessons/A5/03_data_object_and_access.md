---
title: "Data object and the access relationships"
unit: A5
objectives: ["A5.3"]
refs: ["ARCHIMATE §9.4", "ARCHIMATE §9.4.1", "ARCHIMATE §9.5", "ARCHIMATE §3.6", "ARCHIMATE §8.4.1", "ARCHIMATE §C.1.3"]
reading_minutes: 7
source: authored
status: draft
---
## The one passive element of the layer

The passive counterpart of the application component is the data object, used the way object
types are used in data modelling — most directly like a class in a UML class diagram. A data
object can be seen as the application-level representation of a business object, the way a
representation is the perceptible form of one in the Business Layer (ARCHIMATE §9.4). ArchiMate
has no separate "information layer": business objects and data objects together represent the
enterprise's information entities and the logical data components that realize them
(ARCHIMATE §9.4).

<figure class="max-w-lg"><img src="/figure/ARCHIMATE:fig-81" alt="Data object notation" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 81. Data Object Notation (ARCHIMATE)</figcaption></figure>

| Element | Aspect | Notation | Definition in plain words | Typical confusion |
|---|---|---|---|---|
| Data Object | Passive structure | Blue rectangle with a header band | Data structured for automated processing | Confusing it with a business object (the concept) or an artifact (the physical file) |

## Data object

A data object is data structured for automated processing. It should be a self-contained piece
of information whose meaning is clear to the *business*, not only to the application — a customer
record, a client data set, an insurance claim (ARCHIMATE §9.4.1). Like every ArchiMate passive
element it normally models a logical *type*, of which many instances exist in running
applications (ARCHIMATE §9.4.1, ARCHIMATE §3.6).

The relationships are the exam content. A function or process can *operate on* data objects; a
data object may be communicated through interactions and used or produced by services. In
relationship terms, a data object is *accessed* by an application function, interaction or
service. It may *realize* a business object and be *realized by* an artifact. With other data
objects it may have association, specialization, aggregation or composition. Name it with a noun
(ARCHIMATE §9.4.1).

## The access relationship

Access is the dependency relationship between behaviour and passive structure, in every layer.
In the Business Layer the accessing elements are process, function, interaction, event and
service, and the accessed element is a business object; in the Application Layer the same five
kinds of behaviour access data objects (ARCHIMATE §8.4.1, ARCHIMATE §9.4.1). The notation is a
dotted line with a small arrowhead whose direction says what kind of access it is: towards the
object for write, towards the behaviour for read, both ends for read-write, and no arrowhead
for undirected access.

**Trap:** access always has behaviour at one end and a passive element at the other. An
application *component* does not access a data object — the component is active structure, and it
reaches the data only through the function it performs. If an option says "the application
component accesses the data object", it is the distractor (ARCHIMATE §9.4.1).

**Trap:** the direction of the arrow encodes read versus write; a plain line is undirected
access. "Which arrowhead means the process creates the object?" — an arrowhead pointing *at* the
object (write). Read the option text for "read", "write" or "read-write" rather than assuming
"access" is one thing.

## The realization chain

The three passive elements of the core line up in a chain that runs downward through the layers:
a business object is realized by a data object, and a data object is realized by an artifact.
Each step says that the lower element is a more concrete form of the upper one — a digital
representation, then a physical file (ARCHIMATE §9.4.1, ARCHIMATE §8.4.1). Because relationships
can be derived along a chain, an artifact may be drawn as realizing a business object directly.

| Layer | Passive element | Realized by |
|---|---|---|
| Business | Business object | Representation (same layer) or data object (application) |
| Application | Data object | Artifact (technology) |
| Technology | Artifact | — |

**Trap:** realization runs *upward* in this chain: data object → business object, artifact → data
object. Distractors reverse it ("the business object realizes the data object") or substitute
association or serving. Only realization is correct, and only in that direction (ARCHIMATE §9.4.1).

## Where it appears in the viewpoints

The information structure viewpoint is the one built around this chain. It is the counterpart of
the traditional information model: it shows the structure of the information used in the
enterprise or in one process or application, and how business-level information is represented at
application level as data structures and then mapped onto the technology below, for example as a
database schema. Its elements are business object, representation, data object, artifact and
meaning; it is for domain and information architects, its purpose is designing, and its scope is
multiple layers, single aspect (ARCHIMATE §C.1.3).

## The example

An "Online Insurance Quotation" data object is *composed of* "Quoted Price", "Terms and
Conditions" and "Certificate of Authenticity"; "Auto Insurance Quotation" and "Travel Insurance
Quotation" *specialize* it, and the travel one adds "Purchased Itinerary". Composition and
specialization among data objects is all the example shows — a reminder that the same-type
structural relationships are always available (ARCHIMATE §9.4).

Table 7's line for the data object is short — "data structured for automated processing" — and
the exam pairs it with the business object's "concept used within a particular business domain"
and the artifact's "piece of data used or produced ... by deployment and operation of an IT
system" to see whether you can tell the three apart (ARCHIMATE §9.5).
