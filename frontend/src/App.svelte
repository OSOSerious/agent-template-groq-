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
      <div class="min-h-screen p-6 bg-gradient-to-b from-gray-900 via-gray-800 to-gray-900">
        <div class="max-w-6xl mx-auto">
          <!-- Hero Section -->
          <div class="text-center py-16 space-y-6">
            <h1 class="text-6xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-blue-400 via-purple-500 to-pink-500 animate-gradient">
              Welcome to AgentGPT
            </h1>
            <p class="text-xl text-gray-400 max-w-2xl mx-auto">
              Your AI assistant platform powered by Groq, bringing intelligent automation to your fingertips
            </p>
            <div class="flex justify-center gap-4 pt-4">
              <button
                on:click={() => currentView = 'templates'}
                class="px-6 py-3 bg-gradient-to-r from-blue-500 to-purple-600 rounded-lg text-white font-semibold hover:from-blue-600 hover:to-purple-700 transform hover:scale-105 transition-all shadow-lg flex items-center gap-2"
              >
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clip-rule="evenodd" />
                </svg>
                Get Started
              </button>
              <button
                on:click={() => currentView = 'newagent'}
                class="px-6 py-3 bg-gray-800 border border-gray-700 rounded-lg text-white font-semibold hover:bg-gray-700 transform hover:scale-105 transition-all shadow-lg flex items-center gap-2"
              >
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd" d="M10 3a1 1 0 011 1v5h5a1 1 0 110 2h-5v5a1 1 0 11-2 0v-5H4a1 1 0 110-2h5V4a1 1 0 011-1z" clip-rule="evenodd" />
                </svg>
                Create Agent
              </button>
            </div>
          </div>

          <!-- Features Grid -->
          <div class="grid grid-cols-1 md:grid-cols-3 gap-8 py-12">
            <!-- Get Started Card -->
            <div class="group bg-gray-800/50 backdrop-blur-sm p-8 rounded-2xl border border-gray-700/50 hover:border-blue-500/50 transition-all shadow-xl hover:shadow-blue-500/10">
              <div class="w-12 h-12 bg-gradient-to-br from-blue-500 to-purple-600 rounded-lg flex items-center justify-center mb-6 group-hover:scale-110 transition-transform">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-white" viewBox="0 0 20 20" fill="currentColor">
                  <path d="M10.394 2.08a1 1 0 00-.788 0l-7 3a1 1 0 000 1.84L5.25 8.051a.999.999 0 01.356-.257l4-1.714a1 1 0 11.788 1.838L7.667 9.088l1.94.831a1 1 0 00.787 0l7-3a1 1 0 000-1.838l-7-3zM3.31 9.397L5 10.12v4.102a8.969 8.969 0 00-1.05-.174 1 1 0 01-.89-.89 11.115 11.115 0 01.25-3.762zM9.3 16.573A9.026 9.026 0 007 14.935v-3.957l1.818.78a3 3 0 002.364 0l5.508-2.361a11.026 11.026 0 01.25 3.762 1 1 0 01-.89.89 8.968 8.968 0 00-5.35 2.524 1 1 0 01-1.4 0zM6 18a1 1 0 001-1v-2.065a8.935 8.935 0 00-2-.712V17a1 1 0 001 1z" />
                </svg>
              </div>
              <h2 class="text-xl font-bold text-white mb-4 group-hover:text-blue-400 transition-colors">🚀 Get Started</h2>
              <p class="text-gray-400 leading-relaxed">
                Choose from our collection of specialized AI agents, each designed for specific tasks and workflows.
              </p>
              <button
                on:click={() => currentView = 'templates'}
                class="mt-6 text-blue-400 hover:text-blue-300 flex items-center gap-2 group-hover:gap-3 transition-all"
              >
                Browse Templates
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clip-rule="evenodd" />
                </svg>
              </button>
            </div>

            <!-- Custom Agents Card -->
            <div class="group bg-gray-800/50 backdrop-blur-sm p-8 rounded-2xl border border-gray-700/50 hover:border-purple-500/50 transition-all shadow-xl hover:shadow-purple-500/10">
              <div class="w-12 h-12 bg-gradient-to-br from-purple-500 to-pink-600 rounded-lg flex items-center justify-center mb-6 group-hover:scale-110 transition-transform">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-white" viewBox="0 0 20 20" fill="currentColor">
                  <path d="M13 6a3 3 0 11-6 0 3 3 0 016 0zM18 8a2 2 0 11-4 0 2 2 0 014 0zM14 15a4 4 0 00-8 0v3h8v-3zM6 8a2 2 0 11-4 0 2 2 0 014 0zM16 18v-3a5.972 5.972 0 00-.75-2.906A3.005 3.005 0 0119 15v3h-3zM4.75 12.094A5.973 5.973 0 004 15v3H1v-3a3 3 0 013.75-2.906z" />
                </svg>
              </div>
              <h2 class="text-xl font-bold text-white mb-4 group-hover:text-purple-400 transition-colors">🎯 Custom Agents</h2>
              <p class="text-gray-400 leading-relaxed">
                Create your own AI agents with custom capabilities, tailored to your specific needs and preferences.
              </p>
              <button
                on:click={() => currentView = 'newagent'}
                class="mt-6 text-purple-400 hover:text-purple-300 flex items-center gap-2 group-hover:gap-3 transition-all"
              >
                Create Agent
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clip-rule="evenodd" />
                </svg>
              </button>
            </div>

            <!-- Smart Features Card -->
            <div class="group bg-gray-800/50 backdrop-blur-sm p-8 rounded-2xl border border-gray-700/50 hover:border-green-500/50 transition-all shadow-xl hover:shadow-green-500/10">
              <div class="w-12 h-12 bg-gradient-to-br from-green-500 to-emerald-600 rounded-lg flex items-center justify-center mb-6 group-hover:scale-110 transition-transform">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-white" viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd" d="M11.3 1.046A1 1 0 0112 2v5h4a1 1 0 01.82 1.573l-7 10A1 1 0 018 18v-5H4a1 1 0 01-.82-1.573l7-10a1 1 0 011.12-.38z" clip-rule="evenodd" />
                </svg>
              </div>
              <h2 class="text-xl font-bold text-white mb-4 group-hover:text-green-400 transition-colors">💡 Smart Features</h2>
              <p class="text-gray-400 leading-relaxed">
                Powered by advanced AI models and VSM architecture, delivering intelligent and context-aware responses.
              </p>
              <button
                on:click={() => currentView = 'settings'}
                class="mt-6 text-green-400 hover:text-green-300 flex items-center gap-2 group-hover:gap-3 transition-all"
              >
                View Settings
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clip-rule="evenodd" />
                </svg>
              </button>
            </div>
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

  @keyframes gradient {
    0% {
      background-position: 0% 50%;
    }
    50% {
      background-position: 100% 50%;
    }
    100% {
      background-position: 0% 50%;
    }
  }

  .animate-gradient {
    background-size: 200% 200%;
    animation: gradient 8s ease infinite;
  }
</style>
