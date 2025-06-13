import streamlit as st
from mood_logic import get_mood_suggestion
from weather import get_weather

st.title("🌤️ Weather Mood Booster Bot")
st.subheader("Enter your Indian city and get fun, meaningful activity suggestions!")

city = st.text_input("Enter city name (India only):")

if city:
    condition, temp = get_weather(city)
    if condition:
        suggestion = get_mood_suggestion(condition, city)
        st.success(f"Weather in {city.title()}: {condition}, {temp}°C")
        st.markdown("### 🎯 Here's a fun & productive idea for you:")
        st.write(suggestion)
    else:
        st.error("Couldn't fetch weather. Make sure the city name is correct or API key is valid.")
