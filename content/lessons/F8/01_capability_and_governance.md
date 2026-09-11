---
title: Establishing the capability, the Architecture Board, governance, compliance, contracts, maturity and skills
unit: F8
objectives: ["8.1", "8.2", "8.3", "8.4", "8.5"]
refs: ["GOV §2", "GOV §3", "GOV §4", "GOV §5", "GOV §6", "GOV §7", "GOV §8"]
reading_minutes: 10
source: authored
status: draft
---
## Establishing an Architecture Capability (GOV §2)

Setting up an EA practice is itself an ADM cycle: the Preliminary Phase and Phase A applied to
the practice, giving it a business architecture (governance, processes, roles), data (the
repository), applications (tools) and technology. Seven marks in Part 1 come from this
document, so it repays a careful read.

## The Architecture Board (GOV §3)

A cross-organisational body responsible for oversight of the architecture: consistency
between sub-architectures, compliance, granting **dispensations**, resolving ambiguities,
setting priorities. Typically five to ten members representing the key stakeholder groups.

## Architecture Governance (GOV §4)

The practice of managing and controlling architectures enterprise-wide: **controls** over
creation and monitoring, **compliance** with standards, **accountability**, and effective
**processes**. It sits inside corporate and IT governance. The framework has a **conceptual**
structure (process, content, context, repository) and an **organisational** structure
(global, regional, local governance).

<figure class="my-4">
<svg viewBox="0 0 760 196" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="The Architecture Governance Framework as two structures: a conceptual one of process, content, context and repository, and an organizational one of global, regional and local governance">
<rect x="15" y="12" width="330" height="150" rx="10" fill="#fafafa" stroke="#7aa2e3"/>
<text x="180" y="32" text-anchor="middle" font-size="12" fill="#222" font-weight="bold">Conceptual structure</text>
<rect x="35" y="46" width="140" height="40" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="105.0" y="69.8" text-anchor="middle" font-size="11">Process</text>
<rect x="185" y="46" width="140" height="40" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="255.0" y="69.8" text-anchor="middle" font-size="11">Content</text>
<rect x="35" y="98" width="140" height="40" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="105.0" y="121.8" text-anchor="middle" font-size="11">Context</text>
<rect x="185" y="98" width="140" height="40" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="255.0" y="121.8" text-anchor="middle" font-size="11">Repository</text>
<rect x="415" y="12" width="330" height="150" rx="10" fill="#fafafa" stroke="#7fbf7a"/>
<text x="580" y="32" text-anchor="middle" font-size="12" fill="#222" font-weight="bold">Organizational structure</text>
<rect x="435" y="46" width="290" height="30" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/>
<text x="580.0" y="64.8" text-anchor="middle" font-size="11">Global governance</text>
<rect x="455" y="82" width="250" height="30" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/>
<text x="580.0" y="100.8" text-anchor="middle" font-size="11">Regional governance</text>
<rect x="475" y="118" width="210" height="30" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/>
<text x="580.0" y="136.8" text-anchor="middle" font-size="11">Local governance</text>
<text x="380" y="92" text-anchor="middle" font-size="20" fill="#666">+</text>
<text x="380" y="184" text-anchor="middle" font-size="10" fill="#666">Both sit inside corporate and IT governance: controls, compliance, accountability, processes</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">The governance framework's two structures side by side. Original drawing; structures per GOV §3.2.</figcaption>
</figure>

## Architecture Compliance (GOV §5)

Six levels: **irrelevant** (no features in common), **consistent** (some of the spec
implemented, in line), **compliant** (all that is implemented is in line, but not all of the
spec), **conformant** (all of the spec, with additions), **fully conformant** (all of the spec
and nothing else), **non-conformant** (contradicts the spec). Assessed through **Architecture
Compliance Reviews** with checklists per domain.

<figure class="my-4">
<svg viewBox="0 0 760 140" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="Architecture compliance as a scale from irrelevant through consistent, compliant and conformant to fully conformant, with non-conformant set apart as contradicting the specification">
<defs><marker id="arr-f8-b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
<rect x="15" y="30" width="116" height="62" rx="6" fill="#f1f1f1" stroke="#999"/>
<text x="73.0" y="51.5" text-anchor="middle" font-size="10" font-weight="bold">Irrelevant</text>
<text x="73.0" y="64.5" text-anchor="middle" font-size="10">no features in</text>
<text x="73.0" y="77.5" text-anchor="middle" font-size="10">common</text>
<rect x="137" y="30" width="116" height="62" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="195.0" y="51.5" text-anchor="middle" font-size="10" font-weight="bold">Consistent</text>
<text x="195.0" y="64.5" text-anchor="middle" font-size="10">some of the spec, in</text>
<text x="195.0" y="77.5" text-anchor="middle" font-size="10">line</text>
<rect x="259" y="30" width="116" height="62" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="317.0" y="45.0" text-anchor="middle" font-size="10" font-weight="bold">Compliant</text>
<text x="317.0" y="58.0" text-anchor="middle" font-size="10">all implemented is</text>
<text x="317.0" y="71.0" text-anchor="middle" font-size="10">in line, but not all</text>
<text x="317.0" y="84.0" text-anchor="middle" font-size="10">the spec</text>
<rect x="381" y="30" width="116" height="62" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/>
<text x="439.0" y="51.5" text-anchor="middle" font-size="10" font-weight="bold">Conformant</text>
<text x="439.0" y="64.5" text-anchor="middle" font-size="10">all of the spec,</text>
<text x="439.0" y="77.5" text-anchor="middle" font-size="10">with additions</text>
<rect x="503" y="30" width="116" height="62" rx="6" fill="#e3f5e1" stroke="#7fbf7a"/>
<text x="561.0" y="51.5" text-anchor="middle" font-size="10" font-weight="bold">Fully conformant</text>
<text x="561.0" y="64.5" text-anchor="middle" font-size="10">all of the spec and</text>
<text x="561.0" y="77.5" text-anchor="middle" font-size="10">nothing else</text>
<rect x="625" y="30" width="116" height="62" rx="6" fill="#fde8e6" stroke="#c0392b"/>
<text x="683.0" y="58.0" text-anchor="middle" font-size="10" font-weight="bold">Non-conformant</text>
<text x="683.0" y="71.0" text-anchor="middle" font-size="10">contradicts the spec</text>
<line x1="15" y1="110" x2="618" y2="110" stroke="#555" marker-end="url(#arr-f8-b)"/>
<text x="316" y="128" text-anchor="middle" font-size="10" fill="#345">more of the specification implemented, and less that is outside it →</text>
<line x1="618" y1="24" x2="618" y2="100" stroke="#c0392b" stroke-dasharray="4 3"/>
<text x="683" y="128" text-anchor="middle" font-size="10" fill="#c0392b">off the scale</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">The compliance levels as a scale, with non-conformant off the end of it. Original drawing; terms per GOV §6.2.</figcaption>
</figure>

## Architecture Contracts (GOV §6)

Joint agreements between development partners and sponsors on deliverables, quality and
fitness-for-purpose; signed in Phase G. Content includes scope, conformance requirements,
architecture deliverables, quality measures, time window and risks.

<figure class="my-4">
<svg viewBox="0 0 760 200" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="The Architecture Contract signed between sponsors and development partners at the handover from Phase F to Phase G, where compliance reviews are held against it">
<defs><marker id="arr-f8-c" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
<rect x="15" y="60" width="150" height="40" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="90.0" y="77.0" text-anchor="middle" font-size="10" font-weight="bold">Phase F</text>
<text x="90.0" y="90.0" text-anchor="middle" font-size="10">roadmap and plan final</text>
<line x1="165" y1="80" x2="215" y2="80" stroke="#555" marker-end="url(#arr-f8-c)"/>
<rect x="217" y="40" width="190" height="80" rx="6" fill="#fff1d6" stroke="#e0b060"/>
<text x="312.0" y="69.8" text-anchor="middle" font-size="11" font-weight="bold">Architecture Contract</text>
<text x="312.0" y="83.8" text-anchor="middle" font-size="11">signed at the handover</text>
<text x="312.0" y="97.8" text-anchor="middle" font-size="11">to implementation</text>
<text x="312" y="28" text-anchor="middle" font-size="10" fill="#345">sponsors</text>
<line x1="312" y1="32" x2="312" y2="38" stroke="#999" marker-end="url(#arr-f8-c)"/>
<text x="312" y="140" text-anchor="middle" font-size="10" fill="#345">development partners</text>
<line x1="312" y1="130" x2="312" y2="122" stroke="#999" marker-end="url(#arr-f8-c)"/>
<line x1="407" y1="80" x2="455" y2="80" stroke="#555" marker-end="url(#arr-f8-c)"/>
<rect x="457" y="40" width="150" height="80" rx="6" fill="#f3e3f7" stroke="#b58ac9"/>
<text x="532.0" y="64.0" text-anchor="middle" font-size="10" font-weight="bold">Phase G</text>
<text x="532.0" y="77.0" text-anchor="middle" font-size="10">compliance reviews</text>
<text x="532.0" y="90.0" text-anchor="middle" font-size="10">against the contract;</text>
<text x="532.0" y="103.0" text-anchor="middle" font-size="10">change requests</text>
<line x1="607" y1="80" x2="640" y2="80" stroke="#555" marker-end="url(#arr-f8-c)"/>
<rect x="642" y="60" width="103" height="40" rx="6" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="693.5" y="77.0" text-anchor="middle" font-size="10" font-weight="bold">Phase H</text>
<text x="693.5" y="90.0" text-anchor="middle" font-size="10">change managed</text>
<rect x="15" y="158" width="730" height="30" rx="6" fill="#f1f1f1" stroke="#999"/>
<text x="380.0" y="176.5" text-anchor="middle" font-size="10">contents: scope · conformance requirements · architecture deliverables · quality measures · time window · risks</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">The contract at the F to G handover and what it contains. Original drawing; role per GOV §5.3, contents per GOV §5.2, Phase G use per ADM §11.3.</figcaption>
</figure>

## Maturity models and the Skills Framework (GOV §7, §8)

A **maturity model** assesses the architecture practice against levels (from none through
initial, under development, defined, managed, measured) to plan improvement. The **Skills
Framework** defines roles, the skills each needs, and proficiency levels, so an EA team can be
staffed and trained deliberately.

<figure class="my-4">
<svg viewBox="0 0 760 204" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12" role="img" aria-label="Architecture maturity as six ascending steps from none to measured, beside the Skills Framework chain of roles, skills and proficiency levels">
<defs><marker id="arr-f8-d" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>
<rect x="15" y="144" width="96" height="16" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="63" y="126" text-anchor="middle" font-size="10" fill="#222" font-weight="bold">0 None</text>
<rect x="115" y="124" width="96" height="36" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="163" y="106" text-anchor="middle" font-size="10" fill="#222" font-weight="bold">1 Initial</text>
<rect x="215" y="104" width="96" height="56" fill="#e0ecff" stroke="#7aa2e3"/>
<text x="263" y="86" text-anchor="middle" font-size="10" fill="#222" font-weight="bold">2 Under</text>
<text x="263" y="98" text-anchor="middle" font-size="10" fill="#222">development</text>
<rect x="315" y="84" width="96" height="76" fill="#e3f5e1" stroke="#7fbf7a"/>
<text x="363" y="66" text-anchor="middle" font-size="10" fill="#222" font-weight="bold">3 Defined</text>
<rect x="415" y="64" width="96" height="96" fill="#e3f5e1" stroke="#7fbf7a"/>
<text x="463" y="46" text-anchor="middle" font-size="10" fill="#222" font-weight="bold">4 Managed</text>
<rect x="515" y="44" width="96" height="116" fill="#e3f5e1" stroke="#7fbf7a"/>
<text x="563" y="26" text-anchor="middle" font-size="10" fill="#222" font-weight="bold">5 Measured</text>
<line x1="30" y1="176" x2="600" y2="176" stroke="#555" marker-end="url(#arr-f8-d)"/>
<text x="315" y="192" text-anchor="middle" font-size="10" fill="#345">assess where the practice stands, then plan the climb →</text>
<rect x="625" y="40" width="120" height="120" rx="6" fill="#fff1d6" stroke="#e0b060"/>
<text x="685.0" y="71.0" text-anchor="middle" font-size="10" font-weight="bold">Skills Framework</text>
<text x="685.0" y="84.0" text-anchor="middle" font-size="10">roles</text>
<text x="685.0" y="97.0" text-anchor="middle" font-size="10">↓</text>
<text x="685.0" y="110.0" text-anchor="middle" font-size="10">skills each needs</text>
<text x="685.0" y="123.0" text-anchor="middle" font-size="10">↓</text>
<text x="685.0" y="136.0" text-anchor="middle" font-size="10">proficiency levels</text>
</svg>
<figcaption class="text-xs text-base-content/60 mt-1">Maturity levels as steps, with the Skills Framework beside them. Original drawing; levels per GUIDE:architecture-maturity-models §2.3, roles, skills and proficiency per GUIDE:architecture-skills-framework §4.</figcaption>
</figure>
