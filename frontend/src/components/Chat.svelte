<!-- Chat.svelte -->
<script lang="ts">
  import { onMount } from 'svelte';
  import type { Template } from '../types';
  import { groqClient } from '../lib/groq';
  import { DEFAULT_MODEL } from '../config';

  export let template: Template;

  interface ChatMessage {
    role: 'system' | 'user' | 'assistant';
    content: string;
  }

  let messages: ChatMessage[] = [];
  let inputMessage = '';
  let isLoading = false;
  let error: string | null = null;

  // Initialize chat with system prompt
  onMount(() => {
    if (template.system_prompt) {
      messages = [{
        role: 'system',
        content: template.system_prompt
      }];
    }
  });

  async function handleSubmit(event: Event) {
    event.preventDefault();
    if (!inputMessage.trim()) return;

    const userMessage: ChatMessage = {
      role: 'user',
      content: inputMessage
    };

    messages = [...messages, userMessage];
    const currentInput = inputMessage;
    inputMessage = '';
    isLoading = true;
    error = null;

    try {
      const response = await groqClient.chat(messages, DEFAULT_MODEL);
      messages = [...messages, response as ChatMessage];
    } catch (err) {
      const errorMessage = err instanceof Error ? err.message : 'An unknown error occurred';
      error = errorMessage;
      console.error('Chat error:', err);
    } finally {
      isLoading = false;
    }
  }
</script>

<div class="flex flex-col h-full">
  <div class="flex-1 overflow-y-auto p-4 space-y-4">
    {#each messages.filter(m => m.role !== 'system') as message}
      <div class="flex gap-2 {message.role === 'assistant' ? 'flex-row' : 'flex-row-reverse'}">
        <div class="w-8 h-8 rounded-full bg-gradient-to-br flex items-center justify-center text-sm">
          {message.role === 'assistant' ? template.icon : '👤'}
        </div>
        <div class="flex-1 bg-gray-800/50 backdrop-blur-sm p-4 rounded-lg max-w-[80%]">
          <p class="text-sm whitespace-pre-wrap">{message.content}</p>
        </div>
      </div>
    {/each}
    
    {#if isLoading}
      <div class="flex items-center justify-center py-4">
        <div class="animate-spin rounded-full h-8 w-8 border-b-2 border-white"></div>
      </div>
    {/if}
    
    {#if error}
      <div class="bg-red-500/20 border border-red-500/50 p-4 rounded-lg text-red-200">
        {error}
      </div>
    {/if}
  </div>

  <form 
    on:submit={handleSubmit}
    class="border-t border-gray-700/50 p-4 bg-gray-800/30 backdrop-blur-sm"
  >
    <div class="flex gap-2">
      <input
        type="text"
        bind:value={inputMessage}
        placeholder="Type your message..."
        class="flex-1 bg-gray-700/50 border border-gray-600/50 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
      />
      <button
        type="submit"
        disabled={isLoading}
        class="px-4 py-2 bg-blue-600 hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed rounded-lg transition-colors"
      >
        Send
      </button>
    </div>
  </form>
</div>
