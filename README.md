# AI Assistant Platform

A modern AI chatbot platform powered by Groq's API, featuring specialized agents for various tasks including research, travel planning, studying, and game design.

## 🚀 Features

### 🤖 Multiple Specialized Agents

- Research Assistant
- Travel Planner
- Study Buddy
- Game Designer
- And more!

### 💻 Modern Frontend Interface

- Responsive design
- Dark theme
- Interactive chat interface
- Template-based agent creation

### 🔧 Technical Features

- Real-time chat with AI agents
- Template management system
- Persistent conversation history
- Error handling and loading states

## 📋 Prerequisites

- Node.js (v16 or higher)
- npm or yarn
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

## 🎯 CLI Usage Examples

### Starting Both Services

You can start both services in separate terminal windows:

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

### Using the API via curl

Test the API directly from the command line:

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
│   │   ├── lib/           # Utility functions and API calls
│   │   ├── stores/        # Svelte stores for state management
│   │   └── types.ts       # TypeScript type definitions
│   ├── public/           # Static assets
│   └── index.html        # Entry point
├── groq-agents/         # Agent templates
├── main.py             # FastAPI backend entry point
├── groq_interface.py   # Groq API integration
└── requirements.txt    # Python dependencies
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Powered by Groq's API
- Built with Svelte and TailwindCSS
