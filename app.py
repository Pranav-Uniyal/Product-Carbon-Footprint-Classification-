import streamlit as st
import numpy as np
import joblib

# Load your model
with open('carbon-footprint_model.pkl', 'rb') as f:
    model = joblib.load(f)

# Category Mapping
category_mapping = {'Beverages': 0, 'Dairy': 1, 'Desserts': 2, 'Fresh Food': 3,
                    'Frozen Food': 4, 'Meat': 5, 'Other': 6, 'Plant-based': 7,
                    'Prepared Foods': 8, 'Seafood': 9, 'Snacks': 10, 'Spreads': 11, 'Sweeteners': 12}

packaging_mapping = {'Cardboard': 0, 'Glass': 1, 'Metal': 2, 'Mixed': 3,
                     'Other': 4, 'Plastic': 5, 'Tetra Pack': 6}

origins_mapping = {'Belgium': 0, 'Brazil': 1, 'China': 2, 'Colombia': 3, 'Costa Rica': 4,
                   'Dominican Republic': 5, 'Ecuador': 6, 'Ethiopia': 7, 'European Union': 8,
                   'France': 9, 'Guatemala': 10, 'Iceland': 11, 'Italy': 12, 'Mexico': 13,
                   'Morocco': 14, 'Other': 15, 'Paraguay': 16, 'Peru': 17, 'Philippines': 18,
                   'South Africa': 19, 'Spain': 20, 'Sri Lanka': 21, 'Switzerland': 22,
                   'Thailand': 23, 'United Kingdom': 24}

countries_mapping = {'Belgium,France,Switzerland': 0, 'Brazil': 1, 'France': 2,
                     'France,Hong Kong': 3, 'Italy': 4, 'Spain': 5, 'Switzerland': 6,
                     'Tunisia': 7, 'United States,United Kingdom': 8}

# Carbon footprint classes
carbon_footprint_mapping = {0: 'Low', 1: 'Medium', 2: 'High'}

st.title("🌱 Carbon Footprint Prediction App")

# User Inputs
category = st.selectbox("Select Category", list(category_mapping.keys()))
packaging = st.selectbox("Select Packaging", list(packaging_mapping.keys()))
origin = st.selectbox("Select Origin", list(origins_mapping.keys()))
countries = st.selectbox("Select Countries", list(countries_mapping.keys()))

# Predict button
if st.button("Predict Carbon Footprint"):
    # Map to numeric values
    category_val = category_mapping[category]
    packaging_val = packaging_mapping[packaging]
    origin_val = origins_mapping[origin]
    countries_val = countries_mapping[countries]

    # Prepare input
    X_input = np.array([[category_val, packaging_val, origin_val, countries_val]])

    # Predict
    prediction = model.predict(X_input)[0]
    prediction_label = carbon_footprint_mapping.get(prediction, "Unknown")

    st.success(f"🌍 Predicted Carbon Footprint: **{prediction_label} ({prediction})**")
