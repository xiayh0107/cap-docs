from __future__ import annotations

import json
import sys
from argparse import ArgumentParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
REFERENCE = ROOT / "reference" / "python"
if str(REFERENCE) not in sys.path:
    sys.path.insert(0, str(REFERENCE))

from cap_core import build_core_conformance_report  # noqa: E402


def main() -> int:
    parser = ArgumentParser()
    parser.add_argument("--report", type=Path, default=None)
    parser.add_argument("--target-level", default="L3")
    args = parser.parse_args()

    report = build_core_conformance_report(ROOT, target_level=args.target_level)
    if args.report is not None:
        args.report.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    if not report["ok"]:
        print(json.dumps(report, indent=2, sort_keys=True))
        return 1
    print(f"core conformance report ok: {len(report['fixtures'])} fixtures, {len(report['negativeSuites'][0]['cases'])} negative cases")
    return 0


if __name__ == "__main__":
    sys.exit(main())
