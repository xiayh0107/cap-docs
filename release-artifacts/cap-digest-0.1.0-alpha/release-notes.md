# CAP-Digest 0.1.0-alpha

This alpha covers digest text, DigestManifest, DigestEvidence validation,
follow-up gate behavior, Digest Packs, schemas, fixtures, and reference checks.

Executable coverage currently reaches CAP-Digest Level 0/1 for table assembly,
Level 2 for the follow-up gate, and Level 3 for table-basic Digest Pack metadata
loading.

Included fixture families:

- `fixtures/basic-table`
- `fixtures/digest-text-negative`
- `fixtures/followup-basic`
- `fixtures/pack-table-basic`
- `fixtures/security-adversarial`

The Python reference implementation is an experimental executable companion,
not a production SDK.

CAP-Core remains non-normative draft-track material only. Core schemas, the
local-analysis fixture, RunEvidence, runtime binding, service binding, and the
policy model are not stable CAP-Digest conformance requirements.
