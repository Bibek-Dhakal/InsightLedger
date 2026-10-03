# Usage & Operations Guide

## Getting Started

1. **Copy Environment Variables:**
   ```bash
   cp .env.example .env
   ```

2. **Start Infrastructure (PostgreSQL & Metabase):**
   ```bash
   docker-compose up -d
   ```

3. **Install Dependencies & Seed Data:**
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -e .[dev]
   python scripts/init_db.py
   ```

4. **Run dbt Models:**
   ```bash
   cd dbt_project
   dbt deps
   dbt build --profiles-dir .
   ```

5. **Access BI (Metabase):**
   Open `http://localhost:3000` in your browser. Complete the initial admin account setup.
   When asked to "Add your data", select **PostgreSQL** and enter the following details:
    - **Display name:** `InsightLedger` (or your preference)
    - **Host:** `postgres` *(Note: use the Docker service name `postgres`, not `localhost`)*
    - **Port:** `5432`
    - **Database name:** `insightledger`
    - **Username:** `admin`
    - **Password:** `password`

   Click **Save**. You can now query your curated dbt models (e.g., `fct_daily_kpis`) to build your dashboards.

---
