---
title: Phase A step by step — scope, principles, the Vision and the Statement of Architecture Work
unit: P3
objectives: ["P3.1"]
refs: ["ADM §3.1", "ADM §3.3", "ADM §3.3.1", "ADM §3.3.3", "ADM §3.3.4", "ADM §3.3.6", "ADM §3.3.7", "ADM §3.3.8", "ADM §3.3.9", "ADM §3.3.11", "ADM §3.4", "ADM §3.5.1", "ADM §3.5.2", "TECH §2.3", "TECH §2.4", "TECH §2.4.1", "TECH §2.5"]
reading_minutes: 11
source: authored
status: draft
---
## What the exam plants in a Phase A scenario

The previous lesson gave the shape of the answer: Phase A in order. This lesson is the step-by-
step detail that the near-miss answers get wrong — which step produces which document, where
the principles come from, what "scope" actually lists, and what has to happen before Phase B
may start. Phase A has two objectives and the exam keeps returning to the second one: develop a
high-level aspirational vision of the capabilities and business value to be delivered, and
*obtain approval for a Statement of Architecture Work* that defines the programme of works to
develop and deploy the architecture in that vision (ADM §3.1).

The order of steps, and when each starts and finishes, is adapted to the situation under the
established governance; the level of detail depends on the scope and goals of the Request for
Architecture Work or of the current iteration. So the exam does not test a rigid sequence — it
tests whether you know what each step must produce (ADM §3.3).

<figure class="my-4">
<svg viewBox="0 0 760 300" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="10" role="img" aria-label="The eleven Phase A steps as a strip, grouped: establish the project; stakeholders and requirements; goals, drivers and constraints; evaluate capabilities; readiness; scope; principles; Architecture Vision; value propositions and KPIs; risks; Statement of Architecture Work and approval. Below each group the document it produces.">
<defs><marker id="arr-p3-02a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
<text x="380" y="18" text-anchor="middle" font-size="12" font-weight="bold">Phase A: the eleven steps and what each one leaves behind</text>
<g>
<rect x="10" y="36" width="62" height="60" rx="5" fill="#e3f0fb" stroke="#4a7fb5"/><text x="41" y="58" text-anchor="middle" font-size="9">1 Establish</text><text x="41" y="70" text-anchor="middle" font-size="9">the project</text>
<rect x="78" y="36" width="62" height="60" rx="5" fill="#e3f0fb" stroke="#4a7fb5"/><text x="109" y="58" text-anchor="middle" font-size="9">2 Stakeholders,</text><text x="109" y="70" text-anchor="middle" font-size="9">concerns, reqs</text>
<rect x="146" y="36" width="62" height="60" rx="5" fill="#e3f0fb" stroke="#4a7fb5"/><text x="177" y="58" text-anchor="middle" font-size="9">3 Goals, drivers,</text><text x="177" y="70" text-anchor="middle" font-size="9">constraints</text>
<rect x="214" y="36" width="62" height="60" rx="5" fill="#e3f0fb" stroke="#4a7fb5"/><text x="245" y="58" text-anchor="middle" font-size="9">4 Evaluate</text><text x="245" y="70" text-anchor="middle" font-size="9">capabilities</text>
<rect x="282" y="36" width="62" height="60" rx="5" fill="#e3f0fb" stroke="#4a7fb5"/><text x="313" y="58" text-anchor="middle" font-size="9">5 Assess</text><text x="313" y="70" text-anchor="middle" font-size="9">readiness</text>
<rect x="350" y="36" width="62" height="60" rx="5" fill="#fff1d6" stroke="#e0b060"/><text x="381" y="58" text-anchor="middle" font-size="9">6 Define</text><text x="381" y="70" text-anchor="middle" font-size="9">scope</text>
<rect x="418" y="36" width="62" height="60" rx="5" fill="#fff1d6" stroke="#e0b060"/><text x="449" y="58" text-anchor="middle" font-size="9">7 Confirm</text><text x="449" y="70" text-anchor="middle" font-size="9">principles</text>
<rect x="486" y="36" width="62" height="60" rx="5" fill="#e3f5e1" stroke="#7fbf7a"/><text x="517" y="58" text-anchor="middle" font-size="9">8 Develop</text><text x="517" y="70" text-anchor="middle" font-size="9">Arch. Vision</text>
<rect x="554" y="36" width="62" height="60" rx="5" fill="#e3f5e1" stroke="#7fbf7a"/><text x="585" y="58" text-anchor="middle" font-size="9">9 Value props</text><text x="585" y="70" text-anchor="middle" font-size="9">and KPIs</text>
<rect x="622" y="36" width="62" height="60" rx="5" fill="#e3f5e1" stroke="#7fbf7a"/><text x="653" y="58" text-anchor="middle" font-size="9">10 Risks and</text><text x="653" y="70" text-anchor="middle" font-size="9">mitigation</text>
<rect x="690" y="36" width="62" height="60" rx="5" fill="#e3f5e1" stroke="#7fbf7a"/><text x="721" y="58" text-anchor="middle" font-size="9">11 SoAW,</text><text x="721" y="70" text-anchor="middle" font-size="9">approval</text>
</g>
<line x1="41" y1="96" x2="41" y2="120" stroke="#555" marker-end="url(#arr-p3-02a)"/>
<line x1="109" y1="96" x2="109" y2="120" stroke="#555" marker-end="url(#arr-p3-02a)"/>
<line x1="245" y1="96" x2="245" y2="120" stroke="#555" marker-end="url(#arr-p3-02a)"/>
<line x1="313" y1="96" x2="313" y2="120" stroke="#555" marker-end="url(#arr-p3-02a)"/>
<line x1="449" y1="96" x2="449" y2="120" stroke="#555" marker-end="url(#arr-p3-02a)"/>
<line x1="517" y1="96" x2="517" y2="120" stroke="#555" marker-end="url(#arr-p3-02a)"/>
<line x1="721" y1="96" x2="721" y2="120" stroke="#555" marker-end="url(#arr-p3-02a)"/>
<rect x="10" y="122" width="62" height="48" rx="5" fill="#fff" stroke="#666"/><text x="41" y="142" text-anchor="middle" font-size="8">endorsement of</text><text x="41" y="153" text-anchor="middle" font-size="8">corporate and</text><text x="41" y="164" text-anchor="middle" font-size="8">line management</text>
<rect x="78" y="122" width="62" height="48" rx="5" fill="#fff" stroke="#666"/><text x="109" y="142" text-anchor="middle" font-size="8">stakeholder map;</text><text x="109" y="153" text-anchor="middle" font-size="8">ARS in scope,</text><text x="109" y="164" text-anchor="middle" font-size="8">Repository out</text>
<rect x="214" y="122" width="130" height="48" rx="5" fill="#fff" stroke="#666"/><text x="279" y="142" text-anchor="middle" font-size="8">Capability Assessment: EA capability</text><text x="279" y="153" text-anchor="middle" font-size="8">gaps go back to Preliminary; business</text><text x="279" y="164" text-anchor="middle" font-size="8">capability gaps in detail belong to B</text>
<rect x="418" y="122" width="62" height="48" rx="5" fill="#fff" stroke="#666"/><text x="449" y="142" text-anchor="middle" font-size="8">Architecture</text><text x="449" y="153" text-anchor="middle" font-size="8">Principles</text><text x="449" y="164" text-anchor="middle" font-size="8">(from Prelim)</text>
<rect x="486" y="122" width="62" height="48" rx="5" fill="#fff" stroke="#666"/><text x="517" y="142" text-anchor="middle" font-size="8">Architecture</text><text x="517" y="153" text-anchor="middle" font-size="8">Vision, draft</text><text x="517" y="164" text-anchor="middle" font-size="8">ADD</text>
<rect x="690" y="122" width="62" height="48" rx="5" fill="#fff" stroke="#666"/><text x="721" y="142" text-anchor="middle" font-size="8">Approved SoAW,</text><text x="721" y="153" text-anchor="middle" font-size="8">Comms Plan,</text><text x="721" y="164" text-anchor="middle" font-size="8">sponsor sign-off</text>
<rect x="10" y="192" width="742" height="96" rx="6" fill="#f9f9f9" stroke="#999"/>
<text x="381" y="212" text-anchor="middle" font-size="10" font-weight="bold">Where the scenario's planted facts land</text>
<text x="381" y="230" text-anchor="middle" font-size="9">"stakeholders disagree about the problem" → step 2 and a business scenario in step 8 &#183; "change-averse culture, hard deadline" → step 5 readiness, step 10 risk</text>
<text x="381" y="246" text-anchor="middle" font-size="9">"no principles exist" → step 7 goes back to the governance body to define them for the first time &#183; "framework does not fit" → revisit the Preliminary Phase</text>
<text x="381" y="262" text-anchor="middle" font-size="9">"the sponsor has not signed" → step 11 is not complete; Phase B has no mandate &#183; "requirement outside scope" → Requirements Repository, not the ARS</text>
<text x="381" y="278" text-anchor="middle" font-size="9">Steps are re-ordered to suit the situation under governance; what they must produce does not change.</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">Original drawing. Steps and products follow ADM §3.3 to §3.3.11 and the outputs list in §3.4; the "framework does not fit" and "principles for the first time" cases follow §3.5.1 and §3.3.7.</figcaption>
</figure>

## Steps 1 to 3: mandate, stakeholders, goals and constraints

Each ADM cycle is normally run as a project under the enterprise's project management
framework, stand-alone or as part of a larger project, and step 1 secures recognition of the
project, endorsement of corporate management and the commitment of line management, with
references to any other management frameworks in use (ADM §3.3.1). Phase A starts on receipt of
a Request for Architecture Work from the sponsoring organisation (ADM §3.5.1).

Step 3 confirms the business goals and strategic drivers — normally already defined elsewhere,
in which case the job is to check they are current and clear ambiguity; if not, go back to the
originators of the Statement of Architecture Work and secure corporate endorsement. It also
defines constraints, enterprise-wide and project-specific (time, schedule, resources), informed
by the business and architecture principles from the Preliminary Phase (ADM §3.3.3).

## Step 4: two kinds of capability

Evaluate Capabilities has two parts that the exam likes to separate. One is the enterprise's
capability to *develop and consume the architecture*; gaps there — skills, information,
process, tools — require iteration between Architecture Vision and the Preliminary Phase and
are "a serious consideration in the vision of whether the architecture effort should continue".
The other is the baseline and target *business* capability of the enterprise; the detailed
assessment of business capability gaps belongs in Phase B. Both are recorded in the Capability
Assessment, and Value Chain diagrams can show related capabilities in context (ADM §3.3.4).

**Trap.** "Assess the business capability gaps in detail before writing the Vision" scores
below the answer that identifies the *required* capabilities in Phase A and defers the
detailed gap work to Phase B (ADM §3.3.4).

## Step 6: what "scope" lists

Define what is inside and outside the baseline and target efforts, knowing that the two need
not be described at the same depth. Specifically: the breadth of coverage; the level of detail;
the partitioning characteristics; the domains to cover (Business, Data, Application,
Technology); the time period and any intermediate periods; and the architectural assets to be
leveraged from the Repository or from the industry (ADM §3.3.6). Scoping decisions rest on a
practical assessment of resource and competence availability and of the value the chosen scope
can realistically return; they are constrained within the overall scope set in the Preliminary
Phase, and if the framework in place cannot deliver the desired Vision, the Preliminary Phase is
revisited to extend it (ADM §3.5.1).

## Step 7: confirm the principles — and know what a good one looks like

Architecture Principles are normally based on those developed in the Preliminary Phase; Phase A
ensures they are current and clarifies ambiguity, and otherwise goes back to the body
responsible for Architecture Governance to define them for the first time and secure corporate
endorsement (ADM §3.3.7). They are developed by the enterprise architects with key stakeholders
and *approved by the Architecture Board*, informed by enterprise-level principles where these
exist, and chosen to align the target with business strategy (TECH §2.4).

A principle has four parts — name, statement, rationale, implications. The name avoids
technology platforms and ambiguous words such as "support", "open", "consider" and "avoid"; the
rationale is in business terms and says which principle takes precedence when two conflict; the
implications answer "how does this affect me" without trivialising the impact (TECH §2.3). A
good set is understandable, robust, complete, consistent and stable, few in number, and
endorsed by senior management; an amendment process is established once they are ratified
(TECH §2.4.1). Principles compete — accessibility against security is the standard's example —
so each is read "all other things being equal", and the rationale for a precedence decision is
always documented (TECH §2.5).

**Trap.** A principle whose statement is "use vendor X's platform" fails the template on its
face; a scenario offering it as a "principle" is testing TECH §2.3.

## Steps 8 to 10: the Vision, its value and its risks

The Vision starts from an overall architecture showing how the domain deliverables fit
together, then a high-level view of baseline and target across Business, Data, Application and
Technology built from the stakeholder concerns, capability requirements, scope, constraints and
principles. Informal techniques are usual; a Solution Concept diagram is common; business
scenarios are the recommended technique to discover requirements and articulate a Vision that
responds to them. The result is stored in the Repository (ADM §3.3.8). The Vision is the
sponsor's tool to sell the benefits of the proposed capability; clarifying and agreeing the
purpose of the architecture effort "is the whole point" (ADM §3.5.2).

Step 9 develops the business case, a value proposition per stakeholder grouping, procurement
requirements, performance metrics and measures, and assesses business risk — all of which are
incorporated into the Statement of Architecture Work so that performance can be tracked
(ADM §3.3.9). Step 10 identifies the risks of the Vision, assesses the initial level (effect and
frequency), assigns a mitigation strategy per risk, distinguishes initial from residual risk,
and considers the mitigation activities for inclusion in the Statement of Architecture Work
(ADM §3.3.10).

## Step 11 and the outputs

Develop Statement of Architecture Work; Secure Approval decides which domains to develop and to
what detail, which views to build, estimates resources and schedule, develops a roadmap for the
cycle, defines the team's performance metrics, develops the Communications Plan, reviews and
agrees the plans with the sponsors, secures formal approval under governance, and gains the
sponsor's sign-off to proceed (ADM §3.3.11). Consensus is represented by the sponsoring
organisation signing the Statement of Architecture Work; without it "it is very unlikely that
the final architecture will be accepted" (ADM §3.5.2).

The outputs of Phase A: the approved Statement of Architecture Work; refined business
principles, goals and drivers; Architecture Principles; Capability Assessment; Tailored
Architecture Framework for the engagement; the Architecture Vision (problem description,
objective of the Statement of Architecture Work, summary views, optional business scenario,
refined high-level stakeholder requirements); a draft Architecture Definition Document that may
already hold baseline or target of any domain; the Communications Plan; and additional
Repository content (ADM §3.4).

## How the 5-point answer differs from the 3-point one

| Points | What the answer does |
|---|---|
| 5 | Confirms (not invents) goals, drivers and principles from the Preliminary Phase; scopes by breadth, detail, partitioning, domains, time and assets; records EA-capability gaps and loops to Preliminary if needed; produces the Vision, value propositions, KPIs and risks; secures the sponsor's signature on the Statement of Architecture Work before Phase B |
| 3 | Produces the right documents but writes new principles without the governance body, or defines scope only by domain, or forgets the Communications Plan |
| 1 | Skips the Statement of Architecture Work and treats the Vision presentation as approval; or does detailed business capability gap analysis in Phase A |
| 0 | Starts Phase B on the strength of the Request for Architecture Work alone, or adopts a vendor platform as a "principle" |

## Where to look in the book

ADM §3.3.1 to §3.3.11 (one heading per step — the exam answer wording tracks these headings),
§3.4 (outputs), §3.5.1 (the general approach: Request for Architecture Work, scope and the
Preliminary Phase), §3.5.2 (creating the Vision, business models, capabilities, value streams,
organisation maps, consensus by signature). ADM Techniques §2.3 (the four-part template), §2.4
(who develops and approves), §2.4.1 (the five qualities), §2.5 (applying and precedence).
