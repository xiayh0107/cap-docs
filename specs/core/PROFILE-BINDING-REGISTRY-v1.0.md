# CAP-Core v1.0 Profile and Binding Registry Status

> Status: stable v1.0 registry snapshot - Last updated: 2026-07-07

This v1.0 registry snapshot classifies profile and binding families for release
notes. It does not make external standards part of minimal Core.

## Status Terms

| Status | Meaning |
|---|---|
| stable-reference | Stable Core can reference this family in bindings or docs. |
| candidate-binding | Fixture-backed binding family used by v1.0 evidence. |
| draft-profile | Profile document exists but profile semantics are not minimal Core. |
| deferred | Recognized family outside v1.0 evidence. |
| out-of-scope | Not part of v1.0. |

## Snapshot

| Family | v1.0 status |
|---|---|
| CAP-Digest bridge | draft-profile |
| Scientific Computation Profile | draft-profile |
| OCI | candidate-binding |
| JSON Schema | candidate-binding |
| local host process/filesystem | candidate-binding |
| HTTP/HTTPS service binding | candidate-binding |
| W3C PROV, in-toto, Sigstore, SLSA, SPDX, CycloneDX, OpenTelemetry | stable-reference |
| OPA, Cedar | stable-reference |
| MCP, A2A, Skills, WASI, Slurm, REAPI, Arrow Flight, JSON-LD, SHACL | stable-reference |
| CWL, WDL, Nextflow, Snakemake, Kubernetes | deferred |

External standards are referenced or profiled. Their schemas are not copied
into minimal Core requirements.
