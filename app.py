import streamlit as st
import os

# -------------------------
# Page Config
# -------------------------
st.set_page_config(
    page_title="Sentiment Web Analyzer",
    page_icon="😊",
    layout="centered
    
# App Title
# -------------------------
st.title("Sentiment Web Analyzer")

# -------------------------
# Text Input for User
# -------------------------
user_text = st.text_area("Enter text to analyze sentiment:")

# -------------------------
# Button to Analyze
# -------------------------
if st.button("Analyze Sentiment"):
    if user_text.strip() == "":
        st.error("Please enter some text!")
    else:
        # Dummy sentiment analysis (replace with your model)
        if "good" in user_text.lower():
            sentiment = "Positive 😊"
        elif "bad" in user_text.lower():
            sentiment = "Negative 😢"
        else:
            sentiment = "Neutral 😐"

        st.success(f"Sentiment: {sentiment}")
