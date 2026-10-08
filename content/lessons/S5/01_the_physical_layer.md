---
title: "The Physical layer: the builder's view — mechanisms, data structures and platforms"
unit: S5
objectives: ["S5.1"]
refs: ["SABSA §3.4", "SABSA §2", "GUIDE:integrating-risk-and-security §5.5", "GUIDE:integrating-risk-and-security §5.4.1"]
reading_minutes: 9
source: authored
status: draft
---
## Where the Physical layer sits

The SABSA Matrix stacks six layers, and the fourth is the **Physical** layer — the *builder's* view. Above it the Logical layer (the designer) has said *what* security services the business needs; the Physical layer says *how* those services will be delivered in the real world: with which security mechanisms, in which data structures, on which platforms and networks, under which rules and procedures, and to which timetable. It is still architecture, not procurement — the choice of a named product belongs one layer down, in the Component layer (SABSA §3.4).

The easy way to hold the layer in mind is the builder metaphor SABSA itself uses. The architect's drawings (Logical) say "a load-bearing wall here"; the builder (Physical) says "a block wall on this footing, with this reinforcement"; the tradesman (Component) picks the brand of block. Each layer is a complete architecture at its own level of abstraction, and each answers the same six questions (SABSA §2).

**Trap:** "physical" in SABSA does not mean *hardware*. The Physical layer includes data structures, procedures and schedules. A learner who answers "servers and cables" for "what is in the Physical layer" has confused SABSA's builder view with TOGAF's Technology Architecture, which is only one of its six cells (SABSA §3.4).

## The six cells

The cell names have shifted between the Blue Book (2005) and the later White Paper wording; the exam may use either. Both are given.

| Column | Blue Book cell name | Later wording | What actually goes in it |
|---|---|---|---|
| Assets (What) | Business data model | Data assets: data dictionary and data storage devices | The physical data structures that realise the logical information assets: tables, files, schemas, storage |
| Motivation (Why) | Security rules, practices and procedures | Risk management practices: rules and procedures | The concrete practices that enforce the Logical layer's policies |
| Process (How) | Security mechanisms | Process mechanisms: applications, middleware, systems, security mechanisms | Encryption, authentication protocols, logging, filtering — the mechanisms that deliver each security service |
| People (Who) | Users, applications and the user interface | Human interface: user interface to ICT systems, access control systems | How entities meet the system: login screens, tokens, access-control systems |
| Location (Where) | Platform and network infrastructure | ICT infrastructure: host platforms, layout and networks | The platforms and networks on which the domains of the Logical layer are actually hosted |
| Time (When) | Control structure execution | Processing schedule: timing and sequencing of processes and sessions | When controls run: session timeouts, batch windows, key-rotation intervals |

(SABSA §3.4; the Blue Book / White Paper split is the author's reading and should be checked against the registered PDF.)

## Reading the layer column by column

**Assets.** The Logical layer held an *inventory of information assets* classified against the Business Attributes Profile. The Physical layer turns each into a data structure and a storage location — the point at which "customer identity evidence is Confidential" becomes "the evidence table is in the encrypted store with a 30-day retention". The classification does not change on the way down; only its embodiment does (SABSA §3.4; GUIDE:integrating-risk-and-security §5.4.2).

**Motivation.** Policies are Logical; the *practices and procedures* that carry them out are Physical. A domain policy that says "privileged access is reviewed" becomes a quarterly recertification procedure with named steps (SABSA §3.4).

**Process.** This is the cell the exam drills hardest, because it is where the **security mechanism** lives. A mechanism is the physical means by which a logical security service is delivered. One service may need several mechanisms; one mechanism may serve several services. The next lesson but one traces that relationship in full (SABSA §3.4; GUIDE:integrating-risk-and-security §5.4.1).

**People.** The Logical layer defined entities, privilege profiles and a trust relationship model. Physically those become the user interface, the access-control system and the credentials people actually hold (SABSA §3.4).

**Location.** Logical domains and their inter-domain associations are hosted on real platforms and networks. This cell is the closest neighbour of TOGAF's Phase D, and the TOGAF risk and security guide's advice fits it: the Security Architect verifies that the controls are present in the technology and, if asked, produces a view that justifies each technology by the risk it mitigates (GUIDE:integrating-risk-and-security §5.5).

**Time.** Controls have execution timing — session lifetimes, certificate validity, log-retention windows. The Logical layer's calendar of start times, lifetimes and deadlines becomes the Physical layer's control-structure execution schedule (SABSA §3.4).

## How the layer is used

Two rules keep the Physical layer honest. First, **every cell traces upward**: a mechanism with no logical service above it is an orphan and a candidate for removal; a data structure with no classified information asset above it is unowned. Second, **nothing in the layer names a vendor**: "TLS 1.3 with mutual authentication" is Physical; "vendor X's gateway" is Component. Keeping that line lets the enterprise change products without redesigning the architecture (SABSA §3.4, §6).

**Trap:** the TOGAF crosswalk places the Physical layer against Phases C *and* D, not D alone. Application mechanisms (authentication, logging, encryption inside applications) are chosen during Phase C; platform and network hosting during Phase D. Answer "C and D" when a question asks which ADM phases the Physical layer overlaps (GUIDE:integrating-risk-and-security §5.4, §5.5).

## Check yourself

- Name the six Physical-layer cells in either vocabulary.
- Give one example of a security mechanism, one of a data structure and one of a control-timing decision.
- Explain why a product name does not belong in this layer.

*Source note: written from the SABSA framework as published by the SABSA Institute; section numbers refer to the SABSA White Paper and are to be verified against the registered PDF.*
