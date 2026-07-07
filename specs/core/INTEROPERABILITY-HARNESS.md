# CAP-Core Interoperability Harness

> Status: candidate-prep draft - Non-normative - Last updated: 2026-07-07

The interop harness compares fixture pass/fail status and stable error codes
across implementations. It is the candidate-prep basis for L4 review.

## Report Format

Implementation reports use:

```text
schemas/core/cap.core.interop_report.v1.schema.json
```

Comparison reports use:

```text
schemas/core/cap.core.interop_comparison.v1.schema.json
```

Each fixture row records name, path, `ok`, stable error codes, warning codes,
and unsupported features.

## Reference Report

Generate a reference-compatible report:

```bash
python reference/python/scripts/run_core_interop_harness.py \
  --implementation-name cap_core.reference_validator \
  --report core-interop-reference.json
```

## External Validator Command

An external implementation can submit one JSON object per fixture with:

```json
{
  "ok": true,
  "errorCodes": [],
  "warningCodes": [],
  "unsupportedFeatures": []
}
```

Wrap it with:

```bash
python reference/python/scripts/run_core_interop_harness.py \
  --implementation-name example.external \
  --command "example-core-validate --fixture {fixture_path}" \
  --report core-interop-external.json
```

The command template supports `{root}`, `{fixture}`, and `{fixture_path}`.

## Comparison

Compare an external report against the reference report:

```bash
python reference/python/scripts/compare_core_interop_reports.py \
  --expected core-interop-reference.json \
  --actual core-interop-external.json \
  --report core-interop-comparison.json
```

L4 candidate-prep review uses this harness when a second implementation or
external adapter report exists.
