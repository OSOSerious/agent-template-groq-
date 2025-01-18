from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict
import sys
import os

# Add parent directory to path to import GroqInterface
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from groq_interface import GroqInterface

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    messages: List[Dict[str, str]]
    template: str

class ChatResponse(BaseModel):
    response: str
    thoughts: List[str]
    error: bool = False
    template: str
    model: str

groq = GroqInterface()

@app.post("/api/chat")
async def chat(request: ChatRequest) -> ChatResponse:
    try:
        result = groq.get_completion(request.messages, request.template)
        return ChatResponse(**result)
    except Exception as e:
        print(f"Error in chat endpoint: {str(e)}")
        return ChatResponse(
            response="I apologize, but I encountered an error. Please try again.",
            thoughts=["Error occurred while processing your request"],
            error=True,
            template=request.template,
            model=groq.model
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
