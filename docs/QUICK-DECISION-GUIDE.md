# Quick Decision Guide

Use this when somebody asks for a fast answer. Fast does not mean fictional.

## 1. What exactly is being assessed?

Write one sentence naming the organization, system/version, workload, deployment, jurisdiction, data, and date.

If you cannot: `NOT_PROVEN`.

## 2. Can the boundary touch CJI?

Include viewing, transmitting, administration, logs, backups, support tickets, exports, and subcontractor access.

- Proven no: `OUT_OF_SCOPE`.
- Yes: continue.
- Unknown: `NOT_PROVEN`.

## 3. Who has authority?

Name the CSA/CSO or applicable federal, tribal, territorial, or state authority and the agency owner.

- Unknown: `NOT_PROVEN`.
- Named: continue.

## 4. Which rules apply today?

Name the audit baseline, current policy, state/local supplements, agreements, and future controls being tracked.

- Unknown or borrowed from another jurisdiction: `NOT_PROVEN`.
- Confirmed: continue.

## 5. Is the purpose authorized and is the relationship documented?

Check information-exchange and user agreements, contracts, Security Addendum, management control, outsourcing approval, and CHRI dissemination rules as applicable.

- Required authority or agreement absent: `FAIL`.
- Applicability unknown: `NOT_PROVEN`.
- Verified: continue.

## 6. Are all people and machine identities controlled?

Check authorization, screening, agreements, training, least privilege, authentication, periodic review, transfer, termination, provider access, and subprocessors.

- Required control absent: `FAIL`.
- Provider path unknown: `NOT_PROVEN`.
- Verified: continue.

## 7. Are applicable controls implemented and operating?

Assess the official requirements—not merely this summary—across information exchange and every applicable control family. Verify design, implementation, and recent operation.

- Unmet requirement: `FAIL`.
- Missing evidence: `NOT_PROVEN`.
- Internally supported: continue.

## 8. Has the applicable authority accepted this exact boundary?

- No: `READY_FOR_AUTHORITY_REVIEW` at best.
- Yes, in writing, with current scope and conditions: `AUTHORITY_ACCEPTED`.
- Yes, but the system or governing facts changed: `STALE`.

## The sentence to give leadership

> As of [date], [system/version] is [verdict] for [agency/workload/data/jurisdiction] under [policy baseline], based on [evidence package], subject to [conditions]. The deciding authority is [name/role], and the next review trigger is [date/change].

Anything shorter is marketing copy.
