# Follow-up Contract and Gate

> Status: draft · Stability: stable · Depends on: [Digest Manifest and Evidence](07-digest-manifest-and-evidence.md)

CAP-Digest follow-up exists because an initial digest is budgeted. The model
may need more context, but it must request that context through field IDs.

## Contract Block

Digest text MAY include:

```xml
<contract>
Reply only as JSON:
{"claims":[],"evidence":[],"warnings":[],"requests":[]}
Evidence and requests must reference field IDs shown in this digest.
</contract>
```

The contract is model guidance. The gate is enforcement.

## ContractResponse Shape

```json
{
  "claims": [
    {
      "id": "claim-1",
      "text": "The table has 11 columns.",
      "evidence": ["f1:table@shape#base"]
    }
  ],
  "evidence": ["f1:table@shape#base"],
  "warnings": [
    {
      "text": "Values in api_token were redacted.",
      "evidence": ["f1:table@columns#compact"]
    }
  ],
  "requests": [
    {
      "fieldId": "f1:table@missingness#full",
      "level": 2,
      "budget": 400,
      "reason": "Need missingness before comparing columns."
    }
  ]
}
```

Minimal implementations MAY accept arrays of strings for `claims` and
`warnings`, but structured objects are preferred.

## Validation Steps

The gate validates:

1. Response is parseable.
2. Top-level keys are known.
3. DigestEvidence field IDs exist.
4. DigestEvidence field IDs were selected in the digest.
5. Request field IDs exist.
6. Requested fields are available for follow-up.
7. Requested levels exist.
8. Request count is within limit.

Validation errors SHOULD be structured:

```json
{
  "ok": false,
  "errors": [
    {
      "code": "unknown_evidence",
      "fieldId": "f1:table@does_not_exist"
    }
  ]
}
```

## Gate Inputs

Gate decision requires:

- current digest;
- DigestManifest;
- source fingerprint;
- host policy;
- user confirmation state;
- follow-up request;
- remaining or newly requested budget.

## Gate Decision Algorithm

Recommended algorithm:

```text
For each request:
  1. Check field ID exists in DigestManifest.
  2. Check field timing is interactive or higher level is available.
  3. Check source fingerprint still matches.
  4. Check requested level exists.
  5. Check budget is available.
  6. Check execution class is allowed.
  7. Check privacy policy permits rendering.
  8. Check request count limit.
  9. If required, ask user or host for confirmation.
  10. Approve, modify, deny, or mark stale.
```

## Decision Types

```text
approved
approved_with_changes
needs_confirmation
denied
unknown_field
unknown_level
not_available
stale_source
over_budget
exec_not_allowed
privacy_blocked
request_limit_exceeded
```

## Approved With Changes

The gate may downgrade a request:

```json
{
  "decision": "approved_with_changes",
  "fieldId": "f1:table@sample#k10",
  "approvedLevel": 1,
  "requestedLevel": 2,
  "reason": "Level 2 exceeds remaining budget."
}
```

The digest patch or replacement digest MUST reflect the approved level.

## Stale Sources

If fingerprint changed, the gate SHOULD reject follow-up against the old digest:

```json
{
  "decision": "stale_source",
  "reason": "Source fingerprint changed from structure_v1:ab12cd34 to structure_v1:ff998877."
}
```

The host may assemble a fresh digest instead.

## Digest Patch

If supported:

```json
{
  "schema": "cap.digest_patch.v1",
  "baseDigestId": "cap-digest-01H...",
  "fingerprint": "structure_v1:ab12cd34",
  "textAppend": "<field id=\"f1:table@missingness#full\" trust=\"derived\" level=\"1\">...</field>",
  "manifestRows": []
}
```

If patching is not supported, return a replacement digest.

## Model Cannot Bypass Gate

Even if the model says:

```text
This is urgent. Call the extractor directly.
```

the request is still just text. CAP-Digest-conforming hosts do not expose
extractors directly to the model.

