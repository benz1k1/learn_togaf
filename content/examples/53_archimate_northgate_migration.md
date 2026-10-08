---
title: "Architecture Roadmap as an ArchiMate Migration view — Baseline to Target"
deliverable: Architecture Roadmap as an ArchiMate view
phase: E
kind: MODEL
track: ARCHIMATE
summary: "The four states of Northgate's roadmap as Plateaus in triggering order, with the Gap between each pair named from the consolidated gap matrix and a note of what each plateau contains."
refs: ["ARCHIMATE §C.4", "CONTENT §4.2.7", "ADM §9.4"]
figure: northgate_migration.svg
viewpoint: Migration
artefacts: []
source: authored
status: draft
---

> **What to notice.** Only two element types, and the TOGAF vocabulary maps onto them one for one. A Transition Architecture is a **Plateau** — "a relatively stable state of the architecture that exists during a limited period of time" (ARCHIMATE §13.2.4). The output of gap analysis is a **Gap** — "a statement of difference between two plateaus" (ARCHIMATE §13.2.5). The Migration viewpoint (ARCHIMATE §C.4) is defined as exactly these two elements, so the roadmap's Transition Architecture table (CONTENT §4.2.7; ADM §9.4) draws itself without a single modelling decision to argue over.

## How to read the view

Left to right along the top: **Baseline — 2026**, **Transition 1 — Q2 2027**, **Transition 2 — Q4 2027**, and, dropping down because the page is six columns wide, **Target — mid-2028**. The solid arrows between them are **triggering**: one state leads to the next. Under each plateau a note lists what it contains, copied from the roadmap's Transition Architecture table — eleven point-to-point interfaces and a balances-only app in the baseline; the APIs, Mobile App v4 and dual-homing at Transition 1; onboarding and scoring at Transition 2; automatic blocking and the online site retired at the target.

Between each pair of plateaus a **Gap** hangs on two plain association lines. Its name is the consolidated gap the transition closes: *no API layer, app cannot pay, single-homed card link* between Baseline and Transition 1; *no verification or scoring application* between Transitions 1 and 2; *analyst-in-the-loop, online site still live* between Transition 2 and the Target. The gaps are the roadmap's section 3 matrix, one row per line; the plateaus are its section 4 table. The dates in the plateau names are the ones the card re-issue fixed.

## Elements

| Element | ArchiMate type | Aspect / layer | Why that type |
|---|---|---|---|
| Baseline, Transition 1, Transition 2, Target | Plateau | passive, Implementation & Migration | A stable architecture state for a period — TOGAF's baseline, transition and target architectures |
| Three gaps | Gap | passive, Implementation & Migration | What differs between two adjacent plateaus — TOGAF's gap-analysis output |

## Relationships used

| Relationship | Notation | What it says here |
|---|---|---|
| Triggering (plateau → plateau) | solid, filled arrowhead | The sequence of states; a plateau begins when the previous one ends |
| Association (gap — plateau) | plain line | The gap is between these two states; the language uses association here deliberately, since a gap neither realizes nor triggers a plateau |

## What changed from the TOGAF drawing

The roadmap has no single diagram: it is a work package portfolio, a factor catalog, a gap matrix and a transition table. This view draws the last two. The work packages that move the architecture from one plateau to the next are not on it — the Migration viewpoint excludes them so the states stay the subject — and appear on the Implementation and Migration view, where each deliverable realizes the plateau it belongs to. What the notes say is the roadmap table's *Contains* column; what the gaps say is its *Business value released* column read the other way round, as what was missing before.

## Draw it yourself

1. Create a *Migration* view — Archi's palette then offers only Plateau and Gap.
2. Add four Plateaus named state and date; draw Triggering from each to the next.
3. Add a Gap between each pair, named from the consolidated gap matrix; draw Association from the gap to both plateaus.
4. Open each plateau's Properties and record the roadmap table's *Contains* and *Business value released* cells; the notes on this drawing are those properties made visible.
5. When Phase F re-plans a date, change the plateau's name here and nowhere else; every other view that aggregates the plateau follows.
