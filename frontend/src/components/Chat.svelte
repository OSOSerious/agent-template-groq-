<!-- Chat.svelte -->
<script lang="ts">
  import { createEventDispatcher } from 'svelte';
  import type { Template } from '../types';
  import { v4 } from 'https://jspm.dev/uuid@8.3.2';

  const dispatch = createEventDispatcher();

  export let template: Template;
  export let messages: Array<{role: string, content: string, thoughts?: string[]}> = [];
  let userInput = '';
  let isLoading = false;
  let error: string | null = null;
  let sessionId = v4();

  async function handleSubmit(event: Event) {
    event.preventDefault();
    if (!userInput.trim()) return;

    try {
      isLoading = true;
      error = null;

      const newMessage = {
        role: 'user',
        content: userInput
      };

      messages = [...messages, newMessage];
      userInput = '';

      const response = await fetch('http://localhost:8000/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          messages,
          system_prompt: template.system_prompt
        }),
      });

      if (!response.ok) {
        throw new Error('Failed to send message');
      }

      const data = await response.json();
      messages = [...messages, data];
    } catch (err) {
      error = err instanceof Error ? err.message : 'Failed to send message';
    } finally {
      isLoading = false;
    }
  }

  function handleKeydown(event: KeyboardEvent) {
    if (event.key === 'Enter' && !event.shiftKey) {
      event.preventDefault();
      handleSubmit(event);
    }
  }
</script>

<div class="flex flex-col h-full bg-gray-900">
  <header class="bg-gray-800/50 backdrop-blur-sm p-4 flex items-center justify-between border-b border-gray-700/50">
    <div class="flex items-center gap-3">
      <div class="w-10 h-10 rounded-lg bg-gradient-to-br from-blue-500 to-purple-600 flex items-center justify-center text-2xl shadow-lg">
        {template.icon}
      </div>
      <div>
        <h2 class="font-bold text-lg text-white">{template.name}</h2>
        <p class="text-sm text-gray-400">{template.description}</p>
      </div>
    </div>
  </header>

  <div class="flex-1 overflow-y-auto p-4 space-y-4">
    {#if messages.length === 0}
      <div class="flex items-center justify-center h-full text-gray-500">
        <div class="text-center">
          <div class="text-4xl mb-2">{template.icon}</div>
          <p>Start chatting with {template.name}</p>
        </div>
      </div>
    {/if}
    
    {#each messages as message}
      <div class="flex gap-3 {message.role === 'assistant' ? 'flex-row' : 'flex-row-reverse'}">
        <div class="w-8 h-8 rounded-lg flex items-center justify-center bg-gradient-to-br {message.role === 'assistant' ? 'from-blue-500 to-purple-600' : 'from-green-500 to-emerald-600'}">
          {message.role === 'assistant' ? template.icon : '👤'}
        </div>
        <div
          class="max-w-[80%] rounded-lg p-4 shadow-lg {message.role === 'assistant' ? 'bg-gray-800/50 backdrop-blur-sm' : 'bg-blue-600/50 backdrop-blur-sm ml-auto'}"
        >
          <p class="text-white whitespace-pre-wrap">{message.content}</p>
          {#if message.thoughts}
            <div class="mt-3 pt-3 border-t border-gray-700/50">
              <p class="text-sm font-medium text-gray-400 mb-2">Thoughts:</p>
              <ul class="space-y-1">
                {#each message.thoughts as thought}
                  <li class="flex items-start gap-2 text-sm text-gray-400">
                    <span class="mt-1">💭</span>
                    <span>{thought}</span>
                  </li>
                {/each}
              </ul>
            </div>
          {/if}
        </div>
      </div>
    {/each}

    {#if isLoading}
      <div class="flex gap-3">
        <div class="w-8 h-8 rounded-lg flex items-center justify-center bg-gradient-to-br from-blue-500 to-purple-600">
          {template.icon}
        </div>
        <div class="bg-gray-800/50 backdrop-blur-sm rounded-lg p-4 shadow-lg">
          <div class="flex space-x-2">
            <div class="w-2 h-2 bg-blue-500 rounded-full animate-bounce"></div>
            <div class="w-2 h-2 bg-blue-500 rounded-full animate-bounce" style="animation-delay: 0.2s"></div>
            <div class="w-2 h-2 bg-blue-500 rounded-full animate-bounce" style="animation-delay: 0.4s"></div>
          </div>
        </div>
      </div>
    {/if}
  </div>

  <form
    on:submit={handleSubmit}
    class="border-t border-gray-700/50 p-4 bg-gray-800/50 backdrop-blur-sm"
  >
    {#if error}
      <div class="mb-4 p-3 bg-red-500/10 border border-red-500/20 rounded-lg text-red-400">
        <div class="flex items-center gap-2">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
            <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd" />
          </svg>
          {error}
        </div>
      </div>
    {/if}
    
    <div class="flex gap-2">
      <input
        type="text"
        bind:value={userInput}
        on:keydown={handleKeydown}
        placeholder="Type your message..."
        class="flex-1 bg-gray-900/50 border border-gray-700/50 rounded-lg px-4 py-3 text-white placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-blue-500/50 focus:border-transparent transition-shadow"
      />
      <button
        type="submit"
        disabled={isLoading || !userInput.trim()}
        class="bg-gradient-to-r from-blue-500 to-blue-600 text-white px-6 py-3 rounded-lg hover:from-blue-600 hover:to-blue-700 disabled:opacity-50 disabled:cursor-not-allowed shadow-lg transition-all flex items-center gap-2"
      >
        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
          <path d="M10.894 2.553a1 1 0 00-1.788 0l-7 14a1 1 0 001.169 1.409l5-1.429A1 1 0 009 15.571V11a1 1 0 112 0v4.571a1 1 0 00.725.962l5 1.428a1 1 0 001.17-1.408l-7-14z" />
        </svg>
      </button>
    </div>
  </form>
</div>

<style>
  /* Hide scrollbar for Chrome, Safari and Opera */
  .overflow-y-auto::-webkit-scrollbar {
    display: none;
  }

  /* Hide scrollbar for IE, Edge and Firefox */
  .overflow-y-auto {
    -ms-overflow-style: none;  /* IE and Edge */
    scrollbar-width: none;  /* Firefox */
  }
</style>
