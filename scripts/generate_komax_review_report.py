#!/usr/bin/env python3
"""Generate a sandbox Komax review intelligence report."""

from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALID_CADENCES = {"daily", "weekly", "monthly"}


def load_products(source_dir: Path) -> list[dict]:
    products_file = source_dir / "products.json"
    if not products_file.exists():
        return []
    with products_file.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def summarize_products(products: list[dict]) -> str:
    if not products:
        return "- No product review data found yet. Add exports under `sandbox/komax_reviews/`."

    lines = []
    for product in products:
        negatives = ", ".join(product.get("recent_negative_themes", [])) or "none"
        positives = ", ".join(product.get("recent_positive_themes", [])) or "none"
        lines.append(
            "- {name} ({category}): rating {rating}, {reviews} reviews. "
            "Praise: {positives}. Watch: {negatives}.".format(
                name=product.get("product_name", "Unknown product"),
                category=product.get("category", "uncategorized"),
                rating=product.get("rating", "n/a"),
                reviews=product.get("review_count", "n/a"),
                positives=positives,
                negatives=negatives,
            )
        )
    return "\n".join(lines)


def report_sections(cadence: str, products: list[dict]) -> str:
    product_summary = summarize_products(products)
    if cadence == "daily":
        return (
            "## Daily Signals\n\n"
            f"{product_summary}\n\n"
            "## Immediate Actions\n\n"
            "- Review products with fresh complaints about defects, leakage, insulation, or shipping damage.\n"
            "- Escalate only when the same issue appears repeatedly or rating movement is material.\n"
        )
    if cadence == "weekly":
        return (
            "## Executive Summary\n\n"
            "- Review product health, sentiment themes, listing confusion, and action items.\n\n"
            "## Product Alerts\n\n"
            f"{product_summary}\n\n"
            "## Theme Analysis\n\n"
            "- Track positive drivers, negative complaints, and repeated defect language.\n\n"
            "## Listing Fixes\n\n"
            "- Look for confusion about dimensions, capacity, materials, cleaning, and use cases.\n\n"
            "## Action Queue\n\n"
            "- Must fix now\n"
            "- Review this week\n"
            "- Watch only\n"
        )
    return (
        "## Strategy Summary\n\n"
        "- Review category-level trends and product opportunities.\n\n"
        "## Product Portfolio\n\n"
        f"{product_summary}\n\n"
        "## Cross-Product Issues\n\n"
        "- Compare repeated quality, packaging, and expectation gaps across categories.\n\n"
        "## Next-Month Priorities\n\n"
        "- Choose listing refreshes, QA follow-ups, and product development candidates.\n"
    )


def build_report(cadence: str, products: list[dict], run_date: date) -> str:
    title = f"Komax Review Intelligence - {cadence.title()} - {run_date.isoformat()}"
    return (
        f"# {title}\n\n"
        "Source: Coupang Komax brand review monitoring\n\n"
        "Safety: analysis only. Do not modify listings, ads, prices, orders, or customer replies.\n\n"
        f"{report_sections(cadence, products)}\n"
    )


def write_report(cadence: str, source_dir: Path, reports_dir: Path, outbox_dir: Path) -> tuple[Path, Path]:
    today = date.today()
    products = load_products(source_dir)
    report = build_report(cadence, products, today)

    target_dir = reports_dir / cadence
    target_dir.mkdir(parents=True, exist_ok=True)
    outbox_dir.mkdir(parents=True, exist_ok=True)

    report_path = target_dir / f"{today.isoformat()}.md"
    outbox_path = outbox_dir / f"komax-review-{cadence}-{today.isoformat()}.md"
    report_path.write_text(report, encoding="utf-8")
    outbox_path.write_text(report, encoding="utf-8")
    return report_path, outbox_path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cadence", choices=sorted(VALID_CADENCES), required=True)
    parser.add_argument("--source-dir", type=Path, default=ROOT / "sandbox" / "komax_reviews")
    parser.add_argument("--reports-dir", type=Path, default=ROOT / ".runtime" / "reports" / "komax-reviews")
    parser.add_argument("--outbox-dir", type=Path, default=ROOT / ".runtime" / "outbox")
    args = parser.parse_args()

    report_path, outbox_path = write_report(
        args.cadence,
        args.source_dir,
        args.reports_dir,
        args.outbox_dir,
    )
    print(f"wrote report: {report_path}")
    print(f"wrote outbox copy: {outbox_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
