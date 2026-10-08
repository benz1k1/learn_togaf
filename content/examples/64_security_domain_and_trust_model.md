---
title: "Security domain and trust model — Digital Channels"
deliverable: Security domain model and trust model
phase: B
kind: DELIVERABLE
track: SABSA
summary: "The Logical × Location and × People cells: seven security domains with their policy authorities, sub-domains, the one-way, two-way and transitive trust between them, and the inter-domain services that carry every crossing — written so a Grouping/Location drawing can follow it."
refs: ["SABSA §5", "GUIDE:integrating-risk-and-security §5", "GUIDE:integrating-risk-and-security §3", "ADM §4"]
artefacts: []
source: authored
status: draft
---

> **What to notice.** A security domain is a set of elements that answer to one **policy authority** — it is defined by *who sets the rules*, not by a network segment or a firewall. Sub-domains inherit the parent's policy and add their own; trust between domains is a decision, directional, and never assumed to pass through a third domain unless someone says so in writing. The trap is drawing the network diagram and calling it the domain model: the vendor's cloud and the bank's data centre may be one *network* zone over a private link and are still two *domains*, because two different authorities sign their policies.

| | |
|---|---|
| Reference | SEC-DOM-2026-01, version 1.0, 8 May 2026 (Phase B); revised in Phase C for the application detail |
| Owner | Owen Price; agreed by each policy authority named below |

## Domains and policy authorities

| Domain | Policy authority | Sub-domains | What it contains |
|---|---|---|---|
| D1 Customer channel | Head of Retail (with the Head of Risk for authentication policy) | D1a Mobile App on the customer's device; D1b counter and telephone; D1c online site (retired at Target) | Channel presentation, session, device binding |
| D2 Channel API layer | CIO through the platform team; policy set by the Head of Risk | D2a Payments and Card Management APIs; D2b Onboarding API with journey token | Policy enforcement point for every channel: authentication, authorisation, rate limits, OpenAPI contracts |
| D3 Core banking | Retail IT; data policy by the Head of Finance | — | Core Banking v12, system of record for Customer and Account (CN-01) |
| D4 Cards | Head of Cards Operations | D4a Card Switch; D4b fraud rules and thresholds | Authorisation, the ISO 8583 link, rule administration |
| D5 Fraud analytics | Cards Ops Lead (rules), CIO (platform) | D5a Fraud Engine and Kafka feed; D5b analyst console; D5c retraining store (CR-2027-03) | Scoring, features, model, analyst review |
| D6 Identity verification provider | The vendor, bound by contract to the Compliance Officer's rules | — | Document and liveness checks, evidence held ≤ 30 days |
| D7 External parties | Their own | D7a card network; D7b regulator; D7c customers' networks | Outside the bank's authority; rules are taken, not set |

The Head of Risk is the *super-domain* authority: every internal domain's policy must be consistent with the risk appetite and security policy, and a conflict between two authorities (Cards wanting a lower scoring timeout than the platform can give, for instance) is escalated there rather than settled between the two.

## Trust relationships

| From | To | Kind | Basis | Inter-domain service that carries it |
|---|---|---|---|---|
| D1 → D2 | One-way | The channel trusts nothing it did not get from the API layer; the API layer trusts a channel only for an authenticated session | OAuth 2.1 channel authentication; TLS |
| D2 ↔ D3 | Two-way, bounded | Core Banking trusts the API layer's service identity for the operations in IF-01; the API layer trusts Core Banking as the record | Mutually authenticated service call, idempotent transfers |
| D2 → D6 | One-way, contractual | The bank sends evidence and trusts the decision; the vendor is trusted for nothing else and never sees an account | IF-03 asynchronous decision with callback; private link |
| D4 ↔ D5 | Two-way, timed | The Switch trusts a score it receives within 150 ms; the engine trusts the Switch's event stream | IF-02 synchronous scoring; Kafka card events |
| D5 → D4b | One-way | Analysts may block a card; they may not change what a rule says without the rules authority | Console action logged and attributed |
| D4a ↔ D7a | Two-way, standard-defined | Defined entirely by the card network's rules and ISO 8583 | Dual-homed network link (WP-5) |
| D1 → D3 | **Denied** | No channel reaches Core Banking directly; the pre-programme direct integrations are removed | — |
| D6 → D3 | **Denied, no transitive trust** | The vendor's decision is trusted by D2, which then acts on D3; the vendor never inherits D2's trust in Core Banking | Broken deliberately at the API layer |
| D5c → anywhere | Denied until CR-2027-03 conditions met | The retraining store holds pseudonymised data only and exports nothing | — |

The two denied transitive paths are the model's most important lines. Without the second, a compromised verification vendor would have a path to the customer record via the API layer's credentials; the API layer therefore holds a separate, narrower identity for the vendor callback than for its Core Banking calls.

## How a drawing would follow this

Each domain is a **Grouping** labelled with its policy authority, nested for sub-domains; the two data centres, the vendor's in-country site and the customer's device are **Locations** that the groupings sit in (D2 and D5 span both data centres, D6 sits in the vendor location, D1a in the device). Trust is an association from the trusting domain to the trusted one, annotated one-way or two-way; the inter-domain services are **Application Interfaces** on the boundary of the domain that serves them, and the denied paths are drawn as crossed associations so a reviewer can see what was decided rather than what was forgotten.

## In the other frameworks

TOGAF's Phase B holds this as the Security Domain Model and Trust Framework of G152 §5.3, alongside the *Organization/Actor catalog* and the *Business Interaction matrix*; ArchiMate draws it as an *Organization view* with Grouping and Location, and the *Application Cooperation view* for the inter-domain interfaces.

*Source note: SABSA framework as published by the SABSA Institute (open-use with attribution); section numbers refer to the SABSA White Paper and are to be verified against the registered PDF.*
