# Control Family Guide

## How to use this guide

This guide tells you where to look and what evidence usually makes the requirement testable. Use the [v6.1 Control Index](CONTROL-INDEX.md) to locate base controls. Neither document replaces the official “shall” statements, control enhancements, parameters, priorities, sanction dates, or jurisdictional additions.

For every applicable requirement, capture design, implementation, operation, owner, evidence date, responsibility, gaps, and authority treatment.

## Policy Area 1: Information Exchange Agreements

Ask whether every exchange and service relationship is authorized, documented, monitored, and change-controlled. Evidence can include executed agreements, Security Addenda, service descriptions, incident obligations, change notices, oversight reviews, and data-flow mappings.

Failure mode: the technology is secured, but the parties never established the authority and control relationship that permits the exchange.

## The v6.1 families

| Family | What it is really asking | Representative evidence |
|---|---|---|
| AC — Access Control | Can only authorized identities reach only the CJI and functions they need, through approved paths? | Account inventory, role matrix, approvals, privilege reviews, remote/wireless/mobile configuration, access tests |
| AT — Awareness and Training | Do people understand and retain the responsibilities attached to their actual access? | Curricula, completion records, role-based training, exercises, overdue reports |
| AU — Audit and Accountability | Can the agency reconstruct who did what, when, where, to which data—and detect logging failure? | Event catalog, sample records, time synchronization, retention settings, access to logs, review and alert records |
| CA — Assessment, Authorization, and Monitoring | Has somebody independently tested controls, accepted risk, tracked gaps, and kept watching? | Assessment plan/results, authorization record, POA&M, monitoring strategy, connection approvals |
| CM — Configuration Management | Does the agency know what exists, what secure configuration means, and what changed? | Baselines, inventories, configuration exports, change approvals, impact analyses, software restrictions |
| CP — Contingency Planning | Can the service recover CJI safely and prove restoration actually works? | Contingency plan, training, exercise results, backup configuration, restoration evidence, alternate-site agreements |
| IA — Identification and Authentication | Can the system reliably bind a person/device/process to an identity and resist impersonation? | Identity-proofing records, authenticator configuration, MFA tests, device identity, reauthentication, ORI handling |
| IR — Incident Response | Can the organization detect, contain, report, recover, and coordinate before evidence disappears? | Response plan, contacts, reporting procedures, tickets, exercises, after-action reports, provider obligations |
| MA — Maintenance | Can maintenance occur without creating an undocumented access tunnel? | Maintenance authorization, tool controls, session records, remote maintenance protections, personnel approvals |
| MP — Media Protection | Does CJI remain controlled when copied, printed, transported, reused, or destroyed? | Media inventory, labels, storage controls, transport records, sanitization certificates, removable-media restrictions |
| PE — Physical and Environmental Protection | Can unauthorized people or environmental failure reach systems or CJI? | Facility designation, access lists, visitor logs, alarms, camera review, power/fire/water protections, delivery records |
| PL — Planning | Does the security plan describe the real system, real boundary, real behavior, and selected baseline? | System security plan, rules of behavior, architecture, baseline selection and tailoring, central-management plan |
| PS — Personnel Security | Are access decisions connected to role risk, screening, agreements, transfers, sanctions, and termination? | Position designations, screening confirmation, signed agreements, transfer/termination tickets, sanctions policy |
| RA — Risk Assessment | Does the organization know the value, exposure, vulnerabilities, and critical dependencies of the boundary? | Categorization, risk assessment, scan results, remediation decisions, criticality analysis, accepted risk |
| SA — System and Services Acquisition | Did contracts and engineering make security testable before the system arrived? | Acquisition language, requirements traceability, SDLC records, design reviews, developer testing, provider contracts |
| SC — System and Communications Protection | Are boundaries, sessions, shared resources, data in transit, data at rest, and keys protected? | Network diagrams, firewall rules, segmentation tests, encryption configuration, FIPS evidence, key custody and rotation |
| SI — System and Information Integrity | Can the system resist, detect, and repair flaws, malicious code, tampering, and invalid input? | Patch records, monitoring coverage, integrity checks, malware controls, advisories, retention configuration |
| SR — Supply Chain Risk Management | Does the agency understand and control the people and components upstream of the service? | Supplier inventory, SCRM plan, acquisition controls, notification terms, inspection records, disposal records |

## Evidence standard by family

For each family, answer:

1. What exact official requirement applies?
2. Who can perform the action: agency, provider, both, or CJIS/CSO?
3. Who remains accountable?
4. What policy or design establishes intent?
5. What configuration or process implements it?
6. What dated operating record proves it happened?
7. What failure or exception occurred?
8. How was the exception corrected or accepted?
9. When does the evidence expire or require refresh?
10. Has the relevant authority accepted the implementation or tailoring?

The control is not the screenshot. The screenshot is one witness.

## Cloud responsibility

The v6.1 Requirements Companion assigns capability by IaaS, PaaS, and SaaS using agency, provider, both, CJIS/CSO, or TBD categories. Treat that matrix as the beginning of responsibility analysis.

For every inherited or shared control, record:

- the provider service and deployment model;
- the provider artifact supporting the claim;
- the agency configuration still required;
- the contract term preserving evidence, notification, and access;
- any gap between provider capability and agency obligation;
- authority acceptance of the inheritance model.

The provider may run the control. The agency still owns the consequence.
