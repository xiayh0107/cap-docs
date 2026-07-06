from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
REFERENCE = ROOT / "reference" / "python"
if str(REFERENCE) not in sys.path:
    sys.path.insert(0, str(REFERENCE))

from cap_digest import parse_digest_text, validate_manifest_text_consistency  # noqa: E402


class DigestTextTest(unittest.TestCase):
    def test_basic_table_digest_text_is_consistent(self) -> None:
        fixture = ROOT / "fixtures" / "basic-table"
        text = (fixture / "expected-digest.txt").read_text(encoding="utf-8")
        manifest = json.loads((fixture / "expected-manifest.json").read_text(encoding="utf-8"))
        parsed = parse_digest_text(text)
        self.assertEqual(set(parsed.field_ids), {"f1:table@shape#base", "f1:table@columns#compact"})
        self.assertEqual(validate_manifest_text_consistency(parsed, manifest), [])

    def test_duplicate_field_id_is_rejected(self) -> None:
        text = (ROOT / "fixtures" / "digest-text-negative" / "duplicate-field-id.txt").read_text(encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "text_duplicate_field_id"):
            parse_digest_text(text)

    def test_negative_fixture_parse_errors_are_stable(self) -> None:
        fixture = ROOT / "fixtures" / "digest-text-negative"
        cases = {
            "invalid-field-id.txt": "text_invalid_field_id",
            "unclosed-data-fence.txt": "text_unclosed_data",
        }

        for filename, error_code in cases.items():
            with self.subTest(filename=filename):
                text = (fixture / filename).read_text(encoding="utf-8")
                with self.assertRaisesRegex(ValueError, error_code):
                    parse_digest_text(text)

    def test_manifest_text_mismatch_fixtures_report_problem_codes(self) -> None:
        fixture = ROOT / "fixtures" / "digest-text-negative"
        manifest = json.loads((ROOT / "fixtures" / "basic-table" / "expected-manifest.json").read_text(encoding="utf-8"))

        missing_text = (fixture / "manifest-missing-selected-field.txt").read_text(encoding="utf-8")
        missing_problems = validate_manifest_text_consistency(parse_digest_text(missing_text), manifest)
        self.assertEqual(
            [{"code": "evidence_missing_from_text", "fieldId": "f1:table@columns#compact"}],
            missing_problems,
        )

        unknown_text = (fixture / "unknown-text-field.txt").read_text(encoding="utf-8")
        unknown_problems = validate_manifest_text_consistency(parse_digest_text(unknown_text), manifest)
        self.assertEqual(
            [{"code": "text_field_missing_from_manifest", "fieldId": "f1:table@sample#k10"}],
            unknown_problems,
        )


if __name__ == "__main__":
    unittest.main()
