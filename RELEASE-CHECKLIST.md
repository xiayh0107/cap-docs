# CAP-Digest 0.1.0-Alpha Release Checklist

> Status: completed checklist
> Prepared: 2026-07-06

This checklist records the completed CAP-Digest `0.1.0-alpha` release. It does
not define CAP-Core conformance.

For the CAP-Digest v1.0.0 stable release, use
`specs/digest/RELEASE-GATES-v1.0.md` and
`release-artifacts/cap-digest-v1.0.0/`.

## Required Criteria

- [x] Repository maintenance baseline is merged.
- [x] `basic-table` fixture passes reference implementation checks.
- [x] Schema JSON files parse in CI.
- [x] Fixture JSON files parse in CI.
- [x] Follow-up fixture is complete for alpha scope.
- [x] Pack fixture is complete for alpha scope.
- [x] Security/adversarial fixtures cover escaping, masking, malformed digest
  text, evidence validation, and renderer failure shape.
- [x] CAPP-0001, CAPP-0002, and CAPP-0003 have clear statuses.
- [x] `CHANGELOG.md`, `STATUS.md`, and `ROADMAP.md` describe the alpha scope.
- [x] Docs, schemas, reference, and conformance workflows pass on `main`.
- [x] CAP-Core remains reserved, draft-track, and non-normative.
- [x] Release tag created.
- [x] GitHub release notes published.

## Candidate Tag

Use one of:

- `cap-digest-0.1.0-alpha`
- `v0.1.0-alpha`

The historical alpha tag is `cap-digest-0.1.0-alpha`.

## Release Notes Outline

Release notes should include:

- CAP-Digest scope: digest text, DigestManifest, DigestEvidence validation,
  follow-up gate, Digest Packs, schemas, fixtures, and reference checks.
- Current conformance level: Level 0/1 table assembly, Level 2 follow-up gate,
  and Level 3 table-basic pack metadata loading.
- Fixture coverage: `basic-table`, `digest-text-negative`, `followup-basic`,
  `pack-table-basic`, and `security-adversarial`.
- Reference implementation status: experimental executable companion, not a
  production SDK.
- CAP-Core status: non-normative draft-track proposal assets only.

## Known Limitations

- Only one CAP-Digest source type, `table`, has executable coverage.
- The Python reference implementation is intentionally minimal.
- JSON schemas are draft assets and are not yet packaged as an independently
  versioned schema bundle.
- CI parses schema and fixture JSON, validates schema-backed fixtures, and runs
  fixture validation.
- Remote, credentialed, and large-source fixtures are out of scope for alpha.
- CAP-Core schemas, fixtures, RunEvidence, runtime binding, service binding, and
  policy model are not stable conformance requirements.

## Pre-Tag Commands

Run from the repository root:

```bash
python -m unittest discover reference/python/tests
python reference/python/scripts/validate_fixtures.py --report conformance-report.json
python - <<'PY'
import json
from pathlib import Path
for root in (Path('schemas'), Path('fixtures')):
    for path in sorted(root.rglob('*.json')):
        json.loads(path.read_text(encoding='utf-8'))
print('json ok')
PY
git diff --check
```
