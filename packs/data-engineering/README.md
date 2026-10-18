# Pack: Data Engineering and Analytics

Use for data pipelines, analytical models, reporting, and ETL/ELT.

## Standards
- Define source/target schemas, ownership, freshness, and data contracts.
- Specify timezone, currency, null, deduplication, late-arriving data, and correction rules.
- Prefer idempotent and restartable jobs.
- Validate uniqueness, completeness, accepted values, referential integrity, and reconciliation.
- Keep sensitive data out of debug logs and development fixtures.
- Make backfills bounded, observable, and safe to rerun.

## Suggested tools
- dbt Core: https://github.com/dbt-labs/dbt-core (supported analytical transformations)
- Great Expectations: https://github.com/great-expectations/great_expectations
- Trivy: https://github.com/aquasecurity/trivy (where artifact/dependency scanning applies)

## Verification
Use representative fixtures, schema checks, data-quality assertions, row-count/reconciliation checks, and a documented recovery/backfill plan.
