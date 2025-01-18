from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from ..utils.logger import setup_logger
import sys
import os

# Add the project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from groq_interface import GroqInterface

# Configure logging
logger = setup_logger(__name__)

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="AgentGPT API",
    description="API for AgentGPT powered by Groq",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Groq interface
try:
    if not os.getenv("GROQ_API_KEY"):
        logger.error("GROQ_API_KEY environment variable is not set")
        raise ValueError("GROQ_API_KEY environment variable is not set")
    groq_interface = GroqInterface()
    logger.info("Successfully initialized Groq interface")
except Exception as e:
    logger.error(f"Failed to initialize Groq interface: {e}")
    raise

class ChatRequest(BaseModel):
    template: str
    message: str
    systemPrompt: str = None

@app.get("/")
async def read_root():
    """Root endpoint"""
    return {"message": "Welcome to AgentGPT API"}

@app.get("/templates")
async def get_templates():
    """Get available templates"""
    try:
        templates = groq_interface.get_available_templates()
        logger.info(f"Retrieved {len(templates)} templates")
        return templates
    except Exception as e:
        logger.error(f"Error getting templates: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/chat")
async def chat(request: ChatRequest):
    """Handle chat requests"""
    try:
        logger.info(f"Received chat request with template: {request.template}")
        
        # Prepare messages
        messages = [{"role": "user", "content": request.message}]
        
        # Get completion from Groq
        response = groq_interface.get_completion(
            messages=messages,
            template=request.template
        )
        
        # Extract thoughts using simple heuristic
        thoughts = []
        if "Thoughts:" in response:
            parts = response.split("Thoughts:")
            response = parts[0].strip()
            if len(parts) > 1:
                thoughts = [t.strip() for t in parts[1].split("\n") if t.strip()]
        
        logger.info("Successfully generated response")
        return {
            "response": response,
            "thoughts": thoughts
        }
        
    except Exception as e:
        logger.error(f"Error in chat endpoint: {e}")
        raise HTTPException(status_code=500, detail=str(e))
