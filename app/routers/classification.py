from fastapi import APIRouter, HTTPException
from app.services.classification_service import classify_text

router = APIRouter()

@router.post("/")
async def classification_endpoint(text: str):
    try:
        category = classify_text(text)
        return {"category": category}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
