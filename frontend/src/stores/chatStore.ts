import { writable, get } from 'svelte/store';
import { authStore } from './authStore';
import { API_ENDPOINTS } from '../config';

interface ChatMessage {
    id: string;
    role: 'user' | 'assistant';
    content: string;
    thoughts?: string[];
    created_at: string;
}

interface ChatSession {
    id: string;
    agent_id: string;
    agent_name: string;
    created_at: string;
    last_message_at: string;
    messages: ChatMessage[];
}

interface ChatStore {
    sessions: ChatSession[];
    error: string | null;
}

function createChatStore() {
    const { subscribe, set, update } = writable<ChatStore>({
        sessions: [],
        error: null
    });

    return {
        subscribe,
        addMessage: async (sessionId: string, content: string) => {
            try {
                const authState = get(authStore);
                if (!authState.token) {
                    throw new Error('Not authenticated');
                }

                const response = await fetch(API_ENDPOINTS.CHAT_MESSAGE, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${authState.token}`
                    },
                    body: JSON.stringify({
                        session_id: sessionId,
                        message: content
                    })
                });

                if (!response.ok) {
                    throw new Error(`Failed to send message: ${response.statusText}`);
                }

                const data = await response.json();
                update(store => {
                    const session = store.sessions.find(s => s.id === sessionId);
                    if (session) {
                        session.messages.push({
                            id: Date.now().toString(),
                            role: 'assistant',
                            content: data.response,
                            created_at: new Date().toISOString()
                        });
                    }
                    return store;
                });
            } catch (error) {
                console.error('Error sending message:', error);
                update(store => ({ ...store, error: error.message }));
                throw error;
            }
        },
        loadSessions: async () => {
            try {
                const response = await fetch(API_ENDPOINTS.CHAT_SESSIONS);
                
                if (!response.ok) {
                    throw new Error(`Failed to load sessions: ${response.statusText}`);
                }
                
                const sessions = await response.json();
                update(store => ({ ...store, sessions, error: null }));
            } catch (error) {
                console.error('Error loading sessions:', error);
                update(store => ({ ...store, error: error.message }));
                throw error;
            }
        },
        clearError: () => {
            update(store => ({ ...store, error: null }));
        }
    };
}

export const chatStore = createChatStore();
