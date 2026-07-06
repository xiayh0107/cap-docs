from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
REFERENCE = ROOT / "reference" / "python"
if str(REFERENCE) not in sys.path:
    sys.path.insert(0, str(REFERENCE))

from cap_digest import assemble_table, validate_response  # noqa: E402
from cap_core import load_local_analysis_fixture, render_review_summary, validate_core_fixture, validate_negative_record  # noqa: E402


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    problems = validate_basic_table() + validate_core_local_analysis()
    if problems:
        for problem in problems:
            print(f"CHECK: {problem}")
        return 1

    print("OK: fixtures/basic-table")
    print("OK: fixtures/core/local-analysis")
    return 0


def validate_basic_table() -> list[str]:
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
    return problems


def validate_core_local_analysis() -> list[str]:
    fixture_path = ROOT / "fixtures" / "core" / "local-analysis"
    fixture = load_local_analysis_fixture(ROOT)
    expected_validation = load_json(fixture_path / "expected-validation.json")
    expected_summary = (fixture_path / "expected-review-summary.txt").read_text(encoding="utf-8")

    validation = validate_core_fixture(fixture)
    rendered_summary = render_review_summary(fixture)

    problems: list[str] = []
    if validation.as_dict() != {
        "ok": expected_validation["ok"],
        "errors": expected_validation["errors"],
        "warnings": expected_validation["warnings"],
        "summary": expected_validation["summary"],
    }:
        problems.append("core local-analysis validation mismatch")
    if rendered_summary != expected_summary:
        problems.append("core local-analysis review summary mismatch")

    for filename, expected in expected_validation["negativeFixtures"].items():
        record = load_json(fixture_path / "negative" / filename)
        negative = validate_negative_record(record, filename)
        actual_codes = sorted({error["code"] for error in negative.errors})
        expected_codes = sorted(expected["errorCodes"])
        if negative.ok != expected["ok"] or actual_codes != expected_codes:
            problems.append(f"core negative fixture mismatch: {filename}")

    return problems


if __name__ == "__main__":
    sys.exit(main())
