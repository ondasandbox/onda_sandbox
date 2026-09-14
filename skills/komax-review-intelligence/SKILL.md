---
name: komax-review-intelligence
description: Analyze Komax Coupang product reviews and produce daily, weekly, or monthly reports for product, listing, and operations decisions.
---

# Komax Review Intelligence

Use this skill to monitor Komax products on Coupang and turn product reviews into practical actions.

## Source

Primary brand page:

```text
https://www.coupang.com/np/products/brand-shop?listSize=60&sorter=bestAsc&brandName=%EC%BD%94%EB%A9%95%EC%8A%A4
```

If live access is unavailable, use saved exports or mock data under `sandbox/komax_reviews/`.

## Cadence

Run in one of three modes:

- `daily`: detect meaningful changes and urgent negative signals.
- `weekly`: produce a full product and theme report.
- `monthly`: produce a strategy report with category, product, and listing recommendations.

## Analysis Requirements

Analyze:

- Rating, review count, and recent review velocity
- Positive and negative sentiment themes
- Repeated defect or quality complaints
- Listing confusion such as size, material, capacity, use, or compatibility
- Purchase drivers and repeat-purchase language
- Product improvement opportunities
- Products that deserve promotion, listing refresh, QA attention, or human review

Pay special attention to:

- Leaking
- Broken or loose lids
- Weak insulation
- Plastic smell
- Scratches or shipping damage
- Wrong size expectations
- Cleaning difficulty
- Durability complaints
- Packaging damage

## Output

Do not commit generated reports to this repository.

Send each report to the configured external archive, preferably Notion for human-readable operating history. If the runtime needs a local handoff file, write it under:

```text
.runtime/reports/komax-reviews/<cadence>/YYYY-MM-DD.md
```

Optionally create a matching local delivery copy under:

```text
.runtime/outbox/
```

The local runtime folders are ignored by Git. The durable report history should live outside the repo.

## Daily Report

Keep the daily report short. Include:

- New or worsening issues
- Products needing immediate attention
- Review count or rating changes
- Recommended next action

Stay quiet when there are no meaningful changes unless the automation explicitly asks for a heartbeat.

## Weekly Report

Include:

- Executive summary
- Product alert table
- Top positive themes
- Top negative themes
- Listing fixes
- Product or packaging improvement ideas
- Action queue

## Monthly Report

Include:

- Category-level trend summary
- Strongest and weakest products
- Repeated cross-product issues
- Listing strategy recommendations
- Product development opportunities
- Suggested priorities for the next month

## Safety

Do not modify Coupang listings, pricing, ads, supplier orders, customer responses, or production systems. This skill only produces analysis and recommendations unless a human explicitly approves a separate execution issue.
