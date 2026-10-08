---
title: "Triggering, flow, specialization and the junction"
unit: A7
objectives: ["A7.3"]
refs: ["ARCHIMATE §5.3", "ARCHIMATE §5.3.1", "ARCHIMATE §5.3.2", "ARCHIMATE §5.3.3", "ARCHIMATE §5.4.1", "ARCHIMATE §5.5.1", "ARCHIMATE §5.6"]
reading_minutes: 8
source: authored
status: draft
---
## Dynamic relationships: time enters the model

Structural and dependency relationships describe a standing state of affairs. The two dynamic
relationships add *time*: what must happen before what, and what is passed from one behaviour to
another. Both are drawn as solid lines with a filled arrowhead; flow adds dashes (ARCHIMATE §5.3).

| Relationship | Notation | From → To | Meaning | Implies causality? |
|---|---|---|---|---|
| **Triggering** | solid line, filled arrowhead | predecessor → successor | temporal or causal precedence | yes — the target cannot start until part of the source has completed |
| **Flow** | dashed line, filled arrowhead | sender → receiver | transfer of information, goods or money | no |

<figure class="max-w-lg"><img src="/figure/ARCHIMATE:fig-30" alt="Triggering notation" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 30. Triggering Notation (ARCHIMATE)</figcaption></figure>

### Triggering

Triggering orders behaviour: some part of the source must finish before the target can begin. It
does not require that the source actively *starts* the target — the specification's image is a
traffic light turning green, which triggers the cars without doing anything to them. Triggering
is the usual connector between the sub-processes of a process and between events and the
processes they start or end (ARCHIMATE §5.3.1).

### Flow

Flow records that something moves between two behaviour elements: a claims-assessment function
forwarding its decisions to claims settlement, or receiving schedule information from a scheduling
function. Flow is silent about causality — receiving a schedule does not mean assessment waits for
it — so a question that asks which relationship shows "B starts after A" wants triggering, and one
that asks which shows "A passes data to B" wants flow (ARCHIMATE §5.3.2).

**Trap:** triggering and flow are both dynamic, but their semantics come from different families.
Triggering behaves like a *structural* relationship — everything in the target is preceded by some
part of the source, so a triggering from process A to process B orders all of B after part of A.
Flow behaves like a *dependency* — some part of A passes something to some part of B, with no
commitment about the rest. That difference is exactly why the derivation rules treat them
differently (ARCHIMATE §5.3.3).

## Specialization: the "other" relationship

Specialization says an element is a particular kind of another element. It is drawn as a solid
line with a large hollow arrowhead pointing at the *general* element, or by nesting the special
element inside the general one. Like composition and aggregation it is always allowed between two
elements of the same type — a "Take Out Travel Insurance" process specializing a "Take Out
Insurance" process is the specification's own example — and it is the only member of the "other"
family (ARCHIMATE §5.4.1).

<figure class="max-w-lg"><img src="/figure/ARCHIMATE:fig-32" alt="Specialization notation" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 32. Specialization Notation (ARCHIMATE)</figcaption></figure>

**Trap:** the hollow triangle is shared by realization and specialization. Realization has a
*dotted* line and crosses abstraction levels (process → service); specialization has a *solid*
line and stays within one type (process → more general process). An option that has a data object
"specializing" a business object is wrong on both counts — the types differ and the relationship
wanted is realization (ARCHIMATE §5.4.1).

## The junction: a connector, not a relationship

A junction is drawn as a small circle — filled for **and**, hollow for **or** — and joins several
relationships of the *same* type. It may fan in (several incoming, one outgoing), fan out, or both,
the last being shorthand for two junctions back to back. An and-junction says every connected
element takes part together; an or-junction says at least one does, and whether the "or" is
inclusive or exclusive can be recorded in the junction's name. Arrowheads on relationships leading
into a junction may be left off (ARCHIMATE §5.5.1).

<figure class="max-w-lg"><img src="/figure/ARCHIMATE:fig-33" alt="Junction notation" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 33. Junction Notation (ARCHIMATE)</figcaption></figure>

Two rules protect the metamodel. A path through a junction is only legal between two concepts if
the same direct relationship would be legal — junctions never create new permissions. And every
relationship on one junction must be of one type: an and-junction cannot merge a realization with a
serving. A junction may itself be aggregated or composed inside a plateau, grouping or location,
in which case that containment is read on its own and does not join the junction's relationships
(ARCHIMATE §5.5.1).

Junctions are the ArchiMate way to draw high-level process flow: an or-junction on outgoing
triggerings shows a choice (assess a request, then accept *or* reject it), and a label on an
outgoing triggering can name the condition. The label is informal; ArchiMate deliberately defines
no execution semantics so that mappings to BPMN gateways or UML forks stay unconstrained. Two
separate triggerings without a junction are read as *both* successors being triggered
(ARCHIMATE §5.5.1).

## Worked reading

"Sales (function) and Finance (function) both —realize→ [and-junction] —realizes→ Invoicing
Service": the two functions jointly realize the service, neither alone suffices. Compare the
two-arrow version without a junction, where either function on its own would realize the whole
service. "Assess Request —triggers→ [or-junction] —triggers→ Accept Request / Reject Request":
one path is taken. Swap the or for an and and the model claims both paths always follow
(ARCHIMATE §5.6).

## Check yourself

- Which dynamic relationship carries no causal claim?
- Which relationship families do triggering and flow borrow their semantics from?
- Can an or-junction join one realization and one serving relationship?
