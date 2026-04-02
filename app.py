import streamlit as st
import google.generativeai as genai

# 1. إعداد الساروت (عوض AIzaSy... بالساروت ديالك الحقيقي)
API_KEY = "AIzaSy..." 

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# 2. إعدادات الصفحة (العنوان والأيقونة)
st.set_page_config(page_title="مرشد الأمان", page_icon="🛡️")

# 3. واجهة المستخدم بالدارجة
st.markdown("<h1 style='text-align: center; color: red;'>🛡️ مرشد الأمان</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>🔍 رادار الشك</h3>", unsafe_allow_html=True)

st.write("### صيفط ليا أي رابط أو رسالة شاك فيها، وأنا نحللها ليك ونقوليك واش نصابة ولا آمنة.")

# خانة إدخال النص
user_input = st.text_area("كوبي الرابط أو الرسالة هنا:", placeholder="مثلاً: جاني ميساج فيه ربحتي جائزة...")

# 4. منطق التحليل
if st.button("حلل دابا 🛡️"):
    if user_input:
        with st.spinner('جاري الفحص... تسنى شوية'):
            try:
                # طلب التحليل بالدارجة المغربية بشكل صريح
                prompt = f"Analyze strictly in Moroccan Darija if the following content is a scam or safe. Explain the risks
