# InsightLedger

Decision-support analytics: governed KPI definitions, reconciled data, self-serve dashboards, and statistically sound
experiment analysis with quantified uncertainty.

## Problem Solved

Traditional setups often lack consistent KPI definitions, resulting in stakeholders disagreeing on numbers. A/B testing
is frequently reported without robust checks (like Sample Ratio Mismatch or Confidence Intervals). InsightLedger closes
this gap by providing a verified, tested data layer combined with rigorous statistical analysis.

## Core Features

- **Governed KPIs:** Explicit grain, filters, and calculations managed via `dbt`.
- **Reconciled Data:** Automated data tests ensuring totals match the source.
- **Self-Serve Dashboard:** Easily ingestible by Metabase for parameterized reporting.
- **Rigorous Experiment Analysis:** Jupyter notebooks evaluating A/B tests handling validity checks, power, and
  confidence intervals.

## Stack

- **Data Source:** PostgreSQL (local container)
- **Transformations & Testing:** `dbt-postgres`
- **Analytics & BI:** Metabase
- **Statistical Analysis:** Python (`pandas`, `scipy`, `statsmodels`, Jupyter)
- **CI/CD & Code Quality:** GitHub Actions, Pre-commit, Release-Please

## Documentation

Please refer to the following documentation sections:

- [Usage & Getting Started](docs/usage/README.md)
- [KPI Dictionary](docs/kpi_dictionary.md)
- [Architecture](docs/architecture/README.md)
- [Testing Strategy](docs/testing/README.md)
- [Recommendation Memo](docs/recommendation_memo.md)
