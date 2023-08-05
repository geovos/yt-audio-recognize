from fastapi import Depends, FastAPI
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from app.services.converter import convert_video_to_audio
from app.services.downloader import download_video
from app.services.metadata import get_video_metadata
from app.services.shazam import identify_song
from app.services.export import write_to_csv
from app.db import get_session, init_db
from app.model.combined_metadata import CombinedMetadata
import json


app = FastAPI()


@app.get("/ping")
async def pong():
    return {"ping": "pong!"}

@app.get("/whatsong")
async def whatsong(video_url: str,session: AsyncSession = Depends(get_session)):
  """ Identifies the song through ShazamIO and YouTube API and provides related metadata information

  Args:
      video_url (str) -- [_description_]
      session (AsyncSession, optional): _description_. Defaults to Depends(get_session).

  Returns:
      _type_: _description_
  """
  
  yt_video = await download_video(video_url)
  yt_metadata = await get_video_metadata(video_url)
  await convert_video_to_audio(yt_video)
  szm_metadata = await identify_song()
    
  response_info = CombinedMetadata(
            video_url=video_url,
            video_id = yt_metadata["items"][0]["id"],
            channel_id = yt_metadata["items"][0]["snippet"]["channelId"],
            title = yt_metadata["items"][0]["snippet"]["title"],
            channel_title = yt_metadata["items"][0]["snippet"]["channelTitle"],
            tags = yt_metadata["items"][0]["snippet"]["tags"],
            view_count = int(yt_metadata["items"][0]["statistics"]["viewCount"]),
            like_count = int(yt_metadata["items"][0]["statistics"]["likeCount"]),
            favorite_count = int(yt_metadata["items"][0]["statistics"]["favoriteCount"]),
            comment_count = int(yt_metadata["items"][0]["statistics"]["commentCount"]),            
            track_title = szm_metadata["track"]["title"],
            track_subtitle = szm_metadata["track"]["subtitle"],
            track_url = szm_metadata["track"]["url"],
            isrc = szm_metadata["track"]["isrc"],
            primary_genre = szm_metadata["track"]["genres"]["primary"],
            url_params_track_title = szm_metadata["track"]["urlparams"]["{tracktitle}"],
            url_params_track_artist = szm_metadata["track"]["urlparams"]["{trackartist}"],
        )
  session.add(response_info)
  await session.commit()
  await session.refresh(response_info)
  response_dict = response_info.to_dict()
  write_to_csv(response_dict,'search_history_metadata.csv')
  return response_info

@app.get("/all_metadata")
async def get_all_metadata(session: AsyncSession = Depends(get_session)):
    async with session.begin():
        result = await session.execute(select(CombinedMetadata))
        return result.scalars().all()