# CAP-Core Candidate Normative Readiness Report

> Status: candidate-prep decision record - Non-normative - Date: 2026-07-07

This report evaluates CAPP-0005 and Phase 8 tracker #30. It does not promote
CAP-Core; it records whether the repository is ready for candidate normative
review.

## Recommendation

Recommendation: enter candidate normative review with the current review
package, while keeping all Core assets draft-track until a future CAPP accepts
promotion. No stable CAP-Core release should be tagged from this report alone.

## Gate Evaluation

| Gate | Status | Evidence |
|---|---|---|
| L0-L4 conformance levels | Pass | `specs/core/CONFORMANCE-DRAFT.md` |
| Schema versioning and compatibility | Pass | `specs/core/VERSIONING-AND-COMPATIBILITY.md` |
| Eight minimal object schemas covered | Pass | `schemas/core/`, `specs/core/SCHEMA-CANDIDATE-RULES.md`, `fixtures/core/negative/` |
| Non-local service fixture without secrets | Pass | `fixtures/core/remote-service-binding/` |
| Stable machine-readable validator report | Pass | `schemas/core/cap.core.conformance_report.v1.schema.json`, generated report package |
| Stable human-readable inspection report | Pass | `specs/core/INSPECTION-REPORT.md`, `cap.core.inspection_report.v1` |
| Security, privacy, and trust review | Pass | `specs/core/SECURITY-PRIVACY-TRUST.md`, `specs/core/SECRET-SERVICE-BINDING-SAFETY.md` |
| Blocking open questions triaged | Pass | `specs/core/OPEN-QUESTIONS.md` |
| Independent implementation evidence | Pass for candidate entry | Reference report plus external interoperability harness in `specs/core/INTEROPERABILITY-HARNESS.md`; second implementation report remains future evidence. |
| Profile and binding governance | Pass | `specs/core/PROFILE-AND-BINDING-REGISTRY.md`, `specs/core/PROFILE-GOVERNANCE.md` |
| CAP-Digest bridge boundary | Pass | `specs/core/RFC-0004-cap-digest-bridge-profile.md`, bridge fixture and negative tests |
| Terminology collision audit | Pass | `specs/core/TERMINOLOGY-COLLISION-AUDIT.md` |

## Schema Status

The Core schema sketches now cover ArtifactSet, Artifact/ArtifactRef,
Capability, Binding, Assembly, PolicyDecision, Run, RunEvidence, conformance
report, inspection report, interop report, interop comparison, and negative
fixture harness records. Required fields and enums are schema-backed where the
draft object shape is stable enough for review.

## Fixture and Validator Status

Positive fixtures cover local analysis, software build/test, and remote service
binding. The systematic negative suite currently contains 18 cases covering
object identity, reference closure, binding roles, policy, secret handling, run
lifecycle records, Digest bridge separation, and RunEvidence overclaims.

The reference validator emits stable error codes and an L4-target report in
`release-artifacts/core-candidate-review/reports/core-conformance-report.json`.

## Security Status

Security review is explicit for fail-closed policy behavior, opaque secret
references, prohibited inline secret values, remote service freshness and
network declaration, and RunEvidence limitations. Remaining verification of
real signatures, SBOMs, provenance graphs, remote correctness, and credential
exchange is external or profile-owned.

## Profile and Binding Status

Scientific computation and CAP-Digest bridge profiles remain draft profile
proposals. The registry draft lists candidate external binding families and
keeps external standard semantics outside minimal Core.

## Interoperability Status

The repository has a report format, a reference report generator, an external
command wrapper, and a comparison script. This satisfies the CAPP-0005
alternative of reference implementation plus external harness. A second
implementation report would strengthen L4 evidence but is not required before
opening candidate normative review.

## Blockers and Non-Blockers

Blockers: none recorded for entering candidate normative review.

Non-blockers:

- no second independent implementation report yet;
- no runtime execution semantics;
- no policy language semantics;
- no proof of scientific correctness;
- no CAP-Digest behavior changes.

## Final Decision

Date: 2026-07-07.

Decision: ready to enter candidate normative review, not ready to publish a
stable CAP-Core release, and not promoted by this report.
