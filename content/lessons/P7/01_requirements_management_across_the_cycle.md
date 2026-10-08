---
title: Requirements Management in practice, the process that never disposes of a requirement
unit: P7
objectives: ["P7.1"]
refs: ["ADM §13", "ADM §13.1", "ADM §13.2", "ADM §13.3", "ADM §13.4", "ADM §13.5.1", "ADM §13.5.2", "ADM §13.5.3", "CONTENT §4.2.18", "CONTENT §7.6", "TECH §6.6"]
reading_minutes: 10
source: authored
status: draft
---
## What a Requirements Management scenario looks like

Halfway through Phase C a regulator publishes a new rule, a business unit discovers a need
nobody captured in Phase A, or Phase H sends back a change that alters what the target must
do. The scenario then asks what the architecture team should do with the new requirement:
stop, absorb it, defer it, or ignore it. The trap is to treat Requirements Management as
either a filing cabinet or a decision-maker. It is neither. Its objectives are to keep the
process operating for every phase, to manage the requirements found during any execution of
the cycle or a phase, and to make the relevant requirements available to each phase as it
runs (ADM §13.1). The circle at the centre of the ADM graphic means the method is
continuously driven by requirements, and that the circle is a dynamic process, not a static
list (ADM §13.5.1).

The five-point answer identifies and records the requirement, has the phase architects and
stakeholders prioritise it, generates a Requirements Impact Assessment that names the phases
to revisit, lets the current phase decide whether to implement or defer, and updates the
repository. The three-point answer records and assesses but lets the Requirements Management
process decide the priority itself. The one-point answer restarts the cycle at Phase A. The
zero-point answer parks the requirement until the current phase ends.

## The one sentence that decides most questions

"The Requirements Management process itself does not dispose of, address, or prioritize any
requirements; this is done within the relevant phase of the ADM. It is merely the process for
managing requirements throughout the overall ADM" (ADM §13.5.1). Every answer that has the
Requirements Management function accept, reject, rank or implement a requirement on its own
authority violates that sentence, however sensible it sounds. The phase disposes; the process
manages.

The steps table makes the split explicit by putting each step in one of two columns
(ADM §13.3):

| Requirements Management steps | ADM phase steps |
|---|---|
| 2 Establish baseline requirements: priorities, stakeholder agreement, document in the Architecture Requirements Specification and Requirements Repository | 1 Identify requirements (value streams, business scenarios, user experiences, management information) and document them |
| 3 Monitor baseline requirements | 4 Identify new and changed requirements: remove, add, modify and re-assess priorities |
| 5 Identify changed requirements and record priorities: the architects of the current phase and the stakeholders prioritise; conflicts are managed to a conclusion; a Requirements Impact Assessment is generated to steer the team; stakeholder satisfaction with the decisions is determined | 6 Assess the impact on the current phase and previous phases; decide whether to implement or defer to a later cycle; issue Requirements Impact Assessment version n+1 |
| 8 Update the Architecture Requirements Repository, including stakeholder views affected | 7 Implement requirements arising from Phase H |
|  | 9 Implement the change in the current phase |
|  | 10 Assess and revise gap analysis for past phases; address gap requirements |

<figure class="my-4">
<svg viewBox="0 0 760 300" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="11" role="img" aria-label="Requirements Management: the centre process records, monitors, prioritises with the phase, assesses impact and updates the repository; the phases identify, decide to implement or defer, and implement">
<defs><marker id="arr-p7r" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
<rect x="15" y="15" width="300" height="240" rx="10" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="165" y="38" text-anchor="middle" font-weight="bold">Requirements Management (the centre)</text>
<text x="165" y="54" text-anchor="middle">manages; never disposes, addresses or prioritises alone (ADM §13.5.1)</text>
<g fill="#fff" stroke="#7aa2e3">
<rect x="35" y="70" width="260" height="34" rx="6"/>
<rect x="35" y="112" width="260" height="34" rx="6"/>
<rect x="35" y="154" width="260" height="46" rx="6"/>
<rect x="35" y="208" width="260" height="34" rx="6"/>
</g>
<text x="165" y="91" text-anchor="middle">2 baseline requirements, stakeholders agree priorities</text>
<text x="165" y="133" text-anchor="middle">3 monitor the baseline</text>
<text x="165" y="173" text-anchor="middle">5 record changed requirements and new priorities,</text>
<text x="165" y="189" text-anchor="middle">generate the Requirements Impact Assessment</text>
<text x="165" y="229" text-anchor="middle">8 update the Architecture Requirements Repository</text>
<rect x="445" y="15" width="300" height="240" rx="10" fill="#e3f5e1" stroke="#7fbf7a"/>
<text x="595" y="38" text-anchor="middle" font-weight="bold">The ADM phase (Preliminary to H)</text>
<text x="595" y="54" text-anchor="middle">identifies, prioritises with the centre, decides, implements</text>
<g fill="#fff" stroke="#7fbf7a">
<rect x="465" y="70" width="260" height="34" rx="6"/>
<rect x="465" y="112" width="260" height="34" rx="6"/>
<rect x="465" y="154" width="260" height="46" rx="6"/>
<rect x="465" y="208" width="260" height="34" rx="6"/>
</g>
<text x="595" y="91" text-anchor="middle">1 identify requirements  4 identify new and changed</text>
<text x="595" y="133" text-anchor="middle">6 assess impact; implement now or defer to a later cycle</text>
<text x="595" y="173" text-anchor="middle">7 implement requirements arising from Phase H</text>
<text x="595" y="189" text-anchor="middle">9 implement the change in the current phase</text>
<text x="595" y="229" text-anchor="middle">10 revise gap analysis, address gap requirements</text>
<line x1="315" y1="100" x2="445" y2="100" stroke="#555" marker-end="url(#arr-p7r)"/>
<line x1="445" y1="140" x2="315" y2="140" stroke="#555" marker-end="url(#arr-p7r)"/>
<line x1="315" y1="180" x2="445" y2="180" stroke="#555" marker-end="url(#arr-p7r)"/>
<line x1="445" y1="225" x2="315" y2="225" stroke="#555" marker-end="url(#arr-p7r)"/>
<text x="380" y="94" text-anchor="middle" fill="#345">approved requirements for the phase</text>
<text x="380" y="134" text-anchor="middle" fill="#345">new and changed requirements</text>
<text x="380" y="174" text-anchor="middle" fill="#345">Impact Assessment steers the team</text>
<text x="380" y="219" text-anchor="middle" fill="#345">status updated at phase end</text>
<text x="380" y="282" text-anchor="middle" fill="#666">in scope of the current Statement of Architecture Work: Architecture Requirements Specification; out of scope: the Repository, for a later cycle (ADM §13.5.2)</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">The two columns of the Requirements Management steps table as a handshake between the centre and the running phase. Original drawing; the step numbers follow ADM §13.3.</figcaption>
</figure>

## Where a new requirement goes

Each phase, Preliminary through H, selects its approved requirements from the Architecture
Requirements Repository and the Architecture Requirements Specification, and updates their
status when the phase completes. During the phase, new requirements *within* the scope of
the current Statement of Architecture Work are documented in the Architecture Requirements
Specification; new requirements *outside* that scope go into the Architecture Requirements
Repository to be managed for future work (ADM §13.5.2). That routing rule is the second
sentence most Requirements Management scenarios are built on: a request that changes the
agreed scope is not silently absorbed, it is recorded for a later cycle unless the sponsor
changes the Statement of Architecture Work. The same discipline appears in interoperability:
a change to business interoperability requirements must be signed off in a revised
Statement of Architecture Work (TECH §6.6).

The Requirements Impact Assessment is what makes the decision visible. It assesses the
current requirements and specification to identify what should change and the implications;
its contents reference the specific requirements, the stakeholder priority to date, the phases
to be revisited, the phase to lead on prioritisation, the results of phase investigations and
revised priorities, recommendations on managing the requirements, and a repository reference
(CONTENT §4.2.18). It iterates until a final version carries the full implications, costs,
timescales and business metrics, after which the Architecture Requirements Specification is
updated (ADM §13.4).

**Trap.** The Architecture Requirements Specification and the Requirements Impact Assessment
belong to one cycle; the Architecture Requirements Repository can hold information from
multiple cycles (ADM §13.5.1, CONTENT §7.6). An answer that "archives the specification for
next year's cycle" has the wrong container.

## Sources and kinds of requirement

The first high-level requirements come from the Architecture Vision, produced by a business
scenario or an analogous technique (ADM §13.5.2); the business scenario technique analyses
how a business goal can be met by a process or value stream and where activities are
performed by human and computer actors, which is a highly effective way to identify
architecture requirements (ADM §13.5.3). In each phase the architect identifies functional
and non-functional requirements, taking account of assumptions, constraints, domain
principles, policies, standards, organisation guidelines and specifications; later phases
also map to design requirements and generate new kinds such as conformance requirements and
implementation time windows (ADM §13.5.2). The standard mandates no specific process or
tool; it states what an effective process should achieve, and notes that many requirements
tools exist though not designed for architecture (ADM §13.5.3).

**Trap.** Gap analysis produces requirements too. Something present in the baseline and absent
from the target that was eliminated *by accident* is a gap requirement and forces a change to
the Target Architecture; step 10 makes sure it is recorded in the repository and the target
revised (ADM §13.3).

## How the 5, 3 and 1 differ

| Answer | Why it scores that |
|---|---|
| 5 | Records the new requirement, routes it to the specification or the repository depending on the Statement of Architecture Work, has the Phase C architects and the stakeholders prioritise it and resolve the conflict, generates a Requirements Impact Assessment naming the phases to revisit, lets the phase decide implement-or-defer, checks stakeholder satisfaction and updates the repository |
| 3 | Records and assesses impact, but the requirements manager decides the priority and tells the phase; the process must not prioritise alone (ADM §13.5.1, step 5 of ADM §13.3) |
| 1 | Restarts at Phase A because "the vision changed"; the impact assessment decides which phases to revisit, and a deferral to a later cycle is a listed option (ADM §13.3 step 6) |
| 0 | Holds the requirement until Phase C completes and then raises it in Phase D; changed requirements can come in through any route and must be assessed when they arrive (ADM §13.3 step 5) |

## Where to look in the book

ADM chapter 13: §13.3 for the ten-step table and its two columns, §13.4 for the outputs and
the versioning of the impact assessment, §13.5.1 for "does not dispose of" and the repository
spanning cycles, §13.5.2 for the in-scope and out-of-scope routing and the kinds of
requirement, §13.5.3 for business scenarios and tools. Architecture Content §4.2.18 for the
Requirements Impact Assessment and §7.6 for the Architecture Requirements Repository.

## Check yourself

- Which column of the steps table holds "decide whether to implement or defer"?
- Where does a new requirement outside the scope of the Statement of Architecture Work go?
- Which three documents differ in whether they span ADM cycles?
