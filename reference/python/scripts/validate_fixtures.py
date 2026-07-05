from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
REFERENCE = ROOT / "reference" / "python"
if str(REFERENCE) not in sys.path:
    sys.path.insert(0, str(REFERENCE))

from cap_digest import assemble_table, validate_response  # noqa: E402


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    fixture = ROOT / "fixtures" / "basic-table"
    source = load_json(fixture / "source.json")
    policy = load_json(fixture / "policy.json")
    expected_digest = (fixture / "expected-digest.txt").read_text(encoding="utf-8")
    expected_manifest = load_json(fixture / "expected-manifest.json")
    expected_validation = load_json(fixture / "expected-validation.json")

    result = assemble_table(source, policy)
    validation = validate_response(result.text, result.manifest, expected_validation["response"])

    problems: list[str] = []
    if result.text != expected_digest:
        problems.append("digest output mismatch")
    if result.manifest != expected_manifest:
        problems.append("manifest output mismatch")
    if validation != expected_validation["validation"]:
        problems.append("validation output mismatch")

    if problems:
        for problem in problems:
            print(f"CHECK: {problem}")
        return 1

    print("OK: fixtures/basic-table")
    return 0


if __name__ == "__main__":
    sys.exit(main())
