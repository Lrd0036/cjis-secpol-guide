# Sources

This directory contains source material used to build and verify the field guide. Source files are organized by issuing authority and policy version; their presence does not make every version simultaneously applicable.

## Layout

```text
sources/
  alabama/      Alabama administrative code, statutes, legislation, and ALEA forms
  fbi/
    v5.9/       historical policy retained for comparison
    v5.9.5/     current Texas audit baseline materials
    v6.1/       modernization and readiness materials
  texas/        Texas supplement, audit, forms, and reference charts
  contractor/   contractor addendum and onboarding references
  governance/   policy-governance forms
  manifests/    acquisition provenance, URLs, sizes, and hashes
```

Use [`RESEARCH-NOTES.md`](RESEARCH-NOTES.md) for evidence classes and maintenance rules. Use the [Alabama CJIS source manifest](manifests/alabama-cjis-sources.md) and [Texas DPS acquisition manifest](manifests/texas-dps-cjis-documents.md) to verify the state collections. The [local import manifest](manifests/local-imports.md) records source material whose original acquisition URL is not known.

## Source rules

- Pin every assessment to an explicit policy and jurisdictional baseline.
- Cite the exact source, version, section, and page used.
- Do not silently merge requirements from different policy versions.
- Treat summaries, indexes, and model output as navigation aids rather than governing authority.
- Preserve original files and verify hashes before regenerating derived data.
