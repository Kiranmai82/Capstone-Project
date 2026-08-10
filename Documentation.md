# Technical Documentation — Translator + Audio Generator

This document explains the internal architecture, data flow, module responsibilities, and development considerations for the Translator + Audio Generator application.

---

## 1. Purpose

The application provides multilingual translation and text‑to‑speech functionality through a Streamlit interface.  
It supports text input, file uploads, translation using the Gemini API, audio generation using gTTS, and MP3 download.

---

## 2. System Architecture

Streamlit UI (tabs)
↓
Button Handlers
↓
Backend Services
↓
Gemini API / File Parsers


### Architecture Characteristics
- UI triggers backend operations  
- Buttons contain workflow logic  
- Session state stores intermediate results  
- Services handle translation, TTS, and file extraction  

---
## 3.  Internal Architecture

**UI Layer (tabs/)**
- Handles user input
- Displays text, translations, and audio
- Calls button handlers

**Button Logic (buttons/)**
1. translate_button.py
- Reads text
- Calls translation service
- Stores translated text

2. generate_audio_button.py
- Reads translated text
- Calls TTS service
- Stores audio bytes

**Backend Services (services/)**
1. translation_service.py → Gemini translation
2. text_to_speech.py → TTS (gTTS)
3. text_extraction_service.py → PDF/CSV/Excel parsing

**API Layer (api/)**
gemini_client.py
- Tries to load the Gemini API key
   - First from environment variables
   - Then from Streamlit secrets
- Returns the key if found
- Creates a Gemini client

**Utilities (utils/)**
PDF, Excel, CSV parsing helpers

## 4. Module Responsibilities

### **app.py**
- Initializes Streamlit  
- Renders tabs  
- Manages session state  

---

### **tabs/**
#### `text_translate_tab.py`
- Accepts manual text input  
- Sends text for translation  

#### `file_upload_tab.py`
- Handles file uploads  
- Extracts text from PDF/CSV/Excel  
- Sends extracted text for translation  

---

### **buttons/**
#### `translate_button.py`
- Reads text from session state  
- Calls translation service  
- Stores translated output  

#### `generate_audio_button.py`
- Reads translated text  
- Calls gTTS  
- Stores MP3 audio bytes  

---

### **services/**
#### `translation_service.py`
- Sends text to Gemini API  
- Receives translated output  

#### `text_to_speech.py`
- Converts text to speech using **gTTS**  
- Returns MP3 audio bytes  

#### `text_extraction_service.py`
- Detects file type  
- Extracts text using appropriate utility  

#### `gemini_client.py`
- Initializes Gemini API client  
- Handles authentication  

---

### **utils/**
- `pdf_utils.py` → PDF parsing  
- `excel_utils.py` → Excel parsing  
- `csv_utils.py` → CSV parsing  

---

## 5. Data Flow

### **A. Text Translation Flow**
```
User enters text
↓
text_translate_tab.py
↓
translate_button.py
↓
translation_service.py → Gemini API
↓
Translated text stored in st.session_state.translated_output
↓
Displayed in UI
```

---

### **B. File Upload Flow**
```
User uploads file
↓
file_upload_tab.py
↓
text_extraction_service.py
↓
utils (PDF/CSV/Excel parsers)
↓
Extracted text stored in session state
↓
translate_button.py → translation_service.py
↓
Translated text displayed in UI
```
---

### **C. Audio Generation Flow**
```
User clicks Generate Audio
↓
generate_audio_button.py
↓
text_to_speech.py → gTTS
↓
MP3 audio stored in st.session_state.audio_file
↓
Download button provides MP3 file
```

---
```python
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=f"Translate to {selected_label}: {text}"
)
```
## Notes
- Only translation uses Gemini API

- Text‑to‑speech uses gTTS, not Gemini

## 6. Considerations
**API Key Security**
- Use environment variables

- Never commit API keys to GitHub

**File Size**
- Large PDFs/Excels may slow extraction

- Streamlit has upload size limits

**Language Support**
- Translation quality depends on Gemini

- gTTS supports many languages but not all

**Internet Requirement**

Gemini API and gTTS both require internet access

## 7. Limitations
- No offline translation or TTS

- MP3 only

- Scanned PDFs may fail

- No batch translation

- CSV/Excel must contain readable text

## 8. Challenges Faced
**Handling Multiple File Types**
- Different parsing logic required for:
PDFs
CSVs
Excel files

**Managing Session State**
- Needed careful handling to store:
extracted text
translated text
audio bytes
prevent overwriting between tabs

**Managing Streamlit Widget Keys**
- Multiple tabs required unique keys
- Prevented widget conflicts
- Ensured stable UI behavior

**Gemini API Response Handling**
Ensured:
- correct prompt formatting
- safe error handling
- stable client initialization

**Text‑to‑Speech Integration (gTTS)**
Handled:
- MP3 generation
- Temporary file storage
- Browser‑safe downloads





