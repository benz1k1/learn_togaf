---
title: Gap Analysis, and Interoperability Requirements
unit: F5
objectives: ["5.3", "5.4"]
refs: ["TECH §5", "TECH §5.1", "TECH §5.2", "TECH §6.1", "TECH §6.2", "TECH §6.3", "TECH §6.4", "TECH §6.5", "TECH §6.6", "ADM §9.3.3", "ADM §9.3.5"]
reading_minutes: 10
source: authored
status: draft
---
## Gap analysis — validating what has been left out

Gap analysis is used widely in the ADM to **validate** an architecture under development. Its
premise is to highlight the shortfall between the Baseline and the Target: items deliberately
omitted, accidentally left out, or not yet defined (TECH §5).

Validating means asking what may have been forgotten; the architecture must support all of the
organisation's essential information-processing needs. The most critical source of gaps is
**stakeholder concerns not addressed in earlier work**. Other sources, by domain (TECH §5.1):

| Domain | Example gaps |
|---|---|
| Business | People (cross-training), process inefficiencies, duplicate or missing tools, information, measurement, financial, facilities |
| Data | Data not current enough, not where needed, not the data needed, not available when needed, not created, not consumed, relationship gaps |
| Application | Applications impacted, eliminated or created |
| Technology | Technologies impacted, eliminated or created |

### The matrix

| Step | Action |
|---|---|
| 1 | Baseline ABBs down the **vertical** axis; Target ABBs across the **horizontal** axis |
| 2 | Add a final row **"New"** to the baseline axis and a final column **"Eliminated"** to the target axis |
| 3 | An ABB in both → mark the intersection **"Included"** |
| 4 | A baseline ABB missing from the target → review it; if correctly eliminated mark it so in the Eliminated cell; if not, an accidental omission has been found and the ABB is reinstated in the next iteration |
| 5 | A target ABB with no baseline counterpart → mark it in the New row as a gap to fill by developing or procuring |

When done, everything under "Eliminated" or "New" is a gap, to be explained as correctly
eliminated or marked for reinstatement, development or procurement (TECH §5.2).

> **Trap.** "New" is a *row* on the baseline axis; "Eliminated" is a *column* on the target axis.
> An Eliminated cell can hold either a deliberate removal or an accidental omission — the
> review step is what tells them apart (TECH §5.2).

Gap analysis is performed as a step in each of Phases B, C and D; in Phase E the domain results
are consolidated into a single list — the **Consolidated Gaps, Solutions, and Dependencies
matrix** — which identifies SBBs that could address one or more gaps and their dependencies.
Dependencies are found using views such as the Business Interaction, Data Entity/Business
Function and Application/Function matrices; similar gaps are grouped, with reference to the
Implementation Factor catalog (ADM §9.3.3).

## Interoperability requirements

Interoperability is "the ability to share information and services"; defining *the degree* to
which they are shared is a useful requirement, especially in a complex or extended enterprise.
It appears throughout the ADM: revealed in business scenarios in Phase A; defined in business
terms in B; the content of information exchanges detailed in the Data Architecture and the way
applications share in the Application Architecture (C); technical mechanisms in D; actual
solutions selected in E; logically implemented in F (TECH §6.1).

### Categories

Many organisations categorise interoperability as **operational or business** (how processes are
shared), **information** (how information is shared) and **technical** (how technical services
are shared or connected). From an IT/EAI perspective there is also presentation, information,
application and technical integration (TECH §6.2).

### Operating model, degrees and matrices

The corporate **operating model** — the required level of business process integration and
standardisation — usually indicates the appropriate interoperability approach. It should be
determined in Phase A, if not in Phase B, and definitely by Phase E; an extended enterprise may
have a different model from the internal one (TECH §6.3).

Implementing interoperability needs realistic **SMART** standards and clear measures. An example
scheme is the four *Degrees of Interoperability*: 1 unstructured data exchange; 2 structured data
exchange with manual handling; 3 seamless sharing of data on a common exchange model; 4 seamless
sharing of information through co-operating applications. Degree 3 can be refined further (3A
formal message exchange … 3D real-time). Measures go into the strategic direction and the
transformation strategy, and the consolidated gap results are updated afterwards (TECH §6.4).

Co-existence of old and new systems is the hard part; operations staff must be involved, and a
"wrapper" between a legacy application and new infrastructure may become permanent. A
**Business Information Interoperability Matrix** starts in Phase B (sharing between stakeholders)
and evolves in Phase C into an **Information Systems Interoperability Matrix** (specific systems,
refined degrees). Sharing is not necessarily symmetrical (TECH §6.5).

### Reconciling with solutions

The biggest issue when re-using SBBs or COTS is **business interoperability**: packages embed
their own business processes, and changing them can cost more than re-use saves. Any change to
business interoperability requirements must be signed off by the Business Architects and sponsors
in a **revised Statement of Architecture Work** (TECH §6.6). In Phase E the requirements from
earlier phases are consolidated and conflicts minimised; there are two basic responses to a
conflict — create a building block that translates between the conflicting ones, or change the
specification of the conflicting building blocks (ADM §9.3.5).

## Check yourself

- Which axis carries the "Eliminated" column?
- In which phase is the operating model "definitely" needed, at the latest?
- What document records an agreed change to business interoperability requirements?
