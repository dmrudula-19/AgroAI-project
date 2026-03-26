import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

# Sidebar navigation

st.sidebar.title("Settings")
language = st.sidebar.selectbox("Choose Language", ["English", "Hindi", "Kannada"])

# 🔹 Paste the full dictionary here
translations = {
    "English": {
        "login_title": "Login Page",
        "username": "Username",
        "password": "Password",
        "login_success": "Login successful!",
        "login_error": "Invalid credentials",
        "yield_title": "Yield Prediction & Price Forecasting",
        "weather_title": "Weather Forecast",
        "profit_title": "Profitability Calculator",
        "crop_title": "Crop Recommendation",
        "market_title": "Market Price Trends",
        "pest_title": "Pest Outbreak Alert"
    },
    "Hindi": {
        "login_title": "लॉगिन पेज",
        "username": "उपयोगकर्ता नाम",
        "password": "पासवर्ड",
        "login_success": "लॉगिन सफल!",
        "login_error": "अमान्य प्रमाणपत्र",
        "yield_title": "उपज भविष्यवाणी और मूल्य पूर्वानुमान",
        "weather_title": "मौसम पूर्वानुमान",
        "profit_title": "लाभप्रदता कैलकुलेटर",
        "crop_title": "फसल सिफारिश",
        "market_title": "बाजार मूल्य प्रवृत्तियाँ",
        "pest_title": "कीट प्रकोप चेतावनी"
    },
    "Kannada": {
        "login_title": "ಲಾಗಿನ್ ಪುಟ",
        "username": "ಬಳಕೆದಾರ ಹೆಸರು",
        "password": "ಪಾಸ್ವರ್ಡ್",
        "login_success": "ಲಾಗಿನ್ ಯಶಸ್ವಿಯಾಗಿದೆ!",
        "login_error": "ಅಮಾನ್ಯ ದಾಖಲೆಗಳು",
        "yield_title": "ಉತ್ಪಾದನೆ ಭವಿಷ್ಯವಾಣಿ ಮತ್ತು ಬೆಲೆ ಪೂರ್ವಾನುಮಾನ",
        "weather_title": "ಹವಾಮಾನ ಪೂರ್ವಾನುಮಾನ",
        "profit_title": "ಲಾಭದಾಯಕತೆ ಕ್ಯಾಲ್ಕುಲೇಟರ್",
        "crop_title": "ಬೆಳೆ ಶಿಫಾರಸು",
        "market_title": "ಮಾರುಕಟ್ಟೆ ಬೆಲೆ ಪ್ರವೃತ್ತಿಗಳು",
        "pest_title": "ಕೀಟರ ಪ್ರಾದುರ್ಭಾವ ಎಚ್ಚರಿಕೆ"
    }
}

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Login", "Yield Prediction", "Weather", "Profitability", "Crop Recommendation", "Market Trends", "Pest Alert"])

# --- Login Page ---
if page == "Login":
    st.title(translations[language]["login_title"])
    username = st.text_input(translations[language]["username"])
    password = st.text_input(translations[language]["password"], type="password")

    if st.button("Login"):
        if username == "admin" and password == "1234":
            st.success(translations[language]["login_success"])
        else:
            st.error(translations[language]["login_error"])


# --- Yield Prediction & Price Forecasting ---
elif page == "Yield Prediction":
    st.header("📈 " + translations[language]["yield_title"])
    
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

# --- Weather Forecast ---
elif page == "Weather":
    st.header("🌦️ " + translations[language]["weather_title"])
   
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap key
    city = st.text_input("Enter city name", "Bengaluru")

    if st.button("Get Weather"):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            desc = data["weather"][0]["description"]
            st.metric("Temperature (°C)", temp)
            st.metric("Humidity (%)", humidity)
            st.write(f"Condition: {desc.capitalize()}")
        else:
            st.error("Weather data not available")

# --- Profitability Calculator ---
elif page == "Profitability":
    st.header("💰 " + translations[language]["profit_title"])
   
    cost = st.number_input("Enter total cost (₹)", min_value=0)
    yield_val = st.number_input("Enter expected yield (tons)", min_value=0.0)
    price_per_ton = st.number_input("Enter expected price (₹ per ton)", min_value=0)

    if st.button("Calculate Profit"):
        revenue = yield_val * price_per_ton
        profit = revenue - cost
        st.write(f"Estimated Revenue: ₹{revenue}")
        st.write(f"Estimated Profit: ₹{profit}")
        if profit > 0:
            st.success("✅ Profitable!")
        else:
            st.error("⚠️ Loss expected")

# --- Crop Recommendation ---
elif page == "Crop Recommendation":
    st.header("🌱 " + translations[language]["crop_title"])
 
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

# --- Market Price Trends ---
elif page == "Market Trends":
    st.header("📈 " + translations[language]["market_title"])

    data = {
        "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
        "Wheat": [2200, 2300, 2100, 2400, 2500],
        "Rice": [1800, 1750, 1900, 2000, 1950]
    }
    df = pd.DataFrame(data)
    st.line_chart(df.set_index("Month"))

# --- Pest Outbreak Alert ---
elif page == "Pest Alert":
    st.header("🐛 " + translations[language]["pest_title"])
    humidity = st.slider("Humidity (%)", 0, 100, 50)
    temperature = st.slider("Temperature (°C)", 10, 45, 25)
    if st.button("Check Pest Risk"):
        if humidity > 70 and temperature > 25:
            st.error("⚠️ High risk of pest outbreak!")
        else:
            st.success("✅ Low risk of pest outbreak")