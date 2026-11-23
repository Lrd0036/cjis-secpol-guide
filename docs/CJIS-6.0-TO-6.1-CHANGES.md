# CJIS v6.0 to v6.1: verified migration notes

This is a **verified subset**, not a complete release diff or a new baseline.
It compares the official FBI v6.0 policy dated December 27, 2024 [C60] with v6.1
dated June 25, 2026 [C61], reviewed October 16, 2026. Source IDs and downloaded-file
hashes are in the [companion manifest](../sources/manifests/nist-to-cjis-companion.md).
The [main companion](FROM-NIST-TO-CJIS.md) explains how to reconcile NIST evidence.

The v6.1 Summary of Changes (printed p.iii) identifies the 2025 APB Parts 1–3 and
administrative changes. It is not a detailed control-by-control migration table.
The rows below were verified against the actual text in both policy PDFs. The
printed page labels happen to match in both versions for these rows; that does not
mean the text stayed unchanged.

## Selected substantive changes and one identifier correction

The first three columns summarize source text. The final column is suggested
implementation/evidence work, not additional policy.

| Locator in both policies | v6.0 | v6.1 | Suggested migration check |
|---|---|---|---|
| AT-3, p.40 | No note permitting acceptance of another agency's role-based training documentation at this location | Adds CSO/SIB Chief discretion to accept that documentation; accepting agency assumes risk that training does not meet a particular applicable legal/process requirement | Record the actual acceptance and check local training gaps; do not treat any external completion certificate as automatically accepted |
| CM-12(b)–(c), p.78 | (b) identifies users with access to the system/components where information is processed and stored; (c) records changes in those locations | (b) expressly addresses access to CJI and components where CJI is processed, stored, or transmitted; (c) expressly includes transmitted CJI | Reconcile transmission paths, users, and change records as well as storage inventory; (a) already included transmission in v6.0 |
| IR-6(b), p.171 | Authority notification follows an “if confirmed” qualifier; FBI CJIS ISO is not listed in this clause | Removes that qualifier and adds FBI CJIS ISO to the recipient chain | Update escalation logic and contacts; do not retain a confirmation gate from the old runbook |
| SA-15 enhancement, p.233 | Criticality Analysis labeled (1) | Same reviewed control body labeled (3) | Re-key references and evidence links; do not manufacture a new technical requirement from this identifier correction |
| SC-13(b), p.243 | In-transit symmetric-key floor is 128 bits | Floor becomes 256 bits | Inspect actual deployed transport cryptography and validation evidence, including termination points and fallback configurations |
| SC-28, p.246 | FIPS 140-3 module branch has 128-bit floor; FIPS 197 branch already has 256-bit floor | Both stated branches have 256-bit floor | Identify whether any at-rest deployment relied on the old 128-bit module branch; preserve the stated outside-physically-secure-location scope and read the continuation/notes on p.247 |
| SI-2(2), p.252 | Automated flaw-remediation status uses vulnerability scanning at least quarterly or following relevant security incidents | Routine cadence becomes at least monthly; incident trigger remains | Update schedules, coverage and completion monitoring; test that incident-triggered scans remain in the workflow |

## Important items that did not newly appear in v6.1

- **IR-6(a)'s internal clock:** immediate reporting of suspected incidents to the
  organizational incident-response capability, no later than one hour after discovery,
  is present in both versions (p.171). The changed recipient/confirmation text is in (b).
  Do not describe the one-hour ceiling as a new v6.1 requirement or as an independently
  stated deadline for every external recipient.
- **SC-13's FIPS 140-2 date:** the note saying certificates are not acceptable after
  September 21, 2026 is in both versions (p.243). It is not an added v6.1 sunset.
  The date is already past as of this review; check current implementation evidence
  and applicable authority treatment rather than treating it as a future task.
- **SC-28's FIPS 197 branch:** its 256-bit floor already exists in v6.0 (p.246).
  Reporting that both branches changed from 128 to 256 bits would be inaccurate.

## Publication, implementation, and sanction treatment are different fields

CJIS v6.1 §1.4 (pp.1–2) identifies a zero-cycle of October 1, 2024 through September
30, 2027 for modernized Priority 2, 3, and 4 controls, while pre-modernization existing
requirements and Priority 1 requirements remain sanctionable. Do not collapse a
mixed **[Existing] [Priority 2]** heading into a blanket deferred or non-applicable
control. Use the Requirements Companion's requirement-level audit/sanction entries
and obtain the applicable authority's treatment for the exact requirement. [C61; RC61]

For each migration item, retain:

1. Old and new requirement text/locator, and whether the change is substantive,
   an identifier correction, or unchanged context.
2. Current applicable audit baseline, readiness baseline, and verified authority
   transition instructions. A state's date is not a national date.
3. Affected deployment/configuration/procedure and the evidence to re-test.
4. Owner, gap, remediation, and any actual written authority decision or accepted
   treatment. A planned ticket does not by itself satisfy a requirement.

Do not overwrite an old assessment's version or verdict in place. Preserve the
historical conclusion and identify what must be re-evaluated under the new version.
Use the repository's [version profile](VERSION-AND-AUTHORITY.md) and
[verdict rule](COMPLIANCE-FRAMEWORK.md#final-decision-rule).
