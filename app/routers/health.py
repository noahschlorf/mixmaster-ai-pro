# app/routers/health.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/api/health", tags=["Health"])
async def health_check():
    return {"status": "MixMaster AI Pro API is operational."}
