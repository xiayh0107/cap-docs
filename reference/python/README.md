# CAP Python Reference Implementation

This is an experimental executable companion for the CAP-Digest and CAP-Core
drafts. It is not the specification and is not intended as a production SDK.

Current CAP-Digest scope:

- source type: `table`;
- fields: shape, compact columns, sample rows metadata;
- redaction: sensitive-name masking;
- tokenizer: `heuristic_v1` placeholder;
- fingerprint: fixture-provided `structure_v1` value;
- validation: evidence IDs must exist, be selected, and appear in digest text.

Current CAP-Core scope:

- fixture: `fixtures/core/local-analysis/`;
- objects: Artifact, Capability, Binding, Assembly, Run, RunEvidence, DigestBinding;
- validation: required fields, known references, required binding types, policy/run/evidence linkage, no secret values in Core records, and CAP-Digest/CAP-Core evidence separation;
- rendering: stable review summary for the local-analysis fixture.

Run tests:

```bash
cd reference/python
python -m unittest discover tests
```

Run fixture validation from the repository root:

```bash
python reference/python/scripts/validate_fixtures.py
```
