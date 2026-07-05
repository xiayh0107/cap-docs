# CAP — Context Assembly Protocol

> Status: draft · Version: 2026-07-05-draft · Scope: CAP-Digest profile (CAP-Core reserved)

CAP is a family of specifications for turning complex source objects into safe,
bounded, traceable, machine-operable context for AI agents. The repository is
organized as a working draft of one profile plus a reserved upper layer.

```text
cap-docs/
├── README.md                 # this entry point
├── specs/
│   ├── digest/               # CAP-Digest — current draft profile
│   └── core/                 # CAP-Core — reserved, not yet drafted
├── schemas/                  # CAP-Digest JSON schemas
├── fixtures/                 # conformance fixtures
├── packs/                    # Digest Packs
├── reference/                # experimental reference implementation
├── capps/                    # CAP-Digest proposal process
├── notes/                    # non-normative design memos and knowledge notes
└── .github/                  # contribution templates and CI
```

## What is in scope right now

**CAP-Digest** (`specs/digest/`) is the only drafted specification. It defines a
*context evidence layer*: how a source object is safely turned into a
model-readable **context digest** (text + DigestManifest) with stable field
anchors, budgeted selection, redaction, and gated follow-up.

```text
source object -> field catalog -> context digest -> model response -> gated follow-up
```

The central artifact is a **context digest**: a model-readable text object plus a
machine-readable DigestManifest that records exactly what was included, omitted,
redacted, downgraded, or made available for follow-up.

**CAP-Core** (`specs/core/`) is **reserved**, not started. It is intended as a
future upper layer covering artifact graphs, capability/runtime binding,
RunEvidence, and external standard bindings. It will be drafted only after a
fresh research pass; see `specs/core/README.md`.

## Start reading

- For the current spec, start at [CAP-Digest Overview](specs/digest/00-overview.md),
  then follow the reading order it lists (01 → 12).
- For the current implementation status, read [STATUS.md](STATUS.md).
- For near-term work, read [ROADMAP.md](ROADMAP.md).
- For maintenance policy, read [MAINTENANCE.md](MAINTENANCE.md).
- For positioning questions, read [FAQ.md](FAQ.md).
- For the CAP-Digest / CAP-Core split rationale, read
  [CAP 认知差错与正确认知框架报告](notes/2026-07-05-cognitive-error-and-framework.md).
- For retained ecosystem knowledge notes (to seed a future CAP-Core research
  pass), read
  [Deep Research v2 知识留存笔记](notes/2026-07-05-deep-research-v2-knowledge-notes.md).

## Executable draft assets

The repository now includes early executable assets for CAP-Digest:

- `schemas/` — draft JSON schemas for CAP-Digest objects.
- `fixtures/basic-table/` — the first conformance fixture.
- `packs/table-basic/` — the first experimental Digest Pack.
- `reference/python/` — a minimal Python reference implementation and fixture checker.

These assets are intentionally narrow. The first target is CAP-Digest Level 0/1
for one source type: `table`.

## Contribution and governance

- Use [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.
- Use [SECURITY.md](SECURITY.md) for security-sensitive reports.
- Use `capps/` for substantial CAP-Digest changes.
- Use `CHANGELOG.md` to track notable changes.

## Working rule

When making a change in this repository, ask first:

> Is this refining CAP-Digest, or does it actually belong in CAP-Core?

Keeping these two layers separate avoids conflating a context evidence profile
with a full object-assembly protocol. See the notes directory for the analysis
behind this rule.

## Normative language

The CAP-Digest spec set uses **MUST**, **MUST NOT**, **SHOULD**, and **MAY** as
defined in `specs/digest/00-overview.md`. Documents in `notes/`, `reference/`,
and planned or experimental assets are non-normative unless explicitly stated
otherwise.
