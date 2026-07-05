# Vision and Scope

> Status: draft · Stability: stable · Depends on: [Glossary](02-glossary.md)

## One-Sentence Definition

CAP-Digest is a profile of CAP for assembling complex source objects into
AI-readable context digests with stable field IDs, DigestManifest-backed
traceability, privacy controls, and gated follow-up.

## The Problem

Software traditionally exposes results to two kinds of consumers:

1. Humans, through printed output, tables, charts, reports, and dashboards.
2. Programs, through objects, APIs, schemas, and serialized data.

Agents add a third consumer:

3. Models and agent runtimes, which need compact context, stable references,
   evidence anchors, caveats, and safe follow-up mechanisms.

This third consumer is different. A human can inspect a table visually and ask
for clarification. A program can consume exact schemas. A model needs enough
structured context to reason, but not so much raw data that it exceeds budget,
leaks secrets, or confuses data strings with instructions.

## Design Thesis

CAP-Digest treats context as a governed artifact:

```text
Digest(source, budget, intent, policy) = Assemble(Fields(source), budget, intent, policy)
```

The digest is not:

- the source object;
- a full serialization;
- a natural-language summary;
- a screenshot;
- an unchecked prompt snippet.

The digest is:

- budgeted;
- field-addressable;
- redacted;
- caveated;
- backed by a DigestManifest;
- suitable for validation and replay;
- capable of gated follow-up.

## Primary Audiences

### Agent Hosts

Hosts need to decide what context enters the model and what actions the model can
request afterward. CAP-Digest gives hosts a digest artifact, a DigestManifest,
and a gate model instead of forcing them to trust free-form text.

### Source Implementers

Library authors and service owners need to expose complex objects to agents
without handing over unsafe methods or raw data. CAP-Digest gives them fields,
levels, execution classes, and redaction hooks.

### Digest Pack Authors

Pack authors need to distribute reusable object-reading logic. CAP-Digest gives
them a packaging model based on progressive disclosure and conformance fixtures.

### Model Consumers

Models and downstream agents need stable references for claims and requests.
CAP-Digest gives them field IDs and a structured response contract.

## In Scope

CAP-Digest v0.1 specifies:

- source references;
- field catalogs;
- field levels and budget selection;
- digest text format;
- DigestManifest schema;
- caveats;
- redaction and data fencing;
- evidence validation;
- follow-up requests;
- gate decisions;
- digest pack structure;
- conformance levels.

## Out of Scope

CAP-Digest v0.1 does not specify:

- a transport protocol;
- a full agent runtime;
- long-term memory;
- semantic proof that claims are true;
- complete PII detection;
- universal object serialization;
- a global registry;
- default persistence of user data;
- automatic execution of model-requested actions.

These exclusions are intentional. CAP-Digest defines how context is assembled
and validated. Other systems decide how agents plan, call tools, manage
identity, or persist memory.

## Key Boundaries

### CAP-Digest Is Not Tool Calling

Tool calling lets models request actions. CAP-Digest lets systems prepare and
validate context. A CAP-Digest follow-up request can be implemented as a tool
call in some hosts, but the CAP-Digest rule is stricter: the model requests a
field; the gate decides whether additional context may be assembled.

### CAP-Digest Is Not A Skill

A skill teaches an agent how to perform a task. A digest pack teaches a
CAP-Digest assembler how to expose a source type. They can be used together, but
they are different artifacts.

### CAP-Digest Is Not A Summary Format

CAP-Digest digest text is human-readable, but its primary purpose is not prose
quality. Its purpose is evidence anchoring, caveat visibility, budget
accounting, and safe continuation.

## Success Criteria

CAP-Digest is successful when independent implementations can:

- produce digest text with stable field IDs;
- emit a DigestManifest that explains selection and rejection;
- validate model evidence mechanically;
- block unknown or unsafe follow-up requests;
- apply redaction before model-visible rendering;
- compare outputs through conformance fixtures.

