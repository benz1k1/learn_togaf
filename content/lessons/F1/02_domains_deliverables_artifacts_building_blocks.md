---
title: The four domains; deliverables, artifacts and building blocks
unit: F1
objectives: ["1.3", "1.4"]
refs: ["INTRO §2", "INTRO §3"]
reading_minutes: 7
source: authored
status: draft
---
## Four architecture domains

The standard treats an enterprise architecture as four domains, and the ADM develops them in
this order in Phases B, C and D:

| Domain | Describes | Phase |
|---|---|---|
| **Business** | strategy, governance, organisation, key processes | B |
| **Data** | the structure of logical and physical data assets and data management | C |
| **Application** | the applications to be deployed, their interactions, and their relationship to business processes | C |
| **Technology** | the software and hardware capabilities that support the other three | D |

Remember the mnemonic BDAT and that **Data and Application share Phase C**. Security is not a
fifth domain; it is a cross-cutting concern addressed within each.

<figure class="my-4">
<svg viewBox="0 0 760 220" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="The four domains Business, Data, Application, Technology mapped to Phases B, C and D, with Phase C spanning Data and Application">
  <defs><marker id="arr-f1-02a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
  <rect x="20" y="15" width="160" height="62" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
  <text x="100" y="35.85" text-anchor="middle" font-size="11" font-weight="bold">Business</text>
  <text x="100" y="49.85" text-anchor="middle" font-size="11" fill="#345">strategy, governance,</text>
  <text x="100" y="63.85" text-anchor="middle" font-size="11" fill="#345">organisation, key processes</text>
  <rect x="200" y="15" width="160" height="62" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/>
  <text x="280" y="35.85" text-anchor="middle" font-size="11" font-weight="bold">Data</text>
  <text x="280" y="49.85" text-anchor="middle" font-size="11" fill="#345">logical and physical</text>
  <text x="280" y="63.85" text-anchor="middle" font-size="11" fill="#345">data assets, data management</text>
  <rect x="380" y="15" width="160" height="62" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/>
  <text x="460" y="35.85" text-anchor="middle" font-size="11" font-weight="bold">Application</text>
  <text x="460" y="49.85" text-anchor="middle" font-size="11" fill="#345">the applications, their</text>
  <text x="460" y="63.85" text-anchor="middle" font-size="11" fill="#345">interactions, links to processes</text>
  <rect x="560" y="15" width="160" height="62" rx="6" fill="#fff1d6" stroke="#e0b060"/>
  <text x="640" y="35.85" text-anchor="middle" font-size="11" font-weight="bold">Technology</text>
  <text x="640" y="49.85" text-anchor="middle" font-size="11" fill="#345">software and hardware</text>
  <text x="640" y="63.85" text-anchor="middle" font-size="11" fill="#345">capabilities for the other three</text>
  <rect x="20" y="100" width="160" height="40" rx="6" fill="#fff" stroke="#666"/>
  <text x="100" y="116.85" text-anchor="middle" font-size="11" font-weight="bold">Phase B</text>
  <text x="100" y="130.85" text-anchor="middle" font-size="11" fill="#345">Business Architecture</text>
  <rect x="200" y="100" width="340" height="40" rx="6" fill="#fff" stroke="#666"/>
  <text x="370" y="116.85" text-anchor="middle" font-size="11" font-weight="bold">Phase C: one phase, two parts</text>
  <text x="370" y="130.85" text-anchor="middle" font-size="11" fill="#345">Information Systems Architectures</text>
  <rect x="560" y="100" width="160" height="40" rx="6" fill="#fff" stroke="#666"/>
  <text x="640" y="116.85" text-anchor="middle" font-size="11" font-weight="bold">Phase D</text>
  <text x="640" y="130.85" text-anchor="middle" font-size="11" fill="#345">Technology Architecture</text>
  <line x1="100" y1="78" x2="100" y2="98" stroke="#555" marker-end="url(#arr-f1-02a)"/>
  <line x1="280" y1="78" x2="280" y2="98" stroke="#555" marker-end="url(#arr-f1-02a)"/>
  <line x1="460" y1="78" x2="460" y2="98" stroke="#555" marker-end="url(#arr-f1-02a)"/>
  <line x1="640" y1="78" x2="640" y2="98" stroke="#555" marker-end="url(#arr-f1-02a)"/>
  <rect x="20" y="160" width="700" height="26" rx="6" fill="#f4f4f4" stroke="#bbb" stroke-dasharray="5 4"/>
  <text x="370" y="176.85" text-anchor="middle" font-size="11" fill="#345">Security: a cross-cutting concern addressed inside each domain, not a fifth domain</text>
  <text x="370" y="210" text-anchor="middle" font-size="11" fill="#666">mnemonic: B-D-A-T, developed in that order; Data and Application share Phase C</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">BDAT and the phases that develop them. Original drawing; the domain descriptions follow INTRO §3.</figcaption>
</figure>

## Three words the exam refuses to let you confuse

- A **deliverable** is a work product that is *contractually specified*, formally reviewed and
  signed off. It is the output of a project: the Architecture Definition Document, the
  Statement of Architecture Work.
- An **artifact** is a work product that describes *one aspect* of the architecture. Every
  artifact is a **catalog** (a list), a **matrix** (relationships between two lists) or a
  **diagram** (a picture). Deliverables contain artifacts.
- A **building block** is a *potentially reusable component of capability*: a thing that can be
  combined with other building blocks to deliver architectures and solutions. An
  **Architecture Building Block (ABB)** specifies what is needed; a **Solution Building Block
  (SBB)** is a product or custom development that provides it.

<figure class="my-4">
<svg viewBox="0 0 760 240" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="A deliverable contains artifacts (catalog, matrix, diagram); artifacts describe building blocks; an ABB specifies what an SBB provides">
  <defs><marker id="arr-f1-02b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
  <rect x="10" y="10" width="380" height="195" rx="8" fill="#f3e3f7" stroke="#b58ac9"/>
  <text x="200.0" y="28" text-anchor="middle" font-size="12" font-weight="bold">Deliverable: contractually specified, reviewed, signed off</text>
  <rect x="30" y="45" width="340" height="145" rx="8" fill="#fff" stroke="#666"/>
  <text x="200.0" y="63" text-anchor="middle" font-size="12" font-weight="bold">Artifact: describes one aspect of the architecture</text>
  <rect x="45" y="90" width="100" height="48" rx="6" fill="#f4f4f4" stroke="#bbb"/>
  <text x="95" y="110.85" text-anchor="middle" font-size="11" font-weight="bold">catalog</text>
  <text x="95" y="124.85" text-anchor="middle" font-size="11" fill="#345">a list</text>
  <rect x="150" y="90" width="100" height="48" rx="6" fill="#f4f4f4" stroke="#bbb"/>
  <text x="200" y="103.85" text-anchor="middle" font-size="11" font-weight="bold">matrix</text>
  <text x="200" y="117.85" text-anchor="middle" font-size="11" fill="#345">relationships</text>
  <text x="200" y="131.85" text-anchor="middle" font-size="11" fill="#345">between two lists</text>
  <rect x="255" y="90" width="100" height="48" rx="6" fill="#f4f4f4" stroke="#bbb"/>
  <text x="305" y="110.85" text-anchor="middle" font-size="11" font-weight="bold">diagram</text>
  <text x="305" y="124.85" text-anchor="middle" font-size="11" fill="#345">a picture</text>
  <text x="200" y="170" text-anchor="middle" font-size="11" fill="#345">every artifact is one of these three</text>
  <line x1="372" y1="118" x2="428" y2="118" stroke="#555" marker-end="url(#arr-f1-02b)"/>
  <text x="400" y="108" text-anchor="middle" font-size="10" fill="#666">describes</text>
  <rect x="430" y="45" width="320" height="145" rx="8" fill="#e3f5e1" stroke="#7fbf7a"/>
  <text x="590.0" y="63" text-anchor="middle" font-size="12" font-weight="bold">Building block: a potentially reusable component</text>
  <rect x="445" y="90" width="135" height="60" rx="6" fill="#fff" stroke="#666"/>
  <text x="512.5" y="109.85" text-anchor="middle" font-size="11" font-weight="bold">ABB</text>
  <text x="512.5" y="123.85" text-anchor="middle" font-size="11" fill="#345">Architecture Building Block</text>
  <text x="512.5" y="137.85" text-anchor="middle" font-size="11" fill="#345">specifies what is needed</text>
  <line x1="582" y1="120" x2="598" y2="120" stroke="#555" marker-end="url(#arr-f1-02b)"/>
  <rect x="600" y="90" width="135" height="60" rx="6" fill="#fff" stroke="#666"/>
  <text x="667.5" y="104.35" text-anchor="middle" font-size="11" font-weight="bold">SBB</text>
  <text x="667.5" y="117.35" text-anchor="middle" font-size="11" fill="#345">Solution Building Block</text>
  <text x="667.5" y="130.35" text-anchor="middle" font-size="11" fill="#345">product or custom build</text>
  <text x="667.5" y="143.35" text-anchor="middle" font-size="11" fill="#345">that provides it</text>
  <text x="590" y="175" text-anchor="middle" font-size="11" fill="#345">combined with other blocks to deliver architectures and solutions</text>
  <text x="380" y="225" text-anchor="middle" font-size="11" fill="#666">if it is signed, a deliverable; if it is a list, table or picture inside a document, an artifact; if you could reuse it, a building block</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">Deliverable, artifact, building block, and the ABB to SBB step. Original drawing; the definitions follow INTRO §3.</figcaption>
</figure>

A useful test: if it is signed, it is a deliverable; if it is a list, table or picture inside
a document, it is an artifact; if you could reuse it in another architecture, it is a building
block.
