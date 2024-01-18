import streamlit as st
import pytesseract
from PIL import Image

st.title('Reading Texts From an Image')
image = st.file_uploader('Upload your image', type=['png', 'jpeg', 'jpg'])
if image is None:
    st.write('no file here:')
else:
    img = Image.open(image)
    st.image(img, use_column_width=True)
    if st.button('Read this Image'):
        result = pytesseract.image_to_string(img)
        st.success(result)