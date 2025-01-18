from groq_interface import GroqInterface
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def main():
    # Initialize interface
    groq = GroqInterface()
    
    # Example 1: Basic chat
    messages = [
        {"role": "user", "content": "What is quantum computing?"}
    ]
    response = groq.chat_completion(messages)
    print("\nChat Response:")
    print(response)
    
    # Example 2: Image processing
    image_url = "https://upload.wikimedia.org/wikipedia/commons/d/da/SF_From_Marin_Highlands3.jpg"
    image_prompt = "What do you see in this image?"
    response = groq.process_image(image_url, image_prompt)
    print("\nImage Analysis:")
    print(response)
    
    # Example 3: Function calling
    weather_tools = [{
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the current weather in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA"
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"]
                    }
                },
                "required": ["location"]
            }
        }
    }]
    
    function_messages = [
        {"role": "user", "content": "What's the weather like in Boston?"}
    ]
    
    tool_call = groq.function_call(function_messages, weather_tools)
    print("\nFunction Call Response:")
    print(tool_call)

if __name__ == "__main__":
    main()
