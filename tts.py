import requests
import os

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
VOICE_ID = "EXAVITQu4vr4xnSDxMaL"  # يمكنك تغييره إلى صوت آخر من ElevenLabs

def text_to_speech(text, output_path="assets/voice.mp3"):
    print("🔊 Generating audio with ElevenLabs...")

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"

    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": ELEVENLABS_API_KEY
    }

    data = {
        "text": text,
        "voice_settings": {
            "stability": 0.4,
            "similarity_boost": 0.75
        }
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code != 200:
        raise Exception(f"❌ ElevenLabs Error: {response.status_code} - {response.text}")

    os.makedirs("assets", exist_ok=True)
    with open(output_path, "wb") as f:
        f.write(response.content)

    print(f"✅ Audio saved to {output_path}")
    return output_path
