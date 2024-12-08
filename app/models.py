# app/models.py
import uuid
from sqlalchemy import Column, String, Float, Integer, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base
import enum

class ImportStatus(enum.Enum):
    importing = "importing"
    processing = "processing"
    completed = "completed"
    failed = "failed"

class Playlist(Base):
    __tablename__ = "playlists"
    
    playlist_id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    playlist_url = Column(String, unique=True, nullable=False)
    status = Column(Enum(ImportStatus), default=ImportStatus.importing)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    tracks = relationship("Track", back_populates="playlist")

class Track(Base):
    __tablename__ = "tracks"
    
    track_id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    playlist_id = Column(String, ForeignKey("playlists.playlist_id"))
    title = Column(String, nullable=False)
    artist = Column(String, nullable=False)
    bpm = Column(Float)
    key = Column(String)
    energy_level = Column(Float)
    duration = Column(Integer)  # in seconds
    file_path = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    playlist = relationship("Playlist", back_populates="tracks")
