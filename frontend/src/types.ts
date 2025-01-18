export interface Template {
  id: string;
  name: string;
  description?: string;
}

export interface Message {
  role: 'user' | 'assistant';
  content: string;
  thoughts?: string[];
}
