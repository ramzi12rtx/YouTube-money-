from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import os

def upload_to_youtube():
    creds = Credentials(
        None,
        refresh_token=os.getenv("YOUTUBE_REFRESH_TOKEN"),
        token_uri="https://oauth2.googleapis.com/token",
        client_id=os.getenv("YOUTUBE_CLIENT_ID"),
        client_secret=os.getenv("YOUTUBE_CLIENT_SECRET"),
        scopes=["https://www.googleapis.com/auth/youtube.upload"]
    )

    youtube = build("youtube", "v3", credentials=creds)

    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": "Auto Generated Video",
                "description": "This video was created automatically",
                "tags": ["auto", "video", "ai"],
                "categoryId": "22"
            },
            "status": {
                "privacyStatus": "public"
            }
        },
        media_body="assets/final.mp4"
    )

    response = request.execute()
    print("✅ Video uploaded successfully:", response["id"])
