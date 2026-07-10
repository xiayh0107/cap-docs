# CAP-Digest Implementer and Adoption Guide v1.0

> Status: stable v1.0 - Implementer guidance - Last updated: 2026-07-10

This guide summarizes the stable adoption path for CAP-Digest v1.0.0.

## Start With L0/L1

Implement:

- source reference and fingerprint;
- field catalog;
- deterministic field selection;
- digest text writer;
- `DigestManifest` writer;
- redaction before rendering;
- evidence validation.

Use `fixtures/basic-table/` and `fixtures/security-adversarial/` as the first
compatibility target.

## Design the Host Adapter Boundary

Before adding many host-language object classes, define an open source-adapter
boundary. Read [CAP-Digest Source Adapter Guide](SOURCE-ADAPTER-GUIDE.md).

A host implementation should:

- resolve one adapter and keep the core assembly pipeline class-independent;
- separate concrete host classes from broad source-family semantics;
- keep serialized field contracts symbolic and runtime functions host-local;
- make registry resolution deterministic and fail closed on ambiguity;
- preserve adapter identity and compatible bindings across follow-up;
- label generic structural fallback as non-semantic and non-conformant.

Adding a community adapter may produce valid CAP artifacts, but it does not
expand the CAP-Digest v1.0 stable table fixture claim.

## Add L2 Follow-Up

Only after L0/L1 works, implement contract response validation and the follow-up
gate. Models request fields; implementation code enforces the gate and extracts
approved fields.

## Add L3 Pack Hosting

Load Digest Pack metadata fail-closed. Do not execute pack-provided code as
part of a v1.0 claim.

## Adoption Notes

Adopters should publish:

- claimed CAP-Digest level;
- fixture suite version;
- unsupported features;
- conformance report;
- security notes for redaction and extraction;
- whether the implementation is independent or derived from `reference/python/`;
- stable, community, experimental, and fallback adapter scopes separately.

## Out-of-Scope Integrations

Remote sources, credentials, large-source streaming, and second source-type
fixtures are candidates for post-v1.0 work, not requirements for the v1.0.0
stable claim.
