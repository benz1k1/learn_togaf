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

A useful test: if it is signed, it is a deliverable; if it is a list, table or picture inside
a document, it is an artifact; if you could reuse it in another architecture, it is a building
block.
