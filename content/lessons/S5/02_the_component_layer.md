---
title: "The Component layer: the tradesman's view — products, tools and standards"
unit: S5
objectives: ["S5.2"]
refs: ["SABSA §3.5", "SABSA §2", "GUIDE:integrating-risk-and-security §5.6", "GUIDE:integrating-risk-and-security §5.10.3"]
reading_minutes: 8
source: authored
status: draft
---
## Where the Component layer sits

The fifth layer of the SABSA Matrix is the **Component** layer — the *tradesman's* view. It is the most concrete of the five design layers: here the mechanisms of the Physical layer are realised with named products, specific tools, protocols, standards and identifiers. It is the layer at which a purchase order could be written. Below it there is only the Service Management layer, which runs the whole stack once it is built (SABSA §3.5, §2).

A good test for whether something belongs in the Component layer: *could two enterprises with identical Physical layers legitimately differ here?* Two banks may both need "TLS with mutual authentication and hardware-protected keys" (Physical) and choose different gateways and HSM vendors (Component). The architecture is the same; the components are not (SABSA §3.5).

**Trap:** the Component layer is not "the technology layer". It has all six columns, so it holds identities and access-control lists (People), network addresses and locators (Location) and clocks, timers and schedules (Time) as much as it holds boxes and software (SABSA §3.5).

## The six cells

| Column | Blue Book cell name | Later wording | What actually goes in it |
|---|---|---|---|
| Assets (What) | Detailed data structures | ICT components: ICT products, including data repositories and processors | The specific repositories, databases and processors that hold and process the physical data structures |
| Motivation (Why) | Security standards | Risk management tools and standards: risk-analysis tools, risk registers, monitoring and reporting tools | The standards a mechanism must meet (FIPS, ISO, internal baselines) and the tools that measure risk |
| Process (How) | Security products and tools | Process tools and standards: tools and protocols for process delivery | The named products and protocols that realise each mechanism |
| People (Who) | Identities, functions, actions and ACLs | Personnel management tools and standards: identities, job descriptions, roles, functions, actions and ACLs | Concrete identities, roles-as-configured, permission sets |
| Location (Where) | Processes, nodes, addresses and protocols | Locator tools and standards: nodes, addresses and other locators | IP addresses, hostnames, URIs, physical racks |
| Time (When) | Security step timing and sequencing | Step-timing and sequencing tools: time schedules, clocks, timers and interrupts | The scheduler, the NTP source, the timer that enforces a session limit |

(SABSA §3.5; the two-vocabulary split is the author's reading and should be checked against the registered PDF.)

## Products, tools and standards — three different things

The exam expects the three words to be kept apart:

- A **product** realises a mechanism. "Vendor X's web application firewall" is a product; "input filtering at the perimeter" is the mechanism it realises (SABSA §3.5).
- A **tool** supports a process rather than delivering a security service directly: a vulnerability scanner, a risk register application, a log-analysis console. Tools live mostly in the Motivation and Process columns of the Component layer (SABSA §3.5).
- A **standard** constrains the choice of product and the way it is configured: a cryptographic standard, a hardening baseline, an interface protocol. Standards are the Component layer's Motivation cell in the Blue Book wording, and the TOGAF risk and security guide asks that security standards be placed in the Standards Library of the Architecture Repository so that later cycles inherit them (SABSA §3.5; GUIDE:integrating-risk-and-security §5.10.3).

**Trap:** a *standard* is not a *policy*. Policy is Logical (why we protect); a standard is Component (which product or configuration satisfies the mechanism). "All passwords are hashed" is policy; "hash with algorithm A at cost factor B" is a standard (SABSA §3.5).

## The Component layer and TOGAF's Solution Building Blocks

The SABSA Component layer is the Matrix's closest neighbour to TOGAF's **Solution Building Blocks** and to the Solutions Continuum: an Architecture Building Block ("an authentication service") is Logical; its specification as a mechanism is Physical; the SBB that implements it — a product, a configured service, a custom development — is Component. The crosswalk therefore lays the Component layer across Phase D (where technology SBBs are identified) and Phase E, where the risk and security guide says *security building blocks become SBBs* and existing services may be reused only after their efficacy has been verified (GUIDE:integrating-risk-and-security §5.6).

| TOGAF | SABSA | Content |
|---|---|---|
| Architecture Building Block | Logical layer | A security service defined by what it does |
| ABB specification | Physical layer | The mechanism, data structure, platform, timing |
| Solution Building Block | Component layer | The product, tool, standard, identity, address, clock |

(SABSA §3.5; GUIDE:integrating-risk-and-security §5.6.)

## Why the layer is kept separate

If products were named in the Physical layer, every product change would be an architecture change, and every architecture review would become a vendor review. Keeping the Component layer separate gives three things: **substitutability** (swap the product, keep the mechanism), **testability** (the assurance framework can test a component against the mechanism it claims to realise) and **traceability** (a component with no mechanism above it is unjustified spend). Unit S7 builds on the last of these (SABSA §3.5, §6).

## Check yourself

- Distinguish product, tool and standard with one example each.
- Which SABSA layer corresponds to a TOGAF SBB, and which to an ABB?
- Where in the Architecture Repository does the TOGAF guide say security standards go?

*Source note: written from the SABSA framework as published by the SABSA Institute; section numbers refer to the SABSA White Paper and are to be verified against the registered PDF.*
