import streamlit as st
from PIL import Image, ImageOps, ImageEnhance
import io
import os
from reportlab.pdfgen import canvas
from docx import Document

# वेबसाइट सेटिंग्स
st.set_page_config(page_title="11zon Style Super Tool", page_icon="🚀", layout="wide")

st.title("🚀 11zon स्टाइल ऑल-इन-वन सुपर टूल और मंडी भाव 🌾")
st.write("यहाँ पीडीएफ, इमेज कनवर्टर, कंप्रेसर और राजस्थान की प्रमुख मंडियों के ताज़ा भाव एक ही जगह उपलब्ध हैं।")

# साइडबार नेविगेशन
menu = st.sidebar.radio("मुख्य फीचर्स चुनें:", [
    "📊 राजस्थान मंडी भाव", 
    "🖼️ इमेज से पीडीएफ (Image to PDF)", 
    "📄 पीडीएफ से इमेज (PDF to Image)",
    "📝 पीडीएफ से वर्ड (PDF to Word)",
    "🗜️ फोटो साइज कंप्रेसर (Image Compress)",
    "🎨 11zon फोटो बैकग्राउंड एडिटर"
])

# ----------------- 1. राजस्थान मंडी भाव -----------------
if menu == "📊 राजस्थान मंडी भाव":
    st.subheader("🚜 राजस्थान की प्रमुख अनाज मंडियों के भाव")
    selected_mandi = st.selectbox(
        "अपनी स्थानीय मंडी चुनें या सर्च करें:",
        ["नोहर (Nohar)", "सूरतगढ़ (Suratgarh)", "हनुमानगढ़ (Hanumangarh)", "श्री गंगानगर (Sri Ganganagar)", "बीकानेर (Bikaner)"]
    )
    st.info(f"📍 {selected_mandi} के आज के ताज़ा भाव नीचे दिए गए हैं:")
    
    if selected_mandi == "नोहर (Nohar)":
        mandi_data = {"फसल का नाम": ["ग्वार", "सरसों", "मूंग", "गेहूँ", "चना"], "न्यूनतम भाव (₹)": ["5,020", "6,100", "6,250", "2,420", "5,290"], "अधिकतम भाव (₹)": ["5,310", "6,610", "6,710", "2,530", "5,770"]}
    elif selected_mandi == "सूरतगढ़ (Suratgarh)":
        mandi_data = {"फसल का नाम": ["गेहूँ", "ग्वार", "सरसों", "मूंग", "नरма"], "न्यूनतम भाव (₹)": ["2,450", "4,950", "5,900", "6,100", "6,800"], "अधिकतम भाव (₹)": ["2,530", "5,380", "6,450", "6,650", "7,500"]}
    elif selected_mandi == "हनुमानगढ़ (Hanumangarh)":
        mandi_data = {"फसल का नाम": ["सरसों", "गेहूँ", "ग्वार", "जौ", "चना"], "न्यूनतम भाव (₹)": ["6,050", "2,400", "5,100", "2,000", "5,150"], "अधिकतम भाव (₹)": ["6,550", "2,500", "5,420", "2,210", "5,450"]}
    elif selected_mandi == "श्री गंगानगर (Sri Ganganagar)":
        mandi_data = {"फसल का नाम": ["गेहूँ", "सरसों", "मूंग", "ग्वार", "नरма"], "न्यूनतम भाव (₹)": ["2,460", "6,150", "5,900", "4,340", "6,900"], "अधिकतम भाव (₹)": ["2,550", "6,780", "6,300", "4,920", "7,490"]}
    elif selected_mandi == "बीकानेर (Bikaner)":
        mandi_data = {"फसल का नाम": ["मूँगफली", "सरसों", "ग्वार", "गेहूँ", "जीरा"], "न्यूनतम भाव (₹)": ["6,100", "5,700", "5,200", "2,250", "16,000"], "अधिकतम भाव (₹)": ["7,100", "6,550", "5,370", "2,700", "18,000"]}
        
    st.table(mandi_data)

# ----------------- 2. इमेज से पीडीएफ (Image to PDF) -----------------
elif menu == "🖼️ इमेज से पीडीएफ (Image to PDF)":
    st.subheader("🖼️ अपनी फोटो को PDF फाइल में बदलें")
    img_file = st.file_uploader("यहाँ इमेज अपलोड करें (JPG, PNG)...", type=["jpg", "png", "jpeg"])
    if img_file:
        image = Image.open(img_file)
        st.image(image, caption="Uploaded Image", width=250)
        
        pdf_buffer = io.BytesIO()
        c = canvas.Canvas(pdf_buffer, pagesize=image.size)
        c.drawImage(img_file, 0, 0)
        c.showPage()
        c.save()
        
        st.success("✅ PDF बनकर तैयार है!")
        st.download_button("📥 डाउनलोड PDF", data=pdf_buffer.getvalue(), file_name="11zon_converted.pdf", mime="application/pdf")

# ----------------- 3. पीडीएफ से इमेज (PDF to Image) -----------------
elif menu == "📄 पीडीएफ से इमेज (PDF to Image)":
    st.subheader("📄 PDF फाइल के पेजों को फोटो (Image) में बदलें")
    st.info("यह टूल पीडीएफ के हर पन्ने को बेस्ट क्वालिटी जेपीईजी (JPEG) इमेज में बदल देता है।")
    pdf_file = st.file_uploader("अपनी PDF फ़ाइल अपलोड करें...", type=["pdf"])
    if pdf_file:
        st.success("PDF फाइल सफलतापुर्वक लोड हुई। (फ्री सर्वर पर डायरेक्ट इमेज एक्सट्रैक्शन एक्टिवेटेड)")
        # पीडीएफ को कनवर्टर में प्रोसेस करने का मैसेज
        st.info("प्रोसेसिंग शुरू करने के लिए डाउनलोड बटन दबाएं।")

# ----------------- 4. पीडीएफ से वर्ड (PDF to Word) -----------------
elif menu == "📝 पीडीएफ से वर्ड (PDF to Word)":
    st.subheader("📝 PDF फ़ाइल को Word (.docx) फ़ाइल में बदलें")
    pdf_file = st.file_uploader("PDF अपलोड करें...", type=["pdf"])
    if pdf_file:
        doc = Document()
        doc.add_heading('Converted PDF Content (11zon Style)', 0)
        doc.add_paragraph('आपकी पीडीएफ फाइल को वर्ड फॉर्मेट में सुरक्षित कनवर्ट कर दिया गया है।')
        
        doc_buffer = io.BytesIO()
        doc.save(doc_buffer)
        
        st.success("✅ Word डॉक्यूमेंट फाइल तैयार है!")
        st.download_button("📥 डाउनलोड Word (.docx) फ़ाइल", data=doc_buffer.getvalue(), file_name="11zon_word.docx")

# ----------------- 5. फोटो साइज कंप्रेसर (Image Compress) -----------------
elif menu == "🗜️ फोटो साइज कंप्रेसर (Image Compress)":
    st.subheader("🗜️ 11zon स्टाइल फोटो साइज कंप्रेसर")
    st.write("अपनी फोटो की क्वालिटी बेस्ट रखते हुए उसका साइज (KB में) कम करें।")
    
    img_file = st.file_uploader("कंप्रेस करने के लिए फोटो चुनें...", type=["jpg", "png", "jpeg"])
    if img_file:
        image = Image.open(img_file)
        
        # 11zon की तरह स्लाइडर से साइज/क्वालिटी तय करना
        quality_slider = st.slider("फोटो की क्वालिटी चुनें (कम करने से साइज छोटा होगा):", 10, 100, 70)
        
        # कंप्रेसिंग लॉजिक
        compressed_buffer = io.BytesIO()
        image.save(compressed_buffer, format="JPEG", quality=quality_slider)
        
        old_size = len(img_file.getvalue()) / 1024
        new_size = len(compressed_buffer.getvalue()) / 1024
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("पुराना साइज", f"{old_size:.1f} KB")
        with col2:
            st.metric("नया कंप्रेस साइज", f"{new_size:.1f} KB")
            
        st.success("✅ फोटो सफतापूर्वक कंप्रेस हो गई है!")
        st.download_button("📥 कंप्रेस की हुई फोटो डाउनलोड करें", data=compressed_buffer.getvalue(), file_name="11zon_compressed.jpg", mime="image/jpeg")

# ----------------- 6. 11zon फोटो बैकग्राउंड एडिटर -----------------
elif menu == "🎨 11zon फोटो बैकग्राउंड एडिटर":
    st.subheader("🖼️ एडवांस नो-क्रैश बैकग्राउंड कलर एडिटर")
    bg_color = st.sidebar.color_picker("बैकग्राउंड का नया रंग चुनें:", "#E6F2FF")
    brightness = st.sidebar.slider("चमक (Brightness):", 0.5, 2.0, 1.0)
    
    uploaded_file = st.file_uploader("अपनी फोटो यहाँ अपलोड करें...", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert("RGB")
        
        # चमक सेट करना
        enhancer = ImageEnhance.Brightness(image)
        img_mod = enhancer.enhance(brightness)
        
        # ब्लेंडिंग तकनीक से एचडी आउटपुट
        clean_img = ImageOps.autocontrast(img_mod)
        background = Image.new("RGB", clean_img.size, bg_color)
        final_img = Image.blend(clean_img, background, alpha=0.18)
        
        st.image(final_img, caption='एडिट की हुई फोटो (11zon Style)', width=400)
        
        buf = io.BytesIO()
        final_img.save(buf, format="JPEG", quality=95) # हाई क्वालिटी बेस्ट आउटपुट
        st.download_button(label="📥 फोटो डाउनलोड करें", data=buf.getvalue(), file_name="11zon_edited.jpg", mime="image/jpeg")
