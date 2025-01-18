# AI Assistant Platform

A modern AI chatbot platform powered by Groq's API, featuring an AgentGPT-style interface for creating personal AI agents and specialized templates for various tasks.

## 🚀 Features

### 🤖 Personal AI Agent Creation
- Create your own AI agent with a name and goal
- Instantly chat with your personalized agent
- Example goals to help you get started
- Modern, AgentGPT-style interface

### 📚 Specialized Agent Templates
- Research Assistant: Generate comprehensive reports and analysis
- Travel Planner: Plan detailed trips and itineraries
- Study Buddy: Create study plans and learning materials
- Game Designer: Design platformer games and mechanics
- Code Generator: Generate code snippets in various languages
- Web Search Assistant: Search and summarize web information

### 💻 Modern Frontend Interface
- Clean, dark theme design
- Responsive layout for all devices
- Interactive chat interface
- Real-time agent responses
- Template-based agent selection

### 🔧 Technical Features
- Powered by Groq's fast inference API
- Real-time chat with AI agents
- Template management system
- Persistent conversation history
- Error handling and loading states

## 📋 Prerequisites

- Node.js (v16 or higher)
- npm or yarn
- Python 3.8 or higher
- Groq API key (sign up at https://console.groq.com)

## 🛠️ Installation & Running

### Backend Setup

1. Clone the repository:
```bash
git clone https://github.com/OSOSerious/agent-template-groq-.git
cd agent-template-groq-
```

2. Create a backend .env file:
```bash
cat > .env << EOL
GROQ_API_KEY=your_groq_api_key_here
EOL
```

3. Install Python dependencies:
```bash
pip install -r requirements.txt
```

4. Start the backend server:
```bash
uvicorn main:app --reload --port 8000
```

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install Node dependencies:
```bash
npm install
```

3. Create a frontend .env file:
```bash
cat > .env << EOL
VITE_GROQ_API_KEY=your_groq_api_key_here
VITE_API_BASE_URL=http://localhost:8000
EOL
```

4. Start the frontend development server:
```bash
npm run dev
```

The application will be available at:
- Frontend: http://localhost:5173
- Backend API: http://localhost:8000
- API Documentation: http://localhost:8000/docs

## 🎯 Usage Guide

### Creating a Personal Agent
1. Visit the home page
2. Enter a name for your agent
3. Define your agent's goal (or select from examples)
4. Click "Deploy Agent" to start chatting

### Using Template Agents
1. Click "Templates" in the sidebar
2. Browse available specialized agents
3. Select a template to start chatting
4. Interact with the agent based on its specialization

### CLI Commands and Tools

#### Development Commands

Start the backend server with hot reload:
```bash
# Basic start
uvicorn main:app --reload --port 8000

# With specific host
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# With increased worker count
uvicorn main:app --reload --workers 4 --port 8000
```

Start the frontend development server:
```bash
# Basic start
npm run dev

# With specific host and port
npm run dev -- --host 0.0.0.0 --port 3000

# Production build
npm run build
```

#### Database Management
```bash
# Initialize the database
python scripts/init_db.py

# Reset the database
python scripts/reset_db.py
```

#### Template Management
```bash
# List all available templates
python scripts/list_templates.py

# Add a new template
python scripts/add_template.py --name "CustomAgent" --description "Your description" --prompt "Your system prompt"

# Remove a template
python scripts/remove_template.py --name "CustomAgent"
```

#### Testing Commands
```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_groq_interface.py

# Run tests with coverage
pytest --cov=src tests/
```

#### API Usage Examples

Test the chat endpoint:
```bash
# Send a message to the research agent
curl -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{
    "template": "research",
    "message": "Tell me about AI",
    "systemPrompt": null
  }'

# Send a message to a custom agent
curl -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{
    "template": "custom",
    "message": "Hello",
    "systemPrompt": "You are a helpful assistant"
  }'
```

Check server status:
```bash
# Health check
curl http://localhost:8000/health

# Version check
curl http://localhost:8000/version
```

List available templates:
```bash
curl http://localhost:8000/api/templates
```

#### Environment Management
```bash
# Create a new virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Unix or MacOS:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Update dependencies
pip install -r requirements.txt --upgrade
```

#### Docker Commands
```bash
# Build the container
docker build -t agent-template-groq .

# Run the container
docker run -p 8000:8000 -e GROQ_API_KEY=your_key_here agent-template-groq

# Run with volume mount for development
docker run -p 8000:8000 -v $(pwd):/app agent-template-groq

# Docker Compose
docker-compose up --build
```

#### Troubleshooting Commands
```bash
# Check logs
tail -f logs/app.log

# Check running processes
ps aux | grep "uvicorn"

# Kill a specific port
lsof -i :8000
kill -9 <PID>
```

### CLI Usage Examples

Terminal 1 (Backend):
```bash
cd agent-template-groq-
uvicorn main:app --reload --port 8000
```

Terminal 2 (Frontend):
```bash
cd agent-template-groq-/frontend
npm run dev
```

### API Examples

Test the API directly:

1. Send a chat message:
```bash
curl -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"template": "research", "message": "Tell me about AI", "systemPrompt": null}'
```

2. Check API status:
```bash
curl http://localhost:8000/health
```

## 🏗️ Project Structure

```
.
├── frontend/
│   ├── src/
│   │   ├── components/     # Reusable UI components
│   │   │   ├── NewAgent.svelte    # Personal agent creation
│   │   │   ├── Chat.svelte        # Chat interface
│   │   │   └── TemplateGrid.svelte # Template selection
│   │   ├── lib/           # Utility functions and API calls
│   │   ├── stores/        # Svelte stores for state management
│   │   └── types.ts       # TypeScript type definitions
│   ├── public/           # Static assets
│   └── index.html        # Entry point
├── src/
│   ├── templates/        # Agent template definitions
│   └── api/             # API implementations
├── main.py             # FastAPI backend entry point
└── requirements.txt    # Python dependencies
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
