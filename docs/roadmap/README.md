# Roadmap

## Current Milestone (Completed) 🚀

- [x] Initial Scaffolding & System Architecture
- [x] Data Mocking & PostgreSQL DB setup
- [x] Metric Layer (dbt) implementation & Data Quality Tests
- [x] A/B Testing template (Jupyter) with actual statistical significance
- [x] Documentation of Architecture (Mermaid), KPIs, and Executive Memo
- [x] Metabase Integration

## Future Goals (Backlog)

- Implement automated orchestration (e.g., Apache Airflow, Mage, or Dagster) for scheduling the dbt pipelines.
- Add advanced regression testing on experiment datasets (e.g., CUPED for variance reduction).
- Persist Metabase dashboard configurations as code using Metabase Serialization or Terraform.
- Move from local PostgreSQL to a cloud data warehouse (e.g., Snowflake, BigQuery) if scaling is required.
