import requests
import json
import os
API_KEY = os.environ.get("YT_API")

async def get_video_metadata(video_url: str):

  """Fetches the metadata about a specific video from the YouTube Data API. Works with full URL
  """
  # Check if full link was provided and keep only the id
  if video_url.startswith('https'):
      video_url = video_url.split("v=")[-1]
  else:
     video_url
  
  response = requests.get(
      f"https://youtube.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&id={video_url}&key={API_KEY}")
  data = json.loads(response.content)
  return data