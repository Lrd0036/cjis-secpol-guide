# From NIST to CJIS

## What changes, why it matters, and how to demonstrate it

A NIST control implementation is useful starting evidence. It is not a CJIS conclusion.
The practical job is to reconcile the **selected requirements, completed parameters,
CJIS-specific obligations, responsible parties, and operating evidence** for a named
agency and system. Matching control identifiers is only the beginning.

This companion is for engineers, security reviewers, agency owners, and providers
who already have an SP 800-53-based program and need to identify the additional work.
It is an unofficial, targeted first edition, not a complete crosswalk, implementation
baseline, or certification. Use it alongside the [Compliance Framework](COMPLIANCE-FRAMEWORK.md),
not instead of that framework's gates or verdict rules.

### Reading routes

- Understand the relationship: [Foundations](#1-foundations-catalog-baseline-and-governing-policy)
- Reuse an existing assessment: [Reconciliation workflow](#3-turn-an-existing-nist-package-into-a-cjis-review-package)
- Inspect real differences: [Worked control comparisons](#4-worked-control-comparisons)
- Allocate cloud work: [Responsibility and inheritance](#5-responsibility-and-inheritance)
- See a completed example: [Fictional incident-reporting evidence record](../examples/NIST-TO-CJIS-INCIDENT-REPORTING.md)
- Update a v6.0 package: [Verified v6.0-to-v6.1 changes](CJIS-6.0-TO-6.1-CHANGES.md)
- Reproduce the review: [Source and coverage manifest](../sources/manifests/nist-to-cjis-companion.md)

## Version contract

Reviewed October 16, 2026. **CJIS Security Policy v6.1, June 25, 2026** is the
explanatory target; **v6.0, December 27, 2024** is the historical comparison.
That does not establish the version governing your jurisdiction's present audit.
Record both the current audit/sanction baseline and readiness target, along with
state supplements, contracts, and written transition instructions.

The NIST textual comparator is **SP 800-53 Revision 5, September 2020, incorporating
the December 10, 2020 updates**, and **SP 800-53B with the December 10, 2020 updates**.
These are deliberately pinned publications, not a claim that their PDFs represent
all subsequent catalog releases. NIST's publication pages identify **Release 5.2.0,
August 27, 2025**, including catalog changes; the 800-53B notice says that release
made no baseline changes. The selected NIST base-control statements below were also checked against the
official NIST OSCAL catalog, metadata version **5.2.0**, last modified May 11, 2026.
Their substantive requirements match the pinned PDF comparisons; that check does
not extend to every discussion, related-control reference, or enhancement. The
manifest pins the downloaded catalog hash. [N53; N53B; N520]

Source IDs in brackets resolve in the [manifest](../sources/manifests/nist-to-cjis-companion.md).
CJIS page numbers below are the policy's printed page labels, not the PDF viewer's
page count. Each example identifies a control so it can still be located if pagination
changes. Summaries do not replace the full text, enhancements, notes, and exceptions.

## 1. Foundations: catalog, baseline, and governing policy

| Artifact | What it supplies | What it does not establish by itself |
|---|---|---|
| NIST SP 800-53 Rev. 5 | A catalog of security and privacy controls, enhancements, and organization-defined parameters | That every catalog control applies to your system, or that an implementation satisfies CJIS |
| NIST SP 800-53B | Low-, moderate-, and high-impact security baselines, a privacy baseline, and tailoring/overlay guidance | The complete CJIS requirement population or your jurisdiction's acceptance |
| FBI CJIS Security Policy | CJIS requirements, selected modernized control text, parameter values, additional CJIS-specific provisions, roles, and operational context | A transferable product approval or a substitute for applicable supplements and agreements |
| Your scoped assessment | Evidence that named requirements are met within a specified boundary and period | An authority decision unless an actual authorized decision is recorded |

NIST separates control content from baseline selection. Its assignment and selection
parameters are deliberately completed for the applicable context; once specified,
those values become part of the control that is assessed. Common, system-specific,
and hybrid implementations describe where a control is implemented, not an automatic
transfer of accountability. [N53 §2.2 pp.8–11, §2.3 pp.11–13; N53B §2.1]

Consequently, “we implement NIST Moderate” is an input to a comparison, not its
result. Ask which baseline/release, tailoring decisions, enhancements, parameter
values, system boundary, and assessment period that statement means. Then compare
actual requirements. NIST itself cautions that mappings do not establish equivalence.
[N53 publication page, mappings and crosswalks note]

CJIS also has requirements that cannot be reduced to a generic catalog identifier:
ORI-based transaction accountability, access authority, purpose of use, applicable
agreements, and criminal-justice-specific screening and reporting arrangements.
The worked examples below show both familiar IDs with more specific text and a
CJIS-specific control. CJIS §1.2 covers organizations and personnel with access to,
or who operate in support of, criminal justice services and information; §1.3 and
§3.2.1 preserve more stringent or additional local protections. [C61 §§1.2–1.3 p.1,
§3.2.1 p.5]

## 2. Classify the difference before choosing a fix

These are analytical labels for this guide, not official FBI control categories:

| Difference | Question to answer | Typical engineering consequence |
|---|---|---|
| Selection | Is this base control or enhancement actually required by the governing CJIS text? | Add a missing requirement to the assessment population; do not assume a matching family covers it |
| Parameter completion | Did CJIS specify a frequency, recipient, strength, or trigger where NIST leaves an assignment? | Change configuration or procedure if your existing value does not meet the specified value |
| Refinement | Does CJIS prescribe an additional condition, approval, or domain-specific process? | Extend the workflow and its tests, not merely the control label |
| CJIS-specific obligation | Is there a requirement outside the generic control mapping? | Add the missing business/authority workflow and evidence |
| Responsibility | Does the provider perform only part of the control? | Document the split, customer settings, evidence rights, and remaining agency work |
| Version/transition | Did text, location, or sanction treatment change? | Separate substantive remediation from renumbering and from authority-confirmed transition treatment |

Do not infer that a higher NIST impact baseline automatically dominates every CJIS
requirement. A stronger technical mechanism can still omit a required recipient,
authorized purpose, transaction identifier, or agreement.

## 3. Turn an existing NIST package into a CJIS review package

This workflow is an implementation suggestion. It does not create new CJIS requirements.

1. **Freeze the claim.** Name the agency, jurisdiction, system/release, deployment,
   data flows, provider services, assessment period, and responsible authority. Include
   support, administration, logs, backups, exports, and recovery paths. Resolve CJI
   classification before excluding a component.
2. **Freeze the sources.** Record governing CJIS version, readiness version, supplements,
   agreements, NIST release/baseline, and original tailoring decisions. Archive stable
   source identifiers and retrieval dates. Do not silently update a crosswalk underneath
   an already issued conclusion.
3. **Enumerate the CJIS population first.** Include applicable policy areas,
   non-modernized provisions, base controls, enhancements, separately testable parameters,
   appendices, agreements, and local additions. The six examples here and the repository's
   [base-control index](CONTROL-INDEX.md) are not that population.
4. **Attach NIST evidence second.** For each CJIS requirement, identify potentially reusable
   NIST evidence. Compare exact text and values before accepting inheritance or reuse.
   Keep one-to-many and partial mappings visible.
5. **Assign the remainder.** Name the agency and provider owners, service model,
   customer configurations, interfaces, contractual evidence rights, and authority
   questions. An unassigned task is not inherited just because a service is hosted.
6. **Test design, implementation, and operation separately.** A policy says what should
   happen; deployed configuration shows what can happen; dated records show what did
   happen. Test exceptions and failed paths as well as normal operation. Reuse the
   [Control Evidence Record](../templates/CONTROL-EVIDENCE.md).
7. **Resolve differences without overstating progress.** Track current applicable failures,
   missing evidence, readiness work, and authority decisions distinctly. Follow the
   [final decision rule](COMPLIANCE-FRAMEWORK.md#final-decision-rule): a proven applicable
   failure is not erased by unrelated unknowns. Do not call this targeted comparison
   whole-system readiness.
8. **Submit the bounded conclusion.** Use the [System Assessment](../templates/SYSTEM-ASSESSMENT.md)
   and [Authority Decision Record](../templates/AUTHORITY-DECISION.md). Preserve evidence
   privately; commit only sanitized identifiers or fictional examples to this public repository.

### Suggested reconciliation ledger

Add these columns to your controlled assessment worksheet; they complement, rather
than replace, the existing evidence record:

| Field | What to capture |
|---|---|
| CJIS requirement | Version, section/control/enhancement, clause, printed page, exact applicable value |
| NIST starting point | Publication/release, baseline/tailoring, ID, parameter, evidence reference |
| Difference | Selection, parameter, refinement, additional obligation, responsibility, or version |
| Applicability | Existing framework value and documented rationale; unresolved authority questions |
| Owner and boundary | Agency/provider/shared role; service, components, interfaces, authorized users |
| Evidence reuse | What is reusable, what is out of scope, and which layer/period it proves |
| Remaining proof | Test, artifact, population/sample, reviewer, date, and exception handling |
| Treatment | Current audit baseline versus readiness target; authority record for any accepted treatment |
| Result | Existing control-level result and linked finding; no invented “CJIS-equivalent” score |

## 4. Worked control comparisons

The examples are selected to demonstrate different kinds of change. They do not
review all clauses of these controls or their enhancements. A parameter highlighted
here is not the entire requirement.

### 4.1 AU-6: a control ID does not prove weekly review

**NIST starting point.** AU-6 leaves review frequency, relevant activity, and reporting
personnel as organization-defined parameters. [N53 AU-6 p.70; N520 `au-6`]

**CJIS requirement summary.** Review and analyze audit records **weekly** for
inappropriate or unusual activity and potential impact; report findings to the
specified audit-review and security/privacy personnel. Adjust review, analysis, and
reporting when risk changes. [C61 AU-6 p.50]

**Why it matters.** A monthly NIST review procedure does not meet this CJIS frequency.
A SIEM subscription or enabled log collection says nothing about completed review.
A technically continuous rule engine also needs a demonstrated review/reporting
process appropriate to the requirement.

**Suggested demonstration.** Select an assessment period and enumerate its weekly
review windows. Reconcile review records against the scoped log-source inventory.
Inspect reviewer identity, time window, findings, dispositions, and escalation.
Check how new risk information changes depth or frequency. Investigate missing
windows instead of treating a dashboard screenshot as operating evidence.

**Boundary and caveat.** The discussion permits authorized outside organizations to
perform review/analysis when the organization cannot or is prohibited. Document that
arrangement and evidence access; it does not make the review requirement disappear.
No particular SIEM, ticket product, or sampling plan is prescribed by this example.

### 4.2 IA-0: the requesting agency must remain traceable

**NIST starting point.** There is no IA-0 in the reviewed NIST catalog. AC-3 and AU-3
are useful conceptual associations for enforcement and audit content, not an official
one-to-one crosswalk or proof of equivalence. [N520]

**CJIS requirement summary.** IA-0 requires an FBI-authorized ORI in CJIS transactions
and agency traceability. For inquiries on behalf of another authorized agency, a
servicing agency can use the requesting agency's ORI or its own under the stated
audit-trail conditions. The CSA/SIB/Channeler must be able to trace the transaction
to the specific requesting agency. A limited-access ORI must not obtain fuller access
by using another agency's full-access ORI. [C61 IA-0 p.92]

**Why it matters.** A shared integration identity may successfully authenticate while
losing the actual agency's lineage or granting more access than that agency has.
A generic identity-provider audit record cannot by itself establish transaction-level
CJIS attribution.

**Suggested demonstration.** Use synthetic transactions through the actual integration
path. Trace the requesting agency, servicing agency, submitted ORI, user/device
identifiers, and downstream audit record. Test the permitted servicing-agency case
and a denied attempt to escalate limited ORI access. Verify retrieval across the
applicable retention period and delegated interfaces.

**Boundary and caveat.** Do not assert that the requesting agency's ORI is always the
only permitted transmitted value. Preserve IA-0's servicing-agency conditions. The
policy notes future inclusion in AC-3 when modernized; it remains IA-0 in v6.1.

### 4.3 IR-6: time, suspicion, and recipients are separate obligations

**NIST starting point.** IR-6 leaves the reporting interval and authorities as
organization-defined parameters. [N53 IR-6 p.157; N520 `ir-6`]

**CJIS requirement summary.** IR-6(a) requires personnel to report **suspected**
incidents to the organizational incident-response capability **immediately, no later
than one hour after discovery**. IR-6(b) identifies incident-handling personnel,
the CSO, SIB Chief, or Interface Agency Official, and the FBI CJIS ISO as reporting
recipients. [C61 IR-6 p.171]

**Why it matters.** A workflow that waits for confirmed compromise, or whose only
recipient is the vendor's account manager, is not the specified workflow. The
one-hour ceiling is not permission to deliberately wait until minute 59.

**Suggested demonstration.** Reconcile runbooks, contract escalation duties, contact
rosters, paging routes, and fallback contacts. In an authorized exercise, record
discovery, internal report, acknowledgment, and external-notification events as
separate timestamps. Test after-hours and failed-contact paths. Use the
[fictional worked record](../examples/NIST-TO-CJIS-INCIDENT-REPORTING.md) as a model
for what evidence does and does not establish.

**Boundary and caveat.** The one-hour statement explicitly applies to personnel's
reporting to the organizational capability in (a). Do not invent an independently
stated one-hour deadline for every external recipient in (b). Confirm applicable
external timing and routing instructions with the authority. IR-6(1)'s automated
reporting and IR-6(3)'s supply-chain coordination are additional requirements to
assess, not implicitly passed by this base-control example.

### 4.4 PS-3: screening is a legal and access-authorization workflow

**NIST starting point.** PS-3 calls for pre-access screening and rescreening using
organization-defined conditions and frequency. [N53 PS-3 p.223; N520 `ps-3`]

**CJIS requirement summary.** PS-3 elaborates pre-access screening with state-of-residency
and national fingerprint-based record checks, approved legal authority for national
checks, and an additional agency-state check when residency differs. It specifies
who reviews criminal-history results and makes access decisions, and requires the
list of personnel authorized for unescorted access to unencrypted CJI. Read the
actual exceptions and decision pathways. [C61 PS-3 pp.206–207; heading p.205]

**Why it matters.** “Our employees passed background checks” does not establish the
required check type, legal authority, access approval, or coverage of vendor support
staff. An employment decision is not the same decision as CJI access.

**Suggested demonstration.** Reconcile the population with actual privileged and
unescorted-access capabilities, including contractors. Review restricted references
to screening completion, lawful check authority, authorized access determinations,
and provisioning dates. Demonstrate that access cannot precede required approval.
Keep underlying criminal-history records in their authorized system; do not duplicate
them into general engineering tickets or a public assessment.

**Boundary and caveat.** Agencies legally authorized to bypass state repositories
need only the national fingerprint check. Agencies without approved statutory
authority for civil fingerprint checks on personnel with CHRI access have the
specified exemption until authority is obtained; that is not an exemption from all
security obligations. PS-3(b) **recommends** rescreening and requires legal authority
for it. Do not invent a mandatory periodic fingerprint interval. Felony, misdemeanor,
and variance/access-review provisions require their actual authorized decision
process, not an automated blanket rule. CJIS is not uniformly “stricter NIST.”

### 4.5 SA-9: a supplier report does not replace an agreement or oversight

**NIST starting point.** SA-9 leaves required provider controls and ongoing monitoring
methods as organization-defined parameters, while requiring oversight and role
definition. [N53 SA-9 p.271; N520 `sa-9`]

**CJIS requirement summary.** SA-9 specifies applicable CJIS agreements and outsourcing
arrangements, documented oversight roles, and ongoing monitoring including at least
**triennial audits of external service providers with information-system access**.
Its inspection and audit provisions also address unannounced inspections, scheduled
facility audits, and inter-CSA contractor-audit use. [C61 SA-9 pp.228–229]

**Why it matters.** A provider's SOC report may help demonstrate selected operations.
It does not itself establish the applicable executed Security Addendum, management
control arrangement, outsourcing authority, or your right and ability to perform
required oversight.

**Suggested demonstration.** Classify each provider by service, access, function, and
public/private relationship. Identify which agreement applies, then reconcile
executed documents, scope, oversight owner, audit rights, audit dates, findings,
and remediation closure. Make subcontractor/support paths visible. Evaluate reused
assurance reports against the specific service, period, exclusions, and customer duties.

**Boundary and caveat.** Not every provider needs every listed agreement. Government
NCJA management-control agreements, private-contractor Security Addenda, and
channeling/non-channeling outsourcing standards have distinct applicability.
SA-9(c)(4) permits using previous contractor-facility audit results for another CSA
unless that CSA requires a new audit. Do not promise universal acceptance of a
provider's earlier audit.

### 4.6 SC-13: preserve the cryptographic alternatives and the date

**NIST starting point.** SC-13 leaves cryptographic uses and types as organization-defined
parameters. [N53 SC-13 pp.308–309; N520 `sc-13`]

**CJIS requirement summary.** For the stated CJI-in-transit use outside a physically
secure location, SC-13 specifies FIPS 140-3-certified modules **or** a FIPS-validated
AES algorithm (FIPS 197), with at least **256-bit symmetric key strength**. Its note
permits subsequent versions of approved modules under current FIPS 140-3 review
while certification is pending and says FIPS 140-2 certificates are not acceptable
after **September 21, 2026**. That date has passed as of this guide's review.
[C61 SC-13 p.243]

**Why it matters.** “Supports AES-256” is not evidence of the applicable validation,
actual deployed version, enabled mode, or every CJI transport path. Conversely,
rewriting the policy as universally requiring a FIPS 140-3 module erases an explicit
alternative in its text.

**Suggested demonstration.** Map CJI transport paths, endpoints, termination points,
and physically secure boundary assumptions. For the relied-on branch, retain the
exact product/module or algorithm version, validation reference, supported environment,
and configuration evidence. Verify deployed cryptographic settings and the approved
implementation's applicability to that deployment; exercise downgrade and unsupported
paths safely. If relying on the pending-module note, identify the approved predecessor,
subsequent version, and actual current review evidence rather than assuming any
unvalidated module qualifies.

**Boundary and caveat.** Algorithm validation and module certification are different
claims. Neither a marketing page nor a general cloud-region label establishes them.
SC-13 is not all encryption policy: separately assess SC-8(1), SC-28, and relevant
mobile requirements. The v6.0-to-v6.1 appendix separates the new key-strength change
from the already-existing FIPS 140-2 date.

## 5. Responsibility and inheritance

The official Requirements Companion's introduction supplies an IaaS/PaaS/SaaS
responsibility matrix and explicitly leaves the agency ultimately accountable even
when a provider has technical responsibility. Use the row for the actual control and
service model; then validate the real contract, architecture, and customer configuration.
Do not infer a whole family is inherited from a single matrix label. [RC61 introduction]

The following is an **illustrative implementation allocation**, not a replacement
for that official matrix or a claim about any provider:

| Work item | Agency side | Provider side | Proof of the handoff |
|---|---|---|---|
| Audit review | Identify required sources, authorized reviewers, and findings recipients | Supply contracted logging/review capability and scoped operating evidence | Source coverage, weekly review records, escalation and missing-source tests |
| Incident reporting | Maintain CJIS authority chain and agency response capability | Detect and report under the agreed incident workflow; preserve evidence | Tested contacts, discovery/report timestamps, fallback and responsibility records |
| Screening/access | Establish applicable access authority and approved access population | Identify staff/support access and produce authorized screening/approval evidence | Reconciliation of actual capability to authorized personnel, including contractors |
| Cryptography | Define data paths and boundary assumptions; configure customer-controlled settings | Supply supported cryptographic implementations and evidence for provider-managed layers | Exact deployment/version/validation mapping and configuration records |
| External-service oversight | Determine applicable agreements and conduct/arrange required oversight | Support contractual audit/evidence duties and corrective action | Executed scope-specific agreements, audit results, remediation closure |

An acceptable inheritance claim identifies the provider/service, exact control portion,
evidence period, coverage/exclusions, customer obligations, and residual agency work.
An absent artifact is a missing proof item; affirmative evidence of an unmet applicable
requirement is a failure. A FedRAMP authorization or commercial assurance report may
supply evidence, but a label alone does not perform this reconciliation or establish
CJIS authority acceptance.

There is no blanket government-cloud-region conclusion in this guide. Choose and
assess a deployment against the applicable requirements, access model, agreements,
and authority. Likewise, a vendor's “CJIS certified” statement cannot replace the
scoped evidence and authority record required by this repository's decision system.

## 6. Coverage and limitations

This edition deeply compares **six selected examples**: AU-6, IA-0, IR-6, PS-3, SA-9,
and SC-13. It explains the catalog/baseline relationship and gives a method and a
fictional evidence record. The version appendix is a verified subset of changes.

It does **not** enumerate every CJIS control, enhancement, parameter, non-modernized
section, appendix, system manual, dissemination restriction, Compact rule, state
supplement, or contractual requirement. It does not establish a complete NIST
Moderate-to-CJIS gap inventory. Even the selected controls have clauses/enhancements
not fully assessed here. No actual agency system or vendor was assessed.

Before extending this guide, record each new claim's authoritative version and
locator in the manifest, read the complete control and relevant notes, distinguish
policy text from proposed evidence, and test the navigation. Do not promote an
inferred conceptual relationship to official equivalence. Re-check sources and
applicable authority instructions before a real assessment.
