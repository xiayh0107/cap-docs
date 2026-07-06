# CAP-Core External Standard Binding Policy

> Status: draft - Non-normative - Last updated: 2026-07-05

This file defines the first CAP-Core policy for referencing external standards
and host systems. It is a draft source for RFC-0001 and contains no stable
conformance requirements.

## Binding principle

CAP-Core should define the control-plane record that says what is bound. It
should not define the data plane, transport, runtime, policy language,
provenance ontology, attestation format, SBOM format, or observability protocol
owned by another standard.

## Minimal binding envelope

The first RFC-0001 draft should use one minimal envelope for all external
bindings:

```text
id
type
target
standard
standardVersion
profile
constraints
integrity
freshness
status
evidenceRefs
```

Field intent:

| Field | Intent |
|---|---|
| `id` | Assembly-local or globally scoped binding identifier. |
| `type` | Binding role such as runtime, resource, service, policy, evidence, transport, digest, data-plane, or schema. |
| `target` | URI, host reference, registry reference, or profile-defined locator. |
| `standard` | Source label or URI for the external standard or host system. |
| `standardVersion` | Version, release, profile, or date when available. |
| `profile` | Optional CAP profile or external profile that interprets the binding. |
| `constraints` | Bounded requirements that the Assembly relies on. |
| `integrity` | Digest, signature, immutable revision, or other integrity anchor when available. |
| `freshness` | Timestamp, observed version, cache status, or staleness marker. |
| `status` | Candidate, resolved, denied, stale, unavailable, or deferred. |
| `evidenceRefs` | Pointers to policy, resolver, provenance, audit, or digest evidence. |

## Binding categories

| Category | External examples | CAP-Core behavior |
|---|---|---|
| Agent connection | MCP, A2A, host tool APIs | Reference the transport endpoint or catalog; do not define message protocol. |
| Procedure packaging | Codex Skills, Anthropic Skills, Copilot instructions | Reference instruction packages; do not treat them as executable contracts. |
| Workflow | CWL, WDL, Nextflow, Snakemake | Bind as workflow profiles; do not define workflow language semantics. |
| Research object package | RO-Crate, Workflow Run RO-Crate, BagIt | Bind archives or provenance profiles; do not redefine package layout. |
| Runtime | OCI, WASI, local process, Kubernetes, Slurm, REAPI | Reference runtime target and constraints; do not define scheduler or execution behavior. |
| Resource | Kubernetes resources, Slurm allocations, cloud/HPC quotas | Record resource envelope relied on by the Assembly. |
| Service | Object stores, databases, model APIs, secret stores, license services | Record required service references and access mode; do not carry secret values. |
| Policy | OPA, Cedar, OAuth/OIDC, SPIFFE/SPIRE, IAM | Record decision and policy reference; do not define policy language or identity protocol. |
| Provenance | W3C PROV, Workflow Run RO-Crate, MLflow, DataLad | Reference provenance record or profile; do not define full provenance ontology. |
| Supply chain | in-toto, SLSA, Sigstore, SPDX, CycloneDX | Reference attestations, signatures, or BOMs; do not define their formats. |
| Observability | OpenTelemetry, host logs, runtime metrics | Reference telemetry streams or snapshots; do not define telemetry protocol. |
| Data plane | Arrow Flight, object stores, filesystems, content-addressed stores | Reference storage/stream handle; do not move large bytes through Core records. |
| Schema/semantics | JSON Schema, JSON-LD, SHACL, CodeMeta | Reference schema or semantic profile; do not require one semantic stack for all objects. |

## Binding status values

The first draft should use descriptive status values without claiming a complete
state machine:

| Status | Meaning |
|---|---|
| `candidate` | Found during discovery but not yet selected. |
| `resolved` | Selected and sufficiently identified for review or run creation. |
| `denied` | Rejected by policy or host constraints. |
| `stale` | Previously resolved but no longer fresh enough for use. |
| `unavailable` | Required target cannot be reached or verified. |
| `deferred` | Not needed for the current run or intentionally left to a profile. |

## Integrity and freshness

Bindings should carry integrity and freshness anchors when the external system
can supply them. Examples:

- content digest for files, object-store objects, OCI descriptors, or packages;
- commit SHA for repository references;
- image digest for OCI images;
- policy decision timestamp and policy revision;
- run or trace identifier for evidence references;
- schema version or profile version for validation bindings.

When an anchor is not available, the binding should say so explicitly rather
than implying stronger reproducibility than the host can prove.

## Registry policy

RFC-0001 should not create a central CAP-Core external-standard registry. The
first draft should use:

- stable source labels from `RESEARCH-SOURCES.md`;
- source URLs or standard URIs;
- profile identifiers for domain-specific interpretation;
- explicit version/date reviewed fields where relevant.

A future registry can be proposed only after fixtures show that URI/profile
references are insufficient.

## Non-goals

CAP-Core binding records must not:

- define a new transport protocol;
- define a workflow language;
- define a runtime, container, sandbox, or scheduler;
- define a policy language or identity provider;
- carry secret values;
- define a provenance ontology;
- define an SBOM or attestation format;
- carry large artifact bytes;
- claim that a referenced standard proves semantic correctness.

## RFC-0001 draft conclusion

The binding policy is mature enough for a first RFC draft because it keeps
CAP-Core as a small assembly control plane. The policy is not mature enough for
stable conformance until at least one schema sketch and fixture exercise
runtime, resource, policy, evidence, and digest bindings together.
