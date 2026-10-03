# KPI Dictionary

All metrics visualized in the dashboard correspond exactly to models maintained in `dbt`.

| KPI Name | Grain | Filters | Formula | Owner | Table Reference |
|----------|-------|---------|---------|-------|-----------------|
| **Purchasing Users** | Daily | `status = 'completed'` | `COUNT(DISTINCT user_id)` | Data Team | `fct_daily_kpis` |
| **Total Orders** | Daily | `status = 'completed'` | `COUNT(DISTINCT order_id)` | Data Team | `fct_daily_kpis` |
| **Total Revenue** | Daily | `status = 'completed'` | `SUM(amount)` | Finance | `fct_daily_kpis` |

*Reconciliation Note:* Totals reconcile exactly with source database totals. `dbt` tests automatically fail the pipeline
if nulls or duplicates appear in daily grains.
