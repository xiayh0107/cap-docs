from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
REFERENCE = ROOT / "reference" / "python"
if str(REFERENCE) not in sys.path:
    sys.path.insert(0, str(REFERENCE))

from cap_core import load_local_analysis_fixture, render_review_summary, validate_core_fixture, validate_negative_record  # noqa: E402


class CoreLocalAnalysisFixtureTest(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture_path = ROOT / "fixtures" / "core" / "local-analysis"
        self.fixture = load_local_analysis_fixture(ROOT)
        self.expected_validation = json.loads((self.fixture_path / "expected-validation.json").read_text(encoding="utf-8"))
        self.expected_summary = (self.fixture_path / "expected-review-summary.txt").read_text(encoding="utf-8")

    def test_validate_core_fixture_matches_expected(self) -> None:
        validation = validate_core_fixture(self.fixture)
        self.assertEqual(
            validation.as_dict(),
            {
                "ok": self.expected_validation["ok"],
                "errors": self.expected_validation["errors"],
                "warnings": self.expected_validation["warnings"],
                "summary": self.expected_validation["summary"],
            },
        )

    def test_render_review_summary_matches_expected(self) -> None:
        self.assertEqual(render_review_summary(self.fixture), self.expected_summary)

    def test_negative_fixtures_match_expected_errors(self) -> None:
        for filename, expected in self.expected_validation["negativeFixtures"].items():
            with self.subTest(filename=filename):
                record = json.loads((self.fixture_path / "negative" / filename).read_text(encoding="utf-8"))
                validation = validate_negative_record(record, filename)
                actual_codes = sorted({error["code"] for error in validation.errors})
                self.assertEqual(validation.ok, expected["ok"])
                self.assertEqual(actual_codes, sorted(expected["errorCodes"]))


if __name__ == "__main__":
    unittest.main()
