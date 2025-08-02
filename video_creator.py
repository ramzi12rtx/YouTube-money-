from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
from audio_generator import generate_audio
import os
import requests

def download_video():
    url = "https://player.vimeo.com/external/2887463.sd.mp4"  # أي فيديو حر قصير
    r = requests.get(url)
    path = "assets/background.mp4"
    with open(path, "wb") as f:
        f.write(r.content)
    return path

def create_video():
    print("🎥 Creating short video...")
    
    video_path = download_video()
    audio_path = generate_audio("This is an auto-generated short. Stay tuned!")
    
    video = VideoFileClip(video_path).subclip(0, 20).resize(height=1080).crop(x_center=540, width=1080)  # شورت 9:16
    audio = AudioFileClip(audio_path)
    
    video = video.set_audio(audio).set_duration(audio.duration)
    
    output_path = "assets/output.mp4"
    video.write_videofile(output_path, codec="libx264", audio_codec="aac", fps=30, bitrate="3000k", preset="slow")
    
    print("✅ Video created at", output_path)
