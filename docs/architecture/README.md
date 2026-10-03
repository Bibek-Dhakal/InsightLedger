# Architecture

The system leverages standard OSS tools for data operations.

## Components

1. **PostgreSQL**: Analytical data store, holds raw mock data and transformed models.
2. **dbt-postgres**: Handles data modeling, staging, transformation, and automated reconciliation tests.
3. **Jupyter Notebooks**: Statistical analysis environment (A/B testing, SRM checks, Confidence Intervals).
4. **Metabase**: Provides the self-serve BI layer. Read-only access to `marts` models.

## Data Flow

`scripts/init_db.py (Mock Source)` -> `PostgreSQL (Public Schema)` -> `dbt (Staging -> Marts)` -> `Metabase (Dashboard)`
