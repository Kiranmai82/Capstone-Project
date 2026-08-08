import streamlit as st
from app.services.text_to_speech import text_to_speech_conversion

def generate_audio(selected_code):
    
    if not st.session_state.translated_output:
        st.warning("Please translate text first.")
        return
    
    audio_bytes = text_to_speech_conversion(st.session_state.translated_output, selected_code)

    if audio_bytes is None:
        st.error("Audio generation failed.")
        return
    
    st.session_state.audio_file = audio_bytes
    st.audio(audio_bytes, format="audio/mp3")

