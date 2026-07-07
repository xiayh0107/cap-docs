# CAP-Core v1.0 Inspection Report

> Status: stable v1.0 - Normative report format - Last updated: 2026-07-07

The stable inspection report uses
`schemas/core/cap.core.inspection_report.v1.schema.json` and the text renderer
documented in `specs/core/INSPECTION-REPORT.md`.

## Required Coverage

Inspection output MUST include object graph summary, binding summary, policy
summary, Run and RunEvidence summary, limitations, validation errors, and
validation warnings. It MUST preserve Core/Profile/Digest boundaries and MUST
NOT expose secret values.

## Examples

The v1.0 release artifacts include JSON and text inspection reports for all
positive fixture families:

- `reports/core-inspection-local-analysis.*`
- `reports/core-inspection-build-test.*`
- `reports/core-inspection-remote-service-binding.*`

Renderer output is human-readable evidence; conformance claims are based on the
machine-readable report and validator findings.
