# CAP-Core Local-Analysis Fixture Value Review

> Status: decision note - Non-normative - Issue: #25 - Date: 2026-07-06

## Decision

Does `fixtures/core/local-analysis/` prove CAP-Core's draft value?

**Partially yes.** It is strong enough to remain the first CAP-Core draft
example because it connects artifacts, capability, binding roles, policy
decision, run record, RunEvidence, and CAP-Digest bridge in one inspectable
object graph. It is not strong enough to justify normative promotion.

## Review answers

| Question | Assessment |
|---|---|
| Connects artifact, capability, runtime, resource, policy, run, and evidence concerns clearly? | Yes. The fixture links dataset, script, config, environment, output artifacts, capability, binding records, policy decision, Run, RunEvidence, and DigestBinding. |
| Avoids defining workflow semantics? | Yes. It records a local analysis contract and run outcome without introducing workflow steps, dependencies, retries, or scheduling semantics. |
| Avoids defining runtime/container semantics? | Yes. Runtime is represented by a binding handle and constraints; execution behavior remains external. |
| Avoids defining a policy language? | Yes. The fixture records an `allowed_with_constraints` decision and policy reference without defining policy evaluation rules. |
| Avoids defining a provenance ontology? | Mostly yes. RunEvidence is an envelope with provenance references, not a replacement for W3C PROV or Workflow Run RO-Crate. |
| Shows a useful CAP-Digest bridge without confusing evidence layers? | Yes. `DigestBinding` references a CAP-Digest view and the negative fixture rejects DigestEvidence as RunEvidence. |
| What conformance level does it test? | Draft Core reader plus partial Assembly Producer, Run Recorder, and Binding Ecosystem behavior. It is not stable conformance. |
| What would an external implementer need to reproduce it? | The Core schema sketches, local-analysis JSON files, reference validator expectations, and a host-local file/runtime policy model. |

## Value shown

The fixture demonstrates value beyond simply combining existing standards in
three places:

- It creates one reviewable Assembly boundary across artifacts, capability,
  runtime/resource/policy/evidence/digest bindings, and unresolved state.
- It preserves separation between control-plane records and external execution,
  policy, provenance, and data-plane systems.
- It gives CAP-Digest a clear bridge point without making digest evidence stand
  in for run evidence.

## Gaps before normative promotion

| Gap | Required follow-up |
|---|---|
| Only one fixture family exists. | Add a second Core fixture in a different domain or execution setting before normative promotion (#27). |
| `policy-decision.json` has no schema sketch. | Decide whether policy decision is a Core object, a Binding constraint shape, or a profile-owned record (#28). |
| `source-artifacts.json` uses an artifact-set wrapper with no schema. | Either define a wrapper schema or keep artifact sets as fixture harness packaging (#28). |
| External reproducibility instructions are implicit. | Add implementer reproduction notes that distinguish host assumptions from Core records. |
| RunEvidence remains minimal. | Add profile guidance for mapping to PROV or Workflow Run RO-Crate without requiring either as Core. |

## Should it remain the first CAP-Core example?

Yes. Keep `local-analysis` as the first CAP-Core draft fixture, with the
explicit caveat that it is a proof-of-value fixture rather than normative
conformance.
