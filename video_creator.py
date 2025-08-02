from moviepy.editor import VideoFileClip, AudioFileClip

def create_video(audio_path):
    print("🎬 Starting video creation...")

    # حملنا الفيديو مسبقًا إلى هذا المسار
    video_path = "assets/video.mp4"
    
    # قص الفيديو إلى 30 ثانية كحد أقصى
    video = VideoFileClip(video_path).subclip(0, 30)
    
    # تغيير الأبعاد إلى 9:16 (شورت) مع crop من المنتصف
    video = video.resize(height=1920)
    video = video.crop(x_center=video.w / 2, width=1080)  # عرض 1080 مناسب لشورت
    
    # تحميل ملف الصوت
    audio = AudioFileClip(audio_path)

    # دمج الصوت مع الفيديو بالكامل
    video = video.set_audio(audio).set_duration(audio.duration)

    # إخراج الفيديو النهائي
    output_path = "assets/final.mp4"
    video.write_videofile(
        output_path,
        fps=30,
        codec="libx264",
        audio_codec="aac",
        bitrate="3000k",
        preset="medium"
    )

    print(f"✅ Final video saved to: {output_path}")
