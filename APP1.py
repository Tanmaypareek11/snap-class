import streamlit as st

st.write("URL:", st.secrets["SUPABASE_URL"])
st.write("KEY:", st.secrets["SUPABASE_KEY"][:10])