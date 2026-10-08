---
title: "The assurance framework: the evidence that traceability holds"
unit: S7
objectives: ["S7.2"]
refs: ["SABSA §6", "SABSA §3.6", "SABSA §5", "GUIDE:integrating-risk-and-security §5.8", "GUIDE:integrating-risk-and-security §5.8.1"]
reading_minutes: 8
source: authored
status: draft
---
## Traceability is a claim; assurance is the proof

Two-way traceability says that every attribute is delivered by a control and every control is justified by an attribute. That is a statement about the *design*. The **assurance framework** is SABSA's answer to the follow-up question a regulator, a board or an auditor will ask: *show me*. It is the set of activities that produce **evidence** that the controls exist, work as designed, and meet the performance targets the attributes carry — and that they go on doing so (SABSA §6).

Assurance therefore spans the lifecycle. It begins in Design (is the design complete and traceable?), continues through Implement (was what was built what was designed?) and settles in Manage and Measure (does it still perform?). Most of its day-to-day activity lives in the Service Management layer (SABSA §6, §3.6, §4).

## The four questions assurance answers

| Question | Evidence type | When it is gathered | Example |
|---|---|---|---|
| Is the design complete? | Traceability records: attribute → service → mechanism → component, both directions | Design | A traceability matrix with no empty rows or unjustified columns |
| Was it built as designed? | Implementation verification: configuration review, code review, testing | Implement | A penetration test of the deployed authentication mechanism against its specification |
| Does it perform? | Attribute measurements against performance targets | Manage and Measure | Monthly uptime 99.95 % against a 99.9 % target for *Available* |
| Is it still true? | Continuous monitoring; periodic review; re-assessment on change | Manage and Measure | Quarterly recertification of privileged roles; re-test after a change |

(SABSA §6.)

**Trap:** evidence that a control *exists* is not evidence that it *performs*. An inventory listing the log-management product answers question two; only the measured log-completeness figure answers question three. Exam options that offer an asset register as "assurance that the attribute is met" are offering the wrong kind of evidence (SABSA §6, §5).

## Metrics are the hinge

The assurance framework works because the Business Attributes Profile was written with a **metric type**, a **measurement approach** and a **performance target** for each attribute. Assurance does not invent measures after the fact; it collects the ones the business agreed to in Strategy and Planning. If the profile says *Recoverable* is measured by restore time with a target of four hours, the assurance evidence is the restore-test log. If the profile had no metric, there would be nothing to assure — which is why SABSA treats an attribute without a target as incomplete (SABSA §5, §6).

| Metric type | Typical measurement approach | Assurance evidence |
|---|---|---|
| Hard (quantitative) | Automated monitoring | Time series against threshold |
| Soft (qualitative) | Survey, review, inspection | Review report with a rating against the target |
| Compliance | Audit against a standard | Audit finding: conformant / non-conformant |

(SABSA §5.)

## Assurance versus audit, again

Assurance is produced by those who design and operate the architecture; audit is the independent examination of that evidence. The framework needs both. Self-produced evidence without audit invites drift; audit without an assurance framework has nothing structured to examine and degenerates into a checklist. The TOGAF risk and security guide's Phase G *security audit* — reviews of processes, designs, code and configuration, plus security testing — is the audit half; the compliance review it feeds is where the assurance evidence is heard (SABSA §6, §3.6; GUIDE:integrating-risk-and-security §5.8, §5.8.1).

**Trap:** the audit does not *replace* the assurance framework. A common wrong answer says "an annual external audit provides the assurance". It provides independent confirmation of assurance evidence that must already exist (SABSA §6).

## Assurance and TOGAF compliance

TOGAF's compliance scale — irrelevant, consistent, compliant, conformant, fully conformant, non-conformant — is a verdict on whether an implementation matches the architecture. In SABSA terms, a compliance review is an assurance activity of the second kind (built as designed), and its finding is evidence to be filed. What SABSA adds is the third and fourth kinds: the review is not the end, because the attribute's target is measured for as long as the control lives. The crosswalk on `/adm/G` places ASSURANCE_FRAMEWORK and COMPLIANCE_EVIDENCE against Phase G for that reason (GUIDE:integrating-risk-and-security §5.8; SABSA §6).

## What a mature assurance framework contains

- A **traceability record** maintained as the design changes, not reconstructed for audits.
- A **test and review plan** per mechanism, saying how "built as designed" will be shown.
- A **measurement plan** per attribute, straight from the profile's metric and target.
- A **reporting line** to the business owner of each attribute, so the evidence reaches whoever set the target.
- A **re-assessment trigger**: change, incident, or elapsed time, whichever comes first.

Each of these lives in the Service Management layer and feeds the Manage and Measure phase; the last is what makes the lifecycle a loop rather than a line (SABSA §6, §3.6, §4).

## Check yourself

- List the four questions the assurance framework answers and the evidence for each.
- Why can the framework not work without the profile's metrics?
- How do TOGAF compliance reviews fit into SABSA assurance, and what do they leave out?

*Source note: written from the SABSA framework as published by the SABSA Institute; section numbers refer to the SABSA White Paper and are to be verified against the registered PDF.*
