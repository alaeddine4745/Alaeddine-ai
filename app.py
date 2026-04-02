import streamlit as st
import google.generativeai as genai

# --- CONFIGURATION ---
# Replace "YOUR_API_KEY_HERE" with your actual Gemini API Key from AI Studio
genai.configure(api_key="YOUR_API_KEY_HERE")

model = genai.GenerativeModel('gemini-1.5-flash')

# --- PAGE SETUP ---
st.set_page_config(page_title="Security Guide", page_icon="🛡️", layout="centered")

# --- UI DESIGN ---
st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>🛡️ Security Guide</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>🔍 Suspicion Radar</h3>", unsafe_allow_html=True)
st.write("Paste
