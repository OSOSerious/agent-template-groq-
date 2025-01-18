<!-- App.svelte -->
<script lang="ts">
  import { onMount } from 'svelte';
  import Sidebar from './components/Sidebar.svelte';
  import Chat from './components/Chat.svelte';
  import TemplateGrid from './components/TemplateGrid.svelte';
  import Settings from './components/Settings.svelte';
  import NewAgent from './components/NewAgent.svelte';
  import { chatStore } from './stores/chatStore';
  import type { Template } from './types';

  let currentView = 'templates';
  let selectedTemplate: Template | null = null;
  let templates: Template[] = [];

  onMount(async () => {
    try {
      const response = await fetch('http://localhost:8000/templates');
      templates = await response.json();
    } catch (error) {
      console.error('Failed to load templates:', error);
    }
  });

  function handleViewChange(event: CustomEvent) {
    currentView = event.detail.view;
  }

  function handleTemplateSelect(event: CustomEvent) {
    selectedTemplate = event.detail.template;
    currentView = 'chat';
  }

  function handleNewAgent(event: CustomEvent) {
    const newAgent = event.detail;
    templates = [...templates, newAgent];
    currentView = 'templates';
  }
</script>

<div class="flex h-screen bg-gray-900 text-white">
  <Sidebar on:viewChange={handleViewChange} />
  
  <main class="flex-1 overflow-hidden">
    {#if currentView === 'templates'}
      <TemplateGrid {templates} on:select={handleTemplateSelect} />
    {:else if currentView === 'chat' && selectedTemplate}
      <Chat template={selectedTemplate} />
    {:else if currentView === 'settings'}
      <Settings />
    {:else if currentView === 'newagent'}
      <NewAgent on:create={handleNewAgent} />
    {:else if currentView === 'home'}
      <div class="p-6">
        <h1 class="text-4xl font-bold mb-4">Welcome to AgentGPT</h1>
        <p class="text-gray-400 mb-8">Your AI assistant platform powered by Groq</p>
        
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <div class="bg-gray-800 p-6 rounded-lg">
            <h2 class="text-xl font-bold mb-2">🚀 Get Started</h2>
            <p class="text-gray-400">Choose from our collection of specialized AI agents</p>
          </div>
          
          <div class="bg-gray-800 p-6 rounded-lg">
            <h2 class="text-xl font-bold mb-2">🎯 Custom Agents</h2>
            <p class="text-gray-400">Create your own AI agents with custom capabilities</p>
          </div>
          
          <div class="bg-gray-800 p-6 rounded-lg">
            <h2 class="text-xl font-bold mb-2">💡 Smart Features</h2>
            <p class="text-gray-400">Powered by advanced AI models and VSM architecture</p>
          </div>
        </div>
      </div>
    {/if}
  </main>
</div>

<style>
  :global(body) {
    margin: 0;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen-Sans, Ubuntu, Cantarell, 'Helvetica Neue', sans-serif;
  }
</style>
