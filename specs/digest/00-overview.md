# CAP-Digest Overview

> Status: v1.0 stable with historical draft text · Version: 2026-07-07 · Scope: CAP-Digest profile / context evidence layer

CAP-Digest is a profile of CAP that turns complex source objects into safe,
budgeted, traceable, redacted context artifacts for AI agents.

CAP-Digest is not a tool-calling protocol, not a skill format, and not a general
agent framework. It defines the context layer that sits between a source object
and a model:

```text
source object -> field catalog -> context digest -> model response -> gated follow-up
```

The central artifact is a **context digest**: a model-readable text object plus a
machine-readable DigestManifest that records exactly what was included, omitted,
redacted, downgraded, or made available for follow-up.

## Why CAP-Digest Exists

Agents need to inspect objects that are too large, too unsafe, too sensitive, or
too dynamic to place directly in model context:

- data frames, tables, and query results;
- files, notebooks, reports, plots, and dashboards;
- model objects, statistical outputs, enrichment results, and workflow states;
- lazy or remote data sources;
- runtime objects whose inspection can execute code or trigger I/O.

Naive `print()`, `summary()`, JSON dumps, and screenshots lose the properties
agents need:

- stable evidence anchors;
- explicit budget accounting;
- clear caveats and failure records;
- data minimization and redaction;
- guarded inspection of source objects;
- a safe way for the model to request additional context.

CAP-Digest makes object reading a protocol, not an improvised prompt string.

## Normative Language

This document set uses:

- **MUST** for required behavior.
- **MUST NOT** for prohibited behavior.
- **SHOULD** for recommended behavior with valid exceptions.
- **MAY** for optional behavior.

When a document says "implementation", it means any library, service, SDK,
runtime, plugin, or host component that produces or consumes CAP-Digest artifacts.

## The CAP-Digest Promise

A CAP-Digest-conforming digest lets a host or reviewer answer these questions:

- What source was summarized?
- Which fields were available?
- Which fields were included?
- Which fields were rejected, and why?
- Which values were redacted or truncated?
- What did the model cite?
- What did the model request next?
- Was that request allowed by policy?
- Is the source still the same object version?

CAP-Digest does not make model reasoning trustworthy by itself. It makes the
context surface inspectable, bounded, and enforceable.

## Relationship to CAP-Core

CAP-Digest is the **context evidence layer** of CAP: it specifies how a source
object is safely turned into model-readable context with traceable anchors and
gated follow-up. It is deliberately scoped and does not define artifact graphs,
runtime/capability binding, RunEvidence, or external standard bindings. Those
belong to **CAP-Core**, whose v1.0.0 stable release is tracked separately in
`specs/core/`.

CAP-Core v1.0.0 stability does not promote or change CAP-Digest. CAP-Digest
v1.0.0 is accepted separately by CAPP-0009 through the independent track in
`STABLE-TRACK.md`.

When working in this directory, ask first:

> Is this change refining CAP-Digest, or does it actually belong in CAP-Core?

See `notes/2026-07-05-cognitive-error-and-framework.md` for the analysis that
established this split, and `notes/2026-07-05-deep-research-v2-knowledge-notes.md`
for retained knowledge notes on the broader ecosystem.

## Document Set

Read these files in order:

0. [CAP-Digest Overview](00-overview.md) — this document.
1. [Vision and Scope](01-vision-and-scope.md)
2. [Glossary](02-glossary.md)
3. [Core Data Model](03-core-data-model.md)
4. [Architecture](04-architecture.md)
5. [Field Model and Assembly](05-field-model-and-assembly.md)
6. [Digest Text Format](06-digest-text-format.md)
7. [Digest Manifest and Evidence](07-digest-manifest-and-evidence.md)
8. [Security, Privacy, and Trust](08-security-privacy-trust.md)
9. [Follow-up Contract and Gate](09-followup-contract-and-gate.md)
10. [Digest Packs](10-digest-packs.md)
11. [Versioning, Conformance, and Governance](11-versioning-conformance-governance.md)
12. [Implementation Guide](12-implementation-guide.md)
13. [Stable Track](STABLE-TRACK.md)
14. [Stable Scope v1.0](STABLE-SCOPE-v1.0.md)
15. [Text Grammar v1.0](TEXT-GRAMMAR-v1.0.md)
16. [DigestManifest and Evidence Anchors v1.0](MANIFEST-EVIDENCE-v1.0.md)
17. [Follow-Up Gate v1.0](FOLLOWUP-GATE-v1.0.md)
18. [Schema Package v1.0](SCHEMA-PACKAGE-v1.0.md)
19. [Fixtures v1.0](FIXTURES-v1.0.md)
20. [Conformance v1.0](CONFORMANCE-v1.0.md)
21. [Security v1.0](SECURITY-v1.0.md)
22. [Maintenance v1.0](MAINTENANCE-v1.0.md)
