---
title: Stakeholder Management — identify, classify, decide the approach, tailor the deliverables
unit: F5
objectives: ["5.2"]
refs: ["TECH §3.1", "TECH §3.2", "TECH §3.3", "TECH §3.3.1", "TECH §3.3.2", "TECH §3.3.3", "TECH §3.3.4", "TECH §3.4", "ADM §3.3.2"]
reading_minutes: 9
source: authored
status: draft
---
## Why the technique exists

Stakeholder management is how practitioners win support so that the engagement succeeds. Its
benefits: the most powerful stakeholders are found early and their input shapes the architecture;
their backing brings resources; early and frequent communication builds understanding of the
architecture process; likely reactions can be anticipated and planned for; and conflicting
objectives between stakeholders surface early enough to resolve. Every initiative should identify
who contributes, who gains, who loses, and then decide how to deal with each (TECH §3.1).

## When it is done

Stakeholder analysis is used during **Phase A** to identify the key players and is **updated in
every later phase** — new stakeholders tend to appear as work moves into Opportunities &
Solutions, Migration Planning and Architecture Change Management. Just as a building architect
draws wiring diagrams and floor plans for different audiences, the enterprise architect creates
different architecture views for stakeholders with different concerns. The standard supports this
through four concepts: architecture view, architecture viewpoint, concern and stakeholder
(TECH §3.2).

In the ADM, the Phase A step "Identify Stakeholders, Concerns, and Business Requirements" produces
the **stakeholder map** for the engagement — who is involved, how deeply, and their key concerns —
which then feeds the Architecture Vision (relevant concerns and viewpoints), the Communications
Plan (who to communicate with) and the Statement of Architecture Work (roles and responsibilities)
(ADM §3.3.2).

## The four steps

| Step | What happens |
|---|---|
| 1. Identify stakeholders | Work out who is affected, who has power over the work and who has an interest in its outcome |
| 2. Classify stakeholder positions | Record understanding, commitment and readiness to support, per stakeholder |
| 3. Determine stakeholder management approach | Place stakeholders on the power/interest grid to choose the engagement strategy |
| 4. Tailor engagement deliverables | Decide which catalogs, matrices and diagrams each stakeholder group needs |

(TECH §3.3)

### 1. Identify

Think about everyone affected by, influential over, or interested in the Enterprise Architecture:
executives, project and client roles, developers, partners, suppliers, IT operations, customers.
Do not lean only on the formal organisation chart — informal groups can be just as powerful, and
influencers may hold no formal position. Stakeholders can be organisations or people, but in the
end the team communicates with individuals, so name the right individual in each stakeholder
organisation. A sample analysis distinguishes **22 stakeholder types in five categories**, and
the analysis should cover both the *visible* team (obviously involved) and the *invisible* team
(support providers who must contribute for success) (TECH §3.3.1).

### 2. Classify positions

Record, for the most important stakeholders, their ability to disrupt the change, current and
required understanding, current and required commitment, and required support. Also judge each
person's readiness to act supportively: are they ready to move towards the target, can they be a
credible advocate, how involved do they need to be, and have they made a contractual commitment?
For those whose commitment is critical, note current and desired levels (TECH §3.3.2).

### 3. Determine the approach — the power/interest grid

Work out each stakeholder's power, influence and interest and place them on a **power / level of
interest** matrix, which also indicates the engagement strategy for each quadrant (TECH §3.3.3).

| | Low interest | High interest |
|---|---|---|
| **High power** | Keep Satisfied | **Key Players** |
| **Low power** | Minimal Effort | Keep Informed |

(TECH §3.3.3, Figure 3-2)

> **Trap.** Exam questions swap the axes. Power is the vertical axis, interest the horizontal.
> High power + low interest = *Keep Satisfied*; low power + high interest = *Keep Informed*.
> Only high/high are *Key Players* (TECH §3.3.3).

### 4. Tailor engagement deliverables

Identify the catalogs, matrices and diagrams the engagement must produce and validate with each
stakeholder group, so the architecture can be communicated to, and understood by, every
stakeholder, and each can confirm that their concerns are addressed (TECH §3.3.4).

## The template stakeholder map

The stakeholder map is a table with four columns: **stakeholder**, **key concerns**, **class**
(the grid quadrant, e.g. KEEP SATISFIED, KEY PLAYERS, KEEP INFORMED) and the **catalogs, matrices
and diagrams** that address those concerns. For example, CxOs are concerned with high-level
drivers, goals and objectives and are classed Keep Satisfied; Enterprise Security is a Key Player
concerned with access and tamper protection and is served by Data Security and Network diagrams;
Regulatory Bodies are Keep Satisfied and need the Business Footprint and Application Communication
diagrams (TECH §3.4).

## Check yourself

- Which phase first produces the stakeholder map, and what three outputs does it feed?
- What are the four columns of the template stakeholder map?
- Which quadrant holds a stakeholder with high power but little interest?
