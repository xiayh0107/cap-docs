# FAQ

## Is CAP-Digest the whole CAP project?

No. CAP-Digest is the current drafted profile. It defines a context evidence layer for turning source objects into model-readable context with stable field anchors, redaction, manifests, and gated follow-up.

CAP-Core is now a non-normative draft-track proposal area. It has split draft
RFCs, schema sketches, and executable fixture prototypes, but it is not a stable
standard and does not define conformance yet.

## Is CAP-Digest a tool-calling protocol?

No. Tool calling lets models request actions. CAP-Digest prepares and validates context. A follow-up request asks for a field; the gate decides whether additional context may be assembled.

## Is a Digest Pack a Skill?

No. A Skill teaches an agent how to perform a task. A Digest Pack teaches a CAP-Digest assembler how to expose a source type safely and consistently.

## Does DigestEvidence prove that a claim is true?

No. DigestEvidence proves only that the model cited a selected field that appeared in the digest text. It does not prove claim truth, semantic entailment, or source correctness.

## Why is CAP-Core separate?

CAP-Core addresses artifact graphs, capability/runtime binding, resource and
service binding, policy decisions, run lifecycle, RunEvidence, provenance, and
external standard bindings. That is a larger problem and should not be smuggled
into CAP-Digest.

## What should implementers build first?

Start with CAP-Digest and one source type. The current executable CAP-Digest
target is `fixtures/basic-table/` plus the minimal Python reference
implementation under `reference/python/`. Treat CAP-Core fixtures as design
prototypes unless a future CAPP promotes Core conformance.
