from pytube import YouTube

async def download_video(video_url: str):
    """Downloads a YT video from provided URL and saves it as an .mp4

    """
    youtubeObject = YouTube(video_url)
    youtubeObject = youtubeObject.streams.get_lowest_resolution() # lowest_resolution is selected since we only need the file to extract the audio
    try:
        youtubeObject.download(filename='downloaded_video.mp4')
    except:
        print("An error has occurred")
    return 'downloaded_video.mp4'