export interface Template {
  name: string;
  description: string;
  icon: string;
  system_prompt: string;
}

export interface Message {
  role: 'user' | 'assistant';
  content: string;
  thoughts?: string[];
}
