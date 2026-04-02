import streamlit as st
import google.generativeai as genai

# 1. إعداد الساروت (بدل AIza... بالساروت ديالك)
API_KEY = "حط_هنا_API_KEY_ديالك"

genai.configure(api_key=API_KEY)

# استخدام موديل فلاش السريع جداً
model = genai.GenerativeModel('gemini-1.5-flash')

# 2. تحسين أداء الصفحة
st.set_page_config(page_title="مرشد الأمان", page_icon="🛡️")

# ستايل احترافي وبسيط
st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>🛡️ مرشد الأمان</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>تحليل فوري وسريع للروابط والميساجات</p>", unsafe_allow_html=True)

# 3. واجهة الإدخال
user_input = st.text_area("حط النص هنا:", height=100, placeholder="انسخ الرابط أو الرسالة هنا...")

# 4. زر التحليل السريع
if st.button("تحليل سريع ⚡"):
    if user_input:
        with st.spinner('جاري الفحص...'):
            try
