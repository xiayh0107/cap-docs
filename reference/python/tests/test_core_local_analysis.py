from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
REFERENCE = ROOT / "reference" / "python"
if str(REFERENCE) not in sys.path:
    sys.path.insert(0, str(REFERENCE))

from cap_core import (  # noqa: E402
    CORE_FIXTURE_NAMES,
    build_core_conformance_report,
    build_core_inspection_report,
    build_core_inspection_report_from_fixture,
    build_core_interop_report,
    compare_core_interop_reports,
    load_core_fixture,
    render_inspection_report,
    render_review_summary,
    validate_core_fixture,
    validate_core_negative_suite,
    validate_negative_case,
    validate_negative_record,
)


CORE_FIXTURES = CORE_FIXTURE_NAMES


class CoreFixtureTest(unittest.TestCase):
    def fixture_context(self, name: str) -> tuple[Path, dict, dict, str]:
        fixture_path = ROOT / "fixtures" / "core" / name
        fixture = load_core_fixture(ROOT, name)
        expected_validation = json.loads((fixture_path / "expected-validation.json").read_text(encoding="utf-8"))
        expected_summary = (fixture_path / "expected-review-summary.txt").read_text(encoding="utf-8")
        return fixture_path, fixture, expected_validation, expected_summary

    def test_validate_core_fixtures_match_expected(self) -> None:
        for name in CORE_FIXTURES:
            with self.subTest(fixture=name):
                _fixture_path, fixture, expected_validation, _expected_summary = self.fixture_context(name)
                validation = validate_core_fixture(fixture)
                self.assertEqual(
                    validation.as_dict(),
                    {
                        "ok": expected_validation["ok"],
                        "errors": expected_validation["errors"],
                        "warnings": expected_validation["warnings"],
                        "summary": expected_validation["summary"],
                    },
                )

    def test_render_review_summaries_match_expected(self) -> None:
        for name in CORE_FIXTURES:
            with self.subTest(fixture=name):
                _fixture_path, fixture, _expected_validation, expected_summary = self.fixture_context(name)
                self.assertEqual(render_review_summary(fixture), expected_summary)

    def test_negative_fixtures_match_expected_errors(self) -> None:
        for name in CORE_FIXTURES:
            fixture_path, _fixture, expected_validation, _expected_summary = self.fixture_context(name)
            for filename, expected in expected_validation["negativeFixtures"].items():
                with self.subTest(fixture=name, filename=filename):
                    record = json.loads((fixture_path / "negative" / filename).read_text(encoding="utf-8"))
                    if record.get("schema") == "cap.core.negative_case.v1":
                        validation = validate_negative_case(record, filename)
                    else:
                        validation = validate_negative_record(record, filename)
                    actual_codes = sorted({error["code"] for error in validation.errors})
                    self.assertEqual(validation.ok, expected["ok"])
                    self.assertEqual(actual_codes, sorted(expected["errorCodes"]))

    def test_core_negative_suite_matches_expected_errors(self) -> None:
        validation = validate_core_negative_suite(ROOT)
        self.assertTrue(validation["ok"], validation["problems"])
        self.assertGreaterEqual(len(validation["cases"]), 10)

    def test_core_conformance_report_shape(self) -> None:
        report = build_core_conformance_report(ROOT)
        self.assertEqual(report["schema"], "cap.core.conformance_report.v1")
        self.assertEqual(report["targetLevel"], "L3")
        self.assertTrue(report["ok"])
        self.assertEqual([fixture["name"] for fixture in report["fixtures"]], list(CORE_FIXTURES))
        self.assertEqual(report["negativeSuites"][0]["name"], "fixtures/core/negative")
        for fixture in report["fixtures"]:
            self.assertIn("schema", {check["category"] for check in fixture["checks"]})
            self.assertIn("security", {check["category"] for check in fixture["checks"]})

    def test_inspection_reports_cover_positive_and_negative_diagnostics(self) -> None:
        for name in ("local-analysis", "remote-service-binding"):
            with self.subTest(fixture=name):
                report = build_core_inspection_report(ROOT, name)
                text = render_inspection_report(report)
                self.assertEqual(report["schema"], "cap.core.inspection_report.v1")
                self.assertIn("objectGraph", report)
                self.assertIn("bindings", report)
                self.assertIn("policy", report)
                self.assertIn("evidence", report)
                self.assertIn("CAP-Core inspection report\n", text)
                self.assertIn("Diagnostics:", text)

        bad_fixture = load_core_fixture(ROOT, "local-analysis")
        bad_fixture["run_evidence"]["records"]["semanticCorrectnessVerifiedByCore"] = True
        report = build_core_inspection_report_from_fixture("mutated-negative", "memory://mutated-negative", bad_fixture)
        text = render_inspection_report(report)
        self.assertFalse(report["diagnostics"]["ok"])
        self.assertIn("run_evidence_overclaims_correctness", text)

    def test_interop_report_and_comparison(self) -> None:
        expected = build_core_interop_report(ROOT)
        actual = build_core_interop_report(ROOT, implementation_name="external.example")
        comparison = compare_core_interop_reports(expected, actual)
        self.assertEqual(expected["schema"], "cap.core.interop_report.v1")
        self.assertTrue(comparison["ok"], comparison)

        actual["fixtures"][0]["errorCodes"] = ["unknown_reference"]
        mismatch = compare_core_interop_reports(expected, actual)
        self.assertFalse(mismatch["ok"])
        self.assertTrue(
            any("error_codes_mismatch" in check["problems"] for check in mismatch["checks"]),
            mismatch,
        )

    def test_digest_bridge_preserves_run_evidence_separation(self) -> None:
        validation = validate_core_negative_suite(ROOT)
        negative_codes = {
            code
            for case in validation["cases"]
            for code in case["actualErrorCodes"]
        }
        self.assertIn("digest_evidence_used_as_run_evidence", negative_codes)
        self.assertIn("digest_binding_collapses_evidence_layers", negative_codes)

        for name in CORE_FIXTURES:
            with self.subTest(fixture=name):
                fixture = load_core_fixture(ROOT, name)
                digest = fixture["digest_view_ref"]
                self.assertEqual(digest["type"], "digest")
                self.assertIs(digest["constraints"]["digestEvidenceIsRunEvidence"], False)
                self.assertEqual(digest["constraints"]["sourceRunEvidence"], fixture["run_evidence"]["id"])


if __name__ == "__main__":
    unittest.main()
