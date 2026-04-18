CREATE DATABASE telco_churn_db;
USE telco_churn_db;

-- total rows loaded
SELECT COUNT(*) AS total_rows
FROM telco_churn;

-- Preview the first 5 rows
SELECT * FROM telco_churn
LIMIT 5;

-- Q1. Overall churn rate
SELECT
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    SUM(CASE WHEN Churn = 'No'  THEN 1 ELSE 0 END) AS retained_customers,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)/ COUNT(*) * 100, 2
    ) AS churn_rate_pct
FROM telco_churn;

-- Q2. Average tenure and monthly charges — churned vs retained
SELECT
    Churn,
    COUNT(*) AS customer_count,
    ROUND(AVG(tenure), 2) AS avg_tenure_months,
    ROUND(AVG(MonthlyCharges), 2) AS avg_monthly_charges,
    ROUND(AVG(TotalCharges), 2) AS avg_total_charges
FROM telco_churn
GROUP BY Churn;

-- Q3. Churn rate by contract type
SELECT
    Contract,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned,
    SUM(CASE WHEN Churn = 'No'  THEN 1 ELSE 0 END) AS retained,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)/ COUNT(*) * 100, 2
    ) AS churn_rate_pct
FROM telco_churn
GROUP BY Contract
ORDER BY churn_rate_pct DESC;

-- Q4. Monthly and annual revenue lost by contract type
SELECT
    Contract,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS customers_lost,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN MonthlyCharges ELSE 0 END), 2)                                                    AS monthly_revenue_lost,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN MonthlyCharges ELSE 0 END) * 12
    , 2) AS annual_revenue_lost
FROM telco_churn
GROUP BY Contract
ORDER BY monthly_revenue_lost DESC;

-- Q5. Churn rate by tenure group
SELECT
    tenure_group,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)/ COUNT(*) * 100, 2
    ) AS churn_rate_pct
FROM telco_churn
GROUP BY tenure_group
ORDER BY
    CASE tenure_group
        WHEN '0-12 Months'  THEN 1
        WHEN '13-24 Months' THEN 2
        WHEN '25-48 Months' THEN 3
        WHEN '49-72 Months' THEN 4
    END;
    
-- Q6. Total revenue at risk — monthly and annual
SELECT
    ROUND(SUM(MonthlyCharges), 2) AS total_monthly_revenue,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN MonthlyCharges ELSE 0 END)
    , 2) AS monthly_revenue_lost,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN MonthlyCharges ELSE 0 END) * 12
    , 2) AS annual_revenue_lost,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN MonthlyCharges ELSE 0 END)/ SUM(MonthlyCharges) * 100, 2
    ) AS pct_revenue_at_risk
FROM telco_churn;

-- Q7. Churn rate by internet service type
SELECT
    InternetService,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)/ COUNT(*) * 100, 2
    ) AS churn_rate_pct,
    ROUND(AVG(MonthlyCharges), 2) AS avg_monthly_charge
FROM telco_churn
GROUP BY InternetService
ORDER BY churn_rate_pct DESC;

-- Q8. Churn rate by payment method
SELECT
    PaymentMethod,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)/ COUNT(*) * 100, 2
    ) AS churn_rate_pct
FROM telco_churn
GROUP BY PaymentMethod
ORDER BY churn_rate_pct DESC;

-- Q9. Add-on services impact on churn
-- UNION ALL combines OnlineSecurity and TechSupport into one result
-- Filtered to internet customers only — add-ons require internet
SELECT
    'OnlineSecurity' AS addon_service,
    OnlineSecurity AS has_addon,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)/ COUNT(*) 
    * 100, 2) AS churn_rate_pct
FROM telco_churn
WHERE InternetService != 'No'
  AND OnlineSecurity IN ('Yes', 'No')
GROUP BY OnlineSecurity

UNION ALL

SELECT
    'TechSupport',
    TechSupport,
    COUNT(*),
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END),
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)/ COUNT(*) * 100, 2)
FROM telco_churn
WHERE InternetService != 'No'
  AND TechSupport IN ('Yes', 'No')
GROUP BY TechSupport
ORDER BY addon_service, has_addon DESC;

-- Q10. Highest-risk customer segment
SELECT
    COUNT(*) AS segment_size,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS already_churned,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)/ COUNT(*) * 100, 2
    ) AS churn_rate_pct,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN MonthlyCharges ELSE 0 END)
    , 2) AS monthly_revenue_lost
FROM telco_churn
WHERE Contract        = 'Month-to-month'
  AND InternetService = 'Fiber optic'
  AND PaymentMethod   = 'Electronic check'
  AND tenure         <= 12;

-- Q11. High-value customers at risk — uses a subquery
SELECT
    COUNT(*) AS customer_count,
    ROUND(AVG(MonthlyCharges), 2) AS avg_charge_in_segment,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)/ COUNT(*) * 100, 2
    ) AS churn_rate_pct
FROM telco_churn
WHERE MonthlyCharges > (SELECT AVG(MonthlyCharges) FROM telco_churn)
  AND Contract = 'Month-to-month';
  
-- Q12. Percentage of total churn contributed by each contract type
SELECT
    Contract,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        / SUM(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)) OVER () * 100
    , 2) AS pct_of_total_churn
FROM telco_churn
GROUP BY Contract
ORDER BY churned_customers DESC;
