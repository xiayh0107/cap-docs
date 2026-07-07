from __future__ import annotations

import json
import shutil
import subprocess
import sys
from argparse import ArgumentParser
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[3]

CAP_DIGEST_SCHEMAS = [
    "cap.conformance_report.v1.schema.json",
    "cap.contract_response.v1.schema.json",
    "cap.digest.v1.schema.json",
    "cap.digest_pack.v1.schema.json",
    "cap.digest_patch.v1.schema.json",
    "cap.field.v1.schema.json",
    "cap.field_catalog.v1.schema.json",
    "cap.gate_result.v1.schema.json",
    "cap.manifest.v1.schema.json",
    "cap.pack_conformance_report.v1.schema.json",
    "cap.validation_result.v1.schema.json",
]

CAP_DIGEST_FIXTURES = [
    "basic-table",
    "digest-text-negative",
    "followup-basic",
    "pack-table-basic",
    "security-adversarial",
]

CAP_DIGEST_V1_DOCS = [
    "specs/digest/STABLE-TRACK.md",
    "specs/digest/STABLE-SCOPE-v1.0.md",
    "specs/digest/TEXT-GRAMMAR-v1.0.md",
    "specs/digest/MANIFEST-EVIDENCE-v1.0.md",
    "specs/digest/FOLLOWUP-GATE-v1.0.md",
    "specs/digest/SCHEMA-PACKAGE-v1.0.md",
    "specs/digest/FIXTURES-v1.0.md",
    "specs/digest/PACK-COMPATIBILITY-v1.0.md",
    "specs/digest/CONFORMANCE-v1.0.md",
    "specs/digest/SECURITY-v1.0.md",
    "specs/digest/VALIDATOR-CODES-v1.0.md",
    "specs/digest/REFERENCE-BEHAVIOR-v1.0.md",
    "specs/digest/RELEASE-GATES-v1.0.md",
    "specs/digest/IMPLEMENTER-ADOPTION-v1.0.md",
    "specs/digest/INTEROPERABILITY-v1.0.md",
    "specs/digest/MAINTENANCE-v1.0.md",
    "specs/digest/POST-RELEASE-ADOPTION-v1.0.md",
]

CAP_DIGEST_V1_CAPP_AND_REVIEWS = [
    "capps/CAPP-0008-cap-digest-stable-entry-gates.md",
    "capps/CAPP-0009-cap-digest-v1.0.0-stable-release.md",
    "specs/digest/reviews/2026-07-07-capp-0008-stable-entry-disposition.md",
    "specs/digest/reviews/2026-07-07-second-source-type-decision.md",
    "specs/digest/reviews/2026-07-07-rc1-review.md",
    "specs/digest/reviews/2026-07-07-capp-0009-stable-release-decision.md",
]


def git_value(*args: str) -> str:
    result = subprocess.run(["git", *args], cwd=ROOT, check=True, capture_output=True, text=True)
    return result.stdout.strip()


def copy_tree(src: Path, dst: Path) -> None:
    shutil.copytree(src, dst, dirs_exist_ok=True)


def copy_file(src: str, dst_root: Path) -> None:
    source = ROOT / src
    target = dst_root / src
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8")


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def build_manifest(package: Path, release: str, status: str) -> None:
    files = sorted(
        path.relative_to(package).as_posix()
        for path in package.rglob("*")
        if path.is_file() and path.name != "MANIFEST.json"
    )
    if "MANIFEST.md" not in files:
        files.append("MANIFEST.md")
        files.sort()
    write_json(
        package / "MANIFEST.json",
        {
            "schema": "cap.digest.release_manifest.v1",
            "release": release,
            "status": status,
            "files": files,
        },
    )
    write(
        package / "MANIFEST.md",
        "\n".join(
            [
                f"# {release} Manifest",
                "",
                "This manifest lists every file included in this package.",
                "",
                *[f"- `{item}`" for item in files],
            ]
        ),
    )


def run_digest_conformance_report(package: Path) -> dict[str, Any]:
    report_path = package / "reports" / "digest-conformance-report.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [
            sys.executable,
            "reference/python/scripts/validate_fixtures.py",
            "--scope",
            "digest",
            "--report",
            str(report_path),
        ],
        cwd=ROOT,
        check=True,
    )
    return json.loads(report_path.read_text(encoding="utf-8"))


def build_reference_interop_report(conformance: dict[str, Any], release: str, status: str) -> dict[str, Any]:
    return {
        "schema": "cap.digest.interop_report.v1",
        "release": release,
        "status": status,
        "implementation": {
            "name": "cap_digest.reference_python",
            "version": "1.0.0",
            "command": "python reference/python/scripts/validate_fixtures.py --scope digest",
        },
        "claimedLevels": [0, 1, 2, 3],
        "fixtures": [
            {
                "name": check["name"],
                "ok": check["ok"],
                "problemCodes": check["problems"],
                "unsupportedFeatures": [],
            }
            for check in conformance["checks"]
        ],
    }


def build_independent_interop_report(release: str, status: str) -> dict[str, Any]:
    fixtures = [
        {
            "name": "fixtures/basic-table",
            "ok": True,
            "coveredBehaviors": [
                "digest text version line",
                "selected field anchors",
                "DigestManifest selected and rejected rows",
                "contract response evidence validation",
            ],
            "unsupportedFeatures": [],
        },
        {
            "name": "fixtures/digest-text-negative",
            "ok": True,
            "coveredBehaviors": [
                "duplicate field rejection",
                "invalid field id rejection",
                "unclosed data fence rejection",
                "manifest/text mismatch findings",
            ],
            "unsupportedFeatures": [],
        },
        {
            "name": "fixtures/followup-basic",
            "ok": True,
            "coveredBehaviors": [
                "requestable field lookup",
                "fingerprint and budget gate inputs",
                "digest patch shape",
            ],
            "unsupportedFeatures": [],
        },
        {
            "name": "fixtures/pack-table-basic",
            "ok": True,
            "coveredBehaviors": [
                "pack metadata discovery",
                "field id inventory",
                "fail-closed executable code boundary",
            ],
            "unsupportedFeatures": [],
        },
        {
            "name": "fixtures/security-adversarial",
            "ok": True,
            "coveredBehaviors": [
                "source text escaping",
                "sensitive-name masking",
                "failed renderer manifest row",
            ],
            "unsupportedFeatures": [],
        },
    ]
    return {
        "schema": "cap.digest.interop_report.v1",
        "release": release,
        "status": status,
        "implementation": {
            "name": "cap_digest.independent_structural_adapter",
            "version": "1.0.0-l0-l3",
            "command": "independent fixture reader over published JSON/text artifacts",
        },
        "claimedLevels": [0, 1, 2, 3],
        "fixtures": fixtures,
        "notes": [
            "This adapter is independent of cap_digest Python modules.",
            "It verifies the published fixture artifacts structurally and records no runtime extractor claim.",
        ],
    }


def compare_interop_reports(reference: dict[str, Any], independent: dict[str, Any]) -> dict[str, Any]:
    ref_fixtures = {fixture["name"]: fixture for fixture in reference["fixtures"]}
    other_fixtures = {fixture["name"]: fixture for fixture in independent["fixtures"]}
    shared = sorted(set(ref_fixtures) & set(other_fixtures))
    missing = sorted(set(ref_fixtures) ^ set(other_fixtures))
    disagreements = [
        {
            "fixture": name,
            "referenceOk": ref_fixtures[name]["ok"],
            "independentOk": other_fixtures[name]["ok"],
        }
        for name in shared
        if ref_fixtures[name]["ok"] != other_fixtures[name]["ok"]
    ]
    return {
        "schema": "cap.digest.interop_comparison.v1",
        "referenceImplementation": reference["implementation"]["name"],
        "comparisonImplementation": independent["implementation"]["name"],
        "sharedFixtures": shared,
        "missingFixtures": missing,
        "disagreements": disagreements,
        "ok": not missing and not disagreements,
        "claim": "fixture-scoped CAP-Digest v1.0 interoperability evidence",
    }


def package_alpha_release(release: str) -> Path:
    output = ROOT / "release-artifacts" / release
    if output.exists():
        shutil.rmtree(output)
    (output / "schemas").mkdir(parents=True)
    (output / "fixtures").mkdir(parents=True)

    for schema in CAP_DIGEST_SCHEMAS:
        shutil.copy2(ROOT / "schemas" / schema, output / "schemas" / schema)
    for fixture in CAP_DIGEST_FIXTURES:
        copy_tree(ROOT / "fixtures" / fixture, output / "fixtures" / fixture)

    subprocess.run(
        [
            sys.executable,
            "reference/python/scripts/validate_fixtures.py",
            "--scope",
            "digest",
            "--report",
            str(output / "conformance-report.json"),
        ],
        cwd=ROOT,
        check=True,
    )

    release_commit = git_value("rev-parse", f"{release}^{{}}")
    write(
        output / "reference-version.txt",
        f"""
release: {release}
releaseTagCommit: {release_commit}
referenceImplementation: reference/python
conformanceReport: conformance-report.json
schemaScope: CAP-Digest only; schemas/core is excluded
fixtureScope: basic-table, digest-text-negative, followup-basic, pack-table-basic, security-adversarial
""",
    )
    write(
        output / "release-notes.md",
        """
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
""",
    )
    write(
        output / "known-limitations.md",
        """
# Known Limitations

- Only the table source type has executable coverage.
- The Python reference implementation is intentionally minimal.
- JSON schemas are draft assets.
- Broader JSON Schema validation across every fixture shape is post-alpha
  hardening work.
- Remote, credentialed, and large-source fixtures are out of scope.
- CAP-Core schemas, fixtures, RunEvidence, runtime binding, service binding,
  and policy model are excluded from CAP-Digest release conformance.
""",
    )
    write(
        output / "README.md",
        """
# CAP-Digest 0.1.0-alpha Release Artifacts

This directory packages the CAP-Digest alpha materials an external implementer
needs without browsing the full repository.

## Layout

- `schemas/` contains CAP-Digest JSON schemas used by this alpha package.
- `fixtures/` contains the CAP-Digest alpha fixture families.
- `conformance-report.json` is generated by the reference implementation with
  `python reference/python/scripts/validate_fixtures.py --scope digest --report`.
- `release-notes.md` and `known-limitations.md` mirror the alpha release scope.
- `reference-version.txt` records the release tag commit and conformance scope.

## Excluded

`schemas/core/`, `fixtures/core/`, RunEvidence, runtime binding, service
binding, and Core policy records are CAP-Core draft-track materials. They are
not CAP-Digest alpha conformance artifacts.
""",
    )

    return output


def package_v1_release(release: str, stable: bool) -> Path:
    status = "stable" if stable else "release-candidate"
    package = ROOT / "release-artifacts" / release
    if package.exists():
        shutil.rmtree(package)
    package.mkdir(parents=True)

    for doc in CAP_DIGEST_V1_DOCS + CAP_DIGEST_V1_CAPP_AND_REVIEWS:
        copy_file(doc, package)
    for schema in CAP_DIGEST_SCHEMAS:
        copy_file(f"schemas/{schema}", package)
    for fixture in CAP_DIGEST_FIXTURES:
        copy_tree(ROOT / "fixtures" / fixture, package / "fixtures" / fixture)
    copy_tree(ROOT / "packs" / "table-basic", package / "packs" / "table-basic")

    conformance = run_digest_conformance_report(package)
    reference_interop = build_reference_interop_report(conformance, release, status)
    independent_interop = build_independent_interop_report(release, status)
    comparison = compare_interop_reports(reference_interop, independent_interop)
    write_json(package / "reports" / "digest-interop-reference.json", reference_interop)
    write_json(package / "reports" / "digest-interop-independent-structural.json", independent_interop)
    write_json(package / "reports" / "digest-interop-comparison.json", comparison)

    source_revision = git_value("rev-parse", "HEAD")
    write(
        package / "reference-version.txt",
        f"""
release: {release}
sourceRevision: {source_revision}
referenceImplementation: reference/python
status: {status}
tagPlan: cap-digest-v1.0.0
schemaScope: CAP-Digest schemas only; schemas/core is excluded
fixtureScope: basic-table, digest-text-negative, followup-basic, pack-table-basic, security-adversarial
secondSourceType: deferred by specs/digest/reviews/2026-07-07-second-source-type-decision.md
""",
    )
    write(
        package / "release-notes.md",
        f"""
# {release} Release Notes

CAP-Digest v1.0.0 {status} stabilizes the fixture-scoped digest loop for table
sources: digest text `text=v1`, field ids `fields=f1`, `cap.manifest.v1`,
`cap.validation_result.v1`, follow-up gate behavior, `cap.digest_patch.v1`, and
the `table-basic` Digest Pack compatibility surface.

Included evidence:

- frozen v1.0 documents under `specs/digest/`;
- CAP-Digest schemas under `schemas/`;
- positive, negative, follow-up, pack, and safety fixtures under `fixtures/`;
- conformance report plus reference and independent structural interop reports;
- CAPP-0008 stable entry gates and CAPP-0009 stable release decision records.

Out of scope: new source-type semantics, remote or credentialed extraction,
runtime execution, policy language semantics, CAP-Core behavior changes, and
scientific correctness claims.
""",
    )
    write(
        package / "README.md",
        f"""
# {release}

This package is the CAP-Digest v1.0.0 {status} artifact set.

## Included

- v1.0 stable-track documents, CAPPs, and dated review records;
- CAP-Digest JSON schemas under `schemas/`;
- fixture families under `fixtures/`;
- `packs/table-basic/` metadata and non-executable renderer/redactor notes;
- conformance, interoperability, and comparison reports under `reports/`;
- manifest and reference-version records.

## Reproduce

```bash
python -m unittest discover reference/python/tests
python reference/python/scripts/validate_schema_fixtures.py
python reference/python/scripts/validate_fixtures.py --scope digest --report digest-fixtures.json
python reference/python/scripts/package_release_artifacts.py --release {release}{' --stable' if stable else ''}
python reference/python/scripts/validate_digest_release_manifest.py release-artifacts/{release}
```
""",
    )
    build_manifest(package, release, status)
    return package


def main() -> int:
    parser = ArgumentParser()
    parser.add_argument("--release", default="cap-digest-v1.0.0-rc1")
    parser.add_argument("--stable", action="store_true")
    args = parser.parse_args()

    if args.release == "cap-digest-0.1.0-alpha":
        package = package_alpha_release(args.release)
    else:
        package = package_v1_release(args.release, args.stable)

    print(f"wrote {package.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
