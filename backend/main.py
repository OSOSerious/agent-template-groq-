import os
from typing import Optional, List, Dict, Any
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
import glob
import logging
from datetime import datetime
from openai import OpenAI
from fastapi.responses import JSONResponse

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(
    title="AgentGPT API",
    description="Backend API for AgentGPT",
    version="1.0.0"
)

# CORS middleware configuration
origins = [
    "http://localhost:5173",  # Vite default dev server
    "http://localhost:5174",
    "http://localhost:5175",
    "http://localhost:5176",
    "http://localhost:5177",
    "http://localhost:5178",  # Allow the current port
    "http://localhost:3000",  # Alternative local development
    "http://localhost:8080",  # Another common local port
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
    expose_headers=["*"],
    max_age=3600,  # Cache preflight requests for 1 hour
)

# Add error handling middleware
@app.middleware("http")
async def error_handling_middleware(request, call_next):
    try:
        response = await call_next(request)
        return response
    except Exception as e:
        logger.error(f"Unhandled error: {str(e)}")
        return JSONResponse(
            status_code=500,
            content={"detail": "Internal server error occurred"}
        )

# Initialize Groq client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),  # We're using OPENAI_API_KEY for Groq
    base_url="https://api.groq.com/openai/v1"
)

if not os.getenv("OPENAI_API_KEY"):
    logger.error("OPENAI_API_KEY environment variable not set")
    raise ValueError("OPENAI_API_KEY environment variable must be set")

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    template_id: str
    message: str

class ChatResponse(BaseModel):
    response: str
    error: Optional[str] = None

class ChatSession(BaseModel):
    id: str
    name: str
    created_at: str
    messages: List[Dict[str, Any]]

# Load templates
def load_templates():
    templates = []
    template_files = glob.glob("templates/*.json")
    for file_path in template_files:
        try:
            with open(file_path, 'r') as f:
                template = json.load(f)
                template_id = os.path.splitext(os.path.basename(file_path))[0]
                template["id"] = template_id
                templates.append(template)
        except Exception as e:
            logger.error(f"Error loading template {file_path}: {e}")
    return templates

@app.get("/templates")
async def get_templates():
    try:
        templates = load_templates()
        if not templates:
            logger.warning("No templates found")
            return []
        return templates
    except Exception as e:
        logger.error(f"Error loading templates: {e}")
        raise HTTPException(status_code=500, detail="Failed to load templates")

@app.get("/chat/sessions")
async def get_chat_sessions():
    try:
        # Return empty list for now since we're not storing sessions
        return []
    except Exception as e:
        logger.error(f"Error getting chat sessions: {e}")
        raise HTTPException(status_code=500, detail="Failed to get chat sessions")

@app.post("/chat/sessions")
async def create_chat_session(template_id: str):
    try:
        session_id = f"session_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        return {
            "id": session_id,
            "name": f"Chat {datetime.now().strftime('%Y-%m-%d %H:%M')}",
            "created_at": datetime.now().isoformat(),
            "messages": []
        }
    except Exception as e:
        logger.error(f"Error creating chat session: {e}")
        raise HTTPException(status_code=500, detail="Failed to create chat session")

@app.post("/chat/message", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        # Validate request
        if not request.message or not request.message.strip():
            raise HTTPException(
                status_code=400,
                detail="Message cannot be empty"
            )
            
        # Load the template
        template_path = f"templates/{request.template_id}.json"
        logger.info(f"Looking for template at: {template_path}")
        
        if not os.path.exists(template_path):
            logger.warning(f"Template {request.template_id} not found, using default template")
            template_path = "templates/research_agent.json"
            
        try:
            with open(template_path, "r") as f:
                template = json.load(f)
        except Exception as e:
            logger.error(f"Error reading template file {template_path}: {e}")
            raise HTTPException(
                status_code=500,
                detail=f"Error reading template file: {str(e)}"
            )

        # Prepare messages for the API
        messages = [
            {"role": "system", "content": template.get("system_prompt", "You are a helpful assistant.")},
            {"role": "user", "content": request.message}
        ]

        logger.info(f"Sending request to Groq API with template: {template.get('name', 'unknown')}")
        
        try:
            # Call Groq API with timeout
            response = client.chat.completions.create(
                model="mixtral-8x7b-32768",
                messages=messages,
                temperature=0.7,
                max_tokens=1024,
                timeout=30  # 30 second timeout
            )
            
            if not response.choices or len(response.choices) == 0:
                logger.error("No response generated from Groq API")
                raise HTTPException(
                    status_code=500,
                    detail="No response generated from the model"
                )
                
            return ChatResponse(
                response=response.choices[0].message.content
            )
            
        except Exception as api_error:
            logger.error(f"Groq API error: {api_error}")
            raise HTTPException(
                status_code=500,
                detail=f"Error calling Groq API: {str(api_error)}"
            )

    except HTTPException as http_error:
        # Re-raise HTTP exceptions
        raise http_error
    except Exception as e:
        logger.error(f"Unexpected error in chat endpoint: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error: {str(e)}"
        )

if __name__ == "__main__":
    import uvicorn
    logger.info("Starting server...")
    uvicorn.run(app, host="0.0.0.0", port=8002, log_level="info")
