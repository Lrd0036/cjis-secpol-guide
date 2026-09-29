---
name: is-this-cji
description: Determine whether a specific record, field, file, image, audio/video item, API response, dataset, log, AI output, or data flow is CJI, CHRI, CJI-derived PII, exempt transaction information, authorized public information, or unresolved. Use for questions such as Is this CJI, does CJIS apply to this data, and can this data be treated as public. Classify by provenance, content, transformations, release authority, and jurisdiction; do not equate all police data or all PII with CJI. Hand system compliance questions to cjis-compliance-audit.
license: Apache-2.0
compatibility: Requires this complete cjis-secpol-guide checkout, an approved evidence-reading environment, and access to applicable policy and jurisdictional sources. Repository-relative dependencies must remain available.
---

# Is this CJI?

Answer for a named item, copy, or data flow. Distinguish data classification,
required handling, and the scope of the system that handles it. They are separate
questions. This skill supplies Gate 3 of the existing compliance framework; it
does not grant dissemination permission or certify a product.

## Load the classification sources

Resolve paths from this skill's real directory, not the current working directory.
The repository root is `../../..`. Read:

- [Agent operating rules](../../../docs/AGENT-SKILLS.md).
- [Field Guide](../../../docs/CJIS-FIELD-GUIDE.md).
- [Version and Authority](../../../docs/VERSION-AND-AUTHORITY.md).
- Gate 3 of the [Compliance Framework](../../../docs/COMPLIANCE-FRAMEWORK.md).
- [Classification rules and source locators](references/classification-rules.md).
- The new [CJI Classification Record](../../../templates/CJI-CLASSIFICATION.md).

Then read the exact applicable official sections. The reference file is a decision
aid, not a substitute for the policy. For the repository's v6.1 baseline, start
with Sections 4.1, 4.1.1, 4.2, and 4.3. Use the governing version's own wording
for other baselines and check applicable jurisdictional requirements.
If a source is inaccessible, name it and state the resulting limitation; do not
pretend to have read it or silently classify an uncertain item as unprotected.

## 1. Establish safe inputs and the classification unit

Start with descriptions, redacted schemas, synthetic examples, and provenance
records. Before inspecting actual potentially protected content, establish that
the environment and access are approved. Do not ask the user to paste a real rap
sheet, biometric record, or unredacted case file into an unapproved chat or tool.
Do not send samples to public search, external classifiers, or unapproved models.

Use available evidence first. Ask only questions that could change the result:

- What exact item/copy/fields are being classified, at what lifecycle stage?
- Where did each field originate, and through what system or exchange?
- Was it enriched, joined, transcribed, summarized, redacted, or derived?
- Which agency/jurisdiction and applicable policy govern it?
- What authorized purpose, recipients, or documented public-release basis apply?

A missing jurisdiction can leave handling unresolved without preventing a clear
positive CJI classification for a verified FBI CJIS response. Conversely, absence
of known FBI provenance does not prove an item is outside all applicable rules.
Do not guess an agency or jurisdiction from geography, branding, or the user.

## 2. Trace provenance and content

Classify fields and records before aggregating the container. Record the producing
system, record type, route, joins/derivatives, storage location, and evidence ID.
Distinguish verified provenance, user assertions, and inference.

Inspect for the governing policy's biometric, identity-history, biographic,
property-with-PII, and case/incident-history categories. Determine whether CHRI
is present and whether restricted-file rules require CHRI protection; preserve
that distinction rather than assuming every CJI record is CHRI.

A local incident report, public tip, jail roster, body-camera clip, crash video,
or employee contact list is not automatically FBI CJIS-provided data merely
because a law-enforcement agency holds it. Trace its source and applicable
state/local definitions, agreements, and any enrichment from CJIS systems.
Unresolved provenance or an unresolved material overlay yields `UNDETERMINED`,
not a categorical yes or no based on the filename.

For mixed inputs, report each component. Known CJI means the mixed container
contains CJI even when other components are unresolved. A clean field does not
clear the entire response, file, database, application, or support workflow.

## 3. Evaluate exceptions and transformations

Apply the detailed [classification rules](references/classification-rules.md).
For every asserted exception, require the cited rule and evidence that its
conditions hold for this specific copy or flow.

- **Transaction identifiers:** verify the type and that accompanying context does
  not reveal CJI or PII. Do not generalize the exception to any ID, arbitrary hash,
  linkable case number, or record carrying a name or case facts.
- **Authorized public information:** verify the actual dissemination authority or
  the policy's applicable judicial-proceeding/public-record condition. Internet
  availability, a public bucket, a leaked record, or the word non-restricted does
  not establish authorized release. Limit the exception to the qualifying copy;
  internal enriched records and source-system access remain separate.
- **PII extracted from CJI:** identify official-business purpose and applicable
  agency/state/local controls under Section 4.3. Neither treat it as unrestricted
  nor automatically assert every CJI auditing, logging, and personnel requirement.
  If remaining case/history information is still CJI, classify that content as CJI.
- **Encryption, redaction, and AI:** encryption changes protection, not provenance.
  Removing names, hashing, embeddings, a transcript, or a summary does not by
  itself establish an exclusion. Inspect retained facts, linkage, reversibility,
  surrounding context, and applicable authority treatment. Mark uncertainty rather
  than inventing a universal rule that every derivative is or is not CJI.

Distinguish an exception established by the policy from a discretionary authority
approval. Do not invent a requirement for a new approval where the governing rule
already supplies the exception; do require evidence that the conditions are met.

## 4. Record the classification and remaining restrictions

Use these **data dispositions**, which are not system-compliance verdicts:

| Disposition | Use only when |
|---|---|
| `CJI` | Evidence establishes protected CJI in the named item/copy; identify categories and any CHRI/restricted-file treatment. |
| `CJI_DERIVED_PII` | The item is PII extracted from CJI and the analysis specifically concerns Section 4.3 handling; identify any unresolved local obligations. |
| `EXEMPT_TRANSACTION_IDENTIFIER` | The applicable transaction-control-number exception and absence of revealing accompanying information are established. |
| `AUTHORIZED_PUBLIC_INFORMATION` | The applicable authorized-dissemination or judicial-public-record conditions are established for the named information/copy. |
| `NOT_CJI` | Affirmative provenance/content and applicable scope rules support exclusion for the named item; other privacy, contractual, or legal restrictions can remain. |
| `UNDETERMINED` | A material source, lineage, context, exception condition, or authority interpretation remains unresolved. |

For each row also report:

- CJI category and provenance, including original CJI lineage where an exception applies.
- CHRI present: `YES`, `NO`, or `UNDETERMINED`; separately, CHRI protection required
  by a restricted-file rule: `YES`, `NO`, or `UNDETERMINED`.
- Applicable handling, use/dissemination constraints, and state/local overlays.
- Official source/version/section/page, item evidence ID, reasoning, and missing facts.

Use `NO` only when supported, never as a default for an unexamined field. Excluded
or public information is not a license for arbitrary reuse. For unresolved
material, recommend protective handling pending determination as a precaution;
make clear that precaution is not a final legal classification.

## 5. Explain system scope and hand off

Answer the literal question first, in ordinary language:

> [Yes / no for this specifically qualified copy / unresolved / CJI-derived PII
> requiring a separate handling determination], because [decisive provenance and
> rule]. This applies to [item/copy/date], not automatically to [broader system].

Return the Classification Record, or its equivalent fields inline for a small
question. Include per-item rows, the overall container conclusion, exclusions,
unknowns, handling action, and the narrow questions needed for a firmer result.

Then record the system implication separately:

- CJI processing, transmission, viewing, support, administration, logs, backups,
  keys, or recovery access can put a system path in scope without persistent storage.
- An exempt/public/non-CJI item does not establish that its producer, hosting
  environment, integrations, or privileged identities are out of scope.
- Where the user asks about the system, hand the inventory and uncertainties to
  [cjis-compliance-audit](../cjis-compliance-audit/SKILL.md). Its Gate 3 result is
  `NOT_PROVEN` while the material boundary remains unresolved. `OUT_OF_SCOPE`
  requires affirmative evidence of no CJI or supporting-system/access path.

Keep classification and system verdict separate; do not label a CJI item `FAIL`
or a public record `AUTHORITY_ACCEPTED`. Never manufacture an authority decision.
Only save sanitized output to an approved destination when requested, following
[assessment handling rules](../../../assessments/README.md).

Before returning, check: no blanket all-police-data/all-PII rule, no public-equals-
authorized assumption, no encryption-equals-exclusion shortcut, no unsupported
PII-derived control claim, no data-to-system scope leap, and no protected content
included merely to demonstrate that it is protected.
