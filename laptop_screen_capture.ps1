$flags = @(
    "-f", "gdigrab",
    "-i", "desktop",
    "-f", "dshow",
    "-i", "audio=Miks stereo (Realtek(R) Audio)",
    "-c:v", "libx264",
    "-preset", "veryfast",
    "-crf", "28",
    "-b:v", "800k",
    "-s", "1280x720",
    "-c:a", "aac",
    "-b:a", "128k",
    "output1.mp4"
)

ffmpeg @flags
