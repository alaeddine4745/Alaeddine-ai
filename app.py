import streamlit as st
import google.generativeai as genai

# --- API CONFIGURATION ---
# Replace YOUR_API_KEY with your real key from Google AI Studio
genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel('gemini-1.5-flash')

# --- PAGE CONFIG ---
st.set_page_config(page_title="Security Guide", page_icon="🛡️")

# --- UI CONTENT ---
st.markdown("<h1 style='text-align: center; color: red;'>🛡️ Security Guide</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Suspicion Radar</h3>", unsafe_allow_html=True)

user_input = st.text_area("Paste the link or message here:")

# --- LOGIC ---
if st.button("Analyze Now"):
    if user_input:
        with st.spinner('Analyzing...'):
            try:
                # Prompting Gemini to respond in Moroccan Darija
                prompt = f"Analyze if this is a scam or safe. Explain why in Moroccan Darija: {user_input}"
                response = model.generate_content(prompt)
                st.subheader("Result:")
                st.write(response.text)
            except Exception as e:
                st.error("Error: Check your API Key configuration.")
    else:
        st.warning("Please paste something first.")
