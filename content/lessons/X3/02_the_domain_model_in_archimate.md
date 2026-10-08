---
title: "The SABSA domain model with Grouping, Location, Business Role and Interface"
unit: X3
objectives: ["X3.2"]
refs: ["ARCHIMATE §4.5", "ARCHIMATE §8.2", "ARCHIMATE §8.3", "ARCHIMATE §5.1", "ARCHIMATE §5.2", "ARCHIMATE §B.6", "WP:w172 §5", "SABSA §8", "GUIDE:integrating-risk-and-security §5.3.2", "GUIDE:integrating-risk-and-security §5.3.3"]
reading_minutes: 9
source: authored
status: draft
---
## What has to be drawn

A SABSA **security domain** is a set of elements under one **policy authority**, governed by one policy. Domains nest into **sub-domains**, stack into **multi-tiered** domains, and relate to one another through **trust relationships** — one-way, two-way, transitive — carried by **inter-domain services** that cross the boundary. The TOGAF risk and security guide asks Phase B for exactly these: a Security Domain Model and a Trust Framework. This lesson draws them in ArchiMate with four elements and four relationships, the way W172's second half suggests (SABSA §8; GUIDE:integrating-risk-and-security §5.3.2, §5.3.3; WP:w172 §5).

## The four elements

| SABSA concept | ArchiMate element | Why |
|---|---|---|
| Security domain (logical) | **Grouping** | A composite element that aggregates any elements that share a property — here, a policy |
| Security domain (physical or geographic) | **Location** | When the boundary is a place: a site, a data centre, a jurisdiction |
| Policy authority | **Business Role** (with the Business Actor assigned that holds it) | Authority is a responsibility, and responsibilities are roles |
| Inter-domain service and its access point | **Business Service** exposed through a **Business Interface** (or Application Service and Interface at that layer) | The service crosses the boundary; the interface is where the boundary is enforced |
| The policy itself | Principle or Requirement (or a Contract when it is agreed between domains) | Motivation, associated with the Grouping |

(ARCHIMATE §4.5, §8.2, §8.3; SABSA §8.)

**Trap:** Grouping is *not* a visual box for tidiness. In ArchiMate 3 it is a real composite element with real relationships: it *aggregates* (or composes) its members, and other relationships may be drawn to it. A domain drawn as a Group note in Archi (the visual-only object) carries no semantics and will not survive export. Use the Grouping *element* (ARCHIMATE §4.5, §B.6).

## The four relationships

| Meaning | Relationship | Between |
|---|---|---|
| This element is in this domain | **Aggregation** (or Composition when the element can be in no other) from Grouping to member | Grouping → Business Actor, Application Component, Node, Data Object… |
| This domain is a sub-domain of that | **Aggregation** from the outer Grouping to the inner | Grouping → Grouping (nesting draws it) |
| This role is the policy authority of this domain | **Association** Business Role – Grouping, with the Business Actor **assigned** to the Role | Role – Grouping; Actor → Role |
| Domain A trusts domain B for service S | **Serving** from B's Business Interface (exposing S) to A's Business Role, plus the Interface **composed** into B's domain | Interface → Role |

(ARCHIMATE §5.1, §5.2, §8.2; WP:w172 §5.)

## Trust, drawn

Trust in SABSA is *directional*. The direction is the direction of Serving:

- **One-way trust**: Domain *Branch* relies on Domain *Identity Verification*'s service. One Serving arrow from the Identity Verification Interface to the Branch Teller role. Nothing comes back (SABSA §8).
- **Two-way trust**: each domain exposes an Interface and each Serving arrow points the other way as well — two arrows, two interfaces, and usually two policy documents (SABSA §8).
- **Transitive trust**: *Mobile App* trusts *API Layer*, which trusts *Fraud Engine*. Two Serving arrows in a chain. ArchiMate's derivation rules let a reader *derive* a Serving from Fraud Engine to Mobile App — which is precisely the transitive trust SABSA warns must be a deliberate decision, not an accident. If the derived relationship is *not* wanted, the model must show a boundary control at the API Layer interface that breaks the chain (ARCHIMATE §5.7, §B.2; SABSA §8).

**Trap:** "the domains share a network" is not trust. Trust is a relationship between *policy authorities* about a *service*. If two Groupings sit inside the same Location but no Serving crosses between them, they are co-located, not trusting; the model should say so (SABSA §8; ARCHIMATE §4.5).

## Multi-tiered domains

A multi-tiered domain is a policy that applies at several levels — the bank's group policy, a division's policy within it, a system's policy within that. Draw the tiers as nested Groupings, each with its own policy authority Role, and record the *inheritance* as a Specialization between the Requirement (or Principle) elements of the inner and outer policies. Anything in the inner Grouping is automatically in the outer one, which is what the aggregation says (ARCHIMATE §4.5, §5.4; SABSA §8).

## Northgate Bank's domain model, in words

Grouping *Customer Channel Domain* (policy authority: Head of Digital, a Business Actor assigned to the Role *Channel Policy Authority*) aggregates Mobile App v4 and the Payments and Onboarding Interfaces. Grouping *Core Processing Domain* (authority: Head of Operations) aggregates Core Banking, the API Layer and the Fraud Engine. Grouping *Third-Party Verification Domain* (authority: the Supplier's security officer, a role held by an external Actor) aggregates the Identity Verification Service and is inside Location *Supplier Cloud, EU region*. Trust: the Channel domain trusts Core Processing one-way (Serving from the API Layer Interface to the Mobile App's role); Core Processing trusts Third-Party Verification one-way (Serving from the Verification Interface to the API Layer). No direct arrow from Verification to Channel: the transitive path exists and the model shows the API Layer's token check as the control that makes it acceptable. Each Grouping has a Requirement element for its policy associated to it, and the two inter-domain Interfaces have Contracts — the SABSA inter-domain policy — attached (WP:w172 §5; SABSA §8; GUIDE:integrating-risk-and-security §5.3.3).

## Viewpoint and tool

Use the **Organization** viewpoint for the domains and authorities (Groupings, Locations, Actors, Roles) and the **Business Process Cooperation** or **Application Cooperation** viewpoint for the inter-domain services and interfaces; or define a custom *Security Domain* viewpoint with the viewpoint mechanism that admits exactly Grouping, Location, Role, Actor, Interface, Service, Requirement and Contract — which is the SABSA cell "Logical × Location" restated as an ArchiMate viewpoint. In Archi, nest the elements inside the Grouping on the diagram and it creates the aggregation for you; check the model tree afterwards to confirm the relationship exists (ARCHIMATE §13.4, §C.1; SABSA §3).

## Check yourself

- When is a domain a Grouping and when a Location?
- Which relationship and direction expresses "A trusts B for service S"?
- Why is transitive trust visible in an ArchiMate model even when nobody drew it?
