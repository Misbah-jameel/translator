import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

# 🌱 Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# 🔐 Check if API key is set
if not api_key:
    st.error("❌ GEMINI_API_KEY is not set! Please check your `.env` file.")
    st.stop()

# 🔧 Configure Gemini
genai.configure(api_key=api_key)

# 🌎 Supported Languages
languages = [
    "Urdu", "English","French", "Spanish", "German", "Chinese", "Japanese", "Korean", "Arabic",
    "Portuguese", "Russian", "Hindi", "Bengali", "Turkish", "Italian", "Dutch", "Greek",
    "Polish", "Swedish", "Thai", "Vietnamese", "Hebrew", "Malay", "Czech", "Romanian", "Finnish"
]

# 🌟 Streamlit UI
st.set_page_config(page_title="Translator by MISBAH JAMEEL", layout="centered")
st.title("🌐 AI Translator")
st.write("Created by **MISBAH JAMEEL** – Translate your English or Urdu text into various languages using Gemini AI. ✨")

# ✏️ Input Section
text = st.text_area("📝 Enter English or Urdu text to translate:", height=150)
lang = st.selectbox("🌍 Select target language:", languages)
btn = st.button("🚀 Translate")

# 🎯 Translation Logic
if btn and text:
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = f"""
        You are a translation assistant. Detect whether the input is in English or Urdu,
        and then translate the text to {lang}:

        {text}
        """
        response = model.generate_content(prompt)
        st.success(f"✅ Translated to {lang}:")
        st.markdown(f"**{response.text}**")
    except Exception as e:
        st.error(f"⚠️ Oops! Error: {str(e)}")
