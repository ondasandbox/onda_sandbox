# Komax Review Intelligence

This automation analyzes Komax Coupang product reviews and produces recurring reports.

## Artifacts

| Artifact | Path |
| --- | --- |
| Skill | `skills/komax-review-intelligence/SKILL.md` |
| Daily automation | `automations/komax-review-daily.blueprint.yml` |
| Weekly automation | `automations/komax-review-weekly.blueprint.yml` |
| Monthly automation | `automations/komax-review-monthly.blueprint.yml` |
| Runtime scratch reports | `.runtime/reports/komax-reviews/` |
| Runtime outbox fallback | `.runtime/outbox/` |
| Durable report archive | Notion database, recommended: `Onda Komax Review Reports` |

## Cadence

| Cadence | Purpose |
| --- | --- |
| Daily | Catch urgent issues and meaningful changes |
| Weekly | Full product, theme, listing, and action report |
| Monthly | Strategy report for category and product decisions |

## Delivery And History

Do not keep report history in this repo. The repo should hold automation definitions, skills, docs, scripts, tests, and mock data only.

Use Notion as the primary report archive because it is easier to browse, filter, annotate, and turn report findings into action items. If raw exports become large, store raw files in a file archive such as Google Drive, Dropbox, S3, or another object store, and link them from the Notion report record.

The local fallback path is `.runtime/outbox/`, which is ignored by Git. Use it only when external delivery is not connected yet.

## Safety

The automation may only report and recommend. It must not modify Coupang listings, ads, prices, supplier orders, customer replies, or production systems.

## Local Run

```bash
python scripts/generate_komax_review_report.py --cadence daily
python scripts/generate_komax_review_report.py --cadence weekly
python scripts/generate_komax_review_report.py --cadence monthly
```
