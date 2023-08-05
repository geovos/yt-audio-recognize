from moviepy.editor import *

async def convert_video_to_audio(video_file: str):
    
    """Converts a YouTube video to an audio file.

    """
    video = VideoFileClip("/usr/src/app/downloaded_video.mp4")
    audio = video.audio.write_audiofile("converted_audio.mp3")

    return audio