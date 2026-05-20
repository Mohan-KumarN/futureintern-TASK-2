# Customer Retention & Churn Analysis (Task 2)

## Overview
This project analyzes churn patterns and retention drivers for a subscription-based business. It includes:
- Synthetic dataset generation for **2,000 customers**
- Churn/retention analysis via Python
- Visualizations saved in the `assets/` folder
- A markdown report with actionable recommendations
- Power BI build instructions (from `task details.txt`)

## Project Structure
- `generate_churn_data.py` — Generates `customer_churn_data.csv`
- `analyze_churn.py` — Computes churn statistics and saves charts to `assets/`
- `customer_churn_data.csv` — Input dataset for analysis
- `Retention_Analysis_Report.md` — Insights & recommendations
- `assets/` — Output images
  - `churn_by_plan.png`
  - `churn_reasons.png`
  - `support_vs_churn.png`
  - `clv_by_plan.png`
  - `cohort_signups.png`

## Setup / Requirements
- Python 3.x
- Python packages:
  - pandas
  - numpy
  - matplotlib
  - seaborn

Install (example):
```bash
pip install pandas numpy matplotlib seaborn
```

## How to Run
### 1) (Optional) Regenerate the dataset
```bash
python generate_churn_data.py
```
This creates/overwrites `customer_churn_data.csv`.

### 2) Run the analysis and generate charts
```bash
python analyze_churn.py
```
Outputs:
- Console churn summary stats
- Charts saved to `assets/`

## Visual Outputs
`analyze_churn.py` generates:
- `assets/churn_reasons.png`
- `assets/churn_by_plan.png`
- `assets/support_vs_churn.png`
- `assets/clv_by_plan.png`
- `assets/cohort_signups.png`

## Power BI
For dashboard build steps, see:
- `task details.txt`

