---
title: "SABSA beside Zachman and TOGAF, and the SABSA Lifecycle"
unit: S1
objectives: ["S1.3"]
refs: ["SABSA §1.3", "SABSA §2.1", "SABSA §5", "SABSA §5.1", "GUIDE:integrating-risk-and-security §2.8", "GUIDE:integrating-risk-and-security §3", "GUIDE:integrating-risk-and-security §5"]
reading_minutes: 9
source: authored
status: draft
---
## Three frameworks, three questions

The learner who arrives here from TOGAF should hold three frameworks apart by the question each
answers. **Zachman** is a classification scheme: a grid of perspectives against interrogatives
that says *where* an architectural fact belongs, and nothing about how to produce it. **TOGAF**
is a method: the ADM says *how* architecture work is done, governed and changed, with a content
framework for what it produces. **SABSA** is a security-specific framework and method: it says
*why* each security element exists, in the business's own risk terms, and how that reasoning
stays traceable from strategy to daily operations (SABSA §1.3).

## SABSA and Zachman

The SABSA Matrix openly borrows Zachman's shape. Zachman's columns are the six interrogatives
(what, how, where, who, when, why); SABSA uses the same six, reordered and renamed as Assets,
Motivation, Process, People, Location and Time. Zachman's rows are perspectives (planner, owner,
designer, builder, subcontractor, functioning enterprise); SABSA's rows are the business,
architect, designer, builder and tradesman views plus the Service Management view. Two
differences matter for the exam (SABSA §2.1):

| Aspect | Zachman | SABSA |
|---|---|---|
| Purpose | Taxonomy for classifying any enterprise artefact | Security architecture framework *and* development method |
| Column order | What, How, Where, Who, When, Why | Assets (what), Motivation (why), Process (how), People (who), Location (where), Time (when) |
| Sixth row | The functioning enterprise | Service Management, which also cuts across the other five |
| Content of cells | Generic models | Security-specific content, with a risk model down the Motivation column |
| Method | None prescribed | The SABSA Lifecycle and the Business Attributes Profile |

> **Trap.** SABSA's Motivation column is the *second* column, not the last. The paper may ask
> which column holds "why", or which column is second; the answer is Motivation either way.

## SABSA and TOGAF

TOGAF and SABSA are complementary and were formally bridged by The Open Group and the SABSA
Institute. The white paper *TOGAF and SABSA Integration* (W117) maps the Business Attributes
Profile and the Matrix onto the ADM phases, and the Series Guide *Integrating Risk and Security
within a TOGAF Enterprise Architecture* (G152) carries that into the standard's own guidance.
The guide names SABSA as the source of its business-attribute approach and describes the two
as fitting together: TOGAF supplies the method and the governance, SABSA supplies the security
reasoning and the traceability (GUIDE:integrating-risk-and-security §2.8).

The mapping the app uses on `/adm/{phase}` is: Contextual and Conceptual layers ≈ Preliminary
Phase and Phase A; Logical ≈ Phases B–C; Physical ≈ C–D; Component ≈ D; Service Management ≈
G–H. It is a mapping of *where the work is done*, not a claim that the artefacts are identical:
a TOGAF principle is not a SABSA business attribute, and a TOGAF Business Architecture domain is
not a SABSA security domain (GUIDE:integrating-risk-and-security §5).

| Word | TOGAF meaning | SABSA meaning |
|---|---|---|
| Domain | Business, Data, Application or Technology architecture | A set of elements under one policy authority |
| Principle | Enduring rule with rationale and implications | Not a first-class term; policy sits at the Conceptual layer |
| Service | Business, IS or technology service in the metamodel | Security service at the Logical layer |
| Requirement | Managed across the ADM by Requirements Management | A business attribute with a performance target |
| Risk | Technique in Phases A and G; initial versus residual | Two-sided: threat and opportunity |
| View | ISO 42010 sense, from a viewpoint | One of the six Matrix rows |

(SABSA §1.3)

## The SABSA Lifecycle

The Matrix is static; the **Lifecycle** is how it is built and kept alive. It has four phases
(SABSA §5):

| Lifecycle phase | Matrix layers | What happens |
|---|---|---|
| **Strategy and Planning** | Contextual, Conceptual | Understand the business, its drivers and risks; build the Business Attributes Profile, the objectives, the domain framework |
| **Design** | Logical, Physical, Component | Design the services, mechanisms and components that make each attribute true |
| **Implement** | The transition into operations | Build, test and deploy; hand over to service management |
| **Manage and Measure** | Service Management | Run the services; measure attribute performance against target; feed results back into strategy |

The loop closes at the last phase: attribute **metrics** gathered in Manage and Measure return to
Strategy and Planning, so the profile is re-baselined against what the business actually
experienced. That is why a performance target is set at the Conceptual layer and measured at the
Service Management layer — the same attribute, seen twice (SABSA §5.1).

> **Trap.** The Lifecycle is not a seventh row. It is the *process* that fills and maintains the
> six rows. "Manage and Measure" corresponds to the Service Management layer; "Strategy and
> Planning" to the top two layers; "Design" to the middle three.

## In TOGAF terms

The Lifecycle is the ADM cycle with security names. Strategy and Planning is the Preliminary
Phase and Phase A; Design is Phases B to D; Implement is Phases E to G (opportunities, migration
planning and implementation governance); Manage and Measure is Phase H, with the attribute
metrics playing the part of the Architecture Contract's measures and the change requests that
re-enter the cycle. Requirements Management, which runs throughout the ADM, is where the TOGAF
guide places the Business Attribute Profile itself
(GUIDE:integrating-risk-and-security §3).

*Source note: written from the SABSA framework as published by the SABSA Institute; section numbers refer to the SABSA White Paper and are to be verified against the registered PDF.*
