# Glossary

> Status: draft · Stability: stable

## Agent Host

The application or runtime that coordinates the model, user, tools, context, and
policy. A host may include chat applications, coding agents, notebooks, IDEs,
workflow engines, or domain-specific assistants.

## Assembler

The component that implements CAP-Digest assembly. It receives a source
reference, field catalog, budget, intent, and policy; it returns a context
digest.

## Source

The object, data set, file, query, result, runtime state, or service-backed item
being made readable to an agent.

## Source Reference

A structured reference to a source. It identifies what should be read without
necessarily serializing or exposing the source itself.

## Field

A budgetable unit of context. A field has a stable ID, label, extractor,
renderer, trust class, execution class, timing, value prior, and one or more
levels.

## Field Catalog

The list of fields that an assembler can provide for a source, including fields
selected for the current digest and fields available only through follow-up.

## Field ID

A stable identifier used by digest text, manifest rows, model evidence, and
follow-up requests.

## Level

A discrete field variant. Higher levels usually provide more detail and cost
more budget. CAP-Digest uses discrete levels rather than continuous optimization
so behavior can be tested and reproduced.

## Budget

A bounded resource envelope. Token budget is the primary budget in CAP-Digest
v0.1.
Execution cost, latency, remote access, and user confirmation are policy budget
dimensions.

## Context Digest

The main CAP-Digest artifact. It contains model-readable digest text and
associated metadata: DigestManifest, budget use, fingerprint, caveats, and
selection plan.

## Digest Text

The model-visible textual representation of the context digest. It contains a
version line, source line, field blocks, caveats, available-on-request fields,
and optional contract instructions.

## DigestManifest

The machine-readable record of assembly. It records selected and rejected fields,
cost estimates, actual costs, redactions, warnings, errors, elapsed time,
fingerprints, and tokenizer identity.

## Caveat

A visible limitation or warning generated during assembly. Examples include
redaction, truncation, timeout, extraction failure, budget overflow, or
fingerprint failure.

## Fingerprint

An identity or content anchor for the source at the time of assembly. It is used
to detect whether follow-up requests refer to the same source state.

## Trust Class

The classification of field content by instruction risk:

- `code`: implementation-controlled structural text;
- `derived`: summaries computed from source values;
- `data`: source-provided strings or values.

## Execution Class

The classification of a field by execution risk:

- `local_cheap`: cheap local metadata or already materialized values;
- `local_scan`: local scan or computation;
- `remote_query`: network, database, API, or remote execution;
- `unsafe`: requires a stronger sandbox or explicit denial by default.

## Timing

Whether a field is assembled immediately or made available for follow-up:

- `assemble`: eligible for the initial digest;
- `interactive`: available only after gated request.

## Contract Response

A structured response expected from a model after reading a digest:

```json
{
  "claims": [],
  "evidence": [],
  "warnings": [],
  "requests": []
}
```

## DigestEvidence

Field IDs cited by a model to support its claims. CAP-Digest validates whether
cited field IDs exist. It does not prove that claims are semantically entailed.

## Follow-up Request

A model request for additional fields or higher levels. It is not an execution
command. It must pass through a gate.

## Gate

The component that validates contract responses and decides whether follow-up
requests are allowed under DigestManifest, fingerprint, budget, execution,
privacy, and user-confirmation policy.

## Digest Pack

A reusable package of CAP-Digest field definitions, renderers, redactors,
references, and conformance fixtures for a source type or domain.

