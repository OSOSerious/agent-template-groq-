import os
from typing import Optional, List, Dict, Any
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from groq import Groq
import json
import glob
import logging

# Configure logging with more details
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[Message]
    system_prompt: Optional[str] = None

@app.get("/templates")
async def get_templates():
    """Return list of available templates."""
    template_dir = os.path.join(os.path.dirname(__file__), "templates")
    template_files = glob.glob(os.path.join(template_dir, "*.json"))
    templates = []
    
    for file_path in template_files:
        try:
            with open(file_path, 'r') as f:
                template = json.load(f)
                templates.append(template)
                logger.info(f"Loaded template: {template.get('name', 'Unknown')}")
        except Exception as e:
            logger.error(f"Error loading template {file_path}: {e}")
            continue
    
    return templates

@app.post("/chat")
async def chat(request: ChatRequest):
    """Handle chat requests using Groq's API."""
    try:
        # Log incoming request
        logger.info(f"Received chat request with {len(request.messages)} messages")
        
        # Initialize Groq client with API key
        client = Groq(api_key="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")

        # Prepare messages array
        messages = []
        
        # Add system prompt as the first message if provided
        if request.system_prompt:
            messages.append({
                "role": "system",
                "content": request.system_prompt
            })
            logger.info("Added system prompt to messages")

        # Add user messages
        messages.extend([{"role": msg.role, "content": msg.content} for msg in request.messages])
        
        logger.info(f"Making request to Groq API with {len(messages)} messages")

        # Make request to Groq API
        chat_completion = client.chat.completions.create(
            messages=messages,
            model="mixtral-8x7b-32768",
            temperature=0.7,
            max_tokens=1024,
            top_p=1,
            stream=False
        )

        # Log successful response
        logger.info("Successfully received response from Groq API")

        # Return the response
        return {
            "role": "assistant",
            "content": chat_completion.choices[0].message.content
        }

    except Exception as e:
        logger.error(f"Error in chat endpoint: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    logger.info("Starting server...")
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
