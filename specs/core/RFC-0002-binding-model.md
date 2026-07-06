# CAP-Core RFC-0002: Binding Model

> Status: draft proposal - Non-normative - Last updated: 2026-07-06

This split draft defines the generic CAP-Core Binding envelope and binding role
policy. It does not define external standard semantics and does not create
stable CAP-Core conformance.

## Scope

The Binding model owns the typed edge from CAP-Core records to external systems:

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

## Binding Roles

| Role | Purpose | External owner |
|---|---|---|
| `runtime` | Runtime handle for review or execution. | OCI, WASI, Kubernetes, Slurm, REAPI, local host, workflow engine. |
| `resource` | CPU, memory, GPU, time, network, storage, locality, or cost envelope. | Host scheduler, cluster, cloud/HPC quota system. |
| `service` | External service dependency and access mode. | Object store, database, model API, secret store, license service. |
| `policy` | Policy decision basis and audit link. | OPA, Cedar, IAM, OAuth/OIDC, SPIFFE/SPIRE, host policy. |
| `evidence` | Evidence location or evidence family reference. | W3C PROV, Workflow Run RO-Crate, in-toto, Sigstore, SBOM, telemetry, logs. |
| `digest` | Bridge to a CAP-Digest view. | CAP-Digest bridge profile. |
| `transport` | Host/tool/agent transport endpoint. | MCP, A2A, HTTP APIs, host tool APIs, message buses. |
| `data-plane` | Storage or transfer handle. | Filesystems, object stores, Arrow Flight, content-addressed stores. |
| `schema` | Validation or semantic interpretation hook. | JSON Schema, JSON-LD, SHACL, CodeMeta, domain schemas. |

## Status Values

```text
candidate
resolved
denied
stale
unavailable
deferred
```

These values describe binding readiness. They are not a full state machine.

## Boundary Rules

- Bindings identify what Core relies on; they do not copy external formats.
- Runtime bindings do not define execution behavior.
- Resource bindings do not define scheduler behavior.
- Policy bindings do not define policy language or identity semantics.
- Evidence bindings do not define provenance, attestation, SBOM, or telemetry
  formats.
- Service bindings may reference secret requirements but must not carry secret
  values.
- Digest bindings must preserve the distinction between RunEvidence and
  DigestEvidence.

## Draft Schema

The draft schema is:

```text
schemas/core/cap.core.binding.v1.schema.json
```

The schema is a sketch and remains non-normative.

## Fixtures

The binding model is exercised by:

- `fixtures/core/local-analysis/assembly.json`
- `fixtures/core/local-analysis/digest-view-ref.json`
- `fixtures/core/build-test/assembly.json`
- `fixtures/core/build-test/digest-view-ref.json`

The `build-test` fixture adds schema and transport binding examples beyond the
first local-analysis fixture.
