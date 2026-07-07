# CAPP-0007 Stable Release Decision

> Status: accepted decision - Date: 2026-07-07

## Decision

CAPP-0007 is accepted. CAP-Core v1.0.0 stable may be published with release
artifact `release-artifacts/cap-core-v1.0.0/` and tag `cap-core-v1.0.0`.

## Evidence

- Stable scope: `specs/core/STABLE-SCOPE-v1.0.md`
- Stable conformance: `specs/core/CONFORMANCE-v1.0.md`
- Schema package: `specs/core/SCHEMA-PACKAGE-v1.0.md`
- Fixture suite: `specs/core/FIXTURES-v1.0.md`
- Validator registry: `specs/core/VALIDATOR-CODES-v1.0.md`
- Security requirements: `specs/core/SECURITY-v1.0.md`
- Policy/service boundary: `specs/core/POLICY-SERVICE-v1.0.md`
- RunEvidence boundary: `specs/core/RUN-EVIDENCE-v1.0.md`
- Bridge boundary: `specs/core/CAP-DIGEST-BRIDGE-v1.0.md`
- Registry snapshot: `specs/core/PROFILE-BINDING-REGISTRY-v1.0.md`
- RC review: `specs/core/reviews/2026-07-07-rc1-review.md`

## Blocking Objections

No unresolved P0 or P1 blockers are recorded.

## Compatibility

CAP-Core v1.0.0 freezes the minimal Core object contract and report formats
listed in the stable scope. CAP-Digest behavior is unchanged.
