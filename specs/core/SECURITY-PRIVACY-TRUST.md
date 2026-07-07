# CAP-Core Security, Privacy, and Trust

> Status: candidate-prep draft - Non-normative - Last updated: 2026-07-07

This threat model records the security invariants CAP-Core must satisfy before
candidate normative review. It complements the CAP-Digest security model; it
does not replace it.

## Threat Boundaries

CAP-Core describes machine-operable assemblies and evidence. It does not execute
workflows, evaluate policy languages, manage secrets, sandbox runtimes, or prove
that a remote service result is semantically correct.

## Invariants

| Invariant | Enforcement path |
|---|---|
| Capability is not authorization. | CAPP-0005, conformance L2, negative fixture `capability-implies-authorization`. |
| Binding is not trust. | Binding profile docs and security review; bindings identify dependencies only. |
| Absence of PolicyDecision is not allow. | Validator code `missing_policy_decision`; remote fixture negative case. |
| Unknown execution or binding class fails closed. | Validator code `invalid_binding_type`; schema enum coverage. |
| Secret references are opaque. | Validator code `secret_value_in_core_record`; service-binding negative cases. |
| Service bindings must not embed credentials. | Remote fixture service binding uses `secretRef` only. |
| Model-visible text cannot grant source or execution access. | CAP-Digest bridge profile keeps digest views separate from execution evidence. |
| RunEvidence cannot overclaim correctness. | Validator code `run_evidence_overclaims_correctness`; negative fixture suite. |
| Remote/service bindings disclose unverifiable surfaces. | Remote fixture records `remoteLimitations`; validator emits a warning. |
| Redaction, degrade, and truncation must be explicit. | Profiles record degraded or partial evidence in RunEvidence records. |
| Generated artifacts link to RunEvidence. | Conformance L3 checks run outputs and evidence references. |

## Highest-Risk Cases

The candidate-prep negative suite covers embedded secrets, missing policy
decisions, undeclared network access, stale service bindings, DigestEvidence
used as RunEvidence, and RunEvidence overclaiming semantic correctness.

## Deferrals

Sandboxing, policy-engine evaluation, secret-manager APIs, cryptographic
attestation verification, and remote service semantic validation remain external
system responsibilities unless a future CAPP narrows a minimal Core requirement.
