# Profile and Binding Registry Draft

> Status: candidate-prep draft - Non-normative - Last updated: 2026-07-07

This registry lists profile and binding families without making external
standards part of minimal Core.

## Entry Fields

Each future registration should record:

- identifier and display name;
- role or profile family;
- owner or external standard body;
- status: `reference-only`, `candidate-binding`, `deferred`, or `out-of-scope`;
- Core object fields touched;
- fixture evidence;
- validator behavior;
- security considerations;
- CAPP or review link.

## Candidate Families

| Family | Role/profile | Status |
|---|---|---|
| MCP | transport/service | reference-only |
| A2A | transport/service | reference-only |
| Skills | capability/transport | reference-only |
| CWL | runtime/workflow profile | deferred |
| WDL | runtime/workflow profile | deferred |
| Nextflow | runtime/workflow profile | deferred |
| Snakemake | runtime/workflow profile | deferred |
| RO-Crate | evidence/artifact package | reference-only |
| OCI | runtime | candidate-binding |
| WASI | runtime | reference-only |
| Kubernetes | runtime/resource | deferred |
| Slurm | runtime/resource | reference-only |
| REAPI | runtime/resource | reference-only |
| W3C PROV | evidence | reference-only |
| in-toto | evidence/attestation | reference-only |
| Sigstore | evidence/attestation | reference-only |
| SLSA | evidence/attestation | reference-only |
| SPDX | evidence/SBOM | reference-only |
| CycloneDX | evidence/SBOM | reference-only |
| OPA | policy | reference-only |
| Cedar | policy | reference-only |
| OpenTelemetry | evidence/telemetry | reference-only |
| Arrow Flight | data-plane | reference-only |
| JSON Schema | schema | candidate-binding |
| JSON-LD | schema/semantic profile | deferred |
| SHACL | schema/semantic profile | deferred |

## Governance

New or changed registry entries go through CAPP when they affect Core fields,
conformance claims, security posture, or lifecycle status. External standard
schemas are referenced or profiled; they are not copied inline into Core schema
files.
