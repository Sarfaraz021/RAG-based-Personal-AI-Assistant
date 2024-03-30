# app/main.py

from fastapi import FastAPI
from app.routers import chat_router, finetune_router
from fastapi.middleware.cors import CORSMiddleware
# from app.routers.auth_router import router as auth_router
# from app.database import connect_to_mongo, close_mongo_connection


app = FastAPI(title="RAG Assistant API",
              description="API for interacting with the RAG Assistant", version="1.0.0")


# @app.on_event("startup")
# async def startup_db_client():
#     await connect_to_mongo()


# @app.on_event("shutdown")
# async def shutdown_db_client():
#     await close_mongo_connection()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],  # The origin of your frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the routers for different functionalities
app.include_router(chat_router, prefix="/chat", tags=["chat"])
app.include_router(finetune_router, prefix="/finetune", tags=["finetune"])
# app.include_router(auth_router, prefix="/auth", tags=["auth"])