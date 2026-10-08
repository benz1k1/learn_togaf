---
title: "Trust relationships: one-way, two-way, transitive and inter-domain services"
unit: S4
objectives: ["S4.3"]
refs: ["SABSA §6.4", "SABSA §6.4.1", "SABSA §6.4.2", "SABSA §6.3", "GUIDE:integrating-risk-and-security §5.3.3", "GUIDE:integrating-risk-and-security §5.3.2"]
reading_minutes: 10
source: authored
status: draft
---
## Trust is a relationship between domains

In SABSA, **trust** is not a feeling and not a property of a system; it is a **relationship
between two domains** in which one domain's policy authority accepts assertions made under the
other domain's policy. The domain that accepts is the **trusting** party; the domain whose
assertions are accepted is the **trusted** party. The relationship is always explicit, always
has a direction, and always rests on something — a contract, a shared authority, a verified
credential, an audit — that gives the trusting authority grounds for its acceptance
(SABSA §6.4).

Within a single domain, trust is implicit: the elements are under one policy and one authority.
Between domains it must be established, and the **entity and trust framework** of the Logical ×
People cell records how. The TOGAF guide's Phase B trust framework is this record with the
ADM's name (GUIDE:integrating-risk-and-security §5.3.3).

## The kinds of trust relationship

| Relationship | Direction | Meaning | Example |
|---|---|---|---|
| **One-way (unilateral)** | A → B | A trusts B; B does not trust A | A merchant trusts the card scheme's authorisation response; the scheme does not trust the merchant's assertions |
| **Two-way (bilateral, mutual)** | A ↔ B | Each trusts the other, usually under one agreement | Two banks in a payment network authenticate each other's messages |
| **Transitive** | A → B, B → C, therefore A → C | A trusts C *because* B does — only if A's policy explicitly allows trust to pass through B | A partner's staff are accepted because the partner's identity provider vouches for them and the partner is trusted |
| **Non-transitive** | A → B, B → C, but not A → C | Trust stops at B | A supplier's access does not extend to the supplier's own subcontractors |
| **Direct** | A → B on A's own verification | A has checked B itself | A bank verifies a customer's identity documents |
| **Third-party (brokered)** | A → B via T | Both rely on a trusted third party | Two companies rely on a certificate authority or an identity federation hub |

(SABSA §6.4.1)

> **Trap.** Trust is **not transitive by default**. If A trusts B and B trusts C, A trusts C only
> when A's policy authority has decided that trust may pass through B. The paper's favourite
> distractor asserts that transitive trust follows automatically; it does not, and a well-run
> domain model states explicitly where transitivity is permitted.

> **Trap.** One-way trust is a *single* direction. "The merchant trusts the scheme" says nothing
> about the reverse, and a question that adds "and therefore the scheme trusts the merchant" has
> turned one-way into two-way without grounds. Two-way trust needs two decisions, one by each
> authority, even when they are written into one agreement.

## Trust between super- and sub-domains

Inside a multi-tiered structure trust has a natural shape. A super-domain's authority trusts its
sub-domains to the extent that their policies comply with its own, which they must; that trust
is inherent in the containment. A sub-domain trusts its super-domain's authority as the source of
its own policy. Between *peer* sub-domains, however, nothing is inherent: two business units under
the same bank do not trust each other's assertions unless the bank's policy says so or they agree
it between themselves. Peer trust is a designed relationship, like any other (SABSA §6.4).

## Inter-domain services

When two domains with **different policy authorities** need to interact — an independent
supplier and the enterprise, two peer business units, a customer and a bank — the interaction
crosses a boundary where neither policy governs both sides. SABSA handles this with an
**inter-domain service**: a service that operates at the boundary, applies the terms both
authorities have agreed, and translates or checks assertions as they cross. The agreement itself
is an **inter-domain policy** (or association), negotiated between the two authorities; the
service is what enforces it (SABSA §6.4.2).

| Situation | Inter-domain need |
|---|---|
| Supplier staff need access to the enterprise's systems | Federation service that accepts the supplier's authenticated identities under agreed terms, with the enterprise granting privileges |
| Two banks exchange payment messages | Mutual authentication and message-integrity service under the network's rules |
| Customer data is shared with a regulator | Secure transfer service under a data-sharing agreement, with classification preserved |
| Two peer business units share a reporting platform | An internal service agreement, with the platform's domain authority named |

The **trust broker** or **trusted third party** is a special case: an inter-domain service
provided by a domain that both parties already trust, so that they need not establish direct
trust with each other. A certificate authority, an identity federation hub or a clearing house is
a trust broker. Its existence does not make the relationship transitive by accident — each party
has explicitly chosen to trust the broker (SABSA §6.4.2).

> **Trap.** An inter-domain service is needed when the domains have **different policy
> authorities**. Between a super-domain and its sub-domain there is one chain of authority and
> the super-domain's policy already governs the boundary; no inter-domain service is required,
> though the sub-domain's stricter policy still applies on entry.

## Recording trust in the framework

The entity and trust framework lists, for each pair of domains that interact: the direction of
trust, its basis, whether it may be passed on (transitivity), the inter-domain service and
agreement that implement it, and the privileges an entity from the trusted domain receives in the
trusting one. This is a Logical-layer design deliverable; the Physical layer chooses the
mechanisms — certificates, federation protocols, VPNs, contracts — that realise each row
(SABSA §6.4.1).

## In TOGAF terms

The trust framework is a Phase B artefact in the TOGAF guide, drawn beside the security domain
model against the Business Architecture's organisation and actors; the inter-domain services
appear in Phase C's security services catalogue and their mechanisms in Phase D. In ArchiMate
the domains would be Groupings or Locations and the trust relationships would be drawn between
Business Roles and Interfaces; TOGAF itself has no trust concept, which is why cross-framework
questions on trust always resolve to SABSA (GUIDE:integrating-risk-and-security §5.3.2).

*Source note: written from the SABSA framework as published by the SABSA Institute; section numbers refer to the SABSA White Paper and are to be verified against the registered PDF.*
