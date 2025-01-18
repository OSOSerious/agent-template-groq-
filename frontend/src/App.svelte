<!-- App.svelte -->
<script lang="ts">
  import { onMount } from 'svelte';
  import Sidebar from './components/Sidebar.svelte';
  import Chat from './components/Chat.svelte';
  import NewAgent from './components/NewAgent.svelte';
  import Settings from './components/Settings.svelte';
  import Auth from './components/Auth.svelte';
  import TemplateGrid from './components/TemplateGrid.svelte';
  import { authStore } from './stores/authStore';
  import { chatStore } from './stores/chatStore';
  import { defaultTemplates } from './lib/defaultTemplates';
  import type { Template } from './types';

  let currentView = 'home';
  let isAuthenticated = false;
  let selectedTemplate: Template | null = null;
  let templates: Template[] = defaultTemplates;
  let isLoading = false;
  let error: string | null = null;

  // Subscribe to auth store
  authStore.subscribe(auth => {
    isAuthenticated = auth.isAuthenticated;
    if (isAuthenticated) {
      // Load user's chat sessions when authenticated
      chatStore.loadSessions();
    }
  });

  function handleViewChange(event: CustomEvent) {
    currentView = event.detail.view;
  }

  function handleTemplateSelect(event: CustomEvent<Template>) {
    selectedTemplate = event.detail;
    currentView = 'chat';
  }

  function handleNewAgent(event: CustomEvent) {
    const newAgent = event.detail;
    templates = [...templates, newAgent];
    currentView = 'templates';
  }
</script>

<main class="flex h-screen bg-gray-900 text-white">
  {#if !isAuthenticated}
    <Auth />
  {:else}
    <Sidebar on:viewChange={handleViewChange} />
    
    <div class="flex-1 overflow-hidden">
      {#if currentView === 'home' || currentView === 'templates'}
        <div class="h-full p-8">
          <h1 class="text-3xl font-bold mb-8">Choose Your AI Assistant</h1>
          <TemplateGrid 
            {templates} 
            on:select={handleTemplateSelect} 
          />
        </div>
      {:else if currentView === 'chat' && selectedTemplate}
        <Chat template={selectedTemplate} />
      {:else if currentView === 'new-agent'}
        <NewAgent on:create={handleNewAgent} />
      {:else if currentView === 'settings'}
        <Settings />
      {/if}
    </div>
  {/if}
</main>

<style>
  :global(body) {
    background-color: rgb(17, 24, 39);
  }
</style>
