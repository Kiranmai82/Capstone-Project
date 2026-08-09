from app.api.gemini_client import client
import time

def safe_generate(prompt, retries=3):
    for attempt in range(retries):
        try:
            return client.models.generate_content(
                model="gemini-3.6-flash",
                contents=[{
                    "role": "user",
                    "parts": [{"text": prompt}]
                }]
            )
        except Exception as e:
            # Handle rate limits
            if "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e):
                sleep_time = 2 ** attempt
                time.sleep(sleep_time)
            else:
                raise e
    raise RuntimeError("Translation failed after retries due to rate limits.")


def chunk_text(text, size=3000):
    return [text[i:i+size] for i in range(0, len(text), size)]


def translate_text(user_input, selected_label, selected_code):
    if client is None:
        raise RuntimeError(
            "Translation is unavailable because the Gemini API key is not configured."
        )

    prompt_template = f"""
    Translate the following text into {selected_label} only.
    Translate every word unless it is a proper noun.
    Do NOT preserve any original-language words.
    Output should be entirely in {selected_label}.

    Text:
    {{chunk}}
    """

    chunks = chunk_text(user_input)
    translated_chunks = []

    for chunk in chunks:
        prompt = prompt_template.replace("{chunk}", chunk)
        response = safe_generate(prompt)
        translated_chunks.append(response.text)

    return "\n".join(translated_chunks)
