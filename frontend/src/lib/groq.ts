import { GROQ_API_KEY } from '../config';

export const GROQ_BASE_URL = 'https://api.groq.com/openai/v1';

export const groqClient = {
  async chat(messages: any[], model: string = 'llama-3.3-70b-versatile') {
    try {
      const response = await fetch(`${GROQ_BASE_URL}/chat/completions`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${GROQ_API_KEY}`,
        },
        body: JSON.stringify({
          model,
          messages,
          temperature: 0.7,
          max_completion_tokens: 1024,
          stream: false,
        }),
      });

      if (!response.ok) {
        throw new Error(`Groq API error: ${response.statusText}`);
      }

      const data = await response.json();
      return data.choices[0].message;
    } catch (error) {
      console.error('Error calling Groq API:', error);
      throw error;
    }
  },
};
