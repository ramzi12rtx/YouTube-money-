from text_generator import generate_text
from tts import text_to_speech
from video_creator import create_video
from api_video_uploader import upload_to_apivideo
from youtube_uploader import upload_to_youtube
import requests
import random
from config import PEXELS_API_KEY

def download_video_from_pexels():
    headers = {"Authorization": PEXELS_API_KEY}
    res = requests.get("https://api.pexels.com/videos/search?query=nature&per_page=1", headers=headers)
    url = res.json()["videos"][0]["video_files"][0]["link"]
    r = requests.get(url)
    with open("assets/video.mp4", "wb") as f:
        f.write(r.content)

if __name__ == "__main__":
    print("🎯 Starting process")
    text = generate_text()
    download_video_from_pexels()
    text_to_speech(text)
    create_video()
    upload_to_apivideo()
    upload_to_youtube()
