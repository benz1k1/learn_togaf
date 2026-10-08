---
title: "Technology active structure: node, device, system software, collaboration, interface, path, network"
unit: A6
objectives: ["A6.1"]
refs: ["ARCHIMATE §10", "ARCHIMATE §10.1", "ARCHIMATE §10.2", "ARCHIMATE §10.2.1", "ARCHIMATE §10.2.2", "ARCHIMATE §10.2.3", "ARCHIMATE §10.2.4", "ARCHIMATE §10.2.5", "ARCHIMATE §10.2.6", "ARCHIMATE §10.2.7", "ARCHIMATE §10.9"]
reading_minutes: 10
source: authored
status: draft
---
## The Technology Layer

Technology Layer elements model the Technology Architecture: the structure and behaviour of the
enterprise's infrastructure. The layer is drawn in green, and its metamodel again borrows the
three-aspect pattern of the layers above it, then adds several elements of its own because
infrastructure has hardware, software environments and networks to describe (ARCHIMATE §10,
ARCHIMATE §10.1). The physical elements are an extension of this layer for the non-IT world and
are covered in a later lesson (ARCHIMATE §10).

<figure class="max-w-lg"><img src="/figure/ARCHIMATE:fig-82" alt="Technology Layer metamodel" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 82. Technology Layer Metamodel (ARCHIMATE)</figcaption></figure>

## The active-structure family

The main active-structure element is the node. It models structural entities only; behaviour is
attached by an explicit relationship. A technology interface is where a node's services can be
reached by other nodes or by application components. A node can consist of devices and system
software — the usual pattern being a server device plus an operating system — and, since the
physical extension, of facilities and equipment too (ARCHIMATE §10.2). The layer's
interconnections are the communication infrastructure: a path is the logical relation through
which nodes exchange information, and a communication network is its physical realization
(ARCHIMATE §10.2).

<figure class="max-w-lg"><img src="/figure/ARCHIMATE:fig-83" alt="Technology active structure elements" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 83. Technology Active Structure Elements (ARCHIMATE)</figcaption></figure>

| Element | Aspect | Notation | Definition in plain words | Typical confusion |
|---|---|---|---|---|
| Node | Active structure (internal) | Green 3-D box | A computational or physical resource that hosts, manipulates or interacts with other resources | Using node where the question wants the hardware specifically (device) |
| Device | Active structure (internal) | Green box, monitor icon | A physical IT resource on which system software and artifacts can be stored or deployed | Calling virtualised hardware a node: the spec says device covers IaaS hardware too |
| System Software | Active structure (internal) | Green box, disc icon | Software that provides an environment for storing, executing and using other software or data | Modelling an application as system software; an application is an application component |
| Technology Collaboration | Active structure (internal) | Green box, overlapping circles | An aggregate of two or more technology internal active elements working together | Thinking it must exist as a real thing; it is usually logical or temporary |
| Technology Interface | Active structure (external) | Green box, lollipop icon | A point of access where a node's technology services can be reached | Confusing interface with service |
| Path | Active structure | Green box, dashed-line icon | A logical link between two or more nodes through which they exchange data, energy or material | Confusing it with the network that realizes it |
| Communication Network | Active structure | Green box, network icon | Physical structures that connect devices or system software for transmitting, routing and receiving data | Reversing the realization: network realizes path, not the reverse |

### Node

A node is a computational or physical resource that hosts, manipulates or interacts with other
such resources. Nodes perform technology behaviour and execute, store and process artifacts or
materials; the specification points at TOGAF's "application platform" as a typical thing to
model as a node (ARCHIMATE §10.2.1). Nodes are connected by paths, may be *assigned to* an
artifact to show deployment, may consist of sub-nodes, and take a noun as name. An artifact
deployed on a node is drawn either nested inside it or connected by an assignment
(ARCHIMATE §10.2.1).

### Device

A device is a physical IT resource with processing capability: a mainframe, a PC, a smartphone,
a router. It also covers virtualised hardware in an IaaS environment. Devices are usually part of
a node together with system software, may be composite, may be connected by communication
networks, and may be assigned to artifacts and to system software to show deployment on the
device. Name it by hardware type (ARCHIMATE §10.2.2).

### System software

System software is the environment in which artifacts run: an operating system, a JEE server, a
database system, a workflow engine or communication middleware. Combined with a device it makes
a general node (ARCHIMATE §10.2.3). A device or system software may be *assigned to* other system
software to model layered software; system software may be assigned to artifacts (deployment) and
may *realize* other system software; a node may compose or aggregate it; and system software may
be composed of other system software, such as an operating system containing a database
(ARCHIMATE §10.2.3).

**Trap — node vs device vs system software:** node is the generic resource and the container;
device is the hardware; system software is the execution environment. "Which element models a
JEE application server?" is system software; "a blade server" is device; "the platform as a
whole" is node. The three are distinct elements, and device and system software are what a node
typically *consists of* (ARCHIMATE §10.2).

### Technology collaboration and interface

A technology collaboration aggregates two or more technology internal active elements that
cooperate on a task; their collective behaviour, with its communication pattern, is a technology
interaction. It is usually a logical or temporary grouping, may be assigned to interactions, may be
served by and composed of interfaces (ARCHIMATE §10.2.4). A technology interface specifies how a
node's services can be reached, exposes a service to the environment, and acts as a contract the
node must honour — parameters, protocols, data formats. It may be part of a node by composition,
may serve other elements, and is assigned to the service it exposes (ARCHIMATE §10.2.5).

### Path and communication network

A path is the *logical* communication (or distribution) relation between technology internal
active elements, through which they can exchange data, energy or material. It is realized by one
or more communication networks — or distribution networks in the physical extension — and its
properties, such as bandwidth and latency, are usually aggregated from those networks. A path
connects two or more nodes and may aggregate nodes (ARCHIMATE §10.2.6). A communication network is
the *physical* communication infrastructure: it connects two or more devices or system software,
may be a single link or many links with the associated equipment, has bandwidth and latency
properties, realizes one or more paths, may consist of sub-networks, and may aggregate the devices
and system software that make up routers, switches and firewalls (ARCHIMATE §10.2.7).

**Trap:** which realizes which? A communication network *realizes* a path. The path is logical,
the network is physical, and realization runs from the physical to the logical. An option that
has the path realizing the network is reversed (ARCHIMATE §10.2.6, ARCHIMATE §10.2.7).

## The example

Two "Blade System" devices connect to a "Data Center Network"; a "Data Center Switch" node
connects it to a "Wide Area Network"; the two networks together realize a "Data Replication
Path". Each device and the switch has a "Management Interface". One blade deploys a "Hypervisor"
(system software), on which two operating systems are deployed, creating two virtual hosts
modelled as nodes. Device–network connection, network–path realization, interface composition
and layered system software assignment are all shown (ARCHIMATE §10.2).

Table 8 holds the one-line definitions; for the active-structure rows the marker phrases are
"hosts, manipulates, or interacts" (node), "physical IT resource" (device), "environment for
storing, executing, and using" (system software), "link ... data, energy, or material" (path)
and "transmission, routing, and reception of data" (communication network) (ARCHIMATE §10.9).
