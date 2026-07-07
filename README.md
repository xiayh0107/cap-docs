# CAP — Context Assembly Protocol

> Status: draft · Version: 2026-07-06-draft · Scope: CAP-Digest draft profile plus non-normative CAP-Core draft track

CAP is a family of specifications for turning complex source objects and
machine-operable task records into safe, bounded, traceable context and assembly
artifacts for AI agents.

The repository currently has one normative-track draft profile, **CAP-Digest**,
and one non-normative upper-layer draft track, **CAP-Core**.

## Current Scope

**CAP-Digest** is the active draft specification. It defines a context evidence
layer: how a source object is transformed into a model-readable digest plus a
machine-readable `DigestManifest` with stable field anchors, budgeted selection,
redaction, evidence validation, and gated follow-up.

```text
source object -> field catalog -> context digest -> model response -> gated follow-up
```

**CAP-Core** is a draft-track proposal area. It explores artifact graphs,
capability/runtime binding, RunEvidence, policy records, and external standard
bindings through split draft RFCs, but it does not define stable conformance
yet.

## Repository Layout

```text
cap-docs/
├── specs/
│   ├── digest/               # CAP-Digest draft specification
│   └── core/                 # CAP-Core non-normative draft proposal track
├── schemas/                  # CAP-Digest schemas and CAP-Core schema sketches
├── fixtures/                 # executable draft fixtures
├── packs/                    # experimental Digest Packs
├── reference/                # experimental Python reference helpers
├── capps/                    # CAP proposal process
├── notes/                    # non-normative design and research notes
├── RELEASE-CHECKLIST.md      # CAP-Digest 0.1.0-alpha checklist
└── .github/                  # issue/PR templates and CI workflows
```

## Start Reading

- Current CAP-Digest spec: [specs/digest/00-overview.md](specs/digest/00-overview.md)
- Implementation guide: [specs/digest/12-implementation-guide.md](specs/digest/12-implementation-guide.md)
- Current project status: [STATUS.md](STATUS.md)
- Roadmap: [ROADMAP.md](ROADMAP.md)
- Alpha release checklist: [RELEASE-CHECKLIST.md](RELEASE-CHECKLIST.md)
- Governance and CAPP process: [capps/README.md](capps/README.md)
- CAP-Core draft track: [specs/core/README.md](specs/core/README.md)

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

CAP-Core executable draft-track coverage includes:

- `schemas/core/`
- `fixtures/core/local-analysis/`
- `fixtures/core/build-test/`
- `reference/python/cap_core/`

These Core assets are useful for design validation, but they are not stable
CAP-Core conformance requirements.

## Run Checks

From the repository root:

```bash
python -m unittest discover reference/python/tests
python reference/python/scripts/validate_schema_fixtures.py
python reference/python/scripts/validate_fixtures.py
python reference/python/scripts/validate_fixtures.py --report conformance-report.json
python reference/python/scripts/validate_core_fixtures.py --report core-conformance-report.json
```

The conformance report uses `cap.conformance_report.v1` and currently covers
the CAP-Digest fixtures plus the CAP-Core local-analysis, build-test, and
remote-service-binding draft fixtures.

## Conformance Snapshot

Current executable target:

```text
CAP-Digest Level 0/1: table source digest assembly
CAP-Digest Level 2: gated follow-up for table sample rows
CAP-Digest Level 3: table-basic Digest Pack metadata loading
CAP-Core: non-normative local-analysis, build-test, and remote-service-binding draft fixtures
```

CAP-Digest `0.1.0-alpha` is tagged as `cap-digest-0.1.0-alpha`. GitHub release
notes document the alpha scope, fixture coverage, reference implementation
status, known limitations, and non-normative CAP-Core status.

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

Documents in `notes/`, `reference/`, draft fixtures, and CAP-Core draft-track
assets are non-normative unless a future accepted CAPP explicitly promotes them.
