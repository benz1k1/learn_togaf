---
title: Solution Building Blocks — what was actually deployed
deliverable: Solution Building Blocks
phase: G
kind: DELIVERABLE
summary: The products and components that realise each Architecture Building Block after Transition 1, as recorded in the Solutions Landscape, with the ABB each one implements.
refs: ["CONTENT §4.2.19", "CONTENT §5", "ADM §11.4"]
source: authored
status: draft
---

> **What to notice.** Solution Building Blocks are *implementation-specific*: products, versions, hosting, owners. The Content Framework table lists them as an output of Phase G (and an input to A–G), even though Phase E identifies candidates and procurement selects them, because they exist as deployed things only once Phase G has delivered them. Each entry points back at the Architecture Building Block it realises; that trace is what lets Phase H judge whether the architecture, not just the project, was delivered.

| | |
|---|---|
| Location | Architecture Repository › Solutions Landscape › Digital Channels |
| As at | 30 June 2027 (Transition 1 declared); entries for Transition 2 marked *planned* |

| SBB | Realises | Product / component | Version, hosting | Owner | State |
|---|---|---|---|---|---|
| SBB-01 API gateway | ABB-01 Channel API Layer | The selected API management product, configured; Payments, Card Management and Notification APIs; Onboarding API stub | v4.2, containers on Platform Services, both data centres | Digital Platform team | Deployed, Transition 1 |
| SBB-06 Platform services | ABB-06 | Container platform on RHEL 9.3; secrets manager; monitoring stack; deployment pipeline | Both data centres; dev/test/pre-prod/prod | Digital Platform team | Deployed, Transition 1 |
| SBB-04 Mobile App v4 | ABB-04 Mobile Banking Application | Native iOS 4.0 / Android 4.0 with transfers and card controls; onboarding journey hidden until Transition 2 | App stores, 12 May 2027 | Digital Channels product owner | Deployed, Transition 1 |
| SBB-07 Core Banking v12 | ABB-07 Core Banking Services | Vendor package; REST API consumed on IF-01 only | Primary and DR | Retail IT | Unchanged |
| SBB-05 Card Switch | ABB-05 Card Authorisation | Vendor package; dual-homed network link (P3); scoring call not yet enabled | Both data centres | Cards Operations / vendor | Changed (P3); scoring change planned Nov 2027 |
| SBB-08 Network dual-homing and pre-prod | RC-D2, RC-D3 | Card network link terminated in both data centres; pre-prod environment | — | Network team | Deployed, Feb 2027; DR test passed 2 h level |
| SBB-02 Identity Verification | ABB-02 | Selected vendor service, in-country hosted; evidence purge at 30 days | Vendor cloud, private link from both centres | Compliance (procedure), Retail IT (integration) | Planned, Transition 2 (Sep–Nov 2027) |
| SBB-03 Fraud Engine | ABB-03 Fraud Screening Service | Selected product on Platform Services; Kafka feed; analyst console; retraining store per CR-2027-03 | Bank-hosted containers, both centres | Cards Operations (rules), Digital Platform team (run) | Planned, Transition 2 (Nov 2027) |
| Retired: SMS gateway | replaced by SBB-01 Notification API | — | Switched off 20 June 2027 after one quarter parallel run | — | Retired |

## Deviations from the Architecture Building Blocks

| ABB | Deviation | Handling |
|---|---|---|
| ABB-01 | The gateway product's own developer portal was adopted instead of publishing OpenAPI files to the repository | Accepted; the repository's Interface catalog links to the portal (Change Request CR-2027-01, simplification) |
| ABB-03 | Retraining store added | CR-2027-03, incremental |
| ABB-04 | The app vendor's package was not used; built in-house as planned; its cache expires in 15 minutes | As designed |

## Re-use register

SBB-01 and SBB-02 are marked *re-usable* for the Lending cycle; SBB-06 is the bank's standard platform for anything new (Technology Standards catalog updated at Phase H).
