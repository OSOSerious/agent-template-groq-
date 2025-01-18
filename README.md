<<<<<<< HEAD
# AgentGPT - AI Assistant Platform

A modern AI chatbot platform powered by Groq's API, featuring specialized agents for various tasks including research, travel planning, studying, and game design. Built with a VSM (Viable System Model) architecture for enhanced intelligence and adaptability.
=======
AI Assistant Platform
A modern AI chatbot platform powered by Groq's API, featuring specialized agents for various tasks including research, travel planning, studying, and game design.
>>>>>>> 1a38f8062d3a4e5bf43b3a4b18670557b5f33121

🚀 Features
🤖 Multiple Specialized Agents

<<<<<<< HEAD
### 🤖 Multiple Specialized Agents
- Research Assistant with VSM-based analysis
- Travel Planner with itinerary optimization
- Study Buddy for educational support
- Game Designer for creative development
- Custom agent creation capability

### 💻 Modern Frontend Interface
- Clean, responsive design with dark theme
- Interactive chat interface with real-time responses
- Template-based agent selection
- Customizable agent settings
- Chat history and session management

### 🔧 Technical Features
- Real-time chat with AI agents using Groq's API
- VSM-based template management system
- Persistent conversation history
- Comprehensive error handling
- Advanced state management with Svelte stores

## 📋 Prerequisites
- Node.js (v16 or higher)
- npm or yarn
- Groq API key
- Python 3.8+ (for backend)
=======
Research Assistant
Travel Planner
Study Buddy
Game Designer
And more!
💻 Modern Frontend Interface

Responsive design
Dark theme
Interactive chat interface
Template-based agent creation
🔧 Technical Features

Real-time chat with AI agents
Template management system
Persistent conversation history
Error handling and loading states
📋 Prerequisites
Node.js (v16 or higher)
npm or yarn
Groq API key
🛠️ Installation
Clone the repository:

git clone https://github.com/OSOSerious/agent-template-groq-.git
cd agent-template-groq-
Install dependencies:

cd frontend
npm install
Create a .env file in the root directory and add your Groq API key:
>>>>>>> 1a38f8062d3a4e5bf43b3a4b18670557b5f33121

GROQ_API_KEY=your_api_key_here
Start the development server:

<<<<<<< HEAD
1. Clone the repository:
```bash
git clone https://github.com/yourusername/AgentGPT.git
cd AgentGPT
```

2. Install frontend dependencies:
```bash
cd frontend
npm install
```

3. Install backend dependencies:
```bash
cd ../backend
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the backend directory:
```
GROQ_API_KEY=your_api_key_here
```

5. Start the development servers:

Backend:
```bash
cd backend
python main.py
```

Frontend:
```bash
cd frontend
npm run dev
```

## 🎯 Usage

1. Navigate to `http://localhost:5173` in your browser
2. Choose a template from the available agents
3. Start chatting with your chosen AI agent
4. Use the sidebar to:
   - Switch between different views
   - Access chat history
   - Create new agents
   - Adjust settings

## 🏗️ Project Structure

```
AgentGPT/
├── frontend/
│   ├── src/
│   │   ├── components/     # Reusable UI components
│   │   ├── stores/        # Svelte stores for state management
│   │   ├── lib/           # Utility functions and API calls
│   │   └── types.ts       # TypeScript type definitions
│   ├── public/            # Static assets
│   └── index.html         # Entry point
├── backend/
│   ├── main.py           # FastAPI server
│   ├── templates/        # Agent templates
│   └── requirements.txt  # Python dependencies
└── README.md
```

## 🔒 Security

- API keys are securely handled through environment variables
- CORS protection enabled
- Input validation and sanitization
- Error handling and logging

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.
=======
npm run dev
🎯 Usage
Navigate to the application in your browser
Choose a template from the available agents
Start chatting with your chosen AI agent
Use the sidebar to switch between different views and create new agents
🏗️ Project Structure
frontend/
├── src/
│   ├── components/     # Reusable UI components
│   ├── lib/           # Utility functions and API calls
│   ├── stores/        # Svelte stores for state management
│   └── types.ts       # TypeScript type definitions
├── public/            # Static assets
└── index.html         # Entry point
🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.
>>>>>>> 1a38f8062d3a4e5bf43b3a4b18670557b5f33121

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

<<<<<<< HEAD
## 🙏 Acknowledgments

- Powered by Groq's API
- Built with Svelte and FastAPI
- VSM architecture inspired by Stafford Beer's work
- UI components styled with TailwindCSS
=======
🙏 Acknowledgments
Powered by Groq's API
Built with Svelte and TailwindCSS
>>>>>>> 1a38f8062d3a4e5bf43b3a4b18670557b5f33121
