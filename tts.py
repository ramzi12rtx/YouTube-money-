# في ملف tts.py
def text_to_speech(text):
    import requests
    import os

    voice_id = "EXAVITQu4vr4xnSDxMaL"
    api_key = os.getenv("ELEVENLABS_API_KEY")

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {
        "xi-api-key": api_key,
        "Content-Type": "application/json"
    }
    data = {
        "text": text,
        "voice_settings": {
            "stability": 0.4,
            "similarity_boost": 0.75
        }
    }

    response = requests.post(url, headers=headers, json=data)
    output_path = "assets/audio.mp3"
    with open(output_path, "wb") as f:
        f.write(response.content)

    return output_path
