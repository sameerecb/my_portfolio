import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Sameer Bansal")
    content = """ Hi, My name is Sameer Bansal. 
    I am a solution architect and working on SAP HANA Projects.
    I have worked in multiple organisation and with many clients
    to support their infrastructure hosted on cloud as well on prim. 
     I currently work on SAP HANA solution for different hardware."""
    st.write(content)
    st.info(content)  # For different appearance

