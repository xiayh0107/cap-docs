# CAP-Core Boundary Matrix

> Status: planning · Non-normative · Last updated: 2026-07-05

This document is the first construction artifact for CAP-Core. It records where
candidate concepts should live before any RFC-0001 normative text is drafted.

## Boundary rule

A concept belongs in CAP-Core only when it is needed to connect artifacts,
capabilities, bindings, policy decisions, runs, and evidence across otherwise
separate systems.

A concept does **not** belong in CAP-Core merely because an agent might use it.
If an existing standard already defines the object or execution semantics,
CAP-Core should bind to it rather than copy it.

## Layer definitions

| Layer | Meaning |
|---|---|
| Core | Minimal cross-layer object assembly contract. |
| Profile | Domain or execution-specific specialization of Core. |
| Binding | Typed reference from Core to an external standard, runtime, service, policy, or evidence system. |
| Digest | CAP-Digest context evidence view. |
| External | Existing standard or host system that CAP should not redefine. |
| Out of scope | Useful to agents but not part of CAP. |

## Candidate boundary matrix

| Concept | Proposed location | Rationale |
|---|---|---|
| Artifact identity and typed references | Core | Needed to connect data, code, configs, models, logs, environments, and results. |
| Artifact bytes or large data transfer | External | Data planes should use object stores, Arrow Flight, content-addressed storage, filesystems, or domain systems. |
| Artifact graph edges | Core | Core needs typed edges such as input, output, dependency, derived-from, and evidence-for. |
| Domain-specific artifact schema | Profile | BIDS, ML experiment metadata, notebook metadata, and workflow-specific schemas are profile concerns. |
| Capability declaration | Core | Core needs a stable contract for what operation can act on which artifacts. |
| Tool invocation transport | External | MCP, A2A, host tool APIs, and agent runtimes should handle transport. |
| Workflow language | External / Profile | CWL, WDL, Nextflow, Snakemake, Temporal, and Prefect should not be redefined. |
| Runtime reference | Core as binding handle | Core should declare a binding, not define the runtime. |
| Container or sandbox format | External | OCI, WASI, Nix, Conda, and VM/container systems define runtime formats. |
| Resource envelope | Core | CPU, memory, GPU, time, network, storage, and locality budgets are needed for assembly decisions. |
| Scheduler behavior | External | Kubernetes, Slurm, REAPI, Temporal, and Prefect define scheduling/execution behavior. |
| Service reference | Core as binding handle | Core should declare service dependencies without defining the service protocol. |
| Secrets management | External | Secret stores and host policy own secret material. Core may reference secret requirements, not values. |
| Policy decision record | Core | Assemblies need evidence of what was allowed, denied, or deferred. |
| Policy language | External | OPA/Rego, Cedar, IAM systems, OAuth/OIDC, and enterprise policy systems should not be replaced. |
| Run lifecycle record | Core | Core needs a run record to connect assembly, execution state, and evidence. |
| Runtime execution engine | External | CAP-Core must not become an agent runtime or workflow engine. |
| RunEvidence envelope | Core | Core needs a typed envelope for evidence references and completeness claims. |
| Full provenance ontology | External / Binding | W3C PROV and Workflow Run RO-Crate should be reused or mapped. |
| Signing and attestation format | External / Binding | in-toto, DSSE, Sigstore, and SLSA define evidence formats. |
| SBOM and dependency inventory | External / Binding | SPDX and CycloneDX define these formats. |
| Observability traces/logs/metrics | External / Binding | OpenTelemetry and host logs should be referenced, not replaced. |
| Model-visible summary | Digest | CAP-Digest owns field selection, digest text, DigestManifest, and DigestEvidence. |
| Claim truth or semantic entailment | Out of scope | Neither CAP-Core nor CAP-Digest should claim this. |

## Proposed Core minimum

The minimum Core should include these object families:

```text
Artifact / ArtifactRef
Capability
Binding
Profile
Assembly
PolicyBinding
Run
RunEvidence
```

`RuntimeBinding`, `ResourceBinding`, and `ServiceBinding` may either be distinct
objects or typed Binding subtypes. This is an open question for RFC-0001.

## First design hypothesis

CAP-Core should be framed as a **Machine-Operable Object Assembly Contract**.

This phrase is preferred over:

- **Execution Contract**, because CAP-Core should not define an execution engine.
- **Artifact Graph**, because graph identity alone does not bind capability,
  runtime, policy, and evidence.
- **Context Layer**, because CAP-Digest already owns model-visible context.

## Required review before normative drafting

Before this matrix becomes normative, each row must be checked against the
research source map in `RESEARCH-SOURCES.md` and an example assembly in
`EXAMPLE-ASSEMBLY-0001.md`.
