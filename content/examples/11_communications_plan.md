---
title: Communications Plan — Digital Channels architecture
deliverable: Communications Plan
phase: A
kind: DELIVERABLE
summary: Who hears what, how and when about the architecture, grouped by communication need; produced in Phase A and used through Phase F.
refs: ["CONTENT §4.2.12", "ADM §3.4"]
source: authored
status: draft
---

> **What to notice.** Four headings, straight from the contents list: stakeholder groups by communication need; needs, key messages, risks and critical success factors; mechanisms; timetable. The plan exists because architecture information is large and interdependent and the standard treats getting the right piece to the right stakeholder at the right time as a critical success factor. It is a Phase A output and a Phase B–F input; Phase G's governance inputs do *not* list it (a known exam trap).

| | |
|---|---|
| Reference | CP-2026-01, version 1.0, 31 March 2026 |
| Owner | Chief Architect; merged into the programme's PRINCE2 communication approach at Phase F |

## 1. Stakeholder groups by communication requirement

| Group | Members | What they need from communication |
|---|---|---|
| Decide | Head of Retail, CIO, CFO delegate, Architecture Board | Enough to approve each gate: options, cost, risk, what changes |
| Shape | Compliance Officer, Cards Ops Lead, Digital product owner, Core Banking lead | Early sight of designs that touch their controls or systems, and a way to object |
| Prepare | Branch Council, Cards Operations analysts, Retail IT delivery teams | What will change for them and when, in their own terms |
| Know | The rest of the bank; the Core Banking and Card Switch vendors; the card network | Awareness, and for vendors, the interfaces and dates that bind them |

## 2. Communication needs, key messages, risks and critical success factors

| Group | Key messages tied to the Architecture Vision | Risk if it fails | Critical success factor |
|---|---|---|---|
| Decide | "Core Banking stays; we add a service layer and two bought engines; mobile payments before the card re-issue" | Gate decisions slip; the re-issue date is missed | Every gate paper is four pages with the decision on page one |
| Shape | "Your rules do not change; where they run does" (Compliance, Cards Ops); "one API for every channel" (product owner) | Late objections rework Phases C–D | Design reviews before the gate, not at it |
| Prepare | "Counters keep opening accounts, in ten minutes instead of forty-five"; "analysts keep the final say for six months" | Branch and analyst resistance; readiness risk R-1 materialises | Branch Council and analyst representatives attend the Business Scenario review |
| Know | "The bank is building the platform behind Digital First" | Rumour, vendor surprise | One read-only repository page everyone can find |

## 3. Mechanisms

| Mechanism | Used for | Owner |
|---|---|---|
| Architecture Board gate paper and meeting | Decide | Chief Architect |
| Design review sessions (90 minutes, before each gate) | Shape | Domain architect |
| Repository read-only pages, updated at every gate | Know, Shape | EA team |
| Branch Council and Cards Operations team meetings, EA attending | Prepare | Business architect |
| Fortnightly EA surgery | Prepare (delivery teams), Shape | Rotating architect |
| Vendor working sessions with the interface catalog | Know (vendors) | Application architect |
| One-page "what changes for you" sheets per role | Prepare | Business architect, from the Organization/Actor catalog |

## 4. Communications timetable

| When | What | To whom | Where |
|---|---|---|---|
| 31 Mar 2026 | Architecture Vision published; Board approval | All groups | Repository; Board |
| Apr 2026 | Business Architecture design review; Branch Council briefing | Shape; Prepare (branches) | EA room; Branch Council |
| May–Jun 2026 | Data and application reviews; Compliance review of KYC data flow; vendor session on interfaces | Shape; Know (vendors) | EA room; vendor calls |
| Jul 2026 | Technology review including external security review; Cards Operations briefing on scoring-before-authorisation | Shape; Prepare (analysts) | EA room; Operations Centre |
| 29 Aug 2026 | Roadmap and Transition Architectures published; Board gate | Decide; Know | Board; repository |
| 26 Sep 2026 | Implementation and Migration Plan gate; Investment Committee paper | Decide | Board; Investment Committee |
| Oct 2026 onward | Hand-over to the programme's communication approach; EA surgery continues | Prepare; Know | Programme |
