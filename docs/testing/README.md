# Testing Strategy

InsightLedger enforces two distinct types of testing:

## 1. Data Testing (dbt)

Executed via `dbt build` or `dbt test`.
Ensures:

- Primary keys are unique and non-null.
- Reconciled numbers match source expectations.
- Foreign keys map correctly.

## 2. Application Logic Testing (pytest)

Executed via `pytest tests/`.
Ensures:

- Dependencies are correctly loaded.
- Analytical logic functions resolve as expected.
