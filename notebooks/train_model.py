"""
train_model.py
==============
Trains the Logistic Regression churn prediction model and saves it
as a pickle file for use by the Streamlit app.

Run this once before launching the app:
    python train_model.py

Output: model/churn_model.pkl
"""

import pandas as pd
import numpy as np
import pickle
import os
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, recall_score

# ── Config ────────────────────────────────────────────────────
DATA_PATH  = '../data/telco_churn_cleaned.csv'
MODEL_DIR  = 'model'
MODEL_PATH = f'{MODEL_DIR}/churn_model.pkl'

# ── Load data ─────────────────────────────────────────────────
print('Loading data...')
df = pd.read_csv(DATA_PATH)

drop_cols = [
    'customerID', 'Churn', 'Churn_enc', 'tenure_group',
    'SeniorCitizen_enc', 'Partner_enc', 'Dependents_enc',
    'PhoneService_enc', 'PaperlessBilling_enc'
]
X = df.drop(columns=drop_cols)
y = df['Churn_enc']

# ── Column types ──────────────────────────────────────────────
num_cols = ['tenure', 'MonthlyCharges', 'TotalCharges']
cat_cols = [c for c in X.columns if c not in num_cols]

# ── Preprocessing pipeline ────────────────────────────────────
preprocessor = ColumnTransformer(transformers=[
    ('num', StandardScaler(), num_cols),
    ('cat', OneHotEncoder(drop='first', handle_unknown='ignore',
                          sparse_output=False), cat_cols)
])

# ── Model pipeline ────────────────────────────────────────────
model_pipeline = Pipeline([
    ('pre', preprocessor),
    ('clf', LogisticRegression(
        class_weight='balanced',
        max_iter=1000,
        random_state=42
    ))
])

# ── Train on full dataset ─────────────────────────────────────
# We train on the full dataset for deployment — maximising the data
# available to the model. Performance was validated on the test split
# in Notebook 04 (ROC-AUC 0.8417, Recall 78% at threshold 0.5,
# Recall 93% at recommended threshold 0.3).
print('Training model on full dataset...')
model_pipeline.fit(X, y)

# ── Validate ──────────────────────────────────────────────────
# Quick sanity check on a holdout split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)
model_pipeline_check = Pipeline([
    ('pre', preprocessor),
    ('clf', LogisticRegression(class_weight='balanced',
                                max_iter=1000, random_state=42))
])
model_pipeline_check.fit(X_train, y_train)
proba = model_pipeline_check.predict_proba(X_test)[:,1]
auc   = roc_auc_score(y_test, proba)
rec   = recall_score(y_test, (proba >= 0.3).astype(int))
print(f'Validation AUC          : {auc:.4f}')
print(f'Validation Recall @0.3  : {rec*100:.1f}%')

# ── Save model + metadata ─────────────────────────────────────
os.makedirs(MODEL_DIR, exist_ok=True)

model_artifact = {
    'pipeline'          : model_pipeline,
    'feature_columns'   : list(X.columns),
    'num_cols'          : num_cols,
    'cat_cols'          : cat_cols,
    'threshold'         : 0.3,
    'train_churn_rate'  : float(y.mean()),
    'avg_monthly_charge': float(df[df['Churn']=='Yes']['MonthlyCharges'].mean()),
    'annual_rev_at_risk': float(df[df['Churn']=='Yes']['MonthlyCharges'].sum() * 12),
    'col_unique_values' : {col: sorted(df[col].dropna().unique().tolist())
                           for col in cat_cols},
}

with open(MODEL_PATH, 'wb') as f:
    pickle.dump(model_artifact, f)

print(f'\nModel saved to: {MODEL_PATH}')
print('Ready to run: streamlit run app.py')
