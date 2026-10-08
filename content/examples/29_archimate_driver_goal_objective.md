---
title: "Driver/Goal/Objective Catalog as an ArchiMate Goal Realization view — Digital Channels"
deliverable: Driver/Goal/Objective Catalog as an ArchiMate view
phase: B
kind: MODEL
track: ARCHIMATE
summary: "Five catalog rows drawn as Driver → Goal → Outcome chains: the driver influences the goal and the measurable objective is the outcome that realizes it."
refs: ["ARCHIMATE §C.2", "CONTENT §3.6.4"]
figure: DRIVER_GOAL_OBJECTIVE_CATALOG.svg
viewpoint: Goal Realization
artefacts: [DRIVER_GOAL_OBJECTIVE_CATALOG]
source: authored
status: draft
---

> **What to notice.** The Goal Realization viewpoint shows how high-level goals are refined into concrete outcomes and requirements (ARCHIMATE §C.2). The exam cares about one distinction above all: a Goal is an intended end state, an Outcome is an end result that has been *achieved or can be measured*. TOGAF's "objective" — time-bound, with a number in it — is therefore an Outcome, not a second Goal. The other question is direction: a Driver *influences* a goal, it does not realize it; a driver is a condition, and conditions do not achieve anything.

## How to read the view

One catalog row per line of the diagram: the Driver on the left, the Goal it motivates in the middle, the Outcome that states what "achieved" looks like on the right. The dashed open-headed lines from driver to goal are influence with a "+" sign; the dashed hollow-triangle lines from outcome to goal are realization, and they point *left*, towards the goal, because the outcome is the concrete thing and the goal the abstract thing it realizes. Nothing connects the rows: the catalog is cross-organisational and the five drivers are independent, which the view makes visible by leaving the space empty.

## Elements and why each type was chosen

| Element | ArchiMate type | Aspect / layer | Why that type |
|---|---|---|---|
| Customers expect digital banking; Rising card fraud; Cost pressure; New capital rules; Small-business demand | Driver | Motivation | External and internal conditions that create the motivation to change; none of them is something the bank decided (ARCHIMATE §6.2.2) |
| Grow mobile adoption; Reduce fraud losses; Lower cost to serve; Stay compliant; Grow lending | Goal | Motivation | Statements of intent with no measure attached |
| 60% of transfers in the Mobile App by end 2027; Card fraud losses cut 30% within 12 months; Branch time on account opening halved; Regulatory reports from one data source; 80% of small loans approved within a day | Outcome | Motivation | Each carries a number and a date — the definition of a measurable end result (ARCHIMATE §6.3.4) |

Two catalog columns have no element. The *measure* (mobile share of transfers, fraud loss per 1,000 cards, minutes per onboarding, reports with manual rework, median decision time) is a property of the Outcome, because the measure is how you know the outcome has happened. The *organization unit* is a Business Actor and belongs in the Organization view; putting Retail Banking or Finance on a motivation view would need an association that says nothing the Organization view does not already say better.

## Relationships used

| From → to | Relationship | What it says |
|---|---|---|
| Driver → Goal | Influence (+) | The condition strengthens the case for the goal; it does not achieve it (ARCHIMATE §5.2.3) |
| Outcome → Goal | Realization | If this measurable result is reached the goal is achieved (ARCHIMATE §5.1.4) |

## What changed from the TOGAF drawing

The catalog is a five-column table; two of its columns turn out not to be elements at all, and one of them ("objective") changes type. That is the real lesson of this view: TOGAF uses *goal* and *objective* as two levels of the same thing, ArchiMate says one is intent and the other is result, and the moment you draw them the difference is enforced by the shape of the relationship — you cannot draw a Goal realizing a Driver, and a tool will refuse an Outcome without a measure only if you have written one. The empty space between rows is also new information: the catalog looked like a list of related things, and it is five unrelated things.

## Draw it yourself

1. Start a Goal Realization view; add one Driver per catalog row on the left.
2. Add the Goal next to each and draw influence from driver to goal; name the relationship "+".
3. Rewrite each objective as an Outcome with its number and date in the name; draw realization from outcome to goal.
4. Put the measure in an Outcome property (Archi: Properties tab, key "measure").
5. Leave the organisation unit out; note its name in the Outcome's documentation so the Organization view can pick it up.
