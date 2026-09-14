# Onda Komax Review Agent Instructions

This repository is the source of truth for the Komax review intelligence automation.


For now, keep the repo focused on Komax Coupang product review analysis, automation blueprints, mock review inputs, tests, and operating docs.

## Execution Rules

1. Keep changes scoped to Komax review intelligence unless the user explicitly expands the repo scope.
2. Do not commit generated reports or runtime outputs.
3. Keep report history in Notion or another external archive, not Git.
4. Use `.runtime/` only as a local fallback for unsent reports.
5. Do not modify Coupang listings, prices, ads, supplier orders, customer replies, or production systems.
6. Run relevant tests after code changes.

## Required Deliverables

Every implementation should include the durable artifacts needed to operate the change:

- Code or configuration changes
- Tests or validation steps
- Documentation under `docs/`
- Skill updates under `skills/komax-review-intelligence/` when analysis behavior changes
- Automation definitions under `automations/` when scheduled behavior changes

