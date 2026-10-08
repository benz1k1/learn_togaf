---
title: "Physical elements: equipment, facility, distribution network, material"
unit: A6
objectives: ["A6.4"]
refs: ["ARCHIMATE §10", "ARCHIMATE §10.5", "ARCHIMATE §10.6", "ARCHIMATE §10.6.1", "ARCHIMATE §10.6.2", "ARCHIMATE §10.6.3", "ARCHIMATE §10.7", "ARCHIMATE §10.7.1", "ARCHIMATE §10.2.6", "ARCHIMATE §10.9", "ARCHIMATE §C.1.6"]
reading_minutes: 8
source: authored
status: draft
---
## An extension, not a layer

The physical elements extend the Technology Layer so that the non-IT world — machines, buildings,
transport, raw materials — can be modelled. They comprise only active and passive structure
elements; no physical behaviour elements are defined, so physical behaviour is modelled with the
ordinary technology function, process, interaction, event and service. Physical elements may be
combined with IT elements such as devices inside the same node to model integrated operational
and information technology (ARCHIMATE §10). Figure 99 is the metamodel (ARCHIMATE §10.5).

<figure class="max-w-lg"><img src="/figure/ARCHIMATE:fig-99" alt="Physical elements metamodel" loading="lazy" class="rounded border border-base-300"><figcaption class="text-xs text-base-content/60 mt-1">Figure 99. Physical Elements Metamodel (ARCHIMATE)</figcaption></figure>

| Element | Aspect | Notation | Definition in plain words | Typical confusion |
|---|---|---|---|---|
| Equipment | Active structure (physical) | Green box, cog icon | One or more physical machines, tools or instruments that can create, use, store, move or transform material | Confusing it with a device: equipment processes material, a device processes artifacts |
| Facility | Active structure (physical) | Green box, factory icon | A physical structure or environment that houses equipment | Confusing it with location, which is a composite element, not a technology one |
| Distribution Network | Active structure (physical) | Green box, arrows icon | A physical network that transports material or energy | Confusing it with a communication network, which carries data |
| Material | Passive structure (physical) | Green box, material icon | Tangible physical matter or energy | Modelling raw material as an artifact |

## Equipment and facility

Equipment is the main physical active-structure element and models any machinery, tools or
instruments. Like node it is strictly structural; its behaviour is attached through behaviour
elements. A facility models the environment in which equipment is used — office buildings,
factories, laboratories, data centres (ARCHIMATE §10.6). Equipment comprises all the active
processing elements that carry out physical processes in which material is used or transformed.
Nodes may combine IT infrastructure with equipment — an MRI scanner, a production plant with its
control systems (ARCHIMATE §10.6.1).

Equipment's relationships: it may *access* material (create, use, move, transform); it may be
*assigned to* material to show where the material is stored; material may *realize* equipment;
equipment may *serve* other equipment and active structure such as business roles and actors; a
facility may be assigned to equipment (the equipment is installed in the facility); equipment may
be composed of equipment or devices; and equipment may be aggregated in a location. Name it with
a noun (ARCHIMATE §10.6.1).

A facility is a physical resource that can house or locate equipment: a factory, a warehouse, a
laboratory, a shopping mall — the specification also allows a cave or a spaceship. Facilities may
be composite. They may be interconnected by distribution networks, may serve other facilities and
active structure such as roles and actors, may be composed of facilities or nodes, and may be
aggregated in a location. Name it by facility type — "Rotterdam oil refinery" (ARCHIMATE §10.6.2).

**Trap — facility vs location:** location is a composite element from Chapter 4 that can
aggregate almost anything to say where it is; facility is a technology-layer active-structure
element that is itself a physical structure with capability. "The data centre building" as an
active thing that houses equipment is a facility; "Amsterdam" as a place is a location. Both
equipment and facility may be *aggregated in* a location (ARCHIMATE §10.6.1, ARCHIMATE §10.6.2).

## Distribution network and path

The inter-relationships of physical elements are mainly logistics. The path element from the
Technology Layer models the logical relation through which nodes exchange information or
material; its physical realization in the physical world is the distribution network — a
physical connection between pieces of equipment or facilities, such as a rail or road network,
the water supply, the power grid or a gas network (ARCHIMATE §10.6). A distribution network is a
physical network for transporting material or energy; it connects two or more facilities, may
realize one or more paths, may consist of sub-networks, and may aggregate facilities and
equipment — railway stations and trains as parts of a rail network (ARCHIMATE §10.6.3).

**Trap — distribution network vs communication network:** both realize paths and both are
physical. A communication network carries *data* between devices or system software; a
distribution network carries *material or energy* between facilities. The path's own definition
already allows "data, energy, or material", which is why one path element serves both worlds
(ARCHIMATE §10.6.3, ARCHIMATE §10.2.6).

## Material

Material is tangible physical matter or energy: raw materials, physical products, and energy
sources such as fuel and electricity. It is accessed by technology behaviour elements to show how
it is created, used, moved or transformed. Equipment may be assigned to material to show where
the material is stored — the specification's example distinguishes "the sand is in the dump truck"
(assignment) from "the sand is poured into the concrete mixer" (access). Material may realize
equipment, and pieces of material may be composed of other pieces. Name it with a noun
(ARCHIMATE §10.7, ARCHIMATE §10.7.1).

**Trap — material vs artifact:** both are technology passive structure elements, both are
accessed by technology behaviour, and both may have an active element assigned to them. The
difference is what they are: artifact is data (a file, a table), material is matter or energy.
A shipment of circuit boards is material; the firmware image flashed onto them is an artifact
(ARCHIMATE §10.7.1).

## The example

An "Assembly Line" (equipment) installed at a "Manufacturing Plant" (facility) uses three input
materials to produce a "Vehicle Telematics Appliance" (material). The appliance travels to a
national and then a local distribution centre (facilities) over "Overseas Shipping" and "Local
Trucking" (distribution networks), which together realize the path "Intermodal Freight". The
specification notes a real model would split this into production, material-flow and
transport-modality views (ARCHIMATE §10.6, ARCHIMATE §10.7).

## The physical viewpoint

The physical viewpoint holds equipment, how it is connected by distribution networks, and which
other active elements are assigned to it. Its stakeholders are infrastructure architects and
operational managers; its concern is the relationships and dependencies of the physical
environment and how it relates to IT infrastructure; its purpose is designing; its scope is
multiple layers, multiple aspects; and its elements are location, node, device, equipment,
facility, path, communication network, distribution network and material (ARCHIMATE §C.1.6).

Table 8 closes with the four physical definitions; "machines, tools, or instruments" (equipment),
"physical structure or environment" (facility), "transport materials or energy" (distribution
network) and "tangible physical matter or energy" (material) are the phrases to anchor on
(ARCHIMATE §10.9).
