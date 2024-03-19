# main.py
from fastapi import FastAPI
from rag import RAG, initialize_rag
from helpers import chat_completion

app = FastAPI()

rag = RAG()


@app.post("/finetune/")
async def finetune(directory_path: str):
    initialize_rag(rag, directory_path)  # Passing rag object
    return {"message": "Finetuning done Successfully"}


@app.post("/chat/")
async def chat(prompt: str):
    response = chat_completion(prompt)
    return {"response": response}
