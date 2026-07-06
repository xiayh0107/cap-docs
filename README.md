# CAP — Context Assembly Protocol

> Status: draft · Version: 2026-07-05-draft · Scope: CAP-Digest profile plus non-normative CAP-Core proposal

CAP is a family of specifications for turning complex source objects and
machine-operable task records into safe, bounded, traceable context and assembly
artifacts for AI agents. The repository is organized as a working draft of one
profile plus a non-normative upper-layer proposal.

```text
cap-docs/
├── README.md                 # this entry point
├── specs/
│   ├── digest/               # CAP-Digest — current draft profile
│   └── core/                 # CAP-Core — non-normative RFC-0001 proposal
├── schemas/                  # CAP-Digest schemas and CAP-Core schema sketches
├── fixtures/                 # CAP-Digest and CAP-Core draft fixtures
├── packs/                    # Digest Packs
├── reference/                # experimental reference implementation
├── capps/                    # CAP proposal process
├── notes/                    # non-normative design memos and knowledge notes
└── .github/                  # contribution templates and CI
```

## What is in scope right now

**CAP-Digest** (`specs/digest/`) is the only drafted normative-track
specification. It defines a
*context evidence layer*: how a source object is safely turned into a
model-readable **context digest** (text + DigestManifest) with stable field
anchors, budgeted selection, redaction, and gated follow-up.

```text
source object -> field catalog -> context digest -> model response -> gated follow-up
```

The central artifact is a **context digest**: a model-readable text object plus a
machine-readable DigestManifest that records exactly what was included, omitted,
redacted, downgraded, or made available for follow-up.

**CAP-Core** (`specs/core/`) now has a **non-normative draft proposal** plus
Core-scoped schema sketches, a local-analysis fixture, and a validator/renderer
prototype. It is intended as an upper layer covering artifact graphs,
capability/runtime binding, RunEvidence, policy records, and external standard
bindings. It does not define stable conformance; see `specs/core/README.md`.

## Start reading

- For the current spec, start at [CAP-Digest Overview](specs/digest/00-overview.md),
  then follow the reading order it lists (01 → 12).
- For the CAP-Core draft proposal, start at
  [CAP-Core README](specs/core/README.md), then read
  [RFC-0001](specs/core/RFC-0001.md).
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

The repository now includes early executable assets:

- `schemas/` — draft JSON schemas for CAP-Digest and CAP-Core objects.
- `fixtures/basic-table/` — the first CAP-Digest conformance fixture.
- `fixtures/followup-basic/` — the first CAP-Digest follow-up/gate fixture.
- `fixtures/pack-table-basic/` — the first Digest Pack loading fixture.
- `fixtures/core/local-analysis/` — the first CAP-Core draft fixture.
- `packs/table-basic/` — the first experimental Digest Pack.
- `reference/python/` — minimal CAP-Digest and CAP-Core reference helpers and
  fixture checker.

These assets are intentionally narrow. The first CAP-Digest target covers Level
0/1 table assembly, Level 2 follow-up gating, and Level 3 `table-basic` pack
metadata loading. The first CAP-Core target is a local scientific analysis
assembly fixture with draft validator/renderer coverage.

## Contribution and governance

- Use [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.
- Use [SECURITY.md](SECURITY.md) for security-sensitive reports.
- Use `capps/` for substantial CAP-Digest, CAP-Core, pack, or governance changes.
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
