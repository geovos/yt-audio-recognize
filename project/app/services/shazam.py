from shazamio import Shazam

async def identify_song():
  """Identifies a song using ShazamIO library

  """
  shazam = Shazam()
  audio_file = "/usr/src/app/converted_audio.mp3"
  out = await shazam.recognize_song(audio_file)
  return out