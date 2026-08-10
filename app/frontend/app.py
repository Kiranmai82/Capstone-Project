import os
import sys
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if PROJECT_ROOT not in sys.path:
   sys.path.insert(0, PROJECT_ROOT)

import streamlit as st
from app.api.gemini_client import client
from app.services.translation_service import translate_text
from app.config.languages import LANG_MAP
from app.frontend.tabs import text_translate_tab
from app.frontend.tabs import file_upload_tab
from app.frontend.buttons.translate_button import translate_button
from app.frontend.buttons.generate_audio_button import generate_audio
from gtts import gTTS
from app.services.text_to_speech import text_to_speech_conversion


# Initialize session widget keys

if "translate_input_widget_key" not in st.session_state:
    st.session_state.translate_input_widget_key = "translate_input_widget"

if "translated_output_widget_key" not in st.session_state:
    st.session_state.translated_output_widget_key = "translated_output_widget"

if "file_uploader_key" not in st.session_state:
    st.session_state.file_uploader_key = "file_uploader"

# Initialize session state

if "file_uploader_key" not in st.session_state:
   st.session_state.file_uploader_key = "file_uploader_1"

if "audio_file" not in st.session_state:
    st.session_state.audio_file = None

if "save_file" not in st.session_state:
    st.session_state.save_file = None

if "uploaded_file_data" not in st.session_state:
    st.session_state.uploaded_file_data = None

if "text_input_data" not in st.session_state:
    st.session_state.text_input_data = ""

if "translated_output" not in st.session_state:
    st.session_state.translated_output = ""




title = "Translate and Generate Audio"
st.title(title)




# Create a callback to detect tab changes
def clear_tab1_on_tab2_click():
    """Clear tab1 data when user switches to tab2"""
    st.session_state.uploaded_file_data = None


def clear_tab2_on_tab1_click():
    """Clear tab2 data when user switches to tab1"""
    st.session_state.text_input_data = ""


tab1, tab2 = st.tabs(["Upload a File", "Translate Text"])


with tab1:
    if tab1:
       # This block only renders when tab1 is visible
        uploaded_text = file_upload_tab.render()
    if uploaded_text:
        st.session_state.uploaded_file_data = uploaded_text
    else:
        st.session_state.uploaded_file_data = None
    

with tab2:
    
    # This block only renders when tab2 is visible
    plain_text = text_translate_tab.render()
    

 

# -----------------------------
# Language Dropdown
# -----------------------------

selected_label = st.selectbox("Select output language", list(LANG_MAP.keys()))
selected_code = LANG_MAP[selected_label]

if client is None:
    st.warning(
        "No Gemini API key found. Translation is disabled until you configure GEMINI_API_KEY or add it to Streamlit secrets."
    )


button_horizontal = st.container()
col1, col2, col3 = button_horizontal.columns([1,1,1])

# Initialize session state
if "translate_status" not in st.session_state:
    st.session_state.translate_status = False

if "audio_status" not in st.session_state:
    st.session_state.audio_status = False

# -----------------------------
# TRANSLATE BUTTON (always visible)
# -----------------------------
with col1:
    if st.button("Translate", key="translate_button"):
        with st.spinner("Translating..."):
            translate_button(selected_label, selected_code)
        st.session_state.translate_status = True
        st.session_state.audio_status = False   # reset audio state


# -----------------------------
# GENERATE AUDIO BUTTON (visible but disabled until translation)
# -----------------------------
with col2:
    generate_audio_disabled = not st.session_state.translate_status

    if st.button("Generate Audio", key="audio_button", disabled=generate_audio_disabled):
        with st.spinner("Generating audio..."):
            generate_audio(selected_code)
        st.session_state.audio_status = True


# -----------------------------
# DOWNLOAD AUDIO BUTTON (visible but disabled until audio exists)
# -----------------------------
with col3:
    download_disabled = not st.session_state.audio_status

    audio_bytes = st.session_state.get("audio_file")

    st.download_button(
        label="Download Audio",
        data=audio_bytes if audio_bytes else "",
        file_name="output_audio.mp3",
        mime="audio/mp3",
        disabled=download_disabled
    )


# -----------------------------
# DISPLAY TRANSLATED OUTPUT
# -----------------------------
if st.session_state.get("translated_output"):
    st.subheader(f"Translated Output in ({selected_label})")
    st.text_area(
        "Translated Output",
        value=st.session_state.translated_output,
        height=300,
        key="translated_output_widget"
    )




 

    
