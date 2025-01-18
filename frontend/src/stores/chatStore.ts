import { writable } from 'svelte/store';

export interface ChatMessage {
  role: string;
  content: string;
  timestamp?: Date;
}

export interface ChatSession {
  id: string;
  agentName: string;
  messages: ChatMessage[];
  lastUpdated: Date;
}

function createChatStore() {
  const { subscribe, set, update } = writable<ChatSession[]>([]);

  return {
    subscribe,
    addSession: (session: ChatSession) => update(sessions => [...sessions, session]),
    updateSession: (sessionId: string, messages: ChatMessage[]) =>
      update(sessions => sessions.map(s => 
        s.id === sessionId 
          ? { ...s, messages, lastUpdated: new Date() }
          : s
      )),
    deleteSession: (sessionId: string) =>
      update(sessions => sessions.filter(s => s.id !== sessionId)),
    clear: () => set([])
  };
}

export const chatStore = createChatStore();
