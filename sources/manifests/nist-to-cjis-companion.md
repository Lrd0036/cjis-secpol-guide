# NIST-to-CJIS companion: source and coverage manifest

Review date: **2026-10-16**. This manifest supports the
[main guide](../../docs/FROM-NIST-TO-CJIS.md),
[migration appendix](../../docs/CJIS-6.0-TO-6.1-CHANGES.md), and
[fictional IR-6 example](../../examples/NIST-TO-CJIS-INCIDENT-REPORTING.md).
It is not a source inventory for a complete CJIS assessment.

## Authoritative sources and version pins

| ID | Source | Version used and role |
|---|---|---|
| C61 | [FBI CJIS Security Policy v6.1 PDF](https://le.fbi.gov/file-repository/cjis_security_policy_v6-1_20260625.pdf) | Cover: June 25, 2026; current explanatory target; 473 PDF pages |
| C60 | [FBI CJIS Security Policy v6.0 PDF](https://le.fbi.gov/file-repository/cjis_security_policy_v6-0_20241227.pdf) | Cover: December 27, 2024; historical change comparison |
| RC61 | [FBI Requirements Companion](https://le.fbi.gov/cjis-division/cjis-security-policy-resource-center/requirement-companion-document-pdf) | Cover: v6.1, June 25, 2026; introduction, PDF page 2, for sanction labels and cloud responsibility/accountability. Download filename/date must not replace cover version |
| N53 | [NIST SP 800-53 Rev. 5 publication record](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) and [published PDF](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf) | September 2020, updates December 10, 2020; readable control text/page locators and foundations. Publication record separately identifies August 27, 2025 Release 5.2.0 and warns against mapping equivalence |
| N53B | [NIST SP 800-53B publication record](https://csrc.nist.gov/pubs/sp/800/53/b/upd1/final) and [published PDF](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53B.pdf) | October 2020 (PDF cover), updates December 10, 2020; baseline/tailoring distinction. Publication record states Release 5.2.0 makes no baseline changes |
| N520 | [NIST-maintained OSCAL catalog JSON](https://raw.githubusercontent.com/usnistgov/oscal-content/main/nist.gov/SP800-53/rev5/json/NIST_SP-800-53_rev5_catalog.json) | Download metadata version 5.2.0, last-modified 2026-05-11T16:01:09.00000-00:00; selected current base-control statements and catalog ID inspection |
| FBI-RC | [FBI CJIS Security Policy Resource Center](https://le.fbi.gov/cjis-division/cjis-security-policy-resource-center) | Discovery and current-publication check; not a substitute for the pinned policy text |

### Acquired byte fingerprints

Downloaded on the review date. Hashes are SHA-256 of the original downloaded bytes,
not of extracted text. These URLs can change in place, especially the OSCAL `main`
URL. A different future hash means re-review is needed, not necessarily that the
new source is invalid. The downloaded PDFs/JSON are not newly vendored by this
contribution; the repository's existing source collection remains unchanged.

| Source | Bytes | SHA-256 |
|---|---:|---|
| C61 | 4443912 | `0e0f0f53db17f2b6408b2ce486fafb84acb0f628f68a794372ef4eb0c87ff4f8` |
| C60 | 4557967 | `fb580d9d110fd9ac512c026eb881eb900c4f0a43d93d481628ba9bbae45b9c77` |
| RC61 | 1534585 | `5c051b5a60a4d9273deaf676fd68f728864c9a5806dd69ee4043098093d7b975` |
| N53 PDF | 6073678 | `fc63bcd61715d0181dd8e85998b1e6201ae3515fc6626102101cab1841e11ec6` |
| N53B PDF | 1627293 | `8a9dae903c2e4924d7b67c246faa32757d15f9731abb85922fad63f9ea0e02fa` |
| N520 JSON | 10442037 | `01f37cf90ea99d92242c936cbfbdebcc338eef1f71454e2acac36cc56e9bc062` |

## Claim-to-source coverage

“Printed” means the document's own printed page label. CJIS v6.0/v6.1 numeric
body pages used here are 21 fewer than their one-based PDF viewer page number;
appendix labels do not follow that numeric rule. NIST original-PDF locators are
not pagination for the current OSCAL catalog.

| Topic | Reviewed primary locator | Extent/limit |
|---|---|---|
| Catalog, parameters, implementation approaches | N53 abstract and §2.2 printed pp.8–11; §2.3 pp.11–13 | Foundations; no complete catalog or baseline inventory |
| Baselines and tailoring | N53B §2.1 and publication abstract | Low/moderate/high security and separate privacy baseline distinction |
| Catalog release/mapping caution | N53 publication record; N520 metadata | Current-release notice and caution that mappings do not establish equivalence |
| CJIS scope and additional protections | C61 §§1.2–1.3 p.1; §3.2.1 p.5 | Organizational/support scope and more stringent/additional local protections |
| Sanction/zero-cycle distinction | C61 §1.4 pp.1–2; RC61 introduction PDF p.2 | Does not establish any particular jurisdiction's current audit decision |
| AU-6 | C61 p.50; N53 p.70; N520 `au-6` statement/parameters | Selected base-control cadence/recipient comparison |
| IA-0 | C61 p.92; N520 control identifier inspection | CJIS-specific ORI obligation; AC-3/AU-3 association is explicitly analytical, not official equivalence |
| IR-6 | C61 p.171; N53 p.157; N520 `ir-6` statement/parameters | Base clauses (a)–(b); enhancements acknowledged but not fully assessed |
| PS-3 | C61 pp.206–207, heading p.205; N53 p.223; N520 `ps-3` statement/parameters | Screening/authority exceptions and rescreening qualifier; not individualized access advice |
| SA-9 | C61 pp.228–229, heading p.227; N53 p.271; N520 `sa-9` statement/parameters | Applicable agreements and oversight; not full outsourcing-standard analysis |
| SC-13 | C61 p.243; N53 pp.308–309; N520 `sc-13` statement/parameters | Transit alternatives, floor, pending-module note, and certificate date; not all encryption requirements |
| Cloud accountability | RC61 introduction PDF p.2 | Official matrix semantics; guide's allocation table is illustrative, not a transcription of matrix rows |
| AT-3 migration | C60/C61 p.40, PDF p.61 | New cross-agency training acceptance note only |
| CM-12 migration | C60/C61 p.78, PDF p.99 | Clauses (b)–(c) clarified to include transmission; (a) already did |
| IR-6 migration | C60/C61 p.171, PDF p.192 | Recipient/confirmation change; unchanged internal clock |
| SA-15 migration | C60/C61 p.233, PDF p.254 | Criticality Analysis enhancement identifier (1) → (3), reviewed control body unchanged |
| SC-13 migration | C60/C61 p.243, PDF p.264 | Transit key floor 128 → 256; certificate date unchanged |
| SC-28 migration | C60/C61 p.246, PDF p.267 | Module branch 128 → 256; FIPS 197 branch already 256; continuation requires separate reading |
| SI-2(2) migration | C60/C61 p.252, PDF p.273 | Quarterly → monthly routine scanning; incident trigger unchanged |
| Fictional evidence record | C61 IR-6 p.171; N53/N520 IR-6; repository evidence/verdict framework | All scenario facts and artifacts are invented and visibly labeled; no real system assessed |

## Verification method and reproducibility

1. Open official publication records and verify cover/version information rather
   than inferring it from a URL or download filename.
2. Download source bytes and compare SHA-256/byte length with the table above.
3. Extract PDF text with a layout-preserving reader (for example, `pdftotext -layout`)
   and inspect the full cited control, notes, exceptions, and printed page labels.
   Retain original PDFs for visual checks when text extraction is ambiguous.
4. For current NIST checks, parse `catalog.metadata` and locate the specified control
   IDs under `catalog.groups[].controls`, including nested controls when needed.
   Compare statement parts and parameters. This review does not claim all 5.2.0
   discussions, references, enhancements, or assessment procedures match the old PDF.
5. Compare each migration row in both actual policy texts. Do not call a reflow,
   heading renumber, or unchanged sunset a new requirement.
6. Run `python -m unittest discover -s tests -v` and `git diff --check` from the
   repository root. Tests check structure and navigation, not legal correctness,
   complete coverage, live URL availability, or operational compliance.

## Exclusions and maintenance

No exhaustive control crosswalk or machine-generated compliance decision is shipped.
No actual vendor, deployment, cryptographic certificate, authority approval, or
state-specific audit baseline was validated. Those require a separate scoped review.
The FBI's separately linked implementation/use-case materials were not relied on as
current v6.1 normative requirements here.

When sources change, review the affected claims and examples together. Preserve
historical version pins and add a new review date; do not silently replace the
normative source behind an existing assessment. Update hashes only after inspecting
the changed source. Missing source access or conflicting authority instructions
must remain visible, not be filled with an assumed NIST equivalence.
