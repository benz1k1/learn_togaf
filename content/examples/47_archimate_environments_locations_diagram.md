---
title: "Environments and Locations Diagram as an ArchiMate Physical view — Digital Channels"
deliverable: Environments and Locations Diagram as an ArchiMate view
phase: D
kind: MODEL
track: ARCHIMATE
summary: "Northgate's three sites as Locations, each with the Facility and Equipment that house the Nodes of its environments — production, standby, pre-production, development and test."
refs: ["ARCHIMATE §C.1", "CONTENT §3.6.7"]
figure: ENVIRONMENTS_LOCATIONS_DIAGRAM.svg
viewpoint: Physical
artefacts: [ENVIRONMENTS_LOCATIONS_DIAGRAM]
source: authored
status: draft
---

> **What to notice.** The pink frames are not decoration — they are **Location** elements, and everything drawn inside one is aggregated by it (ARCHIMATE §4.5.2). That is how the Physical viewpoint (ARCHIMATE §C.1) answers the TOGAF question "which locations host which environments" (CONTENT §3.6.7): a location aggregates a facility, the facility aggregates the nodes deployed in it, and an environment is simply the name on the node. No new element type is needed for "environment"; it is a property of where a node runs.

## How to read the view

Three locations. **Head Office — primary data centre** holds the **Primary DC hall**, a Facility whose name lists the physical estate (six R760 servers, the SAN, the WAN and internet ingress) and which aggregates four production or pre-production **Nodes** and one piece of **Equipment**, the card-network link termination. **Operations Centre — DR data centre** mirrors it with the standby nodes and the *second* link termination — the dual-homing Phase D added so that authorisation and scoring can fail over within the two-hour level of RQ-08. **Cloud region eu-west** has no facility of Northgate's own, so it aggregates a container-platform node directly, which in turn aggregates the development and test nodes.

Read the node names for the environment: `production`, `production standby`, `pre-production`, `dev / test`. The TOGAF drawing showed the same split with solid and dashed boxes.

## Elements

| Element | ArchiMate type | Aspect / layer | Why that type |
|---|---|---|---|
| Head Office, Operations Centre, Cloud region eu-west | Location | composite | A place; aggregates whatever is deployed there |
| Primary DC hall, DR hall | Facility | active, Physical | A physical structure that houses equipment and nodes |
| Card network link termination A / B | Equipment | active, Physical | A physical machine with no software role of its own on this view |
| Core Banking production, Card Switch production, Mobile backend, Pre-production, standbys, Container platform, dev/test nodes | Node | active, Technology | Computational resources that host the environments |

## Relationships used

| Relationship | Notation | What it says here |
|---|---|---|
| Aggregation (facility → node, facility → equipment, node → node) | hollow diamond at the whole | Housed in; the part can be moved to another whole |
| Aggregation by nesting (location → contents) | drawn as containment | Everything inside the frame is at that site |

Assignment is permitted by the mapping and would appear if system software or artifacts were deployed on the nodes; those belong to the Platform Decomposition and Networked Computing views. Distribution Network is also listed but is not used: nothing physical flows between Northgate's sites, only data, which is a Communication Network on the hardware view.

## What changed from the TOGAF drawing

The TOGAF drawing has two halves: on the left, where the *users* are (Head Office, 42 branches, customers on the internet) and what they use; on the right, which locations host which environments. The Physical viewpoint has no business actors, so the left half is dropped and recorded in the note; the user-to-location mapping belongs on an Organization view. The right half is reproduced site for site. The link terminations are new: the TOGAF drawing said "ISO 8583 link into Primary and DR" as a caption, and here it is two pieces of Equipment, one per site, which is what makes the dual-homing a checkable fact rather than a sentence.

## Draw it yourself

1. Create a *Physical* view; add three Location elements and size them as frames.
2. Inside each, add a Facility (where there is one) and the Nodes; nesting a node inside a location makes Archi create the aggregation.
3. Draw Aggregation from each facility to the nodes and equipment it houses.
4. Name each node `<system> — <environment>` so the environment is visible without a legend.
5. Add the two Equipment elements for the card-network link and check that both sites have one — that is the RQ-08 evidence.
