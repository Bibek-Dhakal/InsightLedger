# InsightLedger

Decision-support analytics: governed KPI definitions, reconciled data, self-serve dashboards, and statistically sound
experiment analysis with quantified uncertainty.

> 🏆 **Check out the [v0.1.0 Release Notes](./docs/releases/v0.1.0.md)** for a full visual walkthrough, including
> architecture diagrams, dbt test runs, mathematical A/B test proofs, and BI dashboard screenshots!

## 🚀 Project Status: End-to-End Complete

This project successfully implements a full modern data stack running locally via Docker. It demonstrates the ability to
ingest data, apply governed transformations with automated testing, visualize KPIs, and conduct rigorous statistical
analysis on experiments.

## 🎯 Problem Solved

Traditional setups often lack consistent KPI definitions, resulting in stakeholders disagreeing on numbers. A/B testing
is frequently reported without robust checks (like Sample Ratio Mismatch or Confidence Intervals). InsightLedger closes
this gap by providing a verified, tested data layer combined with rigorous statistical analysis.

## ⚙️ Core Features

- **Governed KPIs:** Explicit grain, filters, and calculations managed via `dbt`.
- **Reconciled Data:** Automated data tests ensuring totals match the source and primary keys are unique.
- **Self-Serve Dashboard:** Easily ingestible by Metabase for parameterized reporting.
- **Rigorous Experiment Analysis:** Jupyter notebooks evaluating A/B tests handling validity checks (SRM), power, and
  confidence intervals.

## 🛠️ Tech Stack

- **Data Source:** PostgreSQL (local container)
- **Transformations & Testing:** `dbt-postgres`
- **Analytics & BI:** Metabase
- **Statistical Analysis:** Python (`pandas`, `scipy`, `statsmodels`, Jupyter)
- **CI/CD & Code Quality:** GitHub Actions, Pre-commit, Release-Please

## 📚 Documentation

Please refer to the following documentation sections:

- [Usage & Getting Started](docs/usage/README.md)
- [Architecture & Data Flow](docs/architecture/README.md)
- [KPI Dictionary](docs/kpi_dictionary.md)
- [Testing Strategy](docs/testing/README.md)
- [Recommendation Memo (A/B Test Results)](docs/recommendation_memo.md)
- [Project Roadmap](docs/roadmap/README.md)
