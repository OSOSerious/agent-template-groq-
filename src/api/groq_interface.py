from groq import Groq
import os
from typing import List, Dict, Optional
from ..utils.logger import setup_logger

logger = setup_logger(__name__)

class GroqInterface:
    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY environment variable is not set")
            
        self.client = Groq(api_key=api_key)
        self.model = "llama2-70b-4096"
        self.load_templates()
    
    def load_templates(self):
        """Load templates from templates directory"""
        try:
            from ..templates.agent_templates import TEMPLATES
            self.templates = TEMPLATES
            logger.info(f"Loaded {len(self.templates)} templates")
        except Exception as e:
            logger.error(f"Error loading templates: {e}")
            self.templates = {}

    def get_completion(self, messages: List[Dict[str, str]], template: str = None, max_tokens: int = 1024) -> str:
        """
        Get a completion from the Groq API
        """
        try:
            # Validate template
            if template and template not in self.templates:
                raise ValueError(f"Template '{template}' not found. Available templates: {list(self.templates.keys())}")

            # Add template system prompt if specified
            if template:
                logger.info(f"Using template: {template}")
                messages.insert(0, {
                    "role": "system",
                    "content": self.templates[template]["system_prompt"]
                })

            # Log request
            logger.info(f"Sending request to Groq API with {len(messages)} messages")

            # Create chat completion
            completion = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                max_tokens=max_tokens,
                temperature=0.7,
                top_p=1,
                stream=False
            )
            
            response = completion.choices[0].message.content
            logger.info("Successfully received response from Groq API")
            return response

        except ValueError as e:
            # Handle validation errors
            error_msg = str(e)
            logger.error(error_msg)
            raise e

        except Exception as e:
            # Handle API and other errors
            error_msg = f"Error getting completion: {str(e)}"
            logger.error(error_msg)
            raise Exception(error_msg)

    def get_available_templates(self) -> List[Dict[str, str]]:
        """
        Get list of available templates
        """
        return [
            {"id": template_id, "name": template["name"]}
            for template_id, template in self.templates.items()
        ]
