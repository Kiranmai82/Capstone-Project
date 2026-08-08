import streamlit as st
from app.api.gemini_client import client
from app.services.translation_service import translate_text
from app.config.languages import LANG_MAP

def translate_button(selected_label, selected_code):
    if client is None:
        st.error("Translation is unavailable because no Gemini API key is configured.")
        return
    
        # Use the persistent session state data
    user_input = (
        st.session_state.get("text_input_data")
        or st.session_state.get("uploaded_file_data")
    )
        
    if not user_input:
        st.warning("Please enter text or upload a file to translate.")
        return
    
    try:
            
        response = translate_text(user_input, selected_label, selected_code)
        st.session_state.translated_output = response
        
    
    except RuntimeError as err:
        st.error(str(err))
    except Exception as err:
        st.error(f"Translation failed: {err}") 