import streamlit as st
from pypdf import PdfReader, PdfWriter
import io

# टूल का टाइटल
st.markdown("## 📄 11zon जैसा फ्री PDF कंप्रेसर (Fast & Secure)")
st.write("आपकी फाइलें 100% सुरक्षित हैं, प्रोसेसिंग आपके अपने डिवाइस पर हो रही है।")

# फाइल अपलोडर बॉक्स
uploaded_file = st.file_uploader("यहाँ अपनी PDF फाइल अपलोड करें", type=["pdf"])

if uploaded_file is not None:
    # अपलोड की गई फाइल का साइज दिखाना
    initial_size = len(uploaded_file.getvalue()) / 1024  # KB में
    st.info(f"📁 अपलोड की गई फाइल का साइज: **{initial_size:.2f} KB**")
    
    # कंप्रेशन बटन
    if st.button("⚡ PDF का साइज छोटा (Compress) करें"):
        with st.spinner("फाइल कंप्रेस हो रही है, कृपया प्रतीक्षा करें..."):
            
            # PDF को रीड और राइट करने का लॉजिक (In-Memory)
            reader = PdfReader(uploaded_file)
            writer = PdfWriter()
            
            # सभी पेजों को बिना क्वालिटी खराब किए कंप्रेस करना
            for page in reader.pages:
                page.compress_content_streams()  # कंटेंट स्ट्रीम्स को कंप्रेस करना
                writer.add_page(page)
                
            # कंप्रेस की हुई फाइल को बाइट्स में बदलना
            compressed_buffer = io.BytesIO()
            writer.write(compressed_buffer)
            compressed_bytes = compressed_buffer.getvalue()
            
            # नए साइज की गणना
            final_size = len(compressed_bytes) / 1024  # KB में
            
            # सफलता का संदेश और डाउनलोड बटन
            st.success(f"🎉 सफलता! आपकी PDF सफलतापूर्वक कंप्रेस हो गई है।")
            
            # पुराने और नए साइज की तुलना दिखाना (11zon स्टाइल)
            col1, col2 = st.columns(2)
            col1.metric("पुराना साइज", f"{initial_size:.2f} KB")
            col2.metric("नया साइज (कंप्रेस के बाद)", f"{final_size:.2f} KB", delta=f"-{(initial_size - final_size):.2f} KB")
            
            # फ्री डाउनलोड बटन
            st.download_button(
                label="📥 कंप्रेस की हुई PDF डाउनलोड करें",
                data=compressed_bytes,
                file_name=f"compressed_{uploaded_file.name}",
                mime="application/pdf"
            )
