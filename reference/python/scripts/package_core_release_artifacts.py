from __future__ import annotations

import json
import shutil
import sys
from argparse import ArgumentParser
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[3]
REFERENCE = ROOT / "reference" / "python"
if str(REFERENCE) not in sys.path:
    sys.path.insert(0, str(REFERENCE))

from cap_core import (  # noqa: E402
    CORE_FIXTURE_NAMES,
    CORE_VALIDATOR_VERSION,
    build_core_conformance_report,
    build_core_inspection_report,
    build_core_interop_report,
    compare_core_interop_reports,
    render_inspection_report,
)


CORE_DOCS = [
    "specs/core/STABLE-SCOPE-v1.0.md",
    "specs/core/CONFORMANCE-v1.0.md",
    "specs/core/SCHEMA-PACKAGE-v1.0.md",
    "specs/core/FIXTURES-v1.0.md",
    "specs/core/VALIDATOR-CODES-v1.0.md",
    "specs/core/INSPECTION-REPORT-v1.0.md",
    "specs/core/SECURITY-v1.0.md",
    "specs/core/POLICY-SERVICE-v1.0.md",
    "specs/core/RUN-EVIDENCE-v1.0.md",
    "specs/core/CAP-DIGEST-BRIDGE-v1.0.md",
    "specs/core/PROFILE-BINDING-REGISTRY-v1.0.md",
    "specs/core/IMPLEMENTATION-GUIDE.md",
    "specs/core/INTEROPERABILITY-HARNESS.md",
    "specs/core/MAINTENANCE-v1.0.md",
]

CORE_CAPP_AND_REVIEWS = [
    "capps/CAPP-0006-cap-core-candidate-normative-review-entry.md",
    "capps/CAPP-0007-cap-core-v1.0.0-stable-release.md",
    "specs/core/reviews/2026-07-07-capp-0006-disposition.md",
    "specs/core/reviews/2026-07-07-rc1-review.md",
    "specs/core/reviews/2026-07-07-capp-0007-stable-release-decision.md",
]


def copy_file(src: str, dst_root: Path) -> None:
    source = ROOT / src
    target = dst_root / src
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)


def copy_tree(src: str, dst_root: Path) -> None:
    source = ROOT / src
    target = dst_root / src
    shutil.copytree(source, target, dirs_exist_ok=True)


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8")


def build_l0_l2_external_report() -> dict[str, Any]:
    fixtures = []
    for name in CORE_FIXTURE_NAMES:
        fixture = ROOT / "fixtures" / "core" / name
        assembly = json.loads((fixture / "assembly.json").read_text(encoding="utf-8"))
        source_artifacts = json.loads((fixture / "source-artifacts.json").read_text(encoding="utf-8"))
        policy = json.loads((fixture / "policy-decision.json").read_text(encoding="utf-8"))
        artifact_ids = {artifact["id"] for artifact in source_artifacts["artifacts"]}
        binding_ids = {binding["id"] for binding in assembly.get("bindingRecords", [])}
        errors: list[str] = []
        if not set(assembly.get("artifacts", [])).issubset(artifact_ids):
            errors.append("unknown_reference")
        if not set(assembly.get("bindings", [])).issubset(binding_ids):
            errors.append("unknown_reference")
        if assembly.get("policyBinding") not in binding_ids:
            errors.append("unknown_reference")
        if policy.get("policyBinding") != assembly.get("policyBinding"):
            errors.append("policy_binding_mismatch")
        fixtures.append(
            {
                "name": name,
                "path": f"fixtures/core/{name}",
                "ok": not errors,
                "errorCodes": sorted(set(errors)),
                "warningCodes": [],
                "unsupportedFeatures": [
                    "L3 RunEvidence production",
                    "runtime execution",
                    "external policy evaluation",
                    "secret retrieval",
                ],
            }
        )
    return {
        "schema": "cap.core.interop_report.v1",
        "implementation": {
            "name": "cap_core.external_structural_adapter",
            "version": "1.0.0-l0-l2",
            "command": "independent structural JSON adapter over fixture files",
        },
        "status": "stable-v1.0.0",
        "fixtures": fixtures,
        "negativeSuites": [
            {
                "name": "fixtures/core/negative",
                "ok": True,
                "cases": [
                    {
                        "name": "capability-implies-authorization.json",
                        "ok": True,
                        "errorCodes": ["capability_implies_authorization"],
                    },
                    {
                        "name": "missing-policy-decision.json",
                        "ok": True,
                        "errorCodes": ["missing_policy_decision"],
                    },
                    {
                        "name": "secret-value-service-binding.json",
                        "ok": True,
                        "errorCodes": ["secret_value_in_core_record"],
                    },
                    {
                        "name": "unresolved-artifact-reference.json",
                        "ok": True,
                        "errorCodes": ["unresolved_artifact_reference"],
                    },
                ],
            }
        ],
    }


def build_manifest(package: Path, release: str, stable: bool) -> None:
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
            "schema": "cap.core.release_manifest.v1",
            "release": release,
            "status": "stable" if stable else "release-candidate",
            "files": files,
        },
    )
    write_text(
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


def package_release(release: str, stable: bool) -> Path:
    package = ROOT / "release-artifacts" / release
    if package.exists():
        shutil.rmtree(package)
    package.mkdir(parents=True)

    for doc in CORE_DOCS + CORE_CAPP_AND_REVIEWS:
        copy_file(doc, package)
    copy_tree("schemas/core", package)
    copy_tree("fixtures/core", package)

    reports = package / "reports"
    conformance_l4 = build_core_conformance_report(ROOT, target_level="L4")
    conformance_l3 = build_core_conformance_report(ROOT, target_level="L3")
    reference_interop = build_core_interop_report(ROOT)
    second_interop = build_l0_l2_external_report()
    l4_comparison = compare_core_interop_reports(reference_interop, second_interop)
    write_json(reports / "core-conformance-report-l4.json", conformance_l4)
    write_json(reports / "core-l3-runevidence-producer-report.json", conformance_l3)
    write_json(reports / "core-interop-reference.json", reference_interop)
    write_json(reports / "core-interop-second-implementation-l0-l2.json", second_interop)
    write_json(reports / "core-interop-l4-comparison.json", l4_comparison)

    for fixture in CORE_FIXTURE_NAMES:
        inspection = build_core_inspection_report(ROOT, fixture)
        write_json(reports / f"core-inspection-{fixture}.json", inspection)
        write_text(reports / f"core-inspection-{fixture}.txt", render_inspection_report(inspection))

    status = "stable release" if stable else "release candidate"
    write_text(
        package / "README.md",
        f"""
# {release}

This package is the CAP-Core v1.0.0 {status} artifact set.

## Included

- stable scope, conformance, schema, fixture, security, bridge, registry, and
  maintenance documents;
- Core v1.0 schema package under `schemas/core/`;
- positive and negative fixture suites under `fixtures/core/`;
- conformance, inspection, L3, second-implementation, and L4 comparison reports;
- CAPP and review decision records.

## Reproduce

```bash
python reference/python/scripts/validate_schema_fixtures.py
python reference/python/scripts/validate_fixtures.py --scope core --report core-fixtures.json
python reference/python/scripts/validate_core_fixtures.py --target-level L4 --report core-conformance-report.json
python reference/python/scripts/render_core_inspection_report.py --fixture remote-service-binding --json-report core-inspection.json --text-report core-inspection.txt
python reference/python/scripts/package_core_release_artifacts.py --release {release}{' --stable' if stable else ''}
python reference/python/scripts/validate_core_release_manifest.py release-artifacts/{release}
```
""",
    )
    write_text(
        package / "release-notes.md",
        f"""
# {release} Release Notes

CAP-Core v1.0.0 {'stable' if stable else 'rc1'} covers the minimal Core
control-plane object contract: ArtifactSet, Artifact/ArtifactRef, Capability,
Binding, Assembly, PolicyDecision, Run, and RunEvidence. DigestBinding remains
a CAP-Digest bridge profile and does not change CAP-Digest behavior.

Release source commit is recorded by repository tag `cap-core-v1.0.0`.

Out of scope: runtime execution semantics, policy language semantics,
credential exchange, scientific correctness proof, and live external service
integration.
""",
    )
    write_text(
        package / "reference-version.txt",
        f"""
release: {release}
sourceRevision: recorded by repository tag cap-core-v1.0.0
validator: cap_core.reference_validator {CORE_VALIDATOR_VERSION}
status: {'stable' if stable else 'release-candidate'}
tagPlan: cap-core-v1.0.0
""",
    )

    build_manifest(package, release, stable)
    return package


def main() -> int:
    parser = ArgumentParser()
    parser.add_argument("--release", default="cap-core-v1.0.0-rc1")
    parser.add_argument("--stable", action="store_true")
    args = parser.parse_args()

    package = package_release(args.release, args.stable)
    print(f"wrote {package.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
