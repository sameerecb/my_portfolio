import streamlit as st
st.header("Contact Me")
with st.form("key=email_form"):
    user_email = st.text_input("Enter your email address")
    message = st.text_area("Enter your message below")
    button = st.form_submit_button("Send")
    if button:
        print("Pressed")