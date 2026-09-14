#!/usr/bin/env python3
"""Validate the Onda Komax review intelligence sandbox."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def require(path: Path) -> None:
    if not path.exists():
        raise AssertionError(f"Missing required path: {path}")


def main() -> int:
    required_paths = [
        ROOT / "AGENTS.md",
        ROOT / "README.md",
        ROOT / "skills" / "komax-review-intelligence" / "SKILL.md",
        ROOT / "automations" / "README.md",
        ROOT / "automations" / "komax-review-daily.blueprint.yml",
        ROOT / "automations" / "komax-review-weekly.blueprint.yml",
        ROOT / "automations" / "komax-review-monthly.blueprint.yml",
        ROOT / "docs" / "operations" / "hermes-komax-review-integration.md",
        ROOT / "docs" / "operations" / "komax-review-intelligence.md",
        ROOT / "sandbox" / "README.md",
        ROOT / "sandbox" / "komax_reviews" / "README.md",
        ROOT / "sandbox" / "komax_reviews" / "products.json",
        ROOT / "scripts" / "generate_komax_review_report.py",
        ROOT / "scripts" / "run_komax_review_automation.py",
        ROOT / "tests" / "test_generate_komax_review_report.py",
    ]
    for path in required_paths:
        require(path)

    report = load_module(ROOT / "scripts" / "generate_komax_review_report.py", "komax_report")
    products = report.load_products(ROOT / "sandbox" / "komax_reviews")
    if not products:
        raise AssertionError("Expected at least one Komax mock product")

    print("Onda Komax review sandbox validation passed.")
    print(f"Komax mock products: {len(products)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

