# Telco Customer Churn Analysis

End-to-end data analytics and machine learning project identifying **$1.67M in annualised revenue at risk** across 7,043 telecom customers.

**Tools:** Python · MySQL · Power BI · Scikit-learn · XGBoost

---

## Dashboard Preview

![Dashboard](dashboard/dashboard_preview.png)

> 🔗 **[View Live Dashboard](YOUR_POWER_BI_LINK_HERE)** ← replace with your Power BI Service link after publishing

---

## Business Problem

A telecom company is losing **26.54% of its customers every year** — roughly 1 in 4. That translates to **$139,131 in monthly revenue lost** and **$1.67 million annualised**. The business had no visibility into who was churning, why, or when. This project answers all three questions and builds a model to predict which customers are next.

---

## Key Findings

| # | Finding | Impact |
|---|---|---|
| 1 | Month-to-month customers churn at **42.7%** vs 2.8% for two-year — a **15x gap** | Drives 86.9% of all revenue loss |
| 2 | **47.4% of new customers** leave within their first 12 months | Median churn at just 10 months |
| 3 | Churned customers pay **$13 more/month** than retained ones | Value problem, not pricing |
| 4 | Fiber optic — the premium product — has the **highest churn at 41.9%** | 82% of revenue at risk |
| 5 | No OnlineSecurity: **41.8% churn** → With it: **14.6%** | Add-ons triple retention |
| 6 | Electronic check payers churn at **45.3%** vs 15.2% for auto-pay | 3x higher risk |

**Highest-risk segment:** Month-to-month + Fiber optic + Electronic check + Tenure ≤ 12 months → **631 customers, 71.2% churn rate, $37,166/month lost**.

---

## Business Recommendations

1. **Contract upgrade campaign** — Offer 1 month free to 3,875 M2M customers who switch to annual. Addresses 86.9% of all revenue loss.
2. **Bundle add-ons free for 90 days** — OnlineSecurity + TechSupport free for new fiber optic customers.
3. **Auto-pay incentive** — $5/month discount for switching from electronic check. Retaining one customer pays back that discount 15x in a year.

---

## ML Model Results

| Model | Recall | ROC-AUC |
|---|---|---|
| **Logistic Regression** | **78.3%** | **0.8417** ← recommended |
| Random Forest | 73.5% | 0.8408 |
| XGBoost | 77.0% | 0.8410 |

At threshold **0.3**: catches **93% of actual churners** → estimated net annual benefit **$44,628**. Validated via 5-fold cross-validation (mean AUC 0.84).

---

## Project Architecture

```
Raw Data (7,043 customers · 21 columns)
        │
        ▼
01_data_cleaning.ipynb
Fix TotalCharges · engineer tenure_group · binary encoding
        │
        ▼
02_EDA.ipynb
9 business charts · 6 hypotheses validated
        │
        ├─────────────────────────────┐
        ▼                             ▼
SQL — 12 MySQL queries          Power BI Dashboard
Window functions · subqueries   KPIs · 5 charts · 3 slicers
        │                             │
        └──────────────┬──────────────┘
                       ▼
           03_ml_modeling.ipynb
           LR · Random Forest · XGBoost · SMOTE
                       │
                       ▼
           04_model_evaluation.ipynb
           ROC curve · confusion matrix · threshold tuning · revenue impact
```

---

## Project Structure

```
telco-churn-analysis/
├── data/
│   ├── WA_Fn-UseC_-Telco-Customer-Churn.csv
│   └── telco_churn_cleaned.csv
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_EDA.ipynb
│   ├── 03_ml_modeling.ipynb
│   └── 04_model_evaluation.ipynb
├── sql/
│   └── telco_churn_queries.sql
├── dashboard/
│   ├── telco_churn_dashboard.pbix
│   └── dashboard_preview.png
├── PROBLEM_STATEMENT.pdf
├── requirements.txt
├── .gitignore
└── README.md
```

---

## How to Run

```bash
pip install -r requirements.txt
jupyter notebook
# Run notebooks in order: 01 → 02 → 03 → 04
```

---

## Key Learnings & Challenges

**1. Data quality decisions need business context.**
TotalCharges had 11 blank rows. Standard approach: drop them. Correct approach: impute 0 — they were new customers never billed yet. Dropping would silently remove valid data.

**2. Class imbalance silently breaks models.**
Without handling the 2.77:1 imbalance, the model hit 81% accuracy but only 56% recall — missing nearly half of all churners. `class_weight='balanced'` improved recall by 22.5 percentage points. Accuracy is misleading for imbalanced problems.

**3. Threshold matters more than model choice.**
Lowering the decision threshold from 0.5 to 0.3 increased recall from 78% to 93%. For churn — where missing a churner costs far more than an unnecessary outreach call — this single tuning decision had more practical impact than choosing between LR, RF, and XGBoost.

**4. Feature importance validates EDA.**
The ML model's top features (tenure, contract type, fiber optic, electronic check) matched the EDA findings exactly. When two independent methods point to the same patterns, the signals are confirmed as real.

---

## Dataset

IBM Watson Analytics Telco Customer Churn · [Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) · 7,043 rows · 21 columns · 26.54% churn rate

---

**Aditya H H** · BCA Graduate · Aspiring Data Analyst & Data Scientist · Bangalore, India  
[LinkedIn](https://linkedin.com/in/aditya-h-h-3a12b9242) · [GitHub](https://github.com/Adityahh07)
