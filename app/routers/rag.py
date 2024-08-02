from fastapi import APIRouter, HTTPException
from app.services.rag_service import generate_response

router = APIRouter()

@router.post("/")
async def rag_endpoint(prompt: str):
    try:
        response = generate_response(prompt)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
