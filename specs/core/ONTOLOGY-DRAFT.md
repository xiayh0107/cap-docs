# CAP-Core Ontology Draft

> Status: planning · Non-normative · Last updated: 2026-07-05

This file proposes the first CAP-Core object vocabulary. It is a construction
draft, not a normative specification.

## Ontology goal

The ontology should let a host or reviewer answer:

```text
What objects exist?
What capability can act on them?
Where can it run?
What resources and services are bound?
What policy decision allowed or denied the assembly?
What run occurred?
What evidence was produced?
What model-visible digest may summarize it?
```

## Object graph overview

```text
ArtifactRef ──references──> Artifact
Artifact ──constrained by──> Profile
Capability ──accepts/produces──> ArtifactRef
Assembly ──binds──> ArtifactRef + Capability + Binding + PolicyBinding
Run ──instantiates──> Assembly
RunEvidence ──records──> Run
CAP-Digest ──views──> Artifact / Assembly / Run / RunEvidence
```

## Candidate objects

### Artifact

An Artifact is a machine-operable object such as a dataset, file, model, code
object, configuration, notebook, environment reference, log, result, report, or
container reference.

Candidate fields:

```text
id
kind
mediaType or profileType
identity
version or digest
labels
metadata
profiles
bindings
```

Open question: should environment references be artifacts or runtime bindings?

### ArtifactRef

An ArtifactRef is a reference to an Artifact. It may be host-scoped,
content-addressed, URI-addressed, or profile-defined.

Candidate fields:

```text
ref
scope
kind
integrity
profile
accessHints
```

Core should define reference shape and integrity hooks, but not a universal
storage layer.

### Profile

A Profile constrains how a Core object is interpreted. Profiles may represent
domain schemas, workflow profiles, runtime profiles, evidence profiles, or data
model profiles.

Candidate fields:

```text
id
name
version
appliesTo
schemaRef
constraints
compatibility
```

Profiles should carry domain semantics that do not belong in Core.

### Capability

A Capability is a declared operation that may act on artifacts under explicit
constraints.

Candidate fields:

```text
id
name
description
inputs
outputs
sideEffects
requiredBindings
errorSemantics
profiles
```

A Capability is not a tool call. A tool call or MCP method may implement a
Capability through a Binding.

### Binding

A Binding is a typed edge from a CAP-Core object to an external standard, host
resource, runtime, service, policy decision, evidence object, or profile.

Candidate fields:

```text
id
type
target
standard
version
constraints
integrity
status
```

Possible binding subtypes:

```text
RuntimeBinding
ResourceBinding
ServiceBinding
PolicyBinding
EvidenceBinding
TransportBinding
DigestBinding
```

Open question: whether these should be subtype values or separate top-level
objects.

### RuntimeBinding

A RuntimeBinding connects a Capability or Assembly to a concrete runtime
reference such as local process, OCI container, WASI component, Kubernetes job,
HPC scheduler, or remote execution backend.

Candidate fields:

```text
runtimeType
runtimeRef
platform
entrypoint
constraints
isolation
```

Core should reference runtime systems; it should not define runtime execution
semantics.

### ResourceBinding

A ResourceBinding defines a resource envelope.

Candidate fields:

```text
cpu
memory
gpu
timeout
network
storage
locality
costBudget
```

ResourceBinding exists because agent actions need bounded resource commitments
before execution.

### ServiceBinding

A ServiceBinding declares a required external service, such as object storage,
database, model service, license server, API, or secret provider.

Candidate fields:

```text
serviceType
serviceRef
accessMode
secretRefs
networkPolicy
dataPolicy
```

Core should not carry secret values.

### PolicyBinding

A PolicyBinding records the policy basis for an Assembly or Run.

Candidate fields:

```text
principal
action
resource
policyRef
decision
decisionTime
conditions
obligations
auditRef
```

Open question: should CAP-Core require a decision object or allow external-only
policy references?

### Assembly

An Assembly is the resolved contract connecting artifacts, capabilities,
bindings, profiles, and policy.

Candidate fields:

```text
id
artifacts
capability
profiles
bindings
policyBinding
state
createdAt
createdBy
```

Assembly is likely the central CAP-Core object. It says what is assembled before
anything runs.

### Run

A Run is an instance created from an Assembly.

Candidate fields:

```text
id
assemblyId
state
startedAt
endedAt
inputs
outputs
runtimeBinding
resourceBinding
serviceBindings
logs
evidenceRefs
```

Open question: should Core define a strict state machine or only checkpoint
names?

### RunEvidence

RunEvidence is an envelope of records produced by a Run. It may reference logs,
outputs, provenance, signatures, attestations, dependency inventories, metrics,
and CAP-Digest views.

Candidate fields:

```text
id
runId
evidenceType
profile
subject
materials
products
logs
attestations
provenanceRefs
sbomRefs
digestViews
completeness
```

RunEvidence must remain distinct from DigestEvidence. RunEvidence records what
happened during assembly or execution. DigestEvidence records what the model saw
in a digest.

## Candidate minimal graph

The first RFC should test this minimal graph:

```text
ArtifactRef[]
Capability
Assembly
  bindings: RuntimeBinding, ResourceBinding, PolicyBinding
Run
RunEvidence
DigestBinding -> CAP-Digest
```

## Naming constraints

CAP-Core should avoid reusing CAP-Digest names with different meanings. In
particular:

| Avoid | Use |
|---|---|
| Evidence | RunEvidence or DigestEvidence |
| Field | Artifact attribute, Capability input, or Digest Field |
| Gate | PolicyBinding or PolicyDecision |
| Context Pack | Profile or Binding package |
| Capability Discovery | Capability catalog or binding discovery |

## Next step

Use `EXAMPLE-ASSEMBLY-0001.md` to test whether these objects are sufficient
before drafting `RFC-0001.md`.
