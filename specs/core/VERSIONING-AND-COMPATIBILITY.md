# CAP-Core Versioning and Compatibility

> Status: candidate-prep draft - Non-normative - Last updated: 2026-07-07

This document defines the compatibility contract CAP-Core needs before any Core
schema can become candidate normative. It does not freeze the current schemas.

## Version Fields and Schema References

Core records identify their schema with a `schema` string such as
`cap.core.run.v1`. Schema files use the matching path pattern:

```text
schemas/core/cap.core.<object>.<major>.schema.json
```

Fixtures pin schema versions by using the exact `schema` value in each record.
Validators must report unsupported future versions as `unsupported_core_schema`
instead of silently accepting them.

## Change Classes

| Change | Compatibility |
|---|---|
| Add optional field | Additive when unknown fields can be preserved. |
| Add required field | Breaking for the same major version. |
| Remove field | Breaking unless the field was explicitly deprecated first. |
| Tighten enum | Breaking. |
| Add enum value | Additive only when validators treat unknown values as unsupported, not valid. |
| Change field meaning | Breaking even if JSON shape is unchanged. |

## Unknown Fields

Core objects allow unknown fields while draft-track. Implementations must
preserve unknown fields they read and must not infer Core semantics from
unknown fields. Profile-owned unknown fields should use a namespaced profile,
for example `profile.example.remote-service.v0`.

## Enum Extension Policy

Core enum values are closed for a given major schema. New Core enum values
require a schema update and fixture coverage. Profile-specific values must live
inside profile metadata or constraints, not in Core enum fields.

## ID, Reference, and Canonicalization Rules

IDs are fixture-local stable strings. References must point to known object IDs
within the Core package unless a field explicitly accepts an external URI.
Canonical validation order is:

```text
schema parse -> object id inventory -> reference closure -> policy/binding checks -> evidence checks
```

Duplicate IDs are invalid. Missing references are invalid for candidate
conformance levels that require graph closure.

## Fixture Pinning

Each fixture family must state the target schema versions in its records and
expected validation output. Candidate fixtures must not rely on implicit latest
schema behavior.
