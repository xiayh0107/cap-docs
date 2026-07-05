# Fixtures (Planned)

> Status: planned · Last updated: 2026-07-05

This directory will hold conformance fixtures for CAP-Digest implementations.
It currently contains **no fixtures**; the structure below is a planning sketch
aligned with the conformance levels defined in
`specs/digest/11-versioning-conformance-governance.md`.

## Planned layout

Each fixture is a self-contained case directory with a source, a policy, and
expected outputs that an implementation must reproduce:

```text
fixtures/
└── <case-name>/
    ├── source.json            # the input source object
    ├── policy.json            # redaction / budget / trust policy
    ├── expected-digest.txt    # expected digest text
    ├── expected-manifest.json # expected DigestManifest
    └── expected-validation.json # expected evidence/gate validation outcome
```

## Planned initial cases

- `basic-table/` — a small tabular source exercising Level 0 (Digest Producer)
  and Level 1 (Safe Assembler): field catalog, budgeted selection, redaction
  before rendering, evidence validation of cited field IDs.
- A follow-up case exercising Level 2 (Follow-Up Capable): contract response,
  gate decision, digest patch.
- A digest-pack case exercising Level 3 (Digest Pack Ecosystem): pack-driven
  field definitions and renderers.

Cases will be added when the schemas in `../schemas/` reach a stable draft and a
reference implementation is available to validate them.