import streamlit as st

def footer_home():
    logo_url = "http://i.ibb.co/YTYGn5qV/Tanmay.png"

    st.markdown(f"""
        <div style="margin-top:2rem; display: flex; gap:6px; justify-content:center;items-align:center">
        <P style="font-weight:bold; color:white"> Created By </p>
        <img src="{logo_url}" style="max-height:25px" />
        </div>
    """
    , unsafe_allow_html=True)