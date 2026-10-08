---
title: "Business passive structure and product: object, contract, representation, product"
unit: A4
objectives: ["A4.3"]
refs: ["ARCHIMATE §8.4", "ARCHIMATE §8.4.1", "ARCHIMATE §8.4.2", "ARCHIMATE §8.4.3", "ARCHIMATE §8.5", "ARCHIMATE §8.5.1", "ARCHIMATE §8.6", "ARCHIMATE §3.6"]
reading_minutes: 8
source: authored
status: draft
---
## What passive structure means

The passive-structure aspect holds the things that behaviour acts on. In the Business Layer
these are the concepts the business thinks in — a claim, a policy, an order — manipulated by
processes and functions but never performing anything themselves (ARCHIMATE §8.4). The layer
defines two main passive elements, business object and representation, plus contract as a
specialization of business object used in the context of a product (ARCHIMATE §8.4).

<figure class="max-w-lg"><img src="/figure/ARCHIMATE:fig-64" alt="Business passive structure elements" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 64. Business Passive Structure Elements (ARCHIMATE)</figcaption></figure>

| Element | Aspect | Notation | Definition in plain words | Typical confusion |
|---|---|---|---|---|
| Business Object | Passive structure | Yellow rectangle with a header band | A concept used within a business domain, usually an object *type* rather than an instance | Confusing it with a data object: the business object is the concept, the data object is its automated form |
| Contract | Passive structure | Business object icon, labelled contract | A formal or informal agreement between provider and consumer specifying rights, obligations and interaction parameters for a product | Treating it as a separate element type: it is a specialization of business object |
| Representation | Passive structure | Yellow box with a wavy bottom edge | A perceptible form (document, message) of the information a business object carries | Confusing representation with artifact: representation is business-layer and human-perceptible; artifact is technology-layer |
| Product | Composite | Yellow box with a small rectangle icon | A coherent bundle of services and/or passive elements, with a contract, offered as a whole to customers | Assuming it can only contain business-layer things; it aggregates services and objects from any core layer |

## Business object

The language models types, not instances, because types are what matter at enterprise level; a
business object therefore behaves like a UML class of which many instances exist in operation.
Only occasionally — for singleton types with exactly one instance — does it stand for an actual
piece of information (ARCHIMATE §8.4.1, ARCHIMATE §3.6). Business objects are passive: they never
trigger or perform behaviour. They typically represent information assets that matter to the
business and can be realized by data objects (ARCHIMATE §8.4.1).

The relationships are the exam material. A business object may be *accessed* — created, read or
written — by a process, function, interaction, event or service. It may have association,
specialization, aggregation or composition relationships with other business objects. It may be
*realized* by a representation, by a data object, or by both. Name it with a noun (ARCHIMATE §8.4.1).

**Trap:** "which relationship connects a business process to the business object it updates?" is
*access*, not association and not flow. And "which element realizes a business object?" has two
right answers in the specification — representation (same layer) and data object (application
layer) — so read the options for the one that is actually offered (ARCHIMATE §8.4.1).

## Contract

A contract is a specification of an agreement between a provider and a consumer: it names the
rights and obligations attached to a product and sets the functional and non-functional terms
of the interaction. It can be a legal contract or something less formal, and it may be or include
an SLA about the quality of the services in a product (ARCHIMATE §8.4.2). Because it is a
specialization of business object, every relationship a business object supports applies to a
contract too; in addition a contract may be aggregated in a product. Name it with a noun
(ARCHIMATE §8.4.2).

## Representation

A representation is the perceptible carrier of a business object's information — a message or a
document. Representations can be classified by medium (paper, electronic, audio) or format
(PDF, HTML). One business object may have several representations, and one representation may
realize more than one business object (ARCHIMATE §8.4.3). A *meaning* (a motivation element) may
be associated with a representation that carries it. Name it with a noun (ARCHIMATE §8.4.3).

**Trap:** representation realizes business object, in the same layer. Do not confuse this with the
cross-layer chain business object ← data object ← artifact. The specification's example has the
business object "Claim" realized by three representations at different stages — a submission
form, a file summary and a letter — and a "Policy Summary" representation realizing a contract
"Insurance Policy" (ARCHIMATE §8.4).

<figure class="max-w-lg"><img src="/figure/ARCHIMATE:fig-68" alt="Product metamodel" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 68. Product Metamodel (ARCHIMATE)</figcaption></figure>

## Product, the composite element

The Business Layer has one composite element, product, which gathers services and passive
structure elements from across the core layers. Its metamodel in Figure 68 is deliberately
cross-layer, and Chapter 11 returns to it (ARCHIMATE §8.5). A product is a coherent set of
services and/or passive elements, accompanied by a contract, offered as a whole to internal or
external customers. The definition covers intangible, information-based products as well as
physical ones; "buying" is usually one of the product's services and results in a new instance
of the product for that customer (ARCHIMATE §8.5.1).

The product element normally specifies a product *type*; product types are stable compared with
the processes that realize them. A product may aggregate or compose business, application and
technology services, business objects, data objects, artifacts and material, and a contract. A
value may be associated with it. Name it as customers know it ("travel insurance")
(ARCHIMATE §8.5.1).

**Trap:** the exam asks "which of the following may a product aggregate?" and offers a business
process among the options. Processes are not in the list — only services, passive structure
elements and the contract. The processes that *realize* the product's services sit outside it
(ARCHIMATE §8.5.1).

## The example

An "Insurance" product consists of an "Insurance Policy" contract and a "Customer Service"
business service that aggregates four further services (application, renewal, claims processing,
appeal). "Auto Insurance" specializes "Insurance" and adds one more service and its own
agreement contract. Specialization of a product, aggregation of services, and the contract as a
part are the three things to recognise (ARCHIMATE §8.5).

Table 6 gives the one-line definitions for business object, contract, representation and
product; the distinctive words are "concept", "agreement", "perceptible form" and "coherent
collection ... accompanied by a contract" (ARCHIMATE §8.6).
