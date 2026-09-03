# CJIS, Without the Fog

*A plain-language field note on the system, the policy, the data, and the people who can tell you no.*

## The short answer

CJIS is not a security framework.

Well. Not exactly.

**CJIS** is the FBI's Criminal Justice Information Services Division. The division operates and supports national criminal-justice information services. **The CJIS Security Policy** is the minimum security policy for people, agencies, contractors, and systems that access or support Criminal Justice Information. **CJI** is the information being protected. State and federal CJIS authorities decide how access and compliance work inside their jurisdictions.

Those are four different things.

People collapse them into one acronym, then wonder why every conversation sounds like three government agencies arguing through a trench coat.

So, the useful model is:

```text
CJIS Division
    operates criminal-justice information services
        that provide or exchange CJI
            protected by the CJIS Security Policy
                implemented and enforced through federal, state, and local authority
```

That is CJIS.

Not a checkbox. A chain of custody with computers attached.

## First: CJIS is an actual FBI division

The FBI did not begin with a cloud-compliance program. It began collecting fingerprints nationally in 1924. As criminal records and information-sharing systems grew, the machinery around those records grew with them. In 1992, the FBI established the CJIS Division from the former Identification Division and consolidated major information services around it.

That history explains the current shape.

CJIS exists because a patrol officer in one jurisdiction, a court in another, and an authorized background-checking agency somewhere else may need trustworthy information about the same person, fingerprint, firearm, warrant, incident, or criminal history. The data must move. The source must remain intelligible. The recipient must be authorized. The use must be lawful.

And someone has to be accountable when any part of that sentence fails.

So CJIS is not merely a database. The CJIS Division is the institutional hub behind a set of criminal-justice information services, including systems and programs such as NCIC, fingerprint and identity services, crime reporting, and other national information exchanges.

## Second: CJI is the thing everyone is trying to protect

**Criminal Justice Information (CJI)** is the broad category. It covers FBI CJIS-provided data needed by law-enforcement and authorized civil agencies to perform their missions. Depending on the system and use, that can include biometric data, identity information, biographic data, property data, case or incident information, and criminal-history information.

**Criminal History Record Information (CHRI)** is a narrower category inside that world. Federal regulation defines CHRI around identifiable descriptions of a person plus records of arrests, detentions, formal charges, and the dispositions that follow—acquittal, sentencing, supervision, release, and so on.

So:

```text
CJI = broad protected criminal-justice information category
CHRI = criminal-history information with specific legal use and dissemination rules
```

Why does that distinction matter?

Because data classification changes what an agency may do with the information, why it may access the information, who may receive it, what must be logged, and which laws and agreements apply. A system cannot protect “CJIS data” as one undifferentiated blob and call the problem solved. The system has to know what the data is and preserve the authorized purpose around it.

The database does not grant the right to use the record. Authority does.

## Third: the CJIS Security Policy is the floor

The CJIS Security Policy governs the protection of CJI across its lifecycle: creation, viewing, modification, transmission, dissemination, storage, and destruction. It applies to the people and organizations that access CJI and to those that operate systems supporting criminal-justice services and information.

Version 6 modernized the policy into a NIST-like control structure. That makes portions of it look familiar to anyone who has worked with NIST SP 800-53: access control, audit and accountability, identification and authentication, incident response, configuration management, personnel security, physical protection, system integrity, and so forth.

Familiar does not mean interchangeable.

CJIS adds its own institutional machinery:

- information-exchange agreements;
- purpose and dissemination restrictions;
- fingerprint-based personnel screening in applicable circumstances;
- security awareness and role-based training;
- local and state CJIS roles;
- contractor oversight and the CJIS Security Addendum;
- audits, implementation deadlines, and possible sanctions;
- state and local requirements that may exceed the federal minimum.

As of June 25, 2026, the official FBI Requirements Companion tracks **CJIS Security Policy v6.1**. It also shows an important operational distinction: some requirements are already sanctionable, while some modernized controls remain in a “zero-cycle” implementation period. In other words, “the control appears in the document” and “the control is currently sanctionable in an audit” are related claims. They are not the same claim.

Read the requirement. Read its status. Ask the authority.

## Fourth: CJIS compliance is distributed authority

Here is where the usual compliance mental model breaks.

There is no single federal product badge in the CJIS Security Policy that makes a vendor universally “CJIS certified.” The policy establishes requirements, agreements, oversight, audits, and accountable officials. A vendor can provide evidence, implement controls, sign required agreements, support agency audits, and satisfy a customer's CJIS authority. None of that turns “CJIS compliant” into a context-free property of a logo.

The authority chain matters:

```text
FBI Director / CJIS Advisory Process
    approves policy direction

FBI CJIS Information Security Officer
    maintains and distributes the policy
    provides implementation guidance

CJIS Systems Agency (CSA)
    serves the state, territory, tribe, federal agency, or equivalent jurisdiction

CJIS Systems Officer (CSO)
    administers the CJIS network for the CSA
    approves access and enforces standards in that jurisdiction

Agency security and operational roles
    implement controls, document systems, train people, report incidents

Agency and contractor
    operate the actual people, process, and technology boundary
```

The names of agency-level roles can vary under v6.1's broader language, but the accountability does not disappear. The CSO retains jurisdictional authority. The agency remains ultimately accountable for compliance, including when it uses a cloud provider.

Yes, even if the cloud provider has a very impressive compliance webpage.

The FBI v6.1 Requirements Companion includes a cloud responsibility matrix for IaaS, PaaS, and SaaS. It identifies whether the agency, provider, CJIS authority, or a combination of them has the technical ability to perform an action. The matrix still states that the agency is ultimately accountable.

That is the hidden mechanism behind CJIS procurement: outsourcing capability does not outsource responsibility.

## What “CJIS compliant” should actually mean

A defensible CJIS claim needs a complete sentence.

Not:

> Product X is CJIS compliant.

But something closer to:

> Agency A has accepted System X, operated under Agreement Y, for Workload Z and Data Category D, based on the controls and evidence reviewed by the applicable CJIS authority as of Date T.

That sentence is uglier.

It is also real.

The scope changes if the data changes. The scope changes if a contractor can see unencrypted CJI. The scope changes if administrators operate from a different location. The scope changes if a service provider changes a subcontractor, support path, encryption boundary, identity system, or incident-response process. The scope changes across jurisdictions because local policy may raise the floor.

Compliance is not a sticker on the server.

It is a maintained relationship among **data, purpose, people, systems, agreements, evidence, and authority**.

## What this means for builders and vendors

If you are building a system that may touch CJI, start with the boundary—not the control spreadsheet.

1. **Name the data.** Is it CJI? Is it CHRI? Is it information derived from CJI? What classification and use restrictions follow it?
2. **Name the purpose.** Why is the agency allowed to access and use the information?
3. **Name the people.** Who can view it, administer the system, recover backups, inspect logs, or support the service?
4. **Name the systems.** Where is CJI processed, stored, transmitted, backed up, logged, cached, and destroyed?
5. **Name the agreements.** Which user agreement, information-exchange agreement, management-control agreement, contract, or Security Addendum governs the relationship?
6. **Name the authority.** Which CSA, CSO, CSA ISO, Compact Officer, or agency security official can interpret and accept the implementation?
7. **Name the evidence.** What proves the control works in this environment—not merely that a policy says it should?
8. **Name the version and status.** Which CJIS Security Policy version applies, and which controls are sanctionable on the relevant date?

Only then does the technical work become honest: identity, least privilege, encryption, key management, audit records, personnel screening, training, incident response, media protection, physical security, vulnerability management, configuration control, and recovery.

If you start with the spreadsheet, you will eventually rediscover the boundary.

Usually during an audit.

Which is a very expensive way to learn vocabulary.

## The one-sentence model

**CJIS is the trust system that lets authorized institutions share criminal-justice information without surrendering control of who may use it, why they may use it, and who answers when the protection fails.**

The policy supplies the floor.

The agreements define the relationship.

The controls protect the information.

The agency owns the consequence.

There it is.

## Research boundary and sources

This note was researched on September 2, 2026. The O'Reilly Learning catalog search returned no CJIS-specific title among the results reviewed. The most relevant O'Reilly results were background sources on governance, cloud security, and digital forensics. They help explain the neighboring disciplines; they do **not** establish CJIS requirements. FBI and federal regulatory sources control the CJIS-specific claims in this note.

### Governing and primary sources

- [FBI Criminal Justice Information Services](https://www.fbi.gov/services/cjis) — division history, mission, and programs.
- [FBI CJIS Security Policy Resource Center](https://le.fbi.gov/cjis-division/cjis-security-policy-resource-center) — current policy resources and implementation materials.
- [FBI Requirements Companion Document for CJIS Security Policy v6.1](https://le.fbi.gov/cjis-division/cjis-security-policy-resource-center/requirement-companion-document-pdf) — current requirements, responsibility assignments, priorities, and audit/sanction status as of June 25, 2026.
- [FBI CJIS Security Policy appendices](https://le.fbi.gov/cjis-division/cjis-security-policy-resource-center/appendicies) — official definitions, agreements, roles, Security Addendum material, and implementation guidance.
- [28 CFR § 20.3](https://www.law.cornell.edu/cfr/text/28/20.3) — federal definitions, including CHRI.
- [28 CFR § 20.33](https://www.law.cornell.edu/cfr/text/28/20.33) — authorized dissemination and use of federal criminal-history records.

### O'Reilly background sources returned by the catalog search

- Jason Edwards and Griffin Weaver, [*The Cybersecurity Guide to Governance, Risk, and Compliance*](https://learning.oreilly.com/library/view/-/9781394250196/?orm_source=mcp) — GRC operating context.
- Lei Chen, Hassan Takabi, and Nhien-An Le-Khac, [*Security, Privacy, and Digital Forensics in the Cloud*](https://learning.oreilly.com/library/view/-/9781119053286/?orm_source=mcp) — cloud security, privacy, and forensic context.
- Michael Shannon, [*AWS Cloud Security*](https://learning.oreilly.com/videos/-/9780135174784/?orm_source=mcp) — cloud-control implementation context.
- Yvonne Wilson and Abhishek Hingnikar, [*Solving Identity Management in Modern Applications*](https://learning.oreilly.com/library/view/-/9781484282618/?orm_source=mcp) — identity and access-management context.

## Disclaimer

This is an unofficial educational explanation, not an FBI interpretation, legal opinion, audit determination, or authorization to access CJI. Confirm system-specific and jurisdiction-specific requirements with the applicable CJIS authority.
