import os
import json
from typing import List, Dict, Any
from groq import Groq
from dotenv import load_dotenv
from src.utils.logger import setup_logger

# Configure logging
logger = setup_logger(__name__)

# Load environment variables
load_dotenv()

class GroqInterface:
    def __init__(self):
        """Initialize the Groq interface with API key and templates"""
        self.api_key = os.getenv("GROQ_API_KEY")
        if not self.api_key:
            raise ValueError("GROQ_API_KEY environment variable is not set")
        
        self.client = Groq(api_key=self.api_key)
        self.templates = self._load_templates()
        logger.info("GroqInterface initialized successfully")
    
    def _load_templates(self) -> List[Dict[str, Any]]:
        """Load agent templates from the templates directory"""
        try:
            templates_dir = os.path.join(os.path.dirname(__file__), "groq-agents")
            templates = []
            
            if not os.path.exists(templates_dir):
                logger.warning(f"Templates directory not found: {templates_dir}")
                return []
                
            for filename in os.listdir(templates_dir):
                if filename.endswith(".json"):
                    template_path = os.path.join(templates_dir, filename)
                    try:
                        with open(template_path, "r") as f:
                            template = json.load(f)
                            templates.append(template)
                    except json.JSONDecodeError as e:
                        logger.error(f"Error parsing template {filename}: {e}")
                    except Exception as e:
                        logger.error(f"Error loading template {filename}: {e}")
            
            logger.info(f"Loaded {len(templates)} templates")
            return templates
            
        except Exception as e:
            logger.error(f"Error loading templates: {e}")
            return []
    
    def get_completion(self, messages: List[Dict[str, str]], template: str = None) -> str:
        """Get a completion from Groq API"""
        try:
            # Find the template if specified
            system_prompt = None
            if template:
                template_data = next(
                    (t for t in self.templates if t["name"] == template),
                    None
                )
                if template_data:
                    system_prompt = template_data.get("system_prompt")
            
            # Prepare messages
            api_messages = []
            if system_prompt:
                api_messages.append({"role": "system", "content": system_prompt})
            api_messages.extend(messages)
            
            # Call Groq API
            logger.info(f"Sending request to Groq API with {len(api_messages)} messages")
            completion = self.client.chat.completions.create(
                messages=api_messages,
                model="mixtral-8x7b-32768",
                temperature=0.7,
                max_tokens=1024,
                stream=False
            )
            
            response = completion.choices[0].message.content
            logger.info("Successfully received response from Groq API")
            return response
            
        except Exception as e:
            logger.error(f"Error getting completion from Groq API: {e}")
            raise

    def get_available_templates(self) -> List[Dict[str, str]]:
        """
        Get list of available templates
        """
        return [
            {"id": template["name"], "name": template["name"]}
            for template in self.templates
        ]
