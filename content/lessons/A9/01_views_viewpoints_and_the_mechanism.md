---
title: "View versus viewpoint, and the viewpoint mechanism"
unit: A9
objectives: ["A9.1"]
refs: ["ARCHIMATE §13.1", "ARCHIMATE §13.2", "ARCHIMATE §13.3", "ARCHIMATE §13.4", "ARCHIMATE §13.4.1", "ARCHIMATE §13.4.2", "ARCHIMATE §13.5"]
reading_minutes: 9
source: authored
status: draft
---
## Why views exist

An enterprise architecture involves many people with different backgrounds and different
notations. Frameworks such as Zachman and TOGAF tame that by classifying architecture
descriptions; ArchiMate complements a framework by giving those descriptions a precise structure.
Its answer to "who sees what" is that every architecture view is specified by an architecture
viewpoint, aimed at one type of stakeholder and one set of concerns, showing some aspects in
isolation or relating several. Views are partial by design — a view is an incomplete depiction,
and it is the *combination* of views with their underlying relationships that describes an
architecture (ARCHIMATE §13.1).

## The ISO 42010 vocabulary

The viewpoint mechanism follows ISO/IEC 42010, whose conceptual model links four terms:
a **stakeholder** holds **concerns**; a **viewpoint** frames concerns and governs views; a **view**
expresses the architecture for those concerns. TOGAF uses the same words in the same sense, which
is deliberate and is tested by both exams (ARCHIMATE §13.2).

<figure class="max-w-lg"><img src="/figure/ARCHIMATE:fig-114" alt="Conceptual model of an architecture description" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 114. Conceptual Model of an Architecture Description (ARCHIMATE)</figcaption></figure>

| Term | What it is | Test |
|---|---|---|
| **View** | a part of the architecture description addressing related concerns, tailored to specific stakeholders — *what you see* | it contains elements and relationships from the model |
| **Viewpoint** | the specification of a view: the concepts, models, analysis techniques and visualisations the view provides — *where you look from* | it contains no model content; it says what a view may contain |
| **Concern** | an interest a stakeholder has in the system | framed by one or more viewpoints |
| **Stakeholder** | a person, group or organisation with concerns | the audience a viewpoint is designed for |

A viewpoint has two sides: the concerns it frames for stakeholders and the conventions it
establishes on views — notations, model kinds, design rules, analysis techniques. A view is
*governed* by its viewpoint; one concern may be framed by several viewpoints; one viewpoint may
frame several concerns. What a viewpoint shows and hides is decided entirely by relevance to the
stakeholder's concerns; ideally the viewpoint's scope and the stakeholder's interests coincide.
Communication through views is usually two-way: the architect informs, the stakeholder critiques or
consents (ARCHIMATE §13.3).

**Trap:** "the Layered viewpoint of Northgate's claims system" is a category error. The Layered
*viewpoint* is a template; the diagram of a particular enterprise drawn to that template is a
Layered *view*. An option that calls a specific diagram a viewpoint, or calls the generic
specification a view, has swapped the terms (ARCHIMATE §13.3).

## The viewpoint mechanism

Because architects face many stakeholders and concerns, the specification supplies a framework
for defining and classifying viewpoints along two dimensions, **purpose** and **content**. The
sequence is: talk to the stakeholder and record the concerns; use the mechanism to fix purpose and
content and so define or pick a viewpoint; let the viewpoint govern the construction of the view;
present the view (ARCHIMATE §13.4).

<figure class="max-w-lg"><img src="/figure/ARCHIMATE:fig-115" alt="Framing stakeholder concerns using the viewpoint mechanism" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 115. Framing Stakeholder Concerns using the Viewpoint Mechanism (ARCHIMATE)</figcaption></figure>

Creating a viewpoint takes two steps: **select** the subset of elements and relationships from
the metamodel that the concerns need; then **define a representation** for them — a diagram in
standard or customised notation, a catalogue, a matrix of two element groups, or something else
entirely. Applying the viewpoint to a model then means selecting the parts of the model that
match step one and drawing them as step two prescribes (ARCHIMATE §13.4).

## The purpose dimension

| Purpose | Who it helps | Typical representation |
|---|---|---|
| **Designing** | architects and designers, from sketch to detailed design | diagrams |
| **Deciding** | managers making decisions, through cross-domain insight | cross-reference tables, landscape maps, lists, reports |
| **Informing** | any stakeholder needing understanding, commitment or persuasion | illustrations, animations, cartoons, flyers |

A viewpoint may serve more than one purpose: most of the example viewpoints are "designing,
deciding" and several are all three (ARCHIMATE §13.4.1).

## The content dimension

| Content | Spans | Typical stakeholder |
|---|---|---|
| **Details** | one layer and one aspect | a software engineer building a component; a process owner |
| **Coherence** | several layers *or* several aspects | an operational manager responsible for a set of IT services or processes |
| **Overview** | several layers *and* several aspects | enterprise architects, CEOs, CIOs |

**Trap:** the content categories are defined by the *core framework*, layers by aspects. A view of
one application component and its data objects spans one layer and two aspects — that is
coherence, not details. A view of business processes and the application services serving them
spans two layers — also coherence. Only a view confined to one cell of the framework is "details"
(ARCHIMATE §13.4.1).

## Creating the view

With a governing viewpoint chosen, the architect designs the view: elements and relationships
from the metamodel in a representation suited to the stakeholder. The representation need not be
graphical at all, and the profile mechanism of chapter 14 can drive colour-coded heat maps from
element attributes (ARCHIMATE §13.4.2).

The specification's example viewpoints — the subject of the next lesson — live in Appendix C and
are offered as starting points, not as a closed list (ARCHIMATE §13.5).

## Worked reading

A CIO wants to know which business services would be affected if a data-centre network segment
failed. Concern: impact of change. Purpose: deciding. Content: overview — technology, application
and business layers, structure and behaviour aspects. That profile points at the Layered
viewpoint drawn as a diagram, or at a cross-reference table generated from the same model if the
CIO prefers a list (ARCHIMATE §13.4.1).

## Check yourself

- In one sentence each: what is a view, and what is a viewpoint?
- Which purpose category is served by a cross-reference table?
- Is a view of one layer and two aspects "details" or "coherence"?
