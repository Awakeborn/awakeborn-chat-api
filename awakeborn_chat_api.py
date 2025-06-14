from fastapi import FastAPI
from pydantic import BaseModel
from awakeborn_chat_public import chat

app = FastAPI()

class ChatRequest(BaseModel):
    wallet: str
    message: str

class ChatResponse(BaseModel):
    status: str
    reply: str

@app.post("/api/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    reply = chat(request.message)
    return ChatResponse(status="success", reply=reply)
