---
title: "Stakeholder, Driver, Assessment, Goal and Outcome"
unit: A2
objectives: ["A2.1"]
refs: ["ARCHIMATE §6", "ARCHIMATE §6.1", "ARCHIMATE §6.2", "ARCHIMATE §6.2.1", "ARCHIMATE §6.2.2", "ARCHIMATE §6.2.3", "ARCHIMATE §6.2.4", "ARCHIMATE §6.3", "ARCHIMATE §6.3.1", "ARCHIMATE §6.3.2", "ARCHIMATE §6.5", "ARCHIMATE §4.4", "ARCHIMATE §C.2.1"]
reading_minutes: 10
source: authored
status: draft
---
## What the motivation elements are for

The core elements describe the systems that support the enterprise; they say nothing about *why*
those systems are the way they are. The motivation elements fill that gap: they model the
reasons that guide the design or change of an architecture, corresponding to the "Why" column of
the Zachman framework. All of them are drawn with **diagonal corners**, which is how you tell a
motivation element from a structure (square) or behaviour (round) element on sight (ARCHIMATE §6,
§4.4).

The ten elements form two groups. This lesson covers the first five — the ones that describe
*who wants what and why* — and the metamodel that connects them (ARCHIMATE §6.1).

<figure class="max-w-lg"><img src="/figure/ARCHIMATE:fig-34" alt="Motivation elements metamodel" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 34. Motivation Elements Metamodel (ARCHIMATE)</figcaption></figure>

## Stakeholder, Driver, Assessment

Motivation starts with the factors that influence everything else. A **stakeholder** — an
individual, a team, an organization, or a class of them — has interests in the effects of the
architecture. The conditions that motivate the organization are **drivers**; drivers linked to a
stakeholder are commonly called that stakeholder's *concerns*. Enterprises then **assess** those
drivers, typically with a SWOT analysis, to decide how to respond (ARCHIMATE §6.2).

| Element | Aspect | Icon (top-right) | What it represents | Typical mistake |
|---|---|---|---|---|
| **Stakeholder** | motivation | a role-like cylinder outline | the *role* of an individual, team or organization holding interests in the architecture's effects | modelling the CEO as a Business Actor when the question is about concerns; Stakeholder is a role, and a Business Actor may be *assigned* to it |
| **Driver** | motivation | a ship's wheel | an internal or external condition that motivates the organization to set goals and change | assuming every driver needs a stakeholder — external drivers such as new legislation need not have one |
| **Assessment** | motivation | a magnifying glass | the result of analysing the state of affairs against some driver — a strength, weakness, opportunity or threat | drawing the assessment as a Goal; "market share is declining" is a finding, not an intent |

A stakeholder's definition is borrowed from the TOGAF framework: it is a *role*, and it represents
interests. Stakeholders change, set and emphasize goals, and may influence each other. Examples
run from the CEO and shareholders to customers, architects and legislators. Name a stakeholder
with a noun (ARCHIMATE §6.2.1).

A driver can be internal (customer satisfaction, profitability) or external (economic change,
legislation), and an external driver need not be tied to any stakeholder. Name a driver with a
noun (ARCHIMATE §6.2.2).

An assessment reveals strengths and weaknesses (internal) or opportunities and threats
(external). Weaknesses and threats become problems that a goal should negate; strengths and
opportunities can translate straight into goals — the weakness "customers complain about the
helpdesk" leads to the goal "improve helpdesk". Name it with a noun or a very short sentence
(ARCHIMATE §6.2.3).

In the specification's worked example, several C-level stakeholders are associated with drivers
such as market share and profitability; profitability is *composed of* the drivers revenue and
costs; assessments are associated with the drivers; and one assessment *influences* another —
declining market share leads to declining revenue leads to declining profitability (ARCHIMATE
§6.2.4).

**Trap:** which relationship links a Stakeholder to a Driver? **Association**. Which links an
Assessment to a Driver? **Association**. Which links one Assessment to another that it causes?
**Influence**. Drivers decompose with composition or aggregation (ARCHIMATE §6.2.4, §6.1).

## Goal and Outcome

Goals, outcomes, principles, requirements and constraints together express the motivation to
achieve results. A **goal** is what a stakeholder wants to realize; the end results actually
realized are **outcomes** (ARCHIMATE §6.3).

| Element | Icon | Definition in short | Naming |
|---|---|---|---|
| **Goal** | a target (bullseye) | a high-level statement of intent, direction or desired end state | qualitative verbs — "increase", "improve", "easier" |
| **Outcome** | a target with an arrow in it | an end result, effect or consequence of a state of affairs | a result already achieved or expected by a definite point — "first-place customer satisfaction ranking achieved" |

A goal can stand for anything a stakeholder desires — a state of affairs or a produced value —
and goals are typically how success is measured. Goals decompose: "increase profit" into "reduce
cost" and "increase sales". Concrete, quantitative and time-bound results are usually attached as
outcomes rather than written into the goal (ARCHIMATE §6.3.1).

The distinction the exam leans on: **a goal is what you want; an outcome is what you get.**
Outcomes are high-level, business-oriented results produced by *capabilities* (and by the core
elements that realize those capabilities); they are tangible, possibly quantitative, time-related,
and may be associated with assessments. The same outcome can have different value for different
stakeholders. Not every outcome relates to a goal — an outcome can model an *unwanted* effect,
which is useful when designing mitigations; a goal never does (ARCHIMATE §6.3.2).

**Trap:** "Which element models a possibly negative result of a course of action?" — Outcome, not
Goal. "Which element is realized by a capability?" — Outcome (and, further up, Goal). Outcome
names read as achieved states; goal names read as intentions (ARCHIMATE §6.3.2).

## How they relate

Reading the metamodel from left to right: stakeholders are *associated* with drivers; drivers
are *associated* with assessments; assessments and drivers *influence* goals and outcomes; an
outcome *realizes* a goal; and every motivation element may compose, aggregate or specialize
another of the same type, and *influence* any other motivation element. The full table of
permitted relationships is Appendix B, because the figure shows only the direct ones (ARCHIMATE
§6.1, §6.3.6).

These five elements are exactly the content of the **Stakeholder viewpoint**, whose purpose is
designing, deciding and informing about the stakeholders, their drivers, the assessments of those
drivers and the initial goals that answer them (ARCHIMATE §C.2.1).

## Summary table

| Element | Definition (restated) | Corner shape |
|---|---|---|
| Stakeholder | the role of a person, team or organization with interests in the architecture's effects | diagonal |
| Driver | a condition, inside or outside, that motivates goals and change | diagonal |
| Assessment | the outcome of analysing the enterprise against a driver | diagonal |
| Goal | a high-level intent, direction or desired end state | diagonal |
| Outcome | an end result, effect or consequence | diagonal |

(ARCHIMATE §6.5)
