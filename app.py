import streamlit as st

# ----------------- 11zon ऑफिशियल टूल लिंक लेआउट -----------------
st.markdown("<h2 style='text-align: center; color: #EF4444;'>📄 प्रीमियम सुपर-फास्ट PDF कंप्रेसर सेंटर</h2>", unsafe_allow_html=True)
st.write("बड़ी फाइलों को बिना किसी एरर के 100% सुरक्षित और भारी मात्रा में छोटा (MB से KB) करने के लिए नीचे दिए गए बटन पर क्लिक करें। यह टूल आपको सीधे आधिकारिक हाई-कंप्रेशन सर्वर पर ले जाएगा।")

# एक सुंदर बॉक्स और सीधा लिंक बटन बनाना
st.markdown("""
<div style="background-color: #F8FAFC; border: 1px solid #E2E8F0; padding: 25px; border-radius: 10px; text-align: center; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); margin-top: 20px;">
    <div style="font-size: 50px; margin-bottom: 10px;">⚡</div>
    <h3 style="color: #1E293B; margin-bottom: 15px;">11zon ऑफिशियल कंप्रेशन इंजन</h3>
    <p style="color: #64748B; font-size: 14px; margin-bottom: 20px;">चूंकि यह टूल सीधे आधिकारिक सुरक्षित क्लाउड से चलता है, यह आपकी 3.80 MB की फाइल को तुरंत 200 KB से कम में बदल देगा।</p>
    <a href="https://11zon.com" target="_blank" style="text-decoration: none;">
        <button style="background-color: #EF4444; color: white; border: none; padding: 12px 35px; font-size: 16px; font-weight: bold; border-radius: 6px; cursor: pointer; box-shadow: 0 2px 4px rgba(239, 68, 68, 0.3); transition: 0.3s;">
            ओपन 11zon कंप्रेसर (New Window) ↗
        </button>
    </a>
</div>
""", unsafe_allow_html=True)

st.write("")
st.info("💡 नोट: बटन पर क्लिक करते ही कंप्रेसर नए टैब में सुरक्षित खुल जाएगा, जिससे आपकी यह वेबसाइट भी बैकग्राउंड में खुली रहेगी।")
