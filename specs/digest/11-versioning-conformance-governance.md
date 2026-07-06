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

## Version Bump Rules

| Change | Required action |
|---|---|
| Adds or changes CAP-Digest lifecycle primitives or conformance levels | CAPP plus protocol version update. |
| Changes digest text grammar in a way old readers cannot parse | New `text=vN`. |
| Changes Field ID grammar or renaming rules | New `fields=fN`. |
| Adds optional DigestManifest fields | Same `cap.manifest.v1` allowed. |
| Adds required DigestManifest fields or narrows existing meanings | New `cap.manifest.vN`. |
| Changes the digest object envelope incompatibly | New `cap.digest.vN`. |
| Changes digest patch operation semantics incompatibly | New `cap.digest_patch.vN`. |
| Adds fixture-only negative cases for already specified behavior | No version bump; update conformance report expectations. |
| Changes an active fixture's expected output | CAPP unless the previous fixture was plainly wrong. |

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

## CAPP Status Lifecycle

CAPP files use these statuses:

| Status | Meaning |
|---|---|
| `draft` | Author is shaping the proposal; not ready for adoption. |
| `proposed` | Ready for review and compatibility/security analysis. |
| `accepted` | Design accepted; implementation may proceed. |
| `implemented` | Reference assets, schemas, fixtures, or docs have landed. |
| `active` | Current normative guidance for the relevant track. |
| `deferred` | Valid problem, intentionally postponed. |
| `withdrawn` | Proposal will not proceed in its current form. |

Status changes SHOULD be made in the CAPP file itself and mentioned in the PR.
Moving to `accepted`, `implemented`, or `active` SHOULD include links to the
schema, fixture, or reference implementation evidence.

## Release Lifecycle

CAP-Digest release labels use:

| Release state | Meaning |
|---|---|
| `draft` | Work in repository; no release artifact promised. |
| `alpha` | Usable for experimental implementation against listed fixtures; breaking changes likely. |
| `beta` | Feature set mostly complete; breaking changes require stronger justification. |
| `stable` | Compatibility promises apply across the documented version tracks. |
| `deprecated` | Still available but should not be newly adopted. |

The `0.1.0-alpha` target is an alpha release. It must not be described as a
stable standard.

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

Fixture compatibility rules:

- adding a new fixture is compatible when it tests already documented behavior;
- adding a negative fixture is compatible when the rejected behavior was already
  prohibited by spec text;
- changing expected output for an active fixture requires a CAPP unless the old
  output contradicted the active spec;
- fixture README files must state what is intentionally covered and what is not;
- remote or credentialed fixtures must be opt-in and excluded from default CI.

Schema compatibility rules:

- additive optional properties are compatible;
- new required properties, enum narrowing, changed meanings, or removed
  properties require a schema version bump;
- `additionalProperties` behavior is part of compatibility;
- schemas and fixtures should be updated in the same PR when possible.

## Conformance Report

```json
{
  "schema": "cap.conformance_report.v1",
  "ok": true,
  "checks": [
    {
      "name": "fixtures/basic-table",
      "ok": true,
      "problems": []
    }
  ]
}
```

The minimal required fields are `schema`, `ok`, and `checks`. Each check records
`name`, `ok`, and `problems`. Implementations MAY add optional implementation
identity, CAP version, and claimed level only after the schema permits those
fields.

The reference implementation emits this report with:

```bash
python reference/python/scripts/validate_fixtures.py --report conformance-report.json
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

## CAP-Digest 0.1.0-Alpha Checklist

The alpha release checklist lives in
[`../../RELEASE-CHECKLIST.md`](../../RELEASE-CHECKLIST.md). A maintainer should
not tag `0.1.0-alpha` until:

- docs, schema, reference, and conformance workflows pass on `main`;
- `basic-table`, `digest-text-negative`, `followup-basic`, `pack-table-basic`,
  and `security-adversarial` fixtures pass;
- CAPP-0001, CAPP-0002, and CAPP-0003 have clear implemented/active status;
- `CHANGELOG.md`, `STATUS.md`, and `ROADMAP.md` identify the alpha scope and
  known limitations;
- CAP-Core remains explicitly non-normative;
- release notes list current conformance level, fixture coverage, reference
  implementation status, and post-alpha gaps.

## Stability Bias

CAP-Digest should prefer:

- small primitives over many special cases;
- explicit manifests over hidden behavior;
- conformance fixtures over prose-only claims;
- visible caveats over silent best effort;
- host policy over model self-policing;
- progressive disclosure over dumping all instructions into context.
