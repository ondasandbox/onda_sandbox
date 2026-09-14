# Hermes Komax Review Integration

This guide connects Hermes to the Komax Review Intelligence automation.

## Goal

Hermes should run the Komax review analysis on a schedule, archive the report outside Git, and create follow-up GitHub issues only when the report finds actionable work.

The repo remains the source of truth for:

- Skill instructions
- Automation definitions
- Scripts
- Tests
- Operating docs

Report history should live in Notion or another external archive, not in Git.

## Ubuntu Setup

Clone the repo on the Hermes host:

```bash
git clone <your-github-repo-url> /home/onda/onda
cd /home/onda/onda
python3 -m unittest discover -s tests
python3 scripts/validate_onda_sandbox.py
```

Authenticate GitHub:

```bash
gh auth login
gh repo view
```

Optional Notion environment variables:

```bash
export NOTION_TOKEN="..."
export ONDA_KOMAX_REPORTS_DATABASE_ID="..."
```

If Notion is not connected yet, Hermes should write to `.runtime/outbox/` and mention that external archive delivery is pending.

## Hermes Cron Jobs

Create three Hermes cron jobs using `/home/onda/onda` as the workdir.

### Daily

Schedule:

```text
every day at 08:00 Asia/Seoul
```

Prompt:

```text
Use the Komax Review Intelligence skill at `skills/komax-review-intelligence/SKILL.md`.

Run the daily Komax review scan using:

python3 scripts/run_komax_review_automation.py --cadence daily

Archive the report in the configured external archive. If external archive credentials are unavailable, leave the report in `.runtime/outbox/` and do not commit it.

Only create a GitHub issue if the report identifies a concrete follow-up action. Any issue must include `onda-approved` only after human approval; do not self-approve execution work.
```

### Weekly

Schedule:

```text
every Monday at 09:00 Asia/Seoul
```

Prompt:

```text
Use the Komax Review Intelligence skill at `skills/komax-review-intelligence/SKILL.md`.

Run the weekly Komax review analysis using:

python3 scripts/run_komax_review_automation.py --cadence weekly

Archive the report in the configured external archive. If external archive credentials are unavailable, leave the report in `.runtime/outbox/` and do not commit it.

Create draft follow-up GitHub issues only for clear product, listing, QA, or data-collection actions. Do not add `hermes-ready` unless a human has approved the issue.
```

### Monthly

Schedule:

```text
first day of every month at 10:00 Asia/Seoul
```

Prompt:

```text
Use the Komax Review Intelligence skill at `skills/komax-review-intelligence/SKILL.md`.

Run the monthly Komax review strategy report using:

python3 scripts/run_komax_review_automation.py --cadence monthly

Archive the report in the configured external archive. If external archive credentials are unavailable, leave the report in `.runtime/outbox/` and do not commit it.

Create draft GitHub issues for strategic follow-up candidates, but leave prioritization and approval to a human.
```

## Local Smoke Test

From the repo root:

```bash
python3 scripts/run_komax_review_automation.py --cadence daily
python3 scripts/run_komax_review_automation.py --cadence weekly
python3 scripts/run_komax_review_automation.py --cadence monthly
```

Outputs should be under `.runtime/`, which is ignored by Git.

## Follow-Up Issue Rule

Hermes may create a follow-up issue when a report finds a concrete action, such as:

- Product detail page needs clearer dimensions
- Repeated complaint suggests QA review
- Packaging damage appears repeatedly
- Review data source failed or changed shape

Hermes should not directly modify listings, pricing, ads, supplier orders, or customer communications.

