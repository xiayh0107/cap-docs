# Fixtures

> Status: draft · Last updated: 2026-07-06

This directory holds draft fixtures for CAP-Digest and CAP-Core implementations.
Fixtures define executable expectations for draft assets, but they are stable
conformance requirements only when a CAPP marks them active.

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

## Current fixture families

- `basic-table/` — a small tabular source exercising CAP-Digest Level 0 (Digest Producer)
  and Level 1 (Safe Assembler): field catalog, budgeted selection, redaction
  before rendering, evidence validation of cited field IDs.
- `core/local-analysis/` — a CAP-Core draft fixture exercising artifact refs,
  capability, Assembly, Binding records, policy decision, Run, RunEvidence,
  DigestBinding, review rendering, and negative layer/security cases.

## Planned additional cases

- A follow-up case exercising Level 2 (Follow-Up Capable): contract response,
  gate decision, digest patch.
- A digest-pack case exercising Level 3 (Digest Pack Ecosystem): pack-driven
  field definitions and renderers.
