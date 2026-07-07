# CAP-Core Candidate Review Manifest

> Status: candidate-prep draft - Non-normative - Last updated: 2026-07-07

## Governance

- `capps/CAPP-0005-cap-core-candidate-normative-track.md`
- `capps/CAPP-0006-cap-core-candidate-normative-review-entry.md`
- `ROADMAP.md`
- `STATUS.md`
- `CHANGELOG.md`

## Core Drafts and Review Docs

- `specs/core/00-status-and-roadmap.md`
- `specs/core/NORMATIVE-LANGUAGE.md`
- `specs/core/RFC-0001.md`
- `specs/core/RFC-0001-core-object-model.md`
- `specs/core/RFC-0002-binding-model.md`
- `specs/core/RFC-0003-scientific-computation-profile.md`
- `specs/core/RFC-0004-cap-digest-bridge-profile.md`
- `specs/core/SCHEMA-CANDIDATE-RULES.md`
- `specs/core/CONFORMANCE-DRAFT.md`
- `specs/core/VERSIONING-AND-COMPATIBILITY.md`
- `specs/core/SECURITY-PRIVACY-TRUST.md`
- `specs/core/SECRET-SERVICE-BINDING-SAFETY.md`
- `specs/core/INSPECTION-REPORT.md`
- `specs/core/INTEROPERABILITY-HARNESS.md`
- `specs/core/PROFILE-AND-BINDING-REGISTRY.md`
- `specs/core/PROFILE-GOVERNANCE.md`
- `specs/core/TERMINOLOGY-COLLISION-AUDIT.md`
- `specs/core/IMPLEMENTATION-GUIDE.md`
- `specs/core/OPEN-QUESTIONS.md`

## Schemas

- `schemas/core/cap.core.artifact_set.v1.schema.json`
- `schemas/core/cap.core.artifact.v1.schema.json`
- `schemas/core/cap.core.capability.v1.schema.json`
- `schemas/core/cap.core.binding.v1.schema.json`
- `schemas/core/cap.core.assembly.v1.schema.json`
- `schemas/core/cap.core.policy_decision.v1.schema.json`
- `schemas/core/cap.core.run.v1.schema.json`
- `schemas/core/cap.core.run_evidence.v1.schema.json`
- `schemas/core/cap.core.conformance_report.v1.schema.json`
- `schemas/core/cap.core.inspection_report.v1.schema.json`
- `schemas/core/cap.core.interop_report.v1.schema.json`
- `schemas/core/cap.core.interop_comparison.v1.schema.json`
- `schemas/core/cap.core.negative_case.v1.schema.json`
- `schemas/core/cap.core.negative_suite_expected.v1.schema.json`

## Fixtures

- `fixtures/core/local-analysis/README.md`
- `fixtures/core/local-analysis/source-artifacts.json`
- `fixtures/core/local-analysis/capability.json`
- `fixtures/core/local-analysis/assembly.json`
- `fixtures/core/local-analysis/policy-decision.json`
- `fixtures/core/local-analysis/run.json`
- `fixtures/core/local-analysis/run-evidence.json`
- `fixtures/core/local-analysis/digest-view-ref.json`
- `fixtures/core/local-analysis/expected-validation.json`
- `fixtures/core/local-analysis/expected-review-summary.txt`
- `fixtures/core/local-analysis/negative/digest-evidence-as-run-evidence.json`
- `fixtures/core/local-analysis/negative/run-without-assembly.json`
- `fixtures/core/local-analysis/negative/secret-value-in-service-binding.json`
- `fixtures/core/build-test/README.md`
- `fixtures/core/build-test/source-artifacts.json`
- `fixtures/core/build-test/capability.json`
- `fixtures/core/build-test/assembly.json`
- `fixtures/core/build-test/policy-decision.json`
- `fixtures/core/build-test/run.json`
- `fixtures/core/build-test/run-evidence.json`
- `fixtures/core/build-test/digest-view-ref.json`
- `fixtures/core/build-test/expected-validation.json`
- `fixtures/core/build-test/expected-review-summary.txt`
- `fixtures/core/build-test/negative/digest-evidence-as-run-evidence.json`
- `fixtures/core/build-test/negative/policy-decision-invalid-decision.json`
- `fixtures/core/build-test/negative/run-with-invalid-state.json`
- `fixtures/core/build-test/negative/secret-value-in-service-binding.json`
- `fixtures/core/remote-service-binding/README.md`
- `fixtures/core/remote-service-binding/source-artifacts.json`
- `fixtures/core/remote-service-binding/capability.json`
- `fixtures/core/remote-service-binding/assembly.json`
- `fixtures/core/remote-service-binding/policy-decision.json`
- `fixtures/core/remote-service-binding/run.json`
- `fixtures/core/remote-service-binding/run-evidence.json`
- `fixtures/core/remote-service-binding/digest-view-ref.json`
- `fixtures/core/remote-service-binding/expected-validation.json`
- `fixtures/core/remote-service-binding/expected-review-summary.txt`
- `fixtures/core/remote-service-binding/negative/embedded-secret-service-binding.json`
- `fixtures/core/remote-service-binding/negative/missing-policy-decision.json`
- `fixtures/core/remote-service-binding/negative/remote-evidence-overclaim.json`
- `fixtures/core/remote-service-binding/negative/stale-service-binding.json`
- `fixtures/core/remote-service-binding/negative/undeclared-network-access.json`
- `fixtures/core/negative/README.md`
- `fixtures/core/negative/expected-validation.json`
- `fixtures/core/negative/assembly-action-without-capability.json`
- `fixtures/core/negative/capability-implies-authorization.json`
- `fixtures/core/negative/digest-binding-collapses-evidence.json`
- `fixtures/core/negative/digest-evidence-as-run-evidence.json`
- `fixtures/core/negative/duplicate-object-id.json`
- `fixtures/core/negative/external-artifact-unverified-integrity.json`
- `fixtures/core/negative/external-standard-copied-inline.json`
- `fixtures/core/negative/invalid-run-state.json`
- `fixtures/core/negative/missing-policy-decision.json`
- `fixtures/core/negative/policy-decision-missing-obligations.json`
- `fixtures/core/negative/run-completed-without-output.json`
- `fixtures/core/negative/run-evidence-overclaims-correctness.json`
- `fixtures/core/negative/run-without-assembly-reference.json`
- `fixtures/core/negative/runtime-oci-missing-image-reference.json`
- `fixtures/core/negative/secret-value-service-binding.json`
- `fixtures/core/negative/unanchored-reproducible-artifact.json`
- `fixtures/core/negative/unknown-binding-role.json`
- `fixtures/core/negative/unresolved-artifact-reference.json`

## Reference Implementation

- `reference/python/cap_core/__init__.py`
- `reference/python/cap_core/validator.py`
- `reference/python/scripts/validate_core_fixtures.py`
- `reference/python/scripts/render_core_inspection_report.py`
- `reference/python/scripts/run_core_interop_harness.py`
- `reference/python/scripts/compare_core_interop_reports.py`
- `reference/python/scripts/validate_fixtures.py`
- `reference/python/scripts/validate_schema_fixtures.py`
- `reference/python/tests/test_core_local_analysis.py`

## CI

- `.github/workflows/core-draft.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/schemas.yml`
- `.github/workflows/conformance.yml`

## Generated Reports

- `release-artifacts/core-candidate-review/reports/core-conformance-report.json`
- `release-artifacts/core-candidate-review/reports/core-inspection-remote-service-binding.json`
- `release-artifacts/core-candidate-review/reports/core-inspection-remote-service-binding.txt`
- `release-artifacts/core-candidate-review/reports/core-interop-reference.json`
- `release-artifacts/core-candidate-review/reports/core-interop-self-comparison.json`

## Readiness

- `specs/core/reviews/2026-07-07-candidate-readiness.md`
- `specs/core/reviews/2026-07-07-candidate-normative-review-entry.md`
- `release-artifacts/core-candidate-review/known-limitations.md`
