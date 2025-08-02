import requests
from config import API_VIDEO_KEY

def upload_to_apivideo(video_path="assets/final.mp4"):
    headers = {"Authorization": f"Bearer {API_VIDEO_KEY}"}

    res = requests.post("https://ws.api.video/videos", headers=headers, json={
        "title": "Auto Short", "description": "Generated automatically"
    })
    video_id = res.json()["videoId"]

    with open(video_path, 'rb') as f:
        upload = requests.post(
            f"https://ws.api.video/videos/{video_id}/source",
            headers=headers,
            files={"file": f}
        )
    return upload.json()["assets"]["mp4"]
