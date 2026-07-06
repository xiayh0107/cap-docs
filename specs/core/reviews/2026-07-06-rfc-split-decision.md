# CAP-Core RFC-0001 Split Decision

> Status: decision note - Non-normative - Issue: #26 - Date: 2026-07-06

## Decision

Split the integrated CAP-Core RFC-0001 draft into **Core + Bindings + Profiles**.

The current integrated draft is valuable as an orientation document, but it is
too broad for focused review. Splitting reduces ambiguity between the minimal
Core object model, external-standard binding policy, and profile-specific
semantics.

## Split RFC files

| File | Scope | Normative candidate? |
|---|---|---|
| `specs/core/RFC-0001-core-object-model.md` | Artifact, ArtifactRef, Profile reference mechanism, Capability minimum, Assembly, Run, RunEvidence envelope, lifecycle checkpoints. | Candidate only after future CAPP. |
| `specs/core/RFC-0002-binding-model.md` | Generic Binding envelope, binding roles, integrity/freshness/status fields, external-standard binding rules. | Candidate only after future CAPP. |
| `specs/core/RFC-0003-scientific-computation-profile.md` | Local/scientific analysis profile semantics, artifact roles, resource constraints, reproducibility notes, fixture mapping. | Profile draft, non-Core. |
| `specs/core/RFC-0004-cap-digest-bridge-profile.md` | DigestBinding, Digest view references, RunEvidence-to-Digest view rules, separation from DigestEvidence. | Profile draft, coordinated with CAP-Digest CAPP if behavior changes. |

Keep `specs/core/RFC-0001.md` as an integrated overview while the split drafts
are reviewed. Do not promote any split RFC to normative status in the split
work.

Implementation is tracked in #29 and recorded by the split draft files above.

## Review answers

| Question | Answer |
|---|---|
| Is RFC-0001 too broad to review well? | Yes. It mixes object model, binding policy, scientific profile, and CAP-Digest bridge rules. |
| Are bindings complex enough for their own RFC? | Yes. Binding roles carry external-standard reuse policy, integrity/freshness, status values, and boundary rules. |
| Should scientific computation be a profile? | Yes. It is a profile over Core objects and bindings, not part of minimal Core. |
| Should the CAP-Digest bridge be separate? | Yes. It crosses CAP-Core and CAP-Digest and must preserve layer boundaries. |
| Does splitting reduce ambiguity? | Yes. The governance overhead is justified because it prevents Core from absorbing profile or external-standard semantics. |
| Which documents remain notes? | Boundary, ontology, lifecycle, security, conformance, primitive reuse, and example documents remain non-normative support notes until cited by a future CAPP. |

## Non-goals

This decision does not promote CAP-Core conformance, add new Core concepts, or
change CAP-Digest behavior.
