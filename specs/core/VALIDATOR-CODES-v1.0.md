# CAP-Core v1.0 Validator Codes

> Status: stable v1.0 - Normative code registry - Last updated: 2026-07-07

Implementations SHOULD use these stable finding codes when reporting equivalent
conditions.

## Stable Error Codes

| Code | Meaning |
|---|---|
| `artifact_integrity_state_missing` | External ArtifactRef lacks verified/unverified/unavailable integrity state. |
| `assembly_action_without_capability` | Assembly attempts hidden executable action outside Capability. |
| `capability_implies_authorization` | Capability record implies authorization. |
| `digest_binding_collapses_evidence_layers` | DigestBinding fails to keep DigestEvidence separate from RunEvidence. |
| `digest_binding_evidence_mismatch` | DigestBinding points at the wrong RunEvidence. |
| `digest_binding_not_in_assembly` | DigestBinding is not present in Assembly bindings. |
| `digest_evidence_used_as_run_evidence` | CAP-Digest evidence is substituted for RunEvidence. |
| `duplicate_object_id` | Core object ids are duplicated. |
| `external_standard_copied_inline` | External standard schema is copied inline into Core. |
| `invalid_binding_status` | Binding status token is unsupported. |
| `invalid_binding_type` | Binding type token is unsupported. |
| `invalid_digest_binding` | Digest view binding does not use digest type. |
| `invalid_policy_decision` | PolicyDecision decision token is unsupported. |
| `invalid_reference_list` | Reference field is not a list where one is required. |
| `invalid_run_state` | Run state token is unsupported. |
| `missing_policy_decision` | Required PolicyDecision is absent. |
| `missing_required_binding_type` | Capability-required binding role is absent from Assembly. |
| `missing_required_field` | Required field is absent. |
| `policy_binding_mismatch` | PolicyDecision targets a different policy binding than the Assembly. |
| `policy_decision_missing_obligations` | Allowed decision omits explicit obligations. |
| `run_assembly_mismatch` | Run does not reference the Assembly. |
| `run_completed_without_output` | Completed Run lacks output/log evidence. |
| `run_evidence_mismatch` | RunEvidence does not reference the Run. |
| `run_evidence_overclaims_correctness` | RunEvidence claims Core verified semantic correctness. |
| `run_without_assembly_reference` | Run lacks Assembly reference. |
| `runtime_binding_missing_image_reference` | OCI runtime binding is not content-addressed. |
| `secret_value_in_core_record` | Core record carries secret-looking value. |
| `stale_service_binding` | Service binding is stale. |
| `undeclared_network_access` | Remote service network access lacks policy/resource declaration. |
| `unanchored_reproducible_artifact` | Reproducible artifact claim lacks integrity anchor. |
| `unknown_reference` | Reference does not resolve in the package. |
| `unknown_schema` | Schema name is not a supported Core schema. |
| `unresolved_artifact_reference` | Assembly references an unknown artifact. |

## Stable Warning Codes

| Code | Meaning |
|---|---|
| `artifact_integrity_state_implicit` | External artifact integrity state is not explicit. |
| `remote_unverifiable_surface` | Remote service surface is recorded but not semantically verified by Core. |
