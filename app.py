import streamlit as st

st.title("🧠 Resume Skill Extractor")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

if uploaded_file:
    st.write("File upload successfully ✅")