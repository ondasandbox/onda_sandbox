#!/usr/bin/env python3
"""Hermes-friendly entrypoint for Komax review automation."""

from __future__ import annotations

import argparse
import os
from pathlib import Path

from generate_komax_review_report import VALID_CADENCES, write_report


ROOT = Path(__file__).resolve().parents[1]


def notion_configured() -> bool:
    return bool(os.getenv("NOTION_TOKEN") and os.getenv("ONDA_KOMAX_REPORTS_DATABASE_ID"))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cadence", choices=sorted(VALID_CADENCES), required=True)
    args = parser.parse_args()

    report_path, outbox_path = write_report(
        cadence=args.cadence,
        source_dir=ROOT / "sandbox" / "komax_reviews",
        reports_dir=ROOT / ".runtime" / "reports" / "komax-reviews",
        outbox_dir=ROOT / ".runtime" / "outbox",
    )

    print(f"Komax {args.cadence} report generated.")
    print(f"Runtime report: {report_path}")
    print(f"Outbox fallback: {outbox_path}")

    if notion_configured():
        print(
            "Notion credentials are configured. Archive delivery can be wired to "
            "ONDA_KOMAX_REPORTS_DATABASE_ID in the next integration step."
        )
    else:
        print("Notion credentials are not configured. Report remains in .runtime/outbox/.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

