from __future__ import annotations

import json
import sys
from argparse import ArgumentParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
REFERENCE = ROOT / "reference" / "python"
if str(REFERENCE) not in sys.path:
    sys.path.insert(0, str(REFERENCE))

from cap_core import CORE_FIXTURE_NAMES, build_core_inspection_report, render_inspection_report  # noqa: E402


def main() -> int:
    parser = ArgumentParser()
    parser.add_argument("--fixture", choices=CORE_FIXTURE_NAMES, default="local-analysis")
    parser.add_argument("--json-report", type=Path, default=None)
    parser.add_argument("--text-report", type=Path, default=None)
    args = parser.parse_args()

    report = build_core_inspection_report(ROOT, args.fixture)
    text = render_inspection_report(report)
    if args.json_report is not None:
        args.json_report.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    if args.text_report is not None:
        args.text_report.write_text(text, encoding="utf-8")
    if args.json_report is None and args.text_report is None:
        print(text, end="")
    return 0 if report["diagnostics"]["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
