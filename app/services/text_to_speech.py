from gtts import gTTS 
from app.config.languages import LANG_MAP
import streamlit as st
#from app.frontend.app import selected_label, selected_code
from io import BytesIO

# Create a tts object based on the translated text and selected language code

def text_to_speech_conversion(translated_text, selected_code):
    if not translated_text:
        st.warning("No translated text available for audio generation.")
        return None
    try:
        # Create a tts object based on the translated text and selected language code
        tts = gTTS(
            text=translated_text,
            lang=selected_code
        )
        audio_bytes = BytesIO()
        tts.write_to_fp(audio_bytes)
        audio_bytes.seek(0)
        return audio_bytes

        
    except Exception as e:
        st.error(f"Error occurred while generating audio: {e}")
        return None
