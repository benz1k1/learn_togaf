---
title: "The Service Management layer: operations, incident and change, assurance and audit"
unit: S6
objectives: ["S6.2"]
refs: ["SABSA §3.6", "SABSA §4", "GUIDE:integrating-risk-and-security §3.2.4", "GUIDE:integrating-risk-and-security §5.8.1"]
reading_minutes: 9
source: authored
status: draft
---
## A layer that runs across the others

The sixth row of the SABSA Matrix is the **Service Management** layer (the older name is the *Operational* layer) — the *facilities manager's* view. It is drawn differently from the five design layers: rather than sitting beneath the Component layer as a further level of detail, it runs *across* all of them, because operating, monitoring and auditing are needed at every level of abstraction. It is the layer in which the SABSA Lifecycle's Manage and Measure phase is carried out (SABSA §3.6, §4).

**Trap:** the Service Management layer is not "the bottom of the stack". It is orthogonal to the design layers. A question that asks which layer "cuts across" the others wants Service Management; one that asks which is the "lowest design layer" wants Component (SABSA §3.6).

## The six cells

| Column | Blue Book cell name | Later wording | What actually goes in it |
|---|---|---|---|
| Assets (What) | Assurance of operational continuity | Service delivery management: assurance of operational continuity and excellence | Keeping the security services running at the agreed level; continuity and recovery |
| Motivation (Why) | Operational risk management | Operational risk management: risk assessment, monitoring, reporting and treatment | Running the risk process continuously, not once |
| Process (How) | Security service management and support | Process delivery management: management and support of systems, applications and services | Operating the mechanisms; incident, problem and change handling |
| People (Who) | Application and user management and support | Personnel management: account provisioning, user support | Joiners, movers, leavers; access requests; help desk |
| Location (Where) | Security of sites, networks and platforms | Management of environment: buildings, sites, platforms and networks | Physical and network operations, environment monitoring |
| Time (When) | Security operations schedule | Time and performance management: calendar and timetable | When operational tasks run; performance against time targets |

(SABSA §3.6; the two-vocabulary split is the author's reading and should be checked against the registered PDF.)

## The four operational themes

The unit objective names four things the layer must cover. They are not the six cells; they are themes that draw on several cells each.

**Operations.** The day-to-day running of the security services: monitoring, key and certificate management, patching, backup, capacity. Operations is where the Component layer's products are actually driven and where the Physical layer's schedules are actually kept (SABSA §3.6).

**Incident and change.** Two processes that keep the architecture true to its design under pressure. *Incident management* detects, contains and recovers from events that threaten an attribute, and feeds what it learns into operational risk management. *Change management* ensures that a change to a component, mechanism or service is assessed for its effect on the attributes before it is made, so that the traceability chain is not silently broken by a Tuesday-night change. The TOGAF risk and security guide lists the same operational security processes — and expects them to exist before the architecture is called complete (SABSA §3.6; GUIDE:integrating-risk-and-security §3.2.4).

**Assurance.** The collection of evidence that the controls are in place, work, and continue to meet their performance targets. Assurance is what turns Manage and Measure from "we run it" into "we can show it". Unit S7 treats the assurance framework in full (SABSA §3.6, §6).

**Audit.** The independent check. Where assurance is the operator's own evidence, audit is the review of that evidence by someone outside the operating team — internal audit, an external assessor, a regulator. The TOGAF guide's Phase G *security audit* — reviews of processes, designs, code and configuration, and security testing — is the same activity at implementation time (SABSA §3.6; GUIDE:integrating-risk-and-security §5.8.1).

**Trap:** assurance and audit are not synonyms. Assurance is *producing* the evidence and is owned by the people who run the controls; audit is *independently examining* it. An answer that has the operations team "auditing" its own controls has the roles crossed (SABSA §3.6, §6).

## Measurement: the layer's reason for existing

Every business attribute in the profile carries a metric type, a measurement approach and a performance target. The Service Management layer is where those measurements are *taken*. If the attribute *Available* has the target "core banking journeys reachable 99.9 % of the month", the Time and Assets cells of this layer are where uptime is monitored, reported and compared. A profile whose attributes have targets that nothing in the Service Management layer measures is incomplete — the bottom-up check of unit S7 would catch it (SABSA §3.6, §5).

| Attribute (Conceptual) | Measured by (Service Management) | Cell |
|---|---|---|
| Available | Uptime monitoring against the availability target | Assets, Time |
| Auditable | Log review and retention checks | Process, Assets |
| Access-controlled | Recertification results; orphan-account counts | People |
| Recoverable | Restore-test results against the recovery-time target | Assets |

(SABSA §3.6, §5.)

## Relation to TOGAF governance

TOGAF's architecture governance covers the same ground with different labels: compliance reviews (assurance), the Governance Log (evidence), the Architecture Board (the body that hears the audit) and Phase H's change management (change). The next lesson sets the two side by side; for now the point is that the Service Management layer is SABSA's governance and operations in one row (SABSA §3.6; GUIDE:integrating-risk-and-security §5.8, §5.9).

## Check yourself

- Why is the Service Management layer drawn across the Matrix rather than under it?
- Distinguish assurance from audit, and incident management from change management.
- Where are the Business Attributes Profile's metrics actually measured?

*Source note: written from the SABSA framework as published by the SABSA Institute; section numbers refer to the SABSA White Paper and are to be verified against the registered PDF.*
