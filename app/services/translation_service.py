from app.api.gemini_client import client

def translate_text(user_input, selected_label, selected_code):
    if client is None:
        raise RuntimeError(
            "Translation is unavailable because the Gemini API key is not configured."
        )

    #prompt = f"Translate the following text into {selected_label} ({selected_code}):\n\n{user_input}"
    prompt = f"""
      Translate the following text into {selected_label} only.
      Translate **every** word unless it is a proper noun.
      Do NOT preserve any original-language words.
      Output should be entirely in {selected_label}.

      Text:
      {user_input}
    """
    response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=[
        {
            "role": "user",
            "parts": [{"text": prompt}]
        }
    ])

    return response.text
