import streamlit as st
from pypdf import PdfReader, PdfWriter
from PIL import Image
import io

# हैडर
st.markdown("<h1 style='text-align: center;'>Compress PDF</h1>", unsafe_allow_html=True)

# 1. 11zon स्टाइल स्लाइडर (ज्यादा % = ज्यादा कंप्रेशन/छोटा साइज)
col_slider, col_val, col_btn = st.columns([5, 2, 3])
with col_slider:
    compression_percentage = st.slider("Compression Level ⓘ", min_value=10, max_value=95, value=60, step=5)
with col_val:
    st.markdown(f"<div style='border:1px solid #ccc; padding:6px 12px; border-radius:4px; text-align:center; margin-top:28px;'>{compression_percentage} %</div>", unsafe_allow_html=True)

# 2. फाइल अपलोडर
uploaded_file = st.file_uploader("Select PDF Files", type=["pdf"], label_visibility="collapsed")

if uploaded_file is not None:
    file_bytes = uploaded_file.getvalue()
    initial_size_mb = len(file_bytes) / (1024 * 1024)
    
    st.write("")
    card_col1, card_col2 = st.columns(2)
    
    with card_col1:
        st.markdown(f"""
        <div style='border:1px solid #E2E8F0; padding:15px; border-radius:8px; text-align:center; background:#f8fafc;'>
            <div style='font-size:12px; color:#64748B; text-align:left;'>{uploaded_file.name[:10]}... &nbsp;&nbsp;&nbsp; {initial_size_mb:.2f} MB</div>
            <div style='margin:15px 0; font-size:40px;'>📄</div>
        </div>
        """, unsafe_allow_html=True)
        
    with col_btn:
        st.write("") 
        compress_clicked = st.button("Compress", type="primary", use_container_width=True)

    if compress_clicked:
        with st.spinner("Compressing..."):
            try:
                reader = PdfReader(io.BytesIO(file_bytes))
                writer = PdfWriter()
                
                # यूजर के स्लाइडर के हिसाब से क्वालिटी तय करना (90% कंप्रेशन = 10% क्वालिटी)
                target_quality = 100 - compression_percentage
                
                for page in reader.pages:
                    # इमेज की क्वालिटी को बाइट लेवल पर छोटा करना
                    for img_file in page.images:
                        try:
                            img = Image.open(io.BytesIO(img_file.data))
                            img_format = img.format if img.format else "JPEG"
                            
                            # अगर यूजर बहुत ज्यादा कंप्रेस करना चाहता है, तो इमेज का रेजोल्यूशन आधा कर दें
                            if compression_percentage >= 70:
                                img.thumbnail((img.width // 2, img.height // 2))
                                
                            img_buffer = io.BytesIO()
                            img.save(img_buffer, format="JPEG", quality=int(target_quality), optimize=True)
                            img_file.replace(img, quality=int(target_quality))
                        except:
                            continue
                    
                    writer.add_page(page)
                
                # फालतू डुप्लीकेट डेटा हटाना
                writer.compress_identical_objects(remove_duplicates=True, remove_unreferenced=True)
                
                # फाइनल फाइल जनरेट करना
                pdf_output_buffer = io.BytesIO()
                writer.write(pdf_output_buffer)
                compressed_bytes = pdf_output_buffer.getvalue()
                
                final_size_mb = len(compressed_bytes) / (1024 * 1024)
                size_text = f"{final_size_mb * 1024:.2f} KB" if final_size_mb < 1 else f"{final_size_mb:.2f} MB"
                
                with card_col1:
                    st.markdown(f"<div style='font-weight:bold; font-size:14px; margin-top:5px; color:#1E293B; text-align:center;'>New Size: {size_text}</div>", unsafe_allow_html=True)
                    st.download_button(
                        label="Download",
                        data=compressed_bytes,
                        file_name=f"compressed_{uploaded_file.name}",
                        mime="application/pdf",
                        use_container_width=True
                    )
                st.success("Compressed Successfully!")
            except Exception as e:
                st.error(f"Error: {e}")
