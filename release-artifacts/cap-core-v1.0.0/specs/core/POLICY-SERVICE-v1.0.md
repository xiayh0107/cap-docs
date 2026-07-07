# CAP-Core v1.0 PolicyDecision and Service Boundary

> Status: stable v1.0 - Normative - Last updated: 2026-07-07

## PolicyDecision

PolicyDecision records include policy binding, policy system/ref, principal,
action, resource, decision, decision time, conditions, and obligations. Stable
decision outcomes are `allowed`, `denied`, `allowed_with_constraints`,
`needs_confirmation`, and `stale_context`.

At L2 and above, missing required PolicyDecision evidence MUST be reported as
`missing_policy_decision`. Allowed decisions MUST include explicit obligations
or equivalent profile-owned constraints.

## Service Boundary

Service bindings remain external dependencies. They MUST NOT carry secret
values. They SHOULD carry freshness and limitation information. Service network
access must be represented by policy/resource context; otherwise validators
report `undeclared_network_access`.

Core does not define service API semantics, credential exchange, identity
provider semantics, or live service-call behavior.

## Claim Text

```text
Implementation <name> claims CAP-Core v1.0 L2 policy-aware validation and reports missing policy, stale service, undeclared network, and inline secret findings using stable v1.0 codes.
```
