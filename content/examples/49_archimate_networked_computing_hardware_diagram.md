---
title: "Networked Computing/Hardware Diagram as an ArchiMate Technology view — Digital Channels"
deliverable: Networked Computing/Hardware Diagram as an ArchiMate view
phase: D
kind: MODEL
track: ARCHIMATE
summary: "The as-deployed baseline: Devices and Nodes in DMZ, application and data tiers, the Internet, MPLS WAN and branch LAN as Communication Networks, and the card-network link and DR replication as Paths."
refs: ["ARCHIMATE §C.1", "CONTENT §3.6.7"]
figure: NETWORKED_COMPUTING_HARDWARE_DIAGRAM.svg
viewpoint: Technology
artefacts: [NETWORKED_COMPUTING_HARDWARE_DIAGRAM]
source: authored
status: draft
---

> **What to notice.** Two kinds of green box with the same shape: **Device** (a monitor icon) for hardware that is what it is — a phone, a workstation, a firewall — and **Node** (a cube) for a computational resource identified by what runs on it — `app-01, app-02: Core Banking`. And two kinds of line element: a **Communication Network** is a physical medium (the Internet, the MPLS WAN), a **Path** is a logical link between nodes that may cross several networks (ARCHIMATE §10.2). The single-homed ISO 8583 path is drawn as a Path precisely so its single-ness is an element with a name, not a caption.

## How to read the view

Top: the edges. A **Customer phone** reaches the **Internet**; a **Teller workstation** (×420) sits on a **Branch LAN** that joins the **MPLS WAN**. Both networks terminate at the **Firewall pair** in the **DMZ** grouping, behind which the **Load balancer pair** and the **API gateway** front the **Application tier**. The application nodes are named by host and by the application deployed on them; `kafka-01..03` is beside the Card Switch node because Kafka carries its card events. The **Data tier** holds `db-01 primary`, `db-02 replica` and the SAN.

Two Paths. On the right, the **ISO 8583 link** from the external card-network endpoint lands on `app-03, app-04` — the Card Switch — and its name records the Phase D finding: single-homed, which is what fails RQ-08's two-hour failover. At the bottom, **Async replication to DR** carries `db-01` to the DR data centre node.

## Elements

| Element | ArchiMate type | Aspect / layer | Why that type |
|---|---|---|---|
| Customer phone, Teller workstation, Firewall pair, Load balancer pair | Device | active, Technology | Physical hardware with fixed function |
| API gateway, app-01/02, app-05, app-03/04, kafka, db-01, db-02, SAN, DR data centre, Card network endpoint | Node | active, Technology | Computational resources named by what they host |
| Internet, MPLS WAN, Branch LAN | Communication Network | active, Technology | Physical communication media |
| ISO 8583 link, Async replication to DR | Path | active, Technology | Logical links whose existence and redundancy are architecture facts |
| DMZ, Application tier, Data tier | Grouping | composite | The network zones of the TOGAF drawing |

## Relationships used

| Relationship | Notation | What it says here |
|---|---|---|
| Association | plain line | "Is connected to" — the only relationship a communication network needs on a logical hardware view |

Composition is permitted and would tie each tier to the nodes in it; the view uses Groupings for the tiers instead, because a tier is a zone, not a node that contains other nodes.

## What changed from the TOGAF drawing

The TOGAF drawing is a zoned box diagram with plain lines; the ArchiMate view keeps the three zones (as Groupings) and the same hosts, and types every box. The most useful change is the two Paths: in the TOGAF drawing "→ DR DC async replication" and the card-network line were arrows with captions; here each is an element that can carry properties, appear on the Environments and Locations view and be the target of a Gap. The teller LAN and MPLS WAN, which the TOGAF drawing showed as one arrow, are two networks because they have different owners.

## Draw it yourself

1. Create a *Technology* view and add three Groupings for the zones.
2. Add Devices for hardware with a fixed role and Nodes for hosts, naming nodes `host: application`.
3. Add Communication Networks for the Internet, WAN and LAN, and draw Associations along the physical chain: phone → Internet → firewall → load balancer → gateway → application nodes → database nodes.
4. Add the two Paths and associate each with the nodes at its ends; put the finding (single-homed) in the path's name or a property.
5. For the target view, copy this one and add the second ISO 8583 path into the DR data centre — the diff between the two views is the RQ-08 gap.
