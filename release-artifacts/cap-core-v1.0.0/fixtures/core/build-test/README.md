# build-test

> Status: CAP-Core v1.0 positive fixture

This CAP-Core fixture exercises a software build/test scenario. It is one
positive fixture family for CAP-Core v1.0 validation and interop evidence.

It covers:

- source, config, environment, test report, and log artifacts;
- a `run-build-test` capability;
- runtime, resource, policy, evidence, digest, data-plane, transport, and schema
  bindings;
- a policy decision with network disabled;
- a completed Run and RunEvidence record;
- a CAP-Digest bridge through `DigestBinding`;
- negative cases for invalid run state, invalid policy decision, secret values
  in service bindings, and DigestEvidence/RunEvidence layer confusion.

It intentionally does not define a workflow language, scheduler behavior,
runtime/container semantics, policy language, provenance ontology, or CAP-Digest
field semantics.
