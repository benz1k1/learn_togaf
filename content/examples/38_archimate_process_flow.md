---
title: "Process Flow Diagram as an ArchiMate Business Process Cooperation view — Digital Channels"
deliverable: Process Flow Diagram as an ArchiMate view
phase: B
kind: MODEL
track: ARCHIMATE
summary: "\"Open an account\" as a chain of business processes triggered in sequence, the KYC decision as a junction, the three swim lanes as roles assigned to their steps, and the welcome pack as a flow."
refs: ["ARCHIMATE §8.3", "CONTENT §3.6.4"]
figure: PROCESS_FLOW_DIAGRAM.svg
viewpoint: Business Process Cooperation
artefacts: [PROCESS_FLOW_DIAGRAM]
source: authored
status: draft
---

> **What to notice.** The Business Process Cooperation viewpoint shows the relationships of processes to each other and to their environment — the roles that perform them, the events that start them, the information that passes between them (ARCHIMATE §C.1). The exam tests two things on a picture like this: triggering versus flow (triggering is *then*, flow is *something is passed*), and the junction, which is how ArchiMate draws a decision — there is no diamond gateway, there is an And/Or junction with several outgoing triggerings (ARCHIMATE §5.5.1).

## How to read the view

Follow the filled arrowheads. The "Customer walks in" event triggers Submit application; that triggers Verify identity; that triggers the junction, which is the "KYC ok?" decision. Its two outgoing triggerings are named yes and no: yes goes to Select product, then Create account, then Issue card; no goes to Decline application and the "Application declined" end event. The one dashed filled-head line is a flow: Issue card passes the welcome pack to Receive welcome pack, which triggers the "Account open" end event. The three yellow rectangles with the cylinder icon are the roles that were TOGAF's swim lanes, and the dot-to-arrow lines from them are assignments to the steps in their lane.

## Elements and why each type was chosen

| Element | ArchiMate type | Aspect / layer | Why that type |
|---|---|---|---|
| Submit application, Verify identity, Select product, Create account, Issue card, Receive welcome pack, Decline application | Business Process | Business, behaviour | Each is a step with a start and end in a sequence; a process, not a function (ARCHIMATE §8.3.1) |
| Customer walks in, Account open, Application declined | Business Event | Business, behaviour | The start and end circles of the TOGAF flow; an event is something that happens and triggers or is triggered (ARCHIMATE §8.3.4) |
| Customer, Branch Teller, Core Banking (automated role) | Business Role | Business, active | The swim lanes: responsibilities assigned to steps. Core Banking is an application component in Phase C; in this business-layer view its lane is the automated role the system fulfils |
| KYC ok? | Junction (Or) | Relationship connector | A decision is an Or-junction with named outgoing triggerings; ArchiMate has no gateway element |

The "product: welcome pack" and "control: KYC policy" annotations on the TOGAF drawing are not elements here. The welcome pack is what the flow carries, so it is the flow's name; the KYC policy is a Business Object or a Constraint that the Requirements views hold, and the note records it.

## Relationships used

| From → to | Relationship | What it says |
|---|---|---|
| Event → Process, Process → Process, Process → Event | Triggering | Temporal or causal sequence; the source completes, the target starts (ARCHIMATE §5.3.1) |
| Process → Junction → Process | Triggering through a junction | The junction splits the sequence; the outgoing names carry the condition |
| Issue card → Receive welcome pack | Flow | Something (the pack) is transferred; flow says nothing about sequence by itself (ARCHIMATE §5.3.2) |
| Role → Process | Assignment | The role performs the step — the swim lane made explicit (ARCHIMATE §5.1.3) |

## What changed from the TOGAF drawing

Swim lanes are the biggest change: a lane assigns every box inside it implicitly, and the notation has no lanes, so every assignment is a line and the lane for Core Banking had to be given a type. That forced the question the TOGAF drawing dodged — is Core Banking a performer of business behaviour? — and the answer, an automated *role*, is what makes the Phase C application model line up with this one. The decision diamond became a junction with named triggerings, and the "control: KYC policy" label lost its place in the picture, which is right: a control is a constraint on the process, and constraints live in the Motivation and Requirements views, not in the flow.

## Draw it yourself

1. Open a Business Process Cooperation view; add the start event and the processes in order, connected with triggering.
2. At the decision, add an Or-junction; draw triggering into it and two triggerings out, naming them with the conditions.
3. Add the end events and trigger them from the last step of each branch.
4. Add a Business Role per swim lane and draw assignment from the role to each of its steps.
5. Where a step hands something to another, draw flow and name it after the thing passed; do not use flow as a second kind of sequence arrow.
