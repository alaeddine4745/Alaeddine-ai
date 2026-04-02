import streamlit as st
import google.generativeai as genai

# دير الـ API Key ديالك هنا بين جوج علامات تنصيص
genai.configure(api_key="اكتب_هنا_API_KEY_ديالك")

model = genai.GenerativeModel('gemini-1.5-flash')

# إعدادات الصفحة
st.set_page_config(page_title="مرشد الأمان", layout="centered")

# واجهة التطبيق (نفس اللي في الصورة ديالك)
st.markdown("<h1 style='text-align: center; color: red;'>🛡️ مرشد الأمان</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>🔍 رادار الشك</h3>", unsafe_allow_html=True)
st.write("صيفط ليا أي رابط أو رسالة شاك فيها، وأنا نحللها ليك!")

user_input = st.text_area("كوبي الرابط أو الرسالة هنا...", placeholder="https://example.com")

if st.button("حلل دابا"):
    if user_input:
        with st.spinner('جاري الفحص...'):
            try:
                response = model.generate_content(f"حلل هذا الرابط أو الرسالة واذكر إذا كانت احتيالية (Scam) أم لا بالدارجة المغربية: {user_input}")
                st.info("النتيجة:")
                st.write(response.text)
            except Exception as e:
                st.error("كاين مشكل في الـ API Key، تأكد منه.")
    else:
        st.warning("عفاك حط شي رابط أولا نص.")
