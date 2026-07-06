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
- `digest-text-negative/` — parser and manifest/text consistency negative cases
  for duplicate field IDs, invalid field IDs, malformed data fences, and
  selected-field mismatches.
- `followup-basic/` — a CAP-Digest Level 2 fixture exercising ContractResponse,
  gate decision, fingerprint/budget checks, and `cap.digest_patch.v1`.
- `pack-table-basic/` — a CAP-Digest Level 3 fixture exercising pack discovery
  and field/redactor metadata alignment.
- `security-adversarial/` — adversarial security cases for source string
  escaping, secret-like field masking, and renderer failure manifest shape.
- `core/local-analysis/` — a CAP-Core draft fixture exercising artifact refs,
  capability, Assembly, Binding records, policy decision, Run, RunEvidence,
  DigestBinding, review rendering, and negative layer/security cases.

## Planned additional cases

- Additional adversarial security fixtures for escaping, redaction policy
  composition, and stale fingerprints.
