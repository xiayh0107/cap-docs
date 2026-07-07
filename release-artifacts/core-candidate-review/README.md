# CAP-Core Candidate Review Package

> Status: candidate-prep review package - Non-normative - Date: 2026-07-07

This package bounds the CAP-Core candidate review materials. It is not a
stable CAP-Core release and does not promote Core to candidate normative status.

## Review Scope

See `MANIFEST.md` for the full file list. The package points reviewers to:

- Core RFC drafts and candidate-prep rule documents;
- Core schema sketches and report schemas;
- positive fixture families and the systematic negative suite;
- validator, renderer, and interop commands;
- generated conformance, inspection, and interop reports;
- security, profile, binding, Digest bridge, and terminology evidence;
- the dated readiness report.

## Reproduce Reports

From the repository root:

```bash
python reference/python/scripts/validate_core_fixtures.py \
  --target-level L4 \
  --report release-artifacts/core-candidate-review/reports/core-conformance-report.json

python reference/python/scripts/render_core_inspection_report.py \
  --fixture remote-service-binding \
  --json-report release-artifacts/core-candidate-review/reports/core-inspection-remote-service-binding.json \
  --text-report release-artifacts/core-candidate-review/reports/core-inspection-remote-service-binding.txt

python reference/python/scripts/run_core_interop_harness.py \
  --report release-artifacts/core-candidate-review/reports/core-interop-reference.json

python reference/python/scripts/compare_core_interop_reports.py \
  --expected release-artifacts/core-candidate-review/reports/core-interop-reference.json \
  --actual release-artifacts/core-candidate-review/reports/core-interop-reference.json \
  --report release-artifacts/core-candidate-review/reports/core-interop-self-comparison.json
```

## Status Note

All included Core artifacts remain draft-track candidate-prep materials. Any
future candidate normative promotion needs a CAPP decision that cites the
readiness report and this package.
