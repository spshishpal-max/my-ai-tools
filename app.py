import streamlit as st
import streamlit.components.v1 as components

st.markdown("<h1 style='text-align: center; color: #EF4444;'>11zon Style PDF Compressor</h1>", unsafe_allow_html=True)
st.write("यह एडवांस्ड ब्राउज़र कंप्रेसर है, जो इमेज रेजोल्यूशन को डाउन करके साइज़ को सचमुच कम करेगा।")

# नया जावास्क्रिप्ट और HTML कोड जो सीधे ब्राउज़र में इमेज पिक्सल्स को छोटा करेगा
html_code = """
<!DOCTYPE html>
<html>
<head>
    <script src="https://cloudflare.com"></script>
    <script src="https://cloudflare.com"></script>
    <style>
        body { font-family: sans-serif; background: #f8fafc; text-align: center; padding: 10px; }
        .box { border: 2px dashed #cbd5e1; padding: 20px; background: white; border-radius: 8px; max-width: 500px; margin: auto; }
        .btn { background: #ef4444; color: white; border: none; padding: 10px 20px; font-size: 16px; border-radius: 5px; cursor: pointer; margin-top: 15px; width: 100%; }
        .slider-box { margin: 15px 0; text-align: left; }
        #status { font-weight: bold; margin-top: 15px; color: #1e293b; }
    </style>
</head>
<body>

<div class="box">
    <div class="slider-box">
        <label><b>Compression Level (ज़्यादा % = छोटा साइज़):</b> <span id="level_val">90</span>%</label>
        <input type="range" id="compress_level" min="40" max="98" value="90" style="width:100%;" oninput="document.getElementById('level_val').innerText=this.value">
    </div>

    <input type="file" id="pdf_file" accept=".pdf"><br>
    <button class="btn" onclick="processPDF()">Compress PDF</button>
    
    <div id="status"></div>
    <a id="download_btn" style="display:none;"><button class="btn" style="background:#10b981;">Download Compressed PDF</button></a>
</div>

<script>
    pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://cloudflare.com';

    async function processPDF() {
        const fileInput = document.getElementById('pdf_file');
        const status = document.getElementById('status');
        const downloadBtn = document.getElementById('download_btn');
        
        if (fileInput.files.length === 0) {
            alert('कृपया पहले एक PDF फाइल चुनें!');
            return;
        }

        status.innerText = "फाइल प्रोसेसिंग शुरू हो रही है...";
        const file = fileInput.files[0];
        const arrayBuffer = await file.arrayBuffer();
        
        const pdf = await pdfjsLib.getDocument({data: arrayBuffer}).promise;
        const { jsPDF } = window.jspdf;
        const doc = new jsPDF('p', 'mm', 'a4');
        
        const compressionLevel = parseInt(document.getElementById('compress_level').value);
        
        // साइज़ छोटा करने का असली लॉजिक: ज़्यादा कंप्रेशन पर रेजोल्यूशन (Scale) को घटाना
        let scale = 1.0;
        if (compressionLevel >= 90) scale = 0.6; // पिक्सल्स कम करना
        else if (compressionLevel >= 70) scale = 0.8;
        
        const imageQuality = (100 - compressionLevel) / 100; 

        for (let i = 1; i <= pdf.numPages; i++) {
            status.innerText = `पेज ${i} का साइज़ छोटा किया जा रहा है...`;
            const page = await pdf.getPage(i);
            const viewport = page.getViewport({scale: scale});
            
            const canvas = document.createElement('canvas');
            const context = canvas.getContext('2d');
            canvas.height = viewport.height;
            canvas.width = viewport.width;
            
            await page.render({canvasContext: context, viewport: viewport}).promise;
            
            // यहाँ क्वालिटी और डायमेंशन दोनों कंप्रेस हो रहे हैं
            const imgData = canvas.toDataURL('image/jpeg', imageQuality);
            
            if (i > 1) doc.addPage();
            doc.addImage(imgData, 'JPEG', 0, 0, 210, 297, undefined, 'FAST');
        }

        status.innerText = "फाइनल PDF जनरेट हो रही है...";
        const compressedPdfBlob = doc.output('blob');
        const compressedSizeKB = (compressedPdfBlob.size / 1024).toFixed(2);
        const originalSizeMB = (file.size / (1024 * 1024)).toFixed(2);
        
        if (compressedPdfBlob.size >= file.size && compressionLevel >= 90) {
            status.innerHTML = `<span style='color:red;'>संकेत: यह फाइल पहले से ही अधिकतम कंप्रेस है।</span>`;
        } else {
            status.innerHTML = `🎉 **सफलतापूर्वक कंप्रेस हुआ!**<br>पुराना साइज़: ${originalSizeMB} MB<br>नया साइज़: ${compressedSizeKB} KB`;
        }
        
        const blobUrl = URL.createObjectURL(compressedPdfBlob);
        downloadBtn.href = blobUrl;
        downloadBtn.download = "compressed_" + file.name;
        downloadBtn.style.display = "block";
    }
</script>

</body>
</html>
"""

components.html(html_code, height=420)
