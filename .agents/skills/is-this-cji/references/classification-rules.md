# Classification rules and source locators

This is an operational reading guide for `is-this-cji`, not a new policy or a
complete statement of dissemination law. Verify the actual source on each run.
The v6.1 locators below were checked against the FBI-hosted June 25, 2026 policy
on September 28, 2026. They must not be silently reused for another version.

## Read in this order

| Question | Repository source | Locator in v6.1 |
|---|---|---|
| What does the policy cover? | [FBI policy](../../../../sources/fbi/v6.1/cjis-security-policy-v6.1.pdf) | Section 1.3; Section 4.1; Section 5 |
| Which categories and exceptions apply? | Same policy | Section 4.1, printed p. 10 / PDF page 31 |
| Is it CHRI or protected as CHRI? | Same policy | Sections 4.1.1 and 4.2.1-4.2.2, printed pp. 10-11 / PDF pages 31-32 |
| Does non-restricted mean publicly reusable? | Same policy | Sections 4.2.3-4.2.5, printed pp. 11-12 / PDF pages 32-33 |
| What about PII extracted from CJI? | Same policy | Section 4.3, printed pp. 12-13 / PDF pages 33-34 |
| Which other laws/manuals apply? | [Primary source register](../../../../sources/RESEARCH-NOTES.md) | 28 CFR Part 20, applicable Compact rules, system manuals, and agreements |
| Which jurisdictional material is available? | [Source collection](../../../../sources/README.md) | Applicable state collection and its acquisition manifest |

PDF pages above are **one-based viewer pages**, not zero-based indices. Confirm
page labels in the actual file; cite both when useful. If its bytes or pagination
differ, use the page actually read rather than copying this locator blindly.

Official verification entry points:

- [FBI Security Policy Resource Center](https://le.fbi.gov/cjis-division/cjis-security-policy-resource-center)
- [FBI-hosted v6.1 policy](https://le.fbi.gov/file-repository/cjis_security_policy_v6-1_20260625-1.pdf)
- [28 CFR Part 20](https://www.ecfr.gov/current/title-28/chapter-I/part-20), especially Sections 20.3 and 20.33; check applicability before using a dissemination rule.

## Decision rules

### Provenance comes before a keyword match

Section 4.1 describes FBI CJIS-provided data and its categories. A field's name
alone does not establish its origin or the governing jurisdictional scope. A
name and date of birth in an ordinary HR roster and the same fields in a CJIS
response do not acquire identical provenance just because they look alike.

Inspect local records for applicable state/local rules, agreements, and CJIS
content added through a query, attachment, or join. A local-source record can
require protection under other authorities. Do not convert lack of FBI lineage
into permission to publish it. This is the application of the repository's
boundary and authority model, not an additional blanket federal definition.

### CJI and CHRI are different determinations

Read Sections 4.1.1 and 4.2 and the applicable regulatory definition. Verified III
information receives CHRI treatment. NCIC restricted-file information must be
protected as CHRI under Section 4.2.2; record that handling rule separately from
a claim that every such record satisfies a particular legal CHRI definition.
Use the governing version's actual file list. Do not memorize an old list.

NCIC non-restricted data remains subject to access/use/dissemination rules.
Non-restricted is not the same as public, unprotected, or commercially reusable.
A response can contain restricted and non-restricted portions; review both.

### Transaction-control-number exemption is conditional

Section 4.1 gives examples such as ORI, NIC, and UCN when not accompanied by
information revealing CJI or PII. Establish what the artifact actually contains,
including adjacent fields, URL parameters, attachments, and available joins.
Do not declare every identifier exempt or every standalone qualifying identifier
protected merely because it originated in a CJIS transaction.

### Public information requires the policy's release conditions

Section 4.1 distinguishes protection of CJI from information released through
authorized dissemination and addresses qualifying judicial-proceeding records
that can be released through a public-records request. Verify the applicable
condition and the named copy. Do not assume all court records qualify: sealed,
restricted, or unreleasable material requires separate treatment.

A public URL or an accidental disclosure is not evidence of authorized release.
Likewise, a lawful public extract does not declassify an internal enriched
record or its source system. Preserve the lineage and classify those separately.

### Extracted PII has its own handling question

Section 4.3 limits extraction to official business and calls for agency policies
based on state/local privacy rules. It does not supply a blanket set of auditing,
logging, and personnel-security requirements for the entire PII lifecycle.

Use `CJI_DERIVED_PII` to retain this provenance and flag the handling determination.
Do not use it to launder remaining criminal-history or incident content into a
less protected class. Do not claim either that extracted PII is freely reusable
or that every CJI control automatically follows every extracted PII field.

### Derivatives need evidence, not a new exemption

For redactions, transcripts, screenshots, summaries, hashes, embeddings, exports,
and aggregates, inspect which protected facts and linkages remain. Encryption
alone does not remove the underlying classification. A model's summary can retain
CJI; a synthetic example can be independent of actual CJI. Verify the facts.

Where the source does not explicitly resolve the transformation, label the
conclusion as an inference or unresolved authority question. Protective handling
pending review is a recommendation, not a newly invented FBI rule about AI.

## Small worked examples (fictional)

| Input and established facts | Expected disposition | Important limit |
|---|---|---|
| Verified III response with identity and arrest/disposition history, no qualifying release | `CJI`; CHRI present `YES` | A training purpose does not itself authorize sending it to a model. |
| Qualifying transaction identifier, verified to stand alone with no revealing context | `EXEMPT_TRANSACTION_IDENTIFIER` | Does not exclude the system that issued it. |
| The same identifier accompanied by a named person's nonpublic case information from CJIS | `CJI` | The standalone exception is not satisfied. |
| Exact agency extract with documented authorized public dissemination | `AUTHORIZED_PUBLIC_INFORMATION` for that copy | The nonpublic enriched source remains separately classified. |
| A CJIS-derived response accidentally exposed in a public bucket | `CJI` | Exposure is not authorized dissemination. |
| Local crash video or public tip, source and applicable state treatment not established | `UNDETERMINED` | Do not equate all evidence held by police with FBI CJI. |
| Name/contact fields extracted from CJI for official business, remaining item is PII only | `CJI_DERIVED_PII` | Determine local handling; do not invent federal PII lifecycle controls. |
| Approved synthetic test fixture with independently verified no-CJI provenance and no applicable scope overlay | `NOT_CJI` | Hosting/support paths still need separate scoping. |

For broader adversarial and audit scenarios, use the
[skill evaluation cases](../../../../tests/skill_cases.json). These are fictional
acceptance cases, not actual agency determinations or evidence.
