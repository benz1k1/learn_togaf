---
title: "Dependency relationships: serving, access, influence and association"
unit: A7
objectives: ["A7.2"]
refs: ["ARCHIMATE §5.2", "ARCHIMATE §5.2.1", "ARCHIMATE §5.2.2", "ARCHIMATE §5.2.3", "ARCHIMATE §5.2.4", "ARCHIMATE §5.2.5", "ARCHIMATE §5.6"]
reading_minutes: 9
source: authored
status: draft
---
## What a dependency says

A dependency relationship says that one element supports, feeds or affects another without
being part of it. There are four, each drawn with a different line so the eye can tell them
apart: serving is a **solid** line (a control dependency), access is a **dotted** line (a data
dependency), influence is a **dashed** line (an impact dependency), and association is the plain
line used for whatever the other three do not cover (ARCHIMATE §5.2).

| Relationship | Notation | From → To | Meaning |
|---|---|---|---|
| **Serving** | solid line, open arrowhead | provider → the element it serves | provides functionality to |
| **Access** | dotted line, optional arrowhead(s) | behaviour or active structure → passive structure | observes or acts on an object |
| **Influence** | dashed line, open arrowhead, optional +/− label | any element → a motivation element | helps or hinders achievement |
| **Association** | plain line, optionally half-arrow | undirected unless made directed | an unspecified or otherwise unnamed link |

<figure class="max-w-lg"><img src="/figure/ARCHIMATE:fig-26" alt="Serving notation" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 26. Serving Notation (ARCHIMATE)</figcaption></figure>

## Why the arrows point "up"

The dependency arrows in ArchiMate usually point the opposite way to a UML dependency. In UML the
caller points at what it calls; in ArchiMate the *provider* points at the *user*. Two reasons are
given. First, it makes layered models readable: supporting, serving and realizing arrows all point
upward toward the business. Second, it separates delivery from initiative — a service is delivered
in the same direction whether the user pulled it or the provider pushed it. When the initiative
itself matters, that is what triggering is for, and when something is transferred, flow (ARCHIMATE
§5.2).

**Trap:** "served by" reads against the arrow. If an application service serves a business
process, the arrowhead is on the process. An option that draws the arrow from the process to the
service, or phrases it as "the process serves the service", is wrong (ARCHIMATE §5.2.1).

## Serving

Serving was called "used by" until ArchiMate 3.0; the name changed to an active verb so the
direction reads naturally — *a service serves a user* — while the meaning stayed identical, and
"used by" remains accepted but deprecated. It applies to both behaviour (a service serving a process)
and active structure (an interface serving an actor) (ARCHIMATE §5.2.1).

## Access

Access is the only relationship that reaches a **passive structure** element from behaviour or
active structure. At the metamodel level it always points from the accessor to the object; the
notation can still show an arrowhead at either end to say what kind of access it is (ARCHIMATE
§5.2.2).

| Drawn as | Read as |
|---|---|
| dotted line, arrowhead at the object | write (create, update, delete) |
| dotted line, arrowhead at the accessor | read |
| dotted line, arrowheads at both ends | read-write |
| dotted line, no arrowhead | undirected "uses in some way", also for the information carried by an event or service |

<figure class="max-w-lg"><img src="/figure/ARCHIMATE:fig-27" alt="Access notation" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 27. Access Notation (ARCHIMATE)</figcaption></figure>

**Trap:** the arrowhead on an access relationship says *read or write*; it says nothing about
which element is the source. The source is always the behaviour or active-structure element, even
when the arrowhead sits on it (read). This matters in derivation: a read access with the arrow
"pointing back" is still a relationship from the process to the object, so it chains with a
structural relationship on the *process* side, not the object side (ARCHIMATE §5.2.2).

Access can also be shown by nesting a data object inside the component that uses it. The classic
example is a two-step process: "Create Invoice" writes the Invoice object, "Send Invoice" reads it
(ARCHIMATE §5.2.2).

## Influence

Influence says that an element affects — helps or hinders — the achievement of a **motivation**
element such as a goal, principle or requirement. It is the weaker cousin of realization: use
realization when the source is critical to the target's existence, influence when it merely
contributes. A construction crew *realizes* the goal of finishing the building; a requirement for
extra workers on an already adequate crew *influences* it (ARCHIMATE §5.2.3).

It runs both "vertically", from core elements up to requirements and goals to build a traceable
why-chain, and "horizontally" between motivation elements, where one goal's degree of achievement
moves another's. A modeller may attach a sign or strength — `++`, `+`, `0`, `−`, `−−`, or a numeric
scale — but by default the sign and strength are unspecified (ARCHIMATE §5.2.3).

**Trap:** the target of an influence relationship must be a motivation element. "Application
component influences business process" is not a legal influence; "application component influences
requirement" is (ARCHIMATE §5.2.3).

## Association

Association is the catch-all: an unspecified link, or one the other types do not express. It is
always allowed between any two elements and between any relationship and an element, which is why a
first sketch of a model can be drawn entirely in associations and refined later. It is undirected
by default; a directed association (half-arrow at the target) may be drawn, and once directed it
can only take part in derivations in that direction. The specification's own example is a contract
associated with the business objects it refers to, and a flow relationship associated with the
contract that travels along it (ARCHIMATE §5.2.4).

## Dependency semantics: parts, not wholes

Where structural relationships tolerate unmodelled detail on the source, dependency relationships
tolerate it on **both** ends: a dependency between A and B means some part of B depends on some part
of A. If a service serves a process, an unmodelled sub-service may be what serves an unmodelled
sub-process. The same holds for access (some part of the function reads some part of the object)
and for influence. This is why a dependency drawn at a high level does not commit the modeller to
any particular dependency at the detailed level (ARCHIMATE §5.2.5).

## Worked reading

"Payment Service —serves→ Pay Invoices (process); Payment Interface —serves→ Customer (actor);
Pay Invoices —access (arrow at object)→ Invoice." The customer is reached through the interface, the
process uses the service, and the process writes the invoice. Change the access arrowhead to the
process end and the process only reads the invoice; nothing else in the sentence moves (ARCHIMATE
§5.6).

## Check yourself

- Which line style is access, and which is influence?
- Where does the arrowhead sit for a read access, and which element is nevertheless the source?
- Name a legal and an illegal target for influence.
