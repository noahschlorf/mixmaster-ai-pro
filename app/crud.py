# app/crud.py
from sqlalchemy.orm import Session
from . import models, schemas

def create_playlist(db: Session, playlist_url: str) -> models.Playlist:
    playlist = models.Playlist(playlist_url=playlist_url)
    db.add(playlist)
    db.commit()
    db.refresh(playlist)
    return playlist

def get_playlist(db: Session, playlist_id: str) -> models.Playlist:
    return db.query(models.Playlist).filter(models.Playlist.playlist_id == playlist_id).first()

def update_playlist_status(db: Session, playlist_id: str, status: models.ImportStatus) -> models.Playlist:
    playlist = get_playlist(db, playlist_id)
    if playlist:
        playlist.status = status
        db.commit()
        db.refresh(playlist)
    return playlist

def create_track(db: Session, track: schemas.TrackSchema, playlist_id: str, file_path: str) -> models.Track:
    db_track = models.Track(
        playlist_id=playlist_id,
        title=track.title,
        artist=track.artist,
        bpm=track.bpm,
        key=track.key,
        energy_level=track.energy_level,
        duration=track.duration,
        file_path=file_path
    )
    db.add(db_track)
    db.commit()
    db.refresh(db_track)
    return db_track

def get_tracks_by_playlist(db: Session, playlist_id: str) -> List[models.Track]:
    return db.query(models.Track).filter(models.Track.playlist_id == playlist_id).all()
