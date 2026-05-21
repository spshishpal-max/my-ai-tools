import streamlit as st

# मुख्य टाइटल
st.title("🇮🇳 Shishpal Godara ऑल-इन-वन डिजिटल सेवा पोर्टल")
st.write("सभी महत्वपूर्ण सरकारी, श्रम और किसान सेवाएं एक ही स्थान पर")

# 1. श्रम एवं रोजगार सेवाएं
st.header("💼 श्रम, पीएफ और कर्मचारी सेवाएं (PF & ESIC)")
col1, col2, col3 = st.columns(3)
with col1:
    st.link_button("💰 PF मेम्बर पोर्टल (EPFO)", "https://epfindia.gov.in")
with col2:
    st.link_button("🆔 ESIC पहचान पोर्टल", "https://esic.gov.in")
with col3:
    st.link_button("🪪 ई-श्रम कार्ड (e-Shram)", "https://eshram.gov.in")

# 2. किसान एवं मंडी सेवाएं
st.header("🌾 किसान कल्याण एवं कृषि सेवाएं")
col4, col5, col6 = st.columns(3)
with col4:
    st.link_button("📊 दैनिक मंडी भाव", "https://agmarknet.gov.in")
with col5:
    st.link_button("🚜 PM किसान सम्मान निधि", "https://pmkisan.gov.in")
with col6:
    st.link_button("🌤️ मौसम विभाग (IMD Weather)", "https://imd.gov.in")

# 3. दैनिक कैलेंडर एवं पंचांग
st.header("📅 दैनिक पंचांग एवं कैलेंडर")
st.link_button("🗓️ हिंदी कैलेंडर / पंचांग", "https://drikpanchang.com")

# 4. प्रमुख सरकारी मुख्य वेबसाइट्स
st.header("🏛️ राष्ट्रीय एवं राज्य स्तरीय पोर्टल")
col7, col8, col9 = st.columns(3)
with col7:
    st.link_button("🏛️ भारत सरकार (Govt. of India)", "https://india.gov.in")
with col8:
    st.link_button("🎨 राजस्थान सरकार (Govt. of Raj)", "https://rajasthan.gov.in")
with col9:
    st.link_button("👑 राज्यसभा पोर्टल (Rajya Sabha)", "https://sansad.in")
