import requests
from config import ELEVENLABS_API_KEY, VOICE_ID

def text_to_speech(text, output_path="assets/audio.mp3"):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "text": text,
        "voice_settings": {
            "stability": 0.4,
            "similarity_boost": 0.75
        }
    }

    response = requests.post(url, json=payload, headers=headers)
    with open(output_path, "wb") as f:
        f.write(response.content)
