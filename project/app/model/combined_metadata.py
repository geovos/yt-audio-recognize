from sqlalchemy import (
    Column,
    Integer,
    PrimaryKeyConstraint,
    String,
    ARRAY
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class CombinedMetadata(Base):
    __tablename__ = "video_song_metadata"
    id = Column(Integer, primary_key=True, autoincrement=True)
    video_url = Column(String, index=True)
    video_id = Column(String)
    channel_id = Column(String)
    title = Column(String)
    channel_title = Column(String)
    tags = Column(ARRAY(String), nullable=True)
    view_count = Column(Integer)
    like_count = Column(Integer)
    favorite_count = Column(Integer)
    comment_count = Column(Integer)
    track_title = Column(String)
    track_subtitle = Column(String)
    track_url = Column(String)
    isrc = Column(String)
    primary_genre = Column(String)
    url_params_track_title = Column(String)
    url_params_track_artist = Column(String)
    
    

    class Config:
        orm_mode = True
        
    def to_dict(self):
        return {
            "video_url": self.video_url,
            "video_id": self.video_id,
            "channel_id": self.channel_id,
            "title": self.title,
            "channel_title": self.channel_title,
            "tags": self.tags,
            "view_count": self.view_count,
            "like_count": self.like_count,
            "favorite_count": self.favorite_count,
            "comment_count": self.comment_count,
            "track_title": self.track_title,
            "track_subtitle": self.track_subtitle,
            "track_url": self.track_url,
            "isrc": self.isrc,
            "primary_genre": self.primary_genre,
            "url_params_track_title": self.url_params_track_title,
            "url_params_track_artist": self.url_params_track_artist,
        }