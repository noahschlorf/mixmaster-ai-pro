# app/main.py
from fastapi import FastAPI
from .database import engine, Base
from . import models
from app.routers import health

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="MixMaster AI Pro API")

# Include Routers
app.include_router(health.router)
