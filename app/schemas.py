# app/schemas.py
from pydantic import BaseModel, HttpUrl
from typing import List, Optional
from enum import Enum
from datetime import datetime

class ImportStatusEnum(str, Enum):
    importing = "importing"
    processing = "processing"
    completed = "completed"
    failed = "failed"

class ImportRequest(BaseModel):
    playlist_url: HttpUrl

class ImportResponse(BaseModel):
    playlist_id: str
    status: str

class ImportStatusResponse(BaseModel):
    playlist_id: str
    status: ImportStatusEnum
    progress: Optional[float]  # Percentage completed

class TrackSchema(BaseModel):
    track_id: str
    title: str
    artist: str
    bpm: Optional[float]
    key: Optional[str]
    energy_level: Optional[float]
    duration: Optional[int]

    class Config:
        orm_mode = True

class PlaylistMetadataResponse(BaseModel):
    playlist_id: str
    tracks: List[TrackSchema]

class MixSettings(BaseModel):
    fade_duration: int  # in milliseconds
    transition_style: str
    mix_tempo: int

class MixRequest(BaseModel):
    playlist_id: str
    mix_settings: MixSettings

class MixResponse(BaseModel):
    mix_id: str
    status: str

class MixStatusEnum(str, Enum):
    queued = "queued"
    processing = "processing"
    completed = "completed"
    failed = "failed"

class MixStatusResponse(BaseModel):
    mix_id: str
    status: MixStatusEnum
    progress: Optional[float]
