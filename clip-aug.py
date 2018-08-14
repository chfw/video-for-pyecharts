import os
import moviepy.editor as mp
from moviepy.audio.AudioClip import concatenate_audioclips
music = [
    "friends.mp3",
    "laugh1.mp3",
    "normal.mp3",
    "men1.mp3",
    "beyond.mp3"
    ]
vclip = mp.VideoFileClip("gource.mp4")
audio = concatenate_audioclips(
    [mp.AudioFileClip(os.path.join("music", file_name)) for file_name in music]
    )
vclip = vclip.set_audio(audio)
vclip.write_videofile('pyecharts.mp4')
