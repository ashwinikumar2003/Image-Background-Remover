import streamlit as st
from rembg import remove
import cv2

st.title(":rainbow[Image Background Remover]")
st.sidebar.header('Add Your Image Here')
uploaded = st.sidebar.file_uploader("Add your file here...", label_visibility="hidden")
if uploaded is not None:
    inp = cv2.imread(uploaded)
    # img_byte_arr = io.BytesIO()
    # inp.save(img_byte_arr, format='PNG')
    # img_byte_arr = img_byte_arr.getvalue()
    # output = remove(img_byte_arr)
    output=remove(inp)
    col1, col2 = st.columns(2)
    col1.image(uploaded,use_column_width=True,caption="with background")
    col2.image(output, use_column_width=True, caption="without background")
    st.download_button('Download', data=output, file_name="untitled.png", mime="image/png")
else:
    st.header(":blue[drop an image and see the magic!]")
    inp = cv2.imread(uploaded)
    output = remove(inp)
    col1, col2 = st.columns(2)
    col1.image(uploaded,use_column_width=True,caption="with background")
    col2.image(output, use_column_width=True, caption="without background")
