import streamlit as st
import streamlit.components.v1 as components

st.markdown("<h1 style='text-align: center; color: #EF4444;'>11zon Style PDF Compressor</h1>", unsafe_allow_html=True)
st.write("यह जावास्क्रिप्ट पावर्ड कंप्रेसर है, जो बिना किसी एरर के आपकी फाइल का साइज भारी मात्रा में कम करेगा।")

# जावास्क्रिप्ट और HTML कोड का मिश्रण जो सीधे ब्राउज़र में चलेगा
html_code = """
<!DOCTYPE html>
<html>
<head>
    <!-- फ्री PDF और इमेज प्रोसेसिंग लाइब्रेरीज -->
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
        <label><b>Compression Level:</b> <span id="level_val">90</span>%</label>
        <input type="range" id="compress_level" min="50" max="95" value="90" style="width:100%;" oninput="document.getElementById('level_val').innerText=this.value">
    </div>

    <input type="file" id="pdf_file" accept=".pdf"><br>
    <button class="btn" onclick="processPDF()">Compress PDF</button>
    
    <div id="status"></div>
    <a id="download_btn" style="display:none;"><button class="btn" style="background:#10b981;">Download Compressed PDF</button></a>
</div>

<script>
    // pdf.js वर्कर सेटअप
    pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://cloudflare.com';

    async function processPDF() {
        const fileInput = document.getElementById('pdf_file');
        const status = document.getElementById('status');
        const downloadBtn = document.getElementById('download_btn');
        
        if (fileInput.files.length === 0) {
            alert('कृपया पहले एक PDF फाइल चुनें!');
            return;
        }

        status.innerText = "फाइल रीड की जा रही है... (0%)";
        const file = fileInput.files[0];
        const arrayBuffer = await file.arrayBuffer();
        
        const pdf = await pdfjsLib.getDocument({data: arrayBuffer}).promise;
        const { jsPDF } = window.jspdf;
        const doc = new jsPDF('p', 'mm', 'a4');
        
        const compressionLevel = document.getElementById('compress_level').value;
        // अगर 90% चुना है तो इमेज की क्वालिटी केवल 10% (0.1) बचेगी जिससे साइज भारी मात्रा में घटेगा
        const imageQuality = (100 - compressionLevel) / 100; 

        for (let i = 1; i <= pdf.numPages; i++) {
            status.innerText = `पेज ${i} कंप्रेस हो रहा है...`;
            const page = await pdf.getPage(i);
            const viewport = page.getViewport({scale: 1.5}); // रेजोल्यूशन कंट्रोल
            
            const canvas = document.createElement('canvas');
            const context = canvas.getContext('2d');
            canvas.height = viewport.height;
            canvas.width = viewport.width;
            
            await page.render({canvasContext: context, viewport: viewport}).promise;
            
            // असली 11zon कंप्रेशन लॉजिक यहाँ है (इमेज क्वालिटी को सीधे डाउन करना)
            const imgData = canvas.toDataURL('image/jpeg', imageQuality);
            
            if (i > 1) doc.addPage();
            doc.addImage(imgData, 'JPEG', 0, 0, 210, 297, undefined, 'FAST');
        }

        status.innerText = "PDF तैयार की जा रही है...";
        const compressedPdfBlob = doc.output('blob');
        const compressedSize = (compressedPdfBlob.size / (1024 * 1024)).toFixed(2);
        
        status.innerHTML = `🎉 सफलतापूर्वक कंप्रेस हुआ!<br>पुराना साइज: ${(file.size/(1024*1024)).toFixed(2)} MB<br>नया साइज: ${compressedSize} MB`;
        
        const blobUrl = URL.createObjectURL(compressedPdfBlob);
        downloadBtn.href = blobUrl;
        downloadBtn.download = "compressed_" + file.name;
        downloadBtn.style.display = "block";
    }
</script>

</body>
</html>
"""

# Streamlit में HTML कंपोनेंट को रेंडर करना
components.html(html_code, height=400)
