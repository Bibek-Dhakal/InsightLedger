# Architecture

The system leverages standard OSS tools for data operations, running entirely within a local Dockerized environment and
utilizing Python for data generation and statistical testing.

## System Data Flow

```mermaid
graph TD
subgraph "1. Ingestion"
A[scripts/init_db.py\n(Mock Data Generator)] -->|psycopg2 writes|B[(PostgreSQL\nRaw Schema)]
end

subgraph "2. Transformation (dbt)"
B -->|Reads Raw Data| C(Staging Models\nViews)
C -->|Transforms & Joins|D(Marts / Fact Tables\nMaterialized Tables)
D -.->|Automated Data Tests|D
end

subgraph "3. Serving & Analysis"
D -->|Reads Clean Data|E[Metabase\nBI Dashboard]
B -->|Reads Experiment Data|F[Jupyter Notebook\nA/B Test Analysis]
end
```

## Components

1. **PostgreSQL (Container)**: Analytical data store serving as the central warehouse. Holds raw mock data in the
   `public` schema and transformed models.
2. **dbt-postgres (Local Python)**: Handles data modeling, staging, transformation, and automated reconciliation tests
   (`schema.yml`).
3. **Jupyter Notebooks (Local Python)**: Statistical analysis environment executing rigorous A/B testing, SRM checks,
   and Confidence Intervals using `scipy` and `statsmodels`.
4. **Metabase (Container)**: Provides the self-serve BI layer. Connects directly to the PostgreSQL instance to provide
   visual access to `marts` models like `fct_daily_kpis`.
