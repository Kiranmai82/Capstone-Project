import streamlit as st
from app.services.text_extraction_service import extract_text_from_file


def render():
    file_text = None

    uploaded_file = st.file_uploader(
        "Upload a file",
        key=st.session_state.file_uploader_key,
        type=["txt", "pdf", "xls", "csv"],
        accept_multiple_files=False
    )

    if uploaded_file:
        file_text = extract_text_from_file(uploaded_file)
       
    return file_text
