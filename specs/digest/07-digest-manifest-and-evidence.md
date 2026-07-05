# Digest Manifest and Evidence

> Status: draft · Stability: stable · Depends on: [Digest Text Format](06-digest-text-format.md)

The DigestManifest is the black-box recorder for CAP-Digest assembly. It exists
because model context alone is not enough to audit what happened.

## DigestManifest Requirements

A CAP-Digest DigestManifest MUST record:

- the source reference;
- the digest format version;
- the field ID scheme version;
- selected fields;
- rejected fields;
- estimated and actual cost;
- trust and execution classes;
- redaction status;
- warnings, errors, and elapsed time;
- source fingerprint;
- tokenizer or estimator identity.

## Recommended JSON Shape

```json
{
  "schema": "cap.manifest.v1",
  "digestId": "cap-digest-01H...",
  "source": {
    "uri": "session://object/mtcars",
    "sourceType": "table",
    "label": "mtcars"
  },
  "versions": {
    "cap": "2026-07-04-draft",
    "text": "v1",
    "fields": "f1",
    "manifest": "v1"
  },
  "budget": {
    "requested": 2000,
    "estimated": 1234,
    "used": 1180,
    "tokenizer": "heuristic_v1"
  },
  "fingerprint": "structure_v1:ab12cd34",
  "fields": []
}
```

## DigestManifest Field Row

```json
{
  "fieldId": "f1:table@columns#compact",
  "fieldLabel": "Columns",
  "sourceType": "table",
  "timing": "assemble",
  "trust": "derived",
  "exec": "local_cheap",
  "level": 2,
  "selected": true,
  "rejectedReason": null,
  "estimatedCost": 180,
  "actualCost": 172,
  "priorValue": 1.2,
  "renderMethod": "table_columns_compact_v1",
  "redacted": true,
  "ok": true,
  "warnings": ["values in api_token masked"],
  "errorClass": null,
  "elapsedMs": 6,
  "fingerprint": "structure_v1:ab12cd34",
  "tokenizer": "heuristic_v1"
}
```

## Rejected Fields

Rejected fields MUST be recorded when they were candidates.

Common rejection reasons:

```text
over_budget
lower_value
policy_blocked
interactive_only
exec_not_allowed
level_superseded
source_not_supported
field_validation_failed
```

Rejected fields matter because they tell the model and host what was omitted and
what may be available through follow-up.

## DigestEvidence Model

DigestEvidence is a list of field IDs cited by a model.

CAP-Digest validates DigestEvidence mechanically:

```text
For every evidence field ID:
  it must exist in DigestManifest.fields
  it must have selected = true
  it must be present in digest text
```

If a model cites a rejected or unknown field, validation fails.

## What DigestEvidence Validation Does Not Prove

DigestEvidence validation does not prove:

- the claim is true;
- the cited field semantically supports the claim;
- the source data is correct;
- the model ignored all other context.

It proves only that the model cited a field that was actually available in the
digest. This limited guarantee is still valuable because it blocks hallucinated
field IDs and enables audit.

## Claim-Level DigestEvidence

Recommended contract response:

```json
{
  "claims": [
    {
      "id": "claim-1",
      "text": "The data set contains 32 rows.",
      "evidence": ["f1:table@shape#base"]
    }
  ],
  "evidence": ["f1:table@shape#base"],
  "warnings": [],
  "requests": []
}
```

Claim-level DigestEvidence is more useful than a single global evidence list, but
the global list helps simple validators.

## DigestManifest As Single Source Of Truth

Implementations SHOULD avoid duplicate stores of selected, rejected, or
available fields. If a convenience accessor exists, it should derive from the
DigestManifest.

Examples:

```text
selected_fields = manifest.fields where selected = true
rejected_fields = manifest.fields where selected = false
available_on_request = manifest.fields where timing = interactive
```

## Token Accounting

The DigestManifest SHOULD distinguish:

- estimated cost used for planning;
- actual cost after rendering;
- tokenizer or estimator identity.

If actual cost exceeds budget, the digest MAY still be returned, but it MUST
record a budget overflow caveat unless host policy requires fail-closed.

## DigestManifest Compatibility

Readers SHOULD tolerate unknown additional columns. Writers MUST NOT remove or
change the meaning of required columns without changing the DigestManifest
schema version.

