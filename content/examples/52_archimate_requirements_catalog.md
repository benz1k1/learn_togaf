---
title: "Requirements Catalog as an ArchiMate Requirements Realization view — Digital Channels"
deliverable: Requirements Catalog as an ArchiMate view
phase: REQ
kind: MODEL
track: ARCHIMATE
summary: "Five catalog rows as Requirements and Constraints: each realizes the goal above it and is realized by the business service below it, with constraints influencing the requirements they shape."
refs: ["ARCHIMATE §C.2", "CONTENT §3.6.10"]
figure: REQUIREMENTS_CATALOG.svg
viewpoint: Requirements Realization
artefacts: [REQUIREMENTS_CATALOG]
source: authored
status: draft
---

> **What to notice.** A catalog row says *what* is required and *who raised it*; the Requirements Realization viewpoint (ARCHIMATE §C.2) adds *why* and *by what*. Every **Requirement** on this view sits between a **Goal** it realizes and a **Business Service** that realizes it. A requirement with nothing above it has no justification; one with nothing below it has no owner in the architecture. Both are findings the Requirements Management phase exists to catch (CONTENT §3.6.10), and on this view they are visible as a missing line.

## How to read the view

Top to bottom, three rows. **Goals**: 60% of transfers in the Mobile App, card fraud losses down 30%, ten-minute onboarding. **Requirements and Constraints**: RQ-01 (app transfer within ten seconds), RQ-04 (card blocked within five seconds), RQ-02 (every card transaction scored before authorisation), CN-01 (Core Banking stays system of record) and RQ-03 (same KYC rule set at counter and in app). **Business Services**: Transfer funds, Authorise card payment, Maintain customer and account records, Open account.

Follow a column. RQ-01 realizes the mobile-transfers goal and is realized by Transfer funds. RQ-02 and RQ-04 both realize the fraud goal and both are realized by Authorise card payment — one service, two requirements, which is why the Card Switch change in WP-4 is a single deliverable. The two chamfered boxes with the slash icon are **Constraints**. CN-02, the card re-issue date, **influences** RQ-01 ("fixes the date"); CN-01 influences RQ-03 because a shared KYC rule set has to write to the one system of record. A constraint is not realized by a goal — it is imposed from outside — but it is still realized by the service that honours it.

## Elements

| Element | ArchiMate type | Aspect / layer | Why that type |
|---|---|---|---|
| 60% of transfers in the app; fraud losses down 30%; ten-minute onboarding | Goal | motivation | The intent each requirement serves |
| RQ-01, RQ-02, RQ-03, RQ-04 | Requirement | motivation | A statement of need the architecture must realize |
| CN-01, CN-02 | Constraint | motivation | A requirement imposed from outside, not negotiable within the project |
| Transfer funds; Authorise card payment; Maintain customer and account records; Open account | Business Service | behaviour, Business | The architecture element that satisfies the requirement |

## Relationships used

| Relationship | Notation | What it says here |
|---|---|---|
| Realization (requirement → goal) | dashed, hollow triangle | Meeting the requirement is how the goal is achieved |
| Realization (business service → requirement or constraint) | dashed, hollow triangle | The service is what satisfies it |
| Influence (constraint → requirement), labelled | dashed, open arrowhead | The constraint shapes the requirement without being realized by it |

## What changed from the TOGAF drawing

The catalog has five rows of five types: requirement, assumption, constraint, gap, plus *raised in* and *priority*. Two rows do not become elements. AS-01, the assumption that the card network keeps its ISO 8583 version, has no motivation type — ArchiMate treats an assumption as an Assessment or a property, and here it becomes a note. GP-01, the missing fraud-scoring capability, is a Gap, an implementation-and-migration element that belongs on the Migration view, where it is drawn between the Baseline and Transition 1 plateaus. *Raised in* and *priority* become properties on the elements rather than columns. The realizing business services are new: the catalog records that RQ-02 was raised in Phase C, the view records what will satisfy it.

## Draw it yourself

1. Create a *Requirements Realization* view; add the three Goals across the top.
2. Add each RQ as a Requirement and each CN as a Constraint; put the catalog id at the start of the name and *raised in* and *priority* in the Properties tab.
3. Draw Realization from each requirement up to its goal.
4. Add the Business Services and draw Realization from each to the requirements it satisfies; anything unrealized is a gap to raise in Phase E.
5. Draw Influence from each constraint to the requirement it shapes and name the relationship with the effect.
