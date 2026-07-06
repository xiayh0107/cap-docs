# CAP-Core RFC-0003: Scientific Computation Profile

> Status: draft profile proposal - Non-normative - Last updated: 2026-07-06

This split draft captures profile-level guidance for scientific or analytical
computations. It is not part of the minimal Core object model.

## Scope

The profile describes how Core objects may be interpreted for bounded
scientific or analytical runs:

- dataset, script, config, environment, output, report, and log artifact roles;
- local or external runtime references;
- resource constraints such as CPU, memory, timeout, network, and storage;
- policy decisions such as no-network or constrained write scope;
- RunEvidence records that point to outputs, logs, provenance, and telemetry;
- optional CAP-Digest views over RunEvidence.

## Profile-Owned Semantics

These semantics belong to this profile or external standards, not to Core:

- table/dataframe interpretation;
- notebook, script, workflow, or ML experiment semantics;
- result metrics and scientific validity;
- reproducibility scoring;
- domain-specific metadata;
- provenance profile selection.

## Fixture Basis

The profile is currently represented by:

```text
fixtures/core/local-analysis/
```

That fixture demonstrates:

- dataset, script, config, environment, output, and log artifacts;
- `run-analysis` capability;
- runtime/resource/policy/evidence/digest/data-plane/transport bindings;
- policy decision with network disabled;
- completed Run;
- RunEvidence with output, log, provenance, telemetry, and digest references.

## Relationship to Build/Test

`fixtures/core/build-test/` is not a scientific-analysis fixture, but it uses the
same Core object model to prove the model is not tied to one domain. Shared
semantics should remain in Core only when both fixtures need them without
requiring domain interpretation.

## Deferrals

- No mandatory workflow language.
- No mandatory container or scheduler format.
- No policy language.
- No provenance ontology.
- No claim that CAP-Core proves scientific correctness.
- No normative promotion without a future CAPP.
