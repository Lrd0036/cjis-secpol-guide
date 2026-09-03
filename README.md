# CJIS Security Policy Field Guide

This repository is a practical decision system for one deceptively short question:

> Is this CJIS compliant?

The honest answer is never a context-free product badge. It is a scoped conclusion about a named system, data flow, agency, jurisdiction, policy version, body of evidence, and authority decision.

That sounds less convenient than a checkbox.

It is also how the system actually works.

## Start here

1. Read [CJIS, Without the Fog](docs/CJIS-FIELD-GUIDE.md) once. It establishes the nouns and authority model.
2. Use the [Compliance Framework](CJIS-COMPLIANCE-FRAMEWORK.md) to understand the gates and verdicts.
3. Copy the [System Assessment](templates/SYSTEM-ASSESSMENT.md) for the system, service, or vendor being evaluated.
4. Work through the [Control Family Guide](docs/CONTROL-FAMILIES.md), use the [v6.1 Control Index](docs/CONTROL-INDEX.md) to find the base control, and attach evidence using the [Control Evidence Record](templates/CONTROL-EVIDENCE.md).
5. For third parties, complete the [Vendor Questionnaire](templates/VENDOR-QUESTIONNAIRE.md).
6. Record the applicable authority's conclusion in the [Authority Decision Record](templates/AUTHORITY-DECISION.md).
7. Store the sanitized decision record under [assessments](assessments/README.md), with protected evidence kept in its authorized repository.

If you have five minutes, use the [Quick Decision Guide](docs/QUICK-DECISION-GUIDE.md).

If you want to see the verdict logic in motion, read the [fictional cloud-service walkthrough](examples/CLOUD-SERVICE-WALKTHROUGH.md).

## The answer vocabulary

This repository uses six verdicts:

| Verdict | Meaning |
|---|---|
| `OUT_OF_SCOPE` | The documented boundary does not process, store, transmit, or provide access to CJI. |
| `FAIL` | An applicable requirement is unmet or a prohibited condition exists. |
| `NOT_PROVEN` | The claim may be true, but current evidence does not establish it. |
| `READY_FOR_AUTHORITY_REVIEW` | Internal assessment found no known blocking gap; authority acceptance is still pending. |
| `AUTHORITY_ACCEPTED` | The applicable CJIS authority accepted the named boundary under stated conditions and date. |
| `STALE` | The prior conclusion can no longer be relied on because the system, evidence, jurisdiction, or policy changed. |

`READY_FOR_AUTHORITY_REVIEW` is not a synonym for compliant.

`AUTHORITY_ACCEPTED` is not transferable to every customer, state, workload, or future version.

## Current policy boundary

The research baseline in this repository is FBI CJIS Security Policy **v6.1**, dated June 25, 2026. The v6.1 policy distinguishes existing and Priority 1 sanctionable controls from Priority 2-4 controls in a zero-cycle ending September 30, 2027.

But.

The policy published most recently is not automatically the audit baseline used by every jurisdiction today. For example, Texas DPS states that Texas audits continue against v5.9.5 through March 31, 2027 while agencies prepare for v6.1. Your assessment must record both:

- the policy version used for the current authority or audit decision; and
- the newer version used for readiness planning.

See [Version and Authority](docs/VERSION-AND-AUTHORITY.md).

## What this repository can establish

It can establish that:

- scope and assumptions were recorded;
- requirements were evaluated;
- evidence was collected and reviewed;
- gaps and inherited responsibilities were made visible;
- a named authority decision was captured.

It cannot grant access to CJI, interpret a state's private operational manuals, bind a CSA or CSO, or manufacture FBI certification where none was issued.

## Source discipline

FBI CJIS policy, federal regulation, Compact Council rules, applicable state policy, agreements, and the relevant CJIS authority govern the conclusion. O'Reilly research is used for supporting practices in GRC, RMF, auditing, cloud responsibility, identity, incident response, and third-party risk. It does not create CJIS requirements.

See [Research Notes and Sources](sources/RESEARCH-NOTES.md).

## Disclaimer

This is an unofficial educational and assessment aid. It is not legal advice, an FBI interpretation, an audit result, a grant of access, or a substitute for the applicable CSA, CSO, CSA ISO, Compact Officer, or other authorized official.
