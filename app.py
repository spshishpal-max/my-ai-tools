import streamlit as st
from pdf2image import convert_from_bytes
from PIL import Image
import io

# हैडर
st.markdown("<h1 style='text-align: center;'>Compress PDF</h1>", unsafe_allow_html=True)

# 1. स्लाइडर लॉजिक (11zon की तरह: ज्यादा % = ज्यादा कंप्रेशन/छोटा साइज)
col_slider, col_val, col_btn = st.columns([5, 2, 3])
with col_slider:
    compression_percentage = st.slider("Compression Level ⓘ", min_value=10, max_value=95, value=90, step=5)
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
        with st.spinner("Processing High Compression..."):
            try:
                # PDF के सभी पेजों को इमेज में बदलना
                images = convert_from_bytes(file_bytes)
                
                # 11zon की तरह क्वालिटी की गणना (अगर यूजर ने 90% चुना है, तो असली इमेज क्वालिटी 10% बचेगी)
                actual_quality = 100 - compression_percentage
                
                output_pdf_pages = []
                
                for img in images:
                    # इमेज का साइज (Resolution) भी थोड़ा छोटा करना ताकि साइज बहुत कम हो जाए
                    if compression_percentage >= 80:
                        img.thumbnail((1200, 1200), Image.Resampling.LANCZOS)
                    
                    # इमेज को कम क्वालिटी पर कंप्रेस करके बफर में सेव करना
                    img_buffer = io.BytesIO()
                    img.save(img_buffer, format="JPEG", quality=actual_quality, optimize=True)
                    img_buffer.seek(0)
                    
                    # वापस इमेज ऑब्जेक्ट बनाना ताकि PDF में कनवर्ट हो सके
                    output_pdf_pages.append(Image.open(img_buffer))
                
                # सभी कंप्रेस पेजों को मिलाकर नई PDF बनाना
                if output_pdf_pages:
                    pdf_output_buffer = io.BytesIO()
                    output_pdf_pages[0].save(
                        pdf_output_buffer,
                        format="PDF",
                        save_all=True,
                        append_images=output_pdf_pages[1:],
                        optimize=True
                    )
                    compressed_bytes = pdf_output_buffer.getvalue()
                    
                    final_size_mb = len(compressed_bytes) / (1024 * 1024)
                    
                    # अगर साइज MB से छोटा है तो KB में दिखाना
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
                    st.success("PDF Compressed Successfully!")
            
            except Exception as e:
                st.error(f"Error in compression: {e}")
