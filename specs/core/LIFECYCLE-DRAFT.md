# CAP-Core Lifecycle Draft

> Status: planning · Non-normative · Last updated: 2026-07-05

This file proposes a CAP-Core lifecycle for testing the ontology. It is not a
normative state machine.

## Lifecycle hypothesis

CAP-Core should record assembly and run checkpoints rather than define a full
execution engine.

The lifecycle is control-plane oriented:

```text
discover -> describe -> assemble -> bind -> authorize -> record assembly
  -> start run -> observe -> finalize -> record evidence -> render digest view
```

## Stage 1: discover

Goal: find candidate artifacts, capabilities, profiles, and available bindings.

Inputs:

```text
host context
artifact references
capability catalogs
profile registry
binding providers
policy context
```

Outputs:

```text
candidate ArtifactRefs
candidate Capabilities
candidate Profiles
candidate Bindings
```

CAP-Core should not define transport for discovery. Discovery may happen through
MCP, A2A, local host registries, files, databases, workflow engines, or other
systems.

## Stage 2: describe

Goal: normalize enough metadata to decide whether an object can participate in
an Assembly.

Description should answer:

```text
What is it?
What profile constrains it?
What integrity or version anchor exists?
What can act on it?
What policy applies?
```

CAP-Digest may be used to render a model-visible description, but Core should
not require digest text as the only description format.

## Stage 3: assemble

Goal: create a candidate Assembly linking artifacts, capability, profiles, and
binding requirements.

The Assembly should still be pre-execution. It should be safe to review before
anything runs.

Outputs:

```text
Assembly candidate
unresolved bindings
policy questions
resource estimate
```

## Stage 4: bind

Goal: resolve external references without replacing external systems.

Binding categories:

```text
runtime
resource
service
policy
evidence
transport
digest
```

A binding record should contain at least:

```text
binding type
target reference
standard or host system
version or profile
constraints
integrity or freshness anchor when available
```

## Stage 5: authorize

Goal: obtain a policy decision for the candidate Assembly or Run.

CAP-Core should record the decision, not define the policy language.

Possible outcomes:

```text
allowed
denied
allowed_with_constraints
needs_confirmation
stale_context
```

Open question: whether these outcomes should be Core-wide or profile-defined.

## Stage 6: record assembly

Goal: persist or return the Assembly object after bindings and policy are
resolved.

An Assembly record should allow a reviewer to see:

```text
what artifacts were selected
what capability was selected
which runtime/resource/service bindings were resolved
which policy decision applied
what remains unresolved
```

## Stage 7: start run

Goal: create a Run from an Assembly.

CAP-Core should record the run intent and initial state. It should not define how
the runtime executes.

Candidate states:

```text
planned
starting
running
waiting
completed
failed
cancelled
stale
```

## Stage 8: observe

Goal: attach status, logs, metrics, partial outputs, and policy events to the
Run.

Observability systems such as OpenTelemetry or host logs should be bindings, not
Core replacements.

## Stage 9: finalize

Goal: close the Run and record final status.

Finalization should identify:

```text
outputs
errors
resource use
runtime status
policy events
evidence locations
```

## Stage 10: record evidence

Goal: produce RunEvidence or evidence bindings.

RunEvidence may reference:

```text
inputs
parameters
outputs
logs
provenance records
attestations
signatures
SBOMs
metrics
environment locks
CAP-Digest views
```

CAP-Core should define the evidence envelope and references, not the full
content format for every evidence type.

## Stage 11: render digest view

Goal: optionally expose a CAP-Digest view of an Artifact, Assembly, Run, or
RunEvidence object to a model.

Rules:

- DigestEvidence remains model-visible field evidence.
- RunEvidence remains execution/assembly evidence.
- A Digest may cite a RunEvidence reference, but it does not replace it.

## Lifecycle checklist for RFC-0001

RFC-0001 should decide:

- whether the lifecycle is mandatory or explanatory;
- whether Run states are standardized;
- whether policy outcomes are standardized;
- which stages require evidence records;
- how stale or invalid bindings are represented;
- how CAP-Digest views link back to Core objects.
