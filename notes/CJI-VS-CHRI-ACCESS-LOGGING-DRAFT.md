# CJI, CHRI, Access, and Logging

**Status:** Research draft. The claims below require reconciliation against the applicable CJIS policy version, 28 CFR Part 20, relevant CJIS system manuals, the Texas supplement, and authority guidance before operational use.

## Working distinction

Criminal Justice Information (CJI) is the broader policy category. Criminal History Record Information (CHRI) is a sensitive subset with additional access, use, dissemination, and recordkeeping rules.

That distinction can change the controls applied to the same technical system. The system must therefore classify the information being handled rather than treating every CJIS-related record as interchangeable.

## Questions to verify

### Access and authorized use

- Which CJI categories does the system create, receive, display, transmit, store, or support?
- Does any path contain CHRI or information treated as CHRI under the applicable source?
- Which purposes, recipients, and dissemination paths are authorized?
- Which NCIC files or services introduce additional restrictions?

### Logging and secondary dissemination

- Which transactions require secondary-dissemination records?
- What identifying fields must be captured for III or other applicable queries?
- Which control states the requirement in v5.9.5, and where did that requirement move in v6.1?
- How are the operator, receiving agency, requestor, recipient, purpose, and transaction linked without placing unnecessary CJI in the audit system?

### Contractors and vendors

- Does the contractor have direct access, indirect access, administrative capability, or only a demonstrably excluded support path?
- Which agreement, Security Addendum, screening, training, and audit requirements apply?
- What evidence establishes the first-receipt date and subsequent audit cadence?

### Scope exclusions

- Which standalone transaction identifiers are excluded, and under exactly what conditions?
- Does PII extracted from CJI retain CJIS handling obligations under the governing version or jurisdiction?
- Has the authority accepted the classification, or is the conclusion merely inferred?

## Promotion rule

Move a claim from this note into durable guidance only after recording:

1. the exact governing source and version;
2. the section, page, and quoted requirement;
3. the Texas or other jurisdictional overlay;
4. the operational consequence; and
5. any unresolved authority question.

Until then, this document is a question set. Not a control baseline.
