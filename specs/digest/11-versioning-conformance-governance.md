# Versioning, Conformance, and Governance

> Status: draft · Stability: stable

CAP-Digest is intended to become an interoperable standard. That requires
versioning, conformance fixtures, and a proposal process.

## Version Identifiers

CAP-Digest protocol versions use date-based identifiers:

```text
YYYY-MM-DD
```

Draft versions MAY add suffixes:

```text
2026-07-04-draft
```

Independent version tracks:

| Track | Example | Meaning |
|---|---|---|
| Protocol | `2026-07-04-draft` | Core primitives and lifecycle. |
| Digest text | `text=v1` | Text grammar. |
| Field IDs | `fields=f1` | Field ID scheme. |
| DigestManifest | `cap.manifest.v1` | DigestManifest schema. |
| Digest JSON | `cap.digest.v1` | Digest object schema. |
| Patch JSON | `cap.digest_patch.v1` | Digest patch schema. |

These versions change independently.

## Feature States

Features may be:

| State | Meaning |
|---|---|
| `draft` | Under design; not stable. |
| `active` | Current and recommended. |
| `deprecated` | Still recognized but should not be newly adopted. |
| `removed` | No longer part of the current version. |

Deprecated features MUST document a migration path or state that none is
required.

## Conformance Levels

### Level 0: Digest Producer

The implementation can produce digest text and a DigestManifest for at least one
source type.

Required:

- valid version line;
- selected field blocks with IDs;
- manifest rows for selected fields;
- visible caveats;
- data escaping.

### Level 1: Safe Assembler

Adds guard and privacy discipline.

Required:

- guarded source touches;
- redaction before rendering;
- DigestManifest rows for rejected fields;
- deterministic ordering;
- tokenizer or estimator identity;
- failed fields recorded rather than silently omitted.

### Level 2: Follow-Up Capable

Adds model contract validation and gated continuation.

Required:

- parseable contract response;
- evidence validation;
- request validation;
- budget checks;
- fingerprint checks;
- execution policy checks;
- digest patch or replacement digest.

### Level 3: Digest Pack Ecosystem

Adds reusable digest packs and fixture-based compatibility.

Required:

- digest pack discovery;
- pack metadata parsing;
- pack fixture execution;
- conformance report.

## Conformance Fixture Format

Recommended fixture:

```text
fixture-name/
  source.json
  policy.json
  expected-digest.txt
  expected-manifest.json
  expected-validation.json
```

If the source cannot be represented as JSON, the fixture may include a
deterministic setup script. The script must not require hidden credentials or
network access unless the fixture is explicitly marked remote.

## Conformance Report

```json
{
  "implementation": {
    "name": "example-cap-assembler",
    "version": "0.1.0"
  },
  "capVersion": "2026-07-04-draft",
  "level": 2,
  "fixtures": [
    {
      "name": "basic-table",
      "passed": true,
      "failures": []
    }
  ]
}
```

## Change Process

Substantial changes should use a CAP-Digest Proposal, abbreviated `CAPP`.

Write a CAPP for:

- new primitives;
- breaking schema changes;
- new digest text grammar;
- new normative security requirements;
- feature deprecation or removal;
- governance changes.

## CAPP Template

```markdown
# CAPP-0000: Title

## Abstract
## Motivation
## Specification
## Rationale
## Compatibility
## Security and Privacy
## Reference Implementation
## Conformance Fixtures
```

## Acceptance Criteria

A CAPP should not be accepted without:

- a clear problem statement;
- concrete syntax or data model changes;
- compatibility analysis;
- security and privacy analysis;
- at least one reference implementation or executable fixture.

## Stability Bias

CAP-Digest should prefer:

- small primitives over many special cases;
- explicit manifests over hidden behavior;
- conformance fixtures over prose-only claims;
- visible caveats over silent best effort;
- host policy over model self-policing;
- progressive disclosure over dumping all instructions into context.

