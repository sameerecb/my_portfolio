import streamlit as st
import pandas

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
content2 = """Below you can find some of the apps, I have built in python. Feel free to contact me.
           I am 14 years of experience software engineer."""
st.write(content2)

col3, empty_col,  col4 = st.columns([1.5, .5, 1.5])

df = pandas.read_csv("data.csv")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        # st.write("[Source Code](https://pythonhow.com)") Static way to provide a link
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
