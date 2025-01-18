<!-- Chat.svelte -->
<script lang="ts">
  import { createEventDispatcher } from 'svelte';
  import type { Template } from '../types';

  const dispatch = createEventDispatcher();

  export let template: Template;
  export let messages: Array<{role: string, content: string, thoughts?: string[]}> = [];

  let userInput = '';
  let isLoading = false;
  let error: string | null = null;

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

  function handleBack() {
    dispatch('back');
  }
</script>

<div class="flex flex-col h-full">
  <!-- Header -->
  <div class="flex items-center p-4 border-b border-gray-200 dark:border-gray-700">
    <button
      class="mr-4 text-gray-500 hover:text-gray-700 dark:text-gray-400 dark:hover:text-gray-300"
      on:click={handleBack}
    >
      ←
    </button>
    <div class="flex items-center">
      <span class="text-2xl mr-2">{template.icon}</span>
      <div>
        <h2 class="font-semibold text-gray-900 dark:text-white">
          {template.name}
        </h2>
        <p class="text-sm text-gray-500 dark:text-gray-400">
          {template.description}
        </p>
      </div>
    </div>
  </div>

  <!-- Messages -->
  <div class="flex-1 overflow-y-auto p-4 space-y-4">
    {#each messages as message}
      <div class="flex gap-3 {message.role === 'assistant' ? 'flex-row' : 'flex-row-reverse'}">
        <div class="w-10 h-10 rounded-full flex items-center justify-center bg-gray-200 dark:bg-gray-700">
          {message.role === 'assistant' ? template.icon : '👤'}
        </div>
        <div class="flex-1">
          <div class="bg-white dark:bg-gray-800 rounded-lg p-4 shadow">
            <p class="text-gray-900 dark:text-white whitespace-pre-wrap">
              {message.content}
            </p>
          </div>
          {#if message.thoughts}
            <div class="mt-2 text-sm text-gray-500 dark:text-gray-400">
              {#each message.thoughts as thought}
                <p>💭 {thought}</p>
              {/each}
            </div>
          {/if}
        </div>
      </div>
    {/each}
    {#if isLoading}
      <div class="flex gap-3">
        <div class="w-10 h-10 rounded-full flex items-center justify-center bg-gray-200 dark:bg-gray-700">
          {template.icon}
        </div>
        <div class="flex-1">
          <div class="bg-white dark:bg-gray-800 rounded-lg p-4 shadow">
            <p class="text-gray-500 dark:text-gray-400">Thinking...</p>
          </div>
        </div>
      </div>
    {/if}
  </div>

  <!-- Input -->
  <form
    class="p-4 border-t border-gray-200 dark:border-gray-700"
    on:submit={handleSubmit}
  >
    {#if error}
      <div class="mb-4 p-4 bg-red-100 dark:bg-red-900 text-red-700 dark:text-red-100 rounded">
        {error}
      </div>
    {/if}
    <div class="flex gap-4">
      <input
        type="text"
        bind:value={userInput}
        placeholder="Type your message..."
        class="flex-1 p-2 rounded border border-gray-300 dark:border-gray-600 dark:bg-gray-700 dark:text-white"
        disabled={isLoading}
      />
      <button
        type="submit"
        class="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 disabled:opacity-50"
        disabled={isLoading || !userInput.trim()}
      >
        Send
      </button>
    </div>
  </form>
</div>

<style>
  /* Add any custom styles here */
</style>
