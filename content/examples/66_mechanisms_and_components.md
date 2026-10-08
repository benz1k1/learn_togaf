---
title: "Security mechanisms and components — Digital Channels"
deliverable: Security mechanisms and components
phase: D
kind: DELIVERABLE
track: SABSA
summary: "The Physical and Component layers for the top security services: each logical service dropped to the mechanism that realises it and then to the product or standard that implements the mechanism, the same three-step fall as ABB to SBB to product."
refs: ["SABSA §5", "GUIDE:integrating-risk-and-security §5", "GUIDE:integrating-risk-and-security §3", "ADM §7"]
artefacts: []
source: authored
status: draft
---

> **What to notice.** SABSA drops from *service* to *mechanism* to *component* in two deliberate steps. A mechanism is a way of doing it (tokenisation, TLS, a hardware security module) and is still product-neutral; a component is the thing you buy, configure and patch (this vendor's HSM, this version of TLS, this SIEM). The trap is collapsing the steps — "authentication = the identity product" — because then a product swap orphans the service, and a control gap (document 67) cannot say whether the *mechanism* is missing or only the *product* is late. This is TOGAF's Architecture Building Block → Solution Building Block distinction, applied to controls.

| | |
|---|---|
| Reference | SEC-MECH-2026-01, version 1.0, 31 July 2026 (Phase D); products confirmed as SBBs are selected in Phases E–F |
| Owner | Owen Price; standards agreed with the platform team and recorded in the Technology Standards catalog |

## Service → mechanism → component

| Service | Mechanism (Physical) | Component, product or standard (Component) | Where | Status |
|---|---|---|---|---|
| SS-01 Customer authentication | Strong customer authentication: possession (bound device) + knowledge or inherence; risk-based step-up driven by the fraud score | OAuth 2.1 with the gateway's authorisation server; device binding via platform attestation on iOS and Android; step-up by push confirmation | Mobile App, Channel API layer | Gateway product selected (SBB-01); attestation in Mobile App v4 build |
| SS-01 at the counter | Teller-assisted identity check plus one-time code to the customer's registered phone | Counter application; SMS provider; SMS gateway retired for payments at Transition 1 | Branch | Existing, re-pointed at the Onboarding API |
| SS-02 Staff and service authentication | Federated single sign-on for people; mutual TLS with short-lived service certificates for services | Bank identity provider (existing); TLS 1.3 with mutual authentication; certificate issuance from the platform's internal CA | Platform, IF-01/02/03 | Existing IdP; CA in SBB-06 Platform services |
| SS-03 Authorisation | Scope-based access tokens for channels; role-based access in consoles; rule ownership enforced by separate "edit rule" and "block card" roles | Gateway policy engine; console roles in the Fraud Engine and Identity Verification products | API layer, consoles | Console roles to be verified against the vendor at contract |
| SS-04 Confidentiality | Encryption in transit, encryption at rest, tokenisation of card numbers outside the Card Switch, in-country hosting | TLS 1.3 everywhere; AES-256 volume and database encryption; card tokenisation in the Switch's token service; vendor hosting clause CN-05 | All domains | Tokenisation exists in the Switch; vendor clause in RFP |
| SS-05 Integrity | Idempotency keys on money movement; message authentication on the card link | Idempotent POST with client-generated keys on IF-01 (Core Banking v12 API, confirmed 12 May 2026); ISO 8583 MAC per the network standard | IF-01, card link | Existing |
| SS-06 Non-repudiation | Signed payment instructions bound to the authenticated session and device; immutable log | Signature over the instruction with a device-held key; write-once log storage with hash chaining | Mobile App, log platform | New in WP-3 |
| SS-07 Audit and logging | Structured, attributed, tamper-evident event logging from every application to one store | Platform logging pipeline; write-once object storage with 13-month retention; log schema in the Technology Standards catalog | SBB-06 Platform services | New in WP-1 |
| SS-08 Availability | Active-active across two data centres; dual-homed card link; timeout policy | Container platform on RHEL 9.3 in both centres; WP-5 network dual-homing; authorise-and-flag on 150 ms timeout in the Switch | Both data centres | WP-1, WP-5 |
| SS-09 Fraud detection | Real-time scoring before authorisation; feature computation from an event stream; analyst review; rule administration without release | Fraud Engine product (SBB-03) on the platform; Kafka 3.7 card-event feed; vendor console; thresholds as configuration | D5 Fraud analytics | Product selected 14 April 2027 |
| SS-10 Identity proofing | Document capture, liveness detection, sanctions check; evidence purge | Identity Verification service (SBB-02), in-country; purge job at 30 days; IF-03 callback | D6 | Procurement in Phase F |
| SS-11 Key and secret management | Hardware-backed key storage; centrally issued, rotated, audited secrets | HSM cluster (existing, shared with the Card Switch) for signing and tokenisation keys; secrets manager in SBB-06 for application credentials; annual rotation | Both data centres | HSM existing; secrets manager new in WP-1 |
| SS-12 Security monitoring | Central correlation of security events with defined detection rules; alerting to an on-call rota | SIEM fed from the logging pipeline and the gateway; detection rules for takeover patterns, velocity, vendor access; 15-minute alert | Platform team | New in WP-1; rules grow with WP-4 |

## Physical × Location and the standards

Mechanisms sit where the domain model put policy enforcement: the Channel API layer for everything a customer does, the Card Switch for tokenisation and message authentication, the verification service for evidence, the HSM in both data centres for keys. The Component × Process cell is the standards list the Technology Standards catalog now carries as *adopted*: TLS 1.3, OAuth 2.1, OpenAPI 3 (so security scopes are declared with the contract), ISO 8583 as mandated by the network, AES-256, the bank's log schema.

## The ABB → SBB parallel, stated

Each row's *service* is the security reading of an Architecture Building Block: SS-01 is the security content of ABB-01 Channel API Layer and ABB-04 Mobile Banking Application; SS-09 is ABB-03 Fraud Screening Service. Each row's *component* is the matching Solution Building Block: SBB-01 the gateway product, SBB-03 the fraud product, SBB-02 the verification vendor, SBB-06 the platform with its secrets manager and logging. The mechanism column is the bridge TOGAF leaves implicit — the technology-neutral specification an SBB is selected against — and it is the column the Requirements Specification's implementation standards (§7) and the Compliance Assessment's security checklist both check. The Compliance Assessment's condition C-1 (vendor support access path) was a finding against SS-02's mechanism, not its product.

## In the other frameworks

TOGAF Phases C and D carry this as the *Technology Standards catalog* and the technology chapter of the *Architecture Definition Document*, with the ABB/SBB catalogues (documents 17 and 24); ArchiMate draws it in a *Layered view* — Application Service realised by Application Component realised on Node, System Software and Device — or the *Technology view* for the HSM, CA and SIEM nodes.

*Source note: SABSA framework as published by the SABSA Institute (open-use with attribution); section numbers refer to the SABSA White Paper and are to be verified against the registered PDF.*
