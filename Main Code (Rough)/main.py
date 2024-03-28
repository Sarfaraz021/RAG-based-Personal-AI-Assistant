from fastapi import FastAPI
from pydantic import BaseModel

# Assuming 'rag' and 'initialize_rag' are defined in your 'rag.py'
# and 'chat_completion' in your 'helpers.py'
from rag import RAG, initialize_rag
from helpers import chat_completion

app = FastAPI()

rag = RAG()

# Define Pydantic models for the request bodies


class FinetuneRequest(BaseModel):
    directory_path: str


class ChatRequest(BaseModel):
    prompt: str


@app.post("/finetune/")
async def finetune(finetune_request: FinetuneRequest):
    # Use the directory_path attribute from the request model
    initialize_rag(rag, finetune_request.directory_path)
    return {"message": "Finetuning done Successfully"}


@app.post("/chat/")
async def chat(chat_request: ChatRequest):
    # Use the prompt attribute from the request model
    response = chat_completion(chat_request.prompt)
    return {"response": response}
