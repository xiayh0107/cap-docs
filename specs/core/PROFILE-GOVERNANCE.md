# CAP-Core Profile Governance

> Status: candidate-prep draft - Non-normative - Last updated: 2026-07-07

Profiles and bindings add domain-specific constraints while preserving the
minimal Core object model.

## Lifecycle

| State | Meaning |
|---|---|
| proposed | Idea or sketch with no fixture commitment. |
| draft | Documented scope, non-goals, and examples. |
| candidate | Schema refs, fixtures, security notes, and validator behavior are ready for review. |
| accepted | Governance accepts the profile for active use. |
| deprecated | Kept for compatibility; new work should avoid it. |

Current classification:

- Scientific Computation Profile: draft profile proposal.
- CAP-Digest Bridge Profile: candidate-prep draft profile.

## Authoring Checklist

A profile draft should include:

- scope and non-goals;
- object constraints and extension fields;
- schema refs and namespace rules;
- positive and negative fixture coverage;
- validator behavior and stable codes;
- security and privacy considerations;
- compatibility and versioning rules;
- CAPP link when governance impact exists.

## Extension Namespaces

Profile-owned fields should use profile IDs, `profileType`, `profiles`, or
profile-named metadata. Unknown profile fields should be preserved by Core
readers unless a profile-specific validator is active.

## Requirement Precedence

Profiles may be stricter than minimal Core for their own records. They should
not loosen Core safety checks such as secret-value rejection, fail-closed policy
interpretation, or RunEvidence/DigestEvidence separation.

Repeated profile patterns can be proposed for Core inclusion through CAPP only
after at least two fixture families need the same semantics without profile
interpretation.
