import streamlit as st
import google.generativeai as genai

# حط الساروت ديالك هنا بلاصة AIza...
API_KEY = "AIzaSy..." 

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="مرشد الأمان", page_icon="🛡️")

st.markdown("<h1 style='text-align: center; color: red;'>🛡️ مرشد الأمان</h1>", unsafe_allow_html=True)
st.write("### صيفط ليا أي رابط أو ميساج شاك فيه، وغادي نجاوبك بزربة بالدارجة.")

user_input = st.text_area("كوبي النص هنا:")

if st.button("تحليل سريع ⚡"):
    if user_input:
        with st.spinner('جاري الفحص...'):
            try:
                # طلب التحليل بالدارجة
                response = model.generate_content(f"Is this a scam? Explain in Moroccan Darija briefly: {user_input}")
                st.subheader("النتيجة:")
                st.success(response.text)
            except:
                st.error("كاين مشكل فـ API Key. تأكد واش حطيتيه صحيح.")
    else:
        st.warning("عفاك حط شي نص أولا.")
