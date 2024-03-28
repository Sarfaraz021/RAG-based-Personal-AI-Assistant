from fastapi import FastAPI
from app.routers import chat_router, finetune_router

app = FastAPI(title="RAG Assistant API",
              description="API for interacting with the RAG Assistant", version="1.0.0")

# Include the routers for different functionalities
app.include_router(chat_router, prefix="/chat", tags=["chat"])
app.include_router(finetune_router, prefix="/finetune", tags=["finetune"])
