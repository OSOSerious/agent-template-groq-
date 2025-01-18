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
        self.templates = self.load_all_templates()
    
    def load_all_templates(self):
        """Load templates from all sources"""
        templates = {}
        # Load templates from Python file
        try:
            from ..templates.agent_templates import TEMPLATES as PY_TEMPLATES
            templates.update(PY_TEMPLATES)
            logger.info(f"Loaded {len(PY_TEMPLATES)} templates from Python file")
        except Exception as e:
            logger.error(f"Error loading templates from Python file: {e}")

        # Load templates from JSON files in backend/templates directory
        templates_dir = "backend/templates"
        try:
            import json
            base_dir = os.path.dirname(os.path.abspath(__file__))
            full_templates_dir = os.path.join(base_dir, '..', '..', templates_dir)
            for filename in os.listdir(full_templates_dir):
                if filename.endswith(".json"):
                    filepath = os.path.join(full_templates_dir, filename)
                    with open(filepath, 'r') as f:
                        try:
                            template = json.load(f)
                            templates[template["name"].replace(" ", "")] = template
                            logger.info(f"Loaded template from {filename}")
                        except json.JSONDecodeError as e:
                            logger.error(f"Error decoding JSON in {filename}: {e}")
                        except KeyError as e:
                            logger.error(f"Error loading template from {filename}: Missing 'name' key")
            logger.info(f"Loaded {len(templates)} templates from JSON files")
        except FileNotFoundError:
            logger.error(f"Directory not found: {templates_dir}")
        except Exception as e:
            logger.error(f"Error loading templates from {templates_dir}: {e}")
        return templates

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
