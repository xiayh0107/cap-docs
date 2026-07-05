# Core Data Model

> Status: draft · Stability: stable · Depends on: [Glossary](02-glossary.md)

This file defines the primary CAP-Digest data structures. Implementations may
use language-specific classes, but serialized forms should preserve these
fields.

## SourceRef

```json
{
  "uri": "session://object/mtcars",
  "sourceType": "table",
  "label": "mtcars",
  "identity": {
    "class": ["data.frame"],
    "binding": "mtcars"
  },
  "trust": "local_session"
}
```

Required fields:

| Field | Type | Meaning |
|---|---|---|
| `uri` | string | Host-scoped source reference. |
| `sourceType` | string | Broad source type. |
| `label` | string or null | Human-readable label. |
| `identity` | object | Implementation-specific identity metadata. |

`trust` is optional and host-defined.

## Field

```json
{
  "id": "f1:table@shape#base",
  "label": "Shape",
  "description": "Rows, columns, and broad table dimensions.",
  "sourceTypes": ["table"],
  "timing": "assemble",
  "trust": "code",
  "exec": "local_cheap",
  "levels": [
    {
      "level": 1,
      "estimatedCost": 24,
      "priorValue": 1.0,
      "description": "Row and column count."
    }
  ]
}
```

Required fields:

| Field | Type | Meaning |
|---|---|---|
| `id` | string | Stable field ID. |
| `label` | string | Human-readable field label. |
| `description` | string | What the field provides. |
| `sourceTypes` | array | Source types the field supports. |
| `timing` | string | `assemble` or `interactive`. |
| `trust` | string | `code`, `derived`, or `data`. |
| `exec` | string | Execution class. |
| `levels` | array | Discrete field levels. |

Field implementations also have extractor, cost estimator, renderer, and
validator logic, but those functions are implementation-local and are not
serialized in the field catalog unless the host supports executable packs.

## Field ID

Recommended syntax:

```text
f1:<source-family>@<field-name>#<variant>
```

Examples:

```text
f1:table@shape#base
f1:table@columns#compact
f1:table@sample#k3
f1:model@formula#base
f1:query@plan#summary
```

Rules:

- Field IDs MUST be stable within a field ID scheme version.
- Field IDs MUST be unique within a digest manifest.
- Field IDs SHOULD avoid spaces.
- Field IDs SHOULD include a scheme prefix such as `f1:`.
- Renaming a field ID is a compatibility change.

## Digest

```json
{
  "schema": "cap.digest.v1",
  "id": "cap-digest-01H...",
  "source": {},
  "text": "cap digest text=v1 ...",
  "manifest": {},
  "budgetUsed": 1180,
  "budgetEstimated": 1234,
  "fingerprint": "structure_v1:ab12cd34",
  "caveats": [],
  "plan": {}
}
```

Required fields:

| Field | Type | Meaning |
|---|---|---|
| `schema` | string | Digest schema identifier. |
| `id` | string | Host-scoped digest ID. |
| `source` | SourceRef | Source reference. |
| `text` | string | Digest text. |
| `manifest` | DigestManifest | Assembly DigestManifest. |
| `budgetUsed` | integer | Actual model-visible token cost if measured. |
| `budgetEstimated` | integer | Estimated cost used during planning. |
| `fingerprint` | string | Source anchor. |
| `caveats` | array | Digest-level caveats. |
| `plan` | object | Allocation plan. |

## DigestManifest

The DigestManifest is defined in [Digest Manifest and Evidence](07-digest-manifest-and-evidence.md).

At minimum, it contains:

- source metadata;
- field rows;
- selected and rejected status;
- estimated and actual cost;
- redaction status;
- warnings and errors;
- fingerprint and tokenizer identity.

## Caveat

```json
{
  "code": "cap_caveat_redacted",
  "severity": "info",
  "fieldId": "f1:table@columns#compact",
  "message": "Values in column api_token were masked.",
  "details": {
    "redactionRule": "sensitive_name"
  }
}
```

Required fields:

| Field | Type | Meaning |
|---|---|---|
| `code` | string | Stable caveat code. |
| `severity` | string | `info`, `warning`, or `error`. |
| `fieldId` | string or null | Field associated with caveat. |
| `message` | string | Human-readable explanation. |

Common caveat codes:

```text
cap_caveat_redacted
cap_caveat_truncated
cap_caveat_timeout
cap_caveat_field_error
cap_caveat_unfingerprintable
cap_caveat_budget_overflow
cap_caveat_policy_blocked
```

## ContractResponse

```json
{
  "claims": [
    {
      "id": "claim-1",
      "text": "The table has 32 rows and 11 columns.",
      "evidence": ["f1:table@shape#base"]
    }
  ],
  "evidence": ["f1:table@shape#base"],
  "warnings": [],
  "requests": []
}
```

The top-level `evidence` array is a convenient union of evidence cited across
claims. Claim-level evidence is recommended.

## FollowupRequest

```json
{
  "fieldId": "f1:table@missingness#full",
  "level": 2,
  "budget": 400,
  "reason": "Missingness is needed before comparing columns."
}
```

The gate may approve, deny, downgrade, or ask the user for confirmation.

## GateDecision

```json
{
  "request": {},
  "decision": "approved",
  "fieldId": "f1:table@missingness#full",
  "level": 1,
  "reason": "Approved at lower level under remaining budget.",
  "requiresUserConfirmation": false
}
```

Allowed decisions:

```text
approved
approved_with_changes
denied
needs_confirmation
stale_source
unknown_field
over_budget
policy_blocked
```

