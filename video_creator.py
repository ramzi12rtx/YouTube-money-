from moviepy.editor import VideoFileClip, AudioFileClip
import os

def create_video(video_path="assets/video.mp4", audio_path="assets/audio.mp3", output_path="assets/final.mp4"):
    video = VideoFileClip(video_path).subclip(0, 10)
    audio = AudioFileClip(audio_path)

    final = video.set_audio(audio)
    final.write_videofile(output_path, codec="libx264", audio_codec="aac")
