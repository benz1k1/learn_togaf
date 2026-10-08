---
title: "Meaning, Value and the motivation relationships"
unit: A2
objectives: ["A2.3"]
refs: ["ARCHIMATE §6.4", "ARCHIMATE §6.4.1", "ARCHIMATE §6.4.2", "ARCHIMATE §6.4.3", "ARCHIMATE §6.5", "ARCHIMATE §6.6", "ARCHIMATE §6.1", "ARCHIMATE §5.2.3", "ARCHIMATE §5.2.4", "ARCHIMATE §5.7", "ARCHIMATE §C.2", "ARCHIMATE §C.2.4"]
reading_minutes: 9
source: authored
status: draft
---
## Meaning and Value

Different stakeholders attach different value to the same outcome, and give their own
interpretation to the same core element. Two motivation elements capture this (ARCHIMATE §6.4).

| Element | Icon | Definition in short | Attaches to | Typical mistake |
|---|---|---|---|---|
| **Meaning** | a cloud | the knowledge or expertise present in, or the interpretation given to, a concept in a context | any concept; especially passive structure such as a document or message | using Meaning for worth or benefit — that is Value |
| **Value** | an ellipse | the relative worth, utility or importance of a concept | any concept; typically a service, product or outcome, and optionally the stakeholder it is worth something to | assuming value must be money — non-monetary value counts |

A **meaning** describes the intent of an element: how it *informs* whoever reads it. It is used
above all for passive structure — a document, a message — and the same element can mean different
things to different users (a "registration confirmation" to a client is a "client mutation" to the
CRM department), while several representations may carry the same meaning. It may be associated
with any concept, and with a stakeholder to say whose interpretation it is. Name it with a noun
phrase (ARCHIMATE §6.4.1).

A **value** is the usefulness, advantage, benefit or gain something offers a customer,
stakeholder or end user — from selling a product, using a service, completing an activity. Money is
the obvious case but functional value and the value of information or knowledge are explicitly
included, and value most typically sits in a customer–provider relationship. It may be associated
with any concept and with the stakeholder for whom it holds; where the value is functional, the
recommended name is the action or state the element makes possible (ARCHIMATE §6.4.2).

In the worked example, sending push notifications has the value "cost efficiency" for the insurer
and "being informed" and "peace of mind" for the customer, and each kind of notification message
carries its own meaning — "claim has been received", "claim has been paid" (ARCHIMATE §6.4.3).

**Trap:** which element represents "peace of mind" for a customer? **Value**. Which represents what
a "payment complete" message tells the customer? **Meaning**. Both are motivation elements with
diagonal corners, not business objects (ARCHIMATE §6.4.3).

## The motivation relationships

Three relationships do almost all the work among motivation elements, and between motivation
elements and the rest of the model (ARCHIMATE §6.1, §6.6).

<figure class="max-w-lg"><img src="/figure/ARCHIMATE:fig-45" alt="Relationships between motivation elements and core elements" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 45. Relationships Between Motivation Elements and Core Elements (ARCHIMATE)</figcaption></figure>

| Relationship | Notation | Meaning here | Where it is used |
|---|---|---|---|
| **Realization** | dotted line, hollow triangle head | the source is critical to bringing the target about | outcome → goal; principle → outcome/goal; requirement → principle/goal; core element → requirement |
| **Influence** | dashed line, open arrowhead, optional + / − | the source affects the achievement of the target, but is not critical to it | any motivation element → any motivation element; core element → motivation element |
| **Association** | plain line, optionally directed | an unspecified link | stakeholder — driver; driver — assessment; meaning / value — any concept; stakeholder — meaning / value |

**Realization** should be used only when the source is *critical* to the existence or
achievement of the target; the specification's example is a construction crew (a business actor)
that realizes the goal of constructing a building. **Influence** is for contributions that are
*not* critical — adding skilled workers to a crew that is already adequate influences the goal
without realizing it. Influence can be positive (contributes to) or negative (counteracts), with
the sign or strength shown as an attribute such as "+", "−", "++" or a number (ARCHIMATE §5.2.3).

Influence works in two directions of the model. *Vertically*, from core elements upward through
requirements and principles to goals, it gives a traceable path that explains why a particular
application component matters to a corporate goal — the basis for impact analysis. *Horizontally*,
between motivation elements, it captures that achieving one goal to some degree changes the degree
to which another is achieved: improving reputation raises customer satisfaction; laying off staff
lowers reputation, and so indirectly satisfaction (ARCHIMATE §5.2.3).

**Association** is always permitted between any two elements, or between a relationship and an
element, and is the right choice when nothing more specific applies or when a first, high-level
sketch has not yet been refined. In the motivation metamodel it is the relationship of stakeholder
to driver and of meaning and value to whatever they describe (ARCHIMATE §5.2.4, §6.1).

**Trap:** an option offering *serving*, *access*, *triggering* or *flow* between two motivation
elements is wrong; those are core-element relationships. Between motivation elements you have
realization, influence, association, and the structural triple composition / aggregation /
specialization among elements of the same type (ARCHIMATE §6.1).

## Motivation elements and core elements

Every motivation element is meant to explain a core element, so the two must be able to connect.
The rules are few: a **requirement** — and through it a principle, outcome or goal — may be
*realized* by a structure or behaviour element; the weaker *influence* is also allowed; **meaning**
and **value** may be *associated* with any structure or behaviour element; and a business internal
active structure element (actor, role or collaboration) may be *assigned* to a **stakeholder**, to
say that someone with an operational position is also a stakeholder (ARCHIMATE §6.6).

**Trap:** how do you show that the "Head of Claims" business role is a stakeholder? Draw an
**assignment** from the Business Role to the Stakeholder — not a realization, and not by reusing
the role as a stakeholder (ARCHIMATE §6.6).

Indirect relationships can be derived through chains — a component that realizes a requirement
that realizes a principle that realizes a goal yields a derived realization from component to goal
— and Appendix B lists every permitted direct and derived pair (ARCHIMATE §5.7).

## Viewpoints on the motivation aspect

Appendix C defines six motivation viewpoints: Stakeholder, Goal Realization, Goal Contribution
(influence between goals and requirements), Principles, Requirements Realization, and the
all-purpose **Motivation viewpoint**, which admits every motivation element and is used for a
complete or partial overview relating stakeholders, goals, principles and requirements; its
purpose is designing, deciding and informing (ARCHIMATE §C.2, §C.2.4).

## Summary

| Element | Definition (restated) |
|---|---|
| Meaning | the interpretation given to, or knowledge held in, a concept in a context |
| Value | the relative worth, utility or importance of a concept |

(ARCHIMATE §6.5)
