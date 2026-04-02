import streamlit as st
import os

# -------------------------
# Page Config
# -------------------------
st.set_page_config(
    page_title="Sentiment Web Analyzer",
    page_icon="😊",
    layout="centered"
)

# -------------------------
# Load Background Image Safely
# -------------------------
current_dir = os.path.dirname(__file__)  # directory of this script
image_path = os.path.join(current_dir, "image.jpg")  # change filename if needed

if os.path.exists(image_path):
    st.image(image_path, width=700)  # adjust width as needed
else:
    st.warning("Background image not found! Please add 'image.jpg' to the project folder.")

# -------------------------
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