# Worked example: reuse a NIST IR-6 package without hiding CJIS gaps

**All organizations, artifacts, timestamps, and results below are fictional.** This
is a targeted demonstration of the [Control Evidence Record](../templates/CONTROL-EVIDENCE.md),
not a real assessment, an authority decision, or evidence that a system is compliant.
Do not perform real external incident notifications merely to reproduce this example.

## Claim and requirement

Example agency: Juniper City Police. Example service: CaseBridge SaaS, tenant JC-01.
Boundary: agency users and help desk, the provider's on-call response path, the agency's
incident coordinator, and the agency-approved authority notification workflow.
Assessment target: CJIS v6.1 **IR-6(a)–(b) only**, printed p.171. Current jurisdictional
audit baseline and transition treatment are **unverified in this fictional exercise**.
This is a readiness comparison, not a finding of present sanctionability.

NIST starting point: SP 800-53 Rev. 5 IR-6, published PDF p.157 and current 5.2.0 base
statement. The source control leaves time period and reporting authorities to
organization-defined parameters. The existing fictional NIST package chose a
24-hour suspected-incident internal reporting interval and the enterprise response
team as recipient. [N53; N520]

CJIS target: personnel report suspected incidents immediately, no later than one
hour after discovery, to the organizational incident-response capability. The
external/authority chain is separately specified in IR-6(b), including the FBI CJIS
ISO. Source IDs resolve in the [manifest](../sources/manifests/nist-to-cjis-companion.md).

IR-6(1), IR-6(3), the rest of IR, contracts, and the complete system are **not assessed**
by this example. A real full assessment must determine their applicability and test them.

## First pass: identify exactly what can be reused

| Artifact | Reusable evidence | Missing or conflicting element |
|---|---|---|
| E-01: existing incident policy, rev.2 | Named internal response function and suspected-incident trigger | Its 24-hour interval conflicts with the v6.1 target |
| E-02: SaaS response-plan excerpt | Provider on-call function and escalation interface | It only promises notice after confirmation and omits the agency's authority chain |
| E-03: last quarter's internal exercise report | Evidence that a tested employee reached the enterprise response team | Different tenant/workflow; no CJIS authority route tested |
| E-04: draft agency contact matrix | Proposed agency coordinator and CSO route | Draft lacks verified FBI CJIS ISO route and authority approval of routing details |

**Initial targeted result:** `FAIL` against the v6.1 readiness target because E-01
contains an affirmative reporting-interval mismatch. Unverified external routing
is also `NOT_PROVEN`; it does not erase the known mismatch. This is not a conclusion
that the agency is currently sanctionable. The governing audit baseline is unknown.

## Design record after remediation

Fictional remediation changes E-01 to rev.3: personnel report suspected incidents
immediately to the organizational capability, with the one-hour maximum preserved.
The revised provider-to-agency workflow removes confirmation as a prerequisite to
escalation. E-04 rev.2 identifies the agency-authorized notification roles and
verified destinations covering IR-6(b), including the FBI CJIS ISO. The agency owns
external authority notification in this fictional allocation; the provider supplies
its contracted detection and escalation evidence. Another deployment may allocate
this differently.

- Design evidence: E-01 rev.3, E-02 revised agreed escalation annex, E-04 rev.2.
- Design test: trace suspected incident through each role and recipient; inspect
  after-hours and no-acknowledgment fallback instructions.
- Design result: `PASS` **for these reviewed base clauses in this fictional record**.
- Limits: this is not approval of a complete incident plan, a contract, or all IR controls.

The use of paging, acknowledgments, fallback contacts, and specific artifacts is an
implementation suggestion. The authoritative requirement is the policy clause.

## Implementation record

In a safe test environment mirroring the scoped tenant's notification configuration,
the reviewer inspects the deployed route export and compares it with E-04 rev.2.
The reviewer verifies the primary and fallback internal destinations and checks
that external messages can be prepared through the approved workflow without waiting
for confirmation. All test messages go only to prearranged test endpoints.

- Evidence: E-05 route export with tenant, configuration version, capture time, and
  reviewer; E-06 controlled test delivery records; E-07 approved mapping from test
  endpoints to the verified operational destinations.
- Implementation result: `PASS` for the inspected configuration and tested path.
- Limits: a test endpoint is not proof of delivery to an actual authority; a mirrored
  environment is not proof that production is identically configured. A real review
  needs an authorized production configuration reconciliation before claiming that.

Because production equivalence is not verified here, **production implementation
remains `NOT_PROVEN`**. The narrower test result must not be substituted for it.

## Operation record and sampling

Fictional exercise EX-04, October 8, 2026, UTC:

| Time | Observed event | What it supports |
|---|---|---|
| 14:02 | Participant recognizes a suspected incident and records discovery | Start of observed internal reporting clock |
| 14:04 | Organizational response endpoint receives participant's report | This sample reports promptly and inside the one-hour maximum |
| 14:05 | On-call acknowledgment recorded | Tested internal response handoff; acknowledgment is supporting evidence, not a separately invented IR-6(a) deadline |
| 14:09 | Agency coordinator prepares approved test notifications for incident-handling personnel and authority routes | Exercise coverage of named recipient workflow |
| 14:10 | Test endpoints receive those notifications | Delivery within the controlled exercise, not actual notification of authorities |

Sample: one weekday exercise in one tenant, deliberately no real CJI. No real-incident
population, after-hours exercise, unavailable-primary exercise, or production delivery
records were supplied. The sampled timing worked; **sustained production operation
remains `NOT_PROVEN`**. This record does not invent a sample size that proves universal
compliance or a one-hour external deadline.

## Closure decision

The original 24-hour design mismatch has a documented correction in the reviewed
fictional revisions. The targeted v6.1 production result remains **`NOT_PROVEN`**
because production configuration and sustained operation have not been established.
It is not `READY_FOR_AUTHORITY_REVIEW`: the review excludes the rest of IR and the
whole-system requirement population. No authority acceptance is claimed.

Next evidence needed:

1. Authorized production-to-approved-route reconciliation, including the provider
   interface and current authority contact verification.
2. Dated operating evidence over the agreed period, with the incident population
   and justified sample; exercise records for untested failure paths.
3. Applicable audit baseline/transition instructions and separate evaluation of
   IR-6 enhancements and remaining requirements.

Store only sanitized artifact identifiers in a shareable result. Retain contact
rosters, actual incidents, logs, and contractual evidence in authorized repositories.
