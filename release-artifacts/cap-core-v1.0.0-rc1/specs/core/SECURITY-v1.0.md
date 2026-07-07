# CAP-Core v1.0 Security Requirements

> Status: stable v1.0 - Normative - Last updated: 2026-07-07

CAP-Core v1.0 security requirements are structural and review-oriented.

## Requirements

- Implementations MUST reject secret-looking inline values in Core records.
- Implementations MUST treat absent required PolicyDecision evidence as not
  allowed at L2 and above.
- Implementations MUST report stale service bindings.
- Implementations MUST report undeclared network access for service bindings
  when policy/resource context does not declare it.
- Implementations MUST keep RunEvidence and DigestEvidence distinct.
- Implementations MUST report RunEvidence overclaims that Core verified
  semantic correctness.
- Implementations SHOULD report remote unverifiable surfaces as warnings.

## Evidence Map

| Requirement | Fixture/code |
|---|---|
| secret rejection | `secret-value-service-binding.json`, `secret_value_in_core_record` |
| fail-closed policy | `missing-policy-decision.json`, `missing_policy_decision` |
| stale service | `stale-service-binding.json`, `stale_service_binding` |
| undeclared network | `undeclared-network-access.json`, `undeclared_network_access` |
| evidence separation | `digest-evidence-as-run-evidence.json`, `digest_evidence_used_as_run_evidence` |
| overclaim boundary | `run-evidence-overclaims-correctness.json`, `run_evidence_overclaims_correctness` |

## External Responsibilities

Core does not provide a sandbox, policy engine, identity system, credential
exchange, signature verifier, SBOM verifier, provenance graph verifier, or
remote service correctness checker.
