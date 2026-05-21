import streamlit as st

# यह लाइन आपके कोड को स्क्रीन पर बटन में बदलेगी
st.markdown("""
<style>
    .main-container {
        font-family: 'Segoe UI', Arial, sans-serif;
        background: #f4f6f9;
        padding: 20px;
        border-radius: 12px;
        max-width: 850px;
        margin: auto;
    }
    .main-title {
        color: #1e3c72;
        font-size: 28px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 5px;
    }
    .subtitle {
        color: #666;
        font-size: 15px;
        text-align: center;
        margin-bottom: 25px;
    }
    .category-section {
        background: white;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
    .category-title {
        color: #d9534f;
        font-size: 18px;
        font-weight: bold;
        border-bottom: 2px solid #f0f0f0;
        padding-bottom: 8px;
        margin-bottom: 15px;
    }
    .grid-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
        gap: 12px;
    }
    .link-btn {
        display: block;
        padding: 14px;
        background: #f8f9fa;
        color: #1e3c72 !important;
        text-decoration: none !important;
        font-size: 15px;
        font-weight: bold;
        border-radius: 6px;
        border: 1px solid #e2e8f0;
        text-align: center;
        transition: all 0.2s;
    }
    .link-btn:hover {
        background: #1e3c72;
        color: white !important;
        transform: translateY(-2px);
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
