from __future__ import annotations

import json
import sys
from argparse import ArgumentParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
REFERENCE = ROOT / "reference" / "python"
if str(REFERENCE) not in sys.path:
    sys.path.insert(0, str(REFERENCE))

from cap_digest import assemble_table, gate_requests, load_table_basic_pack, validate_response  # noqa: E402
from cap_core import load_local_analysis_fixture, render_review_summary, validate_core_fixture, validate_negative_record  # noqa: E402


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    parser = ArgumentParser()
    parser.add_argument("--report", type=Path, default=None)
    args = parser.parse_args()

    checks = [
        ("fixtures/basic-table", validate_basic_table()),
        ("fixtures/followup-basic", validate_followup_basic()),
        ("fixtures/pack-table-basic", validate_pack_table_basic()),
        ("fixtures/core/local-analysis", validate_core_local_analysis()),
    ]
    problems = [problem for _, fixture_problems in checks for problem in fixture_problems]
    report = {
        "schema": "cap.conformance_report.v1",
        "ok": not problems,
        "checks": [{"name": name, "ok": not fixture_problems, "problems": fixture_problems} for name, fixture_problems in checks],
    }
    if args.report is not None:
        args.report.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    if problems:
        for problem in problems:
            print(f"CHECK: {problem}")
        return 1

    for name, _ in checks:
        print(f"OK: {name}")
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

    negative = load_json(fixture / "negative-validation.json")
    for case in negative["cases"]:
        actual = validate_response(result.text, result.manifest, case["response"])
        if actual != case["validation"]:
            problems.append(f"negative validation mismatch: {case['name']}")
    return problems


def validate_followup_basic() -> list[str]:
    fixture = ROOT / "fixtures" / "followup-basic"
    source = load_json(fixture / "source.json")
    policy = load_json(fixture / "policy.json")
    response = load_json(fixture / "response.json")
    expected_gate = load_json(fixture / "expected-gate.json")
    expected_patch = load_json(fixture / "expected-patch.json")

    result = assemble_table(source, policy)
    decisions = gate_requests(result.text, result.manifest, response, source, policy)
    rendered_gate = {
        "schema": "cap.gate_result.v1",
        "decisions": [
            {
                "fieldId": decision.fieldId,
                "allowed": decision.allowed,
                "reason": decision.reason,
                "patchSchema": decision.patch["schema"] if decision.patch else None,
            }
            for decision in decisions
        ],
    }
    problems: list[str] = []
    if rendered_gate != expected_gate:
        problems.append("follow-up gate decision mismatch")
    patches = [decision.patch for decision in decisions if decision.patch is not None]
    if patches != [expected_patch]:
        problems.append("follow-up digest patch mismatch")
    return problems


def validate_pack_table_basic() -> list[str]:
    expected = load_json(ROOT / "fixtures" / "pack-table-basic" / "expected-pack.json")
    pack = load_table_basic_pack(ROOT)
    actual = {
        "schema": "cap.pack_validation.v1",
        "pack": {
            "name": pack["name"],
            "sourceTypes": pack["sourceTypes"],
            "fieldIds": [field["id"] for field in pack["fields"]],
            "redactors": pack["redactors"],
        },
    }
    if actual != expected:
        return ["pack table-basic validation mismatch"]
    return []


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
