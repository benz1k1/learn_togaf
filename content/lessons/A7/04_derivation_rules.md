---
title: "Derivation: the valid rules, the potential rules and their restrictions"
unit: A7
objectives: ["A7.4"]
refs: ["ARCHIMATE §5.7", "ARCHIMATE §B.1", "ARCHIMATE §B.2", "ARCHIMATE §B.2.1", "ARCHIMATE §B.2.2", "ARCHIMATE §B.2.3", "ARCHIMATE §B.2.4", "ARCHIMATE §B.3", "ARCHIMATE §B.3.1", "ARCHIMATE §B.3.2", "ARCHIMATE §B.3.3", "ARCHIMATE §B.3.4", "ARCHIMATE §B.3.5", "ARCHIMATE §B.4"]
reading_minutes: 12
source: authored
status: draft
---
## Why derivation exists

A detailed model has many intermediate elements. Derivation lets you leave them out and still
draw a true relationship between the elements that remain: an application component *serves* a
business process even though, in the detailed model, the component is assigned to a function that
realizes a service that serves the process. Derivation always runs from *more* detail to *less*;
it summarises, it never adds detail. And any relationship that could be derived may be drawn
directly, without the intermediates ever being modelled — a component realizing a service is
legal on its own, with an unmodelled function assumed (ARCHIMATE §5.7).

**Trap:** you cannot run the machine backwards. From "component realizes service" you may not
conclude which function does the realizing; that is design information a modeller adds by
refining the model (ARCHIMATE §5.7).

## The notation and the two kinds of rule

Appendix B writes a relationship as `p(a,b):S` — relationship *p* from concept *a* to concept *b*
of type *S*. Concepts are named *a, b, c* in order of appearance; types *S, T, U*. The rules only
combine relationships that are themselves allowed, and the result is then allowed by definition.
There are two kinds: **valid** derivations (DR), which hold in any model, and **potential**
derivations (PDR), which may or may not be true depending on the model — the modeller decides. The
rules also do not cross from core elements to motivation, strategy or implementation-and-migration
elements except through realization and influence (ARCHIMATE §B.1).

## Valid derivations (DR 1–8)

| Rule | Given | Derive | Plain reading |
|---|---|---|---|
| **DR 1** | a –spec→ b, b –spec→ c | a –spec→ c | specialization is transitive |
| **DR 2** | a –S→ b, b –T→ c, both structural | a –U→ c, U = weaker of S, T | a structural chain collapses to its weakest link |
| **DR 3** | a –S→ b (structural), b –T→ c (dependency) | a –T→ c | a dependency's source moves back along a structural chain |
| **DR 4** | a –S→ b (structural), c –T→ b (dependency) | c –T→ a | a dependency's target moves back along a structural chain |
| **DR 5** | a –S→ b (structural), b –T→ c (dynamic) | a –T→ c | a dynamic source moves back along structure |
| **DR 6** | a –S→ b (structural), c –flow→ b | c –flow→ a | a flow's target moves back along structure |
| **DR 7** | a –trig→ b, b –T→ c (structural) | a –trig→ c | a triggering's target moves *forward* along structure |
| **DR 8** | a –trig→ b, b –trig→ c | a –trig→ c | triggering is transitive |

The strength order that DR 2 relies on is: **realization** (weakest) < assignment < aggregation <
composition (strongest). So assignment then composition yields assignment; composition then
realization yields realization; and a chain of any length yields whichever is weakest anywhere in
it (ARCHIMATE §B.2.2).

DR 3 and DR 4 are one idea split by direction: the endpoints of a dependency can be transferred
"backwards" — toward the source of the structural relationship — on either side. DR 5 through DR 7
say the same for dynamic relationships, except that triggering, with its structural-style
semantics, moves its *target* forward through the successor's parts rather than backward
(ARCHIMATE §B.2.3, ARCHIMATE §B.2.4).

### Worked chain 1 — a structural chain

"Financial Application (component) —assigned→ Financial Processing (function) —composed of→
Payment Handling (sub-function) —realizes→ Payment Service." DR 2 twice: assignment + composition
→ assignment (weaker); assignment + realization → realization. **Derived: Financial Application
realizes Payment Service.** Legal, and it may be drawn without the functions (ARCHIMATE §B.2.2).

### Worked chain 2 — structure then dependency

Add "Payment Service —serves→ Invoicing (business process)". DR 3 on the derived realization and
the serving: **Financial Application serves Invoicing.** This is the specification's own headline
example of abstracting away functions and services (ARCHIMATE §5.7, ARCHIMATE §B.2.3).

### Worked chain 3 — actor, role, process, trigger

"Sales Department (actor) —assigned→ Selling (process) —triggers→ Invoicing (process) —composed
of→ Billing —…; Invoicing —triggers→ Shipping." DR 5: the department triggers Invoicing. DR 7: the
department triggers Billing, a part of Invoicing. DR 8: Selling triggers Shipping, so the department
triggers Shipping too. All three are *valid* derivations (ARCHIMATE §B.2.4).

## Potential derivations (PDR 1–12)

Potential rules may be true; a well-designed stable model makes them trustworthy, a hastily
refined one does not. Their purpose is twofold: to enrich the metamodel with relationships the
valid rules would never produce, and to help a modeller *discover* relationships worth checking
(ARCHIMATE §B.3).

| Rule | Shape | Reading |
|---|---|---|
| **PDR 1–2** | a –spec→ b, and b is the source (1) or target (2) of a relationship T | the specialized element *a* might inherit b's relationship |
| **PDR 3–4** | a –spec→ b, and a is the source (3) or target (4) of T | the general element *b* might have the relationship a has |
| **PDR 5** | a –S→ b (structural), c –T→ a (dependency) | c –T→ b: the dependency might reach the *part* |
| **PDR 6** | a –S→ b (structural), a –T→ c (dependency) | b –T→ c: the *part* might carry the dependency |
| **PDR 7** | a –S→ b, b –T→ c, both dependency | a –U→ c, U = weaker; order: association < influence < access < serving |
| **PDR 8** | a –flow→ b, b –S→ c (structural) | a –flow→ c |
| **PDR 9** | a –S→ b (structural), a –T→ c (dynamic) | b –T→ c |
| **PDR 10** | a –flow→ b, b –flow→ c | a –flow→ c: flow chains are only *potentially* transitive |
| **PDR 11** | a –trig→ b, c –S→ b (structural) | a –trig→ c |
| **PDR 12** | grouping b aggregates a, and b –realizes/assigned→ c | a –T→ c, only if the metamodel allows it from a to c |

The specification's cautionary example: a component "Suite" served by hosting services is later
split into "Front-end" and "Back-end". PDR 5 offers every combination — front-end served by
database hosting, back-end served by website hosting — and only the architect knows which of them
is real (ARCHIMATE §B.3).

**Trap:** the direction of a specialization changes how likely a potential derivation is. Moving
a composition's source to the *specialized* element (PDR 1) is almost certain: if a project team
aggregates a project manager, an IT project team surely does. Moving a write access from a
specialized "IT Project" to the general "Project" (PDR 3) is only true for the subset of projects
that are IT projects (ARCHIMATE §B.3.1).

**Trap:** DR 8 (triggering transitive) is *valid*; PDR 10 (flow transitive) is only *potential*.
"A flows to B, B flows to C, therefore A flows to C" is a might, not a must — B may consume what it
receives (ARCHIMATE §B.3.4).

## Restrictions: what the rules may not produce

Appendix B groups elements into four domains — Motivation, Strategy, Core (the three layers plus
Location and Grouping) and Implementation and Migration — and forbids a *derived* relationship
when its domains and type do not fit. The ones that decide exam items (ARCHIMATE §B.4):

| Derived from → to | Only these types survive |
|---|---|
| Core, Strategy or I&M → Motivation | assignment, realization, influence, association |
| Motivation → anything else | association |
| Core or I&M → Strategy | realization, association |
| Strategy → Core or I&M | association |
| I&M → Core | realization, association |
| Core → I&M | assignment, association |
| anything → a passive structure element | access, assignment, association (non-passive source); realization, association (passive source) |
| any influence | target must be a motivation element |
| any access | target must be a passive structure element |

A second family of restrictions looks at the *middle* element: a derivation whose joining element
sits in a different domain from both ends is disallowed, except an I&M element reaching Motivation
or Strategy through a Core element. These restrictions apply to derived relationships only — a
relationship drawn explicitly in a metamodel figure is allowed by definition. Product and Plateau,
though composite, may only aggregate what their own metamodel fragments show (ARCHIMATE §B.4).

## A checklist for "is this derived relationship permitted?"

1. Are both input relationships themselves allowed? If not, stop.
2. Does a DR or PDR match the shape (which ends join, which types)? Note the direction of every arrow.
3. Compute the result type: weakest structural (DR 2), weakest dependency (PDR 7), or the dependency / dynamic type carried through.
4. Check the domain restrictions of §B.4 on the *result*.
5. Say whether it is valid (DR) or merely potential (PDR) — the exam distinguishes them (ARCHIMATE §B.1).

## Check yourself

- Assignment followed by realization: which type results, and by which rule?
- Which rule moves a serving relationship's target back along a composition?
- Is "actor triggers process" derivable from actor-assigned-to-process-that-triggers-process, and is it valid or potential?
