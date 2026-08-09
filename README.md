# Capstone-Project
Edureka Capstone Project

# Translator + Audio Generator

A Streamlit application that translates text or uploaded documents into another language and generates spoken audio in MP3 format.

## Project Overview

This app allows users to:
- enter text manually,
- upload supported files (`txt`, `pdf`, `csv`, `xls`),
- translate the text to a selected target language,
- generate spoken audio from the translated text,
- download the resulting MP3 audio.

## Features

- Translate text typed directly into the app
- Extract and translate text from uploaded files
- Generate audio from translated text using `gTTS`
- Download generated audio as an MP3 file
- Support for multiple output languages

## Supported Languages

- English
- Spanish
- French
- German
- Hindi
- Telugu
- Tamil
- Chinese
- Japanese
- Korean

## Supported File Types

- `txt`
- `pdf`
- `csv`
- `xls`

## Prerequisites

- Python 3.8 or higher
- `pip`

## Installation

1. Open a terminal in the project folder:
   
   cd "Capstone_Project"

2. Create and activate a virtual environment:
    Windows:

    python -m venv .venv
    .venv\Scripts\activate

    macOS/Linux:

    python -m venv .venv
    source .venv/bin/activate

3. Install the dependencies:

   pip install -r requirements.txt


## Setting Up the Gemini API Key

This application requires a Google Gemini API key to perform translation and text‑to‑speech operations.

Step 1 — Get Your API Key
Go to: https://ai.google.dev

Sign in with your Google account

Create a new API key

Copy the key

Step 2 -- Set your Gemini API key as an environment variable:

For Windows (PowerShell)

setx GEMINI_API_KEY "your_api_key_here"

For macOS / Linux

export GEMINI_API_KEY="your_api_key_here"

If you use Streamlit secrets, you can also configure GEMINI_API_KEY there.  

Step 3 -- Verify the Key
The app checks for the API key at startup.
If the key is missing or invalid, you will see an error message in the UI.

## Running the App

- Start the Streamlit application using below command in the terminal:

**streamlit run app/frontend/app.py**

- Confirm the UI Loads
  You should see:

  Text translation tab

  File upload tab
  
  Language dropdown

  Translate button

  Generate audio button

  Download audio button

## Usage

1. Open the Streamlit app in your browser.

2. Choose one tab:
   - **Upload a File** to translate text from a file.
   - **Translate Text** to enter text manually.

3. Select the target output language.

4. Click **Translate**.

5. After translation completes, click **Generate Audio**.

6. Download the MP3 audio by clicking **Download Audio**.


## Project Structure
```  
Capstone_Project/
│
├── app.py                         # Main Streamlit application
│
├── tabs/                          # UI tabs for Streamlit
│   ├── file_upload_tab.py         # File upload + extraction + translation UI
│   └── text_translate_tab.py      # Text input + translation UI
│
├── buttons/                       # Button logic (translate + audio)
│   ├── translate_button.py
│   └── generate_audio_button.py
│
├── services/                      # Backend logic (no Streamlit)
│   ├── translation_service.py     # Gemini translation logic
│   ├── text_to_speech.py          # gTTS audio generation
│   ├── text_extraction_service.py # PDF/CSV/Excel extraction
│   └── gemini_client.py           # Gemini API client setup
│
├── utils/                         # Helper utilities
│   ├── pdf_utils.py               # PDF parsing helpers
│   ├── excel_utils.py             # Excel parsing helpers
│   └── csv_utils.py               # CSV parsing helpers
│
├── languages.py                   # Language code mappings
│
├── requirements.txt               # Python dependencies
└── README.md                      # Project documentation
```  

## How the App Works Internally

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
2. text_to_speech.py → TTS (gTTS or Gemini)
3. text_extraction_service.py → PDF/CSV/Excel parsing
4. gemini_client.py → API client setup

**Utilities (utils/)**
PDF, Excel, CSV parsing helpers

## Technologies Used

Python
Streamlit
Gemini API
gTTS 
PyPDF2
Pandas
OpenPyXL
CSV utilities

## Error Handling

The app includes:

* API key validation

* File type validation

* Empty input warnings

* Exception handling for API failures

* User‑friendly messages

## Considerations
**API Key Security**
* Never hard‑code your API key in the code

* Use environment variables

* Do not commit your key to GitHub
 

## File Size
* Large PDFs or Excel files may take longer to process

* Streamlit has upload size limits

## Language Support
* Translation quality depends on Gemini’s language capabilities

* Some languages may have limited TTS support

Internet Requirement
Gemini API calls require an active internet connection

## Limitations
- No offline translation or TTS

- No batch translation for multiple files at once

- TTS output is limited to MP3 format

- PDF extraction may struggle with scanned documents

- CSV/Excel extraction assumes readable text content

- Translation accuracy depends on choosem Gemini model.

## Challenges Faced During Development

1. Handling Multiple File Types
Extracting text from:
PDFs
CSVs
Excel files
required separate parsing logic and error handling.

2. Managing Session State
   Streamlit session state needed careful handling to:

  - store extracted text
  - store translated text
  - store audio bytes
  - avoid losing data between button clicks

3. Managing Streamlit widget keys:
  - Multiple tabs and repeated widgets required unique keys
  - Without keys, widgets conflicted or overwrote session state
  - Assigning keys ensured stable UI behavior and correct state updates


4. Gemini API Response Handling
   Ensuring:
  - correct prompt formatting
  - safe error handling
  - stable API client initialization

## Deployment
This application is deployed on Streamlit Cloud.
Any push to the main branch automatically triggers a redeployment.

**Python Version**
The Python version used by Streamlit Cloud is python-3.12. We can update it under the app settings.

**Dependencies**
All required Python packages are listed in requirements.txt.
Streamlit Cloud installs these automatically during deployment.

**Secrets (API Keys)**
Sensitive keys (e.g., Gemini API key) are not stored in the repository.
They must be added in the Streamlit Cloud dashboard:

1. Go to https://share.streamlit.io

2. Open your app

3. Go to Settings → Secrets

4. Add your key in TOML format:

GEMINI_API_KEY = "your-real-key-here"

**Automatic Redeployment**
Whenever you push changes to GitHub:

- Streamlit Cloud pulls the latest code

- Installs dependencies

- Applies the Python version from runtime.txt

- Loads secrets

- Restarts the app

Working public URL: https://capstone-project-cyqesmecxmwzkbv8tv3capp.streamlit.app/ 

No manual deployment commands are required.
