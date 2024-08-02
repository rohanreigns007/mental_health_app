from fastapi import FastAPI
from app.routers import rag, classification

app = FastAPI(title="Mental Health RAG and Classification API")

app.include_router(rag.router, prefix="/rag", tags=["RAG"])
app.include_router(classification.router, prefix="/classification", tags=["Classification"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Mental Health API"}
