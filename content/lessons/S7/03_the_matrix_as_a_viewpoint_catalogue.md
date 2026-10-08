---
title: "The Matrix as a viewpoint catalogue and a completeness check"
unit: S7
objectives: ["S7.3"]
refs: ["SABSA §3", "SABSA §2", "SABSA §6", "ARCHIMATE §13.3", "GUIDE:integrating-risk-and-security §5.11"]
reading_minutes: 9
source: authored
status: draft
---
## Two uses of one grid

By this point in the syllabus the SABSA Matrix has been filled cell by cell. This lesson steps back and uses it as a *tool* in two ways. As a **viewpoint catalogue**, each row is a view of the whole architecture for one kind of reader, and each cell is a viewpoint that says what that reader needs to see about one question. As a **completeness check**, the grid is a 36-cell inventory: an architecture with an empty cell has an unanswered question, and one whose cells do not connect vertically has a broken traceability chain (SABSA §3, §2, §6).

## The rows as views

SABSA names its six layers after the *people* who look at them, which is exactly the ISO 42010 idea of a view: a representation of the system from the perspective of a set of concerns. The ArchiMate specification defines view and viewpoint in the same sense, and TOGAF borrows the same definitions, so a learner can use one vocabulary across all three (ARCHIMATE §13.3; SABSA §2).

| Layer | Whose view | Their concern |
|---|---|---|
| Contextual | The business | What are we for, and what could help or hurt us? |
| Conceptual | The architect | What must the architecture achieve, measured how? |
| Logical | The designer | Which services, information, domains and trust deliver that? |
| Physical | The builder | Which mechanisms, structures, platforms and schedules deliver the services? |
| Component | The tradesman | Which products, tools and standards realise the mechanisms? |
| Service Management | The facilities manager | How is all of it run, measured and kept true? |

(SABSA §2, §3.)

**Trap:** SABSA's "views" are its *rows*, not its columns. The columns are the six interrogatives (What, Why, How, Who, Where, When) and are the same for every reader. A question asking "which SABSA view answers the builder's questions" wants the Physical layer, not the Process column (SABSA §3).

## The cells as viewpoints

A viewpoint is the specification of *how to construct* a view: the conventions, the model kinds, the questions it answers. Each Matrix cell is exactly that for one reader and one question. "Logical × Location" is the viewpoint *security domain model*: it says the designer should draw domains, sub-domains, policy authorities and inter-domain associations. "Physical × Time" is *control-structure execution*: the builder should show when each control runs. The cell tells you what to produce; the produced thing is the view (SABSA §3; ARCHIMATE §13.3).

Used this way the Matrix becomes a catalogue an architect can pick from. Asked for "the security architecture", the architect asks *for whom and about what*, finds the cell, and produces that view rather than a 200-page document nobody reads. Cross-framework, the ArchiMate viewpoint mechanism does the same job with a formal template, and TOGAF's architecture content framework lists its viewpoints as catalogs, matrices and diagrams; the risk and security guide notes that TOGAF's content metamodel can carry the SABSA cells as additional entities (ARCHIMATE §13.4; GUIDE:integrating-risk-and-security §5.11).

## The grid as a completeness check

The second use is the one the exam calls *completeness*. Lay the 36 cells out and ask, for the architecture in front of you:

1. **Is every cell populated?** An empty cell is an unanswered question. "Contextual × Time" empty means nobody asked when the business is exposed — trading hours, year-end, product launches (SABSA §3, §6).
2. **Does every cell connect upward?** Each cell should trace to the cell above in the same column: the Physical mechanism to the Logical service, the service to the Conceptual attribute, the attribute to a Contextual driver. This is top-down justification, column by column (SABSA §6).
3. **Does every cell connect downward?** Each attribute should reach a component and a Service Management measurement in its column. This is bottom-up completeness, column by column (SABSA §6).
4. **Do the columns cohere within a row?** A Logical-layer domain model (Location) that names roles the entity schema (People) does not know is inconsistent even if both cells are full (SABSA §3).

| Check | Reads the Matrix | Catches |
|---|---|---|
| Population | Cell by cell | Unasked questions |
| Upward links | Column, bottom to top | Unjustified content |
| Downward links | Column, top to bottom | Undelivered requirements |
| Row coherence | Row, left to right | Contradictions between views of the same layer |

(SABSA §3, §6.)

**Trap:** completeness is not "every cell has a document". A cell populated with a template nobody filled fails checks 2 and 3 even though it passes check 1. The Matrix checks *content and its links*, not the existence of files (SABSA §6).

## Using the check at gates

The Matrix check fits naturally at the gates of the SABSA Lifecycle and of the ADM. At the end of Strategy and Planning the top two rows must be complete; at the end of Design all five design rows plus the Service Management design; at the compliance review in Phase G the Component row is compared with what was built; in Manage and Measure the Service Management row must be producing measurements for every attribute. The crosswalk panels under `/adm` show which cells each ADM phase is expected to fill, which is the same check phrased per phase (SABSA §4, §6; GUIDE:integrating-risk-and-security §5).

## Check yourself

- In what sense is each Matrix row a view and each cell a viewpoint?
- Name the four completeness checks the grid supports and what each catches.
- Why does "every cell has a document" not prove completeness?

*Source note: written from the SABSA framework as published by the SABSA Institute; section numbers refer to the SABSA White Paper and are to be verified against the registered PDF.*
