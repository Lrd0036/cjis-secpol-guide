# CJIS Compliance Framework

## The governing idea

A CJIS conclusion is not a property of a product in isolation.

It is a relationship:

```text
data + purpose + people + system + agreements + controls + evidence + authority
```

Remove any term and the conclusion changes.

A beautifully encrypted database used for an unauthorized purpose is still unauthorized. A vendor with excellent controls but no applicable agreement is still missing the relationship that permits the work. A policy document with no operating evidence proves that somebody can write a policy document.

So the framework uses gates. A later gate cannot repair a failed earlier gate.

## Gate 0: Name the question

Record the exact claim before testing it.

```text
Can [named organization] use [named system and version]
for [named workload and authorized purpose]
with [named CJI categories]
in [named jurisdiction]
under [named policy/audit baseline]
as of [date]?
```

If the claim is merely “Is Product X CJIS compliant?”, the first result is `NOT_PROVEN`. The object under assessment has not been defined.

## Gate 1: Establish jurisdiction and authority

Identify:

- the criminal or noncriminal justice agency;
- the CJIS Systems Agency (CSA) or equivalent;
- the CJIS Systems Officer (CSO);
- the CSA Information Security Officer or security point of contact;
- the Compact Officer when CHRI and Compact rules apply;
- the agency security owner;
- the contracting agency and Agency Coordinator when contractors are involved.

Then record which official can approve access, interpret state requirements, accept compensating measures, and issue the final determination.

### Gate result

- Named jurisdiction and decision authority: continue.
- Authority unknown: `NOT_PROVEN`.
- Required authority has denied the design or access: `FAIL`.

## Gate 2: Establish the version profile

Record four separate things:

1. FBI CJIS Security Policy version in force.
2. Jurisdiction's current audit baseline.
3. State, tribal, territorial, federal, or local supplements.
4. Future or zero-cycle controls being tracked for readiness.

Do not silently substitute “latest published” for “currently audited.” Do not silently use an older audit baseline as permission to ignore an announced transition.

### Gate result

- Version and jurisdictional overlays confirmed: continue.
- Version inferred from a vendor webpage: `NOT_PROVEN`.
- Assessment performed against the wrong required baseline: `STALE` or `FAIL`, depending on authority direction.

## Gate 3: Define the CJI boundary

Build the data-flow model.

Inventory where CJI is:

- created or received;
- viewed;
- queried;
- processed or transformed;
- transmitted;
- cached;
- logged;
- backed up or replicated;
- exported or printed;
- supported by administrators;
- disclosed to another party;
- retained;
- sanitized or destroyed.

Classify the data:

- biometric data;
- identity history data;
- biographic data;
- property data accompanied by PII;
- case or incident history;
- CHRI;
- NCIC restricted or non-restricted file information;
- PII extracted from CJI;
- exempt transaction-control numbers not accompanied by CJI or PII;
- authorized public information no longer subject to the policy.

“We do not store CJI” does not end the inquiry. A service can transmit it, display it, decrypt it, administer systems containing it, receive it in support tickets, write it to telemetry, or restore it from backups.

Access follows capability. Not job title.

### Gate result

- No CJI access or supporting-system path, proven by architecture and operations: `OUT_OF_SCOPE` for the named boundary.
- CJI exists and flows are documented: continue.
- Data classification or flow is unknown: `NOT_PROVEN`.
- CJI appears in an unapproved location or flow: `FAIL` until corrected and reviewed.

## Gate 4: Establish lawful purpose and agreements

Document the authorized purpose for each access and dissemination path. Then identify the instruments that govern the exchange or support relationship:

- CJIS user agreement;
- information exchange agreement;
- management control agreement;
- interagency connection agreement;
- noncriminal justice agency agreement or memorandum of understanding;
- outsourcing standard;
- contract and CJIS Security Addendum;
- state-specific agreement or approval;
- CHRI dissemination authority and secondary-dissemination record, when applicable.

A technical control cannot create lawful purpose. TLS does not turn an unauthorized disclosure into an authorized one. It merely encrypts the unauthorized disclosure very professionally.

### Gate result

- Purpose and required agreements verified: continue.
- Agreement applicability unresolved: `NOT_PROVEN`.
- Required agreement or authorized purpose absent: `FAIL`.

## Gate 5: Establish people and access

Inventory every human and non-human path to CJI or systems that protect CJI:

- end users;
- supervisors and approvers;
- privileged administrators;
- developers and release engineers;
- help-desk and support personnel;
- cloud-provider personnel;
- subcontractors;
- incident responders;
- backup and disaster-recovery operators;
- service accounts, workloads, APIs, and automation.

For each path, record authorization, identity proofing, screening, training, access agreement, role, least privilege, authentication, review cadence, transfer process, and termination process. Personnel requirements depend on role, access, encryption state, physical access, agreements, and jurisdictional rules. Do not reduce the analysis to “background check: yes/no.”

### Gate result

- Every access path is authorized and evidenced: continue.
- Unknown provider or subcontractor access: `NOT_PROVEN`.
- Required screening, training, agreement, or authorization missing: `FAIL`.

## Gate 6: Assess the control baseline

Assess Policy Area 1, the relevant non-modernized sections, every applicable control and enhancement in the governing baseline, and every jurisdictional addition.

Use [Control Families](CONTROL-FAMILIES.md) as the navigation layer. Use the official policy and Requirements Companion for the actual “shall” statements, priority, sanction date, and cloud responsibility.

For each requirement, assign:

- `APPLICABLE_AGENCY`
- `APPLICABLE_PROVIDER`
- `APPLICABLE_SHARED`
- `APPLICABLE_CJIS_CSO`
- `INHERITED`
- `NOT_APPLICABLE`
- `TBD_BY_AUTHORITY`

`NOT_APPLICABLE` requires a written rationale and boundary evidence. “The vendor handles that” is not a rationale. It is an invitation to find out what the contract forgot.

### Gate result

- All applicable controls implemented or covered by accepted plans: continue.
- Applicable control unmet: `FAIL`.
- Applicability, inherited control, or shared responsibility unresolved: `NOT_PROVEN`.

## Gate 7: Prove operation

For every applicable control, test three layers:

1. **Design** — the policy, architecture, configuration standard, contract, or procedure says what should happen.
2. **Implementation** — the system configuration and responsible process embody the design.
3. **Operation** — recent records show the control actually happened and exceptions were handled.

Evidence should be:

- attributable to a source and owner;
- scoped to the assessed boundary;
- dated and current;
- reproducible or independently reviewable;
- protected from unauthorized change;
- specific enough to support the requirement;
- sanitized so the assessment does not create a new CJI spill.

Examples include configuration exports, identity and privilege reviews, training records, screening confirmation, signed agreements, network and data-flow diagrams, key-management records, log samples, alert investigations, incident exercises, backup restoration results, vulnerability scans, remediation tickets, change approvals, physical-access records, inventories, and provider attestations.

### Gate result

- Current evidence supports design, implementation, and operation: continue.
- Documentation exists but operating evidence is missing: `NOT_PROVEN`.
- Evidence demonstrates control failure: `FAIL`.

## Gate 8: Obtain and preserve the authority decision

An internal assessment can reach `READY_FOR_AUTHORITY_REVIEW`. It cannot promote itself to `AUTHORITY_ACCEPTED`.

Capture:

- deciding authority and role;
- jurisdiction;
- system and version;
- architecture and deployment boundary;
- workloads and CJI categories;
- policy and supplement versions;
- agreements;
- accepted inherited controls;
- exceptions or conditions;
- open plans of action and milestones;
- effective date, expiration, and review triggers;
- evidence package identifier.

Use the [Authority Decision Record](../templates/AUTHORITY-DECISION.md).

### Gate result

- Written acceptance for the named boundary: `AUTHORITY_ACCEPTED`.
- Internal review complete but authority decision pending: `READY_FOR_AUTHORITY_REVIEW`.
- Authority requests remediation or rejects the boundary: `FAIL` or `NOT_PROVEN`, as directed.

## Gate 9: Keep the conclusion alive

Reassess when any of these changes:

- policy version or sanction status;
- state or local supplement;
- authorized purpose;
- CJI category;
- architecture, hosting region, or network path;
- identity provider or privileged-access model;
- cloud service model;
- provider, subprocessors, or support locations;
- encryption or key custody;
- logging, monitoring, or incident workflow;
- contract or agreement;
- material incident or control failure;
- evidence age beyond the defined cadence.

Until impact analysis is complete, the prior verdict is `STALE`.

Compliance is not a trophy. It is a maintained state.

## Final decision rule

The framework returns the lowest defensible state:

```text
prohibited or unmet requirement      -> FAIL
unknown fact or missing evidence     -> NOT_PROVEN
no CJI/supporting-system path        -> OUT_OF_SCOPE
all internal gates passed            -> READY_FOR_AUTHORITY_REVIEW
authority accepted named boundary    -> AUTHORITY_ACCEPTED
material change invalidated result   -> STALE
```

Never average a failed control into a passing score. Never convert missing evidence into partial credit. Never let a provider's marketing noun substitute for the authority's decision.
