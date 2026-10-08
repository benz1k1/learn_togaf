---
title: "Business Model Diagram as an ArchiMate Strategy view — Digital Channels"
deliverable: Business Model Diagram as an ArchiMate view
phase: A
kind: MODEL
track: ARCHIMATE
summary: "The retail line's business model canvas drawn with strategy elements: the value proposition as a Value, segments and partners as Stakeholders, key activities as Capabilities realizing one Course of Action, key resources as Resources."
refs: ["ARCHIMATE §C.3", "CONTENT §3.6.3"]
figure: BUSINESS_MODEL_DIAGRAM.svg
viewpoint: Strategy
artefacts: [BUSINESS_MODEL_DIAGRAM]
source: authored
status: draft
---

> **What to notice.** The Strategy viewpoint shows the strategy layer — Resource, Capability, Value Stream, Course of Action — and how it connects to motivation (ARCHIMATE §C.3). A business model canvas is nine boxes of text; drawing it forces each box to become one of these types, and the exam-relevant decision is which. A value proposition is a Value (motivation), a customer segment is a Stakeholder, a key activity is a Capability, a key resource is a Resource, and the strategy that ties them together is a Course of Action. Revenue and cost are Values too, with influence between them.

## How to read the view

Row by row. The top row is the canvas's *create and deliver* side: the two customer segments associated with the value proposition, and beside it the revenue the proposition earns (a "+" influence). The second row holds the Course of Action — the retail line's strategy, "mobile-first everyday banking; reinvest in lending" — associated with the proposition it is meant to deliver and with the cost it is meant to move; a "−" influence from the cost Value to the revenue Value is the *capture* side. The third row is key activities as capabilities, each realizing the course of action (dashed, hollow triangle). The bottom row is key resources, associated with the capability that uses them, and the partners as a Stakeholder associated with the resources they provide.

## Elements and why each type was chosen

| Element | ArchiMate type | Aspect / layer | Why that type |
|---|---|---|---|
| Everyday banking that fits in a pocket | Value | Motivation | The worth of the proposition to the segments; a Value, not a Goal, because it is what the customer gets, not what the bank intends (ARCHIMATE §6.3.8) |
| Interest margin, card interchange, account fees; Cost to serve | Value | Motivation | Revenue and cost are value captured and value spent; both are Values with a sign between them |
| Retail customers, Small business owners, Partners | Stakeholder | Motivation | Segments and partners hold an interest in the model; they do not perform behaviour in this view |
| Mobile-first everyday banking; reinvest in lending | Course of Action | Strategy, behaviour | The plan for configuring capabilities and resources to reach a goal — the definition (ARCHIMATE §7.2.4) |
| Onboarding, Payments, Lending | Capability | Strategy, behaviour | Key activities are abilities the line possesses, drawn at strategy level rather than as processes |
| Branch network, Core Banking, Mobile App, Card licence | Resource | Strategy, passive | Assets owned or controlled; Core Banking is a resource here and an application component in Phase C (ARCHIMATE §7.2.1) |

## Relationships used

| From → to | Relationship | What it says |
|---|---|---|
| Stakeholder — Value | Association | The segment receives the value; Value permits only association (ARCHIMATE §6.5) |
| Value → Value | Influence (+ / −) | The proposition earns the revenue; the cost erodes it |
| Capability → Course of Action | Realization | The course of action is realized by these capabilities (ARCHIMATE §7.4, Example 21) |
| Resource — Capability, Stakeholder — Resource | Association | Resources support a capability and partners supply resources; assignment is the stronger choice but is outside this artefact's mapping |

## What changed from the TOGAF drawing

The canvas had *channels* (branch, Mobile App, card); they are not on the view, because a channel is a business interface and the Strategy viewpoint has none — they reappear in the Business Footprint and Application Cooperation views. The canvas's three prose blocks became eleven typed elements, and the biggest change is that "reinvest profit in the Mobile App and lending capacity", a footnote on the drawing, became the one Course of Action everything else realizes or serves: the notation asks what the model is *for*, and the canvas never had to say.

## Draw it yourself

1. Open a Strategy view; add the value proposition as a Value and the segments as Stakeholders, associated with it.
2. Add revenue and cost as two more Values; draw influence between them and from the proposition to revenue, naming the sign.
3. Add one Course of Action for the line's strategy; associate it with the proposition and the cost.
4. Add key activities as Capabilities and draw realization from each to the course of action.
5. Add key resources as Resources associated with the capability that uses them; add partners as a Stakeholder associated with what they supply.
