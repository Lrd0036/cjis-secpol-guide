# Texas DPS CJIS Document Manifest

Source page: <https://www.dps.texas.gov/section/crime-records/cjis-documents>

Downloaded: 2026-09-02

The repository contains every downloadable policy, companion, form, chart, and contractor-reference document linked from the source page on the download date. Files are organized by issuing authority and purpose. SHA-256 hashes identify the exact retrieved files.

| Repository path | Type | Pages | Bytes | SHA-256 | Source URL |
|---|---:|---:|---:|---|---|
| `sources/fbi/v5.9.5/cjis-security-policy-v5.9.5.pdf` | PDF | 451 | 4,496,128 | `55649eb943033495695223855b7ba487d3a3446b6bcc0f597cf6682785560821` | <https://www.dps.texas.gov/sites/default/files/documents/securityreview/documents/cjisSecurityPolicy_v5-9-5.pdf> |
| `sources/fbi/v5.9.5/requirements-companion-v5.9.5.pdf` | PDF | 80 | 1,482,813 | `f23b9daaf03655ee2ce65342e0d3e5427e2cb68d0f4ee0e1dba93ee3383396b0` | <https://www.dps.texas.gov/sites/default/files/documents/securityreview/documents/RequirementCompanionDoc_v5-9-5.pdf> |
| `sources/fbi/v5.9.5/requirements-companion-v5.9.5.xlsx` | XLSX | - | 536,529 | `c8b1a644be05200b48e562ba5f1fb5eaf6d0203e3a24749d32ff52cb554a5736` | <https://www.dps.texas.gov/sites/default/files/documents/securityreview/documents/RequirementCompanionDoc_v5-9-5.xlsx> |
| `sources/fbi/v6.1/cjis-security-policy-v6.1.pdf` | PDF | 473 | 4,513,659 | `b9e40ee0f506c7d8bca6e2ae04dc0d87b5d00b162bb9c5cc48529517a724abfb` | <https://www.dps.texas.gov/sites/default/files/documents/securityreview/documents/cjisSecurityPolicy_v6-1.pdf> |
| `sources/fbi/v6.1/requirements-companion-v6.1.pdf` | PDF | 86 | 1,535,000 | `09e05733e591a7e6a6ad7ac05cd26a4b5989913eb371697e50872102afb762aa` | <https://www.dps.texas.gov/sites/default/files/documents/securityreview/documents/RequirementCompanionDoc_v6-1.pdf> |
| `sources/fbi/v6.1/requirements-companion-v6.1.xlsx` | XLSX | - | 505,872 | `4dae974a2e59cef42903229ae34cda27a4388b39c67a978b05924c9537c09dc0` | <https://www.dps.texas.gov/sites/default/files/documents/securityreview/documents/RequirementCompanionDoc_v6-1.xlsx> |
| `sources/contractor/fbi-security-addendum.pdf` | PDF | 8 | 425,337 | `62470660d88645916eb0d98232fa07647aee7da474428c85470489428b9ddcb1` | <https://www.dps.texas.gov/sites/default/files/documents/securityreview/documents/fbiSecurityAddendum.pdf> |
| `sources/texas/texas-cjis-security-policy-supplement.pdf` | PDF | 1 | 207,190 | `253ebaeacec50cf48b8353cd5f6f9e8551dfb6dfa16a982ee74aedba6e806cdd` | <https://www.dps.texas.gov/SecurityReview/TexasCJISSecurityPolicy.pdf> |
| `sources/texas/audit/technical-audit-v5.9.5.pdf` | PDF | 68 | 397,983 | `24a7e2553cd8a1f628cf0865f61ae98108a213011a2335ae38e89ce1571ac649` | <https://www.dps.texas.gov/sites/default/files/documents/securityreview/documents/cjis_technical_audit_5.9.5_v2.pdf> |
| `sources/texas/forms/incident-response-form.docx` | DOCX | - | 150,483 | `69e5685e8ecd249aec3da38889f18cc40089253e16ddaf6328e67d85c8f8a560` | <https://www.dps.texas.gov/sites/default/files/documents/securityreview/documents/incidentResponseForm.docx> |
| `sources/texas/reference/system-access-chart.pdf` | PDF | 1 | 294,124 | `6a63b3f9ac8b2e9aa50e8a2b1bbb451bbd0efb0418d91c84c547bd4097212abd` | <https://www.dps.texas.gov/sites/default/files/documents/administration/crime_records/docs/txcjissysaccpolicy.pdf> |
| `sources/governance/apb-topic-request-form.pdf` | PDF | 1 | 10,040 | `73fad1ade896f9ad49b169486af3890f26de3e814024388f21093d73521e2849` | <https://www.dps.texas.gov/SecurityReview/apbTopicPaperRqstForm.pdf> |
| `sources/contractor/ncic-2000-manual-reference.pdf` | PDF | 15 | 44,276 | `57b155243ab8a4e17f3d544cef36451f5edf2d3330335199125eab3746a8ebe4` | <https://www.dps.texas.gov/SecurityReview/ContractorEmpRefDocNCIC2000Manual.pdf> |
| `sources/contractor/texas-government-code-reference.pdf` | PDF | 3 | 12,714 | `c2d2aaf7de91910f107926271b2c7e7c484c41e2d6fdabe85906cbd83eee7979` | <https://www.dps.texas.gov/SecurityReview/ContractorEmpRefDocTxGovCode.pdf> |

## External authority reference

The source page also links to the live eCFR presentation of 28 CFR Part 20: <https://www.ecfr.gov/current/title-28/chapter-I/part-20>. It is not a Texas DPS downloadable document and is therefore not frozen in this directory.

## Verification

- Every downloaded PDF was recognized as a PDF and opened successfully with `pdfinfo`.
- Both XLSX files and the DOCX form passed ZIP container integrity checks.
- The manifest excludes unrelated PDFs linked by the site header or footer.
