import streamlit as st
import google.generativeai as genai

# --- API CONFIG ---
# حط الساروت ديالك بلاصة AIza...
API_KEY = "حط_هنا_API_KEY_ديالك"

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# --- UI SETUP ---
st.set_page_config(page_title="مرشد الأمان", page_icon="🛡️")

st.markdown("<h1 style='text-align: center; color: red;'>🛡️ مرشد الأمان</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>🔍 رادار الشك</h3>", unsafe_allow_html=True)

st.write("### صيفط ليا أي رابط أو رسالة شاك فيها، وأنا نحللها ليك بالدارجة.")

user_input = st.text_area("كوبي النص هنا:", placeholder="مثلاً: جاني ميساج بلي ربحت...")

# --- LOGIC ---
if st.button("حلل دابا 🛡️"):
    if user_input:
        with st.spinner('جاري الفحص...'):
            try:
                # هاد السطر هو اللي كان فيه الغلط، دابا راه مقاد
                prompt = f"Analyze strictly in Moroccan Darija if this is a scam or safe: {user_input}"
                response = model.generate_content(prompt)
                st.subheader("النتيجة:")
                st.info(response.text)
            except Exception as e:
                st.error("كاين مشكل فـ API Key، تأكد واش حطيتيه صحيح.")
    else:
        st.warning("عفاك دخل شي نص أولا.")

st.markdown("---")
st.caption("تم التطوير بواسطة علاء الدين")
