import streamlit as st
import pandas as pd

st.title("Login Page")
username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if username == "admin" and password == "1234":
        st.success("Login successful!")
        # Show the dashboard here
    else:
        st.error("Invalid credentials")


# Title
st.title("🌾 Farmer Decision Support System")
st.markdown("Prototype built during a 24h hackathon to support farmer decision-making.")

# --- Yield Prediction & Price Forecasting ---
st.header("📈 Yield Prediction & Price Forecasting")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Predicted Crop Yield")
    st.metric(label="Yield (tons/hectare)", value="2.5", delta="↑ 0.3 from last season")

with col2:
    st.subheader("Price Trend Forecast")
    price_data = pd.DataFrame({
        "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
        "Price (₹/kg)": [22, 24, 23, 25, 27]
    })
    st.line_chart(price_data.set_index("Month"))

# --- Pest Outbreak Early Warning ---
st.header("🐛 Pest Outbreak Early Warning")

risk_level = "High"
recommendation = "Spray preventive pesticide in week 2"

st.warning(f"⚠️ Pest Risk Level: {risk_level}")
st.write(f"✅ Recommendation: {recommendation}")

# --- Footer ---
st.markdown("---")
st.caption("Demo prototype. Data is simulated for hackathon presentation")

# --- Crop Recommendation ---
st.header("🌱 Crop Recommendation")

soil_type = st.selectbox("Select Soil Type", ["Loamy", "Clay", "Sandy", "Alluvial"])
season = st.selectbox("Select Season", ["Kharif", "Rabi", "Summer"])

if st.button("Recommend Crop"):
    if soil_type == "Loamy" and season == "Kharif":
        st.success("Recommended Crop: Rice 🌾")
    elif soil_type == "Clay" and season == "Rabi":
        st.success("Recommended Crop: Wheat 🌾")
    elif soil_type == "Sandy" and season == "Summer":
        st.success("Recommended Crop: Groundnut 🌰")
    elif soil_type == "Alluvial" and season == "Kharif":
        st.success("Recommended Crop: Sugarcane 🍬")
    else:
        st.info("Try Maize 🌽")
