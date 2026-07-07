# CAP-Core v1.0 Fixture Suite

> Status: stable v1.0 - Normative fixture index - Last updated: 2026-07-07

The v1.0 fixture suite freezes positive and negative conformance evidence.

## Positive Fixtures

| Fixture | Purpose | Levels |
|---|---|---|
| `fixtures/core/local-analysis/` | Local scientific analysis object graph with artifacts, capability, policy, run, evidence, and digest bridge. | L0-L3 |
| `fixtures/core/build-test/` | Software build/test object graph proving Core is not scientific-domain specific. | L0-L3 |
| `fixtures/core/remote-service-binding/` | Non-local service dependency with opaque secret reference and remote limitations. | L0-L3 |

Each positive fixture includes `source-artifacts.json`, `capability.json`,
`assembly.json`, `policy-decision.json`, `run.json`, `run-evidence.json`,
`digest-view-ref.json`, expected validation, and expected review summary.

## Negative Suite

`fixtures/core/negative/` is the stable negative suite. It maps each invalid
case to stable error codes in `expected-validation.json` and covers object
identity, reference closure, binding roles, policy records, run lifecycle,
evidence layer separation, sensitive-reference handling, and overclaim
boundaries.

## Fixture Compatibility

Fixture corrections in v1.0.x may fix mistakes only when the correction is
documented in `MAINTENANCE-v1.0.md`. Adding new fixture families after v1.0.0
requires a CAPP or a v1.1 planning issue.
