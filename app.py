import streamlit as st
from rembg import remove
from PIL import Image
import io

st.set_page_config(page_title="AI Multi-Color BG Remover")
st.title("🎨 AI Background Changer")
st.write("बैकग्राउंड हटाएँ और अपनी पसंद का रंग चुनें!")

# साइडबार में कलर चुनने का ऑप्शन
st.sidebar.header("Settings")
bg_color = st.sidebar.color_picker("बैकग्राउंड का रंग चुनें", "#FFFFFF") # डिफ़ॉल्ट सफ़ेद

uploaded_file = st.file_uploader("अपनी फोटो अपलोड करें...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Original Image', use_container_width=True)
    
    st.write("जादू हो रहा है... ⏳")
    
    # 1. बैकग्राउंड हटाना
    no_bg_img = remove(image)
    
    # 2. नया कलर बैकग्राउंड बनाना
    # फोटो को RGBA मोड में बदलना ताकि ट्रांसपेरेंसी बनी रहे
    no_bg_img = no_bg_img.convert("RGBA")
    
    # नया बैकग्राउंड लेयर बनाना जो यूजर के चुने रंग का हो
    new_bg = Image.new("RGBA", no_bg_img.size, bg_color)
    
    # दोनों को मिलाना (नया कलर नीचे, फोटो ऊपर)
    combined = Image.alpha_composite(new_bg, no_bg_img)
    final_img = combined.convert("RGB") # सेव करने के लिए RGB में बदलना
    
    st.success("काम पूरा हुआ!")
    st.image(final_img, caption='New Background', use_container_width=True)
    
    # डाउनलोड बटन
    buf = io.BytesIO()
    final_img.save(buf, format="JPEG")
    st.download_button(label="Download Edited Image", data=buf.getvalue(), file_name="ai_edited.jpg", mime="image/jpeg")

st.info("प्रो टिप: साइडबार (बाएँ तरफ) से रंग बदलें और रिजल्ट तुरंत देखें!")
