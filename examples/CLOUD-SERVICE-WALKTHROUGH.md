# Worked Example: Proposed Cloud Records Service

This example is fictional. It demonstrates the reasoning structure, not an assessment of a real vendor.

## The claim

> Can Example County Sheriff's Office use Vendor Cloud Records, SaaS edition 4.2, to store case and incident CJI in State X as of September 2, 2026?

The vendor says the service is “CJIS compliant.”

Excellent. That gives us a claim to test.

It does not give us an answer.

## Gate results

| Gate | Evidence | Result |
|---|---|---|
| Jurisdiction and authority | State X is named, but the CSA, CSO, and acceptance process are not documented. | `NOT_PROVEN` |
| Version | Vendor materials cite v5.9.5. The jurisdiction's current audit baseline and v6.1 transition instructions are unknown. | `NOT_PROVEN` |
| CJI boundary | Primary database and backups are described. Support tooling, telemetry, and recovery administration are omitted. | `NOT_PROVEN` |
| Purpose and agreements | Law-enforcement case management is a stated purpose. Required agreements and Security Addendum status are unknown. | `NOT_PROVEN` |
| People | Customer user roles are documented. Provider privileged personnel and subprocessors are not. | `NOT_PROVEN` |
| Controls | Vendor supplies a general security white paper and an unrelated compliance report. Customer configuration and v6.1 control applicability are not mapped. | `NOT_PROVEN` |
| Operation | No recent access review, log sample, incident exercise, restoration result, or vulnerability-remediation evidence is available. | `NOT_PROVEN` |
| Authority decision | No written State X decision covers this edition, architecture, or workload. | `NOT_PROVEN` |

## Verdict

`NOT_PROVEN`

The service has not been shown to fail a specific requirement in this fictional record. It has also not been shown to satisfy the complete relationship.

That distinction matters.

“Not proven” is not polite language for “probably fine.” It is the accurate answer when the evidence stops before the claim does.

## What would move the decision

1. Confirm the State X authority and audit/version profile.
2. Complete the CJI lifecycle and administrative-access boundary.
3. Identify required agreements and execute the applicable Security Addendum.
4. Resolve provider personnel, subprocessor, region, and key-custody access.
5. Map official requirements and responsibility across agency and SaaS provider.
6. Collect current design, implementation, and operating evidence.
7. Remediate or formally track gaps.
8. Submit the named boundary for authority review.

Only the eighth step can produce `AUTHORITY_ACCEPTED`.

The vendor can help build the evidence package. The vendor cannot appoint itself State X.
