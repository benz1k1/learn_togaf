---
title: The business architecture guides — capabilities, value streams, information maps, organisation maps and business models
unit: G_BUSINESS_ARCH
objectives: ["G4.1"]
refs: ["GUIDE:business-capabilities §2.1.1", "GUIDE:business-capabilities §3.1", "GUIDE:business-capabilities §3.1.1", "GUIDE:business-capabilities §5.1", "GUIDE:business-capabilities §5.2.2", "GUIDE:business-capabilities §6", "GUIDE:value-streams §1.4", "GUIDE:value-streams §2.1", "GUIDE:value-streams §2.3", "GUIDE:value-streams §3.1", "GUIDE:value-streams §4.3", "GUIDE:information-mapping §2", "GUIDE:information-mapping §4", "GUIDE:information-mapping §5", "GUIDE:information-mapping §6", "GUIDE:organization-mapping §2", "GUIDE:organization-mapping §3", "GUIDE:organization-mapping §4", "GUIDE:organization-mapping §6", "GUIDE:business-models §2", "GUIDE:business-models §4", "GUIDE:business-models §5", "ADM §3.5.2", "ADM §4.5.3"]
reading_minutes: 12
source: authored
status: draft
---
## Five guides, four pillars and a model above them

Business Architecture separates *what* the business does (capabilities) from *who* does it
(organisation), from *how* value is achieved (value streams), from how work is performed at an
operational level (process), from the information needed and the systems used
(GUIDE:value-streams §1.4). Four of the Series Guides describe one pillar each — business
capabilities, value streams, information maps, organisation maps — and a fifth describes the
business model that sits above them: the rationale for how the organisation creates, delivers
and captures value (GUIDE:business-models §2). Phase A searches for existing versions of all of
them, and Phase B applies them to the scope of the project (ADM §3.5.2; ADM §4.5.3).

**Which guide, for which question.** A scenario asking "what must we be able to do" is a
capability question; "how does value reach this customer, and where does it stall" is a value
stream question; "which business units are really involved, including partners" is an
organisation map question; "what do we mean by *customer*, and who owns it" is an information
map question; "the strategy has changed — what now" is a business model question that the
other four then unpack (GUIDE:business-models §4).

<figure class="my-4">
<svg viewBox="0 0 760 320" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="10" role="img" aria-label="The business model above four pillars: capabilities (what), value streams (how value is delivered and for whom), organisation map (who and with whom), information map (the vocabulary). Arrows show the cross-mappings: value stream stages to capabilities, capabilities to organisation units, capabilities to information concepts; and the ADM placement, Phase A finds them, Phase B builds them">
<defs><marker id="arr-g4-01a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
<text x="380" y="18" text-anchor="middle" font-size="12" font-weight="bold">The business model and the four pillars, with their cross-mappings</text>
<rect x="180" y="34" width="400" height="44" rx="6" fill="#fde8e6" stroke="#c0392b"/>
<text x="380" y="52" text-anchor="middle" font-weight="bold">Business model — why: how the enterprise creates, delivers and captures value</text>
<text x="380" y="68" text-anchor="middle" font-size="9">a sketch for leadership alignment; Business Architecture breaks it into the pillars below</text>
<line x1="380" y1="78" x2="380" y2="100" stroke="#555" marker-end="url(#arr-g4-01a)"/>
<rect x="10" y="102" width="175" height="96" rx="6" fill="#e3f0fb" stroke="#4a7fb5"/>
<text x="97" y="122" text-anchor="middle" font-weight="bold">Business capabilities</text>
<text x="97" y="138" text-anchor="middle" font-size="9">WHAT the business can do</text>
<text x="97" y="152" text-anchor="middle" font-size="9">noun-verb names; stable;</text>
<text x="97" y="165" text-anchor="middle" font-size="9">independent of org chart</text>
<text x="97" y="184" text-anchor="middle" font-size="9">people + process + information + resources</text>
<rect x="200" y="102" width="175" height="96" rx="6" fill="#e3f0fb" stroke="#4a7fb5"/>
<text x="287" y="122" text-anchor="middle" font-weight="bold">Value streams</text>
<text x="287" y="138" text-anchor="middle" font-size="9">HOW value is delivered, to WHOM</text>
<text x="287" y="152" text-anchor="middle" font-size="9">verb-noun names; a triggering</text>
<text x="287" y="165" text-anchor="middle" font-size="9">stakeholder; stages with entry, exit,</text>
<text x="287" y="184" text-anchor="middle" font-size="9">value item — outside-in, not process</text>
<rect x="390" y="102" width="175" height="96" rx="6" fill="#e3f0fb" stroke="#4a7fb5"/>
<text x="477" y="122" text-anchor="middle" font-weight="bold">Organisation map</text>
<text x="477" y="138" text-anchor="middle" font-size="9">WHO, with WHOM</text>
<text x="477" y="152" text-anchor="middle" font-size="9">units, partners, stakeholder groups</text>
<text x="477" y="165" text-anchor="middle" font-size="9">and their working relationships —</text>
<text x="477" y="184" text-anchor="middle" font-size="9">a web, not a reporting-line chart</text>
<rect x="580" y="102" width="170" height="96" rx="6" fill="#e3f0fb" stroke="#4a7fb5"/>
<text x="665" y="122" text-anchor="middle" font-weight="bold">Information map</text>
<text x="665" y="138" text-anchor="middle" font-size="9">the business VOCABULARY</text>
<text x="665" y="152" text-anchor="middle" font-size="9">information concepts (nouns) and</text>
<text x="665" y="165" text-anchor="middle" font-size="9">their relationships — not a data</text>
<text x="665" y="184" text-anchor="middle" font-size="9">model; feeds Phase C</text>
<line x1="200" y1="150" x2="187" y2="150" stroke="#555" marker-end="url(#arr-g4-01a)"/>
<text x="193" y="212" text-anchor="middle" font-size="9">stages ↔ capabilities (heat map by stage)</text>
<line x1="390" y1="150" x2="377" y2="150" stroke="#555" marker-end="url(#arr-g4-01a)"/>
<line x1="185" y1="220" x2="477" y2="200" stroke="#555" stroke-dasharray="3 3" marker-end="url(#arr-g4-01a)"/>
<text x="330" y="236" text-anchor="middle" font-size="9">capability / organisation matrix (many-to-many)</text>
<line x1="185" y1="245" x2="665" y2="200" stroke="#555" stroke-dasharray="3 3" marker-end="url(#arr-g4-01a)"/>
<text x="470" y="258" text-anchor="middle" font-size="9">capabilities establish and use information concepts (information / capability matrix)</text>
<rect x="10" y="272" width="740" height="42" rx="6" fill="#fff" stroke="#666"/>
<text x="380" y="290" text-anchor="middle" font-weight="bold">Phase A: find what exists (even an org chart) and identify the required capabilities · Phase B: build, cross-map, heat-map the gaps · Phase C: translate information into data</text>
<text x="380" y="306" text-anchor="middle" font-size="9">value stream first if starting from scratch — it is faster and informs the capability map; but neither should exist without the other for long</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">Original drawing. Pillar definitions follow GUIDE:business-capabilities §2.1.1, GUIDE:value-streams §2.1, GUIDE:organization-mapping §2 and GUIDE:information-mapping §2; cross-mappings follow GUIDE:business-capabilities §5.2.2, GUIDE:organization-mapping §6 and GUIDE:information-mapping §4; the business model follows GUIDE:business-models §4; ADM placement ADM §3.5.2 and §4.5.3, and GUIDE:value-streams §3.1.</figcaption>
</figure>

## Business capabilities: what, not how

A capability delineates what a business does without saying how, why or where; it is named
noun-verb around a business object ("Customer Management"), described as "the ability to…",
and must resist repeating department names because organisations change and capabilities
endure (GUIDE:business-capabilities §2.1.1). Mapping starts top-down (20 to 30 level-1
capabilities with senior leaders) or bottom-up, from three sources: the organisational
structure, the business model, and the strategic, business and financial plans
(GUIDE:business-capabilities §3.1). Transposing the org chart onto the map is the common
mistake — the guide's worked example turns "IT Management" into "Information Management",
recognises distribution and procurement as value stream stages rather than capabilities, and
finds "Business Planning" that no single unit owns (GUIDE:business-capabilities §3.1.1).

Heat maps colour the map by maturity, effectiveness, performance, value or cost, coverage or
criticality; a missing capability "signifies a significant gap" (GUIDE:business-capabilities §5.1).
Mapping capabilities to value stream stages shows which are critical to value delivery and
which appear in several streams (GUIDE:business-capabilities §5.2.2). In the ADM, the required
capabilities are identified in Phase A and the detailed gap assessment with heat mapping
belongs in Phase B (GUIDE:business-capabilities §6).

## Value streams: value from the stakeholder's perspective

A value stream is defined by four elements — name (active, verb-noun: "Acquire Retail
Product"), description, the stakeholder who triggers it, and the value they expect — and
decomposed into stages, each with participating stakeholders, entrance and exit criteria and a
value item (GUIDE:value-streams §2.1). Stages are then cross-mapped to the capability map to
find which capabilities are critical to delivering value and which contribute to no stream and
may be eliminated (GUIDE:value-streams §2.3). Four guiding principles: a clearly defined
triggering stakeholder; start with external, customer-based streams; value streams are not
capabilities; keep it concise — operational detail is process design (GUIDE:value-streams §3.1).

The heat-mapping scenario is the exam's model: a falling offer-acceptance rate, a programme
manager sure the cause is laptop provisioning, and a heat map over the Recruit Employee stream
that — after a week of evidence — finds the real gap is a missing role to track the whole
onboarding sequence, leading to a new subordinate value stream with an owner
(GUIDE:value-streams §4.3).

## Organisation maps: a web, not a chart

An organisation map shows the main units, partners and stakeholder groups of the enterprise
ecosystem and the working relationships, formal and informal, between them; nodes are
organisation units at levels from enterprise through line of business, function, partner and
collaborative team (GUIDE:organization-mapping §2). It differs from an org chart in scope
(whole-system, external parties included), complexity, explicitness (implicit relationships are
shown) and lifecycle (a business model change alters the map but not the chart)
(GUIDE:organization-mapping §3). Its benefits are understanding, cross-organisational planning,
context for deployment, communication, and organisational change management — it is a key input
to the communication plan and stakeholder analysis (GUIDE:organization-mapping §4). In the ADM,
Phase A uses existing descriptions, even conventional charts; Phase B builds the map with its
relationships to capabilities and information (GUIDE:organization-mapping §6).

## Information maps: the vocabulary, not the schema

An information map is a collection of information concepts — the business vocabulary: client,
account, product — and their relationships; listen for the nouns and challenge each one
(GUIDE:information-mapping §2). Concepts link first to capabilities, which establish and modify
them; the link to value streams is indirect, through the capabilities, and using value streams
to drive information directly "probably indicates the architect is really modeling the
implemented business process" (GUIDE:information-mapping §4). An information map is not a data
model: "customer perception" is a legitimate concept that no field can hold; limiting concepts
to what data models can capture "could lead to significant gaps" (GUIDE:information-mapping §5).
Phase A finds existing maps, Phase B builds them, Phases C and D translate into data models,
Phase E may update them (GUIDE:information-mapping §6).

## Business models: the sketch above the pillars

A business model describes how an organisation creates, delivers and captures value, and may be
represented in several frameworks; the Business Model Canvas is the one the guide uses
(GUIDE:business-models §2). It is deliberately abstract — enough to test feasibility and align
leadership, not enough for a risk assessment or an execution plan; Business Architecture breaks
it into capabilities, value streams, organisation and information, and can feed back gaps and
conflicts in the model's assumptions (GUIDE:business-models §4). In the ADM the business model
is associated with Phase A and is a key input to Phase B: identify key partners as
stakeholders, verify goals, drivers and constraints, use capability and value stream mapping to
find what the target model requires, scope the Statement of Architecture Work, formulate
principles, and anchor the project's value proposition (GUIDE:business-models §5).

**Trap.** A "new business model" needs a combined shift in customer segments *and* value
proposition; anything narrower is an adjustment to the current model. And a value stream is
never a capability, nor a component of one — they inform and validate each other
(GUIDE:value-streams §3.1).

## How the 5-point answer differs from the 3-point one

| Points | What the answer does |
|---|---|
| 5 | Picks the pillar that answers the planted question, names the guide's construct correctly (noun-verb capability, verb-noun value stream with a triggering stakeholder, web-style organisation map, concept-level information map), cross-maps it to the others, heat-maps the gap in Phase B, and traces it to the business model |
| 3 | Right pillar but built the wrong way — a capability map copied from the org chart, a value stream at process detail, an information map that is a data model |
| 1 | Uses one pillar for every question (everything is a capability), or does the detailed gap work in Phase A |
| 0 | Treats the org chart as the organisation map, or treats the business model canvas as the architecture |

## Where to look in the book

Business Capabilities §2.1.1, §3.1, §3.1.1, §5.1, §5.2.2, §6. Value Streams §1.4, §2.1, §2.3,
§3.1, §4.3. Information Mapping §2, §4, §5, §6. Organization Mapping §2, §3, §4, §6. Business
Models §2, §4, §5. ADM §3.5.2 (Phase A finds them) and §4.5.3 (Phase B applies them).
