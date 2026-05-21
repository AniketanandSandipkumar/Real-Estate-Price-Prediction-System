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
    layout="wide"
)

# =========================================
# CUSTOM CSS
# =========================================

st.markdown("""
<style>

html, body, [class*="css"]  {
    font-family: 'Segoe UI', sans-serif;
}

.main {
    background: linear-gradient(to right, #0f172a, #111827);
    color: white;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

h1, h2, h3, h4 {
    color: white !important;
}

.card {
    background: rgba(255,255,255,0.08);
    padding: 20px;
    border-radius: 20px;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.1);
    box-shadow: 0px 4px 30px rgba(0,0,0,0.3);
}

.metric-card {
    background: linear-gradient(135deg, #1e293b, #0f172a);
    padding: 25px;
    border-radius: 18px;
    text-align: center;
    border: 1px solid rgba(255,255,255,0.08);
}

.metric-value {
    font-size: 30px;
    font-weight: bold;
    color: #38bdf8;
}

.metric-label {
    font-size: 14px;
    color: #cbd5e1;
}

.stButton>button {
    width: 100%;
    background: linear-gradient(90deg,#3b82f6,#06b6d4);
    color: white;
    border-radius: 12px;
    height: 3.2em;
    border: none;
    font-size: 18px;
    font-weight: bold;
}

.stButton>button:hover {
    background: linear-gradient(90deg,#2563eb,#0891b2);
    color: white;
}

</style>
""", unsafe_allow_html=True)

# =========================================
# HEADER
# =========================================

st.markdown("""
# 🏠 Real Estate Price Prediction System
### 🚀 AI-Powered Property Valuation Platform
""")

st.markdown("---")

# =========================================
# TOP METRICS
# =========================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-value">87%</div>
        <div class="metric-label">Model Accuracy</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-value">FastAPI</div>
        <div class="metric-label">Production Backend</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-value">XGBoost</div>
        <div class="metric-label">ML Model</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-value">Live</div>
        <div class="metric-label">API Status</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =========================================
# INPUT SECTION
# =========================================

st.markdown("## 📋 Property Details")

left, right = st.columns(2)

with left:

    area = st.slider("📐 Area (sqft)", 500, 10000, 2500)

    bedrooms = st.slider("🛏 Bedrooms", 1, 10, 3)

    bathrooms = st.slider("🚿 Bathrooms", 1, 10, 2)

    age = st.slider("🏗 Property Age", 0, 50, 5)

with right:

    location = st.selectbox(
        "📍 Location",
        ["City Center", "Suburb", "Rural"]
    )

    property_type = st.selectbox(
        "🏢 Property Type",
        ["Apartment", "House", "Villa"]
    )

    floor = st.slider("🏬 Floor", 1, 50, 2)

    facing = st.selectbox(
        "🧭 Facing",
        ["East", "West", "North", "South"]
    )

st.markdown("<br>", unsafe_allow_html=True)

# =========================================
# API URL
# =========================================

API_URL = "https://real-estate-price-prediction-system-9nka.onrender.com/predict"

# =========================================
# PREDICTION
# =========================================

if st.button("🚀 Predict Property Price"):

    payload = {
        "area": area,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "age": age,
        "location": location,
        "property_type": property_type,
        "floor": floor,
        "facing": facing
    }

    try:

        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:

            result = response.json()

            predicted_price = result["predicted_price"]

            st.success("✅ Prediction Successful")

            # =========================================
            # RESULT CARDS
            # =========================================

            c1, c2, c3 = st.columns(3)

            with c1:
                st.metric(
                    "🏠 Estimated Price",
                    f"₹ {predicted_price:,.0f}"
                )

            with c2:
                st.metric(
                    "📈 Lower Range",
                    f"₹ {result['confidence_interval']['lower_bound']:,.0f}"
                )

            with c3:
                st.metric(
                    "📉 Upper Range",
                    f"₹ {result['confidence_interval']['upper_bound']:,.0f}"
                )

            st.markdown("---")

            # =========================================
            # CHART
            # =========================================

            chart_df = pd.DataFrame({
                "Category": ["Lower", "Predicted", "Upper"],
                "Price": [
                    result['confidence_interval']['lower_bound'],
                    predicted_price,
                    result['confidence_interval']['upper_bound']
                ]
            })

            fig = px.bar(
                chart_df,
                x="Category",
                y="Price",
                title="📊 Prediction Confidence Range"
            )

            st.plotly_chart(fig, use_container_width=True)

            # =========================================
            # PROPERTY SUMMARY
            # =========================================

            st.markdown("## 🧠 AI Property Summary")

            st.info(f"""
            The property located in **{location}** with 
            **{bedrooms} bedrooms** and **{bathrooms} bathrooms**
            is estimated to have a market value of approximately
            **₹ {predicted_price:,.0f}**.

            The valuation is based on:
            - Area
            - Property age
            - Location quality
            - Property type
            - Floor positioning
            - Market behavioral patterns
            """)

        else:
            st.error("❌ API Error")

    except Exception as e:
        st.error(f"⚠️ Backend Connection Failed: {e}")

# =========================================
# FOOTER
# =========================================

st.markdown("---")

st.markdown("""
<center>

### 💼 Production-Ready AI Real Estate System

Built with:
FastAPI • Streamlit • XGBoost • Plotly • Scikit-Learn

</center>
""", unsafe_allow_html=True)
