# remote-service-binding

> Status: CAP-Core v1.0 positive fixture

This CAP-Core fixture exercises a non-local service dependency without
embedding credentials or defining service API semantics.

It covers:

- request, service contract, client environment, response metadata, and log
  artifacts;
- a `call-remote-service` capability;
- runtime, resource, service, policy, evidence, digest, transport, and
  data-plane bindings;
- a policy decision that permits network access only to an allowlisted service;
- a completed Run with partial RunEvidence because the remote service is not
  semantically verified by Core;
- negative cases for embedded secrets, missing policy decision, undeclared
  network access, stale service binding, and remote evidence overclaiming.

It intentionally does not call a real service, define an HTTP API, evaluate an
external policy language, or prove correctness of the remote response.
