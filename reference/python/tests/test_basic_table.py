from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
REFERENCE = ROOT / "reference" / "python"
if str(REFERENCE) not in sys.path:
    sys.path.insert(0, str(REFERENCE))

from cap_digest import assemble_table, validate_response  # noqa: E402


class BasicTableFixtureTest(unittest.TestCase):
    def setUp(self) -> None:
        fixture = ROOT / "fixtures" / "basic-table"
        self.source = json.loads((fixture / "source.json").read_text(encoding="utf-8"))
        self.policy = json.loads((fixture / "policy.json").read_text(encoding="utf-8"))
        self.expected_digest = (fixture / "expected-digest.txt").read_text(encoding="utf-8")
        self.expected_manifest = json.loads((fixture / "expected-manifest.json").read_text(encoding="utf-8"))
        self.expected_validation = json.loads((fixture / "expected-validation.json").read_text(encoding="utf-8"))
        self.negative_validation = json.loads((fixture / "negative-validation.json").read_text(encoding="utf-8"))

    def test_assemble_matches_fixture(self) -> None:
        result = assemble_table(self.source, self.policy)
        self.assertEqual(result.text, self.expected_digest)
        self.assertEqual(result.manifest, self.expected_manifest)

    def test_validate_response_matches_fixture(self) -> None:
        result = assemble_table(self.source, self.policy)
        validation = validate_response(result.text, result.manifest, self.expected_validation["response"])
        self.assertEqual(validation, self.expected_validation["validation"])

    def test_negative_validation_cases_match_fixture(self) -> None:
        result = assemble_table(self.source, self.policy)
        for case in self.negative_validation["cases"]:
            with self.subTest(case=case["name"]):
                validation = validate_response(result.text, result.manifest, case["response"])
                self.assertEqual(validation, case["validation"])


if __name__ == "__main__":
    unittest.main()
