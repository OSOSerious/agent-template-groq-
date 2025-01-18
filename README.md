

# AgentGPT with Groq Integration

A modern AI chatbot platform powered by Groq's API, featuring specialized agents for various tasks including research, travel planning, studying, and game design.

## 🚀 Features

- 🤖 Multiple Specialized Agents
  - Research Assistant
  - Travel Planner
  - Study Buddy
  - Game Designer
  - And more!

- 💻 Modern Frontend Interface
  - Responsive design
  - Dark theme
  - Interactive chat interface
  - Template-based agent creation

- 🔧 Technical Features
  - Real-time chat with AI agents
  - Template management system
  - Persistent conversation history
  - Error handling and loading states

## 📋 Prerequisites

- Node.js (v16 or higher)
- npm or yarn
- Groq API key

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/OSOSerious/agent-template-groq-.git
   cd agent-template-groq-
   ```

2. Install dependencies:
   ```bash
   cd frontend
   npm install
   ```

3. Create a `.env` file in the root directory and add your Groq API key:
   ```
   GROQ_API_KEY=your_api_key_here
   ```

4. Start the development server:
   ```bash
   npm run dev
   ```

## 🎯 Usage

1. Navigate to the application in your browser
2. Choose a template from the available agents
3. Start chatting with your chosen AI agent
4. Use the sidebar to switch between different views and create new agents

## 🏗️ Project Structure

```
frontend/
├── src/
│   ├── components/     # Reusable UI components
│   ├── lib/           # Utility functions and API calls
│   ├── stores/        # Svelte stores for state management
│   └── types.ts       # TypeScript type definitions
├── public/            # Static assets
└── index.html         # Entry point
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Powered by Groq's API
- Built with Svelte and TailwindCSS
- Icons from Heroicons

