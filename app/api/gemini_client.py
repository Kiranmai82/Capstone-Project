import os
from google import genai


def get_gemini_api_key():
    api_key = os.getenv("GEMINI_API_KEY")
    if api_key:
        return api_key

    try:
        import streamlit as st
    except Exception:
        return None

    try:
        print(f"Streamlit secrets: {st.secrets.get('GEMINI_API_KEY')}")
        return st.secrets.get("api_keys", {}).get("GEMINI_API_KEY")

    except Exception:
        return None


API_KEY = get_gemini_api_key()

if API_KEY:
    client = genai.Client(api_key=API_KEY)
else:
    client = None
