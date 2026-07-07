# local-analysis

> Status: CAP-Core v1.0 positive fixture

This fixture exercises a local scientific analysis object graph. It is one
positive fixture family for CAP-Core v1.0 validation and report generation.

It covers:

- dataset, script, config, environment, summary, plot, and log artifacts;
- a `run-analysis` capability;
- runtime, resource, policy, evidence, digest, data-plane, and transport
  bindings;
- a policy decision with network disabled and explicit obligations;
- a completed Run and partial RunEvidence record;
- a CAP-Digest bridge through `DigestBinding`;
- negative cases for DigestEvidence/RunEvidence confusion, missing Assembly
  reference, and inline secret-looking values.

Scientific interpretation, reproducibility scoring, workflow semantics, and
policy language semantics are profile-owned or external.
