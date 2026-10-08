---
title: Capability Assessment — business, IT, architecture and transformation readiness
deliverable: Capability Assessment
phase: A
kind: ASSESSMENT
summary: The four assessments the contents list asks for, with baseline and target levels per capability and the readiness factors that shaped the roadmap.
refs: ["CONTENT §4.2.10", "TECH §7", "ADM §3.3", "ADM §3.4"]
source: authored
status: draft
---

> **What to notice.** Four parts: Business Capability Assessment, IT Capability Assessment, Architecture maturity assessment, Business Transformation Readiness Assessment. The first is produced in Phase A and *updated in E* (the readiness assessment is conducted in A and reviewed in E, step 7). The architecture maturity part re-uses the Preliminary Phase ACMM scorecard rather than re-scoring. Readiness factors, their vision, current and target ratings and the risks are the ADM Techniques document's readiness technique applied.

| | |
|---|---|
| Reference | CA-2026-01, version 1.0, 31 March 2026; v1.1 after Phase E review, 29 August 2026 |
| Owner | Chief Architect with the Head of Retail's office |

## 1. Business Capability Assessment

| Capability | Baseline performance | Target aspiration | Baseline realisation | Target realisation | Impact of the target on the organisation |
|---|---|---|---|---|---|
| Customer Onboarding | 45 min at a counter; next-day activation; 3 KYC exceptions in audit | Under 10 min, counter or app; immediate activation; zero exceptions | Tellers, paper checks, Core Banking keying | Identity-verification service, one onboarding API, tellers as assisted channel | Counter time on onboarding halves; tellers retrained; no headcount reduction in this cycle |
| Payments — transfers | 22% mobile; legacy online site | 60% mobile by end 2027 | Point-to-point channel integrations | API layer over Core Banking | Online site retired 2028 |
| Payments — card | Batch fraud scoring, 14 h to block | Score before authorisation; block in 5 s | Card Switch, overnight Data Warehouse batch | Fraud Engine called by the Card Switch | Analysts move from morning triage to exception review |
| Risk Management — fraud | Rules maintained by analysts in the warehouse | Rules maintained by analysts in the engine | Data Warehouse | Fraud Engine | Rule ownership unchanged (a Board condition) |
| Lending | Four-day median decision | Out of scope; next cycle | — | — | — |

## 2. IT Capability Assessment

| Aspect | Baseline | Target |
|---|---|---|
| Change process maturity | Projects follow PRINCE2; architecture compliance not checked; releases quarterly | Two architecture checkpoints per project; monthly releases for the app |
| Operational process maturity | ITIL change and incident in place; no automated deployment for Core Banking | Automated deployment for the API layer and app; Core Banking unchanged |
| Capability and capacity | Retail IT: 38 engineers, fully committed to the v12 upgrade until June 2026; no identity-verification or fraud-modelling skills | Two engineers trained on the API product; engines bought with vendor support; no Core Banking change before July 2026 |
| Impact of the target on the IT organisation | — | A platform team for the API layer (4 people, new); Cards Operations gains a rule-tuning role; the Data Warehouse team loses the fraud batch |

## 3. Architecture maturity assessment

From the ACMM scorecard (Preliminary Phase): weighted mean **1.6**, target **2.5** after this cycle.

| Area | Finding |
|---|---|
| Governance processes, organisation, roles | Board exists; compliance checking does not — addressed by the Implementation Governance Model |
| Architecture skills | Four architects cover all domains; no data architect (loaned for Phase C); no security architect (Risk supplies one) |
| Landscape definition in the repository | 40 diagrams, baseline only, unverified; Digital Channels segment created in Phase A |
| Standards definition | Technology standards catalog exists; no application or data standards |
| Reference models | Vendor reference architectures only |
| Re-use potential | The API layer and the identity-verification service are re-usable by Lending in the next cycle — a deliberate roadmap choice |

## 4. Business Transformation Readiness Assessment

Readiness factors from the ADM Techniques document, rated on the five-point scale the technique uses, with the vision for each.

| Factor | Vision | Current | Target | Readiness risk |
|---|---|---|---|---|
| Vision | Every executive can state the three objectives | Medium | High | Low — the Vision is one page |
| Desire, willingness and resolve | Cards Operations wants scoring but fears losing the final say | Low | High | **R-1 High**: analysts resist first-line blocking by an engine. Mitigation: analysts keep the final block for six months; measured hand-over |
| Need | Fraud losses and lost customers are visible in the numbers | High | High | Low |
| Business case | Programme envelope indicative only | Low | High | Medium — Phase F must produce it |
| Funding | £420k committed; £6.5m indicative | Medium | High | Medium — Investment Committee in September |
| Sponsorship and leadership | Head of Retail and CIO are co-sponsors | High | High | Low |
| Governance | Board approves, nothing checks compliance | Low | Medium | **R-2 Medium**: projects deviate unnoticed. Mitigation: Implementation Governance Model, contracts |
| Accountability | Rule ownership stays with Cards Operations; API ownership undefined | Medium | High | Medium — platform team to be created |
| Workable approach and execution model | Two transitions around the card re-issue | Medium | High | Low |
| IT capacity to execute | Retail IT committed to v12 until June | Low | Medium | **R-3 High**: no capacity before July 2026. Mitigation: bought engines and a product API layer need little Core Banking change; WP-1 starts with the platform team |
| Enterprise capacity to execute change | Branches absorbing a 20-branch closure programme in parallel | Medium | Medium | Medium — Branch Council sequencing |
| Enterprise ability to implement and operate | No experience running real-time scoring | Low | Medium | Medium — vendor-run for the first year |

**Phase E review (v1.1).** R-3 confirmed and drove the roadmap sequence (API layer and mobile payments first, onboarding second). R-1 unchanged; the six-month analyst hand-over is written into the Architecture Contract for WP-4.
