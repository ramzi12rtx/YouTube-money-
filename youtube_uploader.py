from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import os
from config import YOUTUBE_REFRESH_TOKEN, YOUTUBE_CLIENT_ID, YOUTUBE_CLIENT_SECRET

def upload_to_youtube(video_path="assets/final.mp4", title="Auto Short", desc="Made by bot"):
    creds = {
        "installed": {
            "client_id": YOUTUBE_CLIENT_ID,
            "client_secret": YOUTUBE_CLIENT_SECRET,
            "redirect_uris": ["urn:ietf:wg:oauth:2.0:oob"],
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token"
        }
    }

    flow = InstalledAppFlow.from_client_config(creds, ["https://www.googleapis.com/auth/youtube.upload"])
    flow.fetch_token(refresh_token=YOUTUBE_REFRESH_TOKEN)
    service = build("youtube", "v3", credentials=flow.credentials)

    request = service.videos().insert(
        part="snippet,status",
        body={
            "snippet": {"title": title, "description": desc, "tags": ["shorts"]},
            "status": {"privacyStatus": "public"}
        },
        media_body=MediaFileUpload(video_path)
    )
    response = request.execute()
    print("✅ Uploaded to YouTube:", response["id"])
