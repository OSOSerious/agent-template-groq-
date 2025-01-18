export const API_BASE_URL = 'http://localhost:8002';

export const API_ENDPOINTS = {
    CHAT_MESSAGE: `${API_BASE_URL}/chat/message`,
    CHAT_SESSIONS: `${API_BASE_URL}/chat/sessions`,
    TEMPLATES: `${API_BASE_URL}/templates`,
};

export const GROQ_API_KEY = import.meta.env.VITE_GROQ_API_KEY || '';

// Default Groq model to use
export const DEFAULT_MODEL = 'llama-3.3-70b-versatile';

// Available Groq models
export const GROQ_MODELS = {
    LLAMA_70B: 'llama-3.3-70b-versatile',
    LLAMA_8B: 'llama-3.1-8b-instant',
    MIXTRAL: 'mixtral-8x7b-32768',
    GEMMA: 'gemma2-9b-it'
};
