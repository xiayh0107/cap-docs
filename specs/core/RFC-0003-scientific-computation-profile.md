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

Core-level validators should not enforce these semantics unless a profile check
is explicitly active. The current reference validator stays at Core level for
shared object closure, policy, secret, binding, Run, and RunEvidence checks.

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

## Fixture Mapping

| Profile role | Fixture artifact or field | Core object surface |
|---|---|---|
| dataset | `artifact.dataset.orders` | `Artifact.kind = data`, profile-owned table semantics |
| script | `artifact.script.analyze` | `Artifact.kind = code`, profile-owned Python semantics |
| config | `artifact.config.analysis` | `Artifact.kind = config`, profile-owned analysis config |
| environment | `artifact.environment.analysis` | `Artifact.kind = environment`, OCI binding reference |
| output summary | `artifact.output.summary` | `Artifact.kind = result`, product of RunEvidence |
| plot | `artifact.output.plot` | `Artifact.kind = result`, optional profile output |
| run log | `artifact.log.run` | `Artifact.kind = log`, Run and RunEvidence log ref |
| resource envelope | `binding.resource.local-analysis` | Binding with profile-owned CPU/memory/network details |
| digest view | `binding.digest.run-summary` | CAP-Digest bridge binding, not replacement evidence |

## Non-Claims

The fixture does not prove scientific correctness, reproducibility scoring,
statistical validity, or workflow-language compatibility. Reproducibility
caveats are evidence limitations unless a future profile adds explicit checks.

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
