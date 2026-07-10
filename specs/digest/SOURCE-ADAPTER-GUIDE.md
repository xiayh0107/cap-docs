# CAP-Digest Source Adapter Guide

> Status: non-normative implementer guidance · Applies to: CAP-Digest v1.0.x and later implementation work · Last updated: 2026-07-10

This guide explains how a host-language implementation can support open-ended,
language-specific object types without turning the CAP-Digest core into an
ever-growing list of object-specific digest methods.

It does not change the CAP-Digest v1.0 stable surface. CAP-Digest v1.0.0 remains
fixture-scoped and table-source-scoped. The normative sources remain the stable
scope, schemas, grammar, fixture index, security requirements, validator code
registry, and conformance documents.

The central design rule is:

> A CAP-Digest runtime should depend on a stable source-adapter contract, not on
> a closed list of host-language classes.

Read this guide together with:

- [CAP-Digest Stable Scope v1.0](STABLE-SCOPE-v1.0.md);
- [Core Data Model](03-core-data-model.md);
- [Field Model and Assembly](05-field-model-and-assembly.md);
- [Implementation Guide](12-implementation-guide.md);
- [Implementer and Adoption Guide v1.0](IMPLEMENTER-ADOPTION-v1.0.md).

## Why This Guide Exists

CAP-Digest defines this logical flow:

```text
source object
    -> source identification
    -> field catalog
    -> budget allocation
    -> guarded extraction
    -> redaction
    -> rendering
    -> digest text + DigestManifest
    -> evidence validation
    -> gated follow-up
```

That flow deliberately does not define how every R, Python, JVM, JavaScript, or
domain-specific object is inspected. A language implementation must supply that
host integration.

Without an explicit adapter design, an implementation often grows like this:

```text
digest(data.frame)
digest(lm)
digest(Seurat)
digest(ggplot)
digest(CustomResult)
...
```

Moving those branches into object-specific methods improves organization, but it
does not by itself create an open protocol. The core still expands one class at a
time, and class dispatch becomes entangled with field semantics, extraction,
rendering, security, and conformance claims.

A source adapter separates those concerns.

## Status and Normative Boundary

This document is implementation guidance.

Capitalized requirement language in the normative CAP-Digest documents and
schemas takes precedence over this guide. In particular:

- `cap.field.v1` and `cap.field_catalog.v1` remain serialized metadata contracts;
- executable extractor, redactor, and renderer functions remain
  implementation-local;
- duplicate field IDs must not be resolved by silent last-writer-wins behavior;
- extraction and rendering are guarded operations;
- redaction precedes rendering;
- models request fields, while a non-model gate authorizes follow-up;
- CAP-Digest v1.0 conformance remains limited to its published fixture scope.

An implementation may use this guide without claiming that its adapter API is
part of the CAP specification.

## Terminology

| Term | Meaning |
|---|---|
| Host object | A language-level value such as an R object, Python object, JVM object, document handle, or database proxy. |
| Host class | The concrete class or type used by the host language. |
| Source family | A broad semantic category used by CAP fields and source metadata, such as `table`, `model`, `document`, `graph`, or `experiment`. |
| Source adapter | Host-local code that maps one or more host object classes to `SourceRef`, a `FieldCatalog`, fingerprint behavior, and runtime contract bindings. |
| Runtime binding | A host-local function bound to a symbolic extractor, redactor, or renderer reference. |
| Adapter registry | A host-controlled mechanism for discovering and selecting adapters without modifying the core package. |
| Structural fallback | A conservative adapter that reports shallow structure but makes no domain-semantic claim. |
| Adapter contract test | An implementation-specific test suite for adapter behavior. It is not automatically a CAP conformance test. |
| CAP conformance claim | A claim tied to a published CAP version, level, fixture suite, and supported stable scope. |

## Reference Architecture

```text
                         host policy
                              |
                              v
host object -> adapter resolution -> resolved adapter
                                     |
                   +-----------------+------------------+
                   |                 |                  |
                   v                 v                  v
               SourceRef        FieldCatalog      runtime bindings
                   |                 |                  |
                   +-----------------+------------------+
                                     |
                                     v
                              planner / allocator
                                     |
                                     v
                         guarded field materialization
                           extract -> redact -> render
                                     |
                                     v
                         digest text + DigestManifest
                                     |
                         +-----------+-----------+
                         |                       |
                         v                       v
                evidence validation        follow-up gate
                                                 |
                                                 v
                                      patch or replacement digest
```

The adapter is resolved once for a digest lifecycle and its provenance is
recorded with the digest. Any later operation that touches the source, especially
follow-up extraction and patch materialization, should use the same adapter
identity and compatible runtime bindings.

The core runtime does not need to know the internal representation of every
object. It needs a resolved adapter that can answer:

1. What source is this?
2. What broad source family does it belong to?
3. Which fields are available?
4. How are the fields extracted?
5. What are their execution, trust, timing, and cost properties?
6. How are values redacted and rendered deterministically?
7. How is source identity or freshness fingerprinted?
8. Which fields may be requested through follow-up?
9. What adapter implementation and version produced the result?

## Minimal Adapter Contract

The exact API is language-specific. A useful conceptual contract is:

```text
Adapter
  identity() -> AdapterIdentity
  matches(source, context) -> MatchResult
  source_ref(source, context) -> SourceRef
  field_catalog(source, context) -> FieldCatalog
  fingerprint(source, context) -> FingerprintResult
  bind(kind, symbolic_contract, context) -> RuntimeFunction
  capabilities(context) -> AdapterCapabilities
```

Suggested adapter identity metadata:

```json
{
  "id": "org.example.analysis-result",
  "version": "1.2.0",
  "provider": "example-package",
  "providerVersion": "4.3.1",
  "maturity": "community",
  "semanticLevel": "domain"
}
```

These fields are implementation metadata, not new required properties of
`cap.field.v1` or `cap.field_catalog.v1`.

An implementation may record adapter provenance in a permitted
implementation-specific part of source identity or manifest metadata, or in a
sidecar record. It should not add undeclared properties to schemas whose
`additionalProperties` policy forbids them.

### Runtime Operation Shapes

A runtime binding should expose structured outcomes rather than returning only a
value or throwing an unrecorded exception.

```text
extract(source, field, level, policy, context)
  -> value
  -> warnings
  -> elapsed time
  -> implementation diagnostics

redact(value, field, policy, context)
  -> safe value
  -> redacted flag
  -> warnings
  -> applied rule identifiers

render(value, field, level, policy, context)
  -> field block
  -> actual cost
  -> warnings
  -> truncation information
```

The assembler translates these outcomes into digest text, caveats, and
`DigestManifest` rows.

## Serialized Catalogs and Executable Bindings

A serialized field definition may contain symbolic contract references:

```yaml
schema: cap.field.v1
id: f1:analysis_result@org_example_overview#base
label: Analysis overview
description: A bounded overview exposed by the source adapter.
sourceTypes:
  - analysis_result
timing: assemble
trust: derived
exec: local_cheap
levels:
  - level: 1
    estimatedCost: 100
    description: Bounded overview.
contracts:
  extractor: org.example.analysis_result.overview
  redactor: cap.default
  renderer: org.example.analysis_result.overview.text_v1
```

The serialized catalog does not contain closures, source code, shell commands,
network locations, or an instruction that a model can execute.

The resolved adapter binds the symbolic names to reviewed host-local functions:

```text
extractor:
  org.example.analysis_result.overview -> local extractor function

redactor:
  cap.default -> host redaction function

renderer:
  org.example.analysis_result.overview.text_v1 -> deterministic renderer
```

This separation provides four useful properties:

- field catalogs remain serializable and inspectable;
- runtime code remains under host control;
- missing or conflicting bindings can fail closed;
- Digest Pack metadata does not become executable merely by being discovered.

## Host Class and Source Family Are Different

A host class is an implementation detail. A source family is a semantic
classification used to organize fields and source behavior.

Many classes may map to one source family:

```text
R data.frame  --------\
R tbl_df      ---------\
R data.table  ----------> table
pandas.DataFrame -------/
polars.DataFrame -------/
```

Conversely, one host class may expose multiple semantic views. In that case the
caller should select a view or adapter explicitly rather than relying on hidden,
order-dependent dispatch.

Do not create a new source family merely because a new class name appears.
Create or select a source family based on field semantics, extraction behavior,
and evidence meaning.

Supporting an additional class through an existing family does not, by itself,
change the CAP protocol. Defining a new stable source family, stable field
semantics, or a broader conformance claim requires separate specification,
fixture, and governance work.

## Adapter Ownership and Packaging

Adapters may be provided by:

```text
core implementation
  built-in adapters for the implementation's supported stable scope

extension package
  domain or ecosystem adapters maintained separately

object-owning package
  adapter supplied alongside the class definition

application
  local adapter for a private or prototype class
```

The core implementation should not require a release whenever a third-party
class gains support.

A package that owns a domain object is usually best placed to define its
semantics. An independent extension package is appropriate when the object-owning
package does not want a direct dependency on a CAP implementation.

## Deterministic Adapter Resolution

A registry is useful only if resolution is deterministic and inspectable.

Recommended precedence:

```text
1. explicit adapter supplied by the caller
2. host-language adapter hook for the most specific class or type
3. registered adapter match
4. generic structural fallback, when enabled
5. adapter-not-found error
```

Recommended conflict rules:

1. Match classes or types using a documented host-language precedence.
2. Use an explicit numeric priority only as a secondary rule.
3. If two different adapters have the same effective match and priority, return
   an ambiguity error.
4. Treat identical repeated registration as idempotent only when adapter ID,
   version, provider, and binding set agree.
5. Never use silent last-registration-wins behavior.
6. Report the selected adapter and the candidates that lost resolution.
7. Keep registry scope host-controlled; loading arbitrary metadata must not
   automatically authorize executable adapter code.

Adapter resolution failures are implementation diagnostics. Implementations
should not reuse a CAP stable validator or gate finding code with a different
meaning. An implementation-specific code such as
`x_capr_adapter_ambiguous` is preferable to overloading a CAP code.

## Pin Adapter Provenance Across Follow-Up

A digest may outlive the process state that created it. Packages can be upgraded,
unloaded, or registered in a different order before a follow-up request arrives.

The implementation should therefore record enough adapter provenance to detect
semantic drift:

```json
{
  "adapter": {
    "id": "org.example.analysis-result",
    "version": "1.2.0",
    "provider": "example-package",
    "providerVersion": "4.3.1",
    "maturity": "community",
    "semanticLevel": "domain"
  }
}
```

For a follow-up operation:

- use the pinned adapter when it is still available and compatible;
- verify the source fingerprint;
- verify that symbolic contracts resolve to compatible bindings;
- fail closed when the adapter is unavailable or incompatible;
- do not silently substitute a different fallback adapter.

Adapter compatibility is implementation-defined, but the decision should be
visible in diagnostics.

## Field IDs and Third-Party Namespaces

CAP-Digest field IDs use the `f1` form:

```text
f1:<source-family>@<field-name>#<variant>
```

Third-party adapters should avoid globally generic field names such as:

```text
summary
results
metadata
details
```

A provider-qualified segment can be encoded inside the field name while
remaining within the current grammar:

```text
f1:model@org_example_coefficients#base
f1:model@org_example_diagnostics#summary
f1:experiment@bioconductor_seurat_assays#base
f1:analysis_result@mypackage_overview#base
```

The source-family segment remains semantic. The provider namespace belongs in
the field-name segment, not in a new dotted source-family syntax.

Within an adapter ecosystem:

- define who owns a provider namespace;
- keep field meanings stable;
- create a new variant when representation changes materially;
- document compatibility when renaming or replacing a field;
- fail closed on duplicate field IDs unless the host requires an explicit,
  recorded override.

A community field ID can be valid under the grammar without becoming part of the
CAP-Digest v1.0 stable fixture surface.

## Generic Structural Fallback

A structural fallback is useful for exploration, but it is not a substitute for
a semantic adapter.

A conservative fallback may expose bounded fields such as:

```text
f1:generic_object@examplehost_identity#base
f1:generic_object@examplehost_dimensions#base
f1:generic_object@examplehost_names#shallow
f1:generic_object@examplehost_structure#shallow
```

The exact source family and field names are implementation-specific and are not
part of the CAP-Digest v1.0 stable field set.

Recommended fallback metadata:

```text
adapter = <implementation>.generic_structural
maturity = fallback
semanticLevel = structural
conformanceClaim = none
```

The fallback should:

- report only shallow, bounded structure by default;
- avoid invoking user-defined display, summary, conversion, or traversal methods
  unless guarded and explicitly allowed;
- treat remote proxies, external pointers, lazy values, connections, and
  environment-like objects conservatively;
- classify potentially expensive inspection as `local_scan`, `remote_query`, or
  `unsafe` rather than assuming it is cheap;
- record failures instead of silently omitting fields;
- make no scientific, statistical, or domain-semantic claim;
- be disabled or changed to fail-closed mode during conformance testing.

Even apparently simple reflection can execute user code or trigger I/O in some
host languages. The fallback should use only operations the host can justify as
safe, or run them under the same guards used for normal extraction.

## Guarded Execution and Security

Adapter extensibility must not bypass CAP-Digest safety behavior.

For every adapter:

- source access is treated as potentially executable;
- execution class controls isolation, timeout, budget, and authorization;
- remote and credentialed access is denied unless explicit host policy allows it;
- redaction runs before rendering;
- data-trust strings are escaped;
- extraction, redaction, and rendering failures are recorded;
- failed fields are not rendered as normal values;
- model-visible text cannot directly invoke adapter functions;
- follow-up requests pass through the gate;
- source fingerprint and adapter compatibility are checked before follow-up;
- registry discovery does not automatically authorize third-party code.

Hosts should consider process isolation for high-risk adapters and should
document when deterministic output is impossible.

## Conformance and Compatibility Claims

Four different claims should not be collapsed into a single statement that an
object is “supported.”

| Layer | What it establishes |
|---|---|
| Artifact validity | Produced JSON and text satisfy the applicable schema and grammar checks. |
| Digest consistency | Text, manifest rows, evidence anchors, rejection state, and gate behavior are internally consistent. |
| Adapter compatibility | The adapter passes the host implementation's adapter-contract tests. |
| CAP conformance | The implementation passes a published CAP fixture suite for a stated CAP version and conformance level. |

Examples:

```text
Built-in table adapter
  CAP-Digest v1.0 L0-L3 claim may be made only when the corresponding published
  fixtures and release requirements pass.

Community model adapter
  May produce valid CAP artifacts and pass the host adapter-contract suite.
  It does not inherit the table fixture conformance claim.

Generic structural fallback
  Structural summary only.
  No CAP-Digest v1.0 source-family conformance claim.
```

A recommended public claim record is:

```text
Implementation:
Implementation version:
CAP version:
Claimed level:
Fixture suite and revision:
Stable source families covered:
Community adapters:
Fallback behavior:
Unsupported features:
Security and isolation notes:
Implementation provenance:
Conformance report location:
```

## Adapter Contract Test Suite

A host implementation should maintain an adapter-contract test suite separate
from CAP fixture conformance.

Recommended checks:

1. Adapter resolution is deterministic.
2. Ambiguous matches fail closed.
3. Adapter identity and version are present.
4. `SourceRef.sourceType` agrees with catalog applicability.
5. Field IDs satisfy the selected field ID grammar.
6. Field IDs are unique after catalog composition.
7. Serialized field definitions contain symbolic contracts, not executable code.
8. Every selected symbolic contract resolves to exactly one approved binding.
9. Missing bindings produce explicit failed-field results.
10. Extraction warnings and elapsed time are captured.
11. Redaction occurs before rendering.
12. Renderer output is bounded and deterministic for fixed inputs.
13. Fallback adapters carry structural-only metadata.
14. Adapter provenance is preserved across follow-up.
15. Incompatible adapter versions fail closed during patch materialization.
16. Registry loading does not execute unapproved pack metadata.
17. Adapter-specific errors do not redefine stable CAP finding codes.
18. A community adapter cannot be included implicitly in a stable table claim.

Passing these tests means the adapter follows the host's extension contract. It
does not replace the CAP-Digest fixture suite.

## Implementation Workflow

When adding support for a host object:

1. Decide whether it maps to an existing source family.
2. Define the adapter owner, ID, version, maturity, and semantic level.
3. Define `SourceRef` and fingerprint behavior.
4. Define a cheap, deterministic field catalog.
5. Choose valid, provider-qualified field IDs.
6. Declare timing, trust, execution class, levels, estimated cost, and prior
   value.
7. Put symbolic contract names in serialized field definitions.
8. Bind those names to host-local extractor, redactor, and renderer functions.
9. Guard extraction and capture warnings, errors, elapsed time, and timeouts.
10. Redact before rendering and escape data-trust strings.
11. Record selected, rejected, and failed candidates in the manifest.
12. Test deterministic resolution, catalog composition, and failure behavior.
13. Test evidence validation and follow-up with pinned adapter provenance.
14. State clearly whether the adapter is stable, community, experimental, or
    fallback.
15. Publish a CAP conformance claim only for the fixture scope actually passed.

When introducing a genuinely new source family, also provide source-family
semantics, positive and negative fixtures, security analysis, compatibility
analysis, and the appropriate CAP governance record before presenting it as a
stable CAP surface.

## Illustrative R Design

This section is illustrative. The function names are not CAP requirements.

A thin R implementation can keep `cap_digest()` as a stable orchestration
function and resolve one adapter:

```r
cap_digest <- function(x, ..., adapter = NULL) {
  adapter <- cap_resolve_adapter(x, adapter = adapter)

  source <- adapter$source_ref(x, ...)
  catalog <- adapter$field_catalog(x, ...)

  cap_assemble(
    source_object = x,
    source_ref = source,
    field_catalog = catalog,
    adapter = adapter,
    ...
  )
}
```

An optional S3 bridge can return an adapter instead of implementing the entire
digest pipeline per class:

```r
cap_adapter <- function(x, ...) {
  UseMethod("cap_adapter")
}

cap_adapter.default <- function(x, ...) {
  NULL
}

cap_adapter.analysis_result <- function(x, ...) {
  analysis_result_adapter()
}
```

The adapter owns serialized metadata and runtime bindings:

```r
analysis_result_adapter <- function() {
  cap_new_adapter(
    id = "org.example.analysis_result",
    version = "1.0.0",
    maturity = "community",
    semantic_level = "domain",
    source_types = "analysis_result",

    source_ref = function(x, context) {
      cap_source_ref_value(
        uri = context$uri,
        source_type = "analysis_result",
        label = context$label,
        identity = list(class = class(x))
      )
    },

    field_catalog = function(x, context) {
      cap_field_catalog_value(
        catalog_id = "org.example.analysis_result",
        source_type = "analysis_result",
        fields = list(
          cap_field_value(
            id = "f1:analysis_result@org_example_overview#base",
            label = "Analysis overview",
            description = "A bounded overview of the analysis result.",
            source_types = "analysis_result",
            timing = "assemble",
            trust = "derived",
            exec = "local_cheap",
            levels = list(list(
              level = 1L,
              estimatedCost = 100L,
              description = "Bounded overview."
            )),
            contracts = list(
              extractor = "org.example.analysis_result.overview",
              redactor = "cap.default",
              renderer = "org.example.analysis_result.overview.text_v1"
            )
          )
        )
      )
    },

    bindings = list(
      extractor = list(
        "org.example.analysis_result.overview" =
          function(x, field, level, policy, context) {
            list(
              value = x$overview,
              warnings = character(),
              elapsed_ms = 0L
            )
          }
      ),
      redactor = list(
        "cap.default" = cap_default_redactor
      ),
      renderer = list(
        "org.example.analysis_result.overview.text_v1" =
          render_analysis_overview
      )
    )
  )
}
```

A package may register the adapter during loading:

```r
.onLoad <- function(libname, pkgname) {
  capR::cap_register_adapter(
    class = "analysis_result",
    adapter_factory = analysis_result_adapter,
    priority = 0L
  )
}
```

The registry should still apply deterministic ambiguity rules. An explicit
`adapter =` argument should remain available for objects with multiple valid
semantic views.

This design avoids requiring:

```r
cap_digest.analysis_result()
cap_source_ref.analysis_result()
cap_field_catalog.analysis_result()
cap_extract_field.analysis_result()
cap_render_field.analysis_result()
```

for every class while preserving separately testable source, catalog, extraction,
redaction, rendering, and assembly responsibilities.

## Mapping to Other Host Ecosystems

The same contract can be implemented through different host mechanisms:

| Ecosystem | Possible adapter discovery mechanism |
|---|---|
| R | One S3 adapter hook plus a host-local registry |
| Python | `Protocol` or abstract base class plus package entry points |
| JVM | Service Provider Interface or dependency-injected registry |
| JavaScript/TypeScript | Explicit adapter objects plus package or application registry |
| Rust | Trait objects plus explicit registration or feature-gated adapters |
| Private application | Direct adapter injection without global registration |

The discovery mechanism is local. The produced CAP artifacts and conformance
claims are the interoperability surface.

## Review Checklist for Language Demos

A language demo or implementation plan should answer all of the following:

- Is the core pipeline class-independent after adapter resolution?
- Are host classes separated from source-family semantics?
- Can an external package add an adapter without modifying the core?
- Is registry resolution deterministic and fail-closed on ambiguity?
- Are adapter identity and version recorded?
- Are field catalogs serializable and executable functions local?
- Do third-party field IDs remain valid and collision-resistant?
- Is generic fallback structural-only and explicitly labeled?
- Are extraction, redaction, rendering, and follow-up guarded?
- Is the adapter pinned across follow-up?
- Are adapter compatibility tests separated from CAP conformance tests?
- Does the public claim name the exact CAP version, level, fixtures, and source
  scope?

A demo that cannot answer these questions may still be useful, but it should be
described as an experiment rather than a complete CAP-Digest implementation
architecture.

## Common Anti-Patterns

### One Digest Method Per Object Class

```text
digest.class_a
digest.class_b
digest.class_c
```

This is acceptable as a temporary façade, but not as the extension architecture
when each method reimplements orchestration.

### Class Name Equals Source Type

A class name identifies host representation. A source type or source family
identifies semantics. Treating them as the same creates unstable field catalogs.

### Executable Functions in Serialized Fields

Closures and source code do not belong in `cap.field.v1` metadata. Use symbolic
contracts and host-local bindings.

### Silent Registry Override

Last-writer-wins makes output depend on load order and prevents reproducible
follow-up.

### Semantic Claims From Reflection

A shallow structure dump cannot determine scientific importance, statistical
meaning, privacy sensitivity, or reasonable follow-up.

### Re-resolving an Adapter During Follow-Up

Selecting a different adapter after a package or registry change can invalidate
field meaning and evidence anchors.

### Community Adapters Inside a Stable Claim

Producing a digest for an object does not place that object in the CAP-Digest
v1.0 stable conformance surface.

### Model-Callable Extractors

A model requests a field ID. The host gate decides whether approved adapter code
runs.

## Maintenance of This Guide

This guide should evolve as independent language implementations report adapter
experience.

Updates that clarify implementation patterns can be made as non-normative
documentation. Changes that alter stable field ID grammar, required serialized
properties, digest text grammar, gate semantics, security requirements, or
conformance scope require the corresponding normative process and versioning
decision.

When an adapter lesson reveals a protocol ambiguity rather than an
implementation choice, open a focused issue and determine whether the change is:

```text
implementation guidance
normative clarification
new fixture coverage
new source-family proposal
schema or grammar change
```

Keeping those categories separate prevents host-language convenience APIs from
silently redefining CAP-Digest.
