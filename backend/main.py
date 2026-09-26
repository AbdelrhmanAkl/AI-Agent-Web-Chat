from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

from backend.agent import AIChatAgent


load_dotenv()


app = FastAPI(
    title="AI Agent Web Chat",
    description="Backend API for an AI Agent Web Chat application.",
    version="1.0.0",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


agent = AIChatAgent()


class ChatRequest(BaseModel):
    message: str
    conversation_id: str = "default"


class ChatResponse(BaseModel):
    response: str
    conversation_id: str


@app.get("/")
def root():
    return {
        "message": "AI Agent Web Chat API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    message = request.message.strip()

    if not message:
        raise HTTPException(
            status_code=400,
            detail="Message cannot be empty."
        )

    try:
        response = agent.chat(
            message=message,
            conversation_id=request.conversation_id,
        )

        return ChatResponse(
            response=response,
            conversation_id=request.conversation_id,
        )

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Agent error: {str(exc)}",
        )


@app.delete("/chat/{conversation_id}")
def clear_conversation(conversation_id: str):

    agent.clear_history(conversation_id)

    return {
        "message": "Conversation history cleared."
    }