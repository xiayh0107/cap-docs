# CAP-Core Inspection Report

> Status: candidate-prep draft - Non-normative - Last updated: 2026-07-07

The reference renderer emits a review-oriented inspection report for Core
fixtures. It helps reviewers inspect object graph links, bindings, policy,
run/evidence records, limitations, and validator diagnostics.

## Formats

Machine-readable report:

```text
schemas/core/cap.core.inspection_report.v1.schema.json
```

Human-readable text:

```bash
python reference/python/scripts/render_core_inspection_report.py \
  --fixture remote-service-binding \
  --json-report core-inspection.json \
  --text-report core-inspection.txt
```

The text format begins with `CAP-Core inspection report` and sections for
object graph, bindings, policy, run and evidence, and diagnostics.

## Included Information

The renderer includes:

- ArtifactSet, Artifact, Capability, Binding, Assembly, PolicyDecision, Run,
  RunEvidence, and DigestBinding identifiers;
- binding type, status, target, secret references, and limitations;
- policy decision, conditions, obligations, and fail-closed marker;
- run state, inputs, outputs, logs, evidence refs, digest views, completeness,
  integrity, and limitations;
- validation warnings and errors from the same fixture validation pass.

## Safety Boundaries

The renderer does not execute assemblies, fetch artifacts, retrieve secrets,
evaluate policy, or generate CAP-Digest text. It keeps RunEvidence and
DigestEvidence distinct and redacts secret-looking targets.
