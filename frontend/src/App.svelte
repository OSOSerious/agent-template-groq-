<!-- App.svelte -->
<script lang="ts">
  import { onMount } from 'svelte';
  import Sidebar from './components/Sidebar.svelte';
  import TemplateGrid from './components/TemplateGrid.svelte';
  import Chat from './components/Chat.svelte';
  import axios from 'axios';
  import type { Template, Message } from './types';

  let activeView = 'home';
  let selectedTemplate: Template | null = null;
  let messages: Array<{role: string, content: string, thoughts?: string[]}> = [];
  let userMessage: string = '';
  let isLoading: boolean = false;
  let error: string | null = null;

  const API_URL = 'http://localhost:8000';

  onMount(async () => {
    try {
      const response = await axios.get(`${API_URL}/templates`);
      // templates = response.data;
    } catch (err) {
      error = 'Failed to load templates';
      console.error(err);
    }
  });

  function handleNavigate(event: CustomEvent) {
    activeView = event.detail.view;
    selectedTemplate = null;
  }

  function handleTemplateSelect(event: CustomEvent<Template>) {
    selectedTemplate = event.detail;
    activeView = 'chat';
  }

  function handleBack() {
    selectedTemplate = null;
    activeView = 'templates';
    messages = [];
  }

  function handleNewAgent() {
    activeView = 'templates';
    selectedTemplate = null;
  }

  async function handleSubmit() {
    if (!selectedTemplate || !userMessage.trim()) {
      error = 'Please select a template and enter a message';
      return;
    }

    try {
      error = null;
      isLoading = true;
      
      // Add user message
      messages = [...messages, { role: 'user', content: userMessage }];
      
      // Get AI response
      const response = await axios.post(`${API_URL}/chat`, {
        template: selectedTemplate,
        message: userMessage
      });
      
      // Add AI response
      messages = [...messages, { 
        role: 'assistant', 
        content: response.data.response,
        thoughts: response.data.thoughts || []
      }];
      
      // Clear input
      userMessage = '';
      
    } catch (err) {
      error = 'Failed to get response from AI';
      console.error(err);
    } finally {
      isLoading = false;
    }
  }
</script>

<div class="flex h-screen bg-gray-900 text-white">
  <Sidebar {activeView} on:navigate={handleNavigate} on:newAgent={handleNewAgent} />

  <main class="flex-1 ml-64">
    {#if !selectedTemplate}
      {#if activeView === 'templates'}
        <div class="p-4">
          <div class="flex items-center justify-between mb-6">
            <h1 class="text-2xl font-bold">Templates</h1>
            <a
              href="#"
              class="text-blue-400 hover:text-blue-300 flex items-center space-x-1"
            >
              <span>Interested in AI Agents to scrape web data?</span>
              <span>Find out more here →</span>
            </a>
          </div>
          <TemplateGrid on:select={handleTemplateSelect} />
        </div>
      {:else if activeView === 'home'}
        <div class="flex flex-col items-center justify-center h-full text-center p-4">
          <h1 class="text-4xl font-bold mb-4">AgentGPT</h1>
          <p class="text-gray-400 mb-8">Create and manage your AI agents</p>
          <div class="max-w-xl">
            <p class="text-gray-300 mb-4">👋 Welcome! I can help you create custom agents for any task.</p>
            <p class="text-gray-400">Browse our templates or create a new agent to get started.</p>
          </div>
        </div>
      {/if}
    {:else}
      <Chat
        {selectedTemplate}
        {messages}
        {userMessage}
        {isLoading}
        {error}
        on:back={handleBack}
        on:submit={handleSubmit}
      />
    {/if}
  </main>
</div>

<style>
  :global(body) {
    @apply bg-gray-900;
    margin: 0;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen,
      Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  }
</style>
