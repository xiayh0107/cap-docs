# Example Assembly 0001: Local Scientific Analysis

> Status: planning · Non-normative · Last updated: 2026-07-05

This example tests whether the proposed CAP-Core ontology can describe a small
machine-operable scientific analysis without defining a new workflow engine,
runtime, policy language, or provenance standard.

## Scenario

A user asks an agent to validate a small analysis result. The host has:

- a dataset;
- an analysis script;
- a configuration file;
- an environment reference;
- a local runtime capable of executing the script;
- a policy that disables network access and limits resources.

The goal is to assemble a contract that can be reviewed, run, evidenced, and
summarized through CAP-Digest.

## Artifact candidates

| Artifact | Kind | Example reference | Notes |
|---|---|---|---|
| Dataset | data | `file://workspace/data/orders.csv` | Profile may define table/dataframe semantics. |
| Script | code | `file://workspace/scripts/analyze.py` | Could bind to CodeMeta or repository metadata later. |
| Config | config | `file://workspace/config/analysis.json` | Inputs and parameters. |
| Environment | environment reference | `oci://example/analysis:sha256-...` | OCI is an external binding, not a CAP runtime format. |
| Output directory | result location | `file://workspace/out/` | Created or updated by the Run. |

## Capability candidate

```text
Capability: run-analysis
Inputs:
  dataset
  script
  config
Outputs:
  result files
  logs
  RunEvidence
Side effects:
  writes output directory
Required bindings:
  runtime
  resource
  policy
```

Open question: whether this Capability should be declared by CAP-Core, a profile,
or an external host catalog.

## Binding candidates

| Binding | Example | Proposed location |
|---|---|---|
| RuntimeBinding | local process or OCI container reference | Core binding handle, external runtime semantics |
| ResourceBinding | CPU=2, memory=4GiB, timeout=10m, network=disabled | Core |
| ServiceBinding | none | Core supports absence explicitly |
| PolicyBinding | user/session authorization, network disabled | Core decision record, external policy language |
| EvidenceBinding | logs, outputs, provenance, optional attestation | Core envelope, external evidence formats |
| DigestBinding | CAP-Digest view of RunEvidence | Core-to-Digest bridge |

## Candidate Assembly

```text
Assembly local-analysis-001
  artifacts:
    dataset: file://workspace/data/orders.csv
    script: file://workspace/scripts/analyze.py
    config: file://workspace/config/analysis.json
    environment: oci://example/analysis:sha256-...
  capability: run-analysis
  profiles:
    table-analysis
  bindings:
    runtime: local-process or OCI reference
    resource: cpu=2, memory=4GiB, timeout=10m, network=disabled
    policy: user-approved, no-network
  unresolved:
    provenance profile choice
```

The Assembly is pre-run. It should be inspectable before execution.

## Candidate Run

```text
Run run-001
  assembly: local-analysis-001
  state: completed
  startedAt: timestamp
  endedAt: timestamp
  outputs:
    file://workspace/out/summary.json
    file://workspace/out/plot.png
  logs:
    file://workspace/out/run.log
```

## Candidate RunEvidence

```text
RunEvidence evidence-001
  run: run-001
  inputs:
    dataset, script, config, environment reference
  products:
    summary.json, plot.png, run.log
  records:
    runtime status
    resource use
    exit code
    timestamps
  externalEvidence:
    optional W3C PROV or Workflow Run RO-Crate
    optional in-toto/Sigstore attestation
    optional SPDX/CycloneDX dependency inventory
  digestViews:
    CAP-Digest view of summary and caveats
```

## CAP-Digest bridge

CAP-Digest may render:

```text
source object: RunEvidence evidence-001
field catalog:
  run status
  input artifact list
  output artifact list
  caveats
  logs available on request
context digest:
  model-visible evidence view
```

This does not make DigestEvidence equivalent to RunEvidence. DigestEvidence
proves what the model saw; RunEvidence records what the run produced.

## What this example validates

This example checks whether CAP-Core can describe:

- artifact references;
- capability intent;
- runtime/resource/policy bindings;
- a run instance;
- evidence records;
- an optional CAP-Digest view.

## What this example avoids

This example intentionally avoids:

- defining a workflow language;
- defining container execution semantics;
- defining a policy language;
- defining a provenance ontology;
- defining an agent transport protocol;
- claiming reproducibility from a digest alone.

## Open decisions revealed by the example

1. Should `Capability` be a Core object or external catalog object?
2. Should `RuntimeBinding`, `ResourceBinding`, and `PolicyBinding` be separate
   objects or subtypes of `Binding`?
3. Should `RunEvidence` require W3C PROV compatibility or only allow a PROV
   profile?
4. Should a CAP-Core Assembly be immutable once a Run starts?
5. Should CAP-Core require content digests for all artifacts, or allow scoped
   references when integrity is unavailable?
