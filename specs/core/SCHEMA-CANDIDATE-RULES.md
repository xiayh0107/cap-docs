# CAP-Core Schema Candidate Rules

> Status: candidate-prep draft - Non-normative - Last updated: 2026-07-07

This document records the candidate review rules for the eight minimal Core
object families. The schemas remain draft-track sketches.

## ArtifactSet, Artifact, ArtifactRef

`ArtifactSet` carries `schema`, `id`, and `artifacts`. Each `Artifact` carries
`schema`, `id`, `kind`, and `ref`. `ArtifactRef` is embedded at `artifact.ref`
with `uri`, `scope`, optional `kind`, optional integrity material, and
`integrityState` for external refs: `verified`, `unverified`, or `unavailable`.

Candidate checks:

- object IDs are unique within a package;
- Assembly, Run, and RunEvidence artifact refs close over the ArtifactSet;
- external refs declare integrity state even when no digest is available;
- reproducibility claims need an integrity anchor or external evidence.

Stable error codes include `duplicate_object_id`,
`unresolved_artifact_reference`, `artifact_integrity_state_missing`, and
`unanchored_reproducible_artifact`.

## Capability

`Capability` declares operation shape: inputs, outputs, side effects, required
binding roles, profiles, implementation binding hints, and error semantics. It
does not authorize execution. Authorization is represented by `PolicyDecision`.

Stable error code: `capability_implies_authorization`.

## Binding

`Binding` carries `schema`, `id`, `type`, `target`, and `status`, with optional
standard/profile/freshness/integrity/evidence fields. Candidate role names are
`runtime`, `resource`, `service`, `policy`, `evidence`, `digest`, `transport`,
`data-plane`, and `schema`.

Status values are `candidate`, `resolved`, `denied`, `stale`, `unavailable`,
and `deferred`. Secret values are disallowed; opaque secret references are
allowed. External standards are referenced, not copied inline.

Stable error codes include `invalid_binding_type`, `invalid_binding_status`,
`secret_value_in_core_record`, `stale_service_binding`,
`runtime_binding_missing_image_reference`, and
`external_standard_copied_inline`.

## Assembly

`Assembly` is the root pre-run review object. It connects artifact IDs, one
Capability ID, binding IDs, embedded binding records, policy binding, profiles,
state, and unresolved items. It does not execute anything.

Candidate checks close artifact, capability, binding, and policy-binding refs.
Stable error codes include `unknown_reference`, `invalid_reference_list`,
`missing_required_binding_type`, and `assembly_action_without_capability`.

## PolicyDecision

`PolicyDecision` records principal, action, resource, decision, conditions,
obligations, policy binding, policy reference, and decision time. Decision
tokens are `allowed`, `denied`, `allowed_with_constraints`,
`needs_confirmation`, and `stale_context`.

Absence of a PolicyDecision is never interpreted as allow. Policy language and
identity semantics remain external.

Stable error codes include `missing_policy_decision`,
`policy_binding_mismatch`, `invalid_policy_decision`, and
`policy_decision_missing_obligations`.

## Run

`Run` is one execution or observation instance linked to an Assembly. Candidate
fields include run id, assembly id, state, timestamps, inputs, outputs,
runtime/resource/service binding refs, logs, and evidence refs.

State vocabulary is `planned`, `starting`, `running`, `waiting`, `completed`,
`failed`, `cancelled`, and `stale`. This is not a workflow engine state
machine.

Stable error codes include `invalid_run_state`, `run_assembly_mismatch`,
`run_without_assembly_reference`, and `run_completed_without_output`.

## RunEvidence

`RunEvidence` records observations around a Run: materials, products, logs,
records, attestations, provenance refs, SBOM refs, telemetry refs, digest views,
completeness, integrity, and limitations. It can record gaps and unverifiable
surfaces. It does not prove semantic correctness or scientific validity.

Evidence categories are observation, attestation, log, hash, policy decision,
and derived claim. DigestEvidence remains CAP-Digest evidence; it is not
RunEvidence.

Stable error codes include `run_evidence_mismatch`,
`digest_evidence_used_as_run_evidence`,
`digest_binding_evidence_mismatch`,
`digest_binding_collapses_evidence_layers`, and
`run_evidence_overclaims_correctness`.
