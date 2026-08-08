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
   ```bash
   cd "Capstone_Project"

2. Create and activate a virtual environment:
    Windows:

    python -m venv .venv
    .venv\Scripts\activate

    macOS/Linux:

    python -m venv .venv
    source .venv/bin/activate

    Project 