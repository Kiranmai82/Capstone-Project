import time
from google.genai.errors import APIError
from app.api.gemini_client import client

def translate_text(user_input, selected_label, selected_code, retries=3, backoff=2):
    if client is None:
        raise RuntimeError(
            "Translation is unavailable because the Gemini API key is not configured."
        )

    prompt = f"""
      Translate the following text into {selected_label} only.
      Translate **every** word unless it is a proper noun.
      Do NOT preserve any original-language words.
      Output should be entirely in {selected_label}.

      Text:
      {user_input}
    """

    for attempt in range(retries):
        try:
            response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents=[
                    {
                        "role": "user",
                        "parts": [{"text": prompt}]
                    }
                ]
            )
            return response.text

        except APIError as e:
            # Handle 429 Too Many Requests
            if "429" in str(e):
                wait_time = backoff * (attempt + 1)
                print(f"Rate limit hit (429). Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
                continue

             return "⚠️ The translation service is temporarily unavailable. Please try again."

        except Exception:
            return "⚠️ An unexpected error occurred. Please try again."

    # If all retries fail
    return "⚠️ Translation failed due to API rate limits. Please wait a moment and try again."
    

