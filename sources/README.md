# Sources

This directory contains source material used to build and verify the field guide. Source files are organized by issuing authority and policy version; their presence does not make every version simultaneously applicable.

## Layout

```text
sources/
  alabama/      Alabama administrative code, statutes, legislation, and ALEA forms
  california/   Revision-specific CLETS policies, practices, and procedures
  fbi/
    v5.9/       historical policy retained for comparison
    v5.9.5/     current Texas audit baseline materials
    v6.1/       modernization and readiness materials
  illinois/     LEADS rules, bulletins, statutes, state technology policies and local agreements
  texas/        Texas DPS materials, statutes, procurement rules, local policies and dated sources
  contractor/   contractor addendum and onboarding references
  governance/   policy-governance forms
  manifests/    acquisition provenance, URLs, sizes, and hashes
```

Use [`RESEARCH-NOTES.md`](RESEARCH-NOTES.md) for evidence classes and maintenance rules. The [November Alabama source register](manifests/alabama-2026-11-19.md) covers all 12 published Commission chapters, all three divisions of Article 23, related statutes, records schedules and state IT policies. See the [September Alabama collection](manifests/alabama-cjis-sources.md) for the earlier versions and forms. The [November Texas source register](manifests/texas-2026-11-19.md) covers the current Texas collection and identifies the system-access chart that supersedes the one in the [September DPS manifest](manifests/texas-dps-cjis-documents.md). The [Illinois source register](manifests/illinois-2026-11-19.md) covers LEADS, DoIT, the Bureau of Identification, state statutes and local authorities. The [local import manifest](manifests/local-imports.md) records source material whose original acquisition URL is not known.

The [state search pilot](../data/state-search-pilot.json) records official URLs, snapshot hashes and provision locators for the [Alabama guide](../docs/states/ALABAMA.md), the [Illinois guide](../docs/states/ILLINOIS.md), the [Texas guide](../docs/states/TEXAS.md), the October 2026 California CLETS manual and selected Michigan State Police guidance.

## Source rules

- Pin every assessment to an explicit policy and jurisdictional baseline.
- Cite the exact source, version, section, and page used.
- Do not silently merge requirements from different policy versions.
- Treat summaries, indexes, and model output as navigation aids rather than governing authority.
- Preserve original files and verify hashes before regenerating derived data.
