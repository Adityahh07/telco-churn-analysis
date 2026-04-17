"""
app.py — Telco Customer Churn Predictor
========================================
Streamlit web app that predicts customer churn probability
using the trained Logistic Regression model.

Run:
    streamlit run app.py
"""

import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os

# ── Page config ───────────────────────────────────────────────
st.set_page_config(
    page_title='Telco Churn Predictor',
    page_icon='📉',
    layout='wide',
    initial_sidebar_state='expanded'
)

# ── Custom CSS ────────────────────────────────────────────────
st.markdown("""
<style>
    .main-title   { font-size:2rem; font-weight:700; color:#1A1A2E; }
    .sub-title    { font-size:1rem; color:#6C757D; margin-bottom:1.5rem; }
    .risk-high    { background:#E84855; color:white; padding:16px 24px;
                    border-radius:10px; text-align:center; font-size:1.4rem;
                    font-weight:700; }
    .risk-medium  { background:#F4A261; color:white; padding:16px 24px;
                    border-radius:10px; text-align:center; font-size:1.4rem;
                    font-weight:700; }
    .risk-low     { background:#2E86AB; color:white; padding:16px 24px;
                    border-radius:10px; text-align:center; font-size:1.4rem;
                    font-weight:700; }
    .metric-card  { background:#F8F9FA; border:1px solid #DEE2E6;
                    border-radius:8px; padding:16px; text-align:center; }
    .metric-val   { font-size:1.8rem; font-weight:700; color:#1A1A2E; }
    .metric-label { font-size:0.85rem; color:#6C757D; }
    .insight-box  { background:#EBF5FB; border-left:4px solid #2E86AB;
                    padding:12px 16px; border-radius:4px;
                    font-size:0.9rem; color:#1A1A2E; }
</style>
""", unsafe_allow_html=True)


# ── Load model ────────────────────────────────────────────────
@st.cache_resource
def load_model():
    model_path = 'model/churn_model.pkl'
    if not os.path.exists(model_path):
        st.error('Model not found. Run `python train_model.py` first.')
        st.stop()
    with open(model_path, 'rb') as f:
        return pickle.load(f)

artifact = load_model()
pipeline  = artifact['pipeline']
threshold = artifact['threshold']
col_vals  = artifact['col_unique_values']
avg_charge = artifact['avg_monthly_charge']


# ── Header ────────────────────────────────────────────────────
st.markdown('<div class="main-title">📉 Telco Customer Churn Predictor</div>',
            unsafe_allow_html=True)
st.markdown(
    '<div class="sub-title">Enter customer details to predict churn probability '
    'and estimated revenue at risk.</div>',
    unsafe_allow_html=True
)
st.markdown('---')


# ── Sidebar — Customer Input ───────────────────────────────────
st.sidebar.header('Customer Profile')
st.sidebar.markdown('Fill in the customer details below.')

def sidebar_select(label, col):
    options = col_vals.get(col, ['No', 'Yes'])
    return st.sidebar.selectbox(label, options)

def sidebar_slider(label, col, min_val, max_val, default, step=1, fmt=None):
    return st.sidebar.slider(label, min_val, max_val, default, step)

st.sidebar.subheader('Demographics')
gender          = sidebar_select('Gender',          'gender')
senior          = sidebar_select('Senior Citizen',  'SeniorCitizen')
partner         = sidebar_select('Has Partner',     'Partner')
dependents      = sidebar_select('Has Dependents',  'Dependents')

st.sidebar.subheader('Account')
tenure          = sidebar_slider('Tenure (months)', 'tenure', 0, 72, 12)
contract        = sidebar_select('Contract Type',   'Contract')
paperless       = sidebar_select('Paperless Billing', 'PaperlessBilling')
payment         = sidebar_select('Payment Method',  'PaymentMethod')
monthly_charge  = st.sidebar.slider('Monthly Charges ($)', 18.0, 119.0, 65.0, 0.5)

# Total charges — calculated from tenure × monthly as a reasonable estimate
# User can override
total_charges   = st.sidebar.number_input(
    'Total Charges ($)',
    min_value=0.0,
    max_value=9000.0,
    value=float(round(tenure * monthly_charge, 2)),
    step=1.0
)

st.sidebar.subheader('Phone Service')
phone_service   = sidebar_select('Phone Service',   'PhoneService')
multiple_lines  = sidebar_select('Multiple Lines',  'MultipleLines')

st.sidebar.subheader('Internet Service')
internet        = sidebar_select('Internet Service', 'InternetService')

# Add-ons — only relevant if customer has internet
addon_disabled = (internet == 'No')
addon_label    = ' (N/A — no internet)' if addon_disabled else ''

online_security  = st.sidebar.selectbox(
    f'Online Security{addon_label}',
    ['No internet service'] if addon_disabled else col_vals.get('OnlineSecurity', ['No','Yes'])
)
online_backup    = st.sidebar.selectbox(
    f'Online Backup{addon_label}',
    ['No internet service'] if addon_disabled else col_vals.get('OnlineBackup', ['No','Yes'])
)
device_protection = st.sidebar.selectbox(
    f'Device Protection{addon_label}',
    ['No internet service'] if addon_disabled else col_vals.get('DeviceProtection', ['No','Yes'])
)
tech_support     = st.sidebar.selectbox(
    f'Tech Support{addon_label}',
    ['No internet service'] if addon_disabled else col_vals.get('TechSupport', ['No','Yes'])
)
streaming_tv     = st.sidebar.selectbox(
    f'Streaming TV{addon_label}',
    ['No internet service'] if addon_disabled else col_vals.get('StreamingTV', ['No','Yes'])
)
streaming_movies = st.sidebar.selectbox(
    f'Streaming Movies{addon_label}',
    ['No internet service'] if addon_disabled else col_vals.get('StreamingMovies', ['No','Yes'])
)

st.sidebar.markdown('---')
predict_btn = st.sidebar.button('Predict Churn Risk', type='primary',
                                  use_container_width=True)


# ── Build input DataFrame ─────────────────────────────────────
input_data = pd.DataFrame([{
    'gender'           : gender,
    'SeniorCitizen'    : senior,
    'Partner'          : partner,
    'Dependents'       : dependents,
    'tenure'           : tenure,
    'PhoneService'     : phone_service,
    'MultipleLines'    : multiple_lines,
    'InternetService'  : internet,
    'OnlineSecurity'   : online_security,
    'OnlineBackup'     : online_backup,
    'DeviceProtection' : device_protection,
    'TechSupport'      : tech_support,
    'StreamingTV'      : streaming_tv,
    'StreamingMovies'  : streaming_movies,
    'Contract'         : contract,
    'PaperlessBilling' : paperless,
    'PaymentMethod'    : payment,
    'MonthlyCharges'   : monthly_charge,
    'TotalCharges'     : total_charges,
}])


# ── Prediction ────────────────────────────────────────────────
churn_proba    = pipeline.predict_proba(input_data)[0][1]
churn_pred     = int(churn_proba >= threshold)

# Risk level
if churn_proba >= 0.6:
    risk_level = 'High Risk'
    risk_class = 'risk-high'
    risk_emoji = '🔴'
elif churn_proba >= 0.35:
    risk_level = 'Medium Risk'
    risk_class = 'risk-medium'
    risk_emoji = '🟠'
else:
    risk_level = 'Low Risk'
    risk_class = 'risk-low'
    risk_emoji = '🟢'

# Revenue at risk for this customer
annual_rev_at_risk = monthly_charge * 12


# ── Main Output ───────────────────────────────────────────────
if predict_btn or True:   # Always show output

    col1, col2, col3 = st.columns([1.2, 1, 1])

    # ── Churn probability gauge ───────────────────────────────
    with col1:
        st.markdown('### Churn Probability')
        st.markdown(
            f'<div class="{risk_class}">'
            f'{risk_emoji} {churn_proba*100:.1f}% — {risk_level}'
            f'</div>',
            unsafe_allow_html=True
        )
        st.markdown('')

        # Progress bar
        st.progress(churn_proba)
        st.caption(f'Recommended action threshold: {threshold*100:.0f}%  '
                   f'→  {"⚠ Flag for outreach" if churn_pred else "✅ No action needed"}')

    # ── Revenue impact ────────────────────────────────────────
    with col2:
        st.markdown('### Revenue at Risk')
        st.markdown(
            f'<div class="metric-card">'
            f'<div class="metric-val">${monthly_charge:,.2f}</div>'
            f'<div class="metric-label">Monthly Revenue</div>'
            f'</div>',
            unsafe_allow_html=True
        )
        st.markdown('')
        st.markdown(
            f'<div class="metric-card">'
            f'<div class="metric-val">${annual_rev_at_risk:,.0f}</div>'
            f'<div class="metric-label">Annual Revenue at Risk</div>'
            f'</div>',
            unsafe_allow_html=True
        )

    # ── Key risk factors ──────────────────────────────────────
    with col3:
        st.markdown('### Key Risk Factors')

        risk_factors = []
        if contract == 'Month-to-month':
            risk_factors.append('🔴 Month-to-month contract (15× more likely to churn)')
        if tenure <= 12:
            risk_factors.append(f'🔴 Early-stage customer ({tenure} months — danger zone)')
        if internet == 'Fiber optic':
            risk_factors.append('🟠 Fiber optic internet (41.9% segment churn rate)')
        if payment == 'Electronic check':
            risk_factors.append('🟠 Electronic check payment (45.3% churn rate)')
        if online_security == 'No':
            risk_factors.append('🟠 No OnlineSecurity (41.8% vs 14.6% with)')
        if tech_support == 'No':
            risk_factors.append('🟠 No TechSupport (41.6% vs 15.2% with)')
        if senior == 'Yes':
            risk_factors.append('🟡 Senior citizen (41.7% churn rate)')
        if monthly_charge > 74.44:
            risk_factors.append(f'🟡 Above-avg monthly charge (${monthly_charge:.2f})')

        positive_factors = []
        if contract == 'Two year':
            positive_factors.append('✅ Two-year contract (only 2.8% churn rate)')
        if tenure > 48:
            positive_factors.append(f'✅ Long-tenure customer ({tenure} months)')
        if online_security == 'Yes':
            positive_factors.append('✅ Has OnlineSecurity')
        if tech_support == 'Yes':
            positive_factors.append('✅ Has TechSupport')
        if payment in ['Bank transfer (automatic)', 'Credit card (automatic)']:
            positive_factors.append('✅ Auto-pay customer (low churn signal)')

        if risk_factors:
            for f in risk_factors:
                st.markdown(f'- {f}')
        if positive_factors:
            st.markdown('**Retention signals:**')
            for f in positive_factors:
                st.markdown(f'- {f}')
        if not risk_factors and not positive_factors:
            st.markdown('No strong risk or retention signals detected.')

    st.markdown('---')

    # ── Recommendation box ────────────────────────────────────
    st.markdown('### Recommended Action')

    if churn_pred == 1:
        action_text = (
            f'This customer is flagged for proactive retention outreach. '
            f'Churn probability is <b>{churn_proba*100:.1f}%</b> — '
            f'above the recommended intervention threshold of {threshold*100:.0f}%. '
        )
        if contract == 'Month-to-month' and tenure <= 12:
            action_text += (
                'Priority action: offer a contract upgrade incentive — '
                'one month free for switching to an annual plan. '
                'This customer is in the highest-risk profile (new + M2M).'
            )
        elif internet == 'Fiber optic' and (online_security == 'No' or tech_support == 'No'):
            action_text += (
                'Priority action: bundle OnlineSecurity and TechSupport free '
                'for 3 months. Fiber + no add-ons is a high-risk combination.'
            )
        elif payment == 'Electronic check':
            action_text += (
                'Priority action: offer a $5/month discount for switching to '
                'auto-pay. Electronic check payers churn at 3× the auto-pay rate.'
            )
        else:
            action_text += (
                'Contact the customer with a personalised retention offer '
                'addressing their specific risk factors above.'
            )
        st.markdown(
            f'<div class="insight-box" style="border-color:#E84855;">'
            f'⚠ <b>Intervention Recommended</b><br>{action_text}'
            f'</div>',
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f'<div class="insight-box">'
            f'✅ <b>No Immediate Action Required</b><br>'
            f'Churn probability is {churn_proba*100:.1f}% — below the '
            f'{threshold*100:.0f}% intervention threshold. '
            f'Continue standard engagement.'
            f'</div>',
            unsafe_allow_html=True
        )

    st.markdown('---')

    # ── Model info footer ─────────────────────────────────────
    with st.expander('Model Information'):
        col_a, col_b, col_c, col_d = st.columns(4)
        col_a.metric('Model',         'Logistic Regression')
        col_b.metric('ROC-AUC',       '0.8417')
        col_c.metric('Recall @0.3',   '92.8%')
        col_d.metric('Threshold',     f'{threshold}')
        st.caption(
            'Trained on 7,043 telecom customers. '
            'Recall of 92.8% at threshold 0.3 means the model correctly '
            'identifies 93% of actual churners. '
            'Performance validated via 5-fold cross-validation (mean AUC 0.84).'
        )

    # ── Raw input preview ─────────────────────────────────────
    with st.expander('Customer Input Summary'):
        st.dataframe(input_data.T.rename(columns={0: 'Value'}))
