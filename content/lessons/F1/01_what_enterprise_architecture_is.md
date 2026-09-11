---
title: What enterprise architecture is, and what the TOGAF Standard is for
unit: F1
objectives: ["1.1", "1.2"]
refs: ["INTRO §1", "INTRO §2"]
reading_minutes: 6
source: authored
status: draft
---
## Why an enterprise needs an architecture

An enterprise is any collection of organisations with a common set of goals: a company, a
government department, a division. Its systems, processes and people were built at different
times for different reasons. **Enterprise architecture** is the discipline of describing that
whole as one system, deciding what it should become, and governing the change from one to the
other, so that investments add up rather than collide.

The standard's own framing (INTRO §1): an architecture is *the fundamental concepts or
properties of a system in its environment, embodied in its elements, relationships, and the
principles of its design and evolution*. Two ideas are doing the work there. First, the
*environment*: an architecture is never just the system. Second, *principles of evolution*:
the architecture is also about how the system is allowed to change.

## What the TOGAF Standard provides

The TOGAF Standard is an **architecture framework**: a method, a set of tools and a common
vocabulary for producing and managing architectures. It is not a reference architecture and
does not prescribe what any enterprise's architecture should look like. It gives (INTRO §2):

- the **Architecture Development Method (ADM)**, a phased, iterative method for developing an
  architecture and managing its realisation;
- a **content framework**, which says what an architecture description consists of;
- a **capability framework**, which says how an organisation sets itself up to do this work;
- guidance on **applying** the method: iteration, partitioning, security, agile.

<figure class="my-4">
<svg viewBox="0 0 760 195" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="The TOGAF Standard as a framework providing the ADM, a content framework, a capability framework and guidance on applying the method">
  <defs><marker id="arr-f1-01a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
  <rect x="230" y="10" width="300" height="40" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
  <text x="380" y="26.85" text-anchor="middle" font-size="11" font-weight="bold">The TOGAF Standard: an architecture framework</text>
  <text x="380" y="40.85" text-anchor="middle" font-size="11" fill="#345">a method, a set of tools and a common vocabulary</text>
  <rect x="10" y="85" width="175" height="84" rx="6" fill="#fff" stroke="#666"/>
  <text x="97.5" y="98.35" text-anchor="middle" font-size="11" font-weight="bold">The ADM</text>
  <text x="97.5" y="111.35" text-anchor="middle" font-size="11" fill="#345">Architecture Development</text>
  <text x="97.5" y="124.35" text-anchor="middle" font-size="11" fill="#345">Method: a phased, iterative</text>
  <text x="97.5" y="137.35" text-anchor="middle" font-size="11" fill="#345">method for developing an</text>
  <text x="97.5" y="150.35" text-anchor="middle" font-size="11" fill="#345">architecture and managing</text>
  <text x="97.5" y="163.35" text-anchor="middle" font-size="11" fill="#345">its realisation</text>
  <line x1="380" y1="50" x2="97" y2="84" stroke="#555" marker-end="url(#arr-f1-01a)"/>
  <rect x="195" y="85" width="175" height="84" rx="6" fill="#fff" stroke="#666"/>
  <text x="282.5" y="117.85" text-anchor="middle" font-size="11" font-weight="bold">Content framework</text>
  <text x="282.5" y="130.85" text-anchor="middle" font-size="11" fill="#345">what an architecture</text>
  <text x="282.5" y="143.85" text-anchor="middle" font-size="11" fill="#345">description consists of</text>
  <line x1="380" y1="50" x2="282" y2="84" stroke="#555" marker-end="url(#arr-f1-01a)"/>
  <rect x="380" y="85" width="175" height="84" rx="6" fill="#fff" stroke="#666"/>
  <text x="467.5" y="117.85" text-anchor="middle" font-size="11" font-weight="bold">Capability framework</text>
  <text x="467.5" y="130.85" text-anchor="middle" font-size="11" fill="#345">how an organisation sets</text>
  <text x="467.5" y="143.85" text-anchor="middle" font-size="11" fill="#345">itself up to do this work</text>
  <line x1="380" y1="50" x2="467" y2="84" stroke="#555" marker-end="url(#arr-f1-01a)"/>
  <rect x="565" y="85" width="175" height="84" rx="6" fill="#fff" stroke="#666"/>
  <text x="652.5" y="117.85" text-anchor="middle" font-size="11" font-weight="bold">Guidance on applying it</text>
  <text x="652.5" y="130.85" text-anchor="middle" font-size="11" fill="#345">iteration, partitioning,</text>
  <text x="652.5" y="143.85" text-anchor="middle" font-size="11" fill="#345">security, agile</text>
  <line x1="380" y1="50" x2="652" y2="84" stroke="#555" marker-end="url(#arr-f1-01a)"/>
  <text x="380" y="185" text-anchor="middle" font-size="11" fill="#666">not a reference architecture: it does not say what any enterprise's architecture should look like</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">The four things the framework gives you. Original drawing; the list follows INTRO §2.</figcaption>
</figure>

## The shape of the 10th Edition

The 10th Edition is a set of documents, not a book. The **TOGAF Fundamental Content** is the
stable core, in six documents: *Introduction and Core Concepts*, *Architecture Development
Method*, *ADM Techniques*, *Applying the ADM*, *Architecture Content*, and *Enterprise
Architecture Capability and Governance*. The **TOGAF Series Guides** extend it with practice
guidance (business scenarios, capabilities, value streams, agile, security, digital, and more)
and are revised more often. Foundation questions come from the Fundamental Content; the
Practitioner exam reaches into the guides.

<figure class="my-4">
<svg viewBox="0 0 760 235" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="The 10th Edition: six Fundamental Content documents plus the Series Guides make up the Standard">
  <defs><marker id="arr-f1-01b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
  <rect x="10" y="10" width="740" height="215" rx="8" fill="#f4f4f4" stroke="#bbb" stroke-dasharray="6 4"/>
  <text x="380.0" y="28" text-anchor="middle" font-size="12" font-weight="bold">The TOGAF Standard, 10th Edition = Fundamental Content + Series Guides</text>
  <rect x="25" y="40" width="480" height="175" rx="8" fill="#e0ecff" stroke="#7aa2e3"/>
  <text x="265.0" y="58" text-anchor="middle" font-size="12" font-weight="bold">TOGAF Fundamental Content: the stable core, six documents</text>
  <rect x="35" y="70" width="145" height="50" rx="6" fill="#fff" stroke="#666"/>
  <text x="107.5" y="91.85" text-anchor="middle" font-size="11" fill="#345">Introduction and Core</text>
  <text x="107.5" y="105.85" text-anchor="middle" font-size="11" fill="#345">Concepts</text>
  <rect x="190" y="70" width="145" height="50" rx="6" fill="#fff" stroke="#666"/>
  <text x="262.5" y="91.85" text-anchor="middle" font-size="11" fill="#345">Architecture</text>
  <text x="262.5" y="105.85" text-anchor="middle" font-size="11" fill="#345">Development Method</text>
  <rect x="345" y="70" width="145" height="50" rx="6" fill="#fff" stroke="#666"/>
  <text x="417.5" y="98.85" text-anchor="middle" font-size="11" fill="#345">ADM Techniques</text>
  <rect x="35" y="135" width="145" height="50" rx="6" fill="#fff" stroke="#666"/>
  <text x="107.5" y="163.85" text-anchor="middle" font-size="11" fill="#345">Applying the ADM</text>
  <rect x="190" y="135" width="145" height="50" rx="6" fill="#fff" stroke="#666"/>
  <text x="262.5" y="163.85" text-anchor="middle" font-size="11" fill="#345">Architecture Content</text>
  <rect x="345" y="135" width="145" height="50" rx="6" fill="#fff" stroke="#666"/>
  <text x="417.5" y="156.85" text-anchor="middle" font-size="11" fill="#345">EA Capability and</text>
  <text x="417.5" y="170.85" text-anchor="middle" font-size="11" fill="#345">Governance</text>
  <text x="512" y="132" text-anchor="middle" font-size="20" font-weight="bold">+</text>
  <rect x="520" y="40" width="215" height="175" rx="8" fill="#fff1d6" stroke="#e0b060"/>
  <text x="627.5" y="58" text-anchor="middle" font-size="12" font-weight="bold">TOGAF Series Guides</text>
  <text x="627" y="78" text-anchor="middle" font-size="11" fill="#345">practice guidance:</text>
  <text x="627" y="93" text-anchor="middle" font-size="11" fill="#345">business scenarios, capabilities,</text>
  <text x="627" y="108" text-anchor="middle" font-size="11" fill="#345">value streams, agile, security,</text>
  <text x="627" y="123" text-anchor="middle" font-size="11" fill="#345">digital, and more</text>
  <text x="627" y="153" text-anchor="middle" font-size="11" fill="#345">revised more often than the core</text>
  <text x="627" y="200" text-anchor="middle" font-size="11" fill="#c0392b">Practitioner exam reaches in here</text>
  <text x="265" y="205" text-anchor="middle" font-size="11" fill="#c0392b">Foundation questions come from here</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">The shape of the 10th Edition. Original drawing; the six titles follow INTRO §2.</figcaption>
</figure>

## Check yourself

- Which of the six documents would you open to find the steps of Phase B?
- Is a Series Guide part of the Fundamental Content?
