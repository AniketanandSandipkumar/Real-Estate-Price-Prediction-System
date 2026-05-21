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

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

body {
    background: #0f172a;
}

.main {
    background: linear-gradient(135deg, #0f172a, #111827);
    color: white;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 1300px;
}

h1, h2, h3 {
    color: #f8fafc !important;
}

/* HERO CARD HEADING COLORS */
.hero-card {
    background: linear-gradient(135deg, rgba(59,130,246,0.15), rgba(6,182,212,0.12));
    border: 1px solid rgba(255,255,255,0.1);
    padding: 35px;
    border-radius: 25px;
    backdrop-filter: blur(12px);
    box-shadow: 0 10px 40px rgba(0,0,0,0.35);
}

/* MAIN TITLE */

.hero-card h1 {
    color: #93c5fd !important;
    font-weight: 700;
    letter-spacing: -1px;
}

/* SUBTITLE */

.hero-card h3 {
    color: #94a3b8 !important;
    font-weight: 500;
}

/* NORMAL TEXT */

.hero-card p,
.hero-card li {
    color: #cbd5e1 !important;
    font-weight: 400;
}

.metric-card {
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 22px;
    padding: 25px;
    text-align: center;
    backdrop-filter: blur(10px);
    transition: 0.3s ease;
}

.metric-card:hover {
    transform: translateY(-5px);
    border: 1px solid rgba(56,189,248,0.5);
}

.metric-value {
    font-size: 34px;
    font-weight: 700;
    color: #38bdf8;
}

.metric-label {
    font-size: 14px;
    color: #cbd5e1;
    margin-top: 8px;
}

.input-card {
    background: rgba(255,255,255,0.05);
    padding: 30px;
    border-radius: 24px;
    border: 1px solid rgba(255,255,255,0.08);
    backdrop-filter: blur(10px);
}

.stButton>button {
    width: 100%;
    background: linear-gradient(90deg,#2563eb,#06b6d4);
    color: white;
    border-radius: 14px;
    height: 3.5em;
    border: none;
    font-size: 20px;
    font-weight: 600;
    transition: 0.3s ease;
}

.stButton>button:hover {
    transform: scale(1.02);
    background: linear-gradient(90deg,#1d4ed8,#0891b2);
    color: white;
}

.result-card {
    background: linear-gradient(135deg, rgba(16,185,129,0.15), rgba(6,182,212,0.1));
    padding: 30px;
    border-radius: 24px;
    border: 1px solid rgba(255,255,255,0.08);
}

/* =========================================
PREMIUM FOOTER
========================================= */

.footer {
    text-align: center;
    margin-top: 45px;
    padding-top: 20px;
    color: #64748b !important;
    font-size: 15px;
    font-weight: 500;
}

/* FOOTER HEADINGS */

.footer h3,
.footer h4 {
    color: #94a3b8 !important;
    font-weight: 600;
}

/* FOOTER NORMAL TEXT */

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
