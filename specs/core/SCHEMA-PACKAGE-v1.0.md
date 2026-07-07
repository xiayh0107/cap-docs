# CAP-Core v1.0 Schema Package

> Status: stable v1.0 - Normative - Last updated: 2026-07-07

The CAP-Core v1.0 schema package consists of the JSON Schema files under
`schemas/core/` and their copies in the v1.0 release artifacts.

## Stable Schema Files

- `cap.core.artifact_set.v1.schema.json`
- `cap.core.artifact.v1.schema.json`
- `cap.core.capability.v1.schema.json`
- `cap.core.binding.v1.schema.json`
- `cap.core.assembly.v1.schema.json`
- `cap.core.policy_decision.v1.schema.json`
- `cap.core.run.v1.schema.json`
- `cap.core.run_evidence.v1.schema.json`
- `cap.core.conformance_report.v1.schema.json`
- `cap.core.inspection_report.v1.schema.json`
- `cap.core.interop_report.v1.schema.json`
- `cap.core.interop_comparison.v1.schema.json`
- `cap.core.negative_case.v1.schema.json`
- `cap.core.negative_suite_expected.v1.schema.json`

## Compatibility Contract

Stable `$id` values are the current `https://cap-spec.org/schemas/core/...`
identifiers in those files. Implementations MUST treat required fields and enum
tokens as v1.0 compatibility commitments.

Additive compatible changes may add optional fields, new report metadata, or
new profile-owned values. Breaking changes include removing required fields,
changing stable enum meanings, changing report schemas incompatibly, or
weakening security findings.

Unknown fields MUST be preserved by readers unless a profile-specific validator
rejects them. Profile-owned extensions should be carried in `profiles`,
`profile`, `profileType`, `metadata`, or clearly namespaced fields.

## Migration From Candidate Prep

Candidate-prep `cap.core.*.v1` records that pass the current schema and fixture
checks are v1.0 records when they also satisfy `STABLE-SCOPE-v1.0.md` and
`CONFORMANCE-v1.0.md`.
