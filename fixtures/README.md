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

## Schema validation map

`reference/python/scripts/validate_schema_fixtures.py` inventories every JSON
file under `fixtures/`. Each file must either be validated against a schema or
be documented as fixture harness data without an alpha schema.

Schema-backed CAP-Digest fixture files:

- `basic-table/expected-manifest.json` validates against `cap.manifest.v1`.
- `basic-table/expected-validation.json` validates nested ContractResponse and
  ValidationResult records.
- `basic-table/negative-validation.json` validates each nested negative
  ContractResponse and ValidationResult record.
- `catalog-table-basic/field-catalog.json` validates against
  `cap.field_catalog.v1`.
- `followup-basic/request-approved.json` and `followup-basic/response.json`
  validate against `cap.contract_response.v1`.
- `followup-basic/expected-validation-approved.json` validates against
  `cap.validation_result.v1`.
- `followup-basic/expected-gate-approved.json` and
  `followup-basic/expected-gate-stale.json` validate against
  `cap.gate_result.v1`, including any nested `cap.digest_patch.v1` patch.
- `followup-basic/expected-patch.json` validates against
  `cap.digest_patch.v1`.
- `pack-table-basic/expected-pack-report.json` validates against
  `cap.pack_conformance_report.v1`.
- `security-adversarial/renderer-failure-manifest.json` validates against
  `cap.manifest.v1`.

Schema-backed CAP-Core draft fixture files:

- `core/local-analysis/source-artifacts.json` validates each nested Artifact
  against the draft `cap.core.artifact.v1` schema. The artifact-set wrapper has
  no schema yet.
- `core/local-analysis/capability.json`, `assembly.json`, `run.json`,
  `run-evidence.json`, and `digest-view-ref.json` validate against the matching
  draft Core schema sketches.
- `core/local-analysis/assembly.json` also validates each nested Binding record
  against `cap.core.binding.v1`.
- `core/local-analysis/negative/secret-value-in-service-binding.json` is schema
  valid but intentionally fails semantic Core validation because it carries a
  secret value.
- `core/local-analysis/negative/run-without-assembly.json` is intentionally
  schema invalid and must continue failing required-field validation.

Fixture harness or no-schema JSON:

- `source.json` and `policy.json` files are fixture inputs. CAP-Digest source
  and policy schemas are not defined for the alpha.
- `followup-basic/expected-gate.json` and `pack-table-basic/expected-pack.json`
  are compact reference-test summaries, not normative schema artifacts.
- `core/local-analysis/policy-decision.json` has no Core schema sketch yet.
- `core/local-analysis/expected-validation.json` is reference-validator
  expected output.
- `core/local-analysis/negative/digest-evidence-as-run-evidence.json` is a
  layer-boundary negative case using a Digest evidence shape not defined in this
  repository.

## Planned additional cases

- Additional adversarial security fixtures for escaping, redaction policy
  composition, and stale fingerprints.
