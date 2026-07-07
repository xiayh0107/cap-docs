# CAP-Core Implementer Guide

> Status: stable v1.0 - Last updated: 2026-07-07

This guide gives implementers a concrete path to read, validate, render, and
report CAP-Core v1.0 packages.

## Minimal Reader Behavior

An implementation should read Core JSON records, preserve unknown profile
fields, inventory object IDs, and avoid executing anything from an Assembly or
Capability record.

## Validation Commands

Run all fixtures:

```bash
python reference/python/scripts/validate_fixtures.py --scope core
```

Generate a Core conformance report:

```bash
python reference/python/scripts/validate_core_fixtures.py \
  --target-level L3 \
  --report core-conformance-report.json
```

Validate schema/fixture mappings:

```bash
python reference/python/scripts/validate_schema_fixtures.py
```

## Renderer Command

```bash
python reference/python/scripts/render_core_inspection_report.py \
  --fixture local-analysis \
  --json-report core-inspection.json \
  --text-report core-inspection.txt
```

## Interop Command

```bash
python reference/python/scripts/run_core_interop_harness.py \
  --report core-interop-reference.json
```

External implementations can submit compatible reports using
`specs/core/INTEROPERABILITY-HARNESS.md`.

## Level Map and Claim Templates

| Level | Implementer task |
|---|---|
| L0 | Read records, validate schema names and required fields, preserve profile fields. |
| L1 | Validate ArtifactSet, Capability, Binding, Assembly, and graph closure. |
| L2 | Add PolicyDecision checks, fail-closed missing policy behavior, and secret scanning. |
| L3 | Add Run, RunEvidence, DigestBinding separation, limitations, and overclaim checks. |
| L4 | Compare implementation reports through the interop harness. |

Claim templates:

```text
Implementation <name> claims CAP-Core v1.0 L0 conformance for structural object reading. Evidence: <report path>.
Implementation <name> claims CAP-Core v1.0 L1 conformance for bound assembly validation. Evidence: <report path>.
Implementation <name> claims CAP-Core v1.0 L2 conformance for policy-aware assembly validation. Evidence: <report path>.
Implementation <name> claims CAP-Core v1.0 L3 conformance for run-evidence producer validation. Evidence: <report path>.
Implementation <name> claims CAP-Core v1.0 L4 conformance for interoperable report comparison. Evidence: <comparison report path>.
```

Each claim should name implementation version, fixture suite version, target
level, unsupported features, and report schema version.

## Common Failure Modes

- missing required field;
- unknown artifact, binding, capability, run, or evidence reference;
- Capability record implying authorization;
- service binding carrying inline secret-looking values;
- missing or stale policy decision;
- completed Run without output/log evidence;
- RunEvidence claiming semantic correctness;
- DigestEvidence used as RunEvidence.

## Non-Execution Rule

Core records alone do not authorize workflow execution, policy evaluation,
secret retrieval, remote calls, or scientific correctness claims. Hosts and
external bindings own those behaviors.

## Release Artifacts

Stable release artifacts live in `release-artifacts/cap-core-v1.0.0/`.
Release-candidate artifacts live in `release-artifacts/cap-core-v1.0.0-rc1/`.
Both include schema copies, fixture copies, reports, release notes, and
manifest files.
