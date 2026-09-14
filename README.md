# Onda Komax Review Intelligence

This repo is focused on Komax Coupang review intelligence and automation.

It contains the skill, automation blueprints, local mock data, and report-generation scripts needed for Hermes to run daily, weekly, and monthly review analysis safely.

Generated reports should not be committed to this repo. Store report history in Notion or another external archive, and use the repo only for durable automation definitions, skills, scripts, tests, mock inputs, and operating docs.

## Quick Start

```powershell
python scripts/validate_onda_sandbox.py
python scripts/run_komax_review_automation.py --cadence daily
python -m unittest discover -s tests
```

On Ubuntu, from the Hermes host:

```bash
git clone <your-repo-url> /home/onda/onda
cd /home/onda/onda
python3 scripts/validate_onda_sandbox.py
python3 scripts/run_komax_review_automation.py --cadence daily
```

## Cadence

| Cadence | Purpose |
| --- | --- |
| Daily | Catch urgent negative signals and meaningful product changes |
| Weekly | Produce the full product, theme, listing, and action report |
| Monthly | Produce strategy recommendations across categories and products |

## Repository Map

| Path | Purpose |
| --- | --- |
| `AGENTS.md` | Project instructions loaded by coding agents in this repo |
| `skills/komax-review-intelligence/SKILL.md` | Komax Coupang review analysis skill |
| `automations/komax-review-*.blueprint.yml` | Daily, weekly, and monthly automation definitions |
| `scripts/generate_komax_review_report.py` | Generates Komax daily, weekly, or monthly reports |
| `scripts/run_komax_review_automation.py` | Hermes-friendly Komax automation entrypoint |
| `sandbox/komax_reviews/` | Mock or exported Komax review data |
| `docs/operations/komax-review-intelligence.md` | Operating notes for review automation |
| `docs/operations/hermes-komax-review-integration.md` | Hermes setup instructions |
| `tests/` | Local tests |

## Report Storage

Use Notion as the preferred human-readable report archive. The scripts write local fallback files under `.runtime/`, which is ignored by Git.

