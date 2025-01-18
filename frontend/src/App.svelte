<!-- App.svelte -->
<script lang="ts">
  import { onMount } from 'svelte';
  import Sidebar from './components/Sidebar.svelte';
  import TemplateGrid from './components/TemplateGrid.svelte';
  import Chat from './components/Chat.svelte';
  import type { Template, Message } from './types';

  let activeView = 'home';
  let selectedTemplate: Template | null = null;
  let templates: Template[] = [];
  let messages: Array<{role: string, content: string, thoughts?: string[]}> = [];
  let isLoading = false;
  let error: string | null = null;

  onMount(async () => {
    try {
      const response = await fetch('http://localhost:8000/templates');
      if (!response.ok) {
        throw new Error('Failed to load templates');
      }
      templates = await response.json();
    } catch (err) {
      error = err instanceof Error ? err.message : 'Failed to load templates';
    }
  });

  function handleTemplateSelect(event: CustomEvent<{template: Template}>) {
    selectedTemplate = event.detail.template;
    activeView = 'chat';
    messages = [];
  }

  function handleBack() {
    activeView = 'home';
    selectedTemplate = null;
    messages = [];
  }
</script>

<div class="h-screen bg-gray-900 text-white">
  <div class="flex h-full">
    <Sidebar />
    
    <div class="flex-1 flex flex-col overflow-hidden">
      {#if activeView === 'home'}
        <div class="flex-1 overflow-y-auto">
          <div class="max-w-7xl mx-auto">
            <header class="px-4 py-6">
              <h1 class="text-2xl font-bold text-white">Templates</h1>
              <p class="mt-1 text-sm text-gray-400">
                Choose from our specialized AI agents to help with your task
              </p>
            </header>

            <TemplateGrid {templates} on:select={handleTemplateSelect} />
          </div>
        </div>
      {:else if activeView === 'chat' && selectedTemplate}
        <Chat
          template={selectedTemplate}
          messages={messages}
          on:back={handleBack}
        />
      {/if}
    </div>
  </div>
</div>

<style>
  :global(body) {
    margin: 0;
    background-color: #111827;
    color: white;
  }
</style>
