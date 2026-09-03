# Assessments

Create one directory per real decision:

```text
assessments/
  YYYY-MM-DD-agency-system-jurisdiction/
    ASSESSMENT.md
    AUTHORITY-DECISION.md
    controls/
      AC-2.md
      AU-3.md
      ...
    FINDINGS.md
```

Start by copying:

- [`templates/SYSTEM-ASSESSMENT.md`](../templates/SYSTEM-ASSESSMENT.md)
- [`templates/CONTROL-EVIDENCE.md`](../templates/CONTROL-EVIDENCE.md)
- [`templates/AUTHORITY-DECISION.md`](../templates/AUTHORITY-DECISION.md)

## Evidence handling

Do not commit CJI, CHRI, PII, credentials, private agreements, personnel screening results, sensitive architecture, unrestricted audit records, or other protected evidence merely to make the repository feel complete.

Assessment records should point to the authorized evidence repository using stable artifact identifiers. Store only sanitized material approved for this repository.

The index should say what was reviewed, by whom, when, for which boundary, and where the authorized copy lives.

Evidence is useful only if preserving it does not create the incident the control was supposed to prevent.

## Required status

Every assessment directory must state one repository verdict:

- `OUT_OF_SCOPE`
- `FAIL`
- `NOT_PROVEN`
- `READY_FOR_AUTHORITY_REVIEW`
- `AUTHORITY_ACCEPTED`
- `STALE`

Never leave an abandoned assessment looking current. Mark it `STALE` and explain the trigger.
