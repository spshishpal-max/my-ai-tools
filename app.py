import streamlit as st

# यह लाइन आपकी स्क्रीन को पूरी चौड़ाई देगी ताकि लेआउट अच्छा दिखे
st.set_page_config(layout="wide")

# CSS स्टाइल - जो टेक्स्ट को सुंदर बटन में बदल देगा
st.markdown("""
<style>
    .main-container {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        background: linear-gradient(135deg, #f5f7fa 0%, #e4ecf7 100%);
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.08);
        max-width: 900px;
        margin: auto;
    }
    .main-title {
        color: #1e3c72;
        font-size: 30px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 5px;
    }
    .subtitle {
        color: #555;
        font-size: 16px;
        text-align: center;
        margin-bottom: 30px;
    }
    .category-section {
        margin-bottom: 25px;
    }
    .category-title {
        color: #d9534f;
        font-size: 18px;
        font-weight: bold;
        border-bottom: 2px solid #d9534f;
        padding-bottom: 5px;
        margin-bottom: 15px;
    }
    .grid-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
        gap: 15px;
    }
    .link-btn {
        display: block;
        padding: 15px;
        background: #ffffff;
        color: #2c3e50 !important;
        text-decoration: none !important;
        font-size: 15px;
        font-weight: 600;
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        border: 1px solid #e1e8ed;
        transition: all 0.3s ease;
        text-align: center;
    }
    .link-btn:hover {
        background: #1e3c72;
        color: #ffffff !important;
        transform: translateY(-3px);
        box-shadow: 0 6px 12px rgba(19, 39, 71, 0.2);
    }
</style>

<div class="main-container">
    <div class="main-title">🇮🇳 11zon ऑल-इन-वन डिजिटल सेवा पोर्टल</div>
    <div class="subtitle">सभी महत्वपूर्ण सरकारी, श्रम और किसान सेवाएं एक ही स्थान पर</div>
    
    <!-- श्रम एवं रोजगार सेवाएं -->
    <div class="category-section">
        <div class="category-title">💼 श्रम, पीएफ और कर्मचारी सेवाएं (PF & ESIC)</div>
        <div class="grid-container">
            <a href="https://epfindia.gov.in" target="_blank" class="link-btn">💰 PF मेम्बर पोर्टल (EPFO)</a>
            <a href="https://esic.gov.in" target="_blank" class="link-btn">🆔 ESIC पहचान पोर्टल</a>
            <a href="https://eshram.gov.in" target="_blank" class="link-btn">🪪 ई-श्रम कार्ड (e-Shram)</a>
        </div>
    </div>

    <!-- किसान एवं मंडी सेवाएं -->
    <div class="category-section">
        <div class="category-title">🌾 किसान कल्याण एवं कृषि सेवाएं</div>
        <div class="grid-container">
            <a href="https://agmarknet.gov.in" target="_blank" class="link-btn">📊 दैनिक मंडी भाव (Agmarknet)</a>
            <a href="https://pmkisan.gov.in" target="_blank" class="link-btn">🚜 PM किसान सम्मान निधि</a>
            <a href="https://imd.gov.in" target="_blank" class="link-btn">🌤️ मौसम विभाग (IMD Weather)</a>
        </div>
    </div>

    <!-- दैनिक कैलेंडर एवं पंचांग -->
    <div class="category-section">
        <div class="category-title">📅 दैनिक पंचांग एवं कैलेंडर</div>
        <div class="grid-container">
            <a href="https://drikpanchang.com" target="_blank" class="link-btn">🗓️ हिंदी कैलेंडर / पंचांग</a>
        </div>
    </div>

    <!-- प्रमुख सरकारी मुख्य वेबसाइट्स -->
    <div class="category-section">
        <div class="category-title">🏛️ राष्ट्रीय एवं राज्य स्तरीय पोर्टल</div>
        <div class="grid-container">
            <a href="https://india.gov.in" target="_blank" class="link-btn">🏛️ भारत सरकार (Govt. of India)</a>
            <a href="https://rajasthan.gov.in" target="_blank" class="link-btn">🎨 राजस्थान सरकार (Govt. of Raj)</a>
            <a href="https://sansad.in" target="_blank" class="link-btn">👑 राज्यसभा पोर्टल (Rajya Sabha)</a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
