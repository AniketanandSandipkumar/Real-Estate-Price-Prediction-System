import streamlit as st
import requests


API_URL = "http://localhost:8000/predict"


st.set_page_config(
    page_title="Real Estate Price Predictor",
    page_icon="🏢",
    layout="wide"
)


st.title("🏢 Real Estate Price Prediction Dashboard")


col1, col2 = st.columns(2)


with col1:

    area = st.number_input("Area (sqft)")
    bedrooms = st.slider("Bedrooms", 1, 10)
    bathrooms = st.slider("Bathrooms", 1, 10)


with col2:

    age = st.slider("Property Age", 0, 50)
    location = st.selectbox(
        "Location",
        ["Mumbai", "Pune", "Delhi", "Bangalore"]
    )

    property_type = st.selectbox(
        "Property Type",
        ["Apartment", "Villa", "Independent House"]
    )


if st.button("🚀 Predict Price"):

    payload = {
        "area": area,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "age": age,
        "location": location,
        "property_type": property_type
    }

    response = requests.post(API_URL, json=payload)

    if response.status_code == 200:

        prediction = response.json()["predicted_price"]

        st.success(
            f"Estimated Property Price: ₹{prediction:,.2f}"
        )

    else:
        st.error("Prediction failed")
