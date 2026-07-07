from __future__ import annotations

import json
import sys
from argparse import ArgumentParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]


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
    return problems


def main() -> int:
    parser = ArgumentParser()
    parser.add_argument("packages", nargs="*", type=Path)
    args = parser.parse_args()

    packages = args.packages or sorted(
        path for path in (ROOT / "release-artifacts").glob("cap-core-v1.0.0*") if path.is_dir()
    )
    problems = [problem for package in packages for problem in validate_package(package)]
    if problems:
        for problem in problems:
            print(problem)
        return 1
    print(f"core release manifest validation ok: {len(packages)} package(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
