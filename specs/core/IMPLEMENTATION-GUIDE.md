# CAP-Core Draft Implementer Guide

> Status: candidate-prep draft - Non-normative - Last updated: 2026-07-07

This guide gives implementers a concrete path to read, validate, render, and
report Core draft packages. It is not stable normative conformance.

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

## Level Map

| Level | Implementer task |
|---|---|
| L0 | Read records, validate schema names and required fields, preserve profile fields. |
| L1 | Validate ArtifactSet, Capability, Binding, Assembly, and graph closure. |
| L2 | Add PolicyDecision checks, fail-closed missing policy behavior, and secret scanning. |
| L3 | Add Run, RunEvidence, DigestBinding separation, limitations, and overclaim checks. |
| L4 | Compare implementation reports through the interop harness. |

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
