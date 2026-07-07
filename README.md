# CAP — Context Assembly Protocol

> Status: stable tracks · Version: 2026-07-07 · Scope: CAP-Digest v1.0.0 plus CAP-Core v1.0.0

CAP is a family of specifications for turning complex source objects and
machine-operable task records into safe, bounded, traceable context and assembly
artifacts for AI agents.

The repository currently has a stable **CAP-Digest v1.0.0** release for the
fixture-scoped context evidence profile and a stable **CAP-Core v1.0.0**
release for the minimal Core control-plane object contract.

## Current Scope

**CAP-Digest v1.0.0** defines a context evidence layer: how a source object is
transformed into a model-readable digest plus a machine-readable
`DigestManifest` with stable field anchors, budgeted selection, redaction,
evidence validation, and gated follow-up. The v1.0.0 stable claim is
fixture-scoped and currently covers the table source family.

```text
source object -> field catalog -> context digest -> model response -> gated follow-up
```

**CAP-Core v1.0.0** defines the minimal structural Core object contract,
conformance levels, schema package, fixture suite, validator/report codes, and
maintenance policy. It does not define runtime execution, policy language
semantics, credential exchange, scientific correctness, or CAP-Digest behavior
changes.

## Repository Layout

```text
cap-docs/
├── specs/
│   ├── digest/               # CAP-Digest v1.0 stable docs plus historical draft material
│   └── core/                 # CAP-Core v1.0.0 stable docs plus historical drafts
├── schemas/                  # CAP-Digest schemas and CAP-Core v1.0 schemas
├── fixtures/                 # executable fixtures and conformance suites
├── packs/                    # experimental Digest Packs
├── reference/                # experimental Python reference helpers
├── capps/                    # CAP proposal process
├── notes/                    # non-normative design and research notes
├── RELEASE-CHECKLIST.md      # CAP-Digest alpha checklist plus v1.0 gate pointer
└── .github/                  # issue/PR templates and CI workflows
```

## Start Reading

- CAP-Digest v1.0 stable track: [specs/digest/STABLE-TRACK.md](specs/digest/STABLE-TRACK.md)
- Current CAP-Digest spec: [specs/digest/00-overview.md](specs/digest/00-overview.md)
- Implementation guide: [specs/digest/12-implementation-guide.md](specs/digest/12-implementation-guide.md)
- Current project status: [STATUS.md](STATUS.md)
- Roadmap: [ROADMAP.md](ROADMAP.md)
- Alpha release checklist: [RELEASE-CHECKLIST.md](RELEASE-CHECKLIST.md)
- Governance and CAPP process: [capps/README.md](capps/README.md)
- CAP-Core v1.0.0 stable: [specs/core/README.md](specs/core/README.md)

## Executable Draft Assets

CAP-Digest executable coverage now includes:

- `fixtures/basic-table/` — Level 0/1 table assembly, manifest generation,
  redaction, and evidence validation.
- `fixtures/digest-text-negative/` — parser and manifest/text consistency
  negative cases.
- `fixtures/followup-basic/` — Level 2 follow-up gate and digest patch behavior.
- `fixtures/pack-table-basic/` — Level 3 `table-basic` Digest Pack metadata
  loading.
- `fixtures/security-adversarial/` — escaping, sensitive-name masking, and
  renderer failure manifest shape.
- `packs/table-basic/` — the first experimental Digest Pack.
- `reference/python/` — experimental executable companion and fixture checker.
- `release-artifacts/cap-digest-v1.0.0/` — CAP-Digest v1.0.0 stable package.

CAP-Core v1.0 executable coverage includes:

- `schemas/core/`
- `fixtures/core/local-analysis/`
- `fixtures/core/build-test/`
- `fixtures/core/remote-service-binding/`
- `fixtures/core/negative/`
- `reference/python/cap_core/`
- `release-artifacts/cap-core-v1.0.0/`

These Core assets are the CAP-Core v1.0.0 fixture and report surface described
by the stable Core documents and release package.

## Run Checks

From the repository root:

```bash
python -m unittest discover reference/python/tests
python reference/python/scripts/validate_schema_fixtures.py
python reference/python/scripts/validate_fixtures.py
python reference/python/scripts/validate_fixtures.py --report conformance-report.json
python reference/python/scripts/validate_core_fixtures.py --report core-conformance-report.json
python reference/python/scripts/render_core_inspection_report.py --fixture local-analysis
python reference/python/scripts/run_core_interop_harness.py --report core-interop-reference.json
python reference/python/scripts/validate_digest_release_manifest.py
```

The conformance report uses `cap.conformance_report.v1` and currently covers
the CAP-Digest fixtures plus the CAP-Core v1.0 fixture families.

## Conformance Snapshot

Current executable target:

```text
CAP-Digest Level 0/1: table source digest assembly
CAP-Digest Level 2: gated follow-up for table sample rows
CAP-Digest Level 3: table-basic Digest Pack metadata loading
CAP-Core v1.0.0: local-analysis, build-test, remote-service-binding, and negative fixtures
```

CAP-Digest v1.0.0 stable is accepted by CAPP-0009 and packaged under
`release-artifacts/cap-digest-v1.0.0/`. CAP-Digest `0.1.0-alpha` remains tagged
as `cap-digest-0.1.0-alpha` as the historical alpha release.

## Contribution and Governance

- Use [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.
- Use [SECURITY.md](SECURITY.md) for security-sensitive reports.
- Use `capps/` for substantial CAP-Digest, CAP-Core, pack, or governance
  changes.
- Use [CHANGELOG.md](CHANGELOG.md) for notable changes.

## Layer Rule

Every change should answer:

> Is this refining CAP-Digest, or does it actually belong in CAP-Core?

CAP-Digest is a context evidence profile. CAP-Core is a broader object assembly
proposal track. Keeping them separate avoids turning digest text, field
selection, and evidence validation into an implicit runtime protocol.

## Normative Language

The CAP-Digest spec uses **MUST**, **MUST NOT**, **SHOULD**, and **MAY** as
defined in [specs/digest/00-overview.md](specs/digest/00-overview.md).

Documents in `notes/` and `reference/` are non-normative. Historical CAP-Core
draft documents remain design records unless cited by CAPP-0007 or the v1.0
stable documents.
