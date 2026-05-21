import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="Real Estate AI",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================
# API URL
# =========================================

API_URL = "https://real-estate-price-prediction-system-9nka.onrender.com/predict"

# =========================================
# CUSTOM CSS
# =========================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

/* =========================================
GLOBAL
========================================= */

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
    color: #e2e8f0;
}

body {
    background: #020617;
}

/* MAIN APP */

.main {
    background:
        radial-gradient(circle at top left, rgba(37,99,235,0.15), transparent 30%),
        radial-gradient(circle at bottom right, rgba(6,182,212,0.10), transparent 30%),
        linear-gradient(135deg, #020617, #0f172a, #111827);
    color: #e2e8f0;
}

/* CONTENT WIDTH */

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 1300px;
}

/* =========================================
HEADINGS
========================================= */

h1 {
    color: #dbeafe !important;
    font-weight: 700 !important;
}

h2 {
    color: #bfdbfe !important;
    font-weight: 600 !important;
}

h3 {
    color: #94a3b8 !important;
    font-weight: 500 !important;
}

p, li, label, span {
    color: #cbd5e1 !important;
}

/* =========================================
HERO SECTION
========================================= */

.hero-card {
    background:
        linear-gradient(
            135deg,
            rgba(15,23,42,0.96),
            rgba(30,41,59,0.92)
        );

    border: 1px solid rgba(148,163,184,0.12);

    padding: 40px;

    border-radius: 28px;

    backdrop-filter: blur(18px);

    box-shadow:
        0 10px 40px rgba(0,0,0,0.45),
        0 0 0 1px rgba(255,255,255,0.02);
}

/* HERO TEXT */

.hero-card h1 {
    color: #93c5fd !important;
    letter-spacing: -1px;
}

.hero-card h3 {
    color: #94a3b8 !important;
}

.hero-card p,
.hero-card li {
    color: #cbd5e1 !important;
}

/* =========================================
METRIC CARDS
========================================= */

.metric-card {
    background: rgba(15,23,42,0.82);

    border: 1px solid rgba(148,163,184,0.10);

    border-radius: 24px;

    padding: 28px;

    text-align: center;

    backdrop-filter: blur(12px);

    transition: all 0.3s ease;

    box-shadow:
        0 6px 24px rgba(0,0,0,0.28);
}

.metric-card:hover {
    transform: translateY(-6px);

    border: 1px solid rgba(59,130,246,0.40);

    box-shadow:
        0 12px 30px rgba(37,99,235,0.15);
}

.metric-value {
    font-size: 34px;
    font-weight: 700;
    color: #38bdf8;
}

.metric-label {
    font-size: 14px;
    color: #94a3b8 !important;
    margin-top: 8px;
}

/* =========================================
INPUT SECTION
========================================= */

.input-card {
    background: rgba(15,23,42,0.80);

    padding: 35px;

    border-radius: 28px;

    border: 1px solid rgba(148,163,184,0.10);

    backdrop-filter: blur(14px);

    box-shadow:
        0 8px 30px rgba(0,0,0,0.30);
}

/* SLIDER LABELS */

.stSlider label,
.stSelectbox label {
    color: #cbd5e1 !important;
    font-weight: 500;
}

/* SLIDER VALUES */

.stSlider div[data-baseweb="slider"] {
    color: #e2e8f0 !important;
}

/* SELECTBOX */

.stSelectbox div[data-baseweb="select"] {
    background-color: #0f172a !important;
    color: #e2e8f0 !important;
}

/* =========================================
BUTTON
========================================= */

.stButton > button {

    width: 100%;

    background:
        linear-gradient(
            90deg,
            #2563eb,
            #0891b2
        );

    color: white !important;

    border-radius: 16px;

    height: 3.6em;

    border: none;

    font-size: 20px;

    font-weight: 600;

    transition: all 0.3s ease;

    box-shadow:
        0 8px 20px rgba(37,99,235,0.25);
}

.stButton > button:hover {

    transform: scale(1.02);

    background:
        linear-gradient(
            90deg,
            #1d4ed8,
            #0e7490
        );

    box-shadow:
        0 12px 28px rgba(37,99,235,0.35);
}

/* =========================================
SUCCESS CARD
========================================= */

.result-card {

    background:
        linear-gradient(
            135deg,
            rgba(16,185,129,0.12),
            rgba(6,182,212,0.08)
        );

    padding: 30px;

    border-radius: 24px;

    border: 1px solid rgba(16,185,129,0.18);

    box-shadow:
        0 8px 28px rgba(0,0,0,0.25);
}

.result-card h2 {
    color: #86efac !important;
}

/* =========================================
METRICS
========================================= */

[data-testid="metric-container"] {

    background: rgba(15,23,42,0.82);

    border: 1px solid rgba(148,163,184,0.10);

    padding: 20px;

    border-radius: 20px;

    box-shadow:
        0 6px 20px rgba(0,0,0,0.25);
}

[data-testid="metric-container"] label {
    color: #94a3b8 !important;
}

[data-testid="metric-container"] div {
    color: #f8fafc !important;
}

/* =========================================
INFO BOX
========================================= */

.stInfo {

    background: rgba(15,23,42,0.92) !important;

    border: 1px solid rgba(59,130,246,0.12) !important;

    border-radius: 20px !important;

    color: #e2e8f0 !important;
}

.stInfo h1 {
    color: #38bdf8 !important;
}

.stInfo h3 {
    color: #93c5fd !important;
}

.stInfo p,
.stInfo li {
    color: #cbd5e1 !important;
}

/* =========================================
SUCCESS / ERROR ALERTS
========================================= */

.stSuccess {
    background-color: rgba(16,185,129,0.15) !important;
    color: #86efac !important;
}

.stError {
    background-color: rgba(239,68,68,0.15) !important;
    color: #fca5a5 !important;
}

/* =========================================
FOOTER
========================================= */

.footer {

    text-align: center;

    margin-top: 45px;

    padding-top: 20px;

    color: #64748b !important;

    font-size: 15px;

    font-weight: 500;
}

.footer h3,
.footer h4 {
    color: #94a3b8 !important;
}

.footer p,
.footer span {
    color: #64748b !important;
}

</style>
""", unsafe_allow_html=True)

# =========================================
# HEADER
# =========================================

st.markdown("""
<div class="hero-card">

# 🏠 Real Estate Price Prediction AI

### 🚀 Production-Ready ML Powered Property Valuation Platform

Predict smart property valuations using:
- XGBoost Machine Learning
- FastAPI Backend
- Real-time AI Predictions
- Interactive Analytics Dashboard

</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =========================================
# METRICS SECTION
# =========================================

col1, col2, col3, col4 = st.columns(4)

metrics = [
    ("87%", "Model Accuracy"),
    ("FastAPI", "Backend API"),
    ("XGBoost", "ML Engine"),
    ("Live", "Deployment Status")
]

for col, (value, label) in zip([col1, col2, col3, col4], metrics):
    with col:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-value">{value}</div>
            <div class="metric-label">{label}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =========================================
# API HEALTH CHECK
# =========================================

try:
    health = requests.get(
        "https://real-estate-price-prediction-system-9nka.onrender.com/",
        timeout=5
    )

    if health.status_code == 200:
        st.success("🟢 Backend API Connected Successfully")

except:
    st.error("🔴 Backend API Offline")

# =========================================
# INPUT SECTION
# =========================================

st.markdown("## 📋 Property Information")

st.markdown('<div class="input-card">', unsafe_allow_html=True)

left, right = st.columns(2)

with left:

    area = st.slider(
        "📐 Area (sqft)",
        500,
        10000,
        2500
    )

    bedrooms = st.slider(
        "🛏 Bedrooms",
        1,
        10,
        3
    )

    bathrooms = st.slider(
        "🚿 Bathrooms",
        1,
        10,
        2
    )

with right:

    age = st.slider(
        "🏗 Property Age",
        0,
        50,
        5
    )

    location = st.selectbox(
        "📍 Location",
        ["City Center", "Suburb", "Rural"]
    )

    property_type = st.selectbox(
        "🏢 Property Type",
        ["Apartment", "House", "Villa"]
    )

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =========================================
# PREDICTION BUTTON
# =========================================

if st.button("🚀 Predict Property Price"):

    payload = {
        "area": area,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "age": age,
        "location": location,
        "property_type": property_type
    }

    try:

        with st.spinner("🤖 AI Model Analyzing Property Data..."):

            response = requests.post(
                API_URL,
                json=payload,
                timeout=20
            )

        if response.status_code == 200:

            result = response.json()

            predicted_price = result["predicted_price"]

            st.markdown("<br>", unsafe_allow_html=True)

            st.markdown("""
            <div class="result-card">
            <h2>✅ Prediction Generated Successfully</h2>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)

            # =========================================
            # MAIN RESULT
            # =========================================

            st.metric(
                "🏠 Estimated Property Price",
                f"₹ {predicted_price:,.0f}"
            )

            # =========================================
            # VISUAL ANALYTICS
            # =========================================

            chart_df = pd.DataFrame({
                "Feature": [
                    "Area",
                    "Bedrooms",
                    "Bathrooms",
                    "Property Age"
                ],
                "Value": [
                    area,
                    bedrooms,
                    bathrooms,
                    age
                ]
            })

            fig = px.bar(
                chart_df,
                x="Feature",
                y="Value",
                title="📊 Property Feature Overview",
                text="Value"
            )

            fig.update_layout(
                template="plotly_dark",
                height=500
            )

            st.plotly_chart(fig, use_container_width=True)

            # =========================================
            # PROPERTY SUMMARY
            # =========================================

            st.markdown("## 🧠 AI Property Insights")

            st.info(f"""
### 📌 Property Summary

The AI model predicts that this **{property_type}**
located in **{location}** has an estimated market value of:

# ₹ {predicted_price:,.0f}

### 🏡 Property Configuration
- 📐 Area: {area} sqft
- 🛏 Bedrooms: {bedrooms}
- 🚿 Bathrooms: {bathrooms}
- 🏗 Age: {age} years

### 🤖 AI Analysis
The valuation is generated using:
- XGBoost Machine Learning
- Feature Engineering
- Property Market Patterns
- Location Intelligence
- Historical Pricing Trends
            """)

        else:

            st.error(f"""
❌ API Error

Status Code: {response.status_code}

Response:
{response.text}
""")

    except Exception as e:

        st.error(f"""
⚠️ Backend Connection Failed

Error:
{e}
""")

# =========================================
# FOOTER
# =========================================

st.markdown("""
<div class="footer">

---

### 💼 Production-Grade AI Real Estate System

Built using:
FastAPI • Streamlit • XGBoost • Plotly • Scikit-Learn • Pandas

Designed & Developed for Modern ML Deployment 🚀

</div>
""", unsafe_allow_html=True)
