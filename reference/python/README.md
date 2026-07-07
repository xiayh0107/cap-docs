# CAP Python Reference Implementation

This is an experimental executable companion for the CAP-Digest and CAP-Core
drafts. It is not the specification and is not intended as a production SDK.

Current CAP-Digest scope:

- source type: `table`;
- fields: shape, compact columns, sample rows metadata;
- redaction: sensitive-name masking;
- tokenizer: `heuristic_v1` placeholder;
- fingerprint: fixture-provided `structure_v1` value;
- validation: evidence IDs must exist, be selected, and appear in digest text;
- follow-up gate: validates evidence, fingerprint, budget, and selected status;
- digest patch: renders `f1:table@sample#k10` after gate approval;
- pack loading: reads `packs/table-basic/fields/*.yaml`;
- conformance report: `validate_fixtures.py --report conformance-report.json`.

Current CAP-Core scope:

- fixtures: `fixtures/core/local-analysis/`, `fixtures/core/build-test/`, and
  `fixtures/core/remote-service-binding/`;
- negative suite: `fixtures/core/negative/`;
- objects: Artifact, Capability, Binding, Assembly, Run, RunEvidence, DigestBinding;
- validation: required fields, known references, required binding types,
  policy/run/evidence linkage, no secret values in Core records,
  remote-service safety checks, and CAP-Digest/CAP-Core evidence separation;
- rendering: stable review summary and inspection reports for Core draft fixtures;
- Core report: `validate_core_fixtures.py --report core-conformance-report.json`.
- interop report: `run_core_interop_harness.py --report core-interop-reference.json`.

Run tests from the repository root:

```bash
python -m unittest discover reference/python/tests
```

Run fixture validation from the repository root:

```bash
python reference/python/scripts/validate_fixtures.py
python reference/python/scripts/validate_fixtures.py --report conformance-report.json
python reference/python/scripts/validate_core_fixtures.py --report core-conformance-report.json
python reference/python/scripts/render_core_inspection_report.py --fixture local-analysis
python reference/python/scripts/run_core_interop_harness.py --report core-interop-reference.json
```

The fixture validator covers `basic-table`, `digest-text-negative`,
`followup-basic`, `pack-table-basic`, `security-adversarial`, and the
non-normative CAP-Core draft fixtures and negative suite.
