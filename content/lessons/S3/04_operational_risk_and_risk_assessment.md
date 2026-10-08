---
title: "Operational risk management and the SABSA risk assessment"
unit: S3
objectives: ["S3.4"]
refs: ["SABSA §4", "SABSA §4.3", "SABSA §4.4", "SABSA §2.2", "SABSA §5.1", "GUIDE:integrating-risk-and-security §3.1.2", "GUIDE:integrating-risk-and-security §5.1.4", "GUIDE:integrating-risk-and-security §5.3.4"]
reading_minutes: 9
source: authored
status: draft
---
## Operational risk

**Operational risk** is the risk of loss — or of missed gain — arising from inadequate or failed
internal processes, people and systems, or from external events. The definition is the one the
banking regulators adopted, and SABSA adopts it because it places information security where the
business already accounts for it: as one category of operational risk beside fraud, process
failure, staff error, supplier failure and physical events. Security is not a separate risk
universe with its own vocabulary; it is a contributor to the operational risk the board already
tracks (SABSA §4.3).

In the Matrix, operational risk management is the **Service Management × Motivation** cell: the
continuous assessment, monitoring, reporting and treatment of risk while the services run. It is
the bottom of the Motivation column, and the point at which the objectives, policies, practices
and tools above it are exercised against real events (SABSA §2.2).

## The operational risk management framework

SABSA's framework for managing operational risk is a loop, run at the Service Management layer
and fed back to the Conceptual layer (SABSA §4.3):

| Stage | What is done | Feeds |
|---|---|---|
| **Identify** | Enumerate the assets, the attributes they need and the events (threats and opportunities) that could affect them | The risk register |
| **Assess** | Estimate impact and likelihood; rate each risk against the attribute targets and the appetite | Prioritised risks |
| **Treat** | Choose avoid, transfer, mitigate, accept or exploit; select control types; design or adjust services | The architecture |
| **Monitor** | Measure attribute performance; detect events; track key risk indicators | Metrics |
| **Report** | Present measured performance against target to the business and the risk function | Governance, appetite review |

The loop is the Manage and Measure phase of the Lifecycle. Its reports are what the Strategy and
Planning phase re-reads when the profile is re-baselined, which is how the framework keeps the
architecture aligned with what the business actually experienced rather than with what it
expected (SABSA §5.1).

## The SABSA risk assessment

The **risk assessment** is the Assess stage made explicit. It is business-attribute-centred:
instead of asking "what could attack this server?", it asks "which attributes does this asset
need, what could stop each attribute being true, how bad would that be for the business, and how
likely is it?" The steps are (SABSA §4.4):

1. **Asset and attribute.** Identify the asset and the attributes from the profile that apply to it.
2. **Threat or opportunity.** For each attribute, identify the events that would degrade it (threats) or improve it (opportunities).
3. **Vulnerability.** Identify the weaknesses that would let a threat succeed, or the enablers that would let an opportunity be taken.
4. **Impact.** Estimate the business consequence, in the business's terms, if the attribute fails — or the gain if the opportunity is realised — using the attribute's metric.
5. **Likelihood.** Estimate how probable the event is, given the current controls.
6. **Risk rating.** Combine impact and likelihood, typically on a matrix, into a priority.
7. **Compare with appetite.** Anything above the attribute's target or the stated appetite needs treatment.

> **Trap.** Impact is assessed against the **business attribute**, in business units, not
> against the asset's technical value. "Impact of losing confidentiality of the customer file"
> is measured as regulatory fine, lost customers and reputational damage, because those are the
> drivers the attribute traces to. A distractor that measures impact as "number of records" or
> "replacement cost of the server" has left the business out.

> **Trap.** SABSA's assessment covers opportunity as well as threat: an assessment that rates
> only losses is incomplete in SABSA's terms, however thorough it is as a threat assessment.

## Key risk indicators and assurance

Because each attribute has a metric, the measured value doubles as a **key risk indicator**: a
falling availability figure or a rising count of failed authentications is the operational-risk
early warning for the attribute concerned. Reporting those indicators against target closes the
loop between the risk assessment (what we expected) and operations (what happened). The
**assurance** activity — audit, testing, independent review — checks that the indicators are
honest and that the controls exist and work as designed (SABSA §4.3).

## Relationship to the TOGAF guide

The TOGAF guide's enterprise risk management section names the same core concepts — asset,
threat, vulnerability, impact, likelihood, appetite, treatment — and its Phase B risk assessment
produces the business risk model or risk register with a security classification for each asset.
Its Preliminary Phase key-risk-areas and business impact analysis are the first pass of the
Identify and Assess stages. Where SABSA adds something is the attribute-centred impact and the
opportunity side (GUIDE:integrating-risk-and-security §3.1.2).

## In TOGAF terms

Operational risk management is the Service Management layer and therefore Phases G and H: the
security audit and monitoring of Phase G, the change management of Phase H, and the metrics that
re-enter the cycle as change requests. The risk assessment itself is done in Phase B according to
the TOGAF guide, on the assets identified in Phases A and B, and its register is maintained by
Requirements Management. The TOGAF risk technique's initial and residual risk are this
assessment's ratings before and after treatment (GUIDE:integrating-risk-and-security §5.3.4).

*Source note: written from the SABSA framework as published by the SABSA Institute; section numbers refer to the SABSA White Paper and are to be verified against the registered PDF.*
