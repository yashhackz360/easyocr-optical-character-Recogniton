import streamlit as st
import easyocr
from PIL import Image
import numpy as np

# Initialize OCR Reader
reader = easyocr.Reader(['en'])  # 'en' for English

# Streamlit UI
st.title("📄  OCR Implemetation with EasyOCR")
st.write("Upload an image to extract text")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Convert image to NumPy array for EasyOCR
    img_array = np.array(image)

    # Extract text
    with st.spinner("Extracting text..."):
        results = reader.readtext(img_array)
    
    # Display results
    st.subheader("Extracted Text:")
    extracted_text = "\n".join([text for _, text, _ in results])
    st.text_area("Detected Text", extracted_text, height=200)

    # Download button for text
    if extracted_text:
        st.download_button("Download Extracted Text", extracted_text, file_name="extracted_text.txt")

