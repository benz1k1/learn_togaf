---
title: "Conceptual Data Diagram as an ArchiMate Information Structure view — Digital Channels"
deliverable: Conceptual Data Diagram as an ArchiMate view
phase: C
kind: MODEL
track: ARCHIMATE
summary: "The five business entities of Northgate's Phase C conceptual model drawn as Business Objects, with cardinalities as association labels and the two payment kinds as specializations."
refs: ["ARCHIMATE §C.1", "CONTENT §3.6.5"]
figure: CONCEPTUAL_DATA_DIAGRAM.svg
viewpoint: Information Structure
artefacts: [CONCEPTUAL_DATA_DIAGRAM]
source: authored
status: draft
---

> **What to notice.** Everything on this view is one element type. The Information Structure viewpoint (ARCHIMATE §C.1) exists to show the structure of the information the business works with, and at the conceptual level that is Business Objects and nothing else — no Data Objects, no components, no processes. The whole meaning is carried by the *relationships*: which entity owns which, which merely refers to which, and which is a kind of another. That is the same discipline the TOGAF Conceptual Data diagram asks for (CONTENT §3.6.5): names and cardinalities, no attributes.

## How to read the view

Start at **Customer**. A customer *holds* accounts, and the account has no meaning without the customer that holds it, so the relationship is **aggregation** (hollow diamond at the whole end), labelled with the cardinality `1..*`. An account is *linked to* cards in the same way. A card *records* transactions, but a transaction is a fact in its own right — it survives the card being cancelled — so that is a plain **association**, again labelled. **Loan** hangs off Customer and Account by two associations, exactly as it does in the TOGAF drawing.

The bottom row is new to the ArchiMate rendering. **Transfer** and **Card Payment** are drawn as **specializations** of Transaction (hollow triangle at the general end, ARCHIMATE §5.4.3). The programme's two headline features — mobile transfers and card payments with real-time scoring — are both *kinds of transaction*, and saying so in the conceptual model is what lets the Fraud Score in the logical model attach to one kind and not the other.

## Elements

| Element | ArchiMate type | Aspect / layer | Why that type |
|---|---|---|---|
| Customer, Account, Card, Transaction, Loan | Business Object | passive structure, Business layer | A conceptual entity is a business-level piece of information, independent of any application that holds it |
| Transfer, Card Payment | Business Object | passive structure, Business layer | Sub-types of Transaction; still business concepts, not records |

## Relationships used

| Relationship | Notation | What it says here |
|---|---|---|
| Aggregation (Customer → Account, Account → Card) | hollow diamond at the whole | The whole groups the parts; a part can exist on its own but belongs to one whole at a time |
| Association, labelled (Card → Transaction, Customer → Loan, Loan → Account) | plain line | A relationship that is not ownership; the label carries the cardinality the TOGAF drawing showed as crow's feet |
| Specialization (Transfer → Transaction, Card Payment → Transaction) | hollow triangle at the general element | Transfer *is a* Transaction; anything true of Transaction is true of Transfer |

Composition is permitted by the viewpoint and would be right for a part that cannot exist without its whole (a statement line inside a statement); Northgate has no such entity at this level, so it is not used.

## What changed from the TOGAF drawing

The TOGAF Conceptual Data diagram is an entity-relationship sketch: boxes, crow's-foot ends, verb labels. The ArchiMate view keeps every box and every verb but replaces the crow's foot with the language's own distinction between aggregation and association, and adds the two specializations. Nothing about the *content* changed — a reader of either tab sees the same five entities and the same cardinalities. What the ArchiMate tab adds is that the same Business Objects will reappear on the Logical Data view, realized by Data Objects, and on the Data Dissemination view, accessed by components: one element, several views (ARCHIMATE §3.4).

## Draw it yourself

1. In Archi, create a new view and choose the *Information Structure* viewpoint so the palette hides everything but passive-structure elements.
2. Add five Business Objects named as above; add Transfer and Card Payment.
3. Draw Aggregation from Customer to Account and from Account to Card; Archi puts the diamond at the source, so start the drag from the whole.
4. Draw the three Associations and type the cardinality into each relationship's name so it appears as a label.
5. Draw Specialization from Transfer and Card Payment to Transaction; run *Validate model* to confirm every relationship is permitted.
