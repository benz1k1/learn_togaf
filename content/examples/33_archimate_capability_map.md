---
title: "Business Capability Map as an ArchiMate Capability Map view — Digital Channels"
deliverable: Business Capability Map as an ArchiMate view
phase: A
kind: MODEL
track: ARCHIMATE
summary: "Northgate's strategic, core and supporting capabilities as nested Capability elements, with composition for the levels and aggregation where a capability is shared across tiers."
refs: ["ARCHIMATE §C.3", "CONTENT §3.6.3"]
figure: BUSINESS_CAPABILITY_MAP.svg
viewpoint: Capability Map
artefacts: [BUSINESS_CAPABILITY_MAP]
source: authored
status: draft
---

> **What to notice.** The Capability Map viewpoint has exactly one core element type, Capability, and exists to give a structured overview of what the enterprise can do (ARCHIMATE §C.3). The exam question is composition versus aggregation: a level-2 capability that exists only inside its level-1 parent is *composed*; a capability that another tier also draws on is *aggregated*, and the diamond is hollow. The heat-map colour TOGAF paints on the map is not part of the language — a tool may colour, but the model must say it in words or properties.

## How to read the view

Three dashed groupings are the three tiers of the TOGAF map: Core on the left, Strategic and Supporting on the right. Inside Core, each wide capability is a level-1 capability and the three beneath it are its level-2 children; the filled diamonds at the parent end are composition. Two hollow diamonds cross the tier boundary: Risk Management aggregates KYC Review, and Finance aggregates Settlement — the two capabilities the bank's specialists share with a core process. "(changes)" and "(new)" in a name replace the orange heat-map overlay: those are the capabilities the Digital Channels programme touches.

## Elements and why each type was chosen

| Element | ArchiMate type | Aspect / layer | Why that type |
|---|---|---|---|
| Customer Onboarding, Payments, Lending | Capability | Strategy, behaviour | Level-1 abilities the bank possesses; not business functions, which would be *how* the organisation is arranged rather than *what* it can do (ARCHIMATE §7.2.2) |
| Identity Verification, Account Opening, KYC Review, Card Payments, Transfers, Settlement, Loan Origination, Credit Assessment, Loan Servicing | Capability | Strategy, behaviour | Level-2 refinements of the parents |
| Product Management, Strategy and Planning, Risk Management, Finance, Human Resources, Technology | Capability | Strategy, behaviour | The strategic and supporting tiers, same type, different grouping |
| Core, Strategic, Supporting | Grouping | Composite | The tiers are a way of arranging the map, not capabilities themselves (ARCHIMATE §4.5) |

A tempting alternative is to model the tiers as three top-level capabilities that aggregate everything. That adds three elements with no ability behind them; Grouping says "these belong together" without claiming they are anything.

## Relationships used

| From → to | Relationship | What it says |
|---|---|---|
| Level-1 → level-2 capability | Composition | The child is part of exactly one parent and does not exist without it (ARCHIMATE §5.1.1) |
| Risk Management → KYC Review; Finance → Settlement | Aggregation | The specialist tier draws on a capability that also belongs to a core parent; shared parts are aggregated, not composed (ARCHIMATE §5.1.2) |

## What changed from the TOGAF drawing

The TOGAF map nests boxes and colours the ones the engagement changes; nesting is ambiguous (composition? aggregation? just layout?) and colour is invisible to a tool. The view makes both explicit: every nesting became a relationship with a diamond, and the diamond's fill had to be decided for each — which is how the two shared capabilities were found. The heat overlay became a suffix in the name; in Archi it would be a property, `state = changes`, that a view can colour by. The strategic and supporting tiers stayed as groupings, which is an admission that the map has *no* relationship between Product Management and Customer Onboarding, and that is correct: a capability map is a catalogue, not a dependency graph.

## Draw it yourself

1. Open a Capability Map view in Archi; add three Groupings for the tiers.
2. Add level-1 capabilities in the Core grouping and nest the level-2 capabilities inside each; when Archi asks, choose composition.
3. Add the strategic and supporting capabilities in their groupings.
4. Where a specialist capability shares a level-2 with a core parent, draw aggregation from the specialist to it.
5. Add a property `state` (new / changes / unchanged) to each capability and, if you want the heat map back, use a view colour rule on that property.
