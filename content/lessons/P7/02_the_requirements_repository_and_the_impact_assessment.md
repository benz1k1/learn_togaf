---
title: The Architecture Requirements Repository, three levels and one impact assessment
unit: P7
objectives: ["P7.1"]
refs: ["CONTENT §7.6", "CONTENT §7.6.1", "CONTENT §7.6.2", "CONTENT §7.7", "CONTENT §3.6.10", "CONTENT §4.2.18", "CONTENT §4.2.11", "ADM §13.2", "ADM §13.4", "ADM §13.5.1", "ADM §12.3.7", "APPLY §3.2"]
reading_minutes: 8
source: authored
status: draft
---
## Why the repository is the exam's favourite artefact

A Requirements Management scenario usually ends by asking where something is recorded and
who maintains it. The Architecture Requirements Repository is used by all phases to record
and manage all information relevant to the architecture requirements, at strategic, segment
and capability level; requirements can be gathered at every stage and must be approved
through the phases and governance processes; and the Requirements Management phase is
responsible for the repository's contents, integrity and availability to every phase
(CONTENT §7.6.1). A populated Architecture Repository is itself an input to Requirements
Management, alongside the Organizational Model, the Tailored Framework, the Statement of
Architecture Work, the Vision, the requirements populating a specification, and the
Requirements Impact Assessment (ADM §13.2).

## Three levels of granularity

Because of the volume and the diversity of stakeholder needs, the repository divides
requirements into three levels (CONTENT §7.6.2):

| Level | What it holds | Who it serves |
|---|---|---|
| Strategic Architecture Requirements | a long-term summary view of requirements for the entire enterprise; operational and change requirements for direction setting | executives |
| Segment Architecture Requirements | more detailed operating-model requirements for areas of the enterprise; program or portfolio level change | portfolio and programme owners |
| Capability Architecture Requirements | detailed requirements for a unit of capability; requirements for individual work packages and projects grouped in portfolios and programs | project teams |

Those three match the Architecture Landscape's Strategic, Segment and Capability
Architectures, which is why a scenario about an enterprise-wide strategy requirement and a
scenario about a single project's requirement expect different repository entries
(APPLY §3.2). When a requirement's business outcome is reflected in the Solutions Landscape
over time, the requirement is met and archived for audit (CONTENT §7.6.2); the Solutions
Landscape holds the SBBs that realise the ABBs, classified as strategic, segment or
capability (CONTENT §7.7).

**Trap.** "Met" requirements are archived, not deleted. An answer that purges satisfied
requirements loses the audit trail the standard says to keep (CONTENT §7.6.2).

<figure class="my-4">
<svg viewBox="0 0 760 260" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="11" role="img" aria-label="The Architecture Requirements Repository holds strategic, segment and capability requirements across cycles; each cycle has its own Architecture Requirements Specification and Requirements Impact Assessment; met requirements are archived when the Solutions Landscape realises them">
<defs><marker id="arr-p7q" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
<rect x="15" y="15" width="330" height="200" rx="10" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="180" y="38" text-anchor="middle" font-weight="bold">Architecture Requirements Repository</text>
<text x="180" y="54" text-anchor="middle">spans ADM cycles (ADM §13.5.1)</text>
<g fill="#fff" stroke="#7aa2e3">
<rect x="35" y="70" width="290" height="34" rx="6"/>
<rect x="35" y="112" width="290" height="34" rx="6"/>
<rect x="35" y="154" width="290" height="34" rx="6"/>
</g>
<text x="180" y="91" text-anchor="middle">Strategic: enterprise-wide, direction setting</text>
<text x="180" y="133" text-anchor="middle">Segment: operating model, program or portfolio</text>
<text x="180" y="175" text-anchor="middle">Capability: unit of capability, work packages, projects</text>
<rect x="400" y="15" width="345" height="90" rx="10" fill="#e3f5e1" stroke="#7fbf7a"/>
<text x="572" y="38" text-anchor="middle" font-weight="bold">one ADM cycle</text>
<text x="572" y="58" text-anchor="middle">Architecture Requirements Specification (in scope of the SoAW)</text>
<text x="572" y="76" text-anchor="middle">Requirements Impact Assessment, version n, n+1 ...</text>
<text x="572" y="94" text-anchor="middle">updated once the cycle's requirements are final (ADM §13.4)</text>
<line x1="345" y1="60" x2="400" y2="60" stroke="#555" marker-end="url(#arr-p7q)"/>
<line x1="400" y1="80" x2="345" y2="80" stroke="#555" marker-end="url(#arr-p7q)"/>
<rect x="400" y="130" width="345" height="60" rx="10" fill="#fff1d6" stroke="#e0b060"/>
<text x="572" y="152" text-anchor="middle" font-weight="bold">Solutions Landscape</text>
<text x="572" y="170" text-anchor="middle">SBBs realising the ABBs; when the outcome is reflected here,</text>
<text x="572" y="184" text-anchor="middle">the requirement is met and archived for audit (CONTENT §7.6.2)</text>
<line x1="345" y1="170" x2="400" y2="170" stroke="#555" stroke-dasharray="4 3" marker-end="url(#arr-p7q)"/>
<text x="380" y="240" text-anchor="middle" fill="#666">Requirements Management owns the repository's contents, integrity and availability to every phase (CONTENT §7.6.1)</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">The repository across cycles, the per-cycle documents, and the archive trigger. Original drawing; the levels follow CONTENT §7.6.2.</figcaption>
</figure>

## The Requirements catalog and the impact assessment

The Requirements Management phase's artefact is the Requirements catalog, which captures the
things the enterprise needs to do to meet its objectives; requirements generated from
architecture engagements are typically implemented through change initiatives scoped in
Phase E, and the catalog doubles as a quality assurance tool to check that an architecture
is fit for purpose. It holds four metamodel entities: requirement, assumption, constraint and
gap (CONTENT §3.6.10). When a scenario asks which artefact records an assumption the
project is relying on, that is the answer.

The Requirements Impact Assessment assesses the current requirements and specification to
identify the changes to make and their implications, and it carries the reference to the
specific requirements, the stakeholder priority to date, the phases to be revisited, the
phase to lead on prioritisation, the results of phase investigations and revised
priorities, recommendations on management of the requirements, and a repository reference
(CONTENT §4.2.18). A Change Request carries the same impact assessment inside it, together
with the description and rationale for the proposed change (CONTENT §4.2.11), so an answer
that raises a Change Request without an impact assessment has produced half a deliverable.
The outputs of the Requirements Management phase are exactly the Requirements Impact
Assessment and, if necessary, an updated Architecture Requirements Specification
(ADM §13.4).

**Trap.** The impact assessment is versioned. Step 6 issues "version n+1" and the statement
goes through iterations until a final version includes the full implications, such as cost,
timescales and business metrics (ADM §13.4). An answer that issues one assessment and
treats it as final before the phase investigations are done has stopped early.

## Phase H and the repository

Changes implemented in Phase H must be captured and documented in the Architecture
Repository (ADM §12.3.7), and requirements arising from Phase H enter the Requirements
Management steps table at step 7 so that new or changing requirements derived from change
management are managed like any other. Together with the routing rule for out-of-scope
requirements, this is how the repository accumulates requirements across cycles while the
specification stays bound to one Statement of Architecture Work (ADM §13.5.1).

## How the 5, 3 and 1 differ

| Answer | Why it scores that |
|---|---|
| 5 | Records the requirement at the right level (strategic, segment or capability) in the Architecture Requirements Repository, keeps the in-scope portion in the specification, issues and iterates a Requirements Impact Assessment with phases to revisit and a repository reference, and archives satisfied requirements when the Solutions Landscape realises them |
| 3 | Records everything in the Architecture Requirements Specification, including requirements for a later cycle; the specification is bound to the current cycle and the repository is where cross-cycle requirements live (ADM §13.5.1) |
| 1 | Writes a Change Request with a description and rationale but no impact assessment, so nobody knows which phases must be revisited (CONTENT §4.2.11) |
| 0 | Deletes satisfied requirements to keep the catalog "current"; met requirements are archived for audit (CONTENT §7.6.2) |

## Where to look in the book

Architecture Content §7.6 for the repository's purpose and the three levels, §7.7 for the
Solutions Landscape, §3.6.10 for the Requirements catalog entities, §4.2.18 for the impact
assessment contents and §4.2.11 for the Change Request. ADM §13.2 for the inputs, §13.4 for
the outputs and the versioning, §13.5.1 for which documents span cycles. Applying the ADM
§3.2 for the three Architecture Landscape levels the repository mirrors.

## Check yourself

- Name the four entities in the Requirements catalog.
- What event causes a requirement to be archived?
- Which two documents does the Requirements Management phase output?
