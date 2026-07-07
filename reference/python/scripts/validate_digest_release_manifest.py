from __future__ import annotations

import json
import sys
from argparse import ArgumentParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]


REQUIRED_V1_FILES = {
    "capps/CAPP-0008-cap-digest-stable-entry-gates.md",
    "capps/CAPP-0009-cap-digest-v1.0.0-stable-release.md",
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
    "reports/digest-conformance-report.json",
    "reports/digest-interop-reference.json",
    "reports/digest-interop-independent-structural.json",
    "reports/digest-interop-comparison.json",
}


def validate_package(package: Path) -> list[str]:
    manifest_path = package / "MANIFEST.json"
    if not manifest_path.exists():
        return [f"{package}: missing MANIFEST.json"]

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    listed = sorted(manifest.get("files", []))
    actual = sorted(
        path.relative_to(package).as_posix()
        for path in package.rglob("*")
        if path.is_file() and path.name != "MANIFEST.json"
    )
    problems: list[str] = []
    if listed != actual:
        missing = sorted(set(actual) - set(listed))
        stale = sorted(set(listed) - set(actual))
        problems.extend(f"{package}: manifest missing {item}" for item in missing)
        problems.extend(f"{package}: manifest lists missing file {item}" for item in stale)

    release = manifest.get("release")
    if release in {"cap-digest-v1.0.0-rc1", "cap-digest-v1.0.0"}:
        package_files = set(actual)
        for required in sorted(REQUIRED_V1_FILES - package_files):
            problems.append(f"{package}: missing required v1 file {required}")
        comparison_path = package / "reports" / "digest-interop-comparison.json"
        if comparison_path.exists():
            comparison = json.loads(comparison_path.read_text(encoding="utf-8"))
            if comparison.get("ok") is not True:
                problems.append(f"{package}: interop comparison is not ok")

    return problems


def main() -> int:
    parser = ArgumentParser()
    parser.add_argument("packages", nargs="*", type=Path)
    args = parser.parse_args()

    packages = args.packages or sorted(
        path for path in (ROOT / "release-artifacts").glob("cap-digest-v1.0.0*") if path.is_dir()
    )
    problems = [problem for package in packages for problem in validate_package(package)]
    if problems:
        for problem in problems:
            print(problem)
        return 1
    print(f"digest release manifest validation ok: {len(packages)} package(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
