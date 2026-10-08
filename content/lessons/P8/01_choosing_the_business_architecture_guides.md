---
title: Choosing the business architecture guides, capability, value stream, information and organization maps
unit: P8
objectives: ["P8.1"]
refs: ["GUIDE:business-capabilities §2", "GUIDE:business-capabilities §2.1.1", "GUIDE:business-capabilities §2.2", "GUIDE:business-capabilities §6", "GUIDE:value-streams §2.1", "GUIDE:value-streams §2.2", "GUIDE:value-streams §2.3", "GUIDE:value-streams §3", "GUIDE:value-streams §3.1", "GUIDE:value-streams §4.3", "GUIDE:information-mapping §2", "GUIDE:information-mapping §6", "GUIDE:organization-mapping §2", "GUIDE:organization-mapping §6", "GUIDE:business-models §2", "GUIDE:business-models §5", "ADM §13.5.3"]
reading_minutes: 11
source: authored
status: draft
---
## What the scenario looks like

A Practitioner scenario in this area describes a Phase A or Phase B engagement and plants a
modelling problem: the executives disagree about what the business does, an HR pain point
nobody can locate, a data team that wants an entity model before the business vocabulary is
agreed, a partner ecosystem that the org chart cannot show, or a new strategy expressed as a
canvas. It then asks which Business Architecture technique to apply, and when. The
five-point answer picks the guide whose *purpose* matches the planted problem and applies it
in the phase the guide names; the three-point answer picks a related but wrong artefact or
the right one in the wrong phase; the one-point answer models at the wrong level of detail;
the zero-point answer substitutes an IT artefact for a business one.

| Planted problem | Guide and artefact | Phase the guide names |
|---|---|---|
| "What does the business do, independent of who does it?" | Business Capabilities: a business capability map | Preliminary and Phase A identify capabilities; Phase B assesses gaps with heat mapping (GUIDE:business-capabilities §6) |
| "How is value created end to end for a customer, and where is it weak?" | Value Streams: value stream with stages, mapped to capabilities, heat-mapped | Phase A for strategic framing, Phase B for mapping and gap analysis (GUIDE:value-streams §3) |
| "We keep using the same nouns to mean different things" | Information Mapping: an information map of concepts and relationships | Phase A finds existing maps, Phase B builds them, C and D translate to data models (GUIDE:information-mapping §6) |
| "Which units, partners and teams actually work together on this?" | Organization Mapping: an organization map of units and relationships | Phase A uses existing descriptions, Phase B builds the map (GUIDE:organization-mapping §6) |
| "The board has a new strategy on a canvas" | Business Models: a business model artefact such as the Business Model Canvas | Input to Phase B via the Architecture Vision (GUIDE:business-models §5) |

## Business capabilities

A business capability is a particular ability or capacity that a business may possess or
exchange to achieve a specific purpose or outcome; it delineates *what* the business does
without explaining how, why or where, and it may exist today or be required by a new
strategy (GUIDE:business-capabilities §2). Naming uses a noun-verb form built around a
persistent business object, "Customer Management", and the guide warns against simply
repeating department names because organisation structures change while capabilities are
stable (GUIDE:business-capabilities §2.1.1). A capability is realised by people, processes,
information and resources, and decomposing it into those four is a test that the thing you
named is a capability and not a process, function or service
(GUIDE:business-capabilities §2.2). In the ADM, capabilities appear in the Preliminary
Phase when the team and organisation are defined, Phase A identifies the capabilities the
strategy requires and uses a map for the high-level baseline and target, and the detailed
gap assessment with heat mapping (maturity, effectiveness, performance, value or cost)
belongs in Phase B (GUIDE:business-capabilities §6).

**Trap.** A capability map is agnostic of organisation structure. An answer that draws the
map from the org chart, or that names capabilities after departments, misses the guide's
central point (GUIDE:business-capabilities §2.1.1).

## Value streams

A value stream is described by four elements: a name in the active, verb-noun form ("Acquire
Retail Product"), a description, the stakeholder who triggers it, and the value that
stakeholder expects on completion (GUIDE:value-streams §2.1). It decomposes into stages, each
with a name, description, participating stakeholders, entrance criteria, exit criteria and
the value item it adds; a stream may stop after any stage if the value has not been created
(GUIDE:value-streams §2.2). The next move is to cross-map the capabilities that enable each
stage, which shows which capabilities are critical to stakeholder value and which contribute
to no core stream and might be eliminated (GUIDE:value-streams §2.3). The guiding principles:
a clearly defined triggering stakeholder, start with external (customer) streams, value
streams are not capabilities nor components of capabilities, and keep it concise, operational
detail is process design (GUIDE:value-streams §3.1). Which comes first? It does not matter,
but the value stream map is often faster to draft and informs the capability model
(GUIDE:value-streams §3).

The guide's worked scenario is a template for exam answers: a falling offer-acceptance rate
leads a cross-functional team, guided by the Business Architect, to refine the "Recruit
Employee" stream, cross-map capabilities to its stages, heat-map how well each capability
supports the value at each stage, gather more information before concluding, and discover
that the root cause is a missing role tracking onboarding, which becomes a new subordinate
value stream with an owner (GUIDE:value-streams §4.3).

<figure class="my-4">
<svg viewBox="0 0 760 300" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="11" role="img" aria-label="Four Business Architecture maps and how they relate: value stream stages map to capabilities; capabilities are realised by people, process, information and resources; the information map supplies the concepts; the organization map supplies the units and relationships; the business model frames all of it">
<defs><marker id="arr-p8b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
<rect x="15" y="10" width="730" height="34" rx="8" fill="#f3e3f7" stroke="#b58ac9"/>
<text x="380" y="31" text-anchor="middle" font-weight="bold">Business model: how the organisation creates, delivers and captures value; input to Phase B via the Vision (GUIDE:business-models §2, §5)</text>
<rect x="15" y="70" width="350" height="70" rx="8" fill="#e3f5e1" stroke="#7fbf7a"/>
<text x="190" y="92" text-anchor="middle" font-weight="bold">Value stream (verb-noun, triggering stakeholder, value)</text>
<g fill="#fff" stroke="#7fbf7a">
<rect x="30" y="102" width="70" height="28" rx="4"/><rect x="110" y="102" width="70" height="28" rx="4"/><rect x="190" y="102" width="70" height="28" rx="4"/><rect x="270" y="102" width="80" height="28" rx="4"/>
</g>
<text x="65" y="120" text-anchor="middle">stage 1</text><text x="145" y="120" text-anchor="middle">stage 2</text><text x="225" y="120" text-anchor="middle">stage 3</text><text x="310" y="120" text-anchor="middle">stage n</text>
<rect x="395" y="70" width="350" height="70" rx="8" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="570" y="92" text-anchor="middle" font-weight="bold">Business capability map (noun-verb, what, not how)</text>
<text x="570" y="112" text-anchor="middle">levels, tiers, heat-mapped in Phase B for maturity,</text>
<text x="570" y="128" text-anchor="middle">effectiveness, performance, value or cost</text>
<line x1="365" y1="105" x2="395" y2="105" stroke="#555" marker-end="url(#arr-p8b)"/>
<text x="380" y="62" text-anchor="middle" fill="#345">stages cross-mapped to enabling capabilities</text>
<rect x="15" y="180" width="230" height="60" rx="8" fill="#fff" stroke="#666"/>
<text x="130" y="202" text-anchor="middle" font-weight="bold">Information map</text>
<text x="130" y="218" text-anchor="middle">business concepts (the nouns) and their</text>
<text x="130" y="232" text-anchor="middle">relationships; not a data model</text>
<rect x="265" y="180" width="230" height="60" rx="8" fill="#fff" stroke="#666"/>
<text x="380" y="202" text-anchor="middle" font-weight="bold">Organization map</text>
<text x="380" y="218" text-anchor="middle">units, partners, collaborative teams and</text>
<text x="380" y="232" text-anchor="middle">their working relationships; not an org chart</text>
<rect x="515" y="180" width="230" height="60" rx="8" fill="#fff" stroke="#666"/>
<text x="630" y="202" text-anchor="middle" font-weight="bold">Capability realisation</text>
<text x="630" y="218" text-anchor="middle">people, processes, information, resources</text>
<text x="630" y="232" text-anchor="middle">(GUIDE:business-capabilities §2.2)</text>
<line x1="130" y1="180" x2="470" y2="140" stroke="#555" stroke-dasharray="4 3" marker-end="url(#arr-p8b)"/>
<line x1="380" y1="180" x2="520" y2="140" stroke="#555" stroke-dasharray="4 3" marker-end="url(#arr-p8b)"/>
<line x1="630" y1="180" x2="600" y2="140" stroke="#555" stroke-dasharray="4 3" marker-end="url(#arr-p8b)"/>
<text x="380" y="275" text-anchor="middle" fill="#666">the four maps are meant to be linked; a well linked organization map helps ensure the real business problem is solved with process, role, data and technology change together (GUIDE:organization-mapping §6)</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">How the Business Architecture guides fit together. Original drawing; the relationships follow the "relationship" chapters of each guide.</figcaption>
</figure>

## Information maps and organization maps

An information map is a collection of information concepts and their relationships; the
concepts reflect the business vocabulary (client, account, product), and the way to find
them is to listen for the nouns and challenge each one: does anyone in the business need to
know, store or manipulate it? (GUIDE:information-mapping §2). The map is a Business
Architecture artefact, distinct from the data models that Phases C and D derive from it; the
guide places finding existing maps in Phase A, building them in Phase B, translation into
data models in C and D, and possible updates in Phase E (GUIDE:information-mapping §6).

An organization map shows the main organisational units, partners and stakeholder groups
that make up the enterprise's ecosystem and the formal and informal working relationships
between them; that is what distinguishes it from an org chart of reporting lines, and it can
extend beyond the legal boundary to partners and even customers, with nodes at enterprise,
line of business, function, partner and collaborative team levels
(GUIDE:organization-mapping §2). To the Enterprise Architect it is a means of identifying
stakeholders for the solutions the later phases produce; Phase A uses whatever descriptions
exist, Phase B builds the map with its relationships to capabilities and information, and the
metamodel's organizational unit entity links it to capabilities, products and functions
(GUIDE:organization-mapping §6).

**Trap.** An entity-relationship diagram from the data team is not an information map, and
an org chart is not an organization map. Both guides exist because the IT-style artefact
answers a different question (GUIDE:information-mapping §2, GUIDE:organization-mapping §2).

## Business models

A business model describes the rationale for how an organisation creates, delivers and
captures value; it may live only in a leader's head or be made concrete in artefacts such as
the Business Model Canvas, which the guide uses to show alignment between strategy and
Business Architecture (GUIDE:business-models §2). Constructing the artefact lets the
architect bridge strategy and architecture; business models are normally associated with the
Architecture Vision phase and are a key input to Phase B, where they identify partner
stakeholders, verify goals, drivers and constraints, drive capability and value stream
mapping to find the capabilities the target model needs, scope the Statement of Architecture
Work, shape principles and anchor the project's value proposition; transition business models
feed transition Business Architectures, and the models keep E and F oriented to value
(GUIDE:business-models §5). Business scenarios, the Requirements Management source technique,
analyse how a goal is met by a process or value stream, which is why the two guides are often
used together (ADM §13.5.3).

## How the 5, 3 and 1 differ

| Answer | Why it scores that |
|---|---|
| 5 | Chooses the artefact whose purpose matches the planted problem, names the stakeholder that triggers the stream or the noun-challenge for the concept, applies it in the phase the guide specifies, and links it to the other maps so the gap is traced to process, role, information and technology |
| 3 | Chooses a related artefact, a capability map for an end-to-end value question or a value stream for a "what do we do" question, or does the Phase B heat map in Phase A |
| 1 | Models at operational detail, business processes instead of value stream stages, or department names instead of capabilities; the guides say keep it concise and organisation-agnostic (GUIDE:value-streams §3.1, GUIDE:business-capabilities §2.1.1) |
| 0 | Substitutes a data model for the information map or an org chart for the organization map, answering an IT or reporting-line question instead of the business one |

## Where to look in the book

Each guide's "what is" chapter (2) for definitions and naming, its "relationship" chapter
for how it links to the others, and its "using with the TOGAF Standard" chapter for the phase
mapping: Business Capabilities §6, Value Streams §3 and §4.3, Information Mapping §6,
Organization Mapping §6, Business Models §5. ADM §13.5.3 for business scenarios as the source
of requirements.

## Check yourself

- Which naming form belongs to capabilities and which to value streams?
- Name the six elements of a value stream stage.
- In which phase does the Business Capabilities guide put heat mapping?
