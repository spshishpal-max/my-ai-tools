import streamlit as st
from pypdf import PdfReader, PdfWriter
from PIL import Image
import io

# 11zon जैसा हैडर और स्टाइल
st.markdown("<h1 style='text-align: center;'>Compress PDF</h1>", unsafe_allow_html=True)

# 1. कंप्रेशन लेवल कंट्रोलर बॉक्स (स्लाइडर)
col_slider, col_val, col_btn = st.columns([6, 2, 4])
with col_slider:
    compression_level = st.slider("Compression Level ⓘ", min_value=10, max_value=100, value=60, step=5)
with col_val:
    st.markdown(f"<div style='border:1px solid #ccc; padding:6px 12px; border-radius:4px; text-align:center; margin-top:28px;'>{compression_level} %</div>", unsafe_allow_html=True)

# 2. फाइल अपलोडर
uploaded_file = st.file_uploader("Select PDF / Add PDF Files", type=["pdf"], label_visibility="collapsed")

if uploaded_file is not None:
    file_bytes = uploaded_file.getvalue()
    initial_size_mb = len(file_bytes) / (1024 * 1024) # MB में
    
    st.write("")
    
    # 11zon जैसा कार्ड लेआउट बनाना
    card_col1, card_col2 = st.columns([4, 6])
    
    with card_col1:
        st.markdown(f"""
        <div style='border:1px solid #E2E8F0; padding:15px; border-radius:8px; text-align:center; background:#f8fafc; position:relative;'>
            <div style='font-size:12px; color:#64748B; text-align:left;'>{uploaded_file.name[:8]}... &nbsp;&nbsp;&nbsp; {initial_size_mb:.2f} MB</div>
            <div style='margin:15px 0; font-size:40px;'>📄</div>
        </div>
        """, unsafe_allow_html=True)
        
    with col_btn:
        # कंप्रेशन बटन जो स्लाइडर की वैल्यू पर काम करेगा
        st.write("") # स्पेसिंग के लिए
        compress_clicked = st.button("Compress", type="primary", use_container_width=True)

    if compress_clicked:
        with st.spinner("Processing..."):
            try:
                reader = PdfReader(io.BytesIO(file_bytes))
                writer = PdfWriter()
                
                # हर पेज को लूप करके उसमें मौजूद इमेज को स्लाइडर क्वालिटी के हिसाब से छोटा करना
                for page in reader.pages:
                    writer.add_page(page)
                    
                    # इमेज कंप्रेशन लॉजिक (क्वालिटी लेवल स्लाइडर से आ रहा है)
                    for img_info in page.images:
                        try:
                            img_obj = Image.open(io.BytesIO(img_info.data))
                            
                            # इमेज फॉर्मेट चेक करना
                            img_format = img_obj.format if img_obj.format else "JPEG"
                            
                            # नई बाइट्स में स्लाइडर की क्वालिटी के साथ सेव करना
                            out_img_bytes = io.BytesIO()
                            img_obj.save(out_img_bytes, format=img_format, quality=int(compression_level), optimize=True)
                            
                            # PDF में पुरानी इमेज को नई कंप्रेस इमेज से बदल देना
                            img_info.replace(img_info.image, quality=int(compression_level))
                        except Exception:
                            continue # अगर किसी इमेज में दिक्कत हो तो स्किप करें
                
                # स्ट्रक्चरल डुप्लीकेट्स हटाकर साइज और छोटा करना
                writer.compress_identical_objects(remove_duplicates=True, remove_unreferenced=True)
                
                # फाइल राइट करना
                compressed_buffer = io.BytesIO()
                writer.write(compressed_buffer)
                compressed_bytes = compressed_buffer.getvalue()
                
                final_size_kb = len(compressed_bytes) / 1024
                final_size_mb = final_size_kb / 1024
                
                # डाउनलोड बटन और न्यू साइज कार्ड के अंदर दिखाना
                with card_col1:
                    st.markdown(f"<div style='font-weight:bold; font-size:14px; margin-top:5px; color:#1E293B;'>New Size: {final_size_mb:.2f} MB</div>", unsafe_allow_html=True)
                    st.download_button(
                        label="Download",
                        data=compressed_bytes,
                        file_name=f"compressed_{uploaded_file.name}",
                        mime="application/pdf",
                        use_container_width=True
                    )
                st.success("PDF Compressed Successfully!")
                
            except Exception as e:
                st.error(f"Error in compression: {e}")
