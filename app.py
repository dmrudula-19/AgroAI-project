import streamlit as st
import pandas as pd

# Page setup
st.set_page_config(page_title="Farmer Decision Support System", layout="wide")

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