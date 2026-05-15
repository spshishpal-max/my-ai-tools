import streamlit as st
from PIL import Image
from rembg import remove, new_session
import io

st.set_page_config(page_title="AI Multi-Color BG Remover")
st.title("🎨 AI Background Changer")
st.write("बैकग्राउंड हटाएँ और अपनी पसंद का रंग चुनें।")

st.sidebar.header("Settings")
bg_color = st.sidebar.color_picker("बैकग्राउंड का रंग चुनें", "#FFFFFF")

# हेक्स कलर को RGB फॉर्मेट में बदलना
bg_rgb = tuple(int(bg_color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))

# हल्का AI मॉडल सेशन बनाना ताकि सर्वर पर लोड न पड़े
@st.cache_resource
def get_rembg_session():
    # 'u2netp' एक छोटा और तेज़ AI मॉडल है जो फ्री सर्वर पर अटकता नहीं है
  return new_session("u2net")

uploaded_file = st.file_uploader("अपनी फोटो अपलोड करें...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Original Image', use_container_width=True)
    
    st.write("AI बैकग्राउंड हटा रहा है... इसमें 10-15 सेकंड लग सकते हैं ⏳")
    
    try:
        session = get_rembg_session()
        # AI की मदद से बैकग्राउंड हटाना (पारदर्शी बनाना)
        output_image = remove(image, session=session)
        
        # नया रंगीन बैकग्राउंड बनाना
        background = Image.new("RGBA", output_image.size, bg_rgb + (255,))
        # पारदर्शी फोटो को नए रंग के ऊपर चिपकाना
        final_img = Image.alpha_composite(background, output_image.convert("RGBA")).convert("RGB")
        
        st.success("काम पूरा हुआ!")
        st.image(final_img, caption='New Background', use_container_width=True)
        
        # डाउनलोड बटन
        buf = io.BytesIO()
        final_img.save(buf, format="JPEG")
        st.download_button(label="Download Edited Image", data=buf.getvalue(), file_name="ai_edited.jpg", mime="image/jpeg")
        
    except Exception as e:
        st.error("सर्वर पर लोड अधिक है। कृपया 'Reboot' करके दोबारा कोशिश करें।")
# Streamlit के एडमिन बटन और मेनू को छिपाने के लिए CSS
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            .viewerBadge_container__1QS1Z {display: none !important;}
            button[title="View source code"] {display: none !important;}
            div[data-testid="stStatusWidget"] {display: none !important;}
            .stAppDeployButton {display: none !important;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
