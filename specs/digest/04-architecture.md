# Architecture

> Status: draft · Stability: stable · Depends on: [Core Data Model](03-core-data-model.md)

## Participants

CAP-Digest defines logical participants. One implementation may combine several
roles.

| Participant | Responsibility |
|---|---|
| Host | Owns user interaction, model context, policy, permissions, and display. |
| Assembler | Produces field catalogs, context digests, DigestManifests, and patches. |
| Source Provider | Owns or exposes source objects. |
| Consumer | Reads digest text and returns claims, evidence, warnings, and requests. |
| Gate | Validates evidence and follow-up requests. |
| Digest Pack | Provides reusable fields, renderers, redactors, and fixtures. | |

The host is responsible for user-facing policy. The assembler is responsible for
correct CAP-Digest artifacts. The gate is responsible for enforcement before
follow-up assembly.

## Lifecycle

```text
1. Discover assembler capabilities
2. Identify source
3. Build or load field catalog
4. Allocate budget
5. Extract and render selected fields
6. Return context digest
7. Consume digest
8. Validate contract response
9. Gate follow-up requests
10. Return digest patch or replacement digest
```

## Capability Discovery

An assembler SHOULD expose a capability document:

```json
{
  "capVersion": "2026-07-04-draft",
  "implementation": {
    "name": "example-cap-assembler",
    "version": "0.1.0"
  },
  "features": {
    "digestTextV1": true,
    "manifestV1": true,
    "fieldCatalog": true,
    "followupRequests": true,
    "digestPacks": true,
    "digestPatch": false
  },
  "limits": {
    "maxInitialBudget": 20000,
    "maxFollowupRequests": 5,
    "maxFieldBlocks": 200
  }
}
```

Capability discovery lets hosts adapt. It MUST NOT be used as a security
boundary. Hosts still enforce policy.

## Source Identification

A source reference identifies the object being assembled:

```json
{
  "uri": "session://object/analysis_result",
  "sourceType": "analysis_result",
  "label": "analysis_result",
  "identity": {
    "binding": "analysis_result",
    "class": ["example_result"]
  }
}
```

The `uri` is scoped to the host or provider. It does not imply universal
addressability.

## Field Catalog Construction

The assembler builds a field catalog from:

- built-in fields;
- source-type fields;
- digest packs;
- host policy;
- source-specific metadata;
- user intent.

Catalog construction SHOULD be cheap. If discovering a field requires expensive
I/O or computation, the field should be represented as `interactive` or marked
with a higher execution class.

## Budget Allocation

The assembler chooses field levels under budget. CAP-Digest does not require one
specific allocator, but output MUST be explainable in the DigestManifest.

A recommended v0.1 allocator is:

1. Expand each field into discrete candidate levels.
2. Compute estimated token cost and value.
3. Reject candidates prohibited by policy.
4. Sort by value-to-cost ratio, then deterministic tie breakers.
5. Select until budget is exhausted.
6. Record selected and rejected candidates in the DigestManifest.

Tie breakers SHOULD include field ID and level so repeated runs are stable.

## Guarded Extraction

Any source touch can execute code, trigger I/O, or allocate large memory.
CAP-Digest therefore treats extraction and rendering as guarded operations.

The assembler MUST record failures as field-level DigestManifest rows and
caveats. One failed field MUST NOT invalidate the entire digest unless host
policy requires fail-closed behavior.

## Redaction and Rendering

Rendering order:

```text
extract -> redact -> render -> escape data fences -> assemble digest text
```

Redaction happens before rendering so sensitive values are not hidden from the
redactor by truncation, formatting, or escaping.

## Consumption and Contract

Digest text MAY include a contract block instructing the model to return:

```json
{"claims":[],"evidence":[],"warnings":[],"requests":[]}
```

The host or gate parses this response and validates field IDs. Invalid evidence
or requests are rejected mechanically.

## Follow-Up

A model may request more context by field ID. The gate checks:

- field exists and is available;
- source fingerprint still matches;
- budget remains or is approved;
- execution class is allowed;
- privacy policy allows the field;
- user or host confirmation is satisfied.

Approved follow-up returns either a digest patch or a replacement digest.

## Failure Philosophy

CAP-Digest favors partial, explicit output over silent failure. When safe to do
so, an assembler should return a minimal digest containing:

- version line;
- source identity if known;
- caveats;
- DigestManifest rows for failed fields.

An empty digest with no explanation is not CAP-Digest-conforming.

