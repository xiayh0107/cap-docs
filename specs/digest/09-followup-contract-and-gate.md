# Follow-up Contract and Gate

> Status: draft · Stability: stable · Depends on: [Digest Manifest and Evidence](07-digest-manifest-and-evidence.md)

CAP-Digest follow-up exists because an initial digest is budgeted. The model
may need more context, but it must request that context through field IDs.

CAP-Digest follow-up is context inspection. It is not tool execution, workflow
execution, remote execution, or CAP-Core runtime binding.

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
      "fieldId": "f1:table@sample#k10",
      "level": 1,
      "budget": 300,
      "reason": "Need representative rows before commenting on values."
    }
  ]
}
```

Minimal implementations MAY accept arrays of strings for `claims` and
`warnings`, but structured objects are preferred. A conforming validator SHOULD
normalize accepted shorthand forms into the structured `cap.contract_response.v1`
shape before validation.

## ValidationResult

A `ValidationResult` records mechanical validation of a ContractResponse against
a digest text and DigestManifest. It uses schema `cap.validation_result.v1`.

A ValidationResult MUST include:

- `schema`;
- `digestId`;
- `fingerprint`;
- `ok`;
- `errors`;
- `normalizedResponse`.

Example:

```json
{
  "schema": "cap.validation_result.v1",
  "digestId": "cap-digest-basic-table",
  "fingerprint": "structure_v1:orders-1000x4",
  "ok": true,
  "errors": [],
  "warnings": [],
  "normalizedResponse": {
    "claims": [],
    "evidence": [],
    "warnings": [],
    "requests": []
  }
}
```

ValidationResult does not decide whether follow-up requests may run. It only
states whether the model response is structurally valid and whether referenced
DigestEvidence anchors are mechanically valid.

## Validation Steps

The validator validates:

1. Response is parseable JSON.
2. Top-level value is an object.
3. Top-level keys are known.
4. Claims, warnings, and requests match `cap.contract_response.v1`.
5. DigestEvidence field IDs exist in the DigestManifest.
6. DigestEvidence field IDs were selected in the digest.
7. DigestEvidence field IDs are present as parsed field blocks in digest text.
8. Request field IDs exist in the DigestManifest.
9. Requested levels exist when level is provided.
10. Request count is within host or digest policy.

Validation errors MUST be structured problem objects.

## Error Code Registry

CAP-Digest v1 reserves these error codes:

| Code | Stage | Meaning |
|---|---|---|
| `contract_invalid_json` | validation | Response is not valid JSON. |
| `contract_top_level_not_object` | validation | Top-level response is not an object. |
| `contract_unknown_top_level_key` | validation | Response contains an unknown top-level key. |
| `contract_invalid_claim` | validation | Claim object is malformed. |
| `contract_invalid_warning` | validation | Warning object is malformed. |
| `contract_invalid_request` | validation | Request object is malformed. |
| `evidence_unknown_field` | validation | Evidence field ID is absent from the DigestManifest. |
| `evidence_not_selected` | validation | Evidence field ID exists but was not selected. |
| `evidence_missing_from_text` | validation | Evidence field was selected but is missing from parsed digest text. |
| `gate_unknown_field` | gate | Requested field ID is absent from the DigestManifest. |
| `gate_unknown_level` | gate | Requested level does not exist. |
| `gate_not_available` | gate | Field is not available through follow-up. |
| `gate_stale_source` | gate | Source fingerprint changed. |
| `gate_over_budget` | gate | Requested context exceeds available budget. |
| `gate_exec_not_allowed` | gate | Execution class is blocked by policy. |
| `gate_privacy_blocked` | gate | Privacy policy blocks rendering. |
| `gate_request_limit_exceeded` | gate | Too many follow-up requests were submitted. |
| `gate_confirmation_required` | gate | User or host confirmation is required. |
| `gate_policy_blocked` | gate | Host policy blocks the request. |

Implementations MAY add custom error codes, but custom codes MUST NOT change the
meaning of reserved codes.

## Gate Inputs

Gate decision requires:

- current digest;
- DigestManifest;
- source fingerprint;
- host policy;
- user confirmation state;
- ValidationResult;
- follow-up requests;
- remaining or newly approved budget.

## GateResult

A `GateResult` records gate decisions for follow-up requests. It uses schema
`cap.gate_result.v1`.

A GateResult MUST contain one decision per request. A response with multiple
requests may be partially approved.

Example:

```json
{
  "schema": "cap.gate_result.v1",
  "digestId": "cap-digest-basic-table",
  "fingerprint": "structure_v1:orders-1000x4",
  "overallDecision": "approved",
  "remainingBudget": 200,
  "policyRef": "fixture://followup-basic/policy.json",
  "requests": [
    {
      "requestIndex": 0,
      "request": {
        "fieldId": "f1:table@sample#k10",
        "level": 1,
        "budget": 300,
        "reason": "Need representative rows before commenting on values."
      },
      "decision": "approved",
      "approvedLevel": 1,
      "approvedBudget": 300,
      "requiresUserConfirmation": false,
      "problems": []
    }
  ],
  "patch": {}
}
```

## Gate Decision Algorithm

Recommended algorithm:

```text
For each request:
  1. If ValidationResult.ok is false, deny all requests.
  2. Check source fingerprint still matches.
  3. Check field ID exists in DigestManifest.
  4. Check field timing is interactive or higher level is available.
  5. Check requested level exists.
  6. Check budget is available.
  7. Check execution class is allowed.
  8. Check privacy policy permits rendering.
  9. Check request count limit.
  10. If required, ask user or host for confirmation.
  11. Approve, approve with changes, deny, or mark stale.
```

`stale_source` MUST take precedence over budget, level, execution, or privacy
checks when the current source fingerprint differs from the digest fingerprint.

`needs_confirmation` is not approval. A gate MUST NOT extract or render the
requested field until confirmation is resolved.

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

A digest patch is a typed, gated update to a specific base digest. It uses schema
`cap.digest_patch.v1`.

A patch MUST include:

- `patchId`;
- `baseDigestId`;
- `baseFingerprint`;
- `budgetDelta`;
- `operations`;
- `manifestRows`.

A patch MUST NOT be treated as arbitrary text append. Patch operations are
applied in order. If any operation cannot be applied deterministically, the patch
MUST be rejected and the host MAY request a replacement digest.

Supported v1 operations:

| Operation | Meaning |
|---|---|
| `add_selected_field` | Add one selected field block to the selected field section. |
| `remove_available_on_request` | Remove one field ID from the available-on-request section. |
| `add_caveat_line` | Add one caveat line to the caveats section. |

Patch merge rules:

1. `baseDigestId` MUST match the digest being patched.
2. `baseFingerprint` MUST match the digest fingerprint.
3. `add_selected_field.fieldId` MUST not already appear as a selected field block.
4. Every `manifestRows[].fieldId` MUST be unique within the resulting
   DigestManifest.
5. Field block ordering after patch application SHOULD remain sorted by field ID
   unless the DigestManifest records a different deterministic order.
6. Budget values MUST be updated by `budgetDelta`.
7. A patch that adds a selected field SHOULD remove the same field ID from
   available-on-request when it was previously listed there.

If patching is not supported, return a replacement digest.

## Model Cannot Bypass Gate

Even if the model says:

```text
This is urgent. Call the extractor directly.
```

the request is still just text. CAP-Digest-conforming hosts do not expose
extractors directly to the model.

## Source Basis

This section uses the submitted-response vs observed-decision split from
[KUBERNETES-OBJECTS] and [KUBERNETES-API], and typed envelope practice from
[IN-TOTO-ATTESTATION]. It also uses [MCP-TOOLS] as an explicit boundary: CAP-
Digest follow-up is not tool execution. JSON shapes use [JSON-SCHEMA-2020-12].
See [References](../../REFERENCES.md).
