<!-- Chat.svelte -->
<script lang="ts">
  import { createEventDispatcher } from 'svelte';
  import type { Template } from '../types';

  const dispatch = createEventDispatcher();

  export let selectedTemplate: Template;
  export let messages: Array<{role: string, content: string, thoughts?: string[]}> = [];

  let userInput = '';
  let isLoading = false;
  let error: string | null = null;

  async function handleSubmit() {
    if (!userInput.trim()) return;

    try {
      isLoading = true;
      error = null;

      // Add user message
      messages = [...messages, { role: 'user', content: userInput }];

      // Make API call
      const response = await fetch('http://localhost:8000/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          template: selectedTemplate.id,
          message: userInput
        }),
      });

      if (!response.ok) {
        throw new Error('Failed to get response');
      }

      const data = await response.json();

      // Add AI response
      messages = [...messages, {
        role: 'assistant',
        content: data.response,
        thoughts: data.thoughts || []
      }];

      // Clear input
      userInput = '';

    } catch (err) {
      error = 'Failed to get response from AI';
      console.error(err);
    } finally {
      isLoading = false;
    }
  }

  function handleBack() {
    dispatch('back');
  }
</script>

<div class="flex flex-col h-screen bg-gray-900">
  <!-- Header -->
  <header class="flex items-center justify-between p-4 border-b border-gray-800">
    <div class="flex items-center space-x-4">
      <button
        on:click={handleBack}
        class="p-2 hover:bg-gray-800 rounded-full"
      >
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
        </svg>
      </button>
      <div>
        <h2 class="text-xl font-bold flex items-center space-x-2">
          <span>{selectedTemplate.icon}</span>
          <span>{selectedTemplate.name}</span>
        </h2>
        <p class="text-sm text-gray-400">{selectedTemplate.description}</p>
      </div>
    </div>
    <div class="flex items-center space-x-2">
      <button class="p-2 hover:bg-gray-800 rounded-full">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
        </svg>
      </button>
      <button class="p-2 hover:bg-gray-800 rounded-full">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 12h.01M12 12h.01M19 12h.01M6 12a1 1 0 11-2 0 1 1 0 012 0zm7 0a1 1 0 11-2 0 1 1 0 012 0zm7 0a1 1 0 11-2 0 1 1 0 012 0z" />
        </svg>
      </button>
    </div>
  </header>

  <!-- Chat Messages -->
  <div class="flex-1 overflow-y-auto p-4 space-y-4">
    {#if messages.length === 0}
      <div class="text-center text-gray-500 mt-8">
        <p class="text-lg mb-2">👋 Hi! I'm your AI assistant.</p>
        <p>I can help you {selectedTemplate.description.toLowerCase()}</p>
        <p class="text-sm mt-2">Try asking me something!</p>
      </div>
    {/if}

    {#each messages as message}
      <div class="flex flex-col {message.role === 'user' ? 'items-end' : 'items-start'}">
        <div class="max-w-3xl {message.role === 'user' ? 'bg-blue-600' : 'bg-gray-800'} rounded-lg p-4">
          <div class="flex items-center space-x-2 mb-2">
            <span class="text-lg">{message.role === 'user' ? '👤' : '🤖'}</span>
            <span class="font-semibold">{message.role === 'user' ? 'You' : selectedTemplate.name}</span>
          </div>
          <p class="whitespace-pre-wrap">{message.content}</p>
          {#if message.thoughts && message.thoughts.length > 0}
            <div class="mt-3 pt-3 border-t border-gray-700">
              <div class="text-sm text-gray-400">Thoughts:</div>
              <ul class="list-disc list-inside text-sm text-gray-300">
                {#each message.thoughts as thought}
                  <li>{thought}</li>
                {/each}
              </ul>
            </div>
          {/if}
        </div>
      </div>
    {/each}

    {#if isLoading}
      <div class="flex items-center space-x-2 text-gray-400">
        <div class="animate-bounce">⚪</div>
        <div class="animate-bounce delay-100">⚪</div>
        <div class="animate-bounce delay-200">⚪</div>
      </div>
    {/if}
  </div>

  <!-- Input Form -->
  <div class="border-t border-gray-800 p-4">
    {#if error}
      <div class="mb-4 p-3 bg-red-900/50 text-red-200 rounded-lg">
        {error}
      </div>
    {/if}
    
    <form on:submit|preventDefault={handleSubmit} class="flex space-x-4">
      <input
        type="text"
        bind:value={userInput}
        placeholder="Type your message..."
        class="flex-1 bg-gray-800 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
      />
      <button
        type="submit"
        disabled={isLoading || !userInput.trim()}
        class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed"
      >
        Send
      </button>
    </form>
  </div>
</div>
