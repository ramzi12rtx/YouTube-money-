from text_generator import generate_text
from tts import text_to_speech
from video_creator import create_video
from api_video_uploader import upload_to_apivideo
from youtube_uploader import upload_to_youtube
import requests
import os
from config import PEXELS_API_KEY


def download_video_from_pexels():
    print("⬇️ Downloading video from Pexels...")
    headers = {"Authorization": PEXELS_API_KEY}
    res = requests.get("https://api.pexels.com/videos/search?query=nature&per_page=1", headers=headers)
    
    video_url = None
    for file in res.json()["videos"][0]["video_files"]:
        if file["quality"] == "hd" and file["width"] >= 1080:
            video_url = file["link"]
            break
    if not video_url:
        video_url = res.json()["videos"][0]["video_files"][-1]["link"]  # fallback
    
    r = requests.get(video_url)
    os.makedirs("assets", exist_ok=True)
    with open("assets/video.mp4", "wb") as f:
        f.write(r.content)
    print("✅ Video downloaded: assets/video.mp4")


if __name__ == "__main__":
    print("🎯 Starting Auto Short Video Generator")

    # 1. Generate text
    text = generate_text()
    print("📝 Generated text:", text)

    # 2. Download background video
    download_video_from_pexels()

    # 3. Generate audio from text
    audio_path = text_to_speech(text)

    # 4. Create final short video
    create_video(audio_path)

    # 5. Upload to api.video (optional)
    upload_to_apivideo()

    # 6. Upload to YouTube
    upload_to_youtube()
