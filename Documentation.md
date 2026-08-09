## Technical Documentation — Translator + Audio Generator

1. Purpose
This application provides multilingual translation and text‑to‑speech functionality through a Streamlit interface. It supports text input, file uploads, translation, audio generation, and MP3 download.

2. System Architecture
Code
Streamlit UI (tabs)
        ↓
Button handlers
        ↓
Backend services
        ↓
Gemini API / File parsers

Characteristics:
- UI triggers backend operations

- Buttons contain workflow logic

- Session state stores intermediate results

- Services handle translation, TTS, and extraction

3. Module Responsibilities
app.py
- Initializes Streamlit

- Renders tabs

- Manages session state

tabs/
- text_translate_tab.py → text input + translation

- file_upload_tab.py → file upload + extraction + translation

buttons/
- translate_button.py → calls translation service

- generate_audio_button.py → calls TTS service

services/
- translation_service.py → Gemini translation

- text_to_speech.py → TTS (gTTS or Gemini)

- text_extraction_service.py → PDF/CSV/Excel parsing

- gemini_client.py → API client setup

utils/
PDF, Excel, CSV parsing helpers

4. How data flows

1. User selects a tab in app.py
   - file_upload_tab.py uploads and extracts text
   - text_translate_tab.py collects manual text
2. User picks a language from languages.py
3. translate_button.py calls translation_service.py
   - uses gemini_client.py
4. Translated text is stored in st.session_state.translated_output
5. generate_audio_button.py calls text_to_speech.py
6. Resulting MP3 audio is stored in st.session_state.audio_file
7. Download button serves the generated audio


5. Gemini API Usage
Translation
python
response = client.models.generate_content(
    model="gemini-1.5-flash",
    contents=f"Translate to {selected_label}: {text}"
)

6. Considerations
API Key Security
Use environment variables

Never commit keys to GitHub

**File Size**
Large PDFs/Excels may slow processing

**Language Support**
Depends on Gemini model

TTS may not support all languages

**Internet Requirement**
Gemini API requires connectivity

7. Limitations
- No offline translation/TTS

- No batch processing

- MP3 only

- Scanned PDFs may fail

- CSV/Excel must contain readable text

8. Challenges Faced
**Handling Multiple File Types**
- Different parsing logic required for PDFs, CSVs, and Excel.

**Managing Session State**
Needed to store:
- extracted text
- translated text
- audio bytes

**Managing Streamlit Widget Keys**
- Multiple tabs required unique keys
- Prevented widget conflicts

**Gemini API Response Handling**
Ensured:
- correct prompt formatting
- safe error handling
- stable client initialization

