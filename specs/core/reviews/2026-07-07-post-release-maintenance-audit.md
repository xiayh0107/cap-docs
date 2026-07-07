# CAP-Core v1.0.x Post-Release Maintenance Audit

> Status: completed audit - Date: 2026-07-07

This record closes the initial post-release maintenance pass for issues #88,
#89, #90, and #91. It does not publish a CAP-Core v1.0.x patch release and does
not change CAP-Core v1.0.0 semantics.

## #88 Errata and Patch Release

Finding: no open errata issue or review record identifies a CAP-Core v1.0.0
semantic, schema, fixture, report, or security defect that requires a v1.0.x
patch release.

Disposition: defer the next CAP-Core patch release. A future v1.0.x release
requires a concrete erratum recorded in `CHANGELOG.md`, a release note, and
evidence tied to `specs/core/MAINTENANCE-v1.0.md`.

## #89 External L4 Feedback

Finding: the initial post-release feedback window is closed with no external
implementation report received. GitHub code and issue searches on 2026-07-07
for `cap.core.interop_report.v1`, `CAP-Core v1.0.0`, and related issue text
found only this repository's own files and issues.

Disposition: do not claim ecosystem-level L4 interoperability. The v1.0.0
release keeps only the reference report, the independent structural L0-L2
adapter report, and the packaged L4 comparison report as release evidence.
Future external reports should open new issues and cite
`specs/core/INTEROPERABILITY-HARNESS.md`.

## #90 Scope Boundary Audit

Finding: current status, roadmap, release, and stable Core documents keep the
CAP-Core v1.0.0 stability claim limited to the minimal control-plane object
contract, schemas, fixtures, reports, and maintenance policy.

Guardrails remain active:

- CAP-Core v1.0.0 does not define runtime execution.
- CAP-Core v1.0.0 does not define policy language semantics.
- CAP-Core v1.0.0 does not define credential exchange.
- CAP-Core v1.0.0 does not prove scientific correctness.
- CAP-Core v1.0.0 does not change or stabilize CAP-Digest behavior.

Disposition: boundary wording is audited for the initial maintenance pass.
Future runtime, policy, credential, scientific, or Digest behavior changes must
use a separate profile or a future CAPP.

## #91 CAP-Digest Stable Route

Finding: CAP-Digest remains an alpha draft profile after CAP-Core v1.0.0.
CAP-Digest stable work now has a separate tracker, #92, and a separate stable
planning note at `specs/digest/STABLE-TRACK.md`.

Disposition: keep Digest stable planning independent from CAP-Core v1.0.x
maintenance. Do not use CAP-Core v1.0.0 release evidence as CAP-Digest stable
evidence.
