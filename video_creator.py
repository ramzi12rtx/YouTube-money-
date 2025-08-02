from moviepy.editor import VideoFileClip, AudioFileClip

def create_video(audio_path):
    print("🎬 Starting video creation...")

    # تحميل ملف الصوت ومعرفة مدته
    audio = AudioFileClip(audio_path)
    audio_duration = audio.duration

    # تحميل الفيديو الأصلي
    video = VideoFileClip("assets/video.mp4")

    # قص الفيديو حسب مدة الصوت (مع حد أقصى مثلاً 60 ثانية)
    video = video.subclip(0, min(audio_duration, 60))

    # تحويله لشكل رأسي 9:16
    video = video.resize(height=1920)
    video = video.crop(x_center=video.w / 2, width=1080)

    # دمج الصوت مع الفيديو
    final_video = video.set_audio(audio).set_duration(audio_duration)

    # حفظ الفيديو النهائي
    output_path = "assets/final.mp4"
    final_video.write_videofile(
        output_path,
        fps=30,
        codec="libx264",
        audio_codec="aac",
        preset="medium"
    )

    print(f"✅ Final video saved to: {output_path}")
