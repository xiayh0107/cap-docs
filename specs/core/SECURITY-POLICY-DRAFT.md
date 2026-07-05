# CAP-Core Security and Policy Draft

> Status: draft - Non-normative - Last updated: 2026-07-05

This document sketches the security and policy model for the first CAP-Core RFC.
It defines records and boundaries, not a policy engine.

## Security goal

CAP-Core should make a machine-operable action reviewable before it runs and
auditable after it runs. The reviewer should be able to answer:

```text
Who or what requested the assembly?
Which artifacts and capabilities were selected?
Which runtime, resources, services, and policies were bound?
What was allowed, denied, constrained, or deferred?
What ran, what changed, and what evidence was produced?
```

## Boundary with CAP-Digest

CAP-Digest protects model-visible context. CAP-Core protects assembly and run
records. The two layers may refer to each other, but their security claims are
different:

| Layer | Security question |
|---|---|
| CAP-Digest | What did the model see, cite, omit, redact, or request as follow-up? |
| CAP-Core | What was assembled, authorized, run, observed, and evidenced? |

DigestEvidence must not be treated as RunEvidence. RunEvidence may include a
DigestBinding that points to a digest view.

## Principal, action, resource

The first draft should use policy records that can bind to external policy
systems using a principal-action-resource shape:

```text
principal:
  subjectRef
  subjectType
  identityBinding
action:
  plan | bind | authorize | run | observe | interrupt | resume | finalize | publish
resource:
  assemblyRef
  artifactRefs
  capabilityRef
  bindingRefs
conditions:
  time
  network
  data locality
  resource budget
  consent
  delegation
  host policy
decision:
  allowed | denied | allowed_with_constraints | needs_confirmation | stale_context
```

External systems such as OPA, Cedar, OAuth/OIDC, SPIFFE/SPIRE, IAM, or local
host policy remain authoritative for policy evaluation.

## PolicyBinding

A `PolicyBinding` should record enough information for audit without embedding
the policy language:

```text
id
policySystem
policyRef
policyVersion
principal
action
resource
decision
decisionTime
conditions
obligations
auditRef
evidenceRefs
```

The first RFC should allow policy engines to return richer records through a
profile. Core should only define the minimal common shape.

## Secrets

CAP-Core must not carry secret values. It may record:

- secret requirement names;
- secret provider references;
- access mode;
- scope requested;
- whether a policy decision allowed or denied use;
- audit/evidence references.

If a secret is materialized during a run, that fact belongs in run evidence or
host audit logs by reference. The secret value must remain outside Core records.

## Network and data locality

Resource and policy bindings should make network and locality constraints
visible before execution:

| Constraint | Examples |
|---|---|
| Network | disabled, internal-only, allow-list, egress-proxy, unrestricted. |
| Data locality | local workspace, trusted research environment, region, cluster, object-store bucket. |
| Write scope | none, output directory, object-store prefix, database table, external service. |
| Time/resource budget | CPU, memory, GPU, wall time, storage, cost. |

The runtime or scheduler enforces these constraints. CAP-Core records what the
Assembly relied on and what the evidence later reports.

## Evidence integrity

RunEvidence should state the integrity level of each referenced record:

| Integrity level | Meaning |
|---|---|
| `unanchored` | Referenced but no digest, signature, or immutable revision is known. |
| `digested` | Content digest or immutable object revision is recorded. |
| `signed` | Signature or attestation reference is recorded. |
| `verified` | Verification result from a trusted verifier is recorded. |
| `external` | Integrity is delegated to an external system by reference. |

These levels are evidence metadata. They do not prove that the result is
scientifically correct.

## Denial and stale records

Denied and stale decisions are first-class records. A failed or denied assembly
can still be useful evidence.

Examples:

- policy denied network access;
- runtime image digest could not be resolved;
- artifact fingerprint changed after discovery;
- user consent expired;
- resource budget exceeded;
- required service binding was unavailable.

RFC-0001 should define how these records appear in an Assembly or Run without
requiring the action to continue.

## Threat model notes

CAP-Core should be designed against these failure modes:

| Failure mode | Draft mitigation |
|---|---|
| Capability confusion | Bind capability identity, inputs, outputs, side effects, and implementation reference separately. |
| Runtime substitution | Prefer immutable runtime refs and record resolver evidence. |
| Policy bypass | Require a policy decision or explicit policy-deferred status before run creation. |
| Secret leakage | Store secret refs only and keep values outside Core. |
| Data exfiltration | Record network/data locality constraints and evidence of observed writes/egress where available. |
| Evidence forgery | Allow signed or verified evidence bindings; record integrity level. |
| Digest/run conflation | Keep DigestEvidence and RunEvidence names and references distinct. |
| Overclaiming reproducibility | Require explicit completeness and integrity statements; allow "unanchored" status. |

## Non-goals

RFC-0001 should not:

- define a new policy language;
- define a new identity protocol;
- define a secret manager;
- define a sandbox, container runtime, or scheduler;
- require one attestation or provenance format for all runs;
- claim that a successful run proves result truth;
- require CAP-Digest for all CAP-Core records.

## First draft conclusion

The security and policy model is ready for RFC-0001 as a record model: Core can
define `PolicyBinding`, policy decision fields, secret-reference rules,
resource/network constraints, denial/stale records, and evidence integrity
metadata. Enforcement and evaluation remain external.
